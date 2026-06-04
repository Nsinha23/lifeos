import sqlite3
conn = sqlite3.connect("lifeos.db")
cursor = conn.cursor() 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        done INTEGER DEFAULT 0
    )
""")
print("✅ Database and habits table created!")