import sqlite3

conn = sqlite3.connect("agriatlas.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO crops (crop_name, season, expected_yield)
VALUES (?, ?, ?)
""", ("Rice", "Kharif", 4.8))

conn.commit()

print("Sample crop inserted successfully!")

conn.close()