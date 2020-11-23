from django.core.management.base import BaseCommand
from django.forms.models import model_to_dict
from django.utils import timezone
import requests
import json
from ...models import Pokemon
import random

class Command(BaseCommand):
    help = "Pokemon practice"

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
    
    all_pokemon = Pokemon.objects.all()
    
    def get_question(self):

        questions = {
                    "shape":"Is your chosen Pokemon '' shaped?",
                    "main_color":"Is your chosen Pokemon ''?",
                    "habitat":"Is your chosen Pokemon found in/on/around the '' areas?",  
                    "has_evolved":"Has your chosen Pokemon evolved?",    
                    "main_type":"Is your chosen Pokemon '' type?",
                    "ears":"Does your chosen Pokemon have any visible ears?",
                    "more_than_two_legs":"Does your chosen Pokemon have 2 or more legs?",
                    "horns":"Does your chosen Pokemon have horns?",
                    "tail":"Does your chosen Pokemon have a tail?",
                    "fins":"Does your chosen Pokemon have fins?",
                    "wings":"Does your chosen Pokemon have wings?",
                    "beak":"Does your chosen Pokemon have a beak?"
                    }

        remaining_questions = self.remaining_questions
        if len(remaining_questions) <= 0:
            print("out of questions")
        else:
            # choose a question from the remaining questions
            remainder = random.choice(remaining_questions)
            question_type = remainder
            question = questions[remainder]

            if question_type == "main_color":
                list_of_values = self.colors 
                main_color = random.choice(list_of_values)
                full_question = question.replace("''", main_color)
                value = main_color
                
            elif question_type == "habitat":
                list_of_values = self.habitats
                habitat = random.choice(list_of_values)
                full_question = question.replace("''", habitat)
                value = habitat

            elif question_type == "shape":
                list_of_values = self.shapes
                shape = random.choice(list_of_values)
                full_question = question.replace("''", shape)
                value = shape

            elif question_type == "main_type": 
                list_of_values = self.types
                poke_type = random.choice(list_of_values)        
                full_question = question.replace("''", poke_type)
                value = poke_type
            
            else: 
            
                full_question = question
                # the boolean fields don't have lists
                value = None
                list_of_values = None

            question = [question_type, full_question, value, list_of_values]

            return question
 
    def remove_question(self, question_type):
        self.remaining_questions.remove(question_type)
 
    def narrow_down(self):
        # un"self" a bunch of stuff..
        all_pokemon = self.all_pokemon
        player_choice = self.player_choice           
    
        # add each id
        output_pokemon = {}
        for pokemon in all_pokemon:
            output_pokemon[pokemon.id] = pokemon
        
        for pokemon in all_pokemon:
            #print(str(player_choice['more_than_two_legs']).lower())
            #print(str(pokemon.more_than_two_legs).lower())
            # shape         
            try:
                if player_choice['shape'] and (str(player_choice['shape']).lower() != str(pokemon.shape).lower()):
                    #print(f"[INFO] ({pokemon.shape}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
                
            except Exception as e:
                print(e)
            
            # main color
            try:
                if player_choice['main_color'] and (str(player_choice['main_color']).lower() != str(pokemon.main_color).lower()):
                    #print(f"[INFO] ({pokemon.main_color}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
            
            # habitat    
            try:
                if player_choice['habitat'] and (str(player_choice['habitat']).lower() != str(pokemon.habitat).lower()):
                    #print(f"[INFO] ({pokemon.habitat}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass                                       
            except Exception as e:
                print(e)   
                                          
            # type
            try:
                if player_choice['main_type'] and (str(player_choice['main_type']).lower() != str(pokemon.main_type).lower()):
                    #print(f"[INFO] ({pokemon.main_type}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
                    #print(output_pokemon[pokemon.id])                 
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # evolves i.e has this pokemon evolved from something else, like you know - as basic pokemon?
            try:
                # if there is a choice at all
                if player_choice['has_evolved'] is not None:
                    #if the choice is false
                    if player_choice['has_evolved'] != True:
                        #print(f"[Warning] {pokemon.evolves_from} evolves into {pokemon.name}")
                        if str(pokemon.evolves_from) != "None":
                            #print(output_pokemon[pokemon.id])
                            del output_pokemon[pokemon.id]                
                    # if the choice is true
                    else:
                        #print(f"[INFO] {pokemon.evolves_from}/{pokemon.name}")
                        if str(pokemon.evolves_from) == "None":
                            del output_pokemon[pokemon.id]
                else:
                    pass
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # ears
            try:
                if player_choice['ears'] and (str(player_choice['ears']).lower() != str(pokemon.ears).lower()):
                    #print(str(player_choice['ears']).lower())
                    #print(str(pokemon.ears).lower())
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
   
            # two legs
            try:
                #print("error 1")
                if player_choice['more_than_two_legs'] and (str(player_choice['more_than_two_legs']).lower() != str(pokemon.more_than_two_legs).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                #print("error 2")               
                pass
            except Exception as e:
                print(e)                        
               
            # horns
            try:
                if player_choice['horns'] and (str(player_choice['horns']).lower() != str(pokemon.horns).lower()):
                    #print(f"[INFO] ({pokemon.horns}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)               
               
            # tail 
            try:
                if player_choice['tail'] and (str(player_choice['tail']).lower() != str(pokemon.tail).lower()):
                    #print(f"[INFO] ({pokemon.tail}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e) 
               
            # fins 
            try:
                if player_choice['fins'] and (str(player_choice['fins']).lower() != str(pokemon.fins).lower()):
                    #print(f"[INFO] ({pokemon.fins}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
            
            # wings
            try:
                if player_choice['wings'] and (str(player_choice['wings']).lower() != str(pokemon.wings).lower()):
                    #print(str(player_choice['wings']).lower())
                    #print(str(pokemon.wings).lower())
                    #print(f"[INFO] ({pokemon.wings}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e) 
           
            # beak
            try:
                if player_choice['beak'] and (str(player_choice['beak']).lower() != str(pokemon.beak).lower()):
                    #print(f"[INFO] ({pokemon.wings}) - {pokemon.name}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
                
        #print(f"{len(output_pokemon)} in this list")        
        if len(output_pokemon) == 1: 
            print("is this your pokemon?")
        #print(len(output_pokemon))
        return output_pokemon

    def get_response(self):
        
        responses = [
                    "Hmm..let me think on that", 
                    "Ah-ha, we are getting somewhere", 
                    "I think I'm getting closer to the answer!", 
                    "Oooh, we are narrowing it down...",
                    "Getting there!",
                    "Just a couple more questions"
                    ]                    
        response = random.choice(responses) 
        return response     
    
    def handle(self, *args, **kwargs): 
        
        win = False
        while win == False:
        
            question = self.get_question()
            if question:        
                question_type = question[0]
                full_question = question[1]
                value = question[2]
                list_of_values = question[3]
                print(full_question)
                answer = input("y / n / unsure\n")

                if answer == "y":
                    try:
                        #print(self.get_response())
                        if list_of_values is not None:
                            # change player choice value
                            self.player_choice[question_type] = value
                            self.remove_question(question_type)
                            #print(f"changing player {value} to {player_choice[question_type]} and removing question") 
                        else: 
                            # for the boolean questions, make True
                            self.player_choice[question_type] = True
                            self.remove_question(question_type)
                    except Exception as e:
                        print(e) 


                        
                elif answer == "n":       
                    #print(self.get_response())      
                    try:
                        # if it is NOT a boolean question
                        if list_of_values is not None:
                            list_of_values.remove(value) 
                            list_items_left = len(list_of_values)  
                            self.player_choice[question_type] = None
                            if list_items_left <= 0: 
                                print(f"Well we are going to have to start again, as I've run out of ideas...")
                                break
                        # if it IS a boolean
                        else:
                            self.player_choice[question_type] = False
                            self.remove_question(question_type)
                    except Exception as e:
                        print(e)
                elif answer == "unsure":  
                    print("I need to find out more...")  
                    # carry on asking, do nothing      
                    pass

                else: 
                    print("Not what I asked for...let's try again...")            
        
            output_pokemon = self.narrow_down()
            print("-" * 15)        
            for pokemon in output_pokemon:            
                print(f"{output_pokemon[pokemon].id} - {output_pokemon[pokemon].name}")
            print("-" * 15)
            print(self.player_choice)
                
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
                
