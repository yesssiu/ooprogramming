# File:         task.py
# Author:       Lauri Kodisoja
# Description:  task class

"""Class definition for a task"""


class Task:
    # class variable, gives task_id automatically and is +1
    # for each task that is created
    task_variable_id = 1

    def __init__(self, task_name: str, category: str, description: str, deadline: str):
        self.__task_id = Task.task_variable_id
        Task.task_variable_id += 1
        self.task_name = task_name
        self.__assigned_to = None
        self.__category = category
        self.description = description
        self.__status = "in progress"
        self.__deadline = deadline

    @property
    def task_id(self):
        return self.__task_id

    @property
    def assigned_to(self):
        return self.__assigned_to

    @assigned_to.setter
    def assigned_to(self, user):
        self.__assigned_to = user

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status: str):
        self.__status = new_status

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        self.__category = new_category

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        self.__deadline = new_deadline

    def __str__(self):
        return f"ID: {self.__task_id}, name: {self.task_name}, assigned to: {self.__assigned_to}, category: {self.__category}, description: {self.description}, status: {self.status}, deadline: {self.deadline}"
