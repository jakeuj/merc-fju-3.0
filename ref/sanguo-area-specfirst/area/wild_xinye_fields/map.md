# 新野郊野

## Area Metadata

- AreaId: `wild_xinye_fields`
- Label: 新野郊野
- Type: wild
- Region: 荊州 (`jingzhou`)
- Theme: 江湖
- Subtheme: 田野 / 村落
- LevelRange: 18-28
- Tags: wild

## Prose Scaffold

Theme: 江湖
Subtheme: 田野 / 村落
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
- 有人提到 新野郊野 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_xinye` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_xinye_fields",
  "label": "新野郊野",
  "type": "wild",
  "region": {
    "id": "jingzhou",
    "label": "荊州"
  },
  "theme": {
    "primary": "江湖",
    "secondary": "田野 / 村落"
  },
  "levelRange": "18-28",
  "tags": [
    "wild"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_xinye",
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
        "id": "wild_xinye_fields:entry",
        "label": "入口區",
        "role": "entry"
      },
      {
        "id": "wild_xinye_fields:wild_core",
        "label": "主野外區",
        "role": "wild_core"
      },
      {
        "id": "wild_xinye_fields:landmark",
        "label": "地標區",
        "role": "landmark"
      },
      {
        "id": "wild_xinye_fields:secret_path",
        "label": "隱藏支線",
        "role": "secret_path"
      }
    ],
    "nodes": [
      {
        "id": "wild_xinye_fields.entry",
        "label": "入口節點",
        "cluster": "wild_xinye_fields:entry",
        "kind": "room_stub"
      },
      {
        "id": "wild_xinye_fields.core",
        "label": "核心節點",
        "cluster": "wild_xinye_fields:wild_core",
        "kind": "room_stub"
      },
      {
        "id": "wild_xinye_fields.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_xinye_fields:landmark",
        "kind": "room_stub"
      },
      {
        "id": "wild_xinye_fields.link1",
        "label": "west 出口",
        "cluster": "wild_xinye_fields:entry",
        "kind": "world_link",
        "worldTarget": "city_xinye",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "wild_xinye_fields.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_xinye_fields:secret_path",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_xinye_fields.entry",
        "to": "wild_xinye_fields.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_xinye_fields.entry",
        "to": "wild_xinye_fields.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_xinye_fields.core",
        "to": "wild_xinye_fields.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_xinye_fields.core",
        "to": "wild_xinye_fields.deep",
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
