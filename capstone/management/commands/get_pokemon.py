from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
import json
from ...models import Pokemon

class Command(BaseCommand):
    help = "Retrieves Pokemon info from API"

    def handle(self, *args, **kwargs):
    
        x = 1
        while x <= 150:
            x = x + 1
            with open(f"/usr/share/edx/project5/project5/data/{x}") as json_file:
                pokemon_info = json.load(json_file)
                #pokemon name
                name = pokemon_info["name"]
                print(f"Name: {name}")              
                # api link for description, colour
                species_api = pokemon_info["species"]["url"]
                print(species_api)              
                #default sprite
                default_sprite = pokemon_info["sprites"]["front_default"]
                print(f"Default: {default_sprite}")
                #shiny sprite
                shiny_sprite = pokemon_info["sprites"]["front_shiny"]
                print(f"Shiny: {shiny_sprite}")
                #types
                main_type = pokemon_info["types"][0]["type"]["name"]
                print(f"Main Type: {main_type}") 

                try:                                                  
                    secondary_type = pokemon_info["types"][1]["type"]["name"]              
                    print(f"Secondary Type: {secondary_type}")
                except IndexError:
                    secondary_type = "None"
                    print("No secondary type")
               
                # use species api link for other things
                api_query = requests.get(f"{species_api}")
                if api_query.status_code != 200:
                    raise Exception("Unable to reach Poke API")
                else: 
                    species_info = api_query.json()
                    #color
                    color = species_info["color"]["name"]
                    print(f"Color: {color}")
                    #egg_group
                    main_egg_group = species_info["egg_groups"][0]["name"]
                    print(main_egg_group)
                    
                    #secondary_egg_group
                    try:
                        secondary_egg_group = species_info["egg_groups"][1]["name"]           
                        print(f"Secondary Egg Group: {secondary_egg_group}")
                    except IndexError:
                        secondary_egg_group = "None"
                        print("No secondary egg group")
                                          
                    #evolves_from
                    try:
                        evolves_from_pokemon = species_info["evolves_from_species"]["name"]
                        print(f"Evolves from: {evolves_from_pokemon}")
                    except TypeError:
                        evolves_from_pokemon = "None"
                        print("Doesn't evolve from anything")
                    
                    #description
                    description = species_info["flavor_text_entries"][0]["flavor_text"]
                    print(f"Description: {description}")
                    #habitat
                    habitat = species_info["habitat"]["name"]
                    print(f"Found in: {habitat}")
                    #id number
                    number = species_info["id"]
                    print(f"ID: {number}")
                    #shape
                    shape = species_info["shape"]["name"]
                    print(f"Shape: {shape}")
                    #default legs
                    legs = "0"
                    
                    Pokemon.objects.create(
                    pokemon_id = number,
                    name = name,
                    description = description,
                    shape = shape,
                    main_color = color,
                    egg_group = main_egg_group,
                    secondary_egg_group = secondary_egg_group,
                    habitat = habitat,
                    img = default_sprite,
                    shiny_img = shiny_sprite,
                    evolves_from = evolves_from_pokemon,
                    main_type = main_type,
                    secondary_type = secondary_type,
                    legs = legs)


                    
