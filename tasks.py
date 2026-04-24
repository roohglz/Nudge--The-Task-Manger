from abc import ABC, abstractmethod

class BaseTask(ABC):
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    def describe(self):
        print("This is a task")

    def __eq__(self, other):
        if isinstance(other, BaseTask):
            return self.title == other.title and self.priority == other.priority
        return False

    def __repr__(self):
        return f"BaseTask(title={self.title}, priority={self.priority})"

class PersonalTask(BaseTask):
    def __init__(self, title, priority, category):
        super().__init__(title, priority)
        self.category = category
        self.__status = "pending"

    def execute(self):
        print(f"Executing personal task: {self.title}")

    def get_details(self):
        print(f"Title: {self.title}, Priority: {self.priority}, Category: {self.category}, Status: {self.status}")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value in ["pending", "in progress", "done"]:
            self.__status = value
        else:
            raise ValueError("Invalid status. Must be 'pending', 'in progress', or 'done'.")

    @property
    def task_type(self):
        return "personal"

    def __str__(self):
        return f"PersonalTask: {self.title} [{self.status}]"

class UrgentMixin:
    def escalate(self):
        print(f"URGENT: {self.title} needs immediate attention")

class WorkTask(BaseTask):
    def __init__(self, title, priority, deadline):
        super().__init__(title, priority)
        self.deadline = deadline

    def execute(self):
        print(f"Executing work task: {self.title}")

    def get_details(self):
        print(f"Title: {self.title}, Priority: {self.priority}, Deadline: {self.deadline}")

    def __str__(self):
        return f"WorkTask: {self.title} [Due: {self.deadline}]"

    @property
    def task_type(self):
        return "work"

class UrgentWorkTask(WorkTask, UrgentMixin):
    def __init__(self, title, priority, deadline, reason):
        super().__init__(title, priority, deadline)
        self.reason = reason

    def execute(self):
        print(f"URGENT execution: {self.title} - Reason: {self.reason}")

    def __str__(self):
        return f"UrgentWorkTask: {self.title} [Due: {self.deadline}]"

    @property
    def task_type(self):
        return "urgent"

class TaskManager:
    total_tasks = 0

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        TaskManager.total_tasks += 1
        return self

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks

    @staticmethod
    def validate_priority(priority):
        if priority in ["Low", "Medium", "High"]:
            return True
        else:
            raise ValueError("Invalid priority. Must be 'Low', 'Medium', or 'High'.")

    def __str__(self):
        return f"TaskManager: {self.name} ({len(self.tasks)} tasks)"

    def __len__(self):
        return len(self.tasks)

    def __repr__(self):
        return f"TaskManager(name={self.name})"

    def get_tasks_by_type(self, task_type):
        return [task for task in self.tasks if isinstance(task, task_type)]

    def summary(self):
        print(f"Manager: {self.name}")
        print(f"Total tasks: {len(self.tasks)}")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
        return self
