from django.urls import path

from . import views


app_name = "file_app"

urlpatterns = [
    path("", views.get_files, name="files"),
    path("upload/", views.upload_file, name="upload"),
    path("delete/<int:id>/", views.delete_file, name="delete"),
    path("download/<int:id>/", views.download_file, name="download"),
    path("search/", views.search_files, name="search"),
    path("image/", views.get_image_files, name="image"),
    path("audio/", views.get_audio_files, name="audio"),
    path("video/", views.get_video_files, name="video"),
    path("documents/", views.get_documents_files, name="documents"),
    path("other_files/", views.get_other_files, name="other_files"),
]