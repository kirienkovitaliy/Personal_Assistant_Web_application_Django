import requests
from django.conf import settings
from django.shortcuts import render


def get_news_by_category(request, category):
    """
    View to get news by category from the GNews API.

    Args:
        request (HttpRequest): The HTTP request object.
        category (str): The category of news.

    Returns:
        HttpResponse: The HTTP response with the news articles.
    """
    url = f"https://gnews.io/api/v4/top-headlines?country=ua&category={category}&apikey={settings.GNEWS_API_KEY}&lang=uk"
    response = requests.get(url)
    news = response.json()
    return render(request, "news/news.html", context={"news": news["articles"]})
