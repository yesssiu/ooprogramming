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

    def get_name(self):
        return self.__name

    def get_password(self):
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

    @tasks.setter
    def tasks(self, new_task):
        return self.tasks.append(new_task)

    def view_tasks(self):
        for task in self.__tasks:
            return task

    def __str__(self):
        return f"User ID: {self.__user_id}, username: {self.__name}"


"""Class definition for a admin"""


class Admin(User):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)
        self.is_manager = True

    def modify_task(self, task_id):
        for task in self.__tasks:
            if task.task_id == task_id:
                task.modify_task()

    def new_task(self, task: Task):
        self.__tasks.append(task)

# testing


# user = User("asd", False, "asd")
# admin = Admin("qwe", True, "qwe")

# print(user.user_id)
# print(admin.user_id)
