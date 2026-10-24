#weapon rarity system
RARITY={"common":{"multiplier":1.0,"critical_bonus":0,"color":"white"},
        "uncommon":{"multiplier":1.1,"critical_bonus":2,"color":"green"},
        "rare":{"multiplier":1.3,"critical_bonus":5,"color":"blue"},
        "super rare":{"multiplier":1.5,"critical_bonus":8,"color":"purple"},
        "epic":{"multiplier":1.8,"critical_bonus":12,"color":"orange"},
        "mythical":{"multiplier":2.2,"critical_bonus":18,"color":"red"},
        "legendary":{"multiplier":2.8,"critical_bonus":25,"color":"gold"}}


#Available weapons
WEAPONS=[
    #common weapons
    {"name":"Wooden Sword","rank":"common","damage":5,"critical_bonus":0,"price":20,"required_level":1},
    {"name":"Rusty Axe","rank":"common","damage":7,"critical_bonus":0,"price":25,"required_level":1},
    {"name":"Training Bow","rank":"common","damage":6,"critical_bonus":0,"price":30,"required_level":1},

    #uncommon weapons
     {"name":"Hunter's Dagger","rank":"uncommon","damage":10,"critical_bonus":2,"price":60,"required_level":3},
     {"name":"Bronze Spear","rank":"uncommon","damage":12,"critical_bonus":2,"price":70,"required_level":4},
     {"name":"Oak Staff","rank":"uncommon","damage":11,"critical_bonus":2,"price":75,"required_level":4},

     #rare
     {"name":"Iron Sword","rank":"rare","damage":18,"critical_bonus":5,"price":150,"required_level":8},
     {"name":"Steel Axe","rank":"rare","damage":20,"critical_bonus":5,"price":180,"required_level":10},
     {"name":"Long Bow","rank":"rare","damage":17,"critical_bonus":5,"price":160,"required_level":8},

     #super rare
     {"name":"Crystal Blade","rank":"super rare","damage":28,"critical_bonus":8,"price":350,"required_level":15},
     {"name":"Shadow Dagger","rank":"super rare","damage":30,"critical_bonus":8,"price":400,"required_level":17},
     {"name":"Lightning Bow","rank":"super rare","damage":27,"critical_bonus":8,"price":375,"required_level":16},

     #epic
     {"name":"Flame Sword","rank":"epic","damage":40,"critical_bonus":12,"price":650,"required_level": 25},
     {"name":"Ice Spear","rank":"epic","damage":42,"critical_bonus":12,"price":700,"required_level":25},
     {"name":"Thunder Hammer","rank":"epic","damage":45,"critical_bonus":12,"price":750,"required_level":30},

     #mythical
     {"name":"Phoenix Blade","rank":"mythical","damage":60,"critical_bonus":18,"price":1200,"required_level": 40},
     {"name":"Demon Slayer","rank":"mythical","damage":65,"critical_bonus":18,"price":1400,"required_level": 45},
     {"name":"Celestial Staff","rank":"mythical","damage":62,"critical_bonus":18,"price":1350,"required_level": 43},

     #Legendary
     {"name":"Dragon King's Sword","rank":"legendary","damage":85,"critical_bonus":25,"price":2500,"required_level": 60},
     {"name":"Blade of Eternity","rank":"legendary","damage":95,"critical_bonus":25,"price":3000,"required_level": 70},
     {"name":"Bow of the Gods","rank":"legendary","damage":90,"critical_bonus":25,"price":2800,"required_level": 65}
    
    ]  

#function to show weapon
def show_weapon():
    print("\n")
    print("======== WEAPON COLLECTION =========")
    print("\n")

    for weapon in WEAPONS:
        print("\nName:",weapon["name"])
        print("Rank:",weapon["rank"])
        print("Base Damage:",weapon["damage"])
        print("Critical Bonus:",weapon["critica_bonus"], "%")
        print("Price",weapon["price"],"gold")
        print("Required level:",weapon["required_level"])
        print("Damage Multiplier:", "x",RARITY[weapon["rank"]]["multiplier"])

#function to find weapon by name
def find_weapon(weapon_name):
    for weapon in WEAPONS:
        if weapon["name"].lower() == weapon_name.lower():
            return weapon.copy()
        else:
            print("No such weapon found!!")

#function to calculate weapon damage
def calc_weapon_damage(weapon):
    rank = weapon["rank"].lower()

    rarity_multiplier = RARITY[rank]["multiplier"]
    
    damage = weapon["damage"] * rarity_multiplier

    return round(damage)

#function to get Weapons critical bonus
def get_crit_bonus(weapon):
    rank = weapon["rank"].lower()
    return RARITY[rank]["critical_bonus"]

#function to check weapon equip status by level requirement checking
def can_equip(player,weapon):
    if player["level"] >= weapon["required_level"]:
        return True
    else:
        return False


#function to equip a weapon
def equip_weapon(player,weapon_name):
    weapon = find_weapon(weapon_name)

    if not weapon:
        print("Weapon Not Found!!")
        return
    #checking for valid level 
    if not can_equip(player,weapon):
        print(f"You need {weapon["required_level"]} to equip this weapon.")
        return

    #displaying player's weapon
    player["weapon"] = weapon 

    print(f"\nYou equipped: {weapon["name"]}\nWeapon Rank: {weapon["rank"]}\nWeapon Damage: {calc_weapon_damage(weapon)}\ncritical Bonus: {get_crit_bonus(weapon)}%") 

#equip collected armor
def equip_collected_armor(player, armor_name):
    for entry in player.get("inventory", []):
        if entry["category"] == "Armor":
            armour = entry["item"]

            if armour["name"].lower() == armor_name.lower():
                player["armour"] = armour
                print("Equipped:", armour["name"])
                return True

    print("You do not own this armor!")
    return False