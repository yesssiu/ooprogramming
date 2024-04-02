# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from users import User, Admin


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list: list):
        self._users_list = users_list
        self._logged_in = False
        self._user = None

    def user_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 View tasks")

    def admin_menu(self):
        print("Commands:")
        print("0 Exit")
        print("1 Log out")
        print("2 View tasks")

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
            self._user = possible_user
            print("Logged in\n")

        else:
            print("Wrong password\n")
            self.login()

    def log_out(self):
        print("Logging out")
        self._logged_in = False

    # def view_tasks(self):

    def run(self):
        self.login()
        if self._user.is_manager == False:
            self.user_menu()
        elif self._user.is_manager == True:
            self.admin_menu()

        while self._logged_in == True and self._user.is_manager == False:
            command = input("Command: ")

            if command == "0":
                print("Closing the program")
                self._logged_in = False
                break

            elif command == "1":
                self.log_out()

            else:
                print("Invalid input\n")
                self.user_menu()

        while self._logged_in == True and self._user.is_manager == True:
            command = input("Command: ")

            if command == "0":
                print("Closing the program")
                self._logged_in = False
                break

            elif command == "1":
                self.log_out

            else:
                print("Invalid input\n")
                self.user_menu()

# testing


user = User("asd", 1, False, "asd")
admin = Admin("qwe", 2, True, "qwe")
users = [user, admin]

app = TaskManagerApp(users)
app.run()
