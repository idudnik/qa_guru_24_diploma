import allure
from selene import browser, have


class ShareHoldersPage:
    def __init__(self):
        self.share_holders_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.all('[href="/ir/"]')
        self.check_the_text = browser.element('#section-id > div > div:nth-child(1) > div > p')

    def share_holders_page_open(self):
        self.share_holders_page.element_by(have.exact_text('Акционерам')).click()
        self.go_to_the_section.element_by(have.text('Перейти в раздел')).click()

    def check_text_is_display(self):
        with allure.step('Проверить, что текст "Новости"- отображается'):
            self.check_the_text.should(have.text('Новости'))


share_holders_page = ShareHoldersPage()
