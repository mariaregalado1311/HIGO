/app.py
→ Entry point. Registra páginas y controla navegación global.

/config.py
→ Fuente única de constantes, paths y límites del sistema.

/ui/home.py
→ UI principal del trayecto y estado del usuario.

/ui/crisis_panel.py
→ UI del flujo de crisis y regulación emocional.

/ui/_brand.py
→ CSS global y tokens visuales.

/logic/routes.py
→ Reglas puras para recomendación de rutas y scoring sensorial.

/logic/sensory.py
→ Reglas puras para calcular desgaste cognitivo.

/data/models.py
→ Modelos de datos y validaciones estructuradas.

/data/database.py
→ Inicialización SQLite y conexión resiliente.

/data/crisis_repo.py
→ Escritura y lectura de eventos de crisis.

/external/transport_api.py
→ Wrapper externo para incidencias y transporte.

/requirements.txt
→ Dependencias pineadas exactas.

/runtime.txt
→ Runtime obligatorio para Streamlit Cloud.

/.streamlit/config.toml
→ Theme base de Streamlit.
