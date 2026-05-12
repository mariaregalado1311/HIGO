import sqlite3

from config import DATABASE_PATH


def get_connection():

    return sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crisis_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        trigger_type TEXT,
        stress_level INTEGER,
        selected_route TEXT
    )
    """)

    connection.commit()

    connection.close()
