# 白狼山

## Area Metadata

- AreaId: `wild_bailang`
- Label: 白狼山
- Type: wild
- Region: 幽州遼東 (`youzhou`)
- Theme: 探險遺跡
- Subtheme: 山區 / 異族
- LevelRange: 30-42
- Tags: explore

## Prose Scaffold

Theme: 探險遺跡
Subtheme: 山區 / 異族
Mood: 未知、風險、可能藏著支線
Signature scenes:
- 岔路
- 自然地標
- 可疑痕跡
NPC factions or roles:
- 行腳客
- 獵戶
- 地方怪物
Quest hooks:
- 探索支線路徑
- 尋找稀有材料
- 追查失蹤者
Interaction cues:
- #Enquire 山路
- #Enquire 出口
- #Enquire 地標
- #Keyword 足跡
- #Keyword 石碑
- #Keyword 裂縫
- #Job 探索
- #Job 採集
- #Job 追查失蹤者
Rumor seeds:
- 有人提到 白狼山 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `fort_yijing` (outgoing)
- north: `wild_wolf_forest` (outgoing)
- down: `dng_ancient_cave` (outgoing)
- east: `wild_barbarian_camp` (outgoing)
- up: `sec_starfall_crater` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_bailang",
  "label": "白狼山",
  "type": "wild",
  "region": {
    "id": "youzhou",
    "label": "幽州遼東"
  },
  "theme": {
    "primary": "探險遺跡",
    "secondary": "山區 / 異族"
  },
  "levelRange": "30-42",
  "tags": [
    "explore"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "fort_yijing",
      "kind": "outgoing"
    },
    {
      "direction": "north",
      "target": "wild_wolf_forest",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "dng_ancient_cave",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "wild_barbarian_camp",
      "kind": "outgoing"
    },
    {
      "direction": "up",
      "target": "sec_starfall_crater",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "山路",
      "出口",
      "地標"
    ],
    "keyword": [
      "足跡",
      "石碑",
      "裂縫"
    ],
    "job": [
      "探索",
      "採集",
      "追查失蹤者"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "wild_bailang:entry",
        "label": "入口區",
        "role": "entry"
      },
      {
        "id": "wild_bailang:wild_core",
        "label": "主野外區",
        "role": "wild_core"
      },
      {
        "id": "wild_bailang:landmark",
        "label": "地標區",
        "role": "landmark"
      },
      {
        "id": "wild_bailang:secret_path",
        "label": "隱藏支線",
        "role": "secret_path"
      }
    ],
    "nodes": [
      {
        "id": "wild_bailang.entry",
        "label": "入口節點",
        "cluster": "wild_bailang:entry",
        "kind": "room_stub"
      },
      {
        "id": "wild_bailang.core",
        "label": "核心節點",
        "cluster": "wild_bailang:wild_core",
        "kind": "room_stub"
      },
      {
        "id": "wild_bailang.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_bailang:landmark",
        "kind": "room_stub"
      },
      {
        "id": "wild_bailang.link1",
        "label": "west 出口",
        "cluster": "wild_bailang:entry",
        "kind": "world_link",
        "worldTarget": "fort_yijing",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "wild_bailang.link2",
        "label": "north 出口",
        "cluster": "wild_bailang:entry",
        "kind": "world_link",
        "worldTarget": "wild_wolf_forest",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "wild_bailang.link3",
        "label": "down 出口",
        "cluster": "wild_bailang:entry",
        "kind": "world_link",
        "worldTarget": "dng_ancient_cave",
        "direction": "down",
        "io": "out"
      },
      {
        "id": "wild_bailang.link4",
        "label": "east 出口",
        "cluster": "wild_bailang:entry",
        "kind": "world_link",
        "worldTarget": "wild_barbarian_camp",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "wild_bailang.link5",
        "label": "up 出口",
        "cluster": "wild_bailang:entry",
        "kind": "world_link",
        "worldTarget": "sec_starfall_crater",
        "direction": "up",
        "io": "out"
      },
      {
        "id": "wild_bailang.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_bailang:secret_path",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.link2",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.link3",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.link4",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.link5",
        "direction": "up",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_bailang.entry",
        "to": "wild_bailang.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_bailang.core",
        "to": "wild_bailang.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_bailang.core",
        "to": "wild_bailang.deep",
        "direction": "deeper",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "未知、風險、可能藏著支線",
    "signatureScenes": [
      "岔路",
      "自然地標",
      "可疑痕跡"
    ],
    "npcRoles": [
      "行腳客",
      "獵戶",
      "地方怪物"
    ],
    "questHooks": [
      "探索支線路徑",
      "尋找稀有材料",
      "追查失蹤者"
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
