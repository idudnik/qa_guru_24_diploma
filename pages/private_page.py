import allure
from selene import browser, have, by


class PrivatePage:
    def __init__(self):
        self.private_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.element(by.text("Перейти в раздел"))
        self.check_the_text = browser.element('#bank-offers p')

    def private_page_open(self):
        self.private_page.element_by(have.text('Частным лицам')).click()
        self.go_to_the_section.click()

    def check_text_is_display(self):
        with allure.step('Проверить, что текст "Предложения банка:" - отображается'):
            self.check_the_text.should(have.exact_text('Предложения банка'))


private_page = PrivatePage()
