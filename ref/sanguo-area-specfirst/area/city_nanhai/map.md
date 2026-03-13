# 南海

## Area Metadata

- AreaId: `city_nanhai`
- Label: 南海
- Type: city
- Region: 荊南南蠻 (`south`)
- Theme: 探險遺跡
- Subtheme: 海港 / 遠航
- LevelRange: 40-54
- Tags: hub

## Prose Scaffold

Theme: 探險遺跡
Subtheme: 海港 / 遠航
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
- 有人提到 南海 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- north: `city_guiyang` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_nanhai",
  "label": "南海",
  "type": "city",
  "region": {
    "id": "south",
    "label": "荊南南蠻"
  },
  "theme": {
    "primary": "探險遺跡",
    "secondary": "海港 / 遠航"
  },
  "levelRange": "40-54",
  "tags": [
    "hub"
  ],
  "worldLinks": [
    {
      "direction": "north",
      "target": "city_guiyang",
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
        "id": "city_nanhai:gate",
        "label": "城門入口",
        "role": "gate"
      },
      {
        "id": "city_nanhai:main_street",
        "label": "主街中心",
        "role": "main_street"
      },
      {
        "id": "city_nanhai:service_quarter",
        "label": "服務區",
        "role": "service_quarter"
      },
      {
        "id": "city_nanhai:branch_zone",
        "label": "支線區",
        "role": "branch_zone"
      }
    ],
    "nodes": [
      {
        "id": "city_nanhai.entry",
        "label": "入口節點",
        "cluster": "city_nanhai:gate",
        "kind": "room_stub"
      },
      {
        "id": "city_nanhai.core",
        "label": "核心節點",
        "cluster": "city_nanhai:main_street",
        "kind": "room_stub"
      },
      {
        "id": "city_nanhai.service",
        "label": "服務 / 互動節點",
        "cluster": "city_nanhai:service_quarter",
        "kind": "room_stub"
      },
      {
        "id": "city_nanhai.link1",
        "label": "north 出口",
        "cluster": "city_nanhai:gate",
        "kind": "world_link",
        "worldTarget": "city_guiyang",
        "direction": "north",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "city_nanhai.entry",
        "to": "city_nanhai.link1",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "city_nanhai.entry",
        "to": "city_nanhai.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "city_nanhai.core",
        "to": "city_nanhai.service",
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
