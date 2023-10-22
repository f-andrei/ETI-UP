import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = 'database'
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_DIR / DB_NAME

PARENT_TABLE = 'parents'
CHILD_TABLE = 'children'
TASK_TABLE = 'tasks'


def establish_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(str(DB_FILE))
    return connection

def get_parent_id_by_email(email: str):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT id FROM {PARENT_TABLE} WHERE email = ?', (email,))
        parent_id = cursor.fetchone()
        if parent_id:
            return parent_id[0] 
        else:
            return None  
    finally:
        connection.close()

def get_parent_by_email(email: str):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {PARENT_TABLE} WHERE email = ?', (email, ))
        parent_data = cursor.fetchone() 
        return parent_data
    finally:
        connection.close()

def get_parent_object(email: str):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT name, age, gender, email, password_hash FROM {PARENT_TABLE} WHERE email = ?', (email, ))
        parent_data = cursor.fetchone()  
        return parent_data
    finally:
        connection.close() 

def get_child_info_by_parent_id(parent_id: int):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT id, name, age, gender FROM {CHILD_TABLE} WHERE parent_id = ?', (parent_id, ))
        children_data = cursor.fetchall()
     
        return children_data
    finally:
        connection.close()

def get_tasks_for_child(child_id):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {TASK_TABLE} WHERE child_id = ?', (child_id,))
        tasks = cursor.fetchall()
        return tasks
    finally:
        connection.close()

def get_last_child_id(parent_id: str):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT id from {CHILD_TABLE} WHERE parent_id = ?', (parent_id,))
        rows = cursor.fetchall()
        if rows:
            last_child_id = max(row[0] for row in rows)
            return last_child_id
        else:
            return None
    finally:
        connection.close()

def get_tasks_for_child_by_child_id(child_id):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT id, name, period, frequency, difficulty, reward, description, child_id FROM {TASK_TABLE} WHERE child_id = ?', (child_id,))
        tasks_data = cursor.fetchall()

        tasks = []
        for task in tasks_data:
            task_dict = {
                "id": task[0],
                "name": task[1],
                "period": task[2],
                "frequency": task[3],
                "difficulty": task[4],
                "reward": task[5],
                "description": task[6],
                "child_id": task[7]
            }
            tasks.append(task_dict)
        
        return tasks
    finally:
        connection.close()


def get_child_id_by_parent_email(email: str):
    parent_id = get_parent_id_by_email(email)
    child_info = get_child_info_by_parent_id(parent_id)
    print(f"Children for email {email}:")
    for idx, child in enumerate(child_info):
        print(f"{idx + 1}: {child[1]}")
    while True:
        try:
            child_index = int(input("Select a child: ")) - 1
            if 0 <= child_index < len(child_info):
                child_id = child_info[child_index][0]
                return child_id
            else:
                print("Invalid selection. Please enter a valid child index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
