
#Leveling system

MAX_LEVEL = 100


#calculating required experience
def req_exp(level):
    return level * 100

#display player level
def show_level(player):
    print("\n============== PLAYER LEVEL ==============")

    print("Name:",player["name"])
    print("Level:",player["level"])
    print("Exp:",player["exp"],"/",req_exp(player["level"]))

    if player["level"] < MAX_LEVEL:

        exp_needed = req_exp(player["level"])

        print("Exp Needed:",exp_needed - player["exp"])

    else:
        print("Maximum level reached!!")

#level_up
def level_up(player):
    if player["level"] >= MAX_LEVEL:

        return

    player["level"] += 1

    # Increase player stats
    player["max_hp"] += 20
    player["hp"] = player["max_hp"]

    player["max_mana"] += 10
    player["mana"] = player["max_mana"]

    player["attack"] += 5
    player["defense"] += 2


#adding experience to player
def gain_exp(player, amount):

    print("\nYou gained", amount, "EXP!")

    if player["level"] >= MAX_LEVEL:

        player["level"] = MAX_LEVEL
        player["exp"] = 0

        print("You have reached the maximum level!")

        return

    player["exp"] += amount

    # Check whether the player can level up
    while player["level"] < MAX_LEVEL:

        needed_exp = req_exp(player["level"])

        if player["exp"] >= needed_exp:

            player["exp"] -= needed_exp

            level_up(player)

        else:

            break


        print("\n================================")
        print("       LEVEL UP!")
        print("================================")
        print("You reached level", player["level"], "!")

        #imporove player stats
        
        player["max_hp"] += 20
        player["hp"] = player["max_hp"]
        player["attack"] += 5
        player["defense"] += 2

        print("Maximum HP increased by 20!")
        print("HP restored completely!")
        print("Attack increased by 5!")
        print("Defense increased by 2!")

        print("\nNew Stats:")
        print("Level:", player["level"])
        print("HP:", player["hp"], "/", player["max_hp"])
        print("Attack:", player["attack"])
        print("Defense:", player["defense"])



if __name__ == "__main__":

    player = {
        "name": "Arin",
        "level": 1,
        "exp": 0,
        "hp": 100,
        "max_hp": 100,
        "mana": 50,
        "max_mana": 50,
        "attack": 20,
        "defense": 10
    }

    show_level(player)

    gain_exp(player, 100)

    show_level(player)