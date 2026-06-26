import sqlite3
import pandas as pd

conn = sqlite3.connect("agriatlas.db")

df = pd.read_sql("SELECT * FROM crop_data", conn)

print(df.head())

conn.close()