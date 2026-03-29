# 成都學舍 (`district_chengdu_scholar`)

## Area Intent

`district_chengdu_scholar` 承接 `city_chengdu` 的學舍外街，把都城裡原本只被嗅到、尚未真正踏進去的紙墨與議論聲，正式展成有書坊、講席、碑廊、靜院與榜帖角的文士腹地。這裡不只是安靜一點的街區，而是一段會讓玩家清楚感到成都除了市井與官府，也有一整套靠知識、問學與議論撐起來的都城節奏。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `文士 / 書院`
- LevelRange: `36-48`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "district_chengdu_scholar",
    "title": "成都學舍",
    "design_notes": "第一版 spec-first 草案。先固定書院街口、書坊長街、講席中庭、碑廊轉角、靜讀側院、榜帖角、抄書小巷與北院牌門，讓成都文士腹地正式成為可載入的 district 骨架。",
    "level_range": "36-48",
    "planned_vnum_range": "20001-20020",
    "reserved_room_block": "20001-20020",
    "theme": {
      "primary": "歷史城市",
      "secondary": "文士 / 書院"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 20001,
        "target_area": "city_chengdu",
        "target_room_vnum": 19706,
        "label": "學舍外街"
      }
    ],
    "clusters": [
      { "id": "entry-lane", "label": "書院入口帶" },
      { "id": "book-street", "label": "書坊與講席" },
      { "id": "quiet-courts", "label": "靜院與抄書巷" },
      { "id": "notice-corner", "label": "碑廊與榜帖角" },
      { "id": "north-yard", "label": "北院尾帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 20001,
      "name": "書院街口",
      "description": "從學舍外街再往北踏進來時，城心的喧聲很快就被壓成較遠的背景，只剩紙墨、木簡與低聲問答把空氣撐得清亮。這裡仍然屬於成都，卻像都城把最浮動的人潮先留在外面，再把願意慢下來的人收進更講秩序的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "entry-lane",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-link", "scholar-threshold"],
      "exits": [
        { "direction": "south", "to": 19706, "external": true },
        { "direction": "north", "to": 20002 },
        { "direction": "east", "to": 20003 }
      ],
      "enquires": ["學舍", "書院", "講席"]
    },
    {
      "vnum": 20002,
      "name": "書坊長街",
      "description": "長街兩側不是米袋與布幌，而是書箱、筆架與一塊塊寫得端正的木牌，讓腳步也自然跟著輕了幾分。成都真正的厚度不只在官署與商街，也在這種不靠喊價、卻一樣讓消息流得很快的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "book-street",
      "coord": [0, 1, 0],
      "labels": ["book-row", "quiet-busy", "core"],
      "exits": [
        { "direction": "south", "to": 20001 },
        { "direction": "north", "to": 20004 },
        { "direction": "east", "to": 20005 }
      ],
      "keywords": [
        {
          "keyword": "書牌",
          "description": "一排排書牌字體端正，標著抄本、筆札與講義所在，像連做買賣這件事都得先講求章法。"
        }
      ],
      "enquires": ["書坊", "抄本", "講義"]
    },
    {
      "vnum": 20003,
      "name": "碑廊轉角",
      "description": "石碑與木廊在這裡轉出一個安靜的角度，往來學子總會順手停下來看上兩眼。它不像榜文長廊那樣偏官府氣，卻同樣讓人意識到成都的消息與學問常常寫在牆上、留在路口，也留在每一次側眼經過之間。",
      "sector_type": "SECT_CITY",
      "cluster": "notice-corner",
      "coord": [1, 0, 0],
      "labels": ["inscriptions", "corner", "reading-stop"],
      "exits": [
        { "direction": "west", "to": 20001 },
        { "direction": "north", "to": 20005 },
        { "direction": "east", "to": 20006 }
      ],
      "keywords": [
        {
          "keyword": "石碑",
          "description": "碑面刻著舊文、講題與名家題字，邊角雖有磨痕，卻反而讓人覺得這裡的字是真的被一代代人看過。"
        }
      ],
      "enquires": ["石碑", "題字", "舊文"]
    },
    {
      "vnum": 20004,
      "name": "講席中庭",
      "description": "中庭鋪得平正，席位與木案也排得乾淨，像只要再多幾個人坐下來，就能立刻把一場講論撐起來。比起市井那種熱鬧，這裡更像另一種收束得很好的力量，靠著辯論、記誦與提問把都城撐得更穩。",
      "sector_type": "SECT_CITY",
      "cluster": "book-street",
      "coord": [0, 2, 0],
      "labels": ["lecture-court", "gathering", "scholar-core"],
      "exits": [
        { "direction": "south", "to": 20002 },
        { "direction": "east", "to": 20007 }
      ],
      "enquires": ["講席", "先生", "學問"]
    },
    {
      "vnum": 20005,
      "name": "榜帖角",
      "description": "牆邊貼著的榜帖不像官府那樣處處帶命令口氣，而更像把徵文、會講、徵抄與問學消息悄悄傳給會來看的人。這裡讓人明白，成都的消息不只靠差役傳，也靠讀書人彼此之間的留字與流轉。",
      "sector_type": "SECT_CITY",
      "cluster": "notice-corner",
      "coord": [1, 1, 0],
      "labels": ["notices", "quest-hook", "local-news"],
      "exits": [
        { "direction": "south", "to": 20003 },
        { "direction": "west", "to": 20002 },
        { "direction": "north", "to": 20007 }
      ],
      "keywords": [
        {
          "keyword": "榜帖",
          "description": "榜帖有新有舊，有些正經得像官文，有些卻只是幾行留字，偏偏最容易讓有心人停下來讀。"
        }
      ],
      "enquires": ["榜帖", "徵文", "問學"]
    },
    {
      "vnum": 20006,
      "name": "靜讀側院",
      "description": "側院裡連風聲都像放低了幾分，只有偶爾翻頁或落筆的細響，讓人很難不跟著收斂動作。這裡不是無事可做，而是所有事情都必須慢下來，才能真正讀得進去。",
      "sector_type": "SECT_CITY",
      "cluster": "quiet-courts",
      "coord": [2, 0, 0],
      "labels": ["quiet-yard", "study", "calm"],
      "exits": [
        { "direction": "west", "to": 20003 },
        { "direction": "north", "to": 20008 }
      ],
      "enquires": ["靜院", "讀書", "抄寫"]
    },
    {
      "vnum": 20007,
      "name": "抄書小巷",
      "description": "小巷不寬，牆邊卻擺滿了晾紙、竹簡與半乾的墨字，像知識在這裡不是只被講述，也被一筆筆地重新抄寫與整理。比起主街顯眼的書坊，這裡更像真正把學舍日常默默運轉起來的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "quiet-courts",
      "coord": [1, 2, 0],
      "labels": ["copy-lane", "paper", "work"],
      "exits": [
        { "direction": "south", "to": 20005 },
        { "direction": "west", "to": 20004 },
        { "direction": "east", "to": 20008 }
      ],
      "enquires": ["抄書", "紙墨", "筆札"]
    },
    {
      "vnum": 20008,
      "name": "北院牌門",
      "description": "走到北院牌門時，成都的喧聲已經遠得像另一層世界，只留下更深、更靜的書院秩序在前頭延伸。這裡不像真正的終點，反而像在提醒人，眼前這一段仍只是成都問學腹地的第一層外圈。",
      "sector_type": "SECT_CITY",
      "cluster": "north-yard",
      "coord": [2, 1, 0],
      "labels": ["north-tail", "future-depth", "academy-gate"],
      "exits": [
        { "direction": "south", "to": 20006 },
        { "direction": "west", "to": 20007 }
      ],
      "enquires": ["北院", "內舍", "深處"]
    }
  ]
}
```
