# File:         task.py
# Author:       Jessica Laamanen
# Description:  main

from users import User
from task import Task
from task_manager_app import TaskManagerApp


user1 = User["User1", "1", "true", "salasana1"]
user2 = User["User2", "2", "false", "salasana2"]

users_list = [user1, user2]


def main():
    TaskManagerApp(users_list)
