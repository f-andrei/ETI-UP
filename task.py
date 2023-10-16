from exceptions import InvalidTaskDataError, TaskNotFoundError
from validations import validate_task_data
from database.insert import save_task_to_database
# from database.update import update_task_in_database
tasks_list = []

class Task:
    """
    Represents a task associated with a child.

    Attributes:
        name (str): The name of the task.
        period (str): The period of the task (e.g., morning, afternoon).
        frequency (str): The frequency of the task (e.g., daily, weekly).
        difficulty (str): The difficulty level of the task.
        reward (str): The reward associated with the task.
        description (str): Description of the task.
        completed (bool): Indicates whether the task is completed or not.
        child (Child): The Child object associated with the task.
        correlation (None): Placeholder for task correlation information.

    Methods:
        edit_task(name=None, period=None, frequency=None, difficulty=None, reward=None, description=None,
                  child=None): Edits the task with the given data.
        correlate_task(child): Correlates the task with a child.
        delete_task(task_index: int) -> bool: Deletes a task by index from the tasks list.
        get_task_by_name(name): Retrieves a task by its name from the tasks list.
        get_task_info() -> str: Returns a formatted string containing task information.
    """
    
    def __init__(self, name: str, period: str, frequency: str,
                 difficulty: str, reward: str, description: str, child):
        """
        Initializes a Task object.

        Args:
            name (str): The name of the task.
            period (str): The period of the task (e.g., morning, afternoon).
            frequency (str): The frequency of the task (e.g., daily, weekly).
            difficulty (str): The difficulty level of the task.
            reward (str): The reward associated with the task.
            description (str): Description of the task.
            child (Child): The Child object associated with the task.

        Raises:
            InvalidTaskDataError: If any of the required task data is missing or empty.
        """
        if not all([name, period, frequency, difficulty, reward, description]):
            raise InvalidTaskDataError("Task data is incomplete.")
        self.name = name
        self.period = period
        self.frequency = frequency
        self.difficulty = difficulty
        self.reward = reward
        self.description = description
        self.completed = False
        self.child = child
        self.correlation = None

    def edit_task(self, name=None, period=None, frequency=None, difficulty=None, reward=None, description=None,
                  child=None):
        """
        Edits the task with the given data.

        Args:
            name (str, optional): The new name of the task.
            period (str, optional): The new period of the task (e.g., morning, afternoon).
            frequency (str, optional): The new frequency of the task (e.g., daily, weekly).
            difficulty (str, optional): The new difficulty level of the task.
            reward (str, optional): The new reward associated with the task.
            description (str, optional): The new description of the task.
            child (Child, optional): The new Child object associated with the task.
        """
        if name is not None:
            self.name = name.strip()

        if period is not None:
            validate_task_data(period, self.frequency, self.difficulty)
            self.period = period

        if frequency is not None:
            validate_task_data(self.period, frequency, self.difficulty)
            self.frequency = frequency

        if difficulty is not None:
            validate_task_data(self.period, self.frequency, difficulty)
            self.difficulty = difficulty

        if reward is not None:
            self.reward = reward

        if description is not None:
            self.description = description

        if child is not None:
            self.child = child

    def correlate_task(self, child) -> None:
        """
        Correlates the task with a child.

        Args:
            child (Child): The Child object to be associated with the task.
        """
        self.child = child

    def delete_task(self, task_index: int) -> bool:
        """
        Deletes a task by index from the tasks list.

        Args:
            task_index (int): The index of the task to be deleted.

        Returns:
            bool: True if the task was successfully deleted, False otherwise.

        Raises:
            IndexError: If the specified task index is out of range.
        """
        if task_index < 0 or task_index >= len(tasks_list):
            raise IndexError("Invalid task number.")
        deleted_task = tasks_list.pop(task_index)
        return True, deleted_task

    @staticmethod
    def get_task_by_name(name):
        """
        Retrieves a task by its name from the tasks list.

        Args:
            name (str): The name of the task to be retrieved.

        Returns:
            Task: The Task object with the specified name.

        Raises:
            TaskNotFoundError: If the specified task is not found in the tasks list.
        """
        for task in tasks_list:
            if task.name == name:
                return task
        raise TaskNotFoundError(f"Task '{name}' not found")

    def get_task_info(self) -> str:
        """
        Returns a formatted string containing task information.

        Returns:
            str: A formatted string containing task information.
        """
        return f"Task information:\n\
                Child: {self.child.name}\n\
                Task name: {self.name}\n\
                Period: {self.period}\n\
                Frequency: {self.frequency}\n\
                Difficulty: {self.difficulty}\n\
                Reward: {self.reward}\n\
                Description: {self.description}\n"
    
    def save_to_database(self):
        # if self.id is None:
        save_task_to_database(self)
        # else:
        #     update_task_in_database(self)
