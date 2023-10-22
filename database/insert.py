import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = 'database'
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_DIR / DB_NAME

# Create a connection to the SQLite database
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

def save_parent_to_database(parent):
    try:
        cursor.execute("INSERT INTO parents (name, age, gender, email, password_hash) VALUES (?, ?, ?, ?, ?)",
                       (parent.name, parent.age, parent.gender, parent.email, parent.password))
        connection.commit()
        parent.parent_id = cursor.lastrowid
        print(f"Parent '{parent.name}' successfully inserted into the database.")
    except Exception as e:
        print(f"Error inserting parent into the database: {e}")

def save_child_to_database(child, parent_id):
    cursor.execute("INSERT INTO children (parent_id, name, age, gender) VALUES (?, ?, ?, ?)",
                   (parent_id, child.name, child.age, child.gender))
    connection.commit()
    child.child_id = cursor.lastrowid

def save_task_to_database(task):
    cursor.execute("INSERT INTO tasks (name, period, frequency, difficulty, reward, description, child_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (task.name, task.period, task.frequency, task.difficulty, task.reward, task.description, task.child_id))
    connection.commit()