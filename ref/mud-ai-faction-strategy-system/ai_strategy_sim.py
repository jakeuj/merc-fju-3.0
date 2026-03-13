
import random
import json

factions = ["wei","shu","wu"]

territories = {
 "洛陽":"wei",
 "襄陽":"shu",
 "建業":"wu",
 "長安":"wei",
 "成都":"shu"
}

def choose_target(faction):
    enemies=[k for k,v in territories.items() if v!=faction]
    return random.choice(enemies)

def simulate_turn():

    faction=random.choice(factions)
    target=choose_target(faction)

    attacker=faction
    defender=territories[target]

    print(f"{attacker} attacks {target} controlled by {defender}")

    if random.random()>0.5:
        territories[target]=attacker
        print("attacker wins")
    else:
        print("defender holds")

def run():

    for i in range(10):
        simulate_turn()
        print("territories:",territories)

if __name__=="__main__":
    run()
