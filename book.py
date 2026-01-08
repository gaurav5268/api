import requests
import sqlite3

book_name = input("Enter book name: ")

url = f"https://www.googleapis.com/books/v1/volumes?q={book_name}"
data = requests.get(url).json()

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

def create_books_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year TEXT
    )
    """)

create_books_table()

item = data.get("items", [None])[0]

if item:
    info = item.get("volumeInfo", {})
    title = info.get("title", "Unknown")
    author = info.get("authors", ["Unknown"])[0]
    year = info.get("publishedDate", "N/A")[:4]

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )

cursor.execute("SELECT title, author, year FROM books")
for row in cursor.fetchall():
    print(f"Title: {row[0]} | Author: {row[1]} | Year: {row[2]}")

conn.commit()
conn.close()
