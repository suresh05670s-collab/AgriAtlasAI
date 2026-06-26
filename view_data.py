import sqlite3

conn = sqlite3.connect("agriatlas.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM crops")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()