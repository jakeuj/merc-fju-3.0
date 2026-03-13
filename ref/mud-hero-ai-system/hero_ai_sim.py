
import random

heroes=["曹操","劉備","孫權","呂布","諸葛亮"]
actions=["attack","defend","duel","plan","recruit"]

def simulate():
    for i in range(10):
        h=random.choice(heroes)
        a=random.choice(actions)
        print(f"{h} performs action: {a}")

if __name__=="__main__":
    simulate()
