from pages.main_page import main_page

from pages.bank_info_page import bank_info_page


def test_open_bank_info_page():
    # GIVEN
    main_page.open()

    # WHEN
    bank_info_page.bank_info_page_open()

    # THEN

