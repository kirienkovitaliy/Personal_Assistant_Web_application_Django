from django.urls import path

from .views import AddNote, ShowNote, AddTag, NoteHome


urlpatterns = [
    path('', NoteHome.as_view(), name='note_home'),
    path('add', AddNote.as_view(), name='add_note'),
    path('add_tag', AddTag.as_view(), name='add_tag'),
    path('note/<int:note_id>', ShowNote.as_view(), name='note_detail'),

]