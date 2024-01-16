from pages.main_page import main_page

from pages.credit_company_page import credit_company_page


def test_open_credit_company_page():
    # GIVEN
    main_page.open()

    # WHEN
    credit_company_page.credit_company_page_open()

    # THEN
