class Task:
    def __init__(self, name, period, frequency, difficulty, reward, description):
        self.name = name
        self.period = period
        self.frequency = frequency
        self.difficulty = difficulty
        self.reward = reward
        self.description = description
        self.completed = False
        self.child = None
        self.correlation = None

    def edit_task(self, name, period, frequency, difficulty, reward, description):
        ...

    def correlate_task(self, child):
        self.child = child

    def delete_task(self, child, task_name):
        for task in child.tasks:
            if task.name == task_name:
                child.tasks.remove(task)
                print(f'Task "{task_name}" deleted successfully.')
                break
        else:
            print(f'Task "{task_name}" not found for child {child.name}.')

    def show_task(self):
        print(
            f'Tarefa: {self.name}, {self.period}, {self.frequency}'
            f'{self.description}'
        )