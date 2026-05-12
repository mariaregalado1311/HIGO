from pathlib import Path

APP_NAME = "NeuroRoute"

DATABASE_DIR = Path("/tmp")
DATABASE_PATH = DATABASE_DIR / "neuroroute.db"

DEFAULT_NOISE_LEVEL = 8
DEFAULT_CROWD_LEVEL = 9

DEFAULT_STRESS_LEVEL = 5

DEFAULT_SENSORY_SCORE = 82

ROUTE_STEPS = [
    "Baja en la próxima parada",
    "Camina 120 metros hasta Avenida América",
    "Toma el Bus 200 (ocupación baja estimada)",
    "Baja en Nuevos Ministerios"
]

CRISIS_TRIGGERS = [
    "Ruido",
    "Aglomeración",
    "Confusión",
    "Retraso inesperado",
    "Contacto físico"
]
