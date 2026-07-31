import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM policy")

data = cursor.fetchall()

print(data)

connection.close()