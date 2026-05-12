from datetime import datetime

import streamlit as st

from config import CRISIS_TRIGGERS
from data.crisis_repo import save_crisis_log
from data.models import CrisisLog


def render_crisis_panel(stress_level: int) -> None:
    """
    Renderiza panel de crisis.

    Inputs:
        stress_level: nivel actual
    """

    st.markdown("## Crisis rápida")

    trigger = st.selectbox(
        "¿Qué te afecta más?",
        CRISIS_TRIGGERS
    )

    if st.button(
        "🆘 Necesito ayuda",
        use_container_width=True
    ):
        log = CrisisLog(
            timestamp=datetime.now().isoformat(),
            trigger_type=trigger,
            stress_level=stress_level,
            selected_route="Ruta alternativa"
        )

        try:
            save_crisis_log(log)

            st.warning(
                "Contacto de emergencia preparado."
            )

        except RuntimeError as error:
            st.error(str(error))
