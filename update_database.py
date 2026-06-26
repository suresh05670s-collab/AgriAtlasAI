import sqlite3
import pandas as pd

# Read cleaned Excel dataset
df = pd.read_excel("dataset/cleaned_crop_data.xlsx")

# Connect to SQLite database
conn = sqlite3.connect("agriatlas.db")

# Replace old data with cleaned data
df.to_sql("crop_data", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("✅ Database updated successfully!")