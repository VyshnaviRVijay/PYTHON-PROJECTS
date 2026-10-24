import random

#importing weapon damge calculation function and critical bonus function
from weapon import calc_weapon_damage,get_crit_bonus


#critical hit 
#function to calculate damage

def calc_damage(player,enemy):
    attack = player["attack"]#player attack

    weapon = player.get("weapon")#weapon details
    weapon_damage = 0
    weapon_critical_bonus = 0

    #calculate weapon damage and critical bonus

    if weapon:
        weapon_damage = calc_weapon_damage(weapon)
        weapon_critical_bonus = get_crit_bonus(weapon)

    #calculate normal damage
    damage = attack + weapon_damage - enemy["defense"]

    #ensuring min damage as 1
    damage = max(1,damage)

    #calculate critical chance
    critical_chance = (player.get("critical_chance",0) + weapon_critical_bonus)

    #add critical chance from active buffs
    for buff in player.get("active_buffs", []):
        critical_chance += buff.get("critical_bonus",0)

    #keep critical chance between 0 and 100
    critical_chance = min(100,max(0,critical_chance))

    #check for critical hit
    if random.randint(1, 100) <= critical_chance:
        critical_multiplier = player.get("critical_multiplier", 2)
        damage = round(damage * critical_multiplier)

        print("\nCRITICAL HIT!")

    return damage


#Player attack

def player_attack(player,enemy):
    damage = calc_damage(player,enemy)

    # reduce enemy hp
    enemy["hp"] = max(0,enemy["hp"] - damage)
    print("\nYou attacked",enemy['name'])
    print("Damage dealt",damage)

    print("Enemy HP:",enemy["hp"],"/",enemy["max_hp"])



#defend mechanics
def defend(player):
    player["defending"] = True

    print("\n You take a defensive position!.\nThe next incoming attack will deal 50% less damage.")
    
#Enemy attack

def enemy_attack(player,enemy):

    #calculate damage after player defense stst
    damage = (enemy["attack"] - player["defense"])

    #Ensure min damage as 1
    damage = max(1,damage)

    #Reduce damance if player is defending
    if player.get("defending",False):
        damage = round(damage * 0.5)
        player["defending"] = False
        print("\nYour defense reduced the incoming damage!")

    #apply damage to player
    player["hp"] = max(0,player["hp"] - damage)

    print("\n",enemy["name"],"attacked you!!")
    print("Damage received:",damage)

    print("Your HP:",player["hp"],"/",player["max_hp"])

#turn-based battle

def start_battle(player,enemy):
    
    enemy = enemy.copy()
    enemy["max_hp"] = enemy["hp"]
    
    player["defending"] = False
    

    print("\n")
    print("=" * 40)
    print("-------------- BATTLE STARTS ---------------")
    print("=" * 40)

    print("Player:",player['name'])
    print("Enemy:",enemy["name"])

    print("Enemy HP",enemy["hp"],"/",enemy["max_hp"])

    #continuing as both alive
    while player["hp"]>0 and enemy["hp"]>0:

        print("\n=========== YOUR TURN ============")

        ch = input("\n1. Attack\n2. Defend\n3. View Stats\n4. Run\nChoose an action: ").strip()

        turn_used = False

        #player attack
        if ch == "1":
            player_attack(player,enemy)
            turn_used = True

        #player defends
        elif ch == "2":
            defend(player)
            turn_used = True

        #view player stats
        elif ch == "3":
            print("\n========== PLAYER STATS ==========")
            print("Name:", player["name"])
            print("HP:", player["hp"], "/", player["max_hp"])
            print("Attack:", player["attack"])
            print("Defense:", player["defense"])

        
        #player attempts run
        elif ch == "4":

            if enemy.get("type") == "boss": 
                print("\nYou cannot escape from a boss battle!") 
                continue
                
            if random.randint(1, 100) <= 50: 
                print("\nYou escaped successfully!") 
                return "escaped" 
            
            print("\nYou failed to escape!") 
            turn_used = True 

        else: 
            print("\nInvalid choice. Please select 1-4.") 
            continue

    #enemy takes turn after valid action
    if turn_used and enemy["hp"] > 0:
        enemy_attack(player, enemy)

    # Check if player is defeated
    if player["hp"] <= 0:
        print("\n========== GAME OVER ==========")
        print("You were defeated!")

        return "defeat"

    # Check if enemy is defeated
    if enemy["hp"] <= 0:

        print("\n========== VICTORY ==========")
        print("You defeated", enemy["name"] + "!")

        return "victory"

#test battle system
if __name__ == "__main__":

    player = {
        "name": "Arin",
        "hp": 200,
        "max_hp": 200,
        "attack": 40,
        "defense": 15,
        "critical_chance": 20,
        "critical_multiplier": 2,
        "weapon": {
            "name": "Iron Sword",
            "rank": "Rare",
            "damage": 25,
            "critical_bonus": 5
        },
        "active_buffs": []
    }

    enemy = {
        "name": "Goblin",
        "hp": 150,
        "attack": 25,
        "defense": 10
    }

    start_battle(player, enemy)

