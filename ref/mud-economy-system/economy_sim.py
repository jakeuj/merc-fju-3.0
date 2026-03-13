
import random

cities={
"洛陽":{"grain":100,"weapon":50},
"襄陽":{"grain":120,"military":60},
"建業":{"fish":200,"ship":20}
}

def simulate_trade():

    city=random.choice(list(cities.keys()))
    resource=random.choice(list(cities[city].keys()))

    change=random.randint(-10,10)
    cities[city][resource]+=change

    print(f"{city} {resource} change {change}")
    print(cities)

for i in range(10):
    simulate_trade()
