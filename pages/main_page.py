from selene import browser, be, have
import allure

class MainPage:
    def open(self):
        with allure.step('Открыть https://vtb.ru/'):
            browser.open('/')