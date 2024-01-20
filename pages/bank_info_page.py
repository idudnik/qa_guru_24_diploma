import allure
from selene import browser, have


class BankinfoPage:
    def __init__(self):
        self.bank_info_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.all('[href="/about/"]')
        self.check_the_text = browser.element('#section-id > div > div:nth-child(1) > div > p')

    def bank_info_page_open(self):
        self.bank_info_page.should(have.size_greater_than(0)).element_by(have.exact_text('О банке')).click()
        self.go_to_the_section.element_by(have.text('Перейти в раздел')).click()

    def check_text_is_display(self):
        with allure.step('Проверить, что текст "Признаны лучшими в разных сферах"- отображается'):
            self.check_the_text.should(have.exact_text('Признаны лучшими в разных сферах'))


bank_info_page = BankinfoPage()
