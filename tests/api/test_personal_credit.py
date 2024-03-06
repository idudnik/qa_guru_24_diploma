import requests
import json
from jsonschema import validate
from utils.schemas_path import load_schema
import allure
from allure_commons._allure import step
@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'sdudnik')
@allure.story('Проверка формы выдачи кредита наличными')
def test_personal_credit(base_url, header):
    with step("Проверка формы выдачи кредита наличными"):
        url = f'{base_url}/sitepages/v2'

    params = {
        'url': '/personal/kredit/nalichnymi/',
        'projectSysName': 'vtb.ru'
    }
    response = requests.request("GET", url, headers=header, params=params)

    body = response.json()
    with allure.step('Статус код = 200'):
        assert response.status_code == 200
    assert body["breadcrumbTitle"] == "Наличными"

    schema = load_schema("personal_credit.json")

    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
