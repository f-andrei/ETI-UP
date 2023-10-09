from exceptions import TaskNotFoundError
from feeling import Feeling
from task import Task

class Child:
    def __init__(self, name: str, age: int, gender: str, parent):
        self.name = name
        self.age = age
        self.gender = gender
        self.parent = parent
        self.tasks: list[Task] = []
        self.feelings: list[Feeling] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the child's task list."""
        self.tasks.append(task)

    def complete_task(self, task_name: str) -> str:
        """Mark a task as completed by name."""
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Task "{task.name}" completed successfully.'
        else:
            raise TaskNotFoundError(f'Task "{task_name}" not found for child {self.name}.')

    def add_feeling(self, feeling: Feeling) -> None:
        """Add a feeling to the child's feelings list."""
        self.feelings.append(feeling)

    def get_child_info(self) -> str:
        """Return a formatted string containing child's information."""
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'
