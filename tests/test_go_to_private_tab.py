
from pages import main_page
from pages.main_page import MainPage
from pages.private_tab import PrivatePage

private_page=PrivatePage()
main_page=MainPage()
def test_go_to_private_tab():
    # GIVEN
    main_page.open()

    # WHEN
    private_page.private_page_open()

    # THEN



