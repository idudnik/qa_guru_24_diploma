import json

import requests
from jsonschema import validate

from tests.api.utils.schemas_path import load_schema


def test_geo():
    url = "https://siteapi.vtb.ru/api/geoip/ip-data"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3'
    }

    response = requests.request("GET", url, headers=headers)
    body = response.json()
    assert response.status_code == 200

    schema = load_schema("geo.json")
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
