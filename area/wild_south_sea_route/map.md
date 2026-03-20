# 南海外航道 (`wild_south_sea_route`)

## Area Intent

`wild_south_sea_route` 承接 `city_nanhai` 的臨海南口，讓玩家從港城秩序切進更看潮汐、礁岸與航道辨位的南境海路前帶。

第一版目標先固定：

- 一條由北向南穿過近岸棧道、潮石灣與外航前帶的主探索線
- 一條往退潮礁坪與側向港外棧橋延伸的側線
- 一條 `up/down` 連到風望高臺與低潮礁面的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示南海、外海、礁岸、棧橋與更深航路

## Theme Positioning

- Theme: `探險`
- Subtheme: `外海南航 / 礁岸水道`
- LevelRange: `98-100`
- Parent region: `南境外海前帶`
- World gap filled: 讓南海港城外的臨海南口正式延伸成可進入的海路 wild，為更深外海與群島題材建立第一層水域前帶

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_south_sea_route",
    "title": "南海外航道",
    "design_notes": "第一版 spec-first 草案。先固定南海南口外的近岸棧道、潮石灣、浮標水道、退潮礁坪與風望高臺，讓南境主線在港城之後自然切進海路 wild。",
    "level_range": "98-100",
    "planned_vnum_range": "15601-15630",
    "reserved_room_block": "15601-15630",
    "theme": {
      "primary": "探險",
      "secondary": "外海南航 / 礁岸水道"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 15601,
        "target_area": "city_nanhai",
        "label": "南海臨海南口"
      },
      {
        "direction": "south",
        "source_vnum": 15610,
        "target_area": "sea_outer_isles",
        "label": "外海群島"
      },
      {
        "direction": "east",
        "source_vnum": 15612,
        "target_area": "district_nanhai_port",
        "label": "港外棧橋"
      }
    ],
    "clusters": [
      { "id": "north-entry", "label": "近岸入口" },
      { "id": "pier-path", "label": "棧道主線" },
      { "id": "reef-bend", "label": "礁岸岔帶" },
      { "id": "tide-flat", "label": "退潮礁坪" },
      { "id": "watch-rise", "label": "風望高臺" }
    ]
  },
  "rooms": [
    {
      "vnum": 15601,
      "name": "近岸棧口",
      "description": "離開南海南口後，石地很快就被潮濕木板與繩柱接手，連腳步聲也從城街的乾脆變成帶著海水回響的節奏。站在這裡時，你會立刻感覺到自己已經離開單純的陸路。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "north", "to": 15510, "external": true },
        { "direction": "south", "to": 15603 },
        { "direction": "east", "to": 15602 }
      ],
      "enquires": ["南海", "入口"]
    },
    {
      "vnum": 15602,
      "name": "漁具歇棚",
      "description": "幾面曬網與木桶靠在歇棚邊，棚角還掛著被海風吹得發硬的繩圈。比起城內的貨棚，這裡更像真正準備面對海面變化的人才會停下來整理裝備的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-entry",
      "coord": [1, 0, 0],
      "labels": ["rest-shed", "gear"],
      "exits": [
        { "direction": "west", "to": 15601 }
      ],
      "enquires": ["漁具", "歇腳"]
    },
    {
      "vnum": 15603,
      "name": "近海棧道",
      "description": "棧道順著岸線一路向南伸去，腳下木板會隨浪聲微微響動，讓每一步都像在提醒你海面永遠不是完全靜止的。這裡還算貼著岸，但節奏已經不是城裡能掌控的那種穩定。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "pier-path",
      "coord": [0, -1, 0],
      "labels": ["main-path", "pier"],
      "exits": [
        { "direction": "north", "to": 15601 },
        { "direction": "south", "to": 15604 },
        { "direction": "west", "to": 15605 }
      ],
      "enquires": ["海路", "外海"]
    },
    {
      "vnum": 15604,
      "name": "潮石灣",
      "description": "幾塊黑亮潮石把灣口分成若隱若現的幾條水線，熟路的人一眼就看得出哪邊能過，外人卻很容易被表面平靜騙住。這裡像是南海外航道真正開始考驗判斷力的地方。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "reef-bend",
      "coord": [0, -2, 0],
      "labels": ["reef", "bay"],
      "exits": [
        { "direction": "north", "to": 15603 },
        { "direction": "south", "to": 15608 },
        { "direction": "east", "to": 15607 }
      ],
      "enquires": ["礁石", "水道"]
    },
    {
      "vnum": 15605,
      "name": "退潮礁坪",
      "description": "退潮時露出的礁坪表面濕滑卻寬闊，像多出了一段暫時可走、卻不一定能準時回收的路。站在這裡時，很容易明白海路最麻煩的地方不是有沒有路，而是路什麼時候還算你的。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "tide-flat",
      "coord": [-1, -1, -1],
      "labels": ["low-tide", "reef-flat"],
      "exits": [
        { "direction": "east", "to": 15603 },
        { "direction": "south", "to": 15606 }
      ],
      "enquires": ["退潮", "礁坪"]
    },
    {
      "vnum": 15606,
      "name": "浪痕低道",
      "description": "低道沿著礁面邊緣延伸，兩側浪痕一層壓著一層，像在告訴人這段路從來不真正屬於誰。你若在這裡停得太久，連方向感都會被潮聲慢慢磨散。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "tide-flat",
      "coord": [-1, -2, -1],
      "labels": ["low-path", "waves"],
      "exits": [
        { "direction": "north", "to": 15605 },
        { "direction": "east", "to": 15608 }
      ],
      "enquires": ["浪痕", "退路"]
    },
    {
      "vnum": 15607,
      "name": "浮標水道",
      "description": "幾支被海風與鹽霧磨得發白的浮標排出一道勉強算穩的水道，像替真正要往外海去的人留下一條最基本的秩序。只是那秩序看起來永遠都比城裡任何路牌脆弱得多。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "reef-bend",
      "coord": [1, -2, 0],
      "labels": ["buoys", "channel"],
      "exits": [
        { "direction": "west", "to": 15604 },
        { "direction": "east", "to": 15609 }
      ],
      "keywords": [
        {
          "keyword": "浮標",
          "description": "木製浮標雖然被潮水與鹽霧侵蝕得厲害，仍盡力把可通行的那道水線指給真正懂得看路的人。"
        }
      ],
      "enquires": ["浮標", "水道"]
    },
    {
      "vnum": 15608,
      "name": "外航前帶",
      "description": "再往前去，岸影開始後退，風聲則明顯多了更寬闊水面的空曠感。這裡不像真正的外海中心，卻已經足夠讓人感受到，回港與繼續往前之間的差別正在快速變大。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "pier-path",
      "coord": [0, -3, 0],
      "labels": ["mainline", "outer-route"],
      "exits": [
        { "direction": "north", "to": 15604 },
        { "direction": "west", "to": 15606 },
        { "direction": "south", "to": 15610 },
        { "direction": "up", "to": 15611 }
      ],
      "enquires": ["外海", "去路", "南邊"]
    },
    {
      "vnum": 15609,
      "name": "東向側棧",
      "description": "一道較窄的側棧往東偏出，木板聲和海風在這裡貼得更近，讓人感覺自己像站在港城與外海之間最細的一條縫上。它不是主路，卻像所有熟門熟路的人都會記住的一條捷徑。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "reef-bend",
      "coord": [2, -2, 0],
      "labels": ["east-branch", "pier-link"],
      "exits": [
        { "direction": "north", "to": 15612 },
        { "direction": "west", "to": 15607 }
      ],
      "enquires": ["東邊", "棧橋"]
    },
    {
      "vnum": 15610,
      "name": "南航分水",
      "description": "前方水面逐漸把近岸與外海分成不同顏色與不同脾氣的幾條線，像任何一步都可能正式把你送進另一個尺度的航程。這裡不像終點，更像真正遠行開始被海面承認的地方。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "pier-path",
      "coord": [0, -4, 0],
      "labels": ["south-edge", "deep-route"],
      "exits": [
        { "direction": "north", "to": 15608 },
        { "direction": "down", "to": 15701, "external": true }
      ],
      "enquires": ["南航", "更南", "下面"]
    },
    {
      "vnum": 15611,
      "name": "風望高臺",
      "description": "沿著高起礁脊走上來後，能看見港城、近岸棧道與外航前帶如何一段段向海面打開。這樣的高度讓人暫時恢復判斷，卻也讓海路的風險變得更一目了然。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "watch-rise",
      "coord": [0, -3, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15608 }
      ],
      "enquires": ["風向", "望臺"]
    },
    {
      "vnum": 15612,
      "name": "港外指標",
      "description": "一組立在側棧邊的繩柱與木牌把港外方向、回港方向與棧橋分區清楚分開，像是海面上少數還願意講道理的秩序殘片。只要再往東去，節奏就會更偏向真正的港埠網與船泊區。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "watch-rise",
      "coord": [2, -1, 0],
      "labels": ["marker", "east-link"],
      "exits": [
        { "direction": "south", "to": 15609 }
      ],
      "enquires": ["港外", "指標", "去路"]
    }
  ]
}
```
