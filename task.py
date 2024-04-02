
"""Class definition for a task"""


class Task:
    def __init__(self, task_name: str, task_id: int, assigned_to: object, description: str, status: str):
        self.task_name = task_name
        self.__task_id = task_id
        self.__asigned_to = assigned_to
        self.description = description
        self.__status = status

    @property
    def task_id(self):
        return self.__task_id

    @property
    def assigned_to(self):
        return self.__asigned_to

    @property
    def status(self):
        return self.__status

    def modify_task(self, new_status: str):
        self.status = new_status
