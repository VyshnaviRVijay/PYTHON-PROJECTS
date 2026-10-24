#import modules
import time 

from player import create_character,player_stats
from enemy_and_bosses import (generate_random_enemy,find_boss,BOSSES)
from battle import start_battle
from level import gain_exp
from loot_drop import drop_loot
from world_map import (show_map,unlock_next_region)
from save_load import save_game,load_game
from weapon import WEAPONS
from armor import ARMOR
from potion import POTIONS

#initialize player stat

def init_stat(player):
    player.setdefault("enemies_defeated", 0) 
    player.setdefault("bosses_defeated", 0) 
    player.setdefault("weapons_collected", 0) 
    player.setdefault("rare_items_found", 0) 
    player.setdefault("play_time_seconds", 0) 
    player.setdefault("inventory", []) 
    player.setdefault("potions", []) 
    player.setdefault("current_region", "Village")

    return player



# play time

def get_total_playtime(player,session_start):
    previous_time = player.get("play_time_seconds",0)
    current_session = time.time() - session_start

    return max(0, int(previous_time + current_session))


def format_playtime(seconds):

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"


# final Score

def calc_final_score(player):

    score = (player.get("level",1) * 100
            + player.get("gold", 0) 
            + player.get("enemies_defeated", 0) * 25 
            + player.get("bosses_defeated", 0) * 250 
            + player.get("weapons_collected", 0) * 50 
            + player.get("rare_items_found", 0) * 100)

    return score

#victory screen

def show_victory_screen(player,session_start):
    print("\n" + "=" * 55) 
    print(" VICTORY! KINGDOM SAVED!") 
    print("=" * 55)

    print("\nThe Ancient Demon King has been defeated!") 
    print("You have brought peace back to Eldoria.")

    total_playtime = get_total_playtime(player, session_start) 
    final_score = calc_final_score(player)

    print("\n========== FINAL GAME SUMMARY ==========") 

    print("Player Name:", player.get("name", "Unknown")) 
    print("Final Level:", player.get("level", 1)) 
    print("Total Gold:", player.get("gold", 0)) 
    print("Bosses Defeated:", player.get("bosses_defeated", 0)) 
    print("Enemies Defeated:", player.get("enemies_defeated", 0)) 
    print("Weapons Collected:", player.get("weapons_collected", 0)) 
    print("Rare Items Found:", player.get("rare_items_found", 0))

    print("Total Play Time:", format_playtime(total_playtime))   
    print("Final Score:", final_score) 
    print("\nCongratulations,", player.get("name", "Hero") + "!") 
    print("Thank you for playing Legends of the Forgotten Realm.") 
    print("=" * 55)


#game over menu

def game_over():
    while True:
        print("\n" + "=" * 30) 
        print(" GAME OVER") 
        print("=" * 30)

        ch = input("\n1. Retry\n2. Load Save\n3. Exit\nEnter your choice").strip()

        if ch == "1":
            print("\nStarting a new adventure...") 
            player = create_character()

            if player is not None:
                return init_stat(player)

            elif ch == "2":
                player = load_game()

                if player is not None:
                    return init_stat(player)

                print("Please try again or choose other option")

            elif ch == "3":
                print("\nThanks for playing!") 
                return None

        else:
            print("Invalid choice!!. Please enter a valid choice")


#loot statistics handling

def award_loot(player,enemy):
    item = drop_loot(player,enemy,WEAPONS,ARMOR,POTIONS)

    if item is None:
        return

    #count collected weapons
    if any(item["name"] == weapon["name"] for weapon in WEAPONS):
        player["weapons_collected"] += 1

    # count rare or higher items
    rare_ranks = {"rare","super rare","epic","mythical","legendary"}

    if item.get("rank"," ").lower() in rare_ranks:
        player["rare_items_found"] += 1


#explore and battle

