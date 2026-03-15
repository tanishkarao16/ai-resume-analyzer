import sqlite3

conn = sqlite3.connect("candidates.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
skills TEXT,
experience TEXT,
score REAL
)
""")

conn.commit()


def insert_candidate(name, skills, experience, score):

    cursor.execute("""
    INSERT INTO candidates(name, skills, experience, score)
    VALUES (?, ?, ?, ?)
    """, (name, skills, experience, score))

    conn.commit()


def get_ranked_candidates():

    cursor.execute("""
    SELECT name, skills, experience, score
    FROM candidates
    ORDER BY score DESC
    """)

    return cursor.fetchall()