# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from users import User, Admin


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list: list):
        self._users_list = users_list
        self._logged_in = False

    def menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 To something")

    def login(self):
        username = input("Please enter your username: ")
        # password = input("Please enter your password: ")
        possible_user = None

        for user in self._users_list:
            if username == user.get_name():
                possible_user = user
                break

        if possible_user is None:
            print("User not found\n")
            self.login()
            return

        password = input("Please enter your password: ")

        if password == possible_user.get_password():
            self._logged_in = True
            print("Logged in\n")

        else:
            print("Wrong password\n")
            self.login()

    def run(self):
        self.login()
        self.menu()
        while self._logged_in == True:
            command = input("Command: ")

            if command == "0":
                print("Closing the program")
                self._logged_in = False
                break

            else:
                print("Invalid input\n")
                self.menu()

# testing


user = User("asd", 1, False, "asd")
admin = Admin("qwe", 2, True, "qwe")
users = [user, admin]

app = TaskManagerApp(users)
app.run()
