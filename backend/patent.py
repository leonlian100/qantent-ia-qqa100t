import sqlite3

def get_patents(query):
    conn = sqlite3.connect("patents.db")

    cur = conn.execute(
        "SELECT title, abstract FROM patents WHERE abstract LIKE ? LIMIT 50",
        (f"%{query}%",)
    )

    return [{"title": r[0], "abstract": r[1]} for r in cur.fetchall()]
