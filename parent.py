from child import Child
from task import Task
from exceptions import ChildNotFoundError

class Parent:
    def __init__(self, username: str, age: int, gender: str, email: str, password: str):
        self.username = username
        self.age = age
        self.gender = gender
        self.email = email
        self.password = password
        self.children: list[Child] = []

    def create_child(self, name: str, age: int, gender: str) -> Child:
        """Create a new child and add it to the parent's children list."""
        child = Child(name, age, gender, self)
        child.parent = self
        self.children.append(child)
        return child
    
    def create_task(self, child: Child, name: str, period: str, frequency: str,
                    difficulty: str, reward: str, description: str) -> Task:
        """Create a task for the given child."""
        if child not in self.children:
            raise ChildNotFoundError("Child not found.")
        task = Task(name, period, frequency, difficulty, reward, description, child)
        child.add_task(task)
        return task
    
    def get_parent_info(self) -> str:
        """Return parent's info."""
        children_names = ", ".join(child.name for child in self.children)
        return f"Parent's info:\n\
                Name: {self.username}\n\
                Age: {self.age}\n\
                Gender: {self.gender}\n\
                E-mail: {self.email}\n\
                Children: {children_names}"
        