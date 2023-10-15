from exceptions import TaskNotFoundError
from feeling import Feeling
from task import Task

class Child:
    """
    Represents a child with tasks and feelings.

    Attributes:
        name (str): The name of the child.
        age (int): The age of the child.
        gender (str): The gender of the child.
        parent (Parent): The parent object associated with the child.
        child_number (int): A unique identifier for the child.
        tasks (list): A list to store Task objects associated with the child.
        feelings (list): A list to store Feeling objects associated with the child.

    Methods:
        add_task(task: Task) -> None: Adds a task to the child's task list.
        complete_task(task_name: str) -> str: Marks a task as completed by name.
        add_feeling(feeling: Feeling) -> None: Adds a feeling to the child's feelings list.
        get_child_info() -> str: Returns a formatted string containing child's information.
    """

    child_counter = 1

    def __init__(self, name: str, age: int, gender: str, parent):
        """
        Initializes a Child object.

        Args:
            name (str): The name of the child.
            age (int): The age of the child.
            gender (str): The gender of the child.
            parent (Parent): The parent object associated with the child.

        Attributes:
            name (str): The name of the child.
            age (int): The age of the child.
            gender (str): The gender of the child.
            parent (Parent): The parent object associated with the child.
            child_number (int): A unique identifier for the child.
            tasks (list): A list to store Task objects associated with the child.
            feelings (list): A list to store Feeling objects associated with the child.
        """
        self.name = name.title()
        self.age = age
        self.gender = gender.title()
        self.parent = parent
        self.child_number = Child.child_counter
        Child.child_counter += 1
        self.tasks: list[Task] = []
        self.feelings: list[Feeling] = []

    def add_task(self, task: Task) -> None:
        """
        Adds a task to the child's task list.

        Args:
            task (Task): The Task object to be added.
        """
        self.tasks.append(task)

    def complete_task(self, task_name: str) -> str:
        """
        Marks a task as completed by name.

        Args:
            task_name (str): The name of the task to be marked as completed.

        Returns:
            str: A message indicating the status of the task completion.

        Raises:
            TaskNotFoundError: If the specified task is not found in the child's tasks list.
        """
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Task "{task.name}" completed successfully.'
        raise TaskNotFoundError(f'Task "{task_name}" not found for child {self.name}.')

    def add_feeling(self, feeling: Feeling) -> None:
        """
        Adds a feeling to the child's feelings list.

        Args:
            feeling (Feeling): The Feeling object to be added.
        """
        self.feelings.append(feeling)

    def get_child_info(self) -> str:
        """
        Returns a formatted string containing child's information.

        Returns:
            str: A formatted string containing child's information.
        """
        parent_info = f'Parent: {self.parent.name}\n\
            Age: {self.parent.age}\n\
            Gender: {self.parent.gender}\n\
            E-mail: {self.parent.email}'
        return f"Child info:\n\
            Name: {self.name}\n\
            Age: {self.age}\n\
            Gender: {self.gender}\n\
            {parent_info}"
