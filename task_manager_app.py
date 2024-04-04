# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from task import Task
from users import User, Admin


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list: list):
        self._users_list = users_list
        self._tasks = []
        self._logged_in = False
        self._user = None

    # menu for regular users
    def user_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 Own tasks")
        print("3 All tasks")
        print("4 New task")
        print()

    # menu for admin users
    def admin_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 Own tasks")
        print("3 All tasks")
        print("4 New task")
        print("5 Edit task status")
        print()

    def register(self):
        username = input("Enter your username: ")
        password_validation = False

        while not password_validation:
            password = input("Enter your password: ")
            password_2 = input("Re-enter your password: ")
            if password == password_2:
                new_user = User(username, password)
                self._users_list.append(new_user)
                print("\nUser created succesfully")
                password_validation = True
            else:
                print("\nPassword did not match, try again\n")

    def login(self):
        username = input("Enter your username (\"exit\" to exit): ")

        # makes it possible to close the program from the login
        if username == "exit":
            print("Closing the program")
            return "exit"

        # if username found it's stored in possible_user which is used to check the password
        possible_user = None
        for user in self._users_list:
            if username == user.name:
                possible_user = user

        if possible_user is None:
            print("User not found\n")
            return self.login()

        password = input("Enter your password: ")

        # comparing password to the possible_user's password
        if password == possible_user.password:
            self._logged_in = True
            self._user = possible_user
            print("Logged in\n")

        else:
            print("Wrong password\n")
            return self.login()

    def log_out(self):
        print("Logging out\n")
        self._logged_in = False

    # for user to see their own tasks
    def view_tasks(self):
        print()
        print(self._user.view_tasks())

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
        print()
        for user in self._users_list:
            print(user)

    # for user to add a task for themselves
    def add_task_user(self):
        task_name = input("\nName of task: ")
        description = input("Short description: ")
        task = Task(task_name, description)
        task.assigned_to = self._user
        self._user.tasks = task
        self._tasks.append(task)

    # for admin to add tasks
    def add_task(self):
        task_name = input("\nName of task: ")
        description = input("Short description: ")
        task = Task(task_name, description)
        choice = input("Assign task to user (y/n): ")

        # possibility to assign a task to any user
        if choice == "y":
            print("\nList of all users:")
            self.view_users()
            try:
                id = int(input("\nSelect a user by their ID: "))
            except ValueError:
                print("Invalid ID, task not assigned")
                self._tasks.append(task)
                return
            for user in self._users_list:
                if user.user_id == id:
                    task.assigned_to = user
                    print(f"Task assigned to {user.name}")
        self._tasks.append(task)

    # for admin to edit task status
    def edit_task_status(self):
        self.view_all_tasks()
        if self._tasks == []:
            return

        else:
            task_to_edit = input("\nInsert task ID to edit: ")
            for task in self._tasks:
                if int(task_to_edit) == task.task_id:
                    new_status = input("New status of the task: ")
                    task.status = new_status
                else:
                    print("No task found with the given ID")

    def run(self):
        while True:
            # exit is used to close the program
            exit = False
            if self.login() == "exit":
                break

            # checks if there is user or an admin and shows according options
            if self._user.is_manager == False:
                self.user_menu()
            elif self._user.is_manager == True:
                self.admin_menu()

            # program for users
            while self._logged_in == True and self._user.is_manager == False:
                command = input("Command: ")

                if command == "0":
                    print("Closing the program")
                    self._logged_in = False
                    exit = True
                    break

                elif command == "1":
                    self.log_out()

                elif command == "2":
                    self.view_tasks()
                    print()

                elif command == "3":
                    self.view_all_tasks()
                    print()

                elif command == "4":
                    self.add_task_user()
                    print()

                else:
                    print("Invalid input\n")
                    self.user_menu()

            # program for admins
            while self._logged_in == True and self._user.is_manager == True:
                command = input("Command: ")

                if command == "0":
                    print("Closing the program")
                    self._logged_in = False
                    exit = True
                    break

                elif command == "1":
                    self.log_out()

                elif command == "2":
                    self.view_tasks()
                    print()

                elif command == "3":
                    self.view_all_tasks()
                    print()

                elif command == "4":
                    self.add_task()
                    print()

                elif command == "5":
                    self.edit_task_status()
                    print()

                else:
                    print("Invalid input\n")
                    self.admin_menu()

            if exit:
                break

# testing


user = User("asd", "asd")
admin = Admin("qwe", "qwe")
users = [user, admin]

app = TaskManagerApp(users)

# app.register()
# app.view_users()
app.run()
