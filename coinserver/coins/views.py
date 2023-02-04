from _decimal import Decimal

from django.shortcuts import render
import requests

from .utils import format_currency


def home(request):
    response = requests.get("https://api.coincap.io/v2/assets/")
    coins_data = response.json()['data']

    for coin in coins_data:
        coin['image'] = "https://coinicons-api.vercel.app/api/icon/{}".format(coin['symbol'].lower())
        coin['priceUsd'] = format_currency(coin['priceUsd'])
        coin['marketCapUsd'] = format_currency(coin['marketCapUsd'])
        coin['volumeUsd24Hr'] = format_currency(coin['volumeUsd24Hr'], is_currency=False)
        coin['changePercent24Hr'] = round(Decimal(coin['changePercent24Hr']), 3)

    return render(request, 'coins/home.html', {
        'coins_list': coins_data
    })


def detail(request, coin_id):
    prices = []
    timestamps = []

    coin_data = requests.get("https://api.coincap.io/v2/assets/{}".format(coin_id))
    variation_data = requests.get("https://api.coincap.io/v2/assets/{}/history?interval=d1".format(coin_id))

    coin = coin_data.json()['data']
    coin['image'] = "https://coinicons-api.vercel.app/api/icon/{}".format(coin['symbol'].lower())
    coin['priceUsd'] = format_currency(coin['priceUsd'])
    coin['marketCapUsd'] = format_currency(coin['marketCapUsd'])
    coin['volumeUsd24Hr'] = format_currency(coin['volumeUsd24Hr'], is_currency=False)
    coin['changePercent24Hr'] = round(Decimal(coin['changePercent24Hr']), 3)
    coin['supply'] = format_currency(coin['supply'], is_currency=False)
    variations = variation_data.json()['data']

    for variation in variations:
        prices.append(variation['priceUsd'])
        timestamps.append(variation['time'])

    return render(request, 'coins/detail.html', {
        'coindata': coin,
        'prices': prices,
        'timestamps': timestamps
    })
