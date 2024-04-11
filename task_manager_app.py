# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from task import Task
from users import User, Admin
from datetime import datetime
import json


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list=None):
        if users_list is None:
            users_list = []
        self._users_list = users_list
        self._tasks = []
        self._logged_in = False
        self._user = None

        self.load_admin_user()  # loading initial admin user data from the json file

    def load_admin_user(self):
        try:
            with open("users.json", "r") as file:
                users_data = json.load(file)
                for user_data in users_data:
                    if user_data.get("is_manager", False):
                        admin_user = Admin(
                            name=user_data["name"], password=user_data["password"]
                        )
                        self._users_list.append(admin_user)
                        # print("Admin user loaded successfully.")
                        return
            print("Admin user not found.")
        except FileNotFoundError:
            print("User data file not found.")

    def read_users_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                users_data = json.load(file)
                self._users_list = []
                for user_data in users_data:
                    if user_data.get("is_manager", False):
                        user = Admin(user_data["name"], user_data["password"])
                    else:
                        user = User(user_data["name"], user_data["password"])
                    user.user_id = user_data["user_id"]  # Set the user_id attribute
                    self._users_list.append(user)
            print("User data loaded successfully.")
        except FileNotFoundError:
            print("User data file not found")

    def save_users_to_json(self, filename):
        users_data = []
        for user in self._users_list:
            user_data = {
                "user_id": user.user_id,
                "name": user.name,
                "password": user.password,
                "is_manager": isinstance(user, Admin),
            }
            users_data.append(user_data)
        try:
            with open(filename, "w") as file:
                json.dump(users_data, file)
            print("Users saved successfully.")
        except IOError as e:
            print(f"Error saving user data to {filename}: {e}")

    def read_tasks_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self._tasks = []
                for task_data in tasks_data:
                    task = Task(
                        task_data["task_name"],
                        task_data["category"],
                        task_data["description"],
                        task_data["deadline"],
                    )
                    task._Task__task_id = task_data[
                        "task_id"
                    ]  # set task_id after creating the Task
                    self._tasks.append(task)
            print("Task data loaded successfully.")
        except FileNotFoundError:
            print("Task data file not found, creating a new empty file.")
            self.tasks_list = []
            self.save_tasks_to_json(filename)
        except (TypeError, ValueError) as e:
            print(f"Error loading task data from {filename}: {e}")

    def save_tasks_to_json(self, filename):
        tasks_data = [task.to_dict() for task in self._tasks]
        try:
            with open(filename, "w") as file:
                json.dump(tasks_data, file, default=str, indent=4)
            print("Tasks saved successfully.")
        except IOError as e:
            print(f"Error saving tasks to {filename}: {e}")

    def start_menu(self):
        print("\nCommands:")
        print("0 Exit")
        print("1 Log in")
        print("2 Register\n")

    # menu for regular users
    def user_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 View all users")
        print("3 All tasks")
        print("4 Own tasks")
        print("5 New task")
        print()

    # menu for admin users
    def admin_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 View all users")
        print("3 All tasks")
        print("4 Own tasks")
        print("5 New task")
        print("6 Assign task")
        print("7 Edit task status")
        print()

    def validate_registration_pw(self, password, min_length=3, require_uppercase=True):
        if len(password) < min_length:
            print(
                f"Password must be at least {min_length} characters long, please try again."
            )
            return False

        if require_uppercase and not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
            return False

        return True

    def register(self):
        username = input("Enter your username: ")
        password_validation = False

        while not password_validation:
            password = input("Enter your password: ")
            if self.validate_registration_pw(password):
                password_2 = input("Re-enter your password: ")
                if password == password_2:

                    new_user = User(username, password)
                    self._users_list.append(new_user)
                    print("\nUser created succesfully")
                    password_validation = True
                else:
                    print("\nPassword did not match, try again\n")
            else:
                print("\nPassword does not meet requirements, try again\n")
        self.save_users_to_json("users.json")

    def login(self):
        username = input('Enter your username ("exit" to exit): ')

        # makes it possible to close the program from the login
        if username == "exit":
            print("Closing the program")
            return "exit"

        try:
            with open("users.json", "r") as file:
                users_data = json.load(file)
        except FileNotFoundError:
            print("User data file not found.")
            return

        # if username found it's stored in possible_user which is used to check the password
        possible_user = next(
            (user for user in self._users_list if user.name == username), None
        )

        if possible_user is None:
            print("User not found\n")
            return self.login()

        password = input("Enter your password: ")

        # comparing password to the possible_user's password
        if password == possible_user.password:
            self._logged_in = True
            self._user = possible_user
            print(f"Logged in as: {self._user.name}\n")

        else:
            print("Wrong password\n")
            return self.login()

    def log_out(self):
        print("Logging out\n")
        self._logged_in = False

    # for user to see their own tasks
    def view_tasks(self):
        print()
        self._user.view_tasks()

    # to see all tasks
    def view_all_tasks(self):
        if self._tasks == []:
            print("\nNo tasks")
        else:
            print("\nAll tasks:")
            for task in self._tasks:
                print(task)

    # to see all users
    def view_users(self):
        print("\nAll users:")
        for user in self._users_list:
            print(user)

    def validate_deadline(self, deadline):
        try:
            datetime.strptime(deadline, "%d.%m.%Y")
            return True
        except ValueError:
            print("Invalid deadline format. Please use dd.mm.yyyy format.")
            return False

    # for user to add a task for themselves
    def add_task_user(self):
        task_name = input("\nName of task: ")
        category = input("Task category: ")
        description = input("Short description: ")
        deadline = input("Task deadline (dd.mm.yyyy): ")
        while not self.validate_deadline(deadline):
            deadline = input("Task deadline (dd.mm.yyyy): ")
        task = Task(task_name, category, description, deadline)
        task.assigned_to = self._user
        self._user.add_task(task)
        self._tasks.append(task)
        self.save_tasks_to_json("tasks.json")

    # for admin to add tasks
    def add_task(self):
        task_name = input("\nName of task: ")
        category = input("Task category: ")
        description = input("Short description: ")
        deadline = input("Task deadline (dd.mm.yyyy): ")
        while not self.validate_deadline(deadline):
            deadline = input("Task deadline (dd.mm.yyyy): ")
        task = Task(task_name, category, description, deadline)
        choice = input("Assign task to user (y/n): ")

        # possibility to assign a task to any user
        if choice == "y":
            print("\nList of all users:")
            self.view_users()
            #
            try:
                id = int(input("\nSelect a user by their ID: "))
            except ValueError:
                print("Invalid ID, task not assigned")
                self._tasks.append(task)
                return
            #
            user_found = False
            for user in self._users_list:
                if user.user_id == id:
                    task.assigned_to = user
                    user.add_task(task)
                    self._tasks.append(task)
                    print(f"\nTask assigned to {user.name}")
                    user_found = True
            if not user_found:
                print("\nUser not found, task not assigned")
                self._tasks.append(task)
        elif choice == "n":
            print("\nTask not assigned")
            self._tasks.append(task)

        else:
            print("\nInvalid input, task not assigned")
            self._tasks.append(task)

    def assign_task(self):

        while True:

            if self._tasks == []:
                print("No tasks to assign")
                return

            else:
                print("\nAll tasks:")
                self.view_all_tasks()

            try:
                task_id = int(input("\nSelect a task by its ID: "))
            except ValueError:
                print("Invalid ID, task not assigned")
                return

            task_found = False
            task_to_assign = None
            for task in self._tasks:
                if task.task_id == task_id:
                    task_to_assign = task
                    task_found = True
            if not task_found:
                print("Task not found")
                return

            print("\nList of all users:")
            self.view_users()

            try:
                user_id = int(input("\nSelect a user by their ID: "))
            except ValueError:
                print("Invalid ID, task not assigned")
                return

            user_found = False
            user_to_assign = None
            for user in self._users_list:
                if user.user_id == user_id:
                    user_to_assign = user
                    task_to_assign.assigned_to = user_to_assign
                    user.add_task(task_to_assign)
                    print(f"\nTask assigned to {user_to_assign.name}")
                    user_found = True
                    return
            if not user_found:
                print("\nUser not found, task not assigned")
                return

    # for admin to edit task status
    def edit_task_status(self):
        # self.view_all_tasks()
        if not self._tasks:
            print("\nNo tasks found")
            return

        while True:
            try:
                self.view_all_tasks()
                task_to_edit_id = int(input("\nEnter the task ID to edit: "))
                # checking task id
                task_to_edit = next(
                    (task for task in self._tasks if task.task_id == task_to_edit_id),
                    None,
                )
                if task_to_edit:
                    break  # exit loop if id is valid
                else:
                    print("\nNo task found with the given ID.")
                    retry = input(
                        "Do you want to try again? \n1 Yes \n2 Back to main menu\n"
                    )
                    if retry == "2":
                        return  # return to main menu
                    elif retry != "1":
                        print("\nInvalid option. Please try again.")
                        continue
            except ValueError:
                print("\nInvalid ID, please enter a valid task ID.")
                retry = input(
                    "\nDo you want to try again? \n1 Yes \n2 Back to main menu\n"
                )
                if retry == "2":
                    return  # return to the main menu
                elif retry != "1":
                    print("\nInvalid option. Please try again.")
                    continue

        while True:  # loop for checking the validity of the input task status
            new_status = input(
                "\nEnter the new status from the following: \nAssigned \nIn progress \nDone \nApproved\n"
            ).lower()
            if new_status in ["assigned", "in progress", "done", "approved"]:
                task_to_edit.status = new_status
                print("Task status updated successfully.")
                break  # end loop if it's valid
            else:
                print(
                    "\nInvalid status. Please choose from 'assigned', 'in progress', 'done', or 'approved'."
                )
                retry = input(
                    "Do you want to try again? \n1 Yes \n2 Back to main menu\n"
                )
                if retry == "2":
                    return  # Return to the main menu
                elif retry != "1":
                    print("Invalid option. Please try again.")
        self.save_tasks_to_json("tasks.json")

    def run(self):

        while True:
            # exit is used to close the program
            exit = False
            starting = True
            self.read_users_from_json("users.json")
            self.read_tasks_from_json("tasks.json")
            print("Task Manager App")
            self.start_menu()

            while starting:
                starting_command = input("Command: ")

                if starting_command == "0":
                    print("Closing the program")
                    starting = False
                    exit = True

                elif starting_command == "1":
                    if self.login() == "exit":
                        starting = False
                        exit = True
                    else:
                        starting = False

                elif starting_command == "2":
                    self.register()
                    starting = False

                else:
                    print("Invalid input\n")
                    self.start_menu()

            # program for users
            while self._logged_in == True and self._user.is_manager == False:
                self.user_menu()
                command = input("Command: ")

                if command == "0":
                    print("Closing the program")
                    self._logged_in = False
                    exit = True
                    break

                elif command == "1":
                    self.log_out()

                elif command == "2":
                    self.view_users()
                    print()

                elif command == "3":
                    self.view_all_tasks()
                    print()

                elif command == "4":
                    self.view_tasks()
                    print()

                elif command == "5":
                    self.add_task_user()
                    print()

                else:
                    print("Invalid input\n")
                    continue

            # program for admins
            while self._logged_in == True and self._user.is_manager == True:
                self.admin_menu()
                command = input("Command: ")

                if command == "0":
                    print("Closing the program")
                    self._logged_in = False
                    exit = True
                    break

                elif command == "1":
                    self.log_out()

                elif command == "2":
                    self.view_users()
                    print()

                elif command == "3":
                    self.view_all_tasks()
                    print()

                elif command == "4":
                    self.view_tasks()
                    print()

                elif command == "5":
                    self.add_task()
                    print()

                elif command == "6":
                    self.assign_task()
                    print()

                elif command == "7":
                    self.edit_task_status()
                    print()

                else:
                    print("Invalid input\n")
                    continue

            if exit:
                break


# testing


# user = User("asd", "asd")
# admin = Admin("qwe", "qwe")
# users = [user, admin]
app = TaskManagerApp()
app.run()
