
import random

npc_types=["bandit","guard","merchant","refugee","beast","spirit"]
areas=["road","city","wild","dungeon"]

def spawn(area):
    if area=="road":
        return random.choice(["merchant","bandit"])
    if area=="city":
        return random.choice(["guard","merchant","refugee"])
    if area=="wild":
        return random.choice(["bandit","beast"])
    if area=="dungeon":
        return random.choice(["spirit","beast"])

def simulate():
    for tick in range(10):
        area=random.choice(areas)
        npc=spawn(area)
        print(f"spawn {npc} in {area}")

if __name__=="__main__":
    simulate()
