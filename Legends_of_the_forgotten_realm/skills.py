SKILLS = [
    {"name": "Power Strike",
        "type": "attack",
        "damage": 30,
        "mana_cost": 10,
        "required_level": 1,
        "description": "A powerful physical attack."},

    { "name": "Fireball",
        "type": "attack",
        "damage": 50,
        "mana_cost": 20,
        "required_level": 3,
        "description": "Launches a ball of fire at the enemy."},

    {"name": "Healing Light",
        "type": "heal",
        "healing": 40,
        "mana_cost": 15,
        "required_level": 2,
        "description": "Restores the player's HP."},

    { "name": "Thunder Strike",
        "type": "attack",
        "damage": 80,
        "mana_cost": 30,
        "required_level": 5,
        "description": "Strikes the enemy with lightning."},

    {"name": "Greater Heal",
        "type": "heal",
        "healing": 100,
        "mana_cost": 35,
        "required_level": 8,
        "description": "Restores a large amount of HP."}
]


#get available skills

def get_available_skills(player_level):

    available_skills = []

    for skill in SKILLS:
        if skill["required_level"] <= player_level:
            available_skills.append(skill)

    return available_skills

#function to display availabe skills

def show_skills(player):
    print("\n============== AVAILABLE SKILLS ================")

    available_skills = get_available_skills(player["level"])

    for skill in available_skills:
        print("\nName:", skill["name"])
        print("Type:", skill["type"])
        print("Mana Cost:", skill["mana_cost"])
        print("Description:", skill["description"])

        if skill["type"] == "attack":
            print("Damage:", skill["damage"])

        elif skill["type"] == "heal":
            print("Healing:", skill["healing"])


#find a skill

def find_skill(skill_name):
    for skill in SKILLS:
        if skill["name"].lower() == skill_name.lower():
            return skill.copy()

    return None

#use a skill

def use_skill(player,enemy,skill_name):

    skill = find_skill(skill_name)

    #check whether the skill exists or not
    if skill is None:
        print("Skill not found!")
        return False

    # Check the player's level

    if player["level"] < skill["required_level"]:
        print("Your level is too low to use this skill!")
        return False

    # Check mana
    if player["mana"] < skill["mana_cost"]:
        print("Not enough mana!")
        return False

    # Spend mana
    player["mana"] -= skill["mana_cost"]

    print("\nYou used", skill["name"] + "!")
    print("Mana consumed:", skill["mana_cost"])

    # Attack skill
    if skill["type"] == "attack":

        damage = skill["damage"] + player["attack"]

        damage = max(1, damage - enemy["defense"])

        enemy["hp"] = max(0, enemy["hp"] - damage)

        print("Damage dealt:", damage)
        print("Enemy HP:", enemy["hp"], "/", enemy.get("max_hp", enemy["hp"]))

    # Healing skill
    elif skill["type"] == "heal":

        old_hp = player["hp"]

        player["hp"] = min(
            player["hp"] + skill["healing"],
            player["max_hp"]
        )

        recovered = player["hp"] - old_hp

        print("HP recovered:", recovered)
        print("Your HP:", player["hp"], "/", player["max_hp"])

    print("Remaining Mana:", player["mana"], "/", player["max_mana"])

    return True

#test

if __name__ == "__main__":

    player = {
        "name": "Arin",
        "level": 5,
        "hp": 100,
        "max_hp": 100,
        "mana": 100,
        "max_mana": 100,
        "attack": 20,
        "defense": 10
    }

    enemy = {
        "name": "Goblin",
        "hp": 100,
        "max_hp": 100,
        "attack": 15,
        "defense": 5
    }

    show_skills(player)

    use_skill(player, enemy, "Fireball")
    