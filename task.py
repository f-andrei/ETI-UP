from exceptions import InvalidTaskDataError, TaskNotFoundError
tasks_list = []
from utils import validate_task_data

class Task:
    def __init__(self, name: str, period: str, frequency: str,
                 difficulty: str, reward: str, description: str, child):
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
        """Edit the task with the given data."""
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
        """Correlate the task with a child."""
        self.child = child

    def delete_task(self, task_index: int) -> bool:
        if task_index < 0 or task_index >= len(tasks_list):
            raise IndexError("Invalid task number.")
        deleted_task = tasks_list.pop(task_index)
        return True, deleted_task
        
            
    @staticmethod
    def get_task_by_name(name):
        for task in tasks_list:
            if task.name == name:
                return task
        raise TaskNotFoundError(f"Task '{name}' not found")
    
    def get_task_info(self) -> str:
        """Return a formatted string containing task information."""
        return f"Task information:\n\
                Task name: {self.name}\n\
                Period: {self.period}\n\
                Frequency: {self.frequency}\n\
                Difficulty: {self.difficulty}\n\
                Reward: {self.reward}\n\
                Description: {self.description}\n"