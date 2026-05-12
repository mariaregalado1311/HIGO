import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NeuroRoute",
    page_icon="🧠",
    layout="wide"
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("neuroroute.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crisis_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    trigger_type TEXT,
    stress_level INTEGER,
    selected_route TEXT
)
""")

conn.commit()

# ---------------- SESSION STATE ----------------
if "stress_level" not in st.session_state:
    st.session_state.stress_level = 5

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("⚙️ Perfil Sensorial")

    sound_sensitivity = st.slider(
        "Sensibilidad al ruido",
        1,
        10,
        8
    )

    crowd_sensitivity = st.slider(
        "Sensibilidad a aglomeraciones",
        1,
        10,
        9
    )

    smell_sensitivity = st.slider(
        "Sensibilidad a olores",
        1,
        10,
        7
    )

    st.divider()

    energy_level = st.select_slider(
        "Energía cognitiva",
        options=[
            "Muy baja",
            "Baja",
            "Media",
            "Alta"
        ],
        value="Baja"
    )

# ---------------- HEADER ----------------
st.title("🧠 NeuroRoute")

st.subheader(
    "Movilidad urbana diseñada para reducir incertidumbre y carga sensorial"
)

# ---------------- INCIDENT ALERT ----------------
st.error(
    "⚠️ Incidencia detectada en Línea 6: retraso estimado de 18 minutos"
)

# ---------------- COLUMNS ----------------
col1, col2 = st.columns([2, 1])

# ---------------- LEFT COLUMN ----------------
with col1:

    st.markdown("## ¿Qué está pasando?")

    st.write(
        "El sistema detectó una interrupción en tu trayecto habitual. "
        "Te mostraremos una alternativa con menor desgaste cognitivo."
    )

    st.divider()

    st.markdown("## Plan B recomendado")

    with st.container(border=True):

        st.markdown("### Ruta alternativa de bajo estrés")

        st.write("**Paso 1:** Baja en la próxima parada")
        st.write("**Paso 2:** Camina 120 metros hasta Avenida América")
        st.write("**Paso 3:** Toma el Bus 200")
        st.write("**Paso 4:** Baja en Nuevos Ministerios")

        st.success("✔ Menor ruido estimado")
        st.success("✔ Menor densidad de pasajeros")
        st.success("✔ Menor número de transbordos")

    st.divider()

    st.markdown("## Compatibilidad sensorial")

    sensory_score = 82

    st.progress(sensory_score / 100)

    st.caption(
        f"Compatibilidad sensorial estimada: {sensory_score}%"
    )

# ---------------- RIGHT COLUMN ----------------
with col2:

    st.markdown("## Regulación")

    stress_level = st.slider(
        "Nivel de estrés actual",
        1,
        10,
        st.session_state.stress_level
    )

    st.session_state.stress_level = stress_level

    st.divider()

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

    st.divider()

    st.markdown("## Herramientas rápidas")

    if st.button("🎧 Modo baja estimulación"):
        st.info(
            "Reduciendo elementos visuales y notificaciones"
        )

    if st.button("📍 Mostrar zonas tranquilas"):
        st.info(
            "Detectando espacios menos concurridos"
        )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "MVP conceptual · Streamlit prototype · "
    "Diseñado para validar reducción de incertidumbre "
    "durante incidencias"
)
