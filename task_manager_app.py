# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from users import User


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list):
        self._users_list = users_list

    def login(users_list):
        login_name = input("Please enter your username: ")
        login_password = input("Please enter your password: ")

        for user in users_list:
            if login_name == User.get_name:
                for user in users_list:
                    if login_password == user.get_password:
                        