import requests
import json
from jsonschema import validate
from tests.api.utils.schemas_path import load_schema


def test_personal_credit():
    url = "https://siteapi.vtb.ru/api/sitepages/v2?url=/personal/kredit/nalichnymi/&projectSysName=vtb.ru"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3',
        'Content-Type': 'application/json',
        'Cookie': 'slb=!7oDxhqJsaoqNOvanJHUxZJVFjylcB44q2kTcHR+pDDALnlG+LpwD50m/NaveRZGrl4iKCBBxSLv7gZpgkocurZVldKwNN+x+lSFngzlNwTg='
    }

    response = requests.request("GET", url, headers=headers)

    body = response.json()
    assert response.status_code == 200

    schema = load_schema("personal_credit.json")
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)