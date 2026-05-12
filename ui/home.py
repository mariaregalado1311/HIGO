import streamlit as st

from config import (
    DEFAULT_CROWD_LEVEL,
    DEFAULT_NOISE_LEVEL,
    DEFAULT_STRESS_LEVEL
)

from external.transport_api import (
    get_transport_incident
)

from logic.routes import get_low_stress_route
from logic.sensory import calculate_sensory_score

from ui.crisis_panel import render_crisis_panel


def render_home_page() -> None:

    st.title("🧠 NeuroRoute")

    st.subheader(
        "Movilidad urbana diseñada para reducir incertidumbre y carga sensorial."
    )

    incident = get_transport_incident()

    st.error(incident["message"])

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("## Ruta alternativa recomendada")

        route_steps = get_low_stress_route()

        with st.container(border=True):

            for index, step in enumerate(route_steps):
                st.write(f"**Paso {index + 1}:** {step}")

        sensory_score = calculate_sensory_score(
            noise_level=DEFAULT_NOISE_LEVEL,
            crowd_level=DEFAULT_CROWD_LEVEL
        )

        st.divider()

        st.metric(
            "Compatibilidad sensorial",
            f"{sensory_score}%"
        )

        st.progress(sensory_score / 100)

    with col2:

        stress_level = st.slider(
            "Nivel de estrés",
            1,
            10,
            DEFAULT_STRESS_LEVEL
        )

        if stress_level >= 8:
            st.warning("Sobrecarga sensorial alta detectada.")

        render_crisis_panel(
            stress_level=stress_level
        )
