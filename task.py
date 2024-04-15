# File:         task.py
# Author:       Lauri Kodisoja
# Description:  task class

"""Class definition for a task"""


class Task:
    # class variable, gives task_id automatically and is +1
    # for each task that is created
    task_variable_id = 0

    @classmethod
    def new_id(cls):
        cls.task_variable_id += 1
        return cls.task_variable_id

    def __init__(self, task_name: str, category: str, description: str, deadline: str):
        self.__task_id = Task.new_id()
        self.task_name = task_name
        self.__assigned_to = None
        self.__category = category
        self.description = description
        self.__status = "Created"
        self.__deadline = deadline

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def user_id(self, value):
        self.__task_id = value

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
        assigned_to_name = (
            self.__assigned_to.name if self.__assigned_to else "Unassigned"
        )
        return f"ID: {self.__task_id}, name: {self.task_name}, assigned to: {assigned_to_name}, category: {self.__category}, description: {self.description}, status: {self.status}, deadline: {self.deadline}"

    def to_dict(self):
        assigned_to_id = None
        if self.__assigned_to:
            assigned_to_id = self.__assigned_to.user_id
        return {
            "task_id": self.__task_id,
            "task_name": self.task_name,
            "assigned_to_id": assigned_to_id,
            "category": self.__category,
            "description": self.description,
            "status": self.__status,
            "deadline": self.__deadline,
        }
