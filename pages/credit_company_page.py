import allure
from selene import browser, have


class CreditcompanyPage:
    def __init__(self):
        self.credit_company_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.all('[href="/credit-organizations/"]')
        self.check_the_text = browser.element('#services  p')

    def credit_company_page_open(self):
        self.credit_company_page.element_by(have.text('Кредитным организациям')).click()
        self.go_to_the_section.element_by(have.text('Перейти в раздел')).click()
        with allure.step('Проверить, что текст "Услуги"- отображается'):
            self.check_the_text.should(have.text('Услуги'))


credit_company_page = CreditcompanyPage()
