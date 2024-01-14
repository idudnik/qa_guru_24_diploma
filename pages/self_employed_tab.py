from pathlib import Path

import allure
from selene import browser, have, be, by, command


class SelfEmployedPage:
    def __init__(self):
        self.private_page = browser.all('[aria-label="Первого уровня"]>label')
        self.go_to_the_section = browser.element(by.text("Перейти в раздел"))

    def open(self):
        browser.open('/')

    def private_page_open(self):
        self.private_page.element_by(have.text('Частным лицам')).click()
        self.go_to_the_section.click()




