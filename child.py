class Child:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.tasks = []
        self.feelings = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        ...

    def add_feeling(self, feeling):
        self.feelings.append(feeling)

    def show_child(self):
        print(f'Filho: {self.name}, {self.age}, {self.gender}')