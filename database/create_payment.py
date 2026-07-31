import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_email TEXT,
    policy_name TEXT,
    amount INTEGER,
    payment_status TEXT
)
""")

connection.commit()
connection.close()

print("Payment table created")