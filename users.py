from task import Task


class User:
    user_variable_id = 0

    @classmethod
    def new_id(cls):
        cls.user_variable_id += 1
        return cls.user_variable_id

    def __init__(self, name: str, password: str):
        self.__user_id = User.new_id()
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

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

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
        # print(f"Tasks after adding: {self.__tasks}")

    def view_tasks(self):
        if self.tasks:
            print("\nYour tasks:")
            for task in self.tasks:
                print(task)
        else:
            print("\nNo tasks.")

    def __str__(self):
        return f"{self.__name} (ID {self.__user_id})"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password,
            "is_manager": self.is_manager,
            "tasks": [task.to_dict() for task in self.tasks],
        }


class Admin(User):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)
        self.is_manager = True

    def modify_task(self, task_id):
        for task in self.__tasks:
            if task.task_id == task_id:
                task.modify_task()
