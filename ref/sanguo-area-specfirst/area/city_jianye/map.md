# 建業

## Area Metadata

- AreaId: `city_jianye`
- Label: 建業
- Type: city
- Region: 江東 (`jiangdong`)
- Theme: 歷史城市
- Subtheme: 江東都城
- LevelRange: 30-44
- Tags: hub, capital

## Prose Scaffold

Theme: 歷史城市
Subtheme: 江東都城
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
- 有人提到 建業 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- north: `city_shouchun` (outgoing)
- east: `district_jianye_port` (outgoing)
- south: `fort_naval_base` (outgoing)
- west: `wild_jianye_west` (outgoing)
- east: `city_kuaiji` (outgoing)
- south: `wild_river_delta` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_jianye",
  "label": "建業",
  "type": "city",
  "region": {
    "id": "jiangdong",
    "label": "江東"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "江東都城"
  },
  "levelRange": "30-44",
  "tags": [
    "hub",
    "capital"
  ],
  "worldLinks": [
    {
      "direction": "north",
      "target": "city_shouchun",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "district_jianye_port",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "fort_naval_base",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "wild_jianye_west",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_kuaiji",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "wild_river_delta",
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
        "id": "city_jianye:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_jianye:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_jianye:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_jianye:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_jianye.entry",
        "label": "入口節點",
        "cluster": "city_jianye:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_jianye.core",
        "label": "核心節點",
        "cluster": "city_jianye:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_jianye.service",
        "label": "服務 / 互動節點",
        "cluster": "city_jianye:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_jianye.link1",
        "label": "north 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "city_shouchun",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_jianye.link2",
        "label": "east 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "district_jianye_port",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_jianye.link3",
        "label": "south 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "fort_naval_base",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "city_jianye.link4",
        "label": "west 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "wild_jianye_west",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_jianye.link5",
        "label": "east 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "city_kuaiji",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_jianye.link6",
        "label": "south 出口",
        "cluster": "city_jianye:gate",
        "kind": "world_link",
        "worldTarget": "wild_river_delta",
        "direction": "south",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link1",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link3",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link4",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link5",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.link6",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_jianye.entry",
        "to": "city_jianye.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_jianye.core",
        "to": "city_jianye.service",
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
