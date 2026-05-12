import streamlit as st

from data.database import initialize_database
from ui._brand import inject_brand_styles
from ui.home import render_home_page


def main() -> None:

    st.set_page_config(
        page_title="NeuroRoute",
        page_icon="🧠",
        layout="wide"
    )

    initialize_database()

    inject_brand_styles()

    render_home_page()


if __name__ == "__main__":
    main()
