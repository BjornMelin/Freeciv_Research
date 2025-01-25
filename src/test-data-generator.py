import random

# global variable for the random operator used to make calls to random shorter
r = random


# get a random value of gold based on turn segment
def get_gold(x):
    g = 0
    if x <= 100:
        g = r.randint(0, 6)
    if (x <= 200) & (x > 100):
        g = r.randint(5, 16)
    if (x <= 300) & (x > 200):
        g = r.randint(15, 31)
    return g


# get a random gov type based on turn number
def get_gov_type(x):
    type = 0
    if x <= 100:
        return type
    if (x <= 150) & (x > 100):
        type = 1
    if x > 150:
        type = r.randint(2, 4)
    return type


# get a random number of cities built per turn
def get_num_cities(x):
    cities = 0
    if x % 6 == 0:
        cities = r.randint(0, 1)
    return cities


# get a random increase in the tech level
def get_tech_level(x):
    level = 0
    if x % 5 == 0:
        level = 1
    return level


# get a random number of allies
# or lose some if value is lower than last turn's
def get_num_allies(x):
    allies = r.randint(0, 3)
    return allies


# get a random of enemies per turn based on number of allies
def get_num_enemies(x):
    enemies = 7 - x
    return enemies


# determine if enemies are near
def get_enemies_near():
    chance = r.randint(0, 100)
    near = 0
    if chance >= 70:
        near = 1
    return near


def generate_data():
    # open/create file for the turn data
    file = open("TurnData.txt", "w+")

    # ptsh (previous tech score holder) is used to contain tech score from previous turn
    gold = 0
    num_cities = 0
    tech_level = 0

    # loop to fill in data and write it to file for 300 turns
    for x in range(300):
        gold += get_gold(x)
        government = get_gov_type(x)
        num_cities += get_num_cities(x)
        tech_level += get_tech_level(x)
        num_allies = get_num_allies(x)
        num_enemies = get_num_enemies(num_allies)
        enemies_near = get_enemies_near()

        if x % 15 == 0:
            gold = 0

        # convert the values into a string to be written to the file
        turnValues = "{g},{gov},{nc},{tl},{na},{ne},{en}\n".format(
            g=str(gold),
            gov=str(government),
            nc=str(num_cities),
            tl=str(tech_level),
            na=str(num_allies),
            ne=str(num_enemies),
            en=str(enemies_near),
        )
        # write the values to the file
        file.write(turnValues)

    # close the file
    file.close()


generate_data()
