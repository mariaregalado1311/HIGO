from dataclasses import dataclass


@dataclass
class CrisisLog:
    """
    Representa un evento de crisis registrado.

    Inputs:
        timestamp: fecha del evento
        trigger_type: detonante seleccionado
        stress_level: nivel de estrés
        selected_route: ruta usada

    Outputs:
        CrisisLog válido

    Raises:
        ValueError si stress_level es inválido
    """

    timestamp: str
    trigger_type: str
    stress_level: int
    selected_route: str

    def validate(self) -> None:
        if self.stress_level < 1 or self.stress_level > 10:
            raise ValueError("Stress level fuera de rango.")
