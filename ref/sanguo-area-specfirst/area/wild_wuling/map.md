# 武陵山

## Area Metadata

- AreaId: `wild_wuling`
- Label: 武陵山
- Type: wild
- Region: 蜀漢 (`shu`)
- Theme: 仙俠
- Subtheme: 深山 / 靈木
- LevelRange: 40-54
- Tags: explore

## Prose Scaffold

Theme: 仙俠
Subtheme: 深山 / 靈木
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
- 有人提到 武陵山 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- north: `city_jiangling` (outgoing)
- east: `wild_spirit_forest` (outgoing)
- west: `wild_hidden_valley` (outgoing)
- east: `city_changsha` (incoming)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_wuling",
  "label": "武陵山",
  "type": "wild",
  "region": {
    "id": "shu",
    "label": "蜀漢"
  },
  "theme": {
    "primary": "仙俠",
    "secondary": "深山 / 靈木"
  },
  "levelRange": "40-54",
  "tags": [
    "explore"
  ],
  "worldLinks": [
    {
      "direction": "north",
      "target": "city_jiangling",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "wild_spirit_forest",
      "kind": "outgoing"
    },
    {
      "direction": "west",
      "target": "wild_hidden_valley",
      "kind": "outgoing"
    },
    {
      "direction": "east",
      "target": "city_changsha",
      "kind": "incoming"
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
        "id": "wild_wuling:entry",
        "label": "入口區",
        "role": "entry"
      },
      {
        "id": "wild_wuling:wild_core",
        "label": "主野外區",
        "role": "wild_core"
      },
      {
        "id": "wild_wuling:landmark",
        "label": "地標區",
        "role": "landmark"
      },
      {
        "id": "wild_wuling:secret_path",
        "label": "隱藏支線",
        "role": "secret_path"
      }
    ],
    "nodes": [
      {
        "id": "wild_wuling.entry",
        "label": "入口節點",
        "cluster": "wild_wuling:entry",
        "kind": "room_stub"
      },
      {
        "id": "wild_wuling.core",
        "label": "核心節點",
        "cluster": "wild_wuling:wild_core",
        "kind": "room_stub"
      },
      {
        "id": "wild_wuling.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_wuling:landmark",
        "kind": "room_stub"
      },
      {
        "id": "wild_wuling.link1",
        "label": "north 出口",
        "cluster": "wild_wuling:entry",
        "kind": "world_link",
        "worldTarget": "city_jiangling",
        "direction": "north",
        "io": "out"
      },
      {
        "id": "wild_wuling.link2",
        "label": "east 出口",
        "cluster": "wild_wuling:entry",
        "kind": "world_link",
        "worldTarget": "wild_spirit_forest",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "wild_wuling.link3",
        "label": "west 出口",
        "cluster": "wild_wuling:entry",
        "kind": "world_link",
        "worldTarget": "wild_hidden_valley",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "wild_wuling.link4",
        "label": "east 出口",
        "cluster": "wild_wuling:entry",
        "kind": "world_link",
        "worldTarget": "city_changsha",
        "direction": "east",
        "io": "in"
      },
      {
        "id": "wild_wuling.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_wuling:secret_path",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_wuling.entry",
        "to": "wild_wuling.link1",
        "direction": "north",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_wuling.entry",
        "to": "wild_wuling.link2",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_wuling.entry",
        "to": "wild_wuling.link3",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_wuling.entry",
        "to": "wild_wuling.link4",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_wuling.entry",
        "to": "wild_wuling.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_wuling.core",
        "to": "wild_wuling.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_wuling.core",
        "to": "wild_wuling.deep",
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
