import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE claim SET policy_name=? WHERE id=?",
    ("Health Secure", 1)
)

connection.commit()
connection.close()

print("Claim updated")
