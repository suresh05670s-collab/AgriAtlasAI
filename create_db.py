import sqlite3

# Connect to database
connection = sqlite3.connect("agriatlas.db")

# Create cursor
cursor = connection.cursor()

# -------------------------
# Users Table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# -------------------------
# Crops Table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS crops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    season TEXT,
    expected_yield REAL
)
""")

# -------------------------
# Soil Table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS soil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soil_type TEXT,
    nitrogen REAL,
    phosphorus REAL,
    potassium REAL,
    ph REAL
)
""")

# -------------------------
# Rainfall Table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS rainfall (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    district TEXT,
    rainfall REAL,
    year INTEGER
)
""")

# -------------------------
# Predictions Table
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    soil_type TEXT,
    rainfall REAL,
    predicted_yield REAL,
    prediction_date TEXT
)
""")

# Save changes
connection.commit()

print("✅ All database tables created successfully!")

# Close database
connection.close()