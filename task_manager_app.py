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
        print("2 View tasks")

    # menu for admin users
    def admin_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 View own tasks")
        print("3 View all tasks")

    def login(self):
        username = input("Enter your username (\"exit\" to exit): ")

        # makes it possible to close the program from the login
        if username == "exit":
            print("Closing the program")
            return 'exit'

        # if username foundit's stored in possible_user which is used to check the password
        possible_user = None
        for user in self._users_list:
            if username == user.get_name():
                possible_user = user
                break

        if possible_user is None:
            print("User not found\n")
            self.login()
            return

        password = input("Enter your password: ")

        # comparing password to the possible_user's password
        if password == possible_user.get_password():
            self._logged_in = True
            self._user = possible_user
            print("Logged in\n")

        else:
            print("Wrong password\n")
            self.login()

    def log_out(self):
        print("Logging out\n")
        self._logged_in = False

    # for user to see their own tasks
    def view_tasks(self):
        print(self._user.view_tasks())

    # for admin to see all tasks
    def view_all_tasks(self):
        for task in self._tasks:
            print(task)

    # for admin to add tasks
    # def add_task(self):
        # task =

    def run(self):
        while True:
            # exit is used to close the program
            exit = False
            if self.login() == 'exit':
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

                else:
                    print("Invalid input\n")
                    self.admin_menu()

            if exit:
                break

# testing


user = User("asd", "asd")
admin = Admin("qwe", "qwe")
users = [user, admin]

task1 = Task("a", user, "first task", "underway")

app = TaskManagerApp(users)

app.run()
