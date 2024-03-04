import requests
from jsonschema import validate


def test_company_credit():
    url = "https://siteapi.vtb.ru/api/calculatorkn/CalculateResult"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3',
        'Cookie': 'slb=!7oDxhqJsaoqNOvanJHUxZJVFjylcB44q2kTcHR+pDDALnlG+LpwD50m/NaveRZGrl4iKCBBxSLv7gZpgkocurZVldKwNN+x+lSFngzlNwTg='
    }

    response = requests.request("POST", url, headers=headers)
    # assert response.status_code == 200
