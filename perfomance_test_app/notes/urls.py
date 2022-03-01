from django.urls import path
from .views import *

urlpatterns = [
    path('',  notes_list, name='notes_list_url'),
    path('note/create/', NotesCreate.as_view(), name='notes_create_url'),
    path('<str:slug>/', NotesDetail.as_view(), name='notes_detail_url'),
    path('<str:slug>/update/',
         NotesUpdate.as_view(), name='notes_update_url'),
    path('<str:slug>/delete/',
         NotesDelete.as_view(), name='notes_delete_url'),
]
