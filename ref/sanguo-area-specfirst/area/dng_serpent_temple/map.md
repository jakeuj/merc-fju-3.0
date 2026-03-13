# 蛇神殿

## Area Metadata

- AreaId: `dng_serpent_temple`
- Label: 蛇神殿
- Type: dungeon
- Region: 荊南南蠻 (`south`)
- Theme: 詭異民俗
- Subtheme: 蛇殿 / 血祭
- LevelRange: 48-62
- Tags: dungeon

## Prose Scaffold

Theme: 詭異民俗
Subtheme: 蛇殿 / 血祭
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
- 有人提到 蛇神殿 最近似乎出現不尋常的動靜。
- 深處可能藏有條件解鎖路線或事件房。

## World Links

- up: `wild_nanman_jungle` (outgoing)
- down: `sec_jungle_ruins` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "dng_serpent_temple",
  "label": "蛇神殿",
  "type": "dungeon",
  "region": {
    "id": "south",
    "label": "荊南南蠻"
  },
  "theme": {
    "primary": "詭異民俗",
    "secondary": "蛇殿 / 血祭"
  },
  "levelRange": "48-62",
  "tags": [
    "dungeon"
  ],
  "worldLinks": [
    {
      "direction": "up",
      "target": "wild_nanman_jungle",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "sec_jungle_ruins",
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
        "id": "dng_serpent_temple:entry_hall",
        "label": "入口前廳",
        "role": "entry_hall"
      },
      {
        "id": "dng_serpent_temple:main_corridor",
        "label": "主通道",
        "role": "main_corridor"
      },
      {
        "id": "dng_serpent_temple:side_room",
        "label": "支路房",
        "role": "side_room"
      },
      {
        "id": "dng_serpent_temple:core",
        "label": "核心區",
        "role": "core"
      },
      {
        "id": "dng_serpent_temple:sealed_room",
        "label": "封印房",
        "role": "sealed_room"
      }
    ],
    "nodes": [
      {
        "id": "dng_serpent_temple.entry",
        "label": "入口節點",
        "cluster": "dng_serpent_temple:entry_hall",
        "kind": "room_stub"
      },
      {
        "id": "dng_serpent_temple.core",
        "label": "核心節點",
        "cluster": "dng_serpent_temple:main_corridor",
        "kind": "room_stub"
      },
      {
        "id": "dng_serpent_temple.service",
        "label": "服務 / 互動節點",
        "cluster": "dng_serpent_temple:side_room",
        "kind": "room_stub"
      },
      {
        "id": "dng_serpent_temple.link1",
        "label": "up 出口",
        "cluster": "dng_serpent_temple:entry_hall",
        "kind": "world_link",
        "worldTarget": "wild_nanman_jungle",
        "direction": "up",
        "io": "out"
      },
      {
        "id": "dng_serpent_temple.link2",
        "label": "down 出口",
        "cluster": "dng_serpent_temple:entry_hall",
        "kind": "world_link",
        "worldTarget": "sec_jungle_ruins",
        "direction": "down",
        "io": "out"
      },
      {
        "id": "dng_serpent_temple.deep",
        "label": "深處 / 支線節點",
        "cluster": "dng_serpent_temple:sealed_room",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "dng_serpent_temple.entry",
        "to": "dng_serpent_temple.link1",
        "direction": "up",
        "type": "world_transition_stub"
      },
      {
        "from": "dng_serpent_temple.entry",
        "to": "dng_serpent_temple.link2",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "dng_serpent_temple.entry",
        "to": "dng_serpent_temple.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "dng_serpent_temple.core",
        "to": "dng_serpent_temple.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "dng_serpent_temple.core",
        "to": "dng_serpent_temple.deep",
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
