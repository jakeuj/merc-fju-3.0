
# 三國 MUD AI 地圖生成器

這是一個 **AI world generator scaffold**，可以根據簡單設定自動生成：

- Areas
- Clusters
- Rooms
- 基本 NPC / Quest hooks

設計用途：

```
region: 荊州
theme: swamp / war / ruins
areas: 8
```

生成：

```
8 areas
40 clusters
200+ rooms
```

---

## 使用方式

```
python ai_map_gen.py config.json
```

範例 config.json

{
  "region": "荊州",
  "theme": ["swamp","war","ruins"],
  "areas": 5
}
