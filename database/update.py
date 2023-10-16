import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

TASK_TABLE = 'tasks'

def establish_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(str(DB_FILE))
    return connection

def update_task_in_database(task):
    """
    Update task data in the database.

    Args:
        task (Task): The Task object with updated data.
    """
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE {TASK_TABLE} SET name=?, period=?, frequency=?, difficulty=?, '
            'reward=?, description=? WHERE id=?',
            (task.name, task.period, task.frequency, task.difficulty, task.reward, 
             task.description, task.id)
        )
        connection.commit()
    finally:
        connection.close()
