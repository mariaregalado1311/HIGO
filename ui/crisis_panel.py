from datetime import datetime

import streamlit as st

from config import CRISIS_TRIGGERS

from data.crisis_repo import save_crisis_log
from data.models import CrisisLog


def render_crisis_panel(
    stress_level: int
) -> None:

    st.markdown("## Regulación rápida")

    trigger = st.selectbox(
        "¿Qué te está afectando más?",
        CRISIS_TRIGGERS
    )

    if st.button(
        "🆘 Activar protocolo de apoyo",
        use_container_width=True
    ):

        with st.spinner(
            "Preparando apoyo..."
        ):

            log = CrisisLog(
                timestamp=datetime.now().isoformat(),
                trigger_type=trigger,
                stress_level=stress_level,
                selected_route="Ruta alternativa"
            )

            save_crisis_log(log)

            st.success(
                "Tu protocolo de apoyo fue activado."
            )

            st.info(
                "Dirígete a una zona menos concurrida."
            )
