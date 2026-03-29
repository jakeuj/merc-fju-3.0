# 夷陵 (`fort_yiling`)

## Area Intent

`fort_yiling` 承接 `city_jiangling` 西關路口，把原本還停在路標、木柵與遠路想像裡的蜀荊咽喉，正式落成一座真正會把人流收束、盤查與再分流的軍事關隘。這裡不是江陵那種能讓旅人鬆口氣的補給城，而是一個一踏進去就會明顯感到自己正站在軍令、關防與遠征壓力之中的地方。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `咽喉 / 關道`
- LevelRange: `42-56`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_yiling",
    "title": "夷陵",
    "design_notes": "第一版 spec-first 草案。先固定江陵西關外的關前路口、關前柵道、夷陵關門、甕城主道、軍需棚與軍令望樓，讓蜀荊關道上的主線 fort 正式落地。",
    "level_range": "42-56",
    "planned_vnum_range": "19401-19420",
    "reserved_room_block": "19401-19420",
    "theme": {
      "primary": "軍旅",
      "secondary": "咽喉 / 關道"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 19401,
        "target_area": "city_jiangling",
        "target_room_vnum": 19308,
        "label": "江陵西關"
      },
      {
        "direction": "west",
        "source_vnum": 19408,
        "target_area": "fort_yongan",
        "label": "西進關道"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "關前入口帶" },
      { "id": "gate", "label": "關門與甕城" },
      { "id": "camp", "label": "軍需與斥候帶" },
      { "id": "watch", "label": "望樓與西向關坪" }
    ]
  },
  "rooms": [
    {
      "vnum": 19401,
      "name": "東關路口",
      "description": "自江陵西關一路走到這裡後，木柵、軍旗與關牆影子會立刻把街路的煙火氣壓下去。東關路口像是一道把城市秩序收成軍事秩序的門檻，讓人明白再往前每一步都不只是旅行，而是進入有人盤查、也有人決定你該往哪裡去的地帶。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 19308, "external": true },
        { "direction": "west", "to": 19402 }
      ],
      "enquires": ["江陵", "西關", "關道"]
    },
    {
      "vnum": 19402,
      "name": "關前柵道",
      "description": "柵道把來者的步伐自然壓慢，兩側木柵和巡視視線一起把人流擠成一條不容亂走的線。這裡不像真正戰地那樣混亂，卻比江陵任何一條街更讓人清楚感覺到自己已站在關隘的脈搏上。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [-1, 0, 0],
      "labels": ["approach", "checkpoint"],
      "exits": [
        { "direction": "east", "to": 19401 },
        { "direction": "west", "to": 19403 },
        { "direction": "south", "to": 19405 }
      ],
      "enquires": ["柵道", "盤查", "守兵"]
    },
    {
      "vnum": 19403,
      "name": "夷陵關門",
      "description": "厚實關門把內外空氣切得很乾淨，門外是仍可回頭的城市邊界，門內則是更偏軍務、命令與備戰的空間。站在這裡時，會很清楚感到夷陵不是給人停留發呆的地方，而是一座只問你是否該被放進去的咽喉。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [-2, 0, 0],
      "labels": ["gate", "threshold"],
      "exits": [
        { "direction": "east", "to": 19402 },
        { "direction": "west", "to": 19404 }
      ],
      "enquires": ["關門", "放行", "軍令"]
    },
    {
      "vnum": 19404,
      "name": "甕城主道",
      "description": "甕城把關防的壓力再收得更緊，短短一段主道上卻同時能看見軍需、傳令與望樓的節奏。比起單純防禦，它更像一個把所有西進與東回動線先壓縮、再重新分配的軍事節點。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [-3, 0, 0],
      "labels": ["core", "military-flow"],
      "exits": [
        { "direction": "east", "to": 19403 },
        { "direction": "west", "to": 19408 },
        { "direction": "south", "to": 19406 },
        { "direction": "up", "to": 19407 }
      ],
      "enquires": ["甕城", "內營", "望樓"]
    },
    {
      "vnum": 19405,
      "name": "斥候側棚",
      "description": "側棚裡堆著地圖木板、備用水囊與剛交回來的塵土披風，看得出這裡真正面對的是路況、敵情與關外風吹草動。它不像主道那麼緊繃，卻反而讓人更直接感受到夷陵的關隘價值來自看得遠、回得快。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-1, -1, 0],
      "labels": ["scout", "side-shelter"],
      "exits": [
        { "direction": "north", "to": 19402 }
      ],
      "enquires": ["斥候", "敵情", "地圖"]
    },
    {
      "vnum": 19406,
      "name": "軍需棚區",
      "description": "糧包、燈油、皮囊與兵械在棚下分得清清楚楚，連空氣都帶著一種只屬於行軍前線的乾燥秩序。對夷陵來說，真正撐住整座關隘節奏的，往往不是牆，而是這些看似不起眼卻不能斷的備給。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-3, -1, 0],
      "labels": ["supply", "service"],
      "exits": [
        { "direction": "north", "to": 19404 }
      ],
      "enquires": ["軍需", "糧草", "燈油"]
    },
    {
      "vnum": 19407,
      "name": "軍令望樓",
      "description": "望樓上不只看得見關前來路，也能把甕城內外的節奏一口氣收進眼底。木案上的軍令與更換班次的記號讓這裡顯得比下方任何地方都更冷，也更像真正決定關隘心跳速度的高點。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [-3, 0, 1],
      "labels": ["watchtower", "orders", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 19404 }
      ],
      "enquires": ["望樓", "軍令", "旗號"]
    },
    {
      "vnum": 19408,
      "name": "西向關坪",
      "description": "再往西去，地勢與風向都開始帶出更長、更硬的遠路感，連關坪上的馬樁與路牌都像是在提醒人這不是回城用的出口，而是通往下一段更深軍旅主線的前口。夷陵在這裡不只是關門，也是西進節奏真正被重新點燃的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [-4, 0, 0],
      "labels": ["west-edge", "future-link", "forward"],
      "exits": [
        { "direction": "east", "to": 19404 }
      ],
      "enquires": ["西邊", "永安", "遠路"]
    }
  ]
}
```
