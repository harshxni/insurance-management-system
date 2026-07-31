import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO policy(policy_name, policy_type, premium, duration)
VALUES 
('Health Secure', 'Health', 5000, '1 Year')
""")

cursor.execute("""
INSERT INTO policy(policy_name, policy_type, premium, duration)
VALUES 
('Life Protect', 'Life', 8000, '5 Years')
""")

cursor.execute("""
INSERT INTO policy(policy_name, policy_type, premium, duration)
VALUES 
('Vehicle Care', 'Vehicle', 3000, '1 Year')
""")

connection.commit()
connection.close()

print("Policies Added")