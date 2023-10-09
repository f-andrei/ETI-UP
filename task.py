from exceptions import InvalidTaskDataError, TaskNotFoundError

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

    def edit_task(self, name: str = None, period: str = None, frequency: str = None,
                  difficulty: str = None, reward: str = None, description: str = None) -> None:
        """Edit task attributes."""
        if name is not None:
            self.name = name
        if period is not None:
            self.period = period
        if frequency is not None:
            self.frequency = frequency
        if difficulty is not None:
            self.difficulty = difficulty
        if reward is not None:
            self.reward = reward
        if description is not None:
            self.description = description

    def correlate_task(self, child) -> None:
        """Correlate the task with a child."""
        self.child = child

    def delete_task(self, child, task_name: str) -> bool:
        """Delete a task by name."""
        tasks_to_keep = [task for task in child.tasks if task.name != task_name]
        if len(tasks_to_keep) < len(child.tasks):
            child.tasks = tasks_to_keep
            print(f'Task "{task_name}" deleted successfully.')
            return True
        else:
            print(f'Task "{task_name}" not found for child {child.name}.')
            return False

    def get_task_info(self) -> str:
        """Return a formatted string containing task information."""
        return (
            f'Task: {self.name}, '
            f'Period: {self.period}, '
            f'Frequency: {self.frequency}, '
            f'Description: {self.description}'
        )
