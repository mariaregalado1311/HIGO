from data.database import get_connection
from data.models import CrisisLog


def save_crisis_log(log: CrisisLog) -> None:
    """
    Guarda evento de crisis en SQLite.

    Inputs:
        log: CrisisLog validado

    Raises:
        RuntimeError si escritura falla
    """

    log.validate()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO crisis_logs (
                timestamp,
                trigger_type,
                stress_level,
                selected_route
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                log.timestamp,
                log.trigger_type,
                log.stress_level,
                log.selected_route
            )
        )

        connection.commit()

    except Exception as error:
        raise RuntimeError(
            f"Error guardando crisis log: {error}"
        ) from error

    finally:
        connection.close()
