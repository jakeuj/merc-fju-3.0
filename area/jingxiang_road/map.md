# 荊襄大道 (`jingxiang_road`)

## Area Intent

`jingxiang_road` 是荊州走廊的交通樞紐帶，承接商旅、押鏢與軍報路線，讓玩家在「城市與城市之間」也能感受到明確玩法節奏，而非純粹趕路。

第一版目標先固定：

- 主幹道南北縱向骨架（襄陽 <-> 江夏）
- 一條西向支線（新野方向）
- 一條 `enter/down` 的可疑驛站地窖連線（非平面）
- 問路與盤查導向的互動節點（`#Enquire` / `#Keyword` / `#Job`）

## Theme Positioning

- Theme: `江湖風`
- Subtheme: `軍旅風`
- LevelRange: `18-30`
- Parent region: `jingzhou corridor`
- World gap filled: 把 `襄陽`、`新野`、`江夏` 之間的過路段補成可探索區，不再只有抽象連線

## Cluster Notes

### `north-south-trunk`
- 主幹道、驛牌與盤查點
- 玩家感受：消息流通快，但風險也高

### `west-fork-field`
- 新野支線、田埂與押運旁道
- 玩家感受：路線選擇與遭遇差異

### `posthouse-cellar`
- 驛館後院與地窖
- 玩家感受：可疑、潮濕、可能藏支線

## Planned World Links

- `north` from `9301`: planned link to `襄陽`
- `south` from `9308`: planned link to `江夏`
- `west` from `9305`: planned link to `新野`
- `down` beyond `9310`: planned continuation to `荊襄暗道 / 事件區`

## Suggested Layout

