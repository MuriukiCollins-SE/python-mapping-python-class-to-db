# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

def init_db():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
    """)
    CONN.commit()

def drop_db():
    CURSOR.execute("DROP TABLE IF EXISTS departments")
    CONN.commit()
