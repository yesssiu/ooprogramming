# File:         task.py
# Author:       Jessica Laamanen
# Description:  main

from users import User, Admin
from task import Task
from task_manager_app import TaskManagerApp


admin = Admin("Admin", 1, True, "asd")
user = User("User", 2, False, )

users_list = [admin, user]


def main():
    TaskManagerApp(users_list)