def explore(player,session_start):

    if player["hp"] <= 0:
        print("\nYour character has no HP remaining.")
        return player,session_start,False

    print("\n========== EXPLORE ==========") 
    print("1. Fight a Normal Enemy") 
    print("2. Challenge the Next Boss") 
    print("3. Return")

    ch = input("\nChoose an option:").strip()

    enemy = None

    if ch == "1":
        enemy = generate_random_enemy(player["level"])

    elif ch == "2":
        defeated_bosses = player.get("bosses_defeated", 0) 
        
        if defeated_bosses >= len(BOSSES): 
            print("\nYou have already defeated every boss!") 
            return player, session_start, False 
        
        next_boss = BOSSES[defeated_bosses] 
        
        if player["level"] < next_boss["level"]: 
            print("\nYou are not strong enough to challenge this boss.") 
            print("Required level:", next_boss["level"]) 
            return player, session_start, False

        enemy = find_boss(next_boss["name"]) 
        
        if enemy is None: 
            print("\nThe boss could not be found.") 
            return player, session_start, False


    elif ch == "3":
        return player, session_start, False 
    
    else: 
        print("\nInvalid choice.") 
        return player, session_start, False 
    
    print("\nYou encountered:", enemy["name"]) 
    
    result = start_battle(player, enemy) 
    
    # DEFEAT 
     
    if result == "defeat": 
        player["play_time_seconds"] = get_total_playtime( player, session_start ) 
        
        player = game_over()

        if player is None:
            return None,session_start,True

        session_start = time.time()
        return player,session_start,False


    #escape

    if result == "escaped": 
        print("\nYou returned safely.") 
        return player, session_start, False

    #victory
    if result == "victory":

        if enemy.get("type") == "boss":
            player["bosses_defeated"] += 1 
            print("\nBoss defeated:", enemy["name"]) 
            
            # Unlock the next region using the defeated boss level. 
            unlock_next_region(enemy["level"])

        else:
            player["enemies_defeated"] += 1

        gain_exp(player, enemy["exp"])

        award_loot(player, enemy)


        # Final boss defeated 
        if enemy["name"] == "Ancient Demon King": 
            show_victory_screen(player, session_start) 
            return player, session_start, True 
        return player, session_start, False


# Instructions

def show_instructions():
    print("\n" + "=" * 35) 
    print(" INSTRUCTIONS") 
    print("=" * 35) 
    
    print("1. Create a character and choose a class." \
    "\n2. Explore to find enemies." \
    "\n3. Defeat enemies to earn EXP and gold." \
    "\n4. Challenge bosses when you reach their required level." \
    "\n5. Defeating bosses increases your boss count." \
    "\n6. Use weapons, armour, and skills supported by your modules." \
    "\n7. Save your progress from the game menu." \
    "\n8. Defeat the Ancient Demon King to complete the game.")


#game menu

def play_game(player): 
    session_start = time.time() 
    ended = False 

    init_stat(player)

    
    while True:

        print("\n============= GAME MENU ============"
        "\n1. Explore\n2. View Character stats\n3. World Map\n4. Save Game\n5. Inventory \n6. Return to Main Menu\n7. Exit Game")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            player, session_start, ended = explore( player, session_start )
            
            if ended or player is None:
                return

        elif choice == "2":
            player_stats(player)

        elif choice == "3": 
            show_map(player) 


        elif choice == "4":
            save_game(player)

        elif choice == "5":
            show_inventory(player)
            input("\nPress Enter to continue...")

        elif choice == "6":
            return
        

        elif choice == "7":
            print("Thanks for Playing!!")
            return

        else:
            print("Invalid choice. Please select valid choice.")



#story of eldoria

def show_story(): 

    print("\n" + "=" * 50) 
    print(" THE STORY OF ELDORIA") 
    print("=" * 50)

    print(""" The kingdom of Eldoria has fallen into darkness. 
        Monsters have taken over villages, forests, caves, and ancient ruins. 
        Fear and destruction spread throughout the realm. Powerful bosses guard the entrances to new regions. 
        Every ten levels, a mighty enemy stands in your way, challenging your strength and courage. 
        You are the hero chosen to save Eldoria. 
        Your mission is to explore the dangerous regions, defeat powerful enemies, grow stronger, and overcome every boss standing in your path. 
        Reach Level 100 and face the ultimate enemy, the Ancient Demon King. Defeat him, destroy the darkness, and bring peace back to the kingdom of Eldoria.
        Your adventure begins now, hero! """)

    print("=" * 50) 
    
    input("\nPress Enter to begin your adventure...")


#display player inventory
def show_inventory(player): 
    print("\n========== INVENTORY ==========") 
    inventory = player.get("inventory", []) 
    potions = player.get("potions", []) 
    
    if not inventory and not potions: 
        print("Your inventory is empty!") 
        return 
    
    for index, entry in enumerate(inventory, start=1): 
        item = entry["item"] 
        print(index, ".", entry["category"], "-", item["name"]) 

        for index, potion in enumerate(potions, start=len(inventory) + 1): 
            print(index, ". Potion -", potion["name"])

##MAIN MENU
#function to start game
def start_game():
    while True:
        print("\n")
        print("=" * 50)
        print("------------LEGENDS OF FORGOTTEN REALM------------")
        print("=" * 50)

        print("\n1. New Game\n2. Continue\n3. Instructions\n4. Exit")
        ch = input("Enter your choice: ").strip()

        if ch == "1":
            player = create_character()

            if player is not None: 
                play_game(player) 
                
        elif ch == "2": 
            player = load_game() 
            
            if player is not None: 
                play_game(player) 
                
        elif ch == "3": 
            show_instructions() 
            
        elif ch == "4": 
            print("\nThanks for playing Legends of the Forgotten Realm!") 
            break

        else:
            print("\nInvalid choice! Please enter a valid choice.")   

#starting the game
if __name__ == "__main__":
    start_game()

                

