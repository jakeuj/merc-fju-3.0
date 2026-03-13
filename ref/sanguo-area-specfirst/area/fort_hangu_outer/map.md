# 函谷關前道

## Area Metadata

- AreaId: `fort_hangu_outer`
- Label: 函谷關前道
- Type: fort
- Region: 關中西域 (`guanzhong`)
- Theme: 軍旅
- Subtheme: 關前營寨
- LevelRange: 20-32
- Tags: fort

## Prose Scaffold

Theme: 軍旅
Subtheme: 關前營寨
Mood: 戒備、軍令、壓迫
Signature scenes:
- 關門
- 望樓
- 營寨
NPC factions or roles:
- 校尉
- 斥候
- 守兵
Quest hooks:
- 傳遞軍令
- 偵查敵情
- 修補防線
Interaction cues:
- #Enquire 關門
- #Enquire 軍營
- #Enquire 將令
- #Keyword 軍旗
- #Keyword 柵門
- #Keyword 望樓
- #Job 傳遞軍令
- #Job 偵查敵情
- #Job 修補防線
Rumor seeds:
- 有人提到 函谷關前道 最近似乎出現不尋常的動靜。
- 深處可能藏有條件解鎖路線或事件房。

## World Links

- east: `fort_hangu` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "fort_hangu_outer",
  "label": "函谷關前道",
  "type": "fort",
  "region": {
    "id": "guanzhong",
    "label": "關中西域"
  },
  "theme": {
    "primary": "軍旅",
    "secondary": "關前營寨"
  },
  "levelRange": "20-32",
  "tags": [
    "fort"
  ],
  "worldLinks": [
    {
      "direction": "east",
      "target": "fort_hangu",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "關門",
      "軍營",
      "將令"
    ],
    "keyword": [
      "軍旗",
      "柵門",
      "望樓"
    ],
    "job": [
      "傳遞軍令",
      "偵查敵情",
      "修補防線"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "fort_hangu_outer:approach",
        "label": "關前道",
        "role": "approach"
      },
      {
        "id": "fort_hangu_outer:gate",
        "label": "關門",
        "role": "gate"
      },
      {
        "id": "fort_hangu_outer:camp",
        "label": "內營",
        "role": "camp"
      },
      {
        "id": "fort_hangu_outer:watch",
        "label": "望樓",
        "role": "watch"
      },
      {
        "id": "fort_hangu_outer:secret_tunnel",
        "label": "密道",
        "role": "secret_tunnel"
      }
    ],
    "nodes": [
      {
        "id": "fort_hangu_outer.entry",
        "label": "入口節點",
        "cluster": "fort_hangu_outer:approach",
        "kind": "room_stub"
      },
      {
        "id": "fort_hangu_outer.core",
        "label": "核心節點",
        "cluster": "fort_hangu_outer:gate",
        "kind": "room_stub"
      },
      {
        "id": "fort_hangu_outer.service",
        "label": "服務 / 互動節點",
        "cluster": "fort_hangu_outer:camp",
        "kind": "room_stub"
      },
      {
        "id": "fort_hangu_outer.link1",
        "label": "east 出口",
        "cluster": "fort_hangu_outer:approach",
        "kind": "world_link",
        "worldTarget": "fort_hangu",
        "direction": "east",
        "io": "out"
      },
      {
        "id": "fort_hangu_outer.deep",
        "label": "深處 / 支線節點",
        "cluster": "fort_hangu_outer:secret_tunnel",
        "kind": "room_stub"
      }
    ],
    "edges": [
      {
        "from": "fort_hangu_outer.entry",
        "to": "fort_hangu_outer.link1",
        "direction": "east",
        "type": "world_transition_stub"
      },
      {
        "from": "fort_hangu_outer.entry",
        "to": "fort_hangu_outer.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "fort_hangu_outer.core",
        "to": "fort_hangu_outer.service",
        "direction": "branch",
        "type": "internal"
      },
      {
        "from": "fort_hangu_outer.core",
        "to": "fort_hangu_outer.deep",
        "direction": "deeper",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "戒備、軍令、壓迫",
    "signatureScenes": [
      "關門",
      "望樓",
      "營寨"
    ],
    "npcRoles": [
      "校尉",
      "斥候",
      "守兵"
    ],
    "questHooks": [
      "傳遞軍令",
      "偵查敵情",
      "修補防線"
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
