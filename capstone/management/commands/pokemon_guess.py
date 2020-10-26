from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
import json
from ...models import Pokemon
import random

class Command(BaseCommand):
    help = "Pokemon practice"
    def handle(self, *args, **kwargs):
        pokemon_list = Pokemon.objects.all()
        user_choice_name = "Unassigned"
        user_choice_shape = "Unassigned"
        user_choice_color = "Unassigned"
        user_choice_egg_group = "Unassigned"
        user_choice_habitat = "Unassigned"
        user_choice_evolves = "Unassigned"
        user_choice_type = "Unassigned"
        user_choice_ears = "Unassigned"
        user_choice_legs = "Unassigned"
        user_choice_horns = "Unassigned"
        user_choice_tail = "Unassigned"
           
        colors = ["black", "blue", "brown", "gray", "green", "pink", "purple", "red", "white", "yellow"]             
        habitats = ["cave", "forest", "grassland", "mountain", "rare", "rough-terrain", "sea", "urban", "waters-edge"]
                             
        shapes = ["ball", "squiggle", "fish", "arms", "blob", "upright", "legs", "quadruped", "wings",  "tentacles", "heads", "humanoid", "bug-wings", "armor"]
        
        responses = ["Hmm..let me think on that", "Ah-ha, we are getting somewhere", "I think I'm getting closer to the answer!", "Oooh, we are narrowing it down..."]

        types = ["normal", "flying", "ground", "bug", "steel", "water", "ice", "dark", "fighting", "poison", "rock", "ghost", "fire", "grass", "psychic", "dragon", "fairy"]
        
        questions = {
                    "color":"Is your chosen Pokemon ''?", 
                    "habitat":"Is your chosen Pokemon found in/on/around the '' areas?", 
                    "shape":"Is your chosen Pokemon '' shaped?",
                    "type":"Is your chosen Pokemon '' type?",
                    "ears":"Does your chosen Pokemon have ears?",
                    "legs":"Does your chosen Pokemon have 2 or more legs?",
                    "horns":"Does your chosen Pokemon have horns?",
                    "tail":"Does your chosen Pokemon have a tail?"
                    }
              
        player_choice = "Pikachu"
        ai_pokemon_guess = "Voltorb"
            

        # pick an initial question    
        key = random.choice(list(questions))
        question_type = key
        question = questions[key]

        # why am i unable to input?
        
        if question_type == "color": 
            if user_choice_color == "Unassigned":
                color = random.choice(colors)
                full_question = question.replace("''", color)
                print(full_question)
                answer = input("Enter yes or no: ")
                if answer == "yes": 
                    response = random.choice(responses) 
                    print(response)
                    user_choice_color = color               
                elif answer == "no":       
                    response = random.choice(responses) 
                    print(response)
                    colors.remove(color)                                     
                elif answer == "unsure":       
                    user_choice_color = "Unknown"
                key = random.choice(list(questions))
                question_type = key
                question = questions[key]
            
        elif question_type == "habitat": 
            if user_choice_habitat == "Unassigned":
                habitat = random.choice(habitats)
                full_question = question.replace("''", habitat)
                print(full_question)
                answer = input("Enter yes or no: ")
                if answer == "yes": 
                    response = random.choice(responses) 
                    print(response)
                    user_choice_habitat = habitat                   
                elif answer == "no": 
                    response = random.choice(responses) 
                    print(response)
                    habitats.remove(habitat)                      
                elif answer == "unsure":       
                    user_choice_color = "Unknown"
                key = random.choice(list(questions))
                question_type = key
                question = questions[key]    
        

        
        elif question_type == "shape": 
            if user_choice_shape == "Unassigned":
                shape = random.choice(shapes)
                full_question = question.replace("''", shape)
                print(full_question)
                answer = input("Enter yes or no: ")
                if answer == "yes": 
                    response = random.choice(responses) 
                    print(response)
                    user_choice_shape = shape                  
                elif answer == "no":       
                    response = random.choice(responses) 
                    print(response)  
                    shapes.remove(shape)
                elif answer == "unsure":       
                    user_choice_shape = "Unknown"
            
        elif question_type == "type": 
            if user_choice_type == "Unassigned":
                type = random.choice(types)        
                full_question = question.replace("''", type)
                print(full_question)
                     
        elif question_type == "ears": 
            if user_choice_type == "Unassigned": 
                print(question)
                     
        elif question_type == "legs": 
            if user_choice_type == "Unassigned":             
                print(question)
                
        elif question_type == "horns": 
            if user_choice_type == "Unassigned": 
                print(question)
            
        elif question_type == "tail": 
            if user_choice_type == "Unassigned":        
                print(question)
        
       
        else: 
            print(f"Is this your chosen Pokemon? >>> {ai_pokemon_guess}")
            answer = input("Enter yes or no: ")
            
            if answer == "yes": 
                print("Good choice! That was a tough one!")
                win = True           
            
            elif answer == "no": 
                print("I'll have to try again")
             

           
        # filter queries based on user_choice values
            