# 帝王古墓

## Area Metadata

- AreaId: `dng_royal_tomb`
- Label: 帝王古墓
- Type: dungeon
- Region: 中原 (`zhongyuan`)
- Theme: 探險遺跡
- Subtheme: 古墓 / 機關
- LevelRange: 18-30
- Tags: dungeon

## Prose Scaffold

Theme: 探險遺跡
Subtheme: 古墓 / 機關
Mood: 幽深、危險、秘密感強
Signature scenes:
- 入口前廳
- 陰暗通道
- 封印或機關
NPC factions or roles:
- 守關怪物
- 殘魂
- 迷途者
Quest hooks:
- 深入調查
- 尋回遺物
- 破解封印
Interaction cues:
- #Enquire 入口
- #Enquire 深處
- #Enquire 退路
- #Keyword 石門
- #Keyword 符文
- #Keyword 水痕
- #Job 深入調查
- #Job 尋回遺物
- #Job 破解封印
Rumor seeds:
- 有人提到 帝王古墓 最近似乎出現不尋常的動靜。
- 深處可能藏有條件解鎖路線或事件房。

## World Links

- up: `dng_sewer_depths` (outgoing)
- down: `sec_catacomb_depths` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "dng_royal_tomb",
  "label": "帝王古墓",
  "type": "dungeon",
  "region": {
    "id": "zhongyuan",
    "label": "中原"
  },
  "theme": {
    "primary": "探險遺跡",
    "secondary": "古墓 / 機關"
  },
  "levelRange": "18-30",
  "tags": [
    "dungeon"
  ],
  "worldLinks": [
    {
      "direction": "up",
      "target": "dng_sewer_depths",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "sec_catacomb_depths",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "入口",
      "深處",
      "退路"
    ],
    "keyword": [
      "石門",
      "符文",
      "水痕"
    ],
    "job": [
      "深入調查",
      "尋回遺物",
      "破解封印"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "dng_royal_tomb:entry_hall",
        "label": "入口前廳",
        "role": "entry_hall"
      },
      {
        "id": "dng_royal_tomb:main_corridor",
        "label": "主通道",
        "role": "main_corridor"
      },
      {
        "id": "dng_royal_tomb:side_room",
        "label": "支路房",
        "role": "side_room"
      },
      {
        "id": "dng_royal_tomb:core",
        "label": "核心區",
        "role": "core"
      },
      {
        "id": "dng_royal_tomb:sealed_room",
        "label": "封印房",
        "role": "sealed_room"
      }
    ],
    "nodes": [
      {
        "id": "dng_royal_tomb.entry",
        "label": "入口節點",
        "cluster": "dng_royal_tomb:entry_hall",
        "kind": "room_stub"
      },
      {
        "id": "dng_royal_tomb.core",
        "label": "核心節點",
        "cluster": "dng_royal_tomb:main_corridor",
        "kind": "room_stub"
      },
      {
        "id": "dng_royal_tomb.service",
        "label": "服務 / 互動節點",
        "cluster": "dng_royal_tomb:side_room",
        "kind": "room_stub"
      },
      {
        "id": "dng_royal_tomb.link1",
        "label": "up 出口",
        "cluster": "dng_royal_tomb:entry_hall",
        "kind": "world_link",
        "worldTarget": "dng_sewer_depths",
        "direction": "up",
        "io": "out"
      },
      {
        "id": "dng_royal_tomb.link2",
        "label": "down 出口",
        "cluster": "dng_royal_tomb:entry_hall",
        "kind": "world_link",
        "worldTarget": "sec_catacomb_depths",
        "direction": "down",
        "io": "out"
      },
      {
        "id": "dng_royal_tomb.deep",
        "label": "深處 / 支線節點",
        "cluster": "dng_royal_tomb:sealed_room",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "dng_royal_tomb.entry",
        "to": "dng_royal_tomb.link1",
        "direction": "up",
        "type": "world_transition_stub"
      },
      {
        "from": "dng_royal_tomb.entry",
        "to": "dng_royal_tomb.link2",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "dng_royal_tomb.entry",
        "to": "dng_royal_tomb.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "dng_royal_tomb.core",
        "to": "dng_royal_tomb.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "dng_royal_tomb.core",
        "to": "dng_royal_tomb.deep",
        "direction": "deeper",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "幽深、危險、秘密感強",
    "signatureScenes": [
      "入口前廳",
      "陰暗通道",
      "封印或機關"
    ],
    "npcRoles": [
      "守關怪物",
      "殘魂",
      "迷途者"
    ],
    "questHooks": [
      "深入調查",
      "尋回遺物",
      "破解封印"
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
