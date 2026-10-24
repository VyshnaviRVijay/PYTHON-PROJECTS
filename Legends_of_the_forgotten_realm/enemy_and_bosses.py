import random

#ENEMY DATA

ENEMIES = [
    #Forest
    {"name":"Goblin","type":"normal","region":"Forest","level":1,
     "hp":100,"attack":15,"defense":5,"exp":20,"gold":15},
    {"name":"Wild Wolf","type":"normal","region":"Forest","level":2,
     "hp":120,"attack":20,"defense":8,"exp":30,"gold":20},
    {"name":"Goblin Archer","type":"normal","region":"Forest","level":3,
    "hp":140,"attack":25,"defense":7,"exp":35,"gold":25},

    #Cave 
    {"name":"Ork Warrior","type":"normal","region":"Cave","level":5,
     "hp":200,"attack":30,"defense":12,"exp":50,"gold":35},
    {"name":"Cave Spider","type":"normal","region":"Cave","level":6,
     "hp":180,"attack":35,"defense":10,"exp":55,"gold":40},
    {"name":"Dessert Scorpion","type":"normal","region":"Cave","level":10,
     "hp":250,"attack":40,"defense":15,"exp":80,"gold":60},

     #Ruins
    {"name":"Skeleton Warrior","type":"normal","region":"Ruins","level":15,
    "hp":300,"attack":45,"defense":40,"exp":100,"gold":75},

    #Castle
    {"name":"Dark Knight","type":"normal","region":"Castle","level":20,
     "hp":400,"attack":55,"defense":25,"exp":150,"gold":100},

    #Volcano
    {"name":"Fire Elemental","type":"normal","region":"Volcano","level":30,
     "hp":500,"attack":70,"defense":30,"exp":200,"gold":150},

    #Frozen Mountain
    {"name":"Ice Golem","type":"normal","region":"Frozen Mountain","level":40,
     "hp":700,"attack":85,"defense":40,"exp":300,"gold":200},

    #Sky Temple
    {"name":"Sky Guardian","type":"normal","region":"Sky Temple","level":50,
    "hp":900,"attack":100,"defense":50,"exp":400,"gold":300},

    #Demon Realm
    {"name":"Demon Soldier","type":"normal","region":"Demon Realm","level":60,
     "hp":1200,"attack":120,"defense":60,"exp":500,"gold":400}
    ]

#BOSS DATA
BOSSES = [
    #Forest
    {"name":"Goblin King","type":"boss","region":"Forest","level":10,
     "hp":1000,"attack":60,"defense":25,"exp":500,"gold":500},
    {"name":"Forest Guardian","type":"boss","region":"Forest","level":20,
     "hp":1800,"attack":90,"defense":40,"exp":1000,"gold":1000},
    
    #Cave
    {"name":"Ancient Golem","type":"boss","region":"Cave","level":30,
     "hp":3000,"attack":120,"defense":60,"exp":1500,"gold":1500},

    #Ruins
    {"name":"Vampire Lord","type":"boss","region":"Ruins","level":40,
     "hp":4500,"attack":150,"defense":75,"exp":2000,"gold":2000},

    #Castle
    {"name":"Dragon Rider","type":"boss","region":"Castle","level":50,
     "hp":6000,"attack":180,"defense":90,"exp":3000,"gold":3000},

    #Volcano
    {"name":"Demon General","type":"boss","region":"Volcano","level":60,
     "hp":8000,"attack":220,"defense":110,"exp":4000,"gold":4000},

    #Frozen Mountain
    {"name":"Ice Titan","type":"boss","region":"Frozen Mountain","level":70,
     "hp":10000,"attack":260,"defense":130,"exp":5000,"gold":5000},

    #Sky Temple
    {"name":"Shadow Emperor","type":"boss","region":"Sky Temple","level":80,
     "hp":13000,"attack":300,"defense":150,"exp":6000,"gold":6000},
    {"name":"Celestial Dragon","type":"boss","region":"Sky Temple","level":90,
     "hp":16000,"attack":350,"defense":175,"exp":8000,"gold":8000},

    #Demon Realm
    {"name":"Ancient Demon King","type":"boss","region":"Demon Realm","level":100,
     "hp":20000,"attack":400,"defense":200,"exp":10000,"gold":10000}

]

def display_enemy(enemy):

    print("\n==========ENEMY DETAILS==========")

    print(f"Name: {enemy['name']}\nType: {enemy['type']}\nRegion: {enemy['region']}\nLevel: {enemy['level']}\nHP: {enemy['hp']}\nAttack: {enemy['attack']}\nDefense: {enemy['defense']}\nEXP Reward: {enemy['exp']}\nGold Reward: {enemy['gold']}")

#display all enemies
def show_all_enemies():
    print("\n==========ENEMY LIST==========")

    for enemy in ENEMIES:
        print(enemy["name"],"|Level:", enemy["level"],"| Region:",enemy["region"])


#Display all Bosses

def show_all_bosses():
    print("\n==============BOSS LIST=============")

    for boss in BOSSES:
        print(boss["name"],"| Level:",boss["level"],"| Region",boss["region"])


#Function to find enemy by name

def find_enemy(enemy_name):
    for enemy in ENEMIES:
        if enemy["name"].lower() == enemy_name.lower():
            return enemy.copy()
    return None


#Function to find boss by name

def find_boss(boss_name):
    for boss in BOSSES:
        if boss["name"].lower() == boss_name.lower():
            return boss.copy()
    return None

#function to get enemy based on the player's level

def get_enemy_level(player_level):
    available_enemies = []
    for enemy in ENEMIES:
        if enemy["level"] <= player_level:
            available_enemies.append(enemy)

    return available_enemies

# funtion to generate a random enemy

def generate_random_enemy(player_level):
    available_enemies = get_enemy_level(player_level)

    if not available_enemies:
        return ENEMIES[0].copy()

    enemy = random.choice(available_enemies).copy()

    if player_level > enemy["level"]:
        difference = player_level - enemy["level"]

        enemy["hp"] += difference * 10
        enemy["attack"] += difference * 2
        enemy["defense"] += difference

    enemy["level"] = player_level

    return enemy

#function to get boss based on player's level
def get_boss_level():
    for boss in BOSSES:
        if boss["level"] == player_level:
            return boss.copy()
    return None

#testing enemy system

if __name__ == "__main__":

    show_all_enemies()

    show_all_bosses()

    player_level = 10

    print("\nGenerating enemy for level",player_level)

    enemy = generate_random_enemy(player_level)

    display_enemy(enemy)




    
    