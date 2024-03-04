from pages.main_page import main_page

from pages.self_employed_page import self_employed_page


def test_open_self_employed_page():
    # GIVEN
    main_page.open()

    # WHEN
    self_employed_page.self_employed_page_open()

    # THEN
    self_employed_page.check_text_is_display()
