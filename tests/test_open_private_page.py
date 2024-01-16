
from pages.main_page import main_page

from pages.private_page import private_page


def test_open_private_page():
    # GIVEN
    main_page.open()

    # WHEN
    private_page.private_page_open()

    # THEN



