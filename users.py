# File:         users.py
# Author:       Lauri Kodisoja
# Description:  class definition for different users

from task import Task

"""Class definition for a user"""


class User:
    # class variable, gives user_id automatically and is +1
    # for each user that is created
    # same variable is used in Admin class
    user_variable_id = 1

    def __init__(self, name: str, password: str):
        self.__user_id = User.user_variable_id
        User.user_variable_id += 1
        self.__name = name
        self.__is_manager = False
        self.__password = password
        self.__tasks = []

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    @property
    def user_id(self):
        return self.__user_id

    @property
    def is_manager(self):
        return self.__is_manager

    @is_manager.setter
    def is_manager(self, value):
        self.__is_manager = value

    @property
    def tasks(self):
        return self.__tasks

    def add_task(self, new_task: Task):
        self.__tasks.append(new_task)

    def view_tasks(self):
        for task in self.__tasks:
            print(task)

    def __str__(self):
        return f"{self.__name} (ID {self.__user_id})"


"""Class definition for a admin"""


class Admin(User):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)
        self.is_manager = True

    def modify_task(self, task_id):
        for task in self.__tasks:
            if task.task_id == task_id:
                task.modify_task()
