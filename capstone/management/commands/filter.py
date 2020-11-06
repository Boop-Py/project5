from django.core.management.base import BaseCommand
from django.forms.models import model_to_dict
from django.utils import timezone
import requests
import json
from ...models import Pokemon
import random

class Command(BaseCommand):
    help = "Pokemon practice"
    TRUE = "y"

    # change all these to a list of dicts.. 
    player_choice = {
            "shape":"wings",
            "main_color":"yellow",
            "habitat":"grassland",
            "type":"water",
            "has_evolved":False,
            "ears":True,
            "more_than_two_legs":True,
            "horns":True,
            "tail":True,
            "fins":True,
            "wings":True,
            "beak":True
            }
    
    # create 12 seperate lists for each choice
    #player_choice.len

    pokemon_possibilities = [[] for i in range(12)]
    all_pokemon = Pokemon.objects.all()
    
    #queryset_pokemon = model_to_dict(all_pokemon)
    
        
    def handle(self, *args, **kwargs): 
        pokemon_possibilities = self.pokemon_possibilities
        all_pokemon = self.all_pokemon
        player_choice = self.player_choice        
        
        
        # Bibble make new object
        self.output_pokemon = {}
        for pokemon in all_pokemon:
            #print(pokemon.id)
            self.output_pokemon[pokemon.id] = pokemon
        
        i = 0
        #for index in range(len(player_choice)):
        #    for key in player_choice[index]:
        #        choice = player_choice[index][key]
        #        if choice is not None:
                    # loop through each pokemon
        for pokemon in all_pokemon:
        
            # Working nicely
            """
            try:
                ears_choice = str(player_choice['ears']).lower()
                pokemon_ears = str(pokemon.ears).lower()
                
                if pokemon_ears != ears_choice:
                    del self.output_pokemon[pokemon.id]
                    print(f"[ERROR] Remove [{pokemon.id}] - {pokemon.name} - ears: {pokemon.ears}")     
            except:
                print("There was an error pokemon man/lady/girl/person")
            """
            
            # Ears
            try:
                if str(player_choice['ears']).lower() != str(pokemon.ears).lower():
                    del self.output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
                    
            # more_than_two_legs
            try:
                if str(player_choice['more_than_two_legs']).lower() != str(pokemon.more_than_two_legs).lower():
                    del self.output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # evolves i.e has this pokemon evolved from something else, like you know - as basic pokemon?
            try:
                if player_choice['has_evolved'] != True:
                    print(f"[Warning] ({pokemon.evolves_from}) Remove non-basic pokemon {pokemon.name} doesn't evolve")
                    if str(pokemon.evolves_from) != "None":
                        del self.output_pokemon[pokemon.id]
                    
                else:
                    print(f"[INFO] ({pokemon.evolves_from}) Remove basic pokemon {pokemon.name} evolves from {pokemon.evolves_from}")
                    if str(pokemon.evolves_from) == "None":
                        del self.output_pokemon[pokemon.id]
                    
            except KeyError:
                pass
            except Exception as e:
                print(e)
            
            
            
            try:
                """
                if pokemon.shape == choice:    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)

                elif pokemon.main_color == choice:    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)

                elif pokemon.habitat == choice:    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)

                elif pokemon.main_type == choice:    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)
                        
                #4
                elif pokemon.evolves_from == choice:                                  
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)
                """
                #print(f"{ str(pokemon.ears).lower()}/{choice}/{pokemon.name}")
                #if str(pokemon.ears).lower() != str(choice).lower(): 
                    #pass
                
                
                
                
                
                
                
                
                

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

                """
                #print(f"{ str(pokemon.more_than_two_legs).lower()}/{choice}/{pokemon.name}")
                if str(pokemon.more_than_two_legs).lower() == str(choice).lower(): 
                    #
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        #print(f"{pokemon.ears}/{choice}/{pokemon.name}")
                        pokemon_possibilities[i].append(pokemon.name)
                """
                '''
                elif str(pokemon.more_than_two_legs).lower() == str(choice).lower():  
                    print(f"{ str(pokemon.more_than_two_legs).lower()}/{choice}/{pokemon.name}")
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)
               
                elif str(pokemon.horns).lower() == str(choice).lower():    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)
                        
                elif str(pokemon.tail).lower() == str(choice).lower():    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)    

                elif str(pokemon.fins).lower() == str(choice).lower():    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)

                elif str(pokemon.wings).lower() == str(choice).lower():    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id)
                        
                elif str(pokemon.beak).lower() == str(choice).lower():    
                    if pokemon.pokemon_id not in pokemon_possibilities[i]:
                        pokemon_possibilities[i].append(pokemon.pokemon_id) 
                '''    
                
            except Exception as e:
                print(e)
                #pass
                 
            i = i + 1
        
        #del self.output_pokemon[20]
        #del self.output_pokemon[151]
        print("-" * 15)
        #print(self.output_pokemon)
        
        for pokemon in self.output_pokemon:
            print(f"{self.output_pokemon[pokemon].id} - {self.output_pokemon[pokemon].name}")
        #print(pokemon_possibilities)
        #print(json.dumps(all_pokemon.values(), indent=4)
        #print(pokemon_possibilities[6])
        #print(pokemon_possibilities[7])  
        #print(pokemon_possibilities[8])
        #print(pokemon_possibilities[9])
        #print(pokemon_possibilities[10])
        #print(pokemon_possibilities[11])
        # get a list of intersections of the sublists. these are the narrowed down pokemon