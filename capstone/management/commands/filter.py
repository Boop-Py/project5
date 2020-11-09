from django.core.management.base import BaseCommand
from django.forms.models import model_to_dict
from django.utils import timezone
import requests
import json
from ...models import Pokemon
import random

class Command(BaseCommand):
    help = "Pokemon practice"

    player_choice = {
            "shape":None,
            "main_color":"yellow",
            "habitat":"grassland",
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
    
    no_of_keys = len(player_choice)
    # create seperate lists for each key choice in dict
    pokemon_possibilities = [[] for i in range(no_of_keys)]
    all_pokemon = Pokemon.objects.all()
        
    def handle(self, *args, **kwargs): 
        pokemon_possibilities = self.pokemon_possibilities
        all_pokemon = self.all_pokemon
        player_choice = self.player_choice           
     
        # Bibble make new object
        output_pokemon = {}
        for pokemon in all_pokemon:
            output_pokemon[pokemon.id] = pokemon
        
        i = 0

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
            
            # shape         
            try:
                if str(player_choice['shape']).lower() != str(pokemon.shape).lower():
                    #print(f"[INFO] ({pokemon.shape}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
                        
            # main color
            try:
                if str(player_choice['main_color']).lower() != str(pokemon.main_color).lower():
                    #print(f"[INFO] ({pokemon.main_color}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # habitat    
            try:
                if str(player_choice['habitat']).lower() != str(pokemon.habitat).lower():
                    #print(f"[INFO] ({pokemon.habitat}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)   
                            
            # type
            try:
                if str(player_choice['main_type']).lower() != str(pokemon.main_type).lower():
                    #print(f"[INFO] ({pokemon.main_type}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # evolves i.e has this pokemon evolved from something else, like you know - as basic pokemon?
            try:
                if player_choice['has_evolved'] != True:
                    #print(f"[Warning] ({pokemon.evolves_from}) Remove non-basic pokemon {pokemon.name} doesn't evolve")
                    if str(pokemon.evolves_from) != "None":
                        del output_pokemon[pokemon.id]                
                else:
                    #print(f"[INFO] ({pokemon.evolves_from}) Remove basic pokemon {pokemon.name} evolves from {pokemon.evolves_from}")
                    if str(pokemon.evolves_from) == "None":
                        del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
    
            # ears
            try:
                if str(player_choice['ears']).lower() != str(pokemon.ears).lower():
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
   
            # more_than_two_legs
            try:
                if str(player_choice['more_than_two_legs']).lower() != str(pokemon.more_than_two_legs).lower():
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)                        
               
            # horns
            try:
                if str(player_choice['horns']).lower() != str(pokemon.horns).lower():
                    #print(f"[INFO] ({pokemon.horns}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)               
               
            # tail 
            try:
                if str(player_choice['tail']).lower() != str(pokemon.tail).lower():
                    #print(f"[INFO] ({pokemon.tail}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e) 
               
            # fins 
            try:
                if str(player_choice['fins']).lower() != str(pokemon.fins).lower():
                    #print(f"[INFO] ({pokemon.fins}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
            
            # wings
            try:
                if str(player_choice['wings']).lower() != str(pokemon.wings).lower():
                    #print(f"[INFO] ({pokemon.wings}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e) 
           
            # beak
            try:
                if str(player_choice['beak']).lower() != str(pokemon.beak).lower():
                    #print(f"[INFO] ({pokemon.wings}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)                
               
            i = i + 1

        print("-" * 15)        
        for pokemon in output_pokemon:       
            print(f"{output_pokemon[pokemon].id} - {output_pokemon[pokemon].name}")
