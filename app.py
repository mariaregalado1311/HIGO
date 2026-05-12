import streamlit as st

from data.database import initialize_database
from ui._brand import inject_brand
from ui.home import render_home_page


def main():

    st.set_page_config(
        page_title="NeuroRoute",
        page_icon="🧠",
        layout="wide"
    )

    initialize_database()

    inject_brand()

    render_home_page()


if __name__ == "__main__":
    main()
