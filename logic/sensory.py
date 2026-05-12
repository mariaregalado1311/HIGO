from config import DEFAULT_SENSORY_SCORE


def calculate_sensory_score(
    noise_level: int,
    crowd_level: int
) -> int:
    """
    Calcula score sensorial.

    Inputs:
        noise_level: sensibilidad ruido
        crowd_level: sensibilidad crowd

    Outputs:
        int score

    Raises:
        ValueError si inputs inválidos
    """

    if noise_level < 1 or crowd_level < 1:
        raise ValueError("Valores inválidos.")

    reduction = (noise_level + crowd_level) // 2

    score = DEFAULT_SENSORY_SCORE - reduction

    return max(score, 1)
