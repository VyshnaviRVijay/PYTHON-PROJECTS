#rarity of potion
POTION_RARITY = {
    "Common": {"price_multiplier": 1.0},
    "Uncommon": {"price_multiplier": 1.2},
    "Rare": {"price_multiplier": 1.5},
    "Super Rare": {"price_multiplier": 2.0},
    "Epic": {"price_multiplier": 3.0},
    "Mythical": {"price_multiplier": 5.0},
    "Legendary": {"price_multiplier": 8.0}
}

#potion collection
POTIONS = [

    # Common Potions
    {"name": "Small Health Potion",
     "rank": "common",
    "type": "health",
    "effect": 50,
    "price": 20,
    "required_level": 1},

    {"name": "Small Mana Potion",
    "rank": "common",
    "type": "mana",
    "effect": 30,
    "price": 20,
    "required_level": 1},

    {"name": "Minor Strength Potion",
    "rank": "common",
    "type": "attack",
    "effect": 5,
    "price": 25,
    "required_level": 1},

    # Uncommon Potions
    {"name": "Health Potion",
    "rank": "uncommon",
    "type": "health",
    "effect": 100,
    "price": 50,
    "required_level": 3},

    {"name": "Mana Potion",
    "rank": "uncommon",
    "type": "mana",
    "effect": 60,
    "price": 50,
    "required_level": 3},

    {"name": "Strength Potion",
    "rank": "uncommon",
    "type": "attack",
    "effect": 10,
    "price": 60,
    "required_level": 5},

    # Rare Potions
    {"name": "Large Health Potion",
    "rank": "rare",
    "type": "health",
    "effect": 200,
    "price": 100,
    "required_level": 10},

    {"name": "Large Mana Potion",
    "rank": "rare",
    "type": "mana",
    "effect": 120,
    "price": 100,
    "required_level": 10},

    {"name": "Defense Potion",
    "rank": "rare",
    "type": "defense",
    "effect": 15,
    "price": 120,
    "required_level": 12},

    # Super Rare Potions
    {"name": "Super Health Potion",
    "rank": "super rare",
    "type": "health",
    "effect": 350,
    "price": 200,
    "required_level": 20},

    {"name": "Super Mana Potion",
    "rank": "super rare",
    "type": "mana",
    "effect": 200,
    "price": 200,
    "required_level": 20},

    # Epic Potions
    {"name": "Epic Healing Potion",
    "rank": "epic",
    "type": "health",
    "effect": 500,
    "price": 350,
    "required_level": 30},

    # Mythical Potions
    {"name": "Mythical Healing Potion",
    "rank": "mythical",
    "type": "health",
    "effect": 750,
    "price": 500,
    "required_level": 50},

    # Legendary Potions
    {"name": "Legendary Healing Potion",
    "rank": "legendary",
    "type": "health",
    "effect": 1000,
    "price": 1000,
    "required_level": 75},

    {"name": "Legendary Mana Potion",
    "rank": "legendary",
    "type": "mana",
    "effect": 500,
    "price": 1000,
    "required_level": 75}
]


#Function to display all potions
def show_all_potions():
    print("\n============ AVAILABLE POTIONS ============")

    for potion in POTIONS:
        print(potion["name"],
              '|Rarity:',potion["rank"],
              "| Type:",potion["type"],
              "| Price:",potion["price"],"gold")

#find potion by name
def find_potion(potion_name):
    for potion in POTIONS:
        if potion["name"].lower() == potion_name.lower():
            return potion.copy()
    
    return None

#function to get available potions at player's level
def get_available_potion(player_level):
    available_potions = []

    for potion in POTIONS:
        if potion["required_level"] <= player_level:
            available_potions.append(potion)

    return available_potions


#use potion in game

def use_potion(player,potion):

    #health restore
    if potion["health_restore"] == "full":
        player["hp"] = player["max_hp"]

    elif potion["health restore"] > 0:
        player["hp"] = min(player["hp"] + player["health_restore"],player["max_hp"])

    #restore mana
    if potion["mana_restore"] == "full":
        player["mana"] = player["max_mana"]

    elif potion["mana_restore"] > 0:
        player["mana"] = min(player["mana"] + potion["mana_restore"],player["max_mana"])


    # Apply temporary buffs
    if potion["attack_bonus"] > 0:
        player["attack"] += potion["attack_bonus"]

    if potion["defense_bonus"] > 0:
        player["defense"] += potion["defense_bonus"]

    if potion["critical_bonus"] > 0:
        player["critical_chance"] += potion["critical_bonus"]


    # Store buff duration information
    if potion["duration"] > 0:

        if "active_buffs" not in player:
            player["active_buffs"] = []

        player["active_buffs"].append({
            "name": potion["name"],
            "attack_bonus": potion["attack_bonus"],
            "defense_bonus": potion["defense_bonus"],
            "critical_bonus": potion["critical_bonus"],
            "turns_left": potion["duration"]
        })

    print("\nYou used:", potion["name"])
    print("Current HP:", player["hp"], "/", player["max_hp"])
    print("Current Mana:", player["mana"], "/", player["max_mana"])

#show player potions
def show_player_potions(player):
    print("\n========== YOUR POTIONS ==========")

    if not player.get("potions"):
        print("You don't have any potions.")
        return

    for index, potion in enumerate(player["potions"], start=1):

        print(index, ".", potion["name"])

#function to use potion from inventory
def use_potion_from_inventory(player):

    show_player_potions(player)

    if not player.get("potions"):
        return
    
    try:
        choice = int(input("\nChoose a potion number: "))

        if choice < 1 or choice > len(player["potions"]):
            print("Invalid potion number.")
            return

        potion = player["potions"][choice - 1]

        use_potion(player, potion)

        # Remove the used potion
        player["potions"].pop(choice - 1)

    except ValueError:
        print("Please enter a valid number.")


#test potion
if __name__ == "__main__":

    show_all_potions()

    player_level = 10

    print("\n========== AVAILABLE POTIONS ==========")

    available_potions = get_available_potion(player_level)

    for potion in available_potions:
        print(potion["name"])


