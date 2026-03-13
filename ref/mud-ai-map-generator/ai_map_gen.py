
import json
from pathlib import Path
import random

CLUSTERS = ["entry","path","landmark","danger","hidden"]
ROOM_TYPES = ["road","camp","ruin","forest","cave","temple"]

def generate(cfg):

    region = cfg["region"]
    areas = cfg["areas"]

    base = Path("generated_world") / region
    base.mkdir(parents=True,exist_ok=True)

    for a in range(areas):

        area_id=f"{region}_area_{a}"
        area=base/area_id
        (area/"clusters").mkdir(parents=True,exist_ok=True)
        (area/"rooms").mkdir(exist_ok=True)

        with open(area/"area.md","w",encoding="utf-8") as f:
            f.write(f"# {area_id}\n")

        # clusters
        for c in CLUSTERS:

            with open(area/"clusters"/f"{c}.md","w",encoding="utf-8") as f:
                f.write(f"# cluster:{c}\n")

            # rooms
            for r in range(random.randint(3,6)):
                room=f"{c}_{r}.md"
                with open(area/"rooms"/room,"w",encoding="utf-8") as f:
                    rtype=random.choice(ROOM_TYPES)
                    f.write(f"# room:{rtype}\n")

if __name__=="__main__":

    cfg=json.load(open("config.json","r",encoding="utf-8"))
    generate(cfg)
