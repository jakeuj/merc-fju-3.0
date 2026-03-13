# 西行商道

## Area Metadata

- AreaId: `road_western_trade`
- Label: 西行商道
- Type: road
- Region: 關中西域 (`guanzhong`)
- Theme: 歷史城市
- Subtheme: 通西域商道
- LevelRange: 20-32
- Tags: connector

## Prose Scaffold

Theme: 歷史城市
Subtheme: 通西域商道
Mood: 旅途中轉、消息流通
Signature scenes:
- 路亭
- 驛站牌
- 分岔口
NPC factions or roles:
- 驛卒
- 旅人
- 押鏢人
Quest hooks:
- 問路
- 護送
- 攔查可疑過客
Interaction cues:
- #Enquire 去路
- #Enquire 驛站
- #Enquire 下一站
- #Keyword 路牌
- #Keyword 驛站
- #Keyword 木樁
- #Job 問路
- #Job 護送
- #Job 盤查過客
Rumor seeds:
- 有人提到 西行商道 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- east: `city_changan` (outgoing)
- west: `wild_salt_road` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "road_western_trade",
  "label": "西行商道",
  "type": "road",
  "region": {
    "id": "guanzhong",
    "label": "關中西域"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "通西域商道"
  },
  "levelRange": "20-32",
  "tags": [
    "connector"
  ],
  "worldLinks": [
    {
      "direction": "east",
      "target": "city_changan",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "wild_salt_road",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "去路",
      "驛站",
      "下一站"
    ],
    "keyword": [
      "路牌",
      "驛站",
      "木樁"
    ],
    "job": [
      "問路",
      "護送",
      "盤查過客"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "road_western_trade:junction",
        "label": "路口",
        "role": "junction"
      },
      {
        "id": "road_western_trade:midway",
        "label": "中段區",
        "role": "midway"
      },
      {
        "id": "road_western_trade:rest_stop",
        "label": "歇腳點",
        "role": "rest_stop"
      }
    ],
    "nodes": [
      {
        "id": "road_western_trade.entry",
        "label": "入口節點",
        "cluster": "road_western_trade:junction",
        "kind": "room_stub"
      },
      {
        "id": "road_western_trade.core",
        "label": "核心節點",
        "cluster": "road_western_trade:midway",
        "kind": "room_stub"
      },
      {
        "id": "road_western_trade.service",
        "label": "服務 / 互動節點",
        "cluster": "road_western_trade:rest_stop",
        "kind": "room_stub"
      },
      {
        "id": "road_western_trade.link1",
        "label": "east 出口",
        "cluster": "road_western_trade:junction",
        "kind": "world_link",
        "worldTarget": "city_changan",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "road_western_trade.link2",
        "label": "west 出口",
        "cluster": "road_western_trade:junction",
        "kind": "world_link",
        "worldTarget": "wild_salt_road",
        "direction": "west",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "road_western_trade.entry",
        "to": "road_western_trade.link1",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "road_western_trade.entry",
        "to": "road_western_trade.link2",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "road_western_trade.entry",
        "to": "road_western_trade.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "road_western_trade.core",
        "to": "road_western_trade.service",
        "direction": "branch",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "旅途中轉、消息流通",
    "signatureScenes": [
      "路亭",
      "驛站牌",
      "分岔口"
    ],
    "npcRoles": [
      "驛卒",
      "旅人",
      "押鏢人"
    ],
    "questHooks": [
      "問路",
      "護送",
      "攔查可疑過客"
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
