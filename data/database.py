import sqlite3
from config import DATABASE_PATH


def get_connection() -> sqlite3.Connection:
    """
    Crea conexión SQLite.

    Outputs:
        sqlite3.Connection

    Raises:
        RuntimeError si la conexión falla
    """

    try:
        connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        return connection

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Error conectando SQLite: {error}"
        ) from error


def initialize_database() -> None:
    """
    Inicializa tablas SQLite.

    Raises:
        RuntimeError si la migración falla
    """

    connection = get_connection()

    try:
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

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Error creando tablas: {error}"
        ) from error

    finally:
        connection.close()
