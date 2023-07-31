from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("world/", views.get_world_news, name="world"),
    path("nation/", views.get_nation_news, name="nation"),
    path("business/", views.get_business_news, name="business"),
    path("technology/", views.get_technology_news, name="technology"),
    path("entertainment/", views.get_entertainment_news, name="entertainment"),
    path("sports/", views.get_sports_news, name="sport"),
    path("science/", views.get_science_news, name="science"),
    path("health/", views.get_health_news, name="health"),
]
