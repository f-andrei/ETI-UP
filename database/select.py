import sqlite3

from main import DB_FILE, TABLE_NAME

# Connection
 
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

row = cur.fetchone()
# Desempacotamento -> remove da tupla
_id, name, weight = row
print(_id, name, weight)
# for row in cur.fetchall():
#     # print(row)
#     _id, name, weight = row
#     print(_id, name, weight)

cur.close()
conn.close()