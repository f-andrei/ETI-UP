import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = 'database'
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_DIR / DB_NAME

TASK_TABLE = 'tasks'

def establish_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(str(DB_FILE))
    return connection

def update_task_in_database(task_id, name, period, frequency, difficulty, reward, description, child_id):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE {TASK_TABLE} SET name=?, period=?, frequency=?, difficulty=?, '
            'reward=?, description=? WHERE child_id=?',
            (name, period, frequency, difficulty, reward, description, child_id)
        )
        connection.commit()
    finally:
        connection.close()