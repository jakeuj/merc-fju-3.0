# 河濱灘地

## Area Metadata

- AreaId: `wild_floodplain`
- Label: 河濱灘地
- Type: wild
- Region: 兗州河北 (`yanzhao`)
- Theme: 詭異民俗
- Subtheme: 濕地 / 夜霧
- LevelRange: 20-30
- Tags: haunted

## Prose Scaffold

Theme: 詭異民俗
Subtheme: 濕地 / 夜霧
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
- 有人提到 河濱灘地 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_puyang` (outgoing)
- down: `dng_river_cavern` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_floodplain",
  "label": "河濱灘地",
  "type": "wild",
  "region": {
    "id": "yanzhao",
    "label": "兗州河北"
  },
  "theme": {
    "primary": "詭異民俗",
    "secondary": "濕地 / 夜霧"
  },
  "levelRange": "20-30",
  "tags": [
    "haunted"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_puyang",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "dng_river_cavern",
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
        "id": "wild_floodplain:entry",
        "label": "入口區",
        "role": "entry"
      },
      {
        "id": "wild_floodplain:wild_core",
        "label": "主野外區",
        "role": "wild_core"
      },
      {
        "id": "wild_floodplain:landmark",
        "label": "地標區",
        "role": "landmark"
      },
      {
        "id": "wild_floodplain:secret_path",
        "label": "隱藏支線",
        "role": "secret_path"
      }
    ],
    "nodes": [
      {
        "id": "wild_floodplain.entry",
        "label": "入口節點",
        "cluster": "wild_floodplain:entry",
        "kind": "room_stub"
      },
      {
        "id": "wild_floodplain.core",
        "label": "核心節點",
        "cluster": "wild_floodplain:wild_core",
        "kind": "room_stub"
      },
      {
        "id": "wild_floodplain.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_floodplain:landmark",
        "kind": "room_stub"
      },
      {
        "id": "wild_floodplain.link1",
        "label": "west 出口",
        "cluster": "wild_floodplain:entry",
        "kind": "world_link",
        "worldTarget": "city_puyang",
        "direction": "west",
        "io": "out"
      },
      {
        "id": "wild_floodplain.link2",
        "label": "down 出口",
        "cluster": "wild_floodplain:entry",
        "kind": "world_link",
        "worldTarget": "dng_river_cavern",
        "direction": "down",
        "io": "out"
      },
      {
        "id": "wild_floodplain.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_floodplain:secret_path",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_floodplain.entry",
        "to": "wild_floodplain.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_floodplain.entry",
        "to": "wild_floodplain.link2",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_floodplain.entry",
        "to": "wild_floodplain.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_floodplain.core",
        "to": "wild_floodplain.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_floodplain.core",
        "to": "wild_floodplain.deep",
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
