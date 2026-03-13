
# 洛陽東郊 (wild_loyang_east)

這是一個 **高品質 AREA 模板範例**，展示如何把 `world-graph.json` 的節點轉為 **Merc-FJU / mapmd-json spec‑first AREA**。  
此格式可直接作為其他 AREA 的複製模板。

---

# Area Metadata

- AreaId: `wild_loyang_east`
- Label: 洛陽東郊
- Type: outskirts
- Region: 中原 (zhongyuan)
- Theme: 江湖
- Subtheme: 城郊 / 官道 / 初級探索
- LevelRange: 1-12
- Tags: starter, outskirts, road

---

# Area Concept

洛陽東郊是玩家離開洛陽城後接觸的第一個野外區域。

此區域具有三個設計目的：

1. **新手探索區**
2. **世界拓撲過渡區**
3. **江湖事件入口**

玩家會在這裡遇到：

- 小股流寇
- 路過商旅
- 茶亭說書人
- 可疑的森林小徑

---

# Mood

城外的空氣帶著塵土與草木氣味。  
遠處可見洛陽城牆輪廓。  
官道上偶爾有商隊經過。

---

# Signature Scenes

- 官道岔路
- 十里茶亭
- 林間小徑
- 荒廢路碑

---

# NPC Roles

- 巡邏守兵
- 茶亭掌櫃
- 路過商旅
- 可疑流寇

---

# Quest Hooks

- 協助巡邏兵清理流寇
- 護送商旅到洛陽城
- 調查林間怪聲

---

# Interaction Cues

```
#Enquire 洛陽
#Enquire 官道
#Enquire 茶亭

#Keyword 路碑
#Keyword 林徑
#Keyword 流寇

#Job 巡邏
#Job 護送
```

---

# World Links

| direction | target |
|---|---|
| west | city_loyang |
| east | wild_longqu_hills |
| north | wild_fengqiu_forest |
| south | wild_farming_village |

---

# mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_loyang_east",
  "label": "洛陽東郊",
  "type": "outskirts",
  "region": {
    "id": "zhongyuan",
    "label": "中原"
  },
  "theme": {
    "primary": "江湖",
    "secondary": "城郊探索"
  },
  "levelRange": "1-12",
  "tags": ["starter","outskirts","road"],
  "worldLinks": [
    {"direction":"west","target":"city_loyang"},
    {"direction":"east","target":"wild_longqu_hills"},
    {"direction":"north","target":"wild_fengqiu_forest"},
    {"direction":"south","target":"wild_farming_village"}
  ],
  "interactionHints": {
    "enquire": ["洛陽","官道","茶亭"],
    "keyword": ["路碑","林徑","流寇"],
    "job": ["巡邏","護送"]
  },
  "topology": {
    "clusters": [
      {"id":"wild_loyang_east:entry","label":"城外官道入口"},
      {"id":"wild_loyang_east:road","label":"主官道"},
      {"id":"wild_loyang_east:tea","label":"十里茶亭"},
      {"id":"wild_loyang_east:forest","label":"林間小徑"}
    ],
    "nodes":[
      {"id":"wild_loyang_east.entry","cluster":"wild_loyang_east:entry"},
      {"id":"wild_loyang_east.crossroad","cluster":"wild_loyang_east:road"},
      {"id":"wild_loyang_east.teahouse","cluster":"wild_loyang_east:tea"},
      {"id":"wild_loyang_east.forest_path","cluster":"wild_loyang_east:forest"}
    ],
    "edges":[
      {"from":"wild_loyang_east.entry","to":"wild_loyang_east.crossroad"},
      {"from":"wild_loyang_east.crossroad","to":"wild_loyang_east.teahouse"},
      {"from":"wild_loyang_east.crossroad","to":"wild_loyang_east.forest_path"}
    ]
  }
}
```

---

# Suggested Room Layout

```
洛陽城門
   │
城外官道入口
   │
官道岔路
 ├── 十里茶亭
 └── 林間小徑
```

---

# Design Notes

這個 AREA 的重點是 **過渡與探索**。

建議房間數量：

- 6~12 rooms

建議怪物：

- 流寇
- 野狗

建議事件：

- 商隊護送
- 流寇伏擊
