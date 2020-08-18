
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('note/', views.note_new, name='note'),
    path('view-note/<pk>',views.note_old, name="view-note"),
    path('note/<pk>',views.note_old, name='note-old'),
    path('all-notes/',views.all_notes.as_view(),name="all-notes"),
]