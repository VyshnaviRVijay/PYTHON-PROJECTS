import json
import os

from world_map import WORLD_MAP

#savefile path
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"saved_game.json")


#save game
def save_game(player):
    try:
        with open(SAVE_FILE,"w") as file:
            json.dump(player,file,indent = 4)

        print("GAME SAVED SUCCESSFULLY!!")

    except (OSError,TypeError) as error:
        print("\nUNABLE TO SAVE GAME",error)

# LOAD GAME 
def load_game(): 
    if not os.path.exists(SAVE_FILE): 
        print("\nNo saved game found!") 
        return None 
    try: 
        with open(SAVE_FILE, "r") as file: 
            player = json.load(file) 
        
        if not isinstance(player, dict):
            print("\nInvalid saved game data!") 
            return None 
        
        if "name" not in player or "level" not in player: 
            print("\nThe saved game is missing required player information!") 
            return None 
        
        print("\nGame loaded successfully!") 
        
        print("Welcome back,", player["name"] + "!") 
        
        return player 
    
    except (OSError, json.JSONDecodeError, TypeError) as error: 
        print("\nUnable to load the game:", error) 
        return None

    