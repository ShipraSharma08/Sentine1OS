import sqlite3

connection = sqlite3.connect("sentinel.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scan_history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

file_name TEXT,

status TEXT

)
""")

connection.commit()

connection.close()

print("Database Created Successfully!")