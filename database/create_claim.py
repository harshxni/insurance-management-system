import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS claim(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    policy_name TEXT,
    claim_reason TEXT,
    status TEXT
)
""")

connection.commit()
connection.close()

print("Claim table created")