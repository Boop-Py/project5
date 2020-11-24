from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("todolist", views.todolist, name="todolist"),
    path("search", views.search, name="search"),
    path("pokemon/<str:pokemon_id>", views.pokemon, name="pokemon"),
    path("randomise", views.randomise, name="randomise"), 
    path("guessing-game", views.guessing_game, name="guessing_game"),
    path("battle", views.battle, name="battle")     
]