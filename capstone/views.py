from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.shortcuts import render
from .models import Pokemon
import requests
import random
import json
import re


## TODO
# https://nostalgic-css.github.io/NES.css/#
# make pokemon game
# fix the weird descriptions
# input tails, legs, horns, tail

all_pokemon = Pokemon.objects.all()

colors = [
        "black", "blue", "brown", "gray", "green", "pink", "purple", "red", "white", "yellow"
        ] 

habitats = [
            "cave", "forest", "grassland", "mountain", "rare", "rough-terrain", "water", "urban"
            ] 

shapes = [
        "ball", "squiggle", "fish", "arms", "blob", "upright", "legs", "quadruped", "wings",  "tentacles", "heads", "humanoid", "bug-wings", "armor"
        ]

types = [
        "normal", "flying", "ground", "bug", "steel", "water", "ice", "dark", "fighting", "poison", "rock", "ghost", "fire", "grass", "psychic", "dragon", "fairy"
        ]

remaining_questions = [
                    "shape", "main_color", "habitat", "has_evolved", "main_type", "ears", "more_than_two_legs", "horns", "tail", "fins", "wings", "beak"
                    ]

player_choice = {
        "shape":None,
        "main_color":None,
        "habitat":None,
        "main_type":None,
        "has_evolved":None,
        "ears":None,
        "more_than_two_legs":None,
        "horns":None,
        "tail":None,
        "fins":None,
        "wings":None,
        "beak":None
        }

def index(request):  
    pokemon_list = Pokemon.objects.all()
    return render(request, "capstone/index.html", {
        "pokemon_list": pokemon_list
    })

def search(request): 
    if request.method == "POST": 
        # all pokemon
        pokemon_list = all_pokemon
        # get value from form   
        raw_pokemon_input = request.POST["search_input"]    
        print(raw_pokemon_input)
        pokemon_input = raw_pokemon_input.lower()
        print(pokemon_input)
        # check if anything matches the input
        target_pokemon = Pokemon.objects.filter(name=pokemon_input).first()
        
        if target_pokemon is not None:  
                   
            target_pokemon_id = target_pokemon.pokemon_id
            print(target_pokemon_id)          
            # redirect to that page if it is an exact match
            return HttpResponseRedirect("pokemon/" + str(target_pokemon_id))
        
        elif target_pokemon is None: 
            # presents a list of all titles with that substring
            # search where pokemon is like the input
            like_pokemon_list = Pokemon.objects.filter(name__contains=pokemon_input)
            print(like_pokemon_list)

            return render(request, "capstone/index.html", {
            "pokemon_list": like_pokemon_list
            })
            
        else: 
            return render(request, "capstone/search.html")
    else:    
        return render(request, "capstone/search.html")          

def pokemon(request, pokemon_id):
    target_pokemon = Pokemon.objects.filter(pokemon_id=pokemon_id).first()
    return render(request, "capstone/pokemon.html", {
        "pokemon_info": target_pokemon
    })
    
def randomise(request):
    if request.method == "GET":
        #takes a random choice from all of the entries and redirects to it
        #select number from 1-151
        random_number = random.randint(1,152)
        print(random_number)       
        return HttpResponseRedirect("pokemon/" + str(random_number))
    else:
        return render(request, "capstone/index.html") 

def todolist(request):
    return render(request, "capstone/todolist.html")
     
def battle(request):           
    return render(request, "capstone/battle.html")

def ai_pokemon_choice(request):
    random_number = random.randint(1,152)
    print(random_number)
    ai_choice = Pokemon.objects.filter(
                id=random_number
                )
    print(ai_choice)
    return JsonResponse({"computerSelection": ai_choice})