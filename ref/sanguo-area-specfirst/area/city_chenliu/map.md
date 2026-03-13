# 陳留

## Area Metadata

- AreaId: `city_chenliu`
- Label: 陳留
- Type: city
- Region: 兗州河北 (`yanzhao`)
- Theme: 歷史城市
- Subtheme: 中原樞紐城
- LevelRange: 15-26
- Tags: hub

## Prose Scaffold

Theme: 歷史城市
Subtheme: 中原樞紐城
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
- 有人提到 陳留 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_loyang` (outgoing)
- east: `city_xuzhou` (outgoing)
- south: `district_chenliu_station` (outgoing)
- west: `wild_chenliu_west` (outgoing)
- west: `road_chenliu_loyang` (outgoing)
- north: `city_puyang` (outgoing)
- west: `road_chenliu` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_chenliu",
  "label": "陳留",
  "type": "city",
  "region": {
    "id": "yanzhao",
    "label": "兗州河北"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "中原樞紐城"
  },
  "levelRange": "15-26",
  "tags": [
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_loyang",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_xuzhou",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "district_chenliu_station",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "wild_chenliu_west",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "road_chenliu_loyang",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "city_puyang",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "road_chenliu",
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
        "id": "city_chenliu:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_chenliu:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_chenliu:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_chenliu:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_chenliu.entry",
        "label": "入口節點",
        "cluster": "city_chenliu:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_chenliu.core",
        "label": "核心節點",
        "cluster": "city_chenliu:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_chenliu.service",
        "label": "服務 / 互動節點",
        "cluster": "city_chenliu:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_chenliu.link1",
        "label": "west 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "city_loyang",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_chenliu.link2",
        "label": "east 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "city_xuzhou",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_chenliu.link3",
        "label": "south 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "district_chenliu_station",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "city_chenliu.link4",
        "label": "west 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "wild_chenliu_west",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_chenliu.link5",
        "label": "west 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "road_chenliu_loyang",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_chenliu.link6",
        "label": "north 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "city_puyang",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_chenliu.link7",
        "label": "west 出口",
        "cluster": "city_chenliu:gate",
        "kind": "world_link",
        "worldTarget": "road_chenliu",
        "direction": "west",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link3",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link4",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link5",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link6",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.link7",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_chenliu.entry",
        "to": "city_chenliu.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_chenliu.core",
        "to": "city_chenliu.service",
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
