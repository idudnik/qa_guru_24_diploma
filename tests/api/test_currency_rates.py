import json

import allure
import requests
from allure_commons._allure import step
from jsonschema import validate

from utils.schemas_path import load_schema


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'sdudnik')
@allure.story('Проверка курса валют')
def test_currency_rates(base_url, header):
    with step("Проверка курса валют"):
        url = f"{base_url}currencyrates/table/card"

    params = {
        'category': '5',
        'type': '1',
        'from': '2024-02-21',
        'to': '2024-02-25'
    }

    response = requests.request("GET", url, headers=header, params=params)

    body = response.json()
    with allure.step('Статус код = 200'):
        assert response.status_code == 200
    assert body["category"]["name"] == "Покупка по карте"

    schema = load_schema("currency_rates.json")
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
