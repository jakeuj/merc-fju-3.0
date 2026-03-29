# 洛陽東市 (`district_loyang_east_market`)

## Area Intent

`district_loyang_east_market` 承接 `loyang` 的商街前帶，把帝都主幹道旁原本只是經過、卻還沒真正走進去的東側市場腹地，正式展開成一段有商行主街、票據棚、馬販角、茶湯攤與差役榜口的城市 district。這裡不是單純把幾間店房搬出來，而是要讓玩家一進來就明白：洛陽真正能替新手和旅人撐起裝備、採買、問路與傳聞交換的地方，其實就在這股被招牌、人流與叫賣聲撐滿的市氣裡。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `市集 / 商業`
- LevelRange: `1-10`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "district_loyang_east_market",
    "title": "洛陽東市",
    "design_notes": "第一版 spec-first 草案。先固定商街前帶入口、東市主街、票據棚、馬販角、茶湯攤、布棚巷、差役榜口與東市尾棚，讓洛陽東側商業 district 正式成為可載入骨架。",
    "level_range": "1-10",
    "planned_vnum_range": "21001-21020",
    "reserved_room_block": "21001-21020",
    "theme": {
      "primary": "歷史城市",
      "secondary": "市集 / 商業"
    },
    "world_links": [
      {
        "direction": "out",
        "source_vnum": 21001,
        "target_area": "loyang",
        "target_room_vnum": 553,
        "label": "商街前帶"
      }
    ],
    "clusters": [
      { "id": "entry-street", "label": "入口街口" },
      { "id": "market-core", "label": "商街主帶" },
      { "id": "service-nodes", "label": "票據與馬販" },
      { "id": "stalls", "label": "茶湯與布棚" },
      { "id": "tail-lane", "label": "榜口與市尾" }
    ]
  },
  "rooms": [
    {
      "vnum": 21001,
      "name": "東市街口",
      "description": "一從洛陽城內商街轉進來，原本只是路過耳邊的叫賣聲就立刻變成迎面撲來的人潮、貨擔與招牌。這裡離帝都主街並不遠，卻已經是另一種節奏更密、眼神更快、每個人都像正在盤算著要買什麼或問什麼的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "entry-street",
      "coord": [0, 0, 0],
      "labels": ["entry", "market-threshold", "city-link"],
      "exits": [
        { "direction": "out", "to": 553, "external": true },
        { "direction": "east", "to": 21002 },
        { "direction": "south", "to": 21003 }
      ],
      "enquires": ["東市", "街口", "商街"]
    },
    {
      "vnum": 21002,
      "name": "東市主街",
      "description": "主街被成排伸出的木招、布幌與棚影切得層層疊疊，行人和買賣聲則把整條街擠成一股穩定向前的熱氣。洛陽的富裕感在這裡不需要官府證明，光是看貨色、看人潮，就知道這是帝都真正養活日常的一條商脈。",
      "sector_type": "SECT_CITY",
      "cluster": "market-core",
      "coord": [1, 0, 0],
      "labels": ["main-street", "busy", "trade-core"],
      "exits": [
        { "direction": "west", "to": 21001 },
        { "direction": "east", "to": 21004 },
        { "direction": "south", "to": 21005 }
      ],
      "keywords": [
        {
          "keyword": "木招",
          "description": "幾塊寫著糧、布、馬具與雜貨的木招一塊壓著一塊往外伸，像恨不得先把買客的目光搶過來再說。"
        }
      ],
      "enquires": ["店家", "招牌", "採買"]
    },
    {
      "vnum": 21003,
      "name": "票據棚前",
      "description": "幾張長案、帳冊與說話急促的人把這一角撐得比別處更像一種忙碌的秩序。有人在此兌銀、有人記帳、有人只是湊近了聽聽最近哪裡又傳出新價與新事，讓這裡成了東市最會把消息和買賣綁在一起的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "service-nodes",
      "coord": [0, -1, 0],
      "labels": ["finance", "paperwork", "news"],
      "exits": [
        { "direction": "north", "to": 21001 },
        { "direction": "east", "to": 21005 },
        { "direction": "south", "to": 21006 }
      ],
      "enquires": ["票據", "帳冊", "兌銀"]
    },
    {
      "vnum": 21004,
      "name": "馬販角",
      "description": "繩索、草料與鞍具味把這一角和一般商街明顯分開，連人們站的位置都像習慣留出給牲口轉身的空間。對真正要上路的人來說，這裡不只是買賣，更像決定你接下來走得快不快、遠不遠的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "service-nodes",
      "coord": [2, 0, 0],
      "labels": ["mounts", "travel-service", "gear"],
      "exits": [
        { "direction": "west", "to": 21002 },
        { "direction": "south", "to": 21007 }
      ],
      "enquires": ["馬匹", "鞍具", "趕路"]
    },
    {
      "vnum": 21005,
      "name": "茶湯攤",
      "description": "熱湯和蒸氣把這段街角養成一種專收留腳步的地方，無論是採買回來的人、剛換好票據的人，還是準備去看馬的旅客，都會在這裡先停下一口氣。也正因如此，東市最好打聽的消息往往不在榜上，而在湯氣上頭。 ",
      "sector_type": "SECT_CITY",
      "cluster": "stalls",
      "coord": [1, -1, 0],
      "labels": ["food", "rumor", "rest"],
      "exits": [
        { "direction": "north", "to": 21002 },
        { "direction": "west", "to": 21003 },
        { "direction": "east", "to": 21007 }
      ],
      "keywords": [
        {
          "keyword": "茶湯",
          "description": "一鍋鍋熱氣在攤前連成不斷的白霧，讓東市這一角總像同時有飯香和閒話在往外冒。"
        }
      ],
      "enquires": ["茶湯", "歇腳", "傳聞"]
    },
    {
      "vnum": 21006,
      "name": "布棚巷",
      "description": "色布從棚沿一路垂到行人肩頭，巷子因此比主街更亮、更近，也更有一種能把人腳步慢下來的柔韌感。這裡不像主街那樣吵，卻更能看出東市究竟是靠多少熟手眼光與細碎交易撐起來的。",
      "sector_type": "SECT_CITY",
      "cluster": "stalls",
      "coord": [0, -2, 0],
      "labels": ["cloth", "side-lane", "slower-pace"],
      "exits": [
        { "direction": "north", "to": 21003 },
        { "direction": "east", "to": 21008 }
      ],
      "enquires": ["布棚", "裁衣", "細貨"]
    },
    {
      "vnum": 21007,
      "name": "差役榜口",
      "description": "幾張新貼的榜示和幾個故意沒寫太明白的名字被釘在牆上，旁邊總有人駐足，也總有人裝作只是順路看一眼。比起官府門前那種正經威嚴，這裡更像東市真正把消息散進人群的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "tail-lane",
      "coord": [2, -1, 0],
      "labels": ["notice", "bailiff", "quest-hook"],
      "exits": [
        { "direction": "north", "to": 21004 },
        { "direction": "west", "to": 21005 },
        { "direction": "south", "to": 21008 }
      ],
      "keywords": [
        {
          "keyword": "榜示",
          "description": "榜紙上有招工、有尋物、有催討，也有一些看著就像會把膽子大的人引去偏門巷角的模糊委託。"
        }
      ],
      "enquires": ["榜示", "差役", "委託"]
    },
    {
      "vnum": 21008,
      "name": "東市尾棚",
      "description": "走到市尾後，人聲終於鬆開一點，卻沒有真正散掉，反而像被更深的巷路慢慢吸走。這裡讓人知道眼前的東市還只是第一層，真正屬於洛陽腹地的細密生活，仍能在棚後和巷尾再往裡展開。",
      "sector_type": "SECT_CITY",
      "cluster": "tail-lane",
      "coord": [1, -2, 0],
      "labels": ["tail", "future-depth", "district-fringe"],
      "exits": [
        { "direction": "north", "to": 21007 },
        { "direction": "west", "to": 21006 }
      ],
      "enquires": ["市尾", "巷尾", "更裡頭"]
    }
  ]
}
```
