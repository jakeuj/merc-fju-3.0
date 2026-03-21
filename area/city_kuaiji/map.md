# 會稽 (`city_kuaiji`)

## Area Intent

`city_kuaiji` 承接 `wild_mountain_pass` 的南下山門，把玩家從山風、棧路與崖邊小徑正式帶進會稽這座帶山城秩序、地方勢力與門派傳聞的江東城市，讓建業鏈重新回到可補給、可問路、也可向更深地脈與支線展開的城市節點。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `山城 / 門派`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_kuaiji",
    "title": "會稽",
    "design_notes": "第一版 spec-first 草案。先固定北口、主街、市集前帶、官廳街與東市轉角，讓江東山道主線正式收束成帶山城與門派氣息的城市 hub。",
    "level_range": "100-100",
    "planned_vnum_range": "16401-16430",
    "reserved_room_block": "16401-16430",
    "theme": {
      "primary": "江湖",
      "secondary": "山城 / 門派"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 16401,
        "target_area": "wild_mountain_pass",
        "label": "會稽北口"
      },
      {
        "direction": "east",
        "source_vnum": 16410,
        "target_area": "wild_river_delta",
        "label": "會稽東市外水"
      },
      {
        "direction": "down",
        "source_vnum": 16406,
        "target_area": "dng_temple_ruins",
        "label": "古祠地脈"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北口入城" },
      { "id": "main-street", "label": "主街中軸" },
      { "id": "market-yard", "label": "市集前帶" },
      { "id": "office-lane", "label": "官廳街" },
      { "id": "east-turn", "label": "東市轉角" }
    ]
  },
  "rooms": [
    {
      "vnum": 16401,
      "name": "北口山門",
      "description": "走出山道最後一段風口後，會稽北口的石門與城牆便把散亂的山路節奏重新收成有秩序的人聲和燈火。這裡不像建業那樣厚重，卻有一種山城才有的收束感，像每個進城的人都先得把一路風塵留在門外。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["north-link", "entry"],
      "exits": [
        { "direction": "north", "to": 16310, "external": true },
        { "direction": "south", "to": 16403 },
        { "direction": "east", "to": 16402 }
      ],
      "enquires": ["山門", "北口", "會稽"]
    },
    {
      "vnum": 16402,
      "name": "門旁值舍",
      "description": "值舍不大，卻把文書、告示與進出盤查都安排得井然有序，像會稽雖處山地，城裡的秩序卻並不打算讓山路旅人帶著太多僥倖混進來。比起大城官氣，這裡更像地方勢力自己磨出來的穩。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["guardhouse", "registry"],
      "exits": [
        { "direction": "west", "to": 16401 }
      ],
      "enquires": ["值舍", "告示"]
    },
    {
      "vnum": 16403,
      "name": "會稽北街",
      "description": "北街沿著山城地勢微微起伏，路旁的人聲和招牌不像平地城市那麼鋪張，卻自有一種靠山勢和久住之人撐出的熟稔感。走到這裡時，旅人很容易明白會稽既是城，也是許多江湖消息真正落腳的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 1, 0],
      "labels": ["main-road", "north-street"],
      "exits": [
        { "direction": "north", "to": 16401 },
        { "direction": "south", "to": 16404 },
        { "direction": "west", "to": 16405 }
      ],
      "enquires": ["北街", "市集", "主街"]
    },
    {
      "vnum": 16404,
      "name": "會稽主街",
      "description": "主街把城裡的人流、貨流和傳聞都攏在一條帶坡的石路上，像每一間鋪面與每一段街階都在提醒人這裡並不是單純的地方小城，而是足以聚攏江東各路人的真正節點。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 2, 0],
      "labels": ["center", "city-core"],
      "exits": [
        { "direction": "north", "to": 16403 },
        { "direction": "south", "to": 16408 },
        { "direction": "east", "to": 16406 }
      ],
      "enquires": ["主街", "官廳", "東市"]
    },
    {
      "vnum": 16405,
      "name": "坡上市集",
      "description": "市集沿著坡面擺開，攤架和屋簷一層層疊著，讓叫賣聲不像平地市街那樣橫向散開，而是順著高低起伏此起彼落。這裡最能讓人感覺到會稽那種山城特有的煙火氣。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "east", "to": 16403 },
        { "direction": "south", "to": 16407 }
      ],
      "enquires": ["市集", "補給", "攤子"]
    },
    {
      "vnum": 16406,
      "name": "官廳街前",
      "description": "官廳街前比主街安靜，但那種安靜裡明顯還混著地方門派、城中頭面與官署彼此觀望的味道。會稽的秩序不像帝都那樣單一，卻正因如此，這條街反而更耐人尋味。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-lane",
      "coord": [1, 2, 0],
      "labels": ["office", "authority"],
      "exits": [
        { "direction": "west", "to": 16404 },
        { "direction": "north", "to": 16409 }
      ],
      "enquires": ["官廳", "門派", "地脈"]
    },
    {
      "vnum": 16407,
      "name": "石階橫街",
      "description": "橫街被石階切出一層一層的視線，讓行人、挑夫和市集腳色都像在同一處來回錯身。比起建業那種寬闊主城感，這裡更像一座真正在山裡長出來的城市。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 2, 0],
      "labels": ["side-street", "stairs"],
      "exits": [
        { "direction": "north", "to": 16405 },
        { "direction": "east", "to": 16408 }
      ],
      "enquires": ["石階", "橫街"]
    },
    {
      "vnum": 16408,
      "name": "城心前庭",
      "description": "前庭把主街、市集和官廳街的節奏都交會在一起，站在這裡時，很容易感覺到會稽雖不如大都龐雜，卻已足夠把山道來客、城中勢力和各種流言都收進同一座城市的呼吸裡。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 3, 0],
      "labels": ["hub", "forecourt"],
      "exits": [
        { "direction": "north", "to": 16404 },
        { "direction": "west", "to": 16407 },
        { "direction": "east", "to": 16409 },
        { "direction": "south", "to": 16410 }
      ],
      "enquires": ["前庭", "去路", "城心"]
    },
    {
      "vnum": 16409,
      "name": "門派街口",
      "description": "街口一帶的人聲明顯比別處更壓低幾分，像很多事不是真的不能說，而是更適合在懂的人面前說。這裡不像宗門本身，卻已經足夠讓人意識到會稽並不只是普通城鎮。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-lane",
      "coord": [1, 3, 0],
      "labels": ["jianghu", "sect-rumor"],
      "exits": [
        { "direction": "west", "to": 16408 },
        { "direction": "south", "to": 16406 }
      ],
      "enquires": ["門派", "傳聞", "街口"]
    },
    {
      "vnum": 16410,
      "name": "東市轉角",
      "description": "再往東去，街面的氣味和聲量都開始更偏向商販、外客與地方消息的聚散點，像會稽把更多對外往來和更細碎的江湖耳語都收在那個方向。這裡既是城內轉角，也是許多支線準備展開的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "east-turn",
      "coord": [0, 4, 0],
      "labels": ["east-link", "market-turn"],
      "exits": [
        { "direction": "north", "to": 16408 },
        { "direction": "east", "to": 16601, "external": true }
      ],
      "enquires": ["東市", "外客", "去路"]
    }
  ]
}
```
