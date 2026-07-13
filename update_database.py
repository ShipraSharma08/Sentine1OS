import sqlite3

connection = sqlite3.connect("sentinel.db")
cursor = connection.cursor()

try:
    cursor.execute(
        "ALTER TABLE scan_history ADD COLUMN scanned_at TEXT"
    )
    print("scanned_at column added successfully!")

except sqlite3.OperationalError:
    print("scanned_at column already exists!")

connection.commit()
connection.close()