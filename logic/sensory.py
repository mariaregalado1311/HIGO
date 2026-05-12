from config import DEFAULT_SENSORY_SCORE


def calculate_sensory_score(
    noise_level: int,
    crowd_level: int
) -> int:

    reduction = (
        noise_level + crowd_level
    ) // 2

    score = DEFAULT_SENSORY_SCORE - reduction

    return max(score, 1)
