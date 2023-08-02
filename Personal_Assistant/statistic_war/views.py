from datetime import datetime
import re

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Union

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

base_url: str = "https://index.minfin.com.ua/ua/russian-invading/casualties"

CATEGORY = (
    "Особовий склад",
    "Танки",
    "ББМ",
    "Гармати",
    "РСЗВ",
    "Засоби ППО",
    "Літаки",
    "Гелікоптери",
    "Автомобілі та автоцистерни",
    "Кораблі (катери)",
    "Крилаті ракети",
    "БПЛА",
    "Спеціальна техніка",
)


def get_url() -> List[str]:
    """
    Retrieves the URLs to scrape data from.

    Returns:
        List of URLs as strings.
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.select("div[class=ajaxmonth] h4[class=normal] a")
    urls = ["/"]
    prefix = "/month.php?month="
    for tag_a in content:
        urls.append(prefix + re.search(r"\d{4}-\d{2}", tag_a["href"]).group())
    return [urls[0]]


def spider(urls: List[str]) -> List[Dict[str, Union[str, Dict[str, str]]]]:
    """
    Scrapes data from the given URLs.

    Args:
        urls: List of URLs as strings.

    Returns:
        List of dictionaries containing the scraped data.
    """
    data = []
    rows_to_fetch = 1

    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.select("ul[class=see-also] li[class=gold]")

        for element in content:
            date = element.find("span", attrs={"class": "black"}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
            except ValueError:
                print(f"error for {date}")
                continue

            existing_item = next((item for item in data if item["date"] == date), None)
            if existing_item:
                losses = element.find("div").find("div").find("ul")
                for loss in losses:
                    title, quantity, *rest = loss.text.split("—")
                    title = title.strip()
                    quantity = re.search(r"\d+", quantity).group()
                    existing_item.update({title: quantity})
            else:
                result = {"Дата": date}
                losses = element.find("div").find("div").find("ul")
                for loss in losses:
                    title, quantity, *rest = loss.text.split("—")
                    title = title.strip()
                    quantity = re.search(r"\d+", quantity).group()
                    result.update({title: quantity})
                data.append(result)
            if len(data) == rows_to_fetch:
                break

    return data


@require_http_methods(["GET"])
def get_spider_data(request) -> render:
    """
    View function to handle HTTP GET requests and return the scraped data in the template.

    Args:
        request: HTTP request object.

    Returns:
        render: HTTP response containing the template with the data.
    """
    result = get_data()
    return render(request, "statistic_war/statistic_war.html", {"data": result})


def get_data() -> List[Dict[str, Union[str, Dict[str, str]]]]:
    """
    Convenience function to retrieve the scraped data.

    Returns:
        List of dictionaries containing the scraped data.
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    response = requests.get(
        f"https://russianwarship.rip/api/v2/statistics/{current_date}"
    )
    data = response.json()["data"]["stats"]
    result = {k: v for k, v in zip(CATEGORY, data.values())}
    return result
