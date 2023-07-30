from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("world/", views.get_news_by_category, {"category": "world"}, name="world_news"),
    path("nation/", views.get_news_by_category, {"category": "nation"}, name="nation_news"),
    path("business/", views.get_news_by_category, {"category": "business"}, name="business_news"),
    path("technology/", views.get_news_by_category, {"category": "technology"}, name="technology_news"),
    path("entertainment/", views.get_news_by_category, {"category": "entertainment"}, name="entertainment_news"),
    path("sports/", views.get_news_by_category, {"category": "sports"}, name="sports_news"),
    path("science/", views.get_news_by_category, {"category": "science"}, name="science_news"),
    path("health/", views.get_news_by_category, {"category": "health"}, name="health_news"),
]
