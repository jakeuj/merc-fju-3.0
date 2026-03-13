# 北平市集

## Area Metadata

- AreaId: `district_beiping_market`
- Label: 北平市集
- Type: district
- Region: 幽州遼東 (`youzhou`)
- Theme: 歷史城市
- Subtheme: 市集 / 商行
- LevelRange: 20-30
- Tags: trade

## Prose Scaffold

Theme: 歷史城市
Subtheme: 市集 / 商行
Mood: 區域功能明確、人流集中
Signature scenes:
- 街口
- 招牌
- 來往人群
NPC factions or roles:
- 店家
- 學子
- 差役
Quest hooks:
- 尋找指定店鋪
- 打聽傳聞
- 完成地方委託
Interaction cues:
- #Enquire 店家
- #Enquire 去路
- #Enquire 街口
- #Keyword 招牌
- #Keyword 告示
- #Keyword 門牌
- #Job 採買
- #Job 問路
Rumor seeds:
- 有人提到 北平市集 最近似乎出現不尋常的動靜。
- 可預留一條支線通往地下、秘境或特殊遭遇區。

## World Links

- west: `city_beiping` (outgoing)

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "district_beiping_market",
  "label": "北平市集",
  "type": "district",
  "region": {
    "id": "youzhou",
    "label": "幽州遼東"
  },
  "theme": {
    "primary": "歷史城市",
    "secondary": "市集 / 商行"
  },
  "levelRange": "20-30",
  "tags": [
    "trade"
  ],
  "worldLinks": [
    {
      "direction": "west",
      "target": "city_beiping",
      "kind": "outgoing"
    }
  ],
  "interactionHints": {
    "enquire": [
      "店家",
      "去路",
      "街口"
    ],
    "keyword": [
      "招牌",
      "告示",
      "門牌"
    ],
    "job": [
      "採買",
      "問路"
    ]
  },
  "topology": {
    "clusters": [
      {
        "id": "district_beiping_market:entry",
        "label": "入口街口",
        "role": "entry"
      },
      {
        "id": "district_beiping_market:core",
        "label": "核心區",
        "role": "core"
      },
      {
        "id": "district_beiping_market:side_lane",
        "label": "支巷區",
        "role": "side_lane"
      }
    ],
    "nodes": [
      {
        "id": "district_beiping_market.entry",
        "label": "入口節點",
        "cluster": "district_beiping_market:entry",
        "kind": "room_stub"
      },
      {
        "id": "district_beiping_market.core",
        "label": "核心節點",
        "cluster": "district_beiping_market:core",
        "kind": "room_stub"
      },
      {
        "id": "district_beiping_market.service",
        "label": "服務 / 互動節點",
        "cluster": "district_beiping_market:side_lane",
        "kind": "room_stub"
      },
      {
        "id": "district_beiping_market.link1",
        "label": "west 出口",
        "cluster": "district_beiping_market:entry",
        "kind": "world_link",
        "worldTarget": "city_beiping",
        "direction": "west",
        "io": "out"
      }
    ],
    "edges": [
      {
        "from": "district_beiping_market.entry",
        "to": "district_beiping_market.link1",
        "direction": "west",
        "type": "world_transition_stub"
      },
      {
        "from": "district_beiping_market.entry",
        "to": "district_beiping_market.core",
        "direction": "forward",
        "type": "internal"
      },
      {
        "from": "district_beiping_market.core",
        "to": "district_beiping_market.service",
        "direction": "branch",
        "type": "internal"
      }
    ]
  },
  "generationHints": {
    "mood": "區域功能明確、人流集中",
    "signatureScenes": [
      "街口",
      "招牌",
      "來往人群"
    ],
    "npcRoles": [
      "店家",
      "學子",
      "差役"
    ],
    "questHooks": [
      "尋找指定店鋪",
      "打聽傳聞",
      "完成地方委託"
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
