from exceptions import InvalidTaskDataError, TaskNotFoundError
tasks_list = []

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
        if name is not None and name != "":
            self.name = name
        if period is not None and period != "":
            self.period = period
        if frequency is not None and frequency != "":
            self.frequency = frequency
        if difficulty is not None and difficulty != "":
            self.difficulty = difficulty
        if reward is not None and reward != "":
            self.reward = reward
        if description is not None and description != "":
            self.description = description
        return True

    def correlate_task(self, child) -> None:
        """Correlate the task with a child."""
        self.child = child

    def delete_task(self) -> bool:
        """Delete a task by name."""
        i = 0
        for task in tasks_list:
            print(f'{i + 1}. {task.name}')
            i += 1
        try:
            task_to_delete = int(input("Which task do you want to delete? ")) - 1
            if 0 <= task_to_delete < len(tasks_list):
                del tasks_list[task_to_delete]
                return True
            else:
                print("Error: Invalid task number.")
                return False
        except ValueError:
            print("Error: Invalid input. Please enter a valid task number.")
            return False
        
    def get_task_info(self) -> str:
        """Return a formatted string containing task information."""
        return f"Task information:\n\
                Task name: {self.name}\n\
                Period: {self.period}\n\
                Frequency: {self.frequency}\n\
                Difficulty: {self.difficulty}\n\
                Reward: {self.reward}\n\
                Description: {self.description}\n"
