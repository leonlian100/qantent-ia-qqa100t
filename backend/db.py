import sqlite3

conn = sqlite3.connect("patents.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS patents (
    id INTEGER PRIMARY KEY,
    title TEXT,
    abstract TEXT,
    assignee TEXT
)
""")
conn.execute(
    "INSERT INTO patents (title, abstract) VALUES (?, ?)",
    (title, abstract)
)
conn.commit()

