import sqlite3

connection = sqlite3.connect("sentinel.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT NOT NULL,
        status TEXT NOT NULL,
        scanned_at TEXT
    )
""")

connection.commit()
connection.close()

print("Database initialized successfully!")