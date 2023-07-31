from django.urls import path

from .views import AddNote, ShowNote, AddTag, NoteHome, EditNote, DeleteNote

app_name = "notebook"

urlpatterns = [
    path("", NoteHome.as_view(), name="note_home"),
    path("add", AddNote.as_view(), name="add_note"),
    path("add_tag", AddTag.as_view(), name="add_tag"),
    path("note/<int:pk>", ShowNote.as_view(), name="note_detail"),
    path("edit/<int:pk>", EditNote.as_view(), name="edit_note"),
    path("delete/<int:pk>", DeleteNote.as_view(), name="delete_note"),
]
