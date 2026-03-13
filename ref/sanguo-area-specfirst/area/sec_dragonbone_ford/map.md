# 龍骨淺灘

## Area Metadata

- AreaId: `sec_dragonbone_ford`
- Label: 龍骨淺灘
- Type: secret
- Region: 兗州河北 (`yanzhao`)
- Theme: 探險遺跡
- Subtheme: 古獸遺骸
- LevelRange: 35-48
- Tags: secret

## Prose Scaffold

Theme: 探險遺跡
Subtheme: 古獸遺骸
Mood: 稀有、神祕、偏高風險高回報
Signature scenes:
- 異象核心
- 特殊祭壇
- 隱藏路徑
NPC factions or roles:
- 守護者
- 秘境居民
- 特殊事件角色
Quest hooks:
- 解鎖條件進入
- 完成祕境試煉
- 取得關鍵線索
Interaction cues:
- #Enquire 異象
- #Enquire 入口條件
- #Enquire 出口
- #Keyword 祭壇
- #Keyword 裂隙
- #Keyword 光紋
- #Job 解鎖條件進入
- #Job 完成祕境試煉
- #Job 取得關鍵線索
Rumor seeds:
- 有人提到 龍骨淺灘 最近似乎出現不尋常的動靜。
- 深處可能藏有條件解鎖路線或事件房。

## World Links

- up: `dng_river_cavern` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "sec_dragonbone_ford",
  "label": "龍骨淺灘",
  "type": "secret",
  "region": {
    "id": "yanzhao",
    "label": "兗州河北"
  },
  "theme": {
    "primary": "探險遺跡",
    "secondary": "古獸遺骸"
  },
  "levelRange": "35-48",
  "tags": [
    "secret"
  ],
  "worldLinks": [
    {
      "direction": "up",
      "target": "dng_river_cavern",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "異象",
      "入口條件",
      "出口"
    ],
    "keyword": [
      "祭壇",
      "裂隙",
      "光紋"
    ],
    "job": [
      "解鎖條件進入",
      "完成祕境試煉",
      "取得關鍵線索"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "sec_dragonbone_ford:condition_gate",
        "label": "條件入口",
        "role": "condition_gate"
      },
      {
        "id": "sec_dragonbone_ford:anomaly_core",
        "label": "異象核心",
        "role": "anomaly_core"
      },
      {
        "id": "sec_dragonbone_ford:reward_room",
        "label": "獎勵區",
        "role": "reward_room"
      }
    ],
    "nodes": [
      {
        "id": "sec_dragonbone_ford.entry",
        "label": "入口節點",
        "cluster": "sec_dragonbone_ford:condition_gate",
        "kind": "room_stub"
      },
      {
        "id": "sec_dragonbone_ford.core",
        "label": "核心節點",
        "cluster": "sec_dragonbone_ford:anomaly_core",
        "kind": "room_stub"
      },
      {
        "id": "sec_dragonbone_ford.service",
        "label": "服務 / 互動節點",
        "cluster": "sec_dragonbone_ford:reward_room",
        "kind": "room_stub"
      },
      {
        "id": "sec_dragonbone_ford.link1",
        "label": "up 出口",
        "cluster": "sec_dragonbone_ford:condition_gate",
        "kind": "world_link",
        "worldTarget": "dng_river_cavern",
        "direction": "up",
        "io": "out"
      },
      {
        "id": "sec_dragonbone_ford.deep",
        "label": "深處 / 支線節點",
        "cluster": "sec_dragonbone_ford:reward_room",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "sec_dragonbone_ford.entry",
        "to": "sec_dragonbone_ford.link1",
        "direction": "up",
        "type": "world_transition_stub"
      },
      {
        "from": "sec_dragonbone_ford.entry",
        "to": "sec_dragonbone_ford.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "sec_dragonbone_ford.core",
        "to": "sec_dragonbone_ford.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "sec_dragonbone_ford.core",
        "to": "sec_dragonbone_ford.deep",
        "direction": "deeper",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "稀有、神祕、偏高風險高回報",
    "signatureScenes": [
      "異象核心",
      "特殊祭壇",
      "隱藏路徑"
    ],
    "npcRoles": [
      "守護者",
      "秘境居民",
      "特殊事件角色"
    ],
    "questHooks": [
      "解鎖條件進入",
      "完成祕境試煉",
      "取得關鍵線索"
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
