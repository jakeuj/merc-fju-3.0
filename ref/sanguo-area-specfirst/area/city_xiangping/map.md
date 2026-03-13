# 襄平

## Area Metadata

- AreaId: `city_xiangping`
- Label: 襄平
- Type: city
- Region: 幽州遼東 (`youzhou`)
- Theme: 軍旅
- Subtheme: 遼東邊城
- LevelRange: 34-46
- Tags: hub

## Prose Scaffold

Theme: 軍旅
Subtheme: 遼東邊城
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
- 有人提到 襄平 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `wild_barbarian_camp` (outgoing)
- north: `wild_liaodong_plain` (outgoing)
- north: `road_north_border` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_xiangping",
  "label": "襄平",
  "type": "city",
  "region": {
    "id": "youzhou",
    "label": "幽州遼東"
  },
  "theme": {
    "primary": "軍旅",
    "secondary": "遼東邊城"
  },
  "levelRange": "34-46",
  "tags": [
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "wild_barbarian_camp",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "wild_liaodong_plain",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "road_north_border",
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
        "id": "city_xiangping:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_xiangping:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_xiangping:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_xiangping:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_xiangping.entry",
        "label": "入口節點",
        "cluster": "city_xiangping:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_xiangping.core",
        "label": "核心節點",
        "cluster": "city_xiangping:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_xiangping.service",
        "label": "服務 / 互動節點",
        "cluster": "city_xiangping:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_xiangping.link1",
        "label": "west 出口",
        "cluster": "city_xiangping:gate",
        "kind": "world_link",
        "worldTarget": "wild_barbarian_camp",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "city_xiangping.link2",
        "label": "north 出口",
        "cluster": "city_xiangping:gate",
        "kind": "world_link",
        "worldTarget": "wild_liaodong_plain",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "city_xiangping.link3",
        "label": "north 出口",
        "cluster": "city_xiangping:gate",
        "kind": "world_link",
        "worldTarget": "road_north_border",
        "direction": "north",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_xiangping.entry",
        "to": "city_xiangping.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "city_xiangping.entry",
        "to": "city_xiangping.link2",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_xiangping.entry",
        "to": "city_xiangping.link3",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_xiangping.entry",
        "to": "city_xiangping.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_xiangping.core",
        "to": "city_xiangping.service",
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
