from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("who_is_that_pokemon", views.who_is_that_pokemon, name="who_is_that_pokemon"),
    path("todolist", views.todolist, name="todolist"),
    path("search", views.search, name="search"),
    path("pokemon/<str:pokemon_id>", views.pokemon, name="pokemon"),
    path("randomise", views.randomise, name="randomise")  
]