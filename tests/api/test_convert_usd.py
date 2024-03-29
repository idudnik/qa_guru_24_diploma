import requests
import json
import allure
from allure_commons._allure import step


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'sdudnik')
@allure.story('Конвертация валюты в евро')
def test_convert_usd(base_url, header):
    with step("Конвертация валюты в USD"):
        url = f'{base_url}currencyrates/convert'

    summa = 100
    payload = json.dumps({
        "categoryId": 1,
        "categoryTypeId": 1,
        "currencyFrom": "USD",
        "currencyTo": "RUB",
        "fromSumma": summa,
        "toSumma": 0
    })

    response = requests.request("POST", url, headers=header, data=payload)
    with allure.step('Статус код = 200'):
        assert response.status_code == 200
    assert response.json()["fromCurrencySymbol"] == "$"
    assert response.json()["fromSumma"] == summa
