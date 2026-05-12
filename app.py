import streamlit as st
# ---------- RIGHT PANEL ----------
with col2:
    st.markdown("## Regulación")

    stress_level = st.slider(
        "Nivel de estrés actual",
        1,
        10,
        st.session_state.stress_level
    )

    st.session_state.stress_level = stress_level

    st.markdown("---")

    st.markdown("## Crisis rápida")

    crisis_trigger = st.selectbox(
        "¿Qué te está afectando más?",
        [
            "Ruido",
            "Aglomeración",
            "Confusión",
            "Retraso inesperado",
            "Contacto físico"
        ]
    )

    if st.button("🆘 Necesito ayuda", use_container_width=True):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
                timestamp,
                crisis_trigger,
                stress_level,
                "Ruta alternativa"
            )
        )

        conn.commit()

        st.warning(
            "Contacto de emergencia preparado. "
            "Respira. Sigue el paso 1 del plan alternativo."
        )

    st.markdown("---")

    st.markdown("## Herramientas rápidas")

    if st.button("🎧 Modo baja estimulación"):
        st.info("Reduciendo elementos visuales y notificaciones")

    if st.button("📍 Mostrar zonas tranquilas"):
        st.info("Detectando espacios menos concurridos")

# ---------- FOOTER ----------
st.divider()

st.caption(
    "MVP conceptual · Streamlit prototype · Diseñado para validar "
    "reducción de incertidumbre durante incidencias"
)
