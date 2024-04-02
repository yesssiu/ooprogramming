# File:         task.py
# Author:       Lauri Kodisoja
# Description:  task class

"""Class definition for a task"""


class Task:
    def __init__(self, task_name: str, task_id: int, assigned_to: object, description: str, status: str):
        self.task_name = task_name
        self.__task_id = task_id
        self.__assigned_to = assigned_to
        self.description = description
        self.__status = status

    @property
    def task_id(self):
        return self.__task_id

    @property
    def assigned_to(self):
        return self.__assigned_to

    @property
    def status(self):
        return self.__status

    def modify_task(self, new_status: str):
        self.status = new_status

    def __str__(self):
        return f"ID: {self.__task_id}, name: {self.task_name}, assigned to: {self.__assigned_to}, description: {self.description}, status: {self.status}"
