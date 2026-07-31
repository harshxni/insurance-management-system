import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("ALTER TABLE claim ADD COLUMN status TEXT")

connection.commit()
connection.close()

print("Claim table updated")