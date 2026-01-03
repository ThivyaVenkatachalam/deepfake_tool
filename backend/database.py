import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("detections.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            media_type TEXT,
            verdict TEXT,
            score REAL
        )
        """)

    def save(self, media_type, verdict, score):
        self.conn.execute(
            "INSERT INTO results (media_type, verdict, score) VALUES (?, ?, ?)",
            (media_type, verdict, score)
        )
        self.conn.commit()
