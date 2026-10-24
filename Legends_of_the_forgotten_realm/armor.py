#rarity of armour
ARMOUR_RARITY = { "Common": {"price_multiplier": 1.0},
                  "Uncommon": {"price_multiplier": 1.2},
                  "Rare": {"price_multiplier": 1.5},
                  "Super Rare": {"price_multiplier": 2.0},
                  "Epic": {"price_multiplier": 3.0}, 
                  "Mythical": {"price_multiplier": 4.5}, 
                  "Legendary": {"price_multiplier": 6.0} }

#armour collection
ARMOR = [ 
    # Common Armor 
    { "name": "Cloth Armor", "rank": "Common", "defense_bonus": 2, "hp_bonus": 10, "mana_bonus": 0, "critical_resistance": 0, "price": 40, "required_level": 1 }, 
    { "name": "Leather Vest", "rank": "Common", "defense_bonus": 4, "hp_bonus": 15, "mana_bonus": 0, "critical_resistance": 1, "price": 60, "required_level": 1 }, 
    
    # Uncommon Armor 
    { "name": "Reinforced Leather Armor", "rank": "Uncommon", "defense_bonus": 7, "hp_bonus": 25, "mana_bonus": 5, "critical_resistance": 2, "price": 130, "required_level": 5 }, 
    { "name": "Apprentice Robe", "rank": "Uncommon", "defense_bonus": 5, "hp_bonus": 15, "mana_bonus": 20, "critical_resistance": 2, "price": 150, "required_level": 5 },
     
    # Rare Armor 
    { "name": "Iron Armor", "rank": "Rare", "defense_bonus": 12, "hp_bonus": 40, "mana_bonus": 5, "critical_resistance": 4, "price": 300, "required_level": 10 },
    { "name": "Ranger's Armor", "rank": "Rare", "defense_bonus": 10, "hp_bonus": 30, "mana_bonus": 10, "critical_resistance": 5, "price": 330, "required_level": 12 },
     
    # Super Rare Armor 
    { "name": "Crystal Armor", "rank": "Super Rare", "defense_bonus": 18, "hp_bonus": 60, "mana_bonus": 20, "critical_resistance": 7, "price": 700, "required_level": 20 },
    { "name": "Shadow Suit", "rank": "Super Rare", "defense_bonus": 15, "hp_bonus": 45, "mana_bonus": 25, "critical_resistance": 10, "price": 750, "required_level": 22 }, 
    
    # Epic Armor 
    { "name": "Flameguard Armor", "rank": "Epic", "defense_bonus": 25, "hp_bonus": 90, "mana_bonus": 20, "critical_resistance": 12, "price": 1400, "required_level": 30 }, 
    { "name": "Frost Mage Robe", "rank": "Epic", "defense_bonus": 20, "hp_bonus": 60, "mana_bonus": 50, "critical_resistance": 12, "price": 1500, "required_level": 32 }, 
    
    # Mythical Armor
    { "name": "Phoenix Armor", "rank": "Mythical", "defense_bonus": 35, "hp_bonus": 130, "mana_bonus": 35, "critical_resistance": 18, "price": 2800, "required_level": 50 }, 
    { "name": "Demon Lord Regalia", "rank": "Mythical", "defense_bonus": 38, "hp_bonus": 120, "mana_bonus": 45, "critical_resistance": 20, "price": 3000, "required_level": 55 },
    { "name": "Dragon Scale Armor", "rank": "Mythical", "defense_bonus": 55, "hp_bonus": 500, "mana_bonus": 150, "critical_resistance": 18, "price": 15000, "required_level": 70},
     
    # Legendary Armor 
    { "name": "Dragon King's Armor", "rank": "Legendary", "defense_bonus": 50, "hp_bonus": 200, "mana_bonus": 50, "critical_resistance": 25, "price": 5500, "required_level": 80 }, 
    { "name": "Armor of Eternity", "rank": "Legendary", "defense_bonus": 55, "hp_bonus": 220, "mana_bonus": 60, "critical_resistance": 30, "price": 6000, "required_level": 85 } 
    ]

#function to show armour
def show_armor():
    print("\n========ARMOR COLLECTION=========")

    for armor in ARMOR:
        print("\nNumber:",armor["name"])
        print("Rank:",armor["rank"])
        print("Defense:",armor["defense_bonus"])
        print("HP:",armor["hp_bonus"])
        print("Mana:",armor["mana_bonus"])
        print("Critical Resistance:",armor["critical_resistance"])
        print("Price:", armor["price"],"gold")
        print("Level:", armor["required_level"])


#function to find armor by name
def find_armor(armor_name):
    for armor in ARMOR:
        if armor["name"].lower() == armor_name.lower():
            return armor
        else:
            return None