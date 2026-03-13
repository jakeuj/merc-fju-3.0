# 古戰場

## Area Metadata

- AreaId: `wild_old_battlefield`
- Label: 古戰場
- Type: wild
- Region: 兗州河北 (`yanzhao`)
- Theme: 軍旅
- Subtheme: 古戰地 / 殘兵
- LevelRange: 22-34
- Tags: battle

## Prose Scaffold

Theme: 軍旅
Subtheme: 古戰地 / 殘兵
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
- 有人提到 古戰場 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- east: `city_puyang` (outgoing)
- down: `sec_yellow_turban_ruins` (outgoing)
- south: `sec_chibi_battlefield` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "wild_old_battlefield",
  "label": "古戰場",
  "type": "wild",
  "region": {
    "id": "yanzhao",
    "label": "兗州河北"
  },
  "theme": {
    "primary": "軍旅",
    "secondary": "古戰地 / 殘兵"
  },
  "levelRange": "22-34",
  "tags": [
    "battle"
  ],
  "worldLinks": [
    {
      "direction": "east",
      "target": "city_puyang",
      "kind": "outgoing"
    },
    {
      "direction": "down",
      "target": "sec_yellow_turban_ruins",
      "kind": "outgoing"
    },
    {
      "direction": "south",
      "target": "sec_chibi_battlefield",
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
        "id": "wild_old_battlefield:entry",
        "label": "入口區",
        "role": "entry"
      },
      {
        "id": "wild_old_battlefield:wild_core",
        "label": "主野外區",
        "role": "wild_core"
      },
      {
        "id": "wild_old_battlefield:landmark",
        "label": "地標區",
        "role": "landmark"
      },
      {
        "id": "wild_old_battlefield:secret_path",
        "label": "隱藏支線",
        "role": "secret_path"
      }
    ],
    "nodes": [
      {
        "id": "wild_old_battlefield.entry",
        "label": "入口節點",
        "cluster": "wild_old_battlefield:entry",
        "kind": "room_stub"
      },
      {
        "id": "wild_old_battlefield.core",
        "label": "核心節點",
        "cluster": "wild_old_battlefield:wild_core",
        "kind": "room_stub"
      },
      {
        "id": "wild_old_battlefield.service",
        "label": "服務 / 互動節點",
        "cluster": "wild_old_battlefield:landmark",
        "kind": "room_stub"
      },
      {
        "id": "wild_old_battlefield.link1",
        "label": "east 出口",
        "cluster": "wild_old_battlefield:entry",
        "kind": "world_link",
        "worldTarget": "city_puyang",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "wild_old_battlefield.link2",
        "label": "down 出口",
        "cluster": "wild_old_battlefield:entry",
        "kind": "world_link",
        "worldTarget": "sec_yellow_turban_ruins",
        "direction": "down",
        "io": "out"
      },
      {
        "id": "wild_old_battlefield.link3",
        "label": "south 出口",
        "cluster": "wild_old_battlefield:entry",
        "kind": "world_link",
        "worldTarget": "sec_chibi_battlefield",
        "direction": "south",
        "io": "out"
      },
      {
        "id": "wild_old_battlefield.deep",
        "label": "深處 / 支線節點",
        "cluster": "wild_old_battlefield:secret_path",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "wild_old_battlefield.entry",
        "to": "wild_old_battlefield.link1",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_old_battlefield.entry",
        "to": "wild_old_battlefield.link2",
        "direction": "down",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_old_battlefield.entry",
        "to": "wild_old_battlefield.link3",
        "direction": "south",
        "type": "world_transition_stub"
      },
      {
        "from": "wild_old_battlefield.entry",
        "to": "wild_old_battlefield.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "wild_old_battlefield.core",
        "to": "wild_old_battlefield.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "wild_old_battlefield.core",
        "to": "wild_old_battlefield.deep",
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
