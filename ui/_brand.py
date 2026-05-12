import streamlit as st


def inject_brand_styles():

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #0F172A;
            color: white;
        }

        h1, h2, h3 {
            color: white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
