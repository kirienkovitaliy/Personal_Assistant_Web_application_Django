import requests
from django.shortcuts import render
from datetime import date


def home(request):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date.today().strftime("%d.%m.%Y")}'
    response = requests.get(url)
    response_json = response.json()

    exchange_rates = {}
    for rate in response_json['exchangeRate']:
        currency = rate['currency']
        if currency in ['USD', 'EUR']:
            if date.today().strftime("%d.%m.%Y") not in exchange_rates:
                exchange_rates[date.today().strftime("%d.%m.%Y")] = {}
            exchange_rates[date.today().strftime("%d.%m.%Y")][currency] = {'sale': float(rate['saleRate']),
                                                                           'purchase': float(rate['purchaseRate'])}

    return render(request, "app/base.html", {"exchange_rates": exchange_rates})
