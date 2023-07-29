from datetime import datetime
import re

import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_url():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ["/"]
    prefix = "/month.php?month="
    for tag_a in content:
        urls.append(prefix + re.search(r"\d{4}-\d{2}", tag_a["href"]).group())
    return [urls[0]]


def spider(urls):
    data = []
    rows_to_fetch = 1

    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')

        for element in content:
            date = element.find('span', attrs={"class": "black"}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
            except ValueError:
                print(f"error for {date}")
                continue

            existing_item = next((item for item in data if item["date"] == date), None)
            if existing_item:
                losses = element.find('div').find('div').find('ul')
                for l in losses:
                    title, quantity, *rest = l.text.split('—')
                    title = title.strip()
                    quantity = re.search(r"\d+", quantity).group()
                    existing_item.update({title: quantity})
            else:
                result = {"Дата": date}
                losses = element.find('div').find('div').find('ul')
                for l in losses:
                    title, quantity, *rest = l.text.split('—')
                    title = title.strip()
                    quantity = re.search(r"\d+", quantity).group()
                    result.update({title: quantity})
                data.append(result)
            if len(data) == rows_to_fetch:
                break

    return data


@require_http_methods(["GET"])
def get_spider_data(request):
    urls_for_parser = get_url()
    r = spider(urls_for_parser)
    return render(request, 'statistic_war/stat.html', {'data': r})


def get_data():
    urls_for_parser = get_url()
    r = spider(urls_for_parser)
    return r
