from django.urls import path

from .views import get_files, upload_file, delete_file


app_name = "file_app"

urlpatterns = [
    path("", get_files, name="files"),
    path("upload/", upload_file, name="upload"),
    path("delete/<int:id>/", delete_file, name="delete"),
]