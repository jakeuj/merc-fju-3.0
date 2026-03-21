# 壽春 (`city_shouchun`)

## Area Intent

`city_shouchun` 承接 `road_shouchun_xuzhou` 南下官道口，把玩家從淮東驛路正式收束進壽春這座淮南據點。這裡不是單純的下一座城，而是一個負責把北路旅人重新安頓下來、分流到田野與更南主線的城市 hub。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `淮南據點 / 北段轉運城`
- LevelRange: `24-36`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_shouchun",
    "title": "壽春",
    "design_notes": "第一版 spec-first 草案。先固定北門入口、主街十字、市集補給、官署前街與城外田野出口，讓淮東官道正式收束成壽春母城節點。",
    "level_range": "24-36",
    "planned_vnum_range": "17001-17020",
    "reserved_room_block": "17001-17020",
    "theme": {
      "primary": "歷史城市",
      "secondary": "淮南據點 / 北段轉運城"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 17001,
        "target_area": "road_shouchun_xuzhou",
        "label": "淮東官道"
      },
      {
        "direction": "out",
        "source_vnum": 17008,
        "target_area": "wild_shouchun_fields",
        "label": "壽春田野"
      },
      {
        "direction": "south",
        "source_vnum": 17009,
        "target_area": "city_jianye",
        "label": "建業南路"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北門緩衝帶" },
      { "id": "main-street", "label": "主街與城心" },
      { "id": "market-yard", "label": "市集補給帶" },
      { "id": "office-lane", "label": "官署前街" },
      { "id": "outer-link", "label": "城外分流帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17001,
      "name": "北門外道",
      "description": "經過長段官道後，壽春北門終於在視野裡站穩了下來。門外仍帶著旅路塵氣，但城牆、旌牌與盤查目光已經把這裡的節奏從路上的漂移重新收回一座城的秩序裡。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 17002 }
      ],
      "enquires": ["壽春", "北門", "官道"]
    },
    {
      "vnum": 17002,
      "name": "北門甬道",
      "description": "甬道兩側的木牌與巡夜告示讓剛進城的人立刻收起旅路上的鬆散。和徐州相比，這裡多了幾分淮南重鎮的防備感，像任何進出都會先被這座城默默記上一筆。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "north", "to": 17001 },
        { "direction": "south", "to": 17003 }
      ],
      "enquires": ["告示", "巡夜"]
    },
    {
      "vnum": 17003,
      "name": "壽春主街",
      "description": "主街上人流雖多，卻不像州城那樣四面消息翻湧，而更像一座據點城市把路上來的人逐一消化。糧車、差役與店招都在說同一件事：這裡是往南與往外再分流前的穩定落腳點。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, 1, 0],
      "labels": ["main-road", "city-flow"],
      "exits": [
        { "direction": "north", "to": 17002 },
        { "direction": "south", "to": 17004 },
        { "direction": "west", "to": 17005 }
      ],
      "enquires": ["主街", "市集", "官署"]
    },
    {
      "vnum": 17004,
      "name": "城心十字",
      "description": "四面街路在這裡交會，一邊往官署，一邊往田野外口，還有更南的道路繼續把人往江東帶去。壽春真正的價值，就在這種既能收束旅程又能迅速再分流的城心節奏。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, 2, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "north", "to": 17003 },
        { "direction": "west", "to": 17006 },
        { "direction": "east", "to": 17007 },
        { "direction": "out", "to": 17008 },
        { "direction": "south", "to": 17009 }
      ],
      "enquires": ["去路", "田野", "南路"]
    },
    {
      "vnum": 17005,
      "name": "市集牌樓",
      "description": "牌樓下糧袋、藥包與水囊堆得很整齊，讓人一看就知道這是專門服務長路與轉運的市集。和北路官道相比，這裡終於有了可以真正停下來整補行囊的厚度。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [0, 1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "east", "to": 17003 }
      ],
      "enquires": ["市集", "糧行", "補給"]
    },
    {
      "vnum": 17006,
      "name": "官署前街",
      "description": "官署前街比主街安靜得多，來往的多是抱文冊的人與等候通傳的差役。這裡把壽春從普通商鎮拉成一座真正有軍政分量的據點，也讓北路消息在此多了一層過濾與判斷。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-lane",
      "coord": [0, 2, 0],
      "labels": ["office", "authority"],
      "exits": [
        { "direction": "east", "to": 17004 }
      ],
      "enquires": ["官署", "差役", "公文"]
    },
    {
      "vnum": 17007,
      "name": "東街坊口",
      "description": "東街坊口的氣氛比城心輕些，像專門留給本地人和中短程行旅喘口氣的地方。可只要往外看，就會知道這座城並沒有真正鬆下來，因為田野和南路都還等著被分派出去。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-link",
      "coord": [2, 2, 0],
      "labels": ["ward", "city-edge"],
      "exits": [
        { "direction": "west", "to": 17004 }
      ],
      "enquires": ["坊口", "外城"]
    },
    {
      "vnum": 17008,
      "name": "田野外口",
      "description": "出了外口，城牆的壓力立刻薄了幾分，取而代之的是田埂、風聲與外郊路感。這裡像壽春特地留給人往外試探的一道口子，讓城市和田野彼此只隔著一步之遙。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-link",
      "coord": [1, 3, 0],
      "labels": ["out-link", "field-edge"],
      "exits": [
        { "direction": "enter", "to": 17004 }
      ],
      "enquires": ["田野", "外面", "去路"]
    },
    {
      "vnum": 17009,
      "name": "南路牌口",
      "description": "往南的路牌把視線一路拖向更遠的江東腹地，像是在提醒旅人壽春不是終點，而是下一段主線真正重新發動的地方。站在這裡時，北路疲態與城內補給已經混成了新的出發感。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-link",
      "coord": [1, 1, 0],
      "labels": ["south-link", "route-node"],
      "exits": [
        { "direction": "north", "to": 17004 }
      ],
      "enquires": ["南路", "建業", "去路"]
    }
  ]
}
```
