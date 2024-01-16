from pages.main_page import main_page

from pages.business_page import business_page


def test_open_business_page():
    # GIVEN
    main_page.open()

    # WHEN
    business_page.business_page_open()

    # THEN
