from pages.main_page import main_page

from pages.share_holders_page import share_holders_page


def test_open_credit_company_page():
    # GIVEN
    main_page.open()

    # WHEN
    share_holders_page.share_holders_page_open()

    # THEN
    share_holders_page.check_text_is_display()
