from child import Child
from task import Task

class Parent:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.children = []

    def create_child(self, name, age, gender):
        child = Child(name, age, gender)
        self.children.append(child)
        return child

    def create_task(self, child, name, period, frequency, difficulty, reward, description):
        task = Task(name, period, frequency, difficulty, reward, description)
        child.add_task(task)
        return task

    # def show_login(self):
    #     print(f'Login: {self.username}, {self.email}, {self.password}')