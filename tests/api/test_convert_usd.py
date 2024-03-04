import requests
import json


def test_convert_usd():
    """тест проверяет конвертер валют"""
    url = "https://siteapi.vtb.ru/api/currencyrates/convert"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.3',

        'Cookie': 'slb=!IIBz6qv6M0BV2gAcvzLgYKq6hu7wqH76BiSNvmbFZAt5NehZfpGFJYxS3lXuTnONnHRr1iyAyW2mZhspv16jGZm4a71zKLfTs0DkEWRAb88=; path=/; Httponly; SameSite=Strict'
    }
    response = requests.request("POST", url, headers=headers)


    # assert response.status_code == 200
