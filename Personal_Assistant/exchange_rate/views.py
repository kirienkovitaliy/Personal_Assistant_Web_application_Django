# app/views.py

from datetime import date
from typing import Dict, Any

from django.shortcuts import render
import requests

from statistic_war.views import get_data


def get_exchange_rates(request) -> render:
    """
    View function to fetch and display the exchange rates from PrivatBank API.

    This function fetches the exchange rates for USD and EUR from PrivatBank API
    for the current date and displays them on the index.html template along with
    other data obtained from the 'get_data' function in the 'statistic_war' app.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        render: The rendered HTML template with exchange rates and other data.
    """
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date.today().strftime('%d.%m.%Y')}"
    response = requests.get(url)
    response_json = response.json()

    exchange_rates: Dict[str, Dict[str, Dict[str, float]]] = {}
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
