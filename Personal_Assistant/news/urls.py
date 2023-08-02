from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("world/", views.get_news_by_category, {"category": "world"}, name="world"),
    path(
        "nation/",
        views.get_news_by_category,
        {"category": "nation"},
        name="nation",
    ),
    path(
        "business/",
        views.get_news_by_category,
        {"category": "business"},
        name="business",
    ),
    path(
        "technology/",
        views.get_news_by_category,
        {"category": "technology"},
        name="technology",
    ),
    path(
        "entertainment/",
        views.get_news_by_category,
        {"category": "entertainment"},
        name="entertainment",
    ),
    path(
        "sports/",
        views.get_news_by_category,
        {"category": "sports"},
        name="sport",
    ),
    path(
        "science/",
        views.get_news_by_category,
        {"category": "science"},
        name="science",
    ),
    path(
        "health/",
        views.get_news_by_category,
        {"category": "health"},
        name="health",
    ),
]
