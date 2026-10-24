import random

#loot_drop chances
LOOT_CHANCES = [("common",50),("uncommon",25),
                ("rare",15),("super rare",6),
                ("epic",3),("mythical",0.9),
                ('legendary',0.1)]

#loot rarity selection

def get_loot_rarity():
    rarities = []
    chances = []

    for rarity, chance in LOOT_CHANCES:
        rarities.append(rarity)
        chances.append(chance)

    return random.choices(rarities, weights=chances, k=1)[0]
    
#generating gold

def generate_gold(enemy):

    gold = random.randint(enemy["gold"]//2,enemy["gold"]*2)
    return gold

#loot item selection
def get_loot_item(weapons, armor, potions, rarity):

    # Find weapons of the selected rarity
    available_weapons = [weapon for weapon in weapons if weapon["rank"].lower() == rarity.lower()]

    # Find armor of the selected rarity
    available_armor = [item for item in armor if item["rank"].lower() == rarity.lower()]

    # Find potions of the selected rarity
    available_potions = [potion for potion in potions if potion["rank"].lower() == rarity.lower()]
   
    # Collect available item categories
    categories = []

    if available_weapons:
        categories.append("Weapon")

    if available_armor:
        categories.append("Armor")

    if available_potions:
        categories.append("Potion")

    # No item of this rarity exists
    if not categories:
        return None

    # Select a random item category
    category = random.choice(categories)

    if category == "Weapon":
        return random.choice(available_weapons)

    elif category == "Armor":
        return random.choice(available_armor)

    else:
        return random.choice(available_potions)

#add item to inventory
def add_loot_to_inventory(player, item, category):

    if category == "Weapon":

        player.setdefault("inventory", [])

        player["inventory"].append({"category": "Weapon",
            "item": item.copy()})

    elif category == "Armor":

        player.setdefault("inventory", [])

        player["inventory"].append({ "category": "Armor",
            "item": item.copy()})

    elif category == "Potion":

        player.setdefault("potions", [])

        player["potions"].append(item.copy())


# drop loot after defeating enemy

def drop_loot(player, enemy, weapons, armor, potions):

    print("\n========== LOOT DROPS ==========")

    # Give gold to the player
    gold = generate_gold(enemy)

    player["gold"] = player.get("gold", 0) + gold

    print("You received", gold, "gold!")

    # Decide whether an item drops
    item_drop_chance = 70

    if random.randint(1, 100) > item_drop_chance:

        print("No item dropped this time.")
        return None

    # Select the rarity
    rarity = get_loot_rarity()

    # Select an item
    item = get_loot_item( weapons,armor,potions,rarity)

    if item is None:

        print("No item of rarity", rarity, "is available.")
        return None

    # Determine the item category
    if item in weapons:
        category = "Weapon"

    elif item in armor:
        category = "Armor"

    else:
        category = "Potion"
    

    # Add the item to inventory
    add_loot_to_inventory(player, item, category)

    #print item details
    print("\nCongratulations! You found an item!")
    print("Item:", item["name"])
    print("Category:", category)
    print("Rarity:", rarity)

    return item

#testing
if __name__ == "__main__":

    from weapon import WEAPONS
    from armor import ARMOR
    from potion import POTIONS

    player = {
        "name": "Arin",
        "level": 10,
        "gold": 100,
        "inventory": [],
        "potions": []
    }

    enemy = {
        "name": "Goblin",
        "gold": 50
    }

    item = drop_loot(
        player,
        enemy,
        WEAPONS,
        ARMOR,
        POTIONS
    )

    print("\n========== UPDATED INVENTORY ==========")
    print(player["inventory"])

    print("\nPotions:", player["potions"])
    print("Gold:", player["gold"])
    print("Dropped item:",item)