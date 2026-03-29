# 宛 (`city_wan`)

## Area Intent

`city_wan` 承接 `city_xinye` 北門路口外那條內陸宛道，把原本仍停在「往宛」路牌語意上的去路，正式展開成一座有南門、主街、榜牌、驛舍與北門官道口的歷史城市。這裡不是另一個像新野那樣靠熟人與邊鎮口氣撐起來的小城，而是一個會讓人從城門尺度、驛傳節奏與行人秩序裡感到「南北交通正在這裡被重新收束整理」的城市 hub。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `南北轉接城`
- LevelRange: `14-24`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_wan",
    "title": "宛",
    "design_notes": "第一版 spec-first 草案。先固定南門驛口、入城長街、南市棚廊、宛城十字、驛舍前街、郡府榜廊、北門官道口與西城牌樓，把新野北向去路正式落成為可載入的宛城骨架。",
    "level_range": "14-24",
    "planned_vnum_range": "20401-20420",
    "reserved_room_block": "20401-20420",
    "theme": {
      "primary": "歷史城市",
      "secondary": "南北轉接城"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 20401,
        "target_area": "city_xinye",
        "target_room_vnum": 20207,
        "label": "新野北門路口"
      },
      {
        "direction": "north",
        "source_vnum": 20407,
        "target_area": "road_wan",
        "target_room_vnum": 20508,
        "label": "往宛官道"
      },
      {
        "direction": "out",
        "source_vnum": 20408,
        "target_area": "wild_wan_outer",
        "label": "宛城外道"
      }
    ],
    "clusters": [
      { "id": "south-gate", "label": "南門與入城口" },
      { "id": "main-street", "label": "主街與十字" },
      { "id": "service-quarter", "label": "市集與驛舍" },
      { "id": "north-west-edge", "label": "北門與西城外口" }
    ]
  },
  "rooms": [
    {
      "vnum": 20401,
      "name": "南門驛口",
      "description": "自新野北門一路上來後，最先撞進視線的是宛城南門外這段帶著驛馬氣味的入城口。門道比邊鎮收得更整，行人、差役與換馬客也更懂得沿線讓路，讓人一踏進來就能感到這裡確實是一座把南北流動重新整理起來的城。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-link", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 20207, "external": true },
        { "direction": "north", "to": 20402 }
      ],
      "enquires": ["新野", "南門", "來路"]
    },
    {
      "vnum": 20402,
      "name": "入城長街",
      "description": "長街沿著城門內線筆直展開，兩側鋪子與行人留出的距離比新野更有秩序，卻還保留著足夠的煙火氣。這裡不像州府那樣壓得人喘不過氣，卻已經很清楚地讓你知道：宛是拿來轉路、補給與打聽正經消息的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 1, 0],
      "labels": ["approach", "city-order", "orientation"],
      "exits": [
        { "direction": "south", "to": 20401 },
        { "direction": "north", "to": 20404 },
        { "direction": "west", "to": 20403 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "木牌沿著長街把市集、驛舍與北門方向寫得一清二楚，像是替一路北上的旅人省下不少多問的力氣。"
        }
      ],
      "enquires": ["市集", "驛舍", "北門"]
    },
    {
      "vnum": 20403,
      "name": "南市棚廊",
      "description": "棚廊下堆著乾糧、酒囊、燈盞與各種趕路人真正會需要的雜物，叫賣聲和討價聲在木樑間來回撞著。比起新野的熟客式熱鬧，宛的市集更像一條專門替旅人整理行囊與下一段去向的補給帶。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [-1, 1, 0],
      "labels": ["market", "supply", "restock"],
      "exits": [
        { "direction": "east", "to": 20402 },
        { "direction": "north", "to": 20405 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "棚廊木樑上掛著幾塊寫得利落的招牌，內容不花哨，只求讓外地人一眼就知道哪裡能補糧、補水與補燈。"
        }
      ],
      "enquires": ["掌櫃", "乾糧", "燈盞"]
    },
    {
      "vnum": 20404,
      "name": "宛城十字",
      "description": "十字街口把宛城的用途分得十分明白，南面收著來自新野的路氣，北面是官道出城，西邊走向驛舍與外城牌樓，東側則是榜牌與郡府消息聚集的地方。站在這裡時，整座城最重要的秩序不是威嚇，而是把去路講清楚。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 2, 0],
      "labels": ["junction", "hub", "city-core"],
      "exits": [
        { "direction": "south", "to": 20402 },
        { "direction": "north", "to": 20407 },
        { "direction": "west", "to": 20405 },
        { "direction": "east", "to": 20406 }
      ],
      "enquires": ["去路", "官道", "城中"]
    },
    {
      "vnum": 20405,
      "name": "驛舍前街",
      "description": "前街靠著驛舍外牆展開，換馬聲、腳步聲與傳信人的低語讓這裡始終有一種不算吵卻很忙的節奏。宛城真正的氣口之一就在這裡，很多消息不是在官面公告上先出現，而是先從這段前街被人帶走。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [-1, 2, 0],
      "labels": ["posthouse", "travel", "information-flow"],
      "exits": [
        { "direction": "south", "to": 20403 },
        { "direction": "east", "to": 20404 },
        { "direction": "west", "to": 20408 }
      ],
      "enquires": ["驛舍", "送信", "換馬"]
    },
    {
      "vnum": 20406,
      "name": "郡府榜廊",
      "description": "榜廊下貼著官告、行旅規條與地方通報，紙張新舊交錯，看得出這裡平常就有很多人停下來核對路況與城中風聲。比起新野那種民間補寫很多的榜牆，宛的榜牌更像城內秩序正經運作的表面。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, 2, 0],
      "labels": ["notice", "official", "clerk-space"],
      "exits": [
        { "direction": "west", "to": 20404 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜牌上的告示寫得工整而直接，從官道盤查到驛傳交遞都列得清楚，像是在提醒人這座城靠的是把流程講明白。"
        }
      ],
      "enquires": ["官府", "榜牌", "差役"]
    },
    {
      "vnum": 20407,
      "name": "北門官道口",
      "description": "北門外的官道口比南門更開闊，備馬樁、里程石與守卒站位都透露出這裡才是宛真正朝向中原主線的出口。如今順著這裡北上，已能正式踏上往洛陽去的官道，讓人更明白宛不是終點，而是把南來的路重新接回更長官道的北向節點。",
      "sector_type": "SECT_CITY",
      "cluster": "north-west-edge",
      "coord": [0, 3, 0],
      "labels": ["north-edge", "world-link-north", "road-gate"],
      "exits": [
        { "direction": "south", "to": 20404 },
        { "direction": "north", "to": 20508, "external": true }
      ],
      "enquires": ["官道", "洛陽", "北門"]
    },
    {
      "vnum": 20408,
      "name": "西城牌樓",
      "description": "西側牌樓把城內石地慢慢放鬆回帶土氣的外街，牆影後方已經能感到城外官道與郊邊茶棚的風氣。這裡不像真正離城那樣空曠，卻很明顯是宛把旅人再一次交還給外圍世界的出口前帶。",
      "sector_type": "SECT_CITY",
      "cluster": "north-west-edge",
      "coord": [-2, 2, 0],
      "labels": ["west-edge", "future-link", "outer-gate"],
      "exits": [
        { "direction": "east", "to": 20405 }
      ],
      "enquires": ["外城", "茶棚", "出城"]
    }
  ]
}
```
