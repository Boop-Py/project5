from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
import json
from ...models import Pokemon
import random

class Command(BaseCommand):
    help = "Pokemon practice"

    player_choice = {
            "name":None,
            "shape":"wings",
            "main_color":"blue",
            "habitat":None,
            "evolves":None,
            "type":None,
            "ears":None,
            "legs":None,
            "horns":None,
            "tail":None,
            "fins":None,
            "wings":True,
            "beak":None
            }
    
    # start off with all pokemon as a possibility
    pokemon_possibilities = []
    all_pokemon = Pokemon.objects.all()

    for each_pokemon in all_pokemon:  
        id_no = each_pokemon.pokemon_id
        pokemon_possibilities.append(id_no)           
      
    def handle(self, *args, **kwargs): 
        pokemon_possibilities = self.pokemon_possibilities
        all_pokemon = self.all_pokemon
        player_choice = self.player_choice        
        values = player_choice.values()
        
         
        for choice in values:  
            # for those in player choice with given values, eg "habitat"
            if choice is not None:                              
                # loop through each pokemon
                for pokemon in all_pokemon: 
                    #attribute = f"{str(pokemon)}.{question_type}"
                    ########## somehow get "main color" as a variable- value
                    if pokemon.shape != choice:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.main_color != choice:
                        pokemon_possibilities.remove(pokemon.pokemon_id)   
                    if pokemon.habitat != choice:
                        pokemon_possibilities.remove(pokemon.pokemon_id)    
                        
                        ### sort out 'evolves'
                    if pokemon.evolves != None:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                        ###
                        
                    if pokemon.type != choice:
                        pokemon_possibilities.remove(pokemon.pokemon_id)    
                    if pokemon.ears != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.legs != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.horns != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.tail != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.fins != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.wings != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    if pokemon.beak != True:
                        pokemon_possibilities.remove(pokemon.pokemon_id)
                    else: 
                        print(f"pokemon {pokemon.pokemon_id} is a possibility")
        
        



                    # if boolean questions have ANYTHING in their values "not none"
                    # elif a boolean is True...

