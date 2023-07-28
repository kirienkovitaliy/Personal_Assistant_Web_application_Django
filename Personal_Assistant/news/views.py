from django.shortcuts import render
from django.conf import settings
import requests

from json import loads


def get_world_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=world&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_nation_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=nation&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_business_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=business&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_technology_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=technology&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_entertainment_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=entertainment&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_sports_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=sports&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_science_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=science&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})


def get_health_news(request):
    response = requests.get(f"https://gnews.io/api/v4/top-headlines?country=ua&category=health&apikey={settings.GNEWS_API_KEY}&lang=uk")
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})
