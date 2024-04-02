# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from users import User, Admin


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list: list):
        self._users_list = users_list
        self._logged_in = False

    def login(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        for user in self._users_list:
            possible_user = []
            if username == user.get_name():
                possible_user.append(user)
                if password == possible_user[0].get_password():
                    self._logged_in = True
                    print("Logged in")
                    return
                else:
                    print("Wrong password")
                    return
            else:
                print("User not found")


# testing

user = User("asd", 1, False, "asd")
admin = Admin("qwe", 2, True, "qwe")
users = [user, admin]

app = TaskManagerApp(users)
app.login()
