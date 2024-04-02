# File:         task.py
# Author:       Jessica Laamanen
# Description:  main

from users import User, Admin
from task import Task
from task_manager_app import TaskManagerApp

"""Definition for the main program"""


def main():
    user = User("asd", False, "asd")
    admin = Admin("qwe", True, "qwe")
    users = [user, admin]

    task1 = Task("a", user, "first task", "underway")

    app = TaskManagerApp(users)
    app.run()
