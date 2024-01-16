import allure
from selene import browser, have, by


class BusinessPage:
    def __init__(self):
        self.business_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.all('[href="/malyj-biznes/"]')
        self.check_the_text = browser.element('#tarifs  p')

    def business_page_open(self):
        self.business_page.element_by(have.text('Бизнесу')).click()
        self.go_to_the_section.element_by(have.text('Перейти в раздел')).click()
        with allure.step('Проверить, что текст "Тарифы для бизнеса"- отображается'):
            self.check_the_text.should(have.exact_text('Тарифы для бизнеса'))


business_page = BusinessPage()
