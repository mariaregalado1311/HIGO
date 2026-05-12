from pathlib import Path

APP_NAME = "NeuroRoute"

DATABASE_DIR = Path("/tmp")
DATABASE_PATH = DATABASE_DIR / "neuroroute.db"

MAX_STRESS_LEVEL = 10
MIN_STRESS_LEVEL = 1

DEFAULT_SENSORY_SCORE = 82

ROUTE_STEPS = [
    "Baja en la próxima parada",
    "Camina 120 metros hasta Avenida América",
    "Toma el Bus 200",
    "Baja en Nuevos Ministerios"
]

CRISIS_TRIGGERS = [
    "Ruido",
    "Aglomeración",
    "Confusión",
    "Retraso inesperado",
    "Contacto físico"
]
