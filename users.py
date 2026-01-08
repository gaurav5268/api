import csv
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

cursor.execute("SELECT name, email FROM users")
rows = cursor.fetchall()

print("Users stored in database:\n")
for row in rows:
    print("Name:", row[0], "| Email:", row[1])

conn.commit()
conn.close()
