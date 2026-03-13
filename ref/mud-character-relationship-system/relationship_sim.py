
import random

relationships=[
("曹操","夏侯惇","command"),
("劉備","關羽","brother"),
("劉備","孫權","ally"),
("曹操","劉備","enemy")
]

def simulate_event():
    a,b,rel=random.choice(relationships)
    print(f"Event triggered between {a} and {b}: relation={rel}")

for i in range(10):
    simulate_event()
