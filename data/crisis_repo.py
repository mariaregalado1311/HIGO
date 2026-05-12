from data.database import get_connection


def save_crisis_log(log):

    connection = get_connection()

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

    connection.close()
