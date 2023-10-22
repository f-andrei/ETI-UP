
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_DIR = 'database'
DB_NAME = 'tamagochi.sqlite3'
DB_FILE = ROOT_DIR / DB_DIR / DB_NAME

PARENT_TABLE = 'parents'
CHILD_TABLE = 'children'
TASK_TABLE = 'tasks'

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

# Clear existing data from tables
cur.execute(f'DELETE FROM {PARENT_TABLE}')
cur.execute(f'DELETE FROM {CHILD_TABLE}')
cur.execute(f'DELETE FROM {TASK_TABLE}')
conn.commit()

# Clear all ids
cur.execute('VACUUM')
conn.commit()


# Create parent table
cur.execute(
    f'CREATE TABLE IF NOT EXISTS {PARENT_TABLE}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'age INTEGER, '
    'gender TEXT, '
    'email TEXT, '
    'password_hash TEXT'
    ')'
)
conn.commit()

# Create child table
cur.execute(
    f'CREATE TABLE IF NOT EXISTS {CHILD_TABLE}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'age INTEGER, '
    'gender TEXT, '
    'parent_id INTEGER, '
    f'FOREIGN KEY (parent_id) REFERENCES {PARENT_TABLE}(id)'
    ')'
)
conn.commit()

# Create task table
cur.execute(
    f'CREATE TABLE IF NOT EXISTS {TASK_TABLE}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'period TEXT, '
    'frequency TEXT, '
    'difficulty TEXT, '
    'reward TEXT, '
    'description TEXT,'
    'child_id INTEGER, '
    f'FOREIGN KEY (child_id) REFERENCES {CHILD_TABLE}(id)'
    ')'
)
conn.commit()

cur.close()
conn.close()
