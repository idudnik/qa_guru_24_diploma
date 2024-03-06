import json
import requests
from jsonschema import validate
import allure
from allure_commons._allure import step

from utils.schemas_path import load_schema


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'sdudnik')
@allure.story('Проверка месторасположения')
def test_geo(base_url, header):
    with step("Проверка месторасположения"):
        url = f"{base_url}/geoip/ip-data"

    response = requests.request("GET", url, headers=header)
    body = response.json()
    with allure.step('Статус код = 200'):
        assert response.status_code == 200
    assert body["name"] == "Москва"

    schema = load_schema("geo.json")
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
