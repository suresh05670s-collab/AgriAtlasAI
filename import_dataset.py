import sqlite3
import pandas as pd

# Read Excel file
df = pd.read_excel("dataset/crop_data.xlsx")

# Connect to SQLite
conn = sqlite3.connect("agriatlas.db")

# Import data into SQLite
df.to_sql("crop_data", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("Excel data imported successfully!")