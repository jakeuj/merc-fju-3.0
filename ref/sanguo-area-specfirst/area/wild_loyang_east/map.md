# 洛陽東郊

## Area Metadata

- AreaId: `wild_loyang_east`
- Label: 洛陽東郊
- Type: outskirts
- Region: 中原 (`zhongyuan`)
- Theme: 江湖
- Subtheme: 城郊 / 官道
- LevelRange: 1-12
- Tags: starter

## Prose Scaffold

Theme: 江湖
Subtheme: 城郊 / 官道
Mood: 城郊過渡、試探與探索並存
Signature scenes:
- 官道
- 路旁林地
- 破舊亭子
NPC factions or roles:
- 巡邏兵
- 路過商旅
- 可疑流民
Quest hooks:
- 清理小股盜匪
- 護送旅人
- 調查郊外異常
Interaction cues:
- #Enquire 回城
- #Enquire 官道
- #Enquire 茶亭
- #Keyword 路碑
- #Keyword 茶亭
- #Keyword 樹叢
- #Job 巡查
- #Job 護送
- #Job 清理流寇
Rumor seeds:
- 有人提到 洛陽東郊 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_loyang` (outgoing)
- east: `wild_longqu_hills` (outgoing)
- north: `wild_fengqiu_forest` (outgoing)
- south: `wild_farming_village` (outgoing)
- south: `wild_old_bridge` (outgoing)

## mapmd-json

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
    "secondary": "城郊 / 官道"
  },
  "levelRange": "1-12",
  "tags": [
    "starter"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_loyang",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "wild_longqu_hills",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "wild_fengqiu_forest",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "wild_farming_village",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "wild_old_bridge",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "回城",
      "官道",
      "茶亭"
    ],
    "keyword": [
      "路碑",
      "茶亭",
      "樹叢"
    ],
    "job": [
      "巡查",
      "護送",
      "清理流寇"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "wild_loyang_east:return_gate",
        "label": "回城點",
        "role": "return_gate"
      },
      {
        "id": "wild_loyang_east:road",
        "label": "主官道",
        "role": "road"
      },
      {
        "id": "wild_loyang_east:wildside",
        "label": "側路野區",
        "role": "wildside"
      },
      {
        "id": "wild_loyang_east:special_entry",
        "label": "特殊入口",
        "role": "special_entry"
      }
    ],
    "nodes": [
      {
        "id": "wild_loyang_east.entry",
        "label": "入口節點",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "room_stub"
      },
      {
        "id": "wild_loyang_east.core",
        "label": "核心節點",
        "cluster": "wild_loyang_east:road",
        "kind": "room_stub"
      },
      {
        "id": "wild_loyang_east.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_loyang_east:wildside",
        "kind": "room_stub"
      },
      {
        "id": "wild_loyang_east.link1",
        "label": "west 出口",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "world_link",
        "worldTarget": "city_loyang",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "wild_loyang_east.link2",
        "label": "east 出口",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "world_link",
        "worldTarget": "wild_longqu_hills",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "wild_loyang_east.link3",
        "label": "north 出口",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "world_link",
        "worldTarget": "wild_fengqiu_forest",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "wild_loyang_east.link4",
        "label": "south 出口",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "world_link",
        "worldTarget": "wild_farming_village",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "wild_loyang_east.link5",
        "label": "south 出口",
        "cluster": "wild_loyang_east:return_gate",
        "kind": "world_link",
        "worldTarget": "wild_old_bridge",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "wild_loyang_east.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_loyang_east:special_entry",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.link3",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.link4",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.link5",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_loyang_east.entry",
        "to": "wild_loyang_east.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_loyang_east.core",
        "to": "wild_loyang_east.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_loyang_east.core",
        "to": "wild_loyang_east.deep",
        "direction": "deeper",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "城郊過渡、試探與探索並存",
    "signatureScenes": [
      "官道",
      "路旁林地",
      "破舊亭子"
    ],
    "npcRoles": [
      "巡邏兵",
      "路過商旅",
      "可疑流民"
    ],
    "questHooks": [
      "清理小股盜匪",
      "護送旅人",
      "調查郊外異常"
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
