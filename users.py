# File:         users.py
# Author:       Lauri Kodisoja
# Description:  class definition for different users

from task import Task

"""Class definition for a user"""


class User:
    def __init__(self, name: str, id: int, is_manager: bool, password: str):
        self.__name = name
        self.__id = id
        self.__is_manager = is_manager
        self.__password = password
        self.__tasks = []

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def view_tasks(self):
        for task in self.__tasks:
            return task

    def __str__(self):
        return f"User ID: {self.__id}, username: {self.__name}"


"""Class definition for a task manager"""


class TaskManager(User):
    def __init__(self, name: str, id: int, is_manager: bool, password: str):
        super().__init__(name, id, is_manager, password)

    def modify_task(self, task_id):
        for task in self.__tasks:
            if task.task_id == task_id:
                task.modify_task()

    def new_task(self, task: Task):
        self.__tasks.append(task)
