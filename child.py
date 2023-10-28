from exceptions import ChildNotFoundError, TaskNotFoundError
from feeling import Feeling
from database.select import get_child_info_by_parent_id, get_parent_id_by_email, get_last_child_id
from utils import get_child_index
class Child:
    """
    Represents a child with tasks and feelings.

    Attributes:
        name (str): The name of the child.
        age (int): The age of the child.
        gender (str): The gender of the child.
        parent (Parent): The parent object associated with the child.
        child_id (int): A unique identifier for the child.
        tasks (list): A list to store Task objects associated with the child.
        feelings (list): A list to store Feeling objects associated with the child.

    Methods:
        complete_task(task_name: str) -> str: Marks a task as completed by name.
        add_feeling(feeling: Feeling) -> None: Adds a feeling to the child's feelings list.
    """

    child_counter = 1

    def __init__(self, name: str, age: int, gender: str, parent, child_id=None):
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
            feelings (list): A list to store Feeling objects associated with the child.
        """
        self.child_id = child_id or Child.child_counter
        self.name = name.title()
        self.age = age
        self.gender = gender.title()
        self.parent = parent
        self.feelings: list[Feeling] = []
        
        parent_id = get_parent_id_by_email(self.parent.email)
        child_data = get_child_info_by_parent_id(parent_id)
        
        
        if len(child_data) > 1:
            selected_child, _ = get_child_index(child_data, allow_selection=True)
            self.child_id = child_data[selected_child][0]
        else:
            last_id = get_last_child_id(parent_id)
            self.child_id = last_id


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
        ...

    def add_feeling(self, feeling: Feeling) -> None:
        """
        Adds a feeling to the child's feelings list.

        Args:
            feeling (Feeling): The Feeling object to be added.
        """
        self.feelings.append(feeling)

    