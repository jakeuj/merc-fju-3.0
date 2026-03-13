# 洛陽

## Area Metadata

- AreaId: `city_loyang`
- Label: 洛陽
- Type: city
- Region: 中原 (`zhongyuan`)
- Theme: 歷史城市
- Subtheme: 帝都 / 新手主城
- LevelRange: 1-15
- Tags: capital, hub

## Prose Scaffold

Theme: 歷史城市
Subtheme: 帝都 / 新手主城
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
- 有人提到 洛陽 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `fort_hulao` (outgoing)
- east: `city_chenliu` (outgoing)
- enter: `district_loyang_palace` (outgoing)
- east: `district_loyang_east_market` (outgoing)
- west: `district_loyang_west_market` (outgoing)
- north: `district_loyang_scholar` (outgoing)
- east: `wild_loyang_east` (outgoing)
- north: `road_puyang` (outgoing)
- south: `road_wan` (outgoing)
- east: `road_chenliu` (outgoing)
- down: `dng_loyang_sewer` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_loyang",
  "label": "洛陽",
  "type": "city",
  "region": {
    "id": "zhongyuan",
    "label": "中原"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "帝都 / 新手主城"
  },
  "levelRange": "1-15",
  "tags": [
    "capital",
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "fort_hulao",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_chenliu",
      "kind": "outgoing"
    },
    {
      "direction": "enter",
      "target": "district_loyang_palace",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "district_loyang_east_market",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "district_loyang_west_market",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "district_loyang_scholar",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "wild_loyang_east",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "road_puyang",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "road_wan",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "road_chenliu",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "dng_loyang_sewer",
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
        "id": "city_loyang:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_loyang:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_loyang:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_loyang:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_loyang.entry",
        "label": "入口節點",
        "cluster": "city_loyang:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_loyang.core",
        "label": "核心節點",
        "cluster": "city_loyang:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_loyang.service",
        "label": "服務 / 互動節點",
        "cluster": "city_loyang:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_loyang.link1",
        "label": "west 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "fort_hulao",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_loyang.link2",
        "label": "east 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "city_chenliu",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_loyang.link3",
        "label": "enter 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "district_loyang_palace",
        "direction": "enter",
        "io": "out"
      },
      {
        "id": "city_loyang.link4",
        "label": "east 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "district_loyang_east_market",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_loyang.link5",
        "label": "west 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "district_loyang_west_market",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_loyang.link6",
        "label": "north 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "district_loyang_scholar",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_loyang.link7",
        "label": "east 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "wild_loyang_east",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_loyang.link8",
        "label": "north 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "road_puyang",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_loyang.link9",
        "label": "south 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "road_wan",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "city_loyang.link10",
        "label": "east 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "road_chenliu",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "city_loyang.link11",
        "label": "down 出口",
        "cluster": "city_loyang:gate",
        "kind": "world_link",
        "worldTarget": "dng_loyang_sewer",
        "direction": "down",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link3",
        "direction": "enter",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link4",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link5",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link6",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link7",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link8",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link9",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link10",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.link11",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "city_loyang.entry",
        "to": "city_loyang.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_loyang.core",
        "to": "city_loyang.service",
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
