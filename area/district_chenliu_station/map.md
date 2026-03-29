# 陳留驛站 (`district_chenliu_station`)

## Area Intent

`district_chenliu_station` 承接 `city_chenliu` 的南驛前院，把原本只停在站牌、車次與下一站語意上的南向轉接帶，正式展成車馬棚、旅票櫃、行李長棚、旅舍前廊與小販棚口交錯的人流分區。這裡不是另一段主街，也不是抽象補給點，而是一段會讓玩家清楚感到「陳留真正把旅人交給下一段路的地方，其實都在這些驛棚、帳簿和站尾街聲裡」的城市 district。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `驛站 / 補給`
- LevelRange: `15-25`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "district_chenliu_station",
    "title": "陳留驛站",
    "design_notes": "第一版 spec-first 草案。先固定南驛街口、車馬棚道、旅票棚前、驛丞櫃口、行李長棚、旅舍前廊、小販棚口與南站尾街，讓陳留南向驛站分區正式成為可載入的 district 骨架。",
    "level_range": "15-25",
    "planned_vnum_range": "20701-20720",
    "reserved_room_block": "20701-20720",
    "theme": {
      "primary": "歷史城市",
      "secondary": "驛站 / 補給"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 20701,
        "target_area": "city_chenliu",
        "target_room_vnum": 13816,
        "label": "陳留驛站前院"
      }
    ],
    "clusters": [
      { "id": "entry-lane", "label": "南驛入口" },
      { "id": "traffic-core", "label": "車馬與票櫃" },
      { "id": "service-row", "label": "行李與旅舍" },
      { "id": "side-stalls", "label": "棚口與站尾" }
    ]
  },
  "rooms": [
    {
      "vnum": 20701,
      "name": "南驛街口",
      "description": "一離開陳留驛站前院，街面上的節奏便不再只是問時辰，而是直接化成牽馬、抬箱、催車與四處打聽下一站的忙亂。這裡仍屬於陳留城內，卻已經是旅人真正開始被交給驛站系統與長路規矩的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "entry-lane",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link", "travel-threshold"],
      "exits": [
        { "direction": "north", "to": 13816, "external": true },
        { "direction": "east", "to": 20702 },
        { "direction": "south", "to": 20703 }
      ],
      "enquires": ["驛站", "回城", "去路"]
    },
    {
      "vnum": 20702,
      "name": "車馬棚道",
      "description": "棚道邊繫著幾匹正換韁整鞍的驛馬，車輪、草料與木樁把整條路挤得滿滿的。這裡真正重要的不是體面，而是任何要上路的人都得在這裡先被整理進某種可運作的次序。",
      "sector_type": "SECT_CITY",
      "cluster": "traffic-core",
      "coord": [1, 0, 0],
      "labels": ["horses", "traffic", "waypoint"],
      "exits": [
        { "direction": "west", "to": 20701 },
        { "direction": "south", "to": 20705 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "幾根磨得發亮的木樁沿棚道排開，繩痕深得一看就知道陳留往南的旅運從來沒有真正停過。"
        }
      ],
      "enquires": ["車馬", "驛馬", "木樁"]
    },
    {
      "vnum": 20703,
      "name": "旅票棚前",
      "description": "棚前擠著等時辰、等座位，也等人順手替自己把消息一起帶出去的旅人。很多人嘴上問的是票、問的是車，真正想確認的卻往往是哪條路最近還算太平。",
      "sector_type": "SECT_CITY",
      "cluster": "traffic-core",
      "coord": [0, -1, 0],
      "labels": ["tickets", "queue", "rumor"],
      "exits": [
        { "direction": "north", "to": 20701 },
        { "direction": "east", "to": 20705 },
        { "direction": "south", "to": 20706 },
        { "direction": "enter", "to": 20704 }
      ],
      "enquires": ["票", "時辰", "南路"]
    },
    {
      "vnum": 20704,
      "name": "驛丞櫃口",
      "description": "櫃口後方堆著竹簡、行程簿與木牌，桌面被翻得很勤，像每一筆紀錄都在替陳留和更遠的地方維持某種看不見卻不能亂掉的節奏。能不能順利上路，很多時候就在這方櫃口前被決定。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "traffic-core",
      "coord": [0, -1, 1],
      "labels": ["inside", "clerk", "records"],
      "exits": [
        { "direction": "out", "to": 20703 }
      ],
      "enquires": ["驛丞", "櫃口", "路引"]
    },
    {
      "vnum": 20705,
      "name": "行李長棚",
      "description": "長棚下堆著包袱、木箱、草索與寫著人名地點的短牌，讓整片空間像被各種尚未上路、卻已經半只腳踩進遠行的人生暫時借住。這裡不是城市最顯眼的地方，卻很像一座樞紐真正的內臟。 ",
      "sector_type": "SECT_CITY",
      "cluster": "service-row",
      "coord": [1, -1, 0],
      "labels": ["luggage", "storage", "travel-service"],
      "exits": [
        { "direction": "north", "to": 20702 },
        { "direction": "west", "to": 20703 },
        { "direction": "east", "to": 20707 }
      ],
      "enquires": ["行李", "木箱", "寄放"]
    },
    {
      "vnum": 20706,
      "name": "旅舍前廊",
      "description": "前廊掛著幾盞並不講究卻足夠暖人的燈，總有人在這裡灌下一口熱湯、問一聲價錢，或是先讓緊繃的腳步慢半拍再決定要不要繼續趕路。驛站分區若真有一點人情味，通常都藏在這種地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "service-row",
      "coord": [0, -2, 0],
      "labels": ["inn", "rest", "warmth"],
      "exits": [
        { "direction": "north", "to": 20703 },
        { "direction": "east", "to": 20708 }
      ],
      "enquires": ["旅舍", "熱湯", "歇腳"]
    },
    {
      "vnum": 20707,
      "name": "小販棚口",
      "description": "棚口只擺了幾樣最趕路的人一定會買的東西，乾糧、燈油、水囊，外加一些總被順手問起的小道消息。它的存在像在提醒人，真正懂旅路的人，賣的從來不只是一口吃食。 ",
      "sector_type": "SECT_CITY",
      "cluster": "side-stalls",
      "coord": [2, -1, 0],
      "labels": ["stall", "small-goods", "gossip"],
      "exits": [
        { "direction": "west", "to": 20705 },
        { "direction": "south", "to": 20708 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "木招牌上只寫著幾個大字：乾糧、熱水、夜燈，像是在說真正趕路的人其實要不了太多花樣。"
        }
      ],
      "enquires": ["乾糧", "夜燈", "小販"]
    },
    {
      "vnum": 20708,
      "name": "南站尾街",
      "description": "走到站尾後，人聲雖然還在，卻已經被拉成較長、較鬆，也更接近真正離城前的尾音。這裡不像終點，反而像陳留把旅人交給更南方路網之前，最後一段還帶著城內秩序的緩衝帶。 ",
      "sector_type": "SECT_CITY",
      "cluster": "side-stalls",
      "coord": [1, -2, 0],
      "labels": ["tail", "future-link", "departure"],
      "exits": [
        { "direction": "north", "to": 20707 },
        { "direction": "west", "to": 20706 }
      ],
      "enquires": ["站尾", "南邊", "下一站"]
    }
  ]
}
```
