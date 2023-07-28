"""
URL configuration for Personal_Assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from addressbook.views import ContactsHome
from exchange_rate import views
from statistic_war.views import get_spider_data

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home", ContactsHome.as_view(), name='home'),
    path('', views.home, name='home'),
    path('addressbook/', include('addressbook.urls')),
    path("file/", include("file_app.urls")),
    path("users/", include("users.urls")),
    path('vtraty_pidariv/', get_spider_data, name='get_spider_data'),
    path("", include("app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
