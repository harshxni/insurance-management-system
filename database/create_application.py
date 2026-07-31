import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS application(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_email TEXT,
    policy_name TEXT,
    status TEXT
)
""")

connection.commit()
connection.close()

print("Application table created")