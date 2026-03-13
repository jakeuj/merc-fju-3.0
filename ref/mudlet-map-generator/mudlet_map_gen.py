
import json
import sys
from pathlib import Path

def generate(world_file):
    data = json.load(open(world_file,"r",encoding="utf-8"))
    
    rooms=[]
    exits=[]
    
    for i,node in enumerate(data["nodes"]):
        rooms.append(f"{i},{node['id']},{node['label']},{node['type']}")
    
    node_index={n["id"]:i for i,n in enumerate(data["nodes"])}
    
    for e in data["edges"]:
        a=node_index[e["from"]]
        b=node_index[e["to"]]
        d=e.get("dir","link")
        exits.append(f"{a},{b},{d}")
    
    Path("rooms.csv").write_text("\n".join(rooms),encoding="utf-8")
    Path("exits.csv").write_text("\n".join(exits),encoding="utf-8")

if __name__=="__main__":
    generate(sys.argv[1])
