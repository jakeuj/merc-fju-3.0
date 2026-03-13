
# 三國 MUD World Builder

這是一個簡單的 **世界生成器 scaffold**，可以從 `world-graph.json` 自動生成：

- AREA scaffold
- Cluster scaffold
- Room scaffold

設計流程：

world-graph.json
↓
AREA
↓
CLUSTER
↓
ROOM

典型規模：

120 AREA
≈ 400 clusters
≈ 2500–3500 rooms

---

## 使用方式

1. 放入 world-graph.json
2. 執行

```bash
python world_builder.py world-graph.json
```

生成結果：

```
world/
  area/
     city_loyang/
        clusters/
        rooms/
```

---

## Cluster 規則

City
- gate
- main_street
- market
- palace

Wild
- entrance
- landmark
- hidden_path

Dungeon
- entry
- corridor
- trap_room
- boss_room
