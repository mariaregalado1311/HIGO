from data.database import initialize_database
from ui._brand import inject_brand_styles
from ui.home import render_home_page


def main() -> None:
    """
    Entry point aplicación.
    """

    initialize_database()

    inject_brand_styles()

    render_home_page()


if __name__ == "__main__":
    main()
