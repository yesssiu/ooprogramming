from task import Task

"""Class definition for a user"""


class User:
    def __init__(self, name: str, id: int, is_manager: bool, password: str):
        self.__name = name
        self.__id = id
        self.__is_manager = is_manager
        self.__password = password
        self.__tasks = []

    def view_tasks(self):
        for task in self.__tasks:
            return task

    def __str__(self):
        return F"User ID: {self.__id}, username: {self.__name}"


"""Class definition for a task manager"""


class TaskManager(User):
    def __init__(self, name: str, id: int, is_manager: bool, password: str):
        super().__init__(name, id, is_manager, password)

    def modify_tasks(self):
        

    def new_task(self, task: Task):
        self.__tasks.append(task)