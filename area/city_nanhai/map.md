# 南海 (`city_nanhai`)

## Area Intent

`city_nanhai` 承接 `city_guiyang` 南向主線，讓玩家從桂陽的邊地轉運節奏，再往南推進後，進入一座真正帶海風、碼頭、南貨與遠航氣味的港城 hub。

第一版目標先固定：

- 一條由北向南穿過城門、港街、市集與臨海路的主探索線
- 一條往港務與補給區延伸的側線
- 一條 `up/down` 連到望臺或坡港高處的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示南海、桂陽、碼頭、海路與更南去路

## Theme Positioning

- Theme: `探險`
- Subtheme: `海港 / 遠航`
- LevelRange: `96-100`
- Parent region: `南境海門`
- World gap filled: 讓南境主線從桂陽繼續推進到南海港市，為海路、遠航與更南題材建立穩定城市 hub

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_nanhai",
    "title": "南海",
    "design_notes": "第一版 spec-first 草案。先固定北門、港街、市集、港務前院與南向臨海路骨架，讓南境主線在南海收束成更開闊的海港 hub。",
    "level_range": "96-100",
    "planned_vnum_range": "15501-15530",
    "reserved_room_block": "15501-15530",
    "theme": {
      "primary": "探險",
      "secondary": "海港 / 遠航"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 15501,
        "target_area": "city_guiyang",
        "label": "桂陽南路"
      },
      {
        "direction": "south",
        "source_vnum": 15510,
        "target_area": "sea_south_route",
        "label": "外海南航"
      },
      {
        "direction": "east",
        "source_vnum": 15512,
        "target_area": "district_nanhai_port",
        "label": "港埠棧橋"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北向城門" },
      { "id": "harbor-street", "label": "港街主線" },
      { "id": "market-quarter", "label": "市集補給區" },
      { "id": "port-office", "label": "港務前院" },
      { "id": "south-seafront", "label": "臨海南口" }
    ]
  },
  "rooms": [
    {
      "vnum": 15501,
      "name": "北向城門",
      "description": "自桂陽再往南行到此，城門外的風裡已明顯帶著鹹潮與遠水氣味。這裡仍保有城市秩序，卻也讓人一踏進來就知道，接下來的方向不再只是官道，而是更大的水路與海路。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "north", "to": 15210, "external": true },
        { "direction": "south", "to": 15503 },
        { "direction": "east", "to": 15502 },
        { "direction": "west", "to": 15505 }
      ],
      "enquires": ["桂陽", "進城"]
    },
    {
      "vnum": 15502,
      "name": "北牌港坡",
      "description": "坡口邊掛著幾面指往桂陽、港埠與外海棧橋的木牌，邊角都被潮風吹得發亮。來往商旅與水手總會在這裡稍微停一下，像在心裡重新盤算自己接下來走的是陸路、港路還是海路。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["wayfinding", "slope"],
      "exits": [
        { "direction": "west", "to": 15501 },
        { "direction": "south", "to": 15504 }
      ],
      "enquires": ["路牌", "港埠"]
    },
    {
      "vnum": 15503,
      "name": "南海港街",
      "description": "港街把城門、市集與臨海路穩穩串成一條主線，行人與貨車不算喧鬧，卻始終帶著一種港城獨有的流動感。站在這裡時，很容易感覺到南海不只是終點，也是另一段遠行的起點。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-street",
      "coord": [0, -1, 0],
      "labels": ["main-street", "harbor"],
      "exits": [
        { "direction": "north", "to": 15501 },
        { "direction": "east", "to": 15504 },
        { "direction": "south", "to": 15506 }
      ],
      "enquires": ["南海", "市集"]
    },
    {
      "vnum": 15504,
      "name": "港街十字",
      "description": "南貨招牌、港務榜示與遠行叫賣聲在這裡交會，讓南海作為最南港城的節奏一眼可辨。站在十字口時，你會自然明白哪裡能補給、哪裡能問海路、哪裡則會把你送向棧橋與外海。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-street",
      "coord": [1, -1, 0],
      "labels": ["crossroads", "civic"],
      "exits": [
        { "direction": "north", "to": 15502 },
        { "direction": "west", "to": 15503 },
        { "direction": "east", "to": 15508 },
        { "direction": "south", "to": 15507 },
        { "direction": "up", "to": 15511 }
      ],
      "enquires": ["官府", "海路", "碼頭"]
    },
    {
      "vnum": 15505,
      "name": "北巷貨棚",
      "description": "這條北巷比港街安靜，牆邊卻堆著從南北兩路送來的貨簍與繩具。它不像主街那麼醒目，卻讓整座南海顯得更像真正有人長住、也有人準備一出海就很久不回的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [-1, 0, 0],
      "labels": ["side-lane", "cargo"],
      "exits": [
        { "direction": "east", "to": 15501 }
      ],
      "enquires": ["貨棚", "城門"]
    },
    {
      "vnum": 15506,
      "name": "南貨市口",
      "description": "市口裡擺滿乾貨、藥材、繩索與海行必需的小器具，像所有長途遠行最後都會在這裡補齊一輪。比起內陸城市，這裡更有一種『該備的東西一樣都不能少』的港城務實氣味。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [0, -2, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 15503 },
        { "direction": "east", "to": 15507 }
      ],
      "enquires": ["市集", "補給"]
    },
    {
      "vnum": 15507,
      "name": "藥舖街角",
      "description": "幾家藥舖與行商把街角擠得滿是草藥、桐油與海鹽味，來往行旅在這裡總會不自覺多停一會。這種節奏讓南海顯得既不張揚，卻又明顯是所有遠航前該來的一站。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [1, -2, 0],
      "labels": ["herbal", "service"],
      "exits": [
        { "direction": "north", "to": 15504 },
        { "direction": "west", "to": 15506 },
        { "direction": "south", "to": 15510 }
      ],
      "enquires": ["藥舖", "南口"]
    },
    {
      "vnum": 15508,
      "name": "港務前街",
      "description": "港務前街雖然整齊，卻不像帝都衙門那樣板正，反而有一種港城辦事講效率也講水路時刻的風格。榜示貼得清楚，來往的人也總會下意識瞄上一眼，像這裡是整座南海的節奏器。",
      "sector_type": "SECT_CITY",
      "cluster": "port-office",
      "coord": [2, -1, 0],
      "labels": ["port-office", "order"],
      "exits": [
        { "direction": "north", "to": 15509 },
        { "direction": "west", "to": 15504 },
        { "direction": "south", "to": 15512 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜示上既有港務消息，也有船期、潮汐與外海南航提醒，讓人一看就知道這裡已是南境海門。"
        }
      ],
      "enquires": ["港務", "榜示"]
    },
    {
      "vnum": 15509,
      "name": "港務偏院",
      "description": "偏院不大，卻收拾得頗有秩序，像地方主事者把文牘、貨單與船期消息暫時收進來整理的角落。比起熱鬧市口，這裡更像南海真正穩住節奏的後場。",
      "sector_type": "SECT_CITY",
      "cluster": "port-office",
      "coord": [2, 0, 0],
      "labels": ["side-yard", "quiet"],
      "exits": [
        { "direction": "south", "to": 15508 }
      ],
      "enquires": ["偏院", "消息"]
    },
    {
      "vnum": 15510,
      "name": "臨海南口",
      "description": "南口外的道路很快就被更開闊的風與水氣接手，地面上留著長年貨車、鹽包與船夫腳步壓出的痕跡。站在這裡時，你會清楚地知道，這一帶真正往前走的方式已不只靠雙腳。 ",
      "sector_type": "SECT_CITY",
      "cluster": "south-seafront",
      "coord": [1, -3, 0],
      "labels": ["south-edge", "seafront"],
      "exits": [
        { "direction": "north", "to": 15507 }
      ],
      "enquires": ["外海", "南邊"]
    },
    {
      "vnum": 15511,
      "name": "臨海望臺",
      "description": "走上望臺後，能把北門、港街與更遠的海面收進眼底。從這裡看南海，會更明白它雖是主線南端城市，卻也是把玩家送往更遠世界的門面。",
      "sector_type": "SECT_CITY",
      "cluster": "port-office",
      "coord": [1, -1, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15504 }
      ],
      "enquires": ["望臺", "海面"]
    },
    {
      "vnum": 15512,
      "name": "東棧路牌",
      "description": "一面路牌立在港務前街側緣，明白指著東向棧橋與更細的港埠分區。它替南海添上一層不只守著陸路終點，也能把人送進真正水路網的港城氣味。",
      "sector_type": "SECT_CITY",
      "cluster": "south-seafront",
      "coord": [2, -2, 0],
      "labels": ["marker", "east-link"],
      "exits": [
        { "direction": "north", "to": 15508 }
      ],
      "enquires": ["棧橋", "東邊", "去路"]
    }
  ]
}
```
