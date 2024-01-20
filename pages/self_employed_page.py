import allure
from selene import browser, have, by


class SelfEmployedPage:
    def __init__(self):
        self.self_employed_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.all('[href="/samozanyatym/"]')
        self.check_the_text = browser.element('#komu-podoydet  p')

    def self_employed_page_open(self):
        self.self_employed_page.element_by(have.text('Самозанятым')).click()
        self.go_to_the_section.element_by(have.text('Перейти в раздел')).click()


    def check_text_is_display(self):
        with allure.step('Проверить, что текст "Кому подойдет самозанятость"- отображается'):
            self.check_the_text.should(have.exact_text('Кому подойдет самозанятость'))

self_employed_page = SelfEmployedPage()
