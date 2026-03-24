# 南皮 (`city_nanpi`)

## Area Intent

`city_nanpi` 承接 `city_puyang` 北路牌樓，把玩家從前沿軍旅主城帶進一座更具河北地方秩序與勢力氣味的城鎮。這裡不是單純換一個城市名字，而是要讓節奏從濮陽的糧道壓力，轉成北地主城的主街、市面、官署與出城分流。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `河北城鎮 / 袁紹勢力前帶`
- LevelRange: `24-36`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_nanpi",
    "title": "南皮",
    "design_notes": "第一版 spec-first 草案。先固定南口北路、主街十字、市集補給、官署前街與東向平原分流，讓南皮成為河北主線的下一座城市 hub。",
    "level_range": "24-36",
    "planned_vnum_range": "17401-17420",
    "reserved_room_block": "17401-17420",
    "theme": {
      "primary": "歷史城市",
      "secondary": "河北城鎮 / 袁紹勢力前帶"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 17401,
        "target_area": "city_puyang",
        "label": "河北南路"
      },
      {
        "direction": "east",
        "source_vnum": 17408,
        "target_area": "wild_hebei_plain",
        "label": "平原外道"
      },
      {
        "direction": "north",
        "source_vnum": 17409,
        "target_area": "road_nanpi_beiping",
        "label": "河北北道"
      }
    ],
    "clusters": [
      { "id": "south-gate", "label": "南口北路" },
      { "id": "main-street", "label": "主街與城心" },
      { "id": "market-yard", "label": "市集補給帶" },
      { "id": "east-road", "label": "平原外道帶" },
      { "id": "north-road", "label": "北道分流帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17401,
      "name": "南路牌口",
      "description": "從濮陽一路北來時，南皮的第一印象不像前線那麼緊，而是帶著一種有勢力、有秩序、也有地方脾氣的北城感。南路牌口把進城的腳步慢慢收緊，像任何外來消息都會先在這裡被看上一眼。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 17209, "external": true },
        { "direction": "north", "to": 17402 }
      ],
      "enquires": ["南路", "濮陽", "進城"]
    },
    {
      "vnum": 17402,
      "name": "南皮南街",
      "description": "南街的屋舍與牌樓比濮陽更有地方城鎮的煙火氣，卻也不乏守望與打量的眼神。越往城心走，越能感覺這裡並非單純商街，而是一座會把各路人等重新編進地方秩序的北方城鎮。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 1, 0],
      "labels": ["street", "transition"],
      "exits": [
        { "direction": "south", "to": 17401 },
        { "direction": "north", "to": 17403 }
      ],
      "enquires": ["南街", "城裡"]
    },
    {
      "vnum": 17403,
      "name": "南皮主街",
      "description": "主街上人流穩定，往來的不只是貨客，也有替各方勢力跑腿的差人與傳話者。與濮陽那種隨時聞得到前線的味道不同，這裡更像是一座把北地消息慢慢沉澱成地方秩序的城市。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 2, 0],
      "labels": ["main-road", "city-flow"],
      "exits": [
        { "direction": "south", "to": 17402 },
        { "direction": "north", "to": 17404 },
        { "direction": "west", "to": 17405 }
      ],
      "enquires": ["主街", "南皮", "消息"]
    },
    {
      "vnum": 17404,
      "name": "城心十字",
      "description": "城心十字把南皮真正的性格攤在眼前：西邊是較有人聲的市集，東邊是往平原外道的分流，北邊則是更遠的河北北路。站在這裡時，最能感覺這座城不是前線，也不是單純後方，而是北地主線的真正轉運點。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 3, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "south", "to": 17403 },
        { "direction": "west", "to": 17406 },
        { "direction": "east", "to": 17408 },
        { "direction": "north", "to": 17409 }
      ],
      "enquires": ["去路", "平原", "北道"]
    },
    {
      "vnum": 17405,
      "name": "里坊側街",
      "description": "這條側街沒有主街那麼開闊，卻能更清楚看見南皮居民日常生活的節奏。坊門、院牆和低聲談話把城市的地方性格收得很緊，像外人很容易在這裡被一眼認出來。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 2, 0],
      "labels": ["residential", "side-lane"],
      "exits": [
        { "direction": "east", "to": 17403 }
      ],
      "enquires": ["里坊", "住戶"]
    },
    {
      "vnum": 17406,
      "name": "市集牌樓",
      "description": "牌樓和棚市把這裡撐成一塊熱鬧卻不失規矩的補給帶，貨色以布匹、乾糧、路具和日用雜貨為主。與濮陽賣的是前線急用不同，南皮市集更像在替整個河北主線維持穩定流通。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 3, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "east", "to": 17404 },
        { "direction": "north", "to": 17407 }
      ],
      "enquires": ["市集", "補給", "買賣"]
    },
    {
      "vnum": 17407,
      "name": "官署前街",
      "description": "越靠近官署，街上的聲音就會自然壓低一些。這裡讓人強烈感受到南皮並不是鬆散城鎮，而是一座有地方勢力、有行政秩序，也有明確權力層次的北方主城。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 4, 0],
      "labels": ["office", "authority"],
      "exits": [
        { "direction": "south", "to": 17406 }
      ],
      "enquires": ["官署", "勢力", "告示"]
    },
    {
      "vnum": 17408,
      "name": "東向平原口",
      "description": "東邊的城口把視線慢慢放向更開闊的河北平原，連風都像變得更直接一些。這裡不像主街那麼有人聲，卻能讓人清楚意識到南皮並不是終點，而只是更大北地路網的一個節點。",
      "sector_type": "SECT_CITY",
      "cluster": "east-road",
      "coord": [1, 3, 0],
      "labels": ["east-link", "open-road"],
      "exits": [
        { "direction": "west", "to": 17404 },
        { "direction": "east", "to": 17501, "external": true }
      ],
      "enquires": ["平原", "東路", "外道"]
    },
    {
      "vnum": 17409,
      "name": "北道牌樓",
      "description": "北道牌樓比南路牌口更有遠行感，來往者的裝束與口音也明顯更雜。站在這裡時，會覺得南皮真正的角色不是把路收住，而是把不同方向的河北消息整成能繼續往北送出的秩序。",
      "sector_type": "SECT_CITY",
      "cluster": "north-road",
      "coord": [0, 4, 0],
      "labels": ["north-link", "gate-road"],
      "exits": [
        { "direction": "south", "to": 17404 }
      ],
      "enquires": ["北道", "北邊", "去路"]
    }
  ]
}
```
