import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS policy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_name TEXT,
    policy_type TEXT,
    premium INTEGER,
    duration TEXT
)
""")

connection.commit()
connection.close()

print("Policy table created")