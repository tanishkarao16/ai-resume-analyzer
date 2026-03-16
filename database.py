import sqlite3

DB_NAME = "candidates.db"


def insert_candidate(name, skills, experience, score):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates (name, skills, experience, score)
        VALUES (?, ?, ?, ?)
    """, (name, skills, experience, score))

    conn.commit()
    conn.close()


def get_ranked_candidates():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, skills, experience, score
        FROM candidates
        ORDER BY score DESC
    """)

    candidates = cursor.fetchall()

    conn.close()

    return candidates