```text
襄陽方向
   |
[9301] 北向路碑 -- [9302] 官道巡檢亭 -- [9303] 荊襄主道中段 -- [9304] 分岔馬樁 -- [9308] 南向長坡
                                                           |
                                                        [9305] 西岔田道 -- [9306] 押運土道 -- [9307] 蘆棚歇腳點
                                                           |
                                                        [9309] 驛館後院
                                                           |
                                                         enter
                                                           |
                                                        [9310] 石階地窖
                                                           |
                                                         down (future)

江夏方向
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "jingxiang_road",
    "title": "荊襄大道",
    "design_notes": "先落地主幹道、支線與驛站地窖非平面入口，作為未來荊州系城市鏈整合的第一版 spec。",
    "level_range": "18-30",
    "theme": {
      "primary": "江湖風",
      "secondary": "軍旅風"
    },
    "planned_vnum_range": "9301-9310",
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 9301,
        "target_area": "city_xiangyang",
        "label": "襄陽"
      },
      {
        "direction": "south",
        "source_vnum": 9308,
        "target_area": "city_jiangxia",
        "label": "江夏"
      },
      {
        "direction": "west",
        "source_vnum": 9305,
        "target_area": "city_xinye",
        "label": "新野"
      }
    ],
    "clusters": [
      { "id": "north-south-trunk", "label": "荊襄主幹道" },
      { "id": "west-fork-field", "label": "新野西向支線" },
      { "id": "posthouse-cellar", "label": "驛站後院與地窖" }
    ]
  },
  "rooms": [
    {
      "vnum": 9301,
      "name": "北向路碑",
      "description": "一面刻著荊襄里程的石碑立在道旁，碑角還貼著剛換上的巡檢告示。北面道路筆直，馬蹄印密得幾乎重疊。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-south-trunk",
      "coord": [0, 0, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 9302 }
      ],
      "enquires": ["襄陽", "北路"]
    },
    {
      "vnum": 9302,
      "name": "官道巡檢亭",
      "description": "木亭內掛著點名牌與輪值簿冊，幾名巡檢兵正在核對來往旅人的行牒。氣氛不算緊張，卻讓人不敢多停。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-south-trunk",
      "coord": [0, 1, 0],
      "labels": ["checkpoint", "service"],
      "exits": [
        { "direction": "north", "to": 9301 },
        { "direction": "south", "to": 9303 }
      ],
      "keywords": [
        {
          "keyword": "行牒",
          "description": "巡檢兵要求旅人先出示行牒，再詢問來路與去向。"
        }
      ],
      "enquires": ["巡檢", "官道"]
    },
    {
      "vnum": 9303,
      "name": "荊襄主道中段",
      "description": "寬闊官道在此略微下沉，兩側是半乾的車轍與被踏平的草埂。南北往來的商隊在這段最常交錯，消息也傳得最快。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-south-trunk",
      "coord": [0, 2, 0],
      "labels": ["trunk", "traffic"],
      "exits": [
        { "direction": "north", "to": 9302 },
        { "direction": "south", "to": 9304 }
      ]
    },
    {
      "vnum": 9304,
      "name": "分岔馬樁",
      "description": "路心插著多根舊馬樁，旁邊懸著簡易木牌，標記南往江夏、西折新野。押鏢人常在此分隊，避免整支隊伍走同一路線。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-south-trunk",
      "coord": [0, 3, 0],
      "labels": ["junction", "enquire"],
      "exits": [
        { "direction": "north", "to": 9303 },
        { "direction": "south", "to": 9308 },
        { "direction": "west", "to": 9305 },
        { "direction": "east", "to": 9309 }
      ],
      "keywords": [
        {
          "keyword": "木牌",
          "description": "木牌上粗筆寫著「南江夏、西新野」，還有人另外刻了避盜小徑的暗記。"
        }
      ],
      "enquires": ["江夏", "新野", "去路"]
    },
    {
      "vnum": 9305,
      "name": "西岔田道",
      "description": "官道往西收窄成田道，路邊可見臨時埋鍋與熄滅炭灰，像是鏢隊或行商夜宿後留下的痕跡。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fork-field",
      "coord": [-1, 3, 0],
      "labels": ["west-fork", "world-link-west"],
      "exits": [
        { "direction": "east", "to": 9304 },
        { "direction": "west", "to": 9306 }
      ],
      "enquires": ["新野", "西路"]
    },
    {
      "vnum": 9306,
      "name": "押運土道",
      "description": "這段土道比主路更顛簸，卻能避開官道上最顯眼的盤查點。幾道新鮮車痕往西北斜去，顯示近來押運頻繁。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fork-field",
      "coord": [-2, 3, 0],
      "labels": ["escort-route"],
      "exits": [
        { "direction": "east", "to": 9305 },
        { "direction": "south", "to": 9307 }
      ]
    },
    {
      "vnum": 9307,
      "name": "蘆棚歇腳點",
      "description": "幾座臨時蘆棚圍成半圈，棚下留有舊水缸與破布包。看似平常歇腳點，卻常有人在夜裡悄悄交換情報。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fork-field",
      "coord": [-2, 2, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "north", "to": 9306 }
      ],
      "jobs": [
        {
          "keyword": "拉桿",
          "function": "job_pull_bar",
          "position": "POS_STANDING"
        }
      ]
    },
    {
      "vnum": 9308,
      "name": "南向長坡",
      "description": "地勢向南緩緩下沉，遠方可見河霧貼地飄移。這段路白天看似平和，入夜後卻常傳出劫道與追緝消息。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-south-trunk",
      "coord": [0, 4, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 9304 }
      ],
      "enquires": ["江夏", "南路"]
    },
    {
      "vnum": 9309,
      "name": "驛館後院",
      "description": "後院堆著草料與木桶，牆角有一口常年半掩的地窖門。驛卒對此總是語焉不詳，只說別在深夜下去。",
      "sector_type": "SECT_FIELD",
      "cluster": "posthouse-cellar",
      "coord": [-1, 2, 0],
      "labels": ["posthouse", "hidden-entry"],
      "exits": [
        { "direction": "west", "to": 9304 },
        { "direction": "enter", "to": 9310 }
      ],
      "keywords": [
        {
          "keyword": "地窖門",
          "description": "厚木門板潮得發黑，門環上纏著新換的麻繩，像是近期才被頻繁開關。"
        }
      ],
      "enquires": ["驛館", "地窖"]
    },
    {
      "vnum": 9310,
      "name": "石階地窖",
      "description": "地窖內潮氣濃重，石階向下延伸到更暗的甬道口。牆面刻著模糊路記，似乎指向不在官圖上的秘密路線。",
      "sector_type": "SECT_INSIDE",
      "cluster": "posthouse-cellar",
      "coord": [-1, 2, -1],
      "labels": ["cellar", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 9309 }
      ],
      "enquires": ["出口", "暗道"]
    }
  ]
}
```
