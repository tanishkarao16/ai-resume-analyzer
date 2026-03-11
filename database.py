import sqlite3

def create_table():

    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY,
        name TEXT,
        skills TEXT,
        experience TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()
    
def save_candidate(name, skills, experience, score):

    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO candidates (name, skills, experience, score) VALUES (?, ?, ?, ?)",
        (name, skills, experience, score)
    )

    conn.commit()
    conn.close()
    