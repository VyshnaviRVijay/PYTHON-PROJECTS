#Character creation

#character class creation and base stats

CLASSES = {
    "1":{"name":"Warrior","hp":150,"mana":40,"attack":20,"defense":15,"crit_chance":5},
    "2":{"name":"Mage","hp":90,"mana":150,"attack":25,"defense":5,"crit_chance":10},
    "3":{"name":"Archer","hp":110,"mana":80,"attack":18,"defense":3,"crit_chance":20},
    "4":{"name":"Assasin","hp":80,"mana":70,"attack":30,"defense":5,"crit_chance":30}
    }

#new character creation function
def create_character():
    print("\n")
    print("=" * 40)
    print("-----------CHARACTER CREATION----------")
    print("=" * 40)
    print("\n")

    #get player's name
    while True:
        name = input("Enter player name: ").strip()

        #breaking loop after getting a name 
        if name:
            break
        else:
            print("Name cannot be empty. Try again!!.")

    #display available classes
    while True:
        ch = input("\n Choose Your Class: \n1. Warrior\n2. Mage\n3. Archer\n4. Assasin\nEnter Your Choice: " )
        if ch in CLASSES:
            break  
        else:
            print("Invalid. PLease enter valid choice.")

    #selected class statistics
    selected_class = CLASSES[ch]
    print("Class Selected: ",selected_class["name"])

    #since the player is weapon equipped and armour equipped we need starting weapon and armour
    starting_weapon = {"name": "Wodden Sword",
                        "rank": "common",
                        "damage": 5,
                        "critical_bonus": 0,
                        "price": 20,
                        "required_level": 1}

    starting_armor = { "name": "Leather Armor", 
                       "rank": "common", 
                       "defense": 3, 
                       "price": 20, 
                       "required_level": 1 }

    #player stats
    player={
        "name":name,"class":selected_class,"level":1,"exp":0,

        "hp":selected_class["hp"],"max_hp":selected_class["hp"],

        "mana":selected_class["mana"],"max_mana":selected_class["mana"],

        "attack":selected_class["attack"],"defense":selected_class["defense"],

        "gold":100,

        "crit_chance":selected_class["crit_chance"],"crit_damage":2,

        "weapon":starting_weapon,"armor":starting_armor,"health_potions":3,

        "mana_potions":2,"enemies_defeated":0,"bosses_defeated":0,"weapons_collected":0,"rare_items_found":0,"inventory":[],
        "potions": [] , "active_buffs":[],"current_region":"Village"}
    

    print("\nCharacter created successfully!")
    print("Starting Weapon: ",player["weapon"]["name"])
    print("Starting Armor: ",player["armor"]["name"])

    return player


#character stats display
def player_stats(player):

    print("\n") 
    print("=" * 40)
    print(" CHARACTER STATISTICS") 
    print("=" * 40)

    print("Name:",player["name"])
    print("Class:",player["class"])
    print("Level:",player["level"])
    print("Experience:",player["exp"])
    print("Gold:",player["gold"])
    print("HP:",player["hp"])
    print("Mana:",player["mana"],"/",player["max_mana"])
    print("Base Attack:",player["attack"])
    print("Base Defense:",player["defense"])
    print("Critical chance:",player["crit_chance"])
    print("Weapon:",player["weapon"]["name"])
    print("Weapon Damage:",player["weapon"]["damage"])
    print("Armor:",player["armor"]["name"])
    print("Armor Defense:",player["armor"]["defense"])
    print("Health Potions:",player["health_potions"])
    print("mana_Potions:",player["mana_potions"])
    
    
    print("=" * 40)
    