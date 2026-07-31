import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("ALTER TABLE policy ADD COLUMN policy_type TEXT")

cursor.execute("ALTER TABLE policy ADD COLUMN duration TEXT")

connection.commit()
connection.close()

print("Policy table updated")