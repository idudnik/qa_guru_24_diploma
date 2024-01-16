from selene import browser
import allure


class MainPage:
    def open(self):
        with allure.step('Открыть https://vtb.ru/'):
            browser.open('/')


main_page = MainPage()
