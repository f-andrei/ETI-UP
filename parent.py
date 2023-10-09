from child import Child
from task import Task
from exceptions import ChildNotFoundError

class Parent:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.children: list[Child] = []

    def create_child(self, name: str, age: int, gender: str) -> Child:
        """Create a new child and add it to the parent's children list."""
        child = Child(name, age, gender, self)
        self.children.append(child)
        return child
    
    def edit_child(self, **kwargs) -> None:
        """Edit child attributes based on provided keyword arguments."""
        if 'name' in kwargs:
            self.username = kwargs['name']
        if 'age' in kwargs:
            self.password = kwargs['age']
        if 'gender' in kwargs:
            self.email = kwargs['gender']

    def create_task(self, child: Child, name: str, period: str, frequency: str,
                    difficulty: str, reward: str, description: str) -> Task:
        """Create a task for the given child."""
        if child not in self.children:
            raise ChildNotFoundError("Child not found.")
        task = Task(name, period, frequency, difficulty, reward, description, child)
        child.add_task(task)
        return task
