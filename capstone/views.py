from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
import requests
import random
import csv

## TODO
# add pokemon the database
# random pokemon page


def index(request):
    # query the poke API with kanto pokedex as parameter
    #f = open("pokemon.csv", "a")
    #f.write("ID_No, Name, Shiny, Default, \n")
    
    
    x = 1
    api_query = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(x))
    if api_query.status_code != 200:
        raise Exception("Unable to reach Poke API")
    else: 
        pokemon_info = api_query.json()
        # for pokemon name
        name = pokemon_info["name"]
        print(f"Name: {name}")
        # api link for description, colour
        species_api = pokemon_info["species"]["url"]
        print(species_api)
        # for default sprite
        default_sprite = pokemon_info["sprites"]["front_default"]
        print(f"Default: {default_sprite}")
        # for shiny sprite
        shiny_sprite = pokemon_info["sprites"]["front_shiny"]
        print(f"Shiny: {shiny_sprite}")
        # for types
        main_type = pokemon_info["types"][0]["type"]["name"]
        secondary_type = pokemon_info["types"][1]["type"]["name"]
        print(f"Type(s): {main_type}, {secondary_type}")

        # use species api link for other things
        api_query_2 = requests.get(f"{species_api}")
        if api_query_2.status_code != 200:
            raise Exception("Unable to reach Poke API")
        else: 
            species_info = api_query_2.json()
            color = species_info["color"]["name"]
            print(f"Color: {color}")
            main_egg_group = species_info["egg_groups"][0]["name"]
            secondary_egg_group = species_info["egg_groups"][1]["name"]
            print(f"Egg Group(s): {main_egg_group}, {secondary_egg_group}")
            evolves_from_pokemon = species_info["evolves_from_species"]
            print(f"Evolves from: {evolves_from_pokemon}")
            description = species_info["flavor_text_entries"][0]["flavor_text"]
            print(f"Description: {description}")
            habitat = species_info["habitat"]["name"]
            print(f"Found in: {habitat}")
            number = species_info["id"]
            print(f"ID: {number}")
            shape = species_info["shape"]["name"]
            print(f"Shape: {shape}")



        #f.write( + ", " + shiny + ", " + default + "\n")  



        '''
        pokemon_id
    
        name
        description
        shape
        main_color
        egg_group
        habitat
        img
        shiny_img
        ears
        legs
        horns
        tail
        #can evolve
        #evolved from another pokemon
        #type
        '''
        return render(request, "capstone/index.html", {
           # "pokemon_list": pokemon_list
        })

def who_is_that_pokemon(request):    
    return render(request, "capstone/who.html")    
        
def search(request): 
    if request.method == "POST":
        # get value from form   
        pokemon_input = request.POST["search_input"]           
        print(pokemon_input)
        # format for part compare
        like_pokemon_input = "%{}%".format(pokemon_input)

        return render(request, "capstone/search.html")
    else:    
        return render(request, "capstone/search.html")          

def randomise(request):
    if request.method == "GET":
        #takes a random choice from all of the entries and redirects to it
        #select number from 1-151
        random_choice = randrange(151)
        print(random_choice)
        
        return HttpResponseRedirect(randomised_choice)
    else:
        return render(request, "capstone/index.html") 


def todolist(request):
    return render(request, "capstone/todolist.html")

