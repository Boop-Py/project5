from django.core.management.base import BaseCommand
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.shortcuts import render
from ...models import Pokemon
import requests
import random
import json
import re


## TODO
# https://nostalgic-css.github.io/NES.css/#
# when "no" answered to "ears" in filter_down()

class Command(BaseCommand):

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

    def get_question(self):
    
        questions = {
                    "shape":"Is your chosen Pokemon '' shaped?",
                    "main_color":"Is your chosen Pokemon ''?",
                    "habitat":"Is your chosen Pokemon found in/on/around the '' areas?",  
                    "has_evolved":"Has your chosen Pokemon evolved before?",    
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
            
            # format the question
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
        remaining_questions = self.remaining_questions
        remaining_questions.remove(question_type)       
        return remaining_questions
        
    def narrow_down(self):
        # un"self" a bunch of stuff - not needed when used in views          
        player_choice = self.player_choice
        all_pokemon = self.all_pokemon
        
        # add each pokemon's id into a dictionary of objects - eg {146: <Pokemon: Pokemon object (146)>, 147: <Pokemon: Pokemon object (147)>}
        output_pokemon = {}
        
        for pokemon in all_pokemon:
            output_pokemon[pokemon.id] = pokemon
            
        for pokemon in all_pokemon:

            # shape         
            try:
                if player_choice['shape'] and (str(player_choice['shape']).lower() != str(pokemon.shape).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass               
            except Exception as e:
                print(e)
            
            # main color
            try:
                if player_choice['main_color'] and (str(player_choice['main_color']).lower() != str(pokemon.main_color).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)
            
            # habitat    
            try:
                if player_choice['habitat'] and (str(player_choice['habitat']).lower() != str(pokemon.habitat).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass                                       
            except Exception as e:
                print(e)   
                                          
            # type
            try:
                if player_choice['main_type'] and (str(player_choice['main_type']).lower() != str(pokemon.main_type).lower()):
                    del output_pokemon[pokemon.id]              
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # evolves i.e has this pokemon evolved from something else, like you know - as basic pokemon?
            try:
                # if there is anything in the "has evolved"
                if player_choice['has_evolved'] is not None:
                    #if the choice is false
                    if player_choice['has_evolved'] != True:
                        if str(pokemon.evolves_from) != "None":
                            del output_pokemon[pokemon.id]                
                    # if the choice is true
                    else:
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
                # both strings but false when compares with "is"
                #print(f"{str(player_choice['ears']).lower()} - {str(pokemon.ears).lower()}")
                if player_choice['ears'] and (str(player_choice['ears']).lower() != str(pokemon.ears).lower()):                  
                    #print(f"removing - {output_pokemon[pokemon.id]}")
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)

            # two legs
            try:
                if player_choice['more_than_two_legs'] and (str(player_choice['more_than_two_legs']).lower() != str(pokemon.more_than_two_legs).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:              
                pass
            except Exception as e:
                print(e)                        
               
            # horns
            try:
                if player_choice['horns'] and (str(player_choice['horns']).lower() != str(pokemon.horns).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e)               
               
            # tail 
            try:
                if player_choice['tail'] and (str(player_choice['tail']).lower() != str(pokemon.tail).lower()):
                    del output_pokemon[pokemon.id]
            except KeyError:
                pass
            except Exception as e:
                print(e) 
               
            # fins 
            try:
                if player_choice['fins'] and (str(player_choice['fins']).lower() != str(pokemon.fins).lower()):
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

        player_choice = self.player_choice
        
        end_game = False
        while end_game == False:
        
            # these values should change upon answering the qs
            print(player_choice)
            
            # get a question   
            full_question = self.get_question()
            if full_question:        
                question_type = full_question[0]
                question = full_question[1]
                value = full_question[2]    
                list_of_values = full_question[3]        
                print(question)
                
                answer = input("y / n / unsure\n")
                
                if answer == "y":         
                    try:
                        # if the value is a variable rather than a boolean
                        if list_of_values is not None: 
                            # change player choice value
                            player_choice[question_type] = value
                            # remove question so it can't be asked again
                            self.remove_question(question_type)  
                        else: 
                            # takes care of the booleans
                            player_choice[question_type] = True
                            self.remove_question(question_type)
                    except Exception as e:
                        print(e)
                
                elif answer == "n":
                    try:
                        if list_of_values is not None:
                            list_of_values.remove(value)
                            if len(list_of_values) >= 1:
                                self.remove_question(question_type)
                            else:
                                print("out of questions")
                                question = "I give up! No Pokemon match your description!"
                                end_game = True  
                                                                                                                 
                        else:                         
                            player_choice[question_type] = False
                            self.remove_question(question_type)
                            
                    except Exception as e:
                        print(e)
                else: 
                    print("Let's try again...")  
                 
            remaining_pokemon = self.narrow_down()
            print(f"{len(remaining_pokemon)} remaining pokemon")
            if len(remaining_pokemon) == 0:
                print("out of pokemon")
                question = "I give up! No Pokemon match your description!"
                end_game = True
                
            elif len(remaining_pokemon) <= 5:
                print("less than 5 pokemon")              
                try:
                    correct = False
                    while correct == False:
                        #print(f"{remaining_pokemon}")
                        guess = random.choice(list(remaining_pokemon.keys()))                 
                        question = "Is the Pokemon you are thinking of " + str(guess) + "?"
                        print(question)
                        guess_check = input("y / n / unsure\n")
                        if guess_check == "y":
                            correct = True
                            end_game = True                          
                            print(f"I win! Your Pokemon is {guess}. Good choice!")
                        elif guess_check == "n":
                            pass
                except Exception as e:
                    print(e)
                       
                

