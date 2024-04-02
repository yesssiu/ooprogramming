# File:         task_manager_app.py
# Author:       Lauri Kodisoja
# Description:  task manager application

from users import User, TaskManager
from main import main


"""Class definition for the application"""


class TaskManagerApp:

    def __init__(self, users_list):
        self._users_list = users_list

    def login():
        login_name = input("Please enter your username: ")
        login_password = input("Please enter your password: ")
