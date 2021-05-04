from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/ed_<str:name>", views.edit, name="edit"),
    path("wiki/new", views.new, name="new"),
    path('wiki/randomArt', views.random, name='random'),
    path('wiki/search', views.search, name='search'),
    path("<str:name>", views.greet, name="greet"),
    path("wiki/<str:name>", views.greet, name="greet")
]
