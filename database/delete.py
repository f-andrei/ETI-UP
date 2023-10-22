import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = 'database'
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_DIR / DB_NAME

# Create a connection to the SQLite database
def establish_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(str(DB_FILE))
    return connection

TASK_TABLE = 'tasks'

def delete_task_from_database(task_id):
    connection = establish_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM {TASK_TABLE} WHERE id = ?', (task_id,))
        connection.commit()
        print(f"Task with ID {task_id} deleted successfully.")
    finally:
        connection.close()