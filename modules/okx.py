import json
import random

import requests

from settings import (
    OKX_API_KEY,
    OKX_API_PASSPHRASE,
    TRANSFER_AMOUNT_RANGE,
    TRANSFER_CHAIN,
    TRANSFER_CURRENCY,
)
from utils import sign_request

OKX_BASE_API_URL = "https://www.okx.com"  # базовый URL для запросов к API OKX


def withdraw(recipient: str):
    method = "POST"  # метод http запроса
    request_path = "/api/v5/asset/withdrawal"  # путь запроса к API OKX для перевода токенов

    amount_to_transfer = random.uniform(
        TRANSFER_AMOUNT_RANGE[0], TRANSFER_AMOUNT_RANGE[1]
    )  # рандомное количество токенов для перевода

    # формируем тело http запроса
    body = {
        "ccy": TRANSFER_CURRENCY,
        "amt": str(amount_to_transfer),
        "dest": "4",  # 4 - кошелек, 3 - биржа
        "chain": f"{TRANSFER_CURRENCY}-{TRANSFER_CHAIN}",
        "toAddr": recipient,  # адрес кошелька куда будем переводить
        "walletType": "private",
    }

    # подписываем запрос через созданную функцию sign_request
    timestamp, base64_signature = sign_request(
        method=method, request_path=request_path, body=json.dumps(body)
    )

    # формируем заголовки http запроса
    headers = {
        "OK-ACCESS-KEY": OKX_API_KEY,
        "OK-ACCESS-SIGN": base64_signature,
        "OK-ACCESS-PASSPHRASE": OKX_API_PASSPHRASE,
        "OK-ACCESS-TIMESTAMP": timestamp,
    }

    # формируем http запрос к API OKX и выполняем его
    response = requests.request(
        method=method,
        url=OKX_BASE_API_URL + request_path,
        headers=headers,
        json=body,
    )
    # получаем ответ от OKX API в JSON формате
    response_data = response.json()

    if response_data.get("code", "") == "0":
        print(
            f"Инициировал перевод | {amount_to_transfer} {TRANSFER_CURRENCY} | {recipient}"
        )
    else:
        print(f"Не удалось инициировать перевод | {response_data.get('msg', 'No message provided')}")

    return response_data
