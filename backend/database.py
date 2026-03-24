import sqlite3

DB_NAME = "ametra.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
    
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        time TEXT,
        place TEXT,
        archetype TEXT,
        top_system TEXT,
        payment_status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()    