

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

    def create_task(self, child, name, period, frequency, description):
        task = Task(name, period, frequency, description)
        child.add_task(task)
        return task

    def show_login(self):
        print(f'Login: {self.username}, {self.email}, {self.password}')


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


class Task:
    def __init__(self, name, period, frequency, description):
        self.name = name
        self.period = period
        self.frequency = frequency
        self.description = description
        self.completed = False
        self.correlation = None

    def edit_task(self, name, period, frequency, description):
        ...

    def correlate_task(self, child):
        ...

    def show_task(self):
        print(
            f'Tarefa: {self.name}, {self.period}, {self.frequency}'
            f'{self.description}'
        )


class Feeling:
    def __init__(self, mood, description):
        self.mood = mood
        self.description = description


parent = Parent("pai", "123456", "email@gmail.com")

filho = parent.create_child("filho", 5, 'male')
tarefa = parent.create_task(filho, "Estudar", "Diariamente", "A noite", "Descricao")
filho.complete_task(tarefa)
sentimento = Feeling("Feliz", "Felicidade")
tarefa.edit_task("Tarefa editada", "Semanalmente", "De manha", "Descricaoo")
tarefa.correlate_task(filho)

parent.show_login()
filho.show_child()
tarefa.show_task()