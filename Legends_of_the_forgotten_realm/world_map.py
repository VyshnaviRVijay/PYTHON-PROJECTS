
#Regions in map
WORLD_MAP = [
    {"name":"Village","required_level":1,"boss_level":0,"unlocked":True},
    {"name":"Forest","required_level":1,"boss_level":10,"unlocked":False},
    {"name":"Cave","required_level":10,"boss_level":20,"unlocked":False},
    {"name":"Desert","required_level":20,"boss_level":30,"unlocked":False},
    {"name":"Ruins","required_level":30,"boss_level":40,"unlocked":False},
    {"name":"Castle","required_level":40,"boss_level":50,"unlocked":False},
    {"name":"Volcano","required_level":50,"boss_level":60,"unlocked":False},
    {"name":"Frozen Mountain","required_level":60,"boss_level":70,"unlocked":False},
    {"name":"Sky Temple","required_level":70,"boss_level":80,"unlocked":False},
    {"name":"Demon Realm","required_level":80,"boss_level":90,"unlocked":False}
]

#function to display map
def show_map(player):
    print("\n==========WORLD MAP=========")

    current_region = player.get("current_region","Village")
    for index,region in enumerate(WORLD_MAP):
        if region["unlocked"]:
            status = "Unlocked"
        else:
            status = "Locked"

        if region["name"] == current_region:
            status = "Current Region"

        print(index, ".", region["name"],"|",status)


#checking whether region iis unlocked or not
def unlock_region(region_name):
    for region in WORLD_MAP:
        if region["name"].lower() == region_name.lower():
            region["unlocked"] = True

            print("\n",region["name"], "has been unlocked")
            return True
        else:
            print("Region not found")
            return False

#function for travelling to a region
def travel_to_region(player, region_name):
    for region in WORLD_MAP:
        if region["name"].lower() == region_name.lower():
            if not region["unlocked"]:
                print("\nThis region is locked!")
                print("Defeat the required boss to unlock it.")
                return False

            if player["level"] < region["required_level"]:
                print("\nYour level is too low!")
                print("Required level:",region["required_level"])
                return False

            player["current_region"] = region["name"]

            print("\nYou travelled to", region["name"] + "!")

            return True

    print("\nInvalid region name.")

    return False

#unlock next region after boss defeat
# boss levels are 10,20,30 and so on
# each bosses unlocks next region
def unlock_next_region(defeated_boss_level):
    next_index = None  

    for index, region in enumerate(WORLD_MAP):
        if region["boss_level"] == defeated_boss_level:
            next_index = index + 1
            break  

    if next_index is not None:
        if next_index < len(WORLD_MAP):
            next_region = WORLD_MAP[next_index]
            next_region["unlocked"] = True
            print("\n New Region Unlocked:", next_region["name"])
            return next_region["name"]
        else:
            print("\nYou have unlocked the final region!")
            return None

    print("\nNo region is linked to this boss level")
    return None 


if __name__ == "__main__":

    player = {
        "name": "Arin",
        "level": 10,
        "current_region": "Village"
    }

    # Unlock the starting region
    WORLD_MAP[0]["unlocked"] = True

    # Display map
    show_map(player)

    # Travel to Village
    travel_to_region(player, "Village")

    # Simulate defeating the level 10 boss
    unlock_next_region(10)

    # Display updated map
    show_map(player)

    # Travel to Forest
    travel_to_region(player, "Forest")