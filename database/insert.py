import sqlite3

# Create a connection to the SQLite database
connection = sqlite3.connect('tamagochi.sqlite3')
cursor = connection.cursor()

def save_parent_to_database(parent):
    cursor.execute("INSERT INTO parents (name, age, gender, email, password_hash) VALUES (?, ?, ?, ?, ?)",
                   (parent.name, parent.age, parent.gender, parent.email, parent.password))
    connection.commit()
    parent.parent_id = cursor.lastrowid

def save_child_to_database(child):
    cursor.execute("INSERT INTO children (name, age, gender, parent_id) VALUES (?, ?, ?, ?)",
                   (child.name, child.age, child.gender, child.parent.parent_id))
    connection.commit()
    child.child_id = cursor.lastrowid

def save_task_to_database(task):
    cursor.execute("INSERT INTO tasks (name, period, frequency, difficulty, reward, description, child_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (task.name, task.period, task.frequency, task.difficulty, task.reward, task.description, task.child.child_id))
    connection.commit()