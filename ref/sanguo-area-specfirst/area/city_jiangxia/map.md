# 江夏

## Area Metadata

- AreaId: `city_jiangxia`
- Label: 江夏
- Type: city
- Region: 荊州 (`jingzhou`)
- Theme: 軍旅
- Subtheme: 水軍重鎮
- LevelRange: 28-42
- Tags: hub

## Prose Scaffold

Theme: 軍旅
Subtheme: 水軍重鎮
Mood: 秩序、煙火氣、地方勢力流動
Signature scenes:
- 城門
- 主街
- 市集
- 行人往來
NPC factions or roles:
- 守門兵
- 掌櫃
- 行人
- 差役
Quest hooks:
- 打聽地方消息
- 協助跑腿送信
- 追查城內異聞
Interaction cues:
- #Enquire 城門
- #Enquire 市集
- #Enquire 驛站
- #Enquire 官府
- #Keyword 告示
- #Keyword 招牌
- #Keyword 路牌
- #Keyword 城門
- #Job 跑腿
- #Job 巡查
- #Job 採買
Rumor seeds:
- 有人提到 江夏 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- north: `road_jingxiang` (outgoing)
- east: `fort_river_fort` (outgoing)
- east: `city_chaisang` (outgoing)
- south: `wild_yunmeng` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_jiangxia",
  "label": "江夏",
  "type": "city",
  "region": {
    "id": "jingzhou",
    "label": "荊州"
  },
  "theme": {
    "primary": "軍旅",
    "secondary": "水軍重鎮"
  },
  "levelRange": "28-42",
  "tags": [
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "north",
      "target": "road_jingxiang",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "fort_river_fort",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_chaisang",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "wild_yunmeng",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "城門",
      "市集",
      "驛站",
      "官府"
    ],
    "keyword": [
      "告示",
      "招牌",
      "路牌",
      "城門"
    ],
    "job": [
      "跑腿",
      "巡查",
      "採買"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "city_jiangxia:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_jiangxia:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_jiangxia:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_jiangxia:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_jiangxia.entry",
        "label": "入口節點",
        "cluster": "city_jiangxia:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_jiangxia.core",
        "label": "核心節點",
        "cluster": "city_jiangxia:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_jiangxia.service",
        "label": "服務 / 互動節點",
        "cluster": "city_jiangxia:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_jiangxia.link1",
        "label": "north 出口",
        "cluster": "city_jiangxia:gate",
        "kind": "world_link",
        "worldTarget": "road_jingxiang",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_jiangxia.link2",
        "label": "east 出口",
        "cluster": "city_jiangxia:gate",
        "kind": "world_link",
        "worldTarget": "fort_river_fort",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_jiangxia.link3",
        "label": "east 出口",
        "cluster": "city_jiangxia:gate",
        "kind": "world_link",
        "worldTarget": "city_chaisang",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_jiangxia.link4",
        "label": "south 出口",
        "cluster": "city_jiangxia:gate",
        "kind": "world_link",
        "worldTarget": "wild_yunmeng",
        "direction": "south",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_jiangxia.entry",
        "to": "city_jiangxia.link1",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jiangxia.entry",
        "to": "city_jiangxia.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jiangxia.entry",
        "to": "city_jiangxia.link3",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jiangxia.entry",
        "to": "city_jiangxia.link4",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jiangxia.entry",
        "to": "city_jiangxia.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_jiangxia.core",
        "to": "city_jiangxia.service",
        "direction": "branch",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "秩序、煙火氣、地方勢力流動",
    "signatureScenes": [
      "城門",
      "主街",
      "市集",
      "行人往來"
    ],
    "npcRoles": [
      "守門兵",
      "掌櫃",
      "行人",
      "差役"
    ],
    "questHooks": [
      "打聽地方消息",
      "協助跑腿送信",
      "追查城內異聞"
    ],
    "notes": [
      "這是 spec-first scaffold，先調整 prose 與 topology，再交給 generator。",
      "worldLinks 對應世界圖節點，不等於最終 room 出口數量。",
      "每個 world_link 可在 area 內展開成 1~3 個過渡房。"
    ]
  }
}
```

## Editing Notes

- 先維持 `mapmd-json` 是內部 schema，不要把 prose 寫成假 JSON。
- `topology.nodes` 是 AREA 內的最小節點 stub，後續可擴到真正房間。
- `worldLinks` 建議對應到 AREA 邊界房，而不是直接所有房都能外連。
- 若此區是 choke point，可把 world link 改成 gate / one_way / event gate。
- 若此區是秘境，建議加入條件節點或 `down / enter / pass` 型路徑。
