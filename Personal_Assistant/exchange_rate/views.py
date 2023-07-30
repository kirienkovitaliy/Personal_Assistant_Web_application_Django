from datetime import date

from django.shortcuts import render
import requests

from statistic_war.views import get_data


def get_exchange_rates(request):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date.today().strftime('%d.%m.%Y')}"
    response = requests.get(url)
    response_json = response.json()

    exchange_rates = {}
    for rate in response_json["exchangeRate"]:
        currency = rate["currency"]
        if currency in ["USD", "EUR"]:
            if date.today().strftime("%d.%m.%Y") not in exchange_rates:
                exchange_rates[date.today().strftime("%d.%m.%Y")] = {}
            exchange_rates[date.today().strftime("%d.%m.%Y")][currency] = {
                "sale": float(rate["saleRate"]),
                "purchase": float(rate["purchaseRate"]),
            }

    return render(
        request,
        "app/index.html",
        {"exchange_rates": exchange_rates, "data": get_data()},
    )
