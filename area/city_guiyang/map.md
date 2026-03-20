# 桂陽 (`city_guiyang`)

## Area Intent

`city_guiyang` 承接 `city_lingling` 南向主線，讓玩家從零陵山城再往南推進後，進入一座更靠邊地、更有南貨、南路與遠行氣味的城鎮 hub。

第一版目標先固定：

- 一條由北向南穿過城門、主街與南口的主探索線
- 一條往市集與補給區延伸的側線
- 一條 `up/down` 連到城樓或坡城望臺的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示桂陽、零陵、南海、南蠻與更南去路

## Theme Positioning

- Theme: `江湖`
- Subtheme: `南嶺城鎮 / 邊地轉運`
- LevelRange: `90-100`
- Parent region: `荊南最南段`
- World gap filled: 讓南境主線從零陵繼續推進到桂陽，為南海與南蠻方向建立最後一層穩定城市 hub

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_guiyang",
    "title": "桂陽",
    "design_notes": "第一版 spec-first 草案。先固定北門、主街、市集、官署與南向出城骨架，讓南境主線在桂陽收束成更靠邊地的城鎮 hub。",
    "level_range": "90-100",
    "planned_vnum_range": "15201-15230",
    "reserved_room_block": "15201-15230",
    "theme": {
      "primary": "江湖",
      "secondary": "南嶺城鎮 / 邊地轉運"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 15201,
        "target_area": "city_lingling",
        "label": "零陵北路"
      },
      {
        "direction": "south",
        "source_vnum": 15210,
        "target_area": "city_nanhai",
        "label": "南海港路"
      },
      {
        "direction": "west",
        "source_vnum": 15212,
        "target_area": "wild_nanman_jungle",
        "label": "南蠻外徑"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北向城門" },
      { "id": "main-street", "label": "主街中心" },
      { "id": "market-quarter", "label": "市集補給區" },
      { "id": "yamen-quarter", "label": "官署與榜示區" },
      { "id": "south-road", "label": "南向出城區" }
    ]
  },
  "rooms": [
    {
      "vnum": 15201,
      "name": "北向城門",
      "description": "自零陵再往南行到此，城門與坡道讓人明顯感覺到自己已更靠近邊地。這裡仍保有城市秩序，卻多了一種『再往下去就不是普通官道了』的臨界感。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "south", "to": 15203 },
        { "direction": "east", "to": 15202 },
        { "direction": "west", "to": 15205 }
      ],
      "enquires": ["零陵", "進城"]
    },
    {
      "vnum": 15202,
      "name": "北牌坡口",
      "description": "坡口邊掛著幾面指往零陵、南海與邊地林線的路牌，木面斑駁卻仍收拾得乾淨。來往商旅總會在這裡停一下，像在心裡重新盤算自己接下來要走的是哪一種遠路。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["wayfinding", "slope"],
      "exits": [
        { "direction": "west", "to": 15201 },
        { "direction": "south", "to": 15204 }
      ],
      "enquires": ["路牌", "去路"]
    },
    {
      "vnum": 15203,
      "name": "桂陽主街",
      "description": "主街把城門、市集與官署串成穩定的一條線，行人雖不算擁擠，卻總帶著一種邊地城鎮才有的務實與緊湊。站在這裡時，很容易感覺到桂陽是讓更南路線重新變得可控的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, -1, 0],
      "labels": ["main-street", "hub"],
      "exits": [
        { "direction": "north", "to": 15201 },
        { "direction": "east", "to": 15204 },
        { "direction": "south", "to": 15206 }
      ],
      "enquires": ["桂陽", "市集"]
    },
    {
      "vnum": 15204,
      "name": "主街十字",
      "description": "榜示、店招與南貨叫賣聲在這裡交會，讓桂陽作為邊地轉運城鎮的節奏一眼可辨。站在十字口時，你會自然明白哪裡能補給、哪裡能問路、哪裡則會把你送向更南與更野的方向。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, -1, 0],
      "labels": ["crossroads", "civic"],
      "exits": [
        { "direction": "north", "to": 15202 },
        { "direction": "west", "to": 15203 },
        { "direction": "east", "to": 15208 },
        { "direction": "south", "to": 15207 },
        { "direction": "up", "to": 15211 }
      ],
      "enquires": ["官府", "南海", "南蠻"]
    },
    {
      "vnum": 15205,
      "name": "北巷轉角",
      "description": "這條北巷比主街安靜，牆角卻仍留著來往商旅與馬匹的痕跡。它不像主街那麼醒目，卻讓整座桂陽顯得更像真正有人長住、也有人準備繼續遠行的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [-1, 0, 0],
      "labels": ["side-lane", "quiet"],
      "exits": [
        { "direction": "east", "to": 15201 }
      ],
      "enquires": ["巷子", "城門"]
    },
    {
      "vnum": 15206,
      "name": "南貨市口",
      "description": "市口裡堆著乾貨、藥材、繩索與遠行必需的小器具，像一切都在為更南、更遠的旅程準備。比起北方城市，這裡更有一種『先把東西備齊再說』的邊地實用氣味。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [0, -2, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 15203 },
        { "direction": "east", "to": 15207 }
      ],
      "enquires": ["市集", "補給"]
    },
    {
      "vnum": 15207,
      "name": "藥鋪街角",
      "description": "幾家藥鋪與雜行把街角擠得滿是乾草藥與桐油味，來往行旅在這裡總會不自覺多停一會。這種節奏讓桂陽顯得既不張揚，卻又明顯是所有遠路前該來的一站。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [1, -2, 0],
      "labels": ["herbal", "service"],
      "exits": [
        { "direction": "north", "to": 15204 },
        { "direction": "west", "to": 15206 },
        { "direction": "south", "to": 15210 }
      ],
      "enquires": ["藥鋪", "南路"]
    },
    {
      "vnum": 15208,
      "name": "官署前街",
      "description": "官署前街雖然整齊，卻不像帝都那樣板正，反而有一種邊地辦事講效率也講人情的風格。榜示貼得清楚，來往的人也總會下意識瞄上一眼，像這裡是整座桂陽的節奏器。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, -1, 0],
      "labels": ["yamen", "order"],
      "exits": [
        { "direction": "north", "to": 15209 },
        { "direction": "west", "to": 15204 },
        { "direction": "south", "to": 15212 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜示上既有官道消息，也有更南路線與邊地盤查的提醒，讓人一看就知道這裡已接近主線末段。"
        }
      ],
      "enquires": ["官府", "榜示"]
    },
    {
      "vnum": 15209,
      "name": "城巷偏院",
      "description": "偏院不大，卻收拾得頗有秩序，像地方主事者把雜務與消息暫時收進來整理的角落。比起熱鬧市口，這裡更像桂陽真正穩住節奏的後場。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, 0, 0],
      "labels": ["side-yard", "quiet"],
      "exits": [
        { "direction": "south", "to": 15208 }
      ],
      "enquires": ["偏院", "消息"]
    },
    {
      "vnum": 15210,
      "name": "南門官道",
      "description": "南門外的官道把桂陽再往更深南境送去，地面上留下了長年車馬與遠行包袱壓出的痕跡。站在這裡時，你會清楚地知道，這一帶的安全與秩序正慢慢變成一種需要自己維持的事。 ",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [1, -3, 0],
      "labels": ["south-edge", "road"],
      "exits": [
        { "direction": "north", "to": 15207 }
      ],
      "enquires": ["南海", "南邊"]
    },
    {
      "vnum": 15211,
      "name": "坡城望樓",
      "description": "走上望樓後，能把北門、主街與更遠的南路都收入眼底。從這裡看桂陽，會更明白它雖是邊地城鎮，卻有一種替所有遠行人先穩住局面的力量。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [1, -1, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15204 }
      ],
      "enquires": ["望樓", "北門"]
    },
    {
      "vnum": 15212,
      "name": "西岔路牌",
      "description": "一面路牌立在南街側緣，明白指著西向外徑與更深邊地林線。它替桂陽添上一層不只守著官道，也能把人送往更野外帶的氣味，讓這座城顯得更接近主線末段邊界。",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [2, -2, 0],
      "labels": ["marker", "west-link"],
      "exits": [
        { "direction": "north", "to": 15208 }
      ],
      "enquires": ["南蠻", "西邊", "去路"]
    }
  ]
}
```
