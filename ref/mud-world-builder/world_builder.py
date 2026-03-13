
import json
import sys
from pathlib import Path

def generate(world_file):
    data = json.load(open(world_file,"r",encoding="utf-8"))
    base = Path("world")
    base.mkdir(exist_ok=True)

    for node in data["nodes"]:
        area = base / "area" / node["id"]
        (area / "clusters").mkdir(parents=True,exist_ok=True)
        (area / "rooms").mkdir(parents=True,exist_ok=True)

        with open(area / "area.md","w",encoding="utf-8") as f:
            f.write(f"# {node['label']} ({node['id']})\n")
            f.write(f"type: {node['type']}\n")
            f.write("\n## Clusters\n")

        # simple cluster generation
        clusters = ["entry","main","landmark"]
        for c in clusters:
            cfile = area / "clusters" / f"{c}.md"
            with open(cfile,"w",encoding="utf-8") as f:
                f.write(f"# cluster:{c}\n")

        # room scaffold
        for i in range(5):
            rfile = area / "rooms" / f"room_{i}.md"
            with open(rfile,"w",encoding="utf-8") as f:
                f.write(f"# room {i}\n")

if __name__ == "__main__":
    generate(sys.argv[1])
