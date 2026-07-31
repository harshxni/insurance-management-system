import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(payment)")

data = cursor.fetchall()

print(data)

connection.close()