from django.urls import path

from . import views


app_name = "news"

urlpatterns = [
    path("world/", views.get_world_news, name="world_news"),
    path("nation/", views.get_nation_news, name="nation_news"),
    path("business/", views.get_business_news, name="business_news"),
    path("technology/", views.get_technology_news, name="technology_news"),
    path("entertainment/", views.get_entertainment_news, name="entertainment_news"),
    path("sports/", views.get_sports_news, name="sports_news"),
    path("science/", views.get_science_news, name="science_news"),
    path("health/", views.get_health_news, name="health_news"),
]