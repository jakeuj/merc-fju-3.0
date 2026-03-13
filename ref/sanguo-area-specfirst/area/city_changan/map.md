# 長安

## Area Metadata

- AreaId: `city_changan`
- Label: 長安
- Type: city
- Region: 關中西域 (`guanzhong`)
- Theme: 歷史城市
- Subtheme: 關中都城
- LevelRange: 18-30
- Tags: hub

## Prose Scaffold

Theme: 歷史城市
Subtheme: 關中都城
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
- 有人提到 長安 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_anding` (outgoing)
- east: `city_hongnong` (outgoing)
- enter: `district_changan_palace` (outgoing)
- west: `district_changan_west_market` (outgoing)
- north: `district_changan_noble` (outgoing)
- south: `wild_changan_outer` (outgoing)
- out: `road_return_changan` (outgoing)
- east: `fort_hangu` (outgoing)
- west: `road_western_trade` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_changan",
  "label": "長安",
  "type": "city",
  "region": {
    "id": "guanzhong",
    "label": "關中西域"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "關中都城"
  },
  "levelRange": "18-30",
  "tags": [
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_anding",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_hongnong",
      "kind": "outgoing"
    },
    {
      "direction": "enter",
      "target": "district_changan_palace",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "district_changan_west_market",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "district_changan_noble",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "wild_changan_outer",
      "kind": "outgoing"
    },
    {
      "direction": "out",
      "target": "road_return_changan",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "fort_hangu",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "road_western_trade",
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
        "id": "city_changan:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_changan:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_changan:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_changan:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_changan.entry",
        "label": "入口節點",
        "cluster": "city_changan:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_changan.core",
        "label": "核心節點",
        "cluster": "city_changan:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_changan.service",
        "label": "服務 / 互動節點",
        "cluster": "city_changan:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_changan.link1",
        "label": "west 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "city_anding",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_changan.link2",
        "label": "east 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "city_hongnong",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_changan.link3",
        "label": "enter 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "district_changan_palace",
        "direction": "enter",
        "io": "out"
      },
      {
        "id": "city_changan.link4",
        "label": "west 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "district_changan_west_market",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_changan.link5",
        "label": "north 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "district_changan_noble",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_changan.link6",
        "label": "south 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "wild_changan_outer",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "city_changan.link7",
        "label": "out 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "road_return_changan",
        "direction": "out",
        "io": "out"
      },
      {
        "id": "city_changan.link8",
        "label": "east 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "fort_hangu",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_changan.link9",
        "label": "west 出口",
        "cluster": "city_changan:gate",
        "kind": "world_link",
        "worldTarget": "road_western_trade",
        "direction": "west",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_changan.entry",
        "to": "city_changan.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link3",
        "direction": "enter",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link4",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link5",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link6",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link7",
        "direction": "out",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link8",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.link9",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_changan.entry",
        "to": "city_changan.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_changan.core",
        "to": "city_changan.service",
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
