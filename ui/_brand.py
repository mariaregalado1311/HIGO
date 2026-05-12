import streamlit as st


def inject_brand():

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=Inter:wght@400;500&family=Space+Grotesk:wght@500;600&display=swap');

        :root {

            --primary: #2F5D8C;
            --secondary: #DCE8F2;
            --accent: #7DB8B6;

            --bg: #F5F7FA;
            --surface: #FFFFFF;
            --text: #1F2A37;

            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 16px;

            --shadow-sm: 0 1px 2px rgba(15,23,42,0.04);
            --shadow-md: 0 6px 18px rgba(15,23,42,0.08);

            --spacing-1: 4px;
            --spacing-2: 8px;
            --spacing-3: 12px;
            --spacing-4: 16px;
            --spacing-5: 24px;
            --spacing-6: 32px;
        }

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
            color: var(--text);
        }

        .stApp {
            background-color: var(--bg);
        }

        section.main > div {
            max-width: 1200px;
            padding-top: 2rem;
        }

        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif;
            letter-spacing: -0.03em;
            color: var(--text);
        }

        h1 {
            font-size: 2.6rem;
            font-weight: 600;
        }

        h2 {
            font-size: 1.6rem;
            font-weight: 600;
        }

        .stButton button {

            background-color: var(--primary);
            color: white;

            border: none;
            border-radius: var(--radius-md);

            padding: 0.7rem 1rem;

            font-weight: 500;

            transition: 0.2s ease;

            box-shadow: var(--shadow-sm);
        }

        .stButton button:hover {

            background-color: #264C73;

            transform: translateY(-1px);

            box-shadow: var(--shadow-md);
        }

        .stTextInput input,
        .stSelectbox div,
        .stTextArea textarea {

            background-color: var(--surface);

            border-radius: var(--radius-md);

            border: 1px solid #D7E0EA;

            padding: 0.65rem;

            box-shadow: none;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {

            border-color: var(--primary);

            box-shadow: 0 0 0 1px var(--primary);
        }

        .stSlider {

            padding-top: 0.5rem;
        }

        .stMetric {

            background: var(--surface);

            border-radius: var(--radius-lg);

            padding: 1rem;

            box-shadow: var(--shadow-sm);
        }

        div[data-testid="stSidebar"] {

            background-color: #EDF3F8;

            border-right: 1px solid #DCE8F2;
        }

        .stAlert {

            border-radius: var(--radius-md);
        }

        .stProgress > div > div {

            background-color: var(--accent);
        }

        code {
            font-family: 'IBM Plex Mono', monospace;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
