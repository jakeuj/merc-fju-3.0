# 襄陽城 (`city_xiangyang`)

## Area Intent

`city_xiangyang` 承接 `fort_hulao` 之後的主線節奏，讓玩家從軍事門戶重新走回一座真正活著的城市。這裡不只要能補給，還要讓人從城門盤查、市集招牌、官府榜文與東側碼頭感受到「荊州門戶」的地方厚度。

第一版目標先固定：

- 一條由南城門進城並穿過主街十字的城市主線
- 一條向西展開的市集 / 客棧補給線
- 一條向東通往官府與碼頭的地方治理 / 水路支線
- 以 `#Enquire` / `#Keyword` 暗示城門、市集、官府與江路去向

這一版刻意讓玩家感受到：

- 襄陽不是純粹戰鬥場，而是軍旅與民生交會的主城
- 主線進到荊州後，交通不再只靠官道，也開始帶出水路與碼頭
- 城市資訊密度、補給便利與地方勢力流動，都是玩法的一部分

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `荊州門戶 / 軍旅樞紐`
- LevelRange: `35-45`
- Parent region: `荊州`
- World gap filled: 讓主世界 progression 在軍事關卡之後重新落回主城 hub，並替江夏方向的水路外野鋪路

## Player Flow

1. 玩家由南城門入城，先從盤查與榜文感受到門戶城市的秩序。
2. 主街十字把補給、市集、官府與碼頭分成一眼可懂的城市 loop。
3. 西側市集與客棧提供明確的主城補給節奏。
4. 東側官署與碼頭讓人意識到襄陽不只是內陸城，也是一座接水路、接軍務的樞紐。
5. 出城方向則自然預告樊城 / 新野與江夏水路的下一階段世界。

## Cluster Notes

### `south-gate`

- 房間重點：南城門、盤查棚、入城榜文
- 玩家感受：這裡是門戶，而不是可任意穿越的小城
- 對外角色：作為未來接 `jingxiang_road` 的城門入口

### `main-avenue`

- 房間重點：主街、十字口、往來行旅
- 玩家感受：一進城就能讀懂主要服務與去路
- 對外角色：作為全區節奏與問路骨幹

### `market-quarter`

- 房間重點：市集、客棧、商舖與錢莊
- 玩家感受：煙火氣、補給便利、商旅流動
- 對外角色：提供未來 runtime 服務 NPC 與補給 loop 空間

### `yamen-quarter`

- 房間重點：官府、榜文、差役廊
- 玩家感受：地方治理與軍旅消息在同一座城裡流動
- 對外角色：提供任務、問路與地方情報節點

### `east-wharf`

- 房間重點：東碼頭、江風木棧、渡口路牌
- 玩家感受：襄陽開始把主線從陸路轉向水路
- 對外角色：作為未來接 `wild_jiangxia_river` 的主城前帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `south` from `14201`: planned link to `jingxiang_road`
- `north` from `14208`: runtime link to `fort_fancheng`
- `east` from `14212`: planned link to `wild_jiangxia_river`
- `west` from `14209`: planned link to `city_xinye`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `城門 / 市集 / 官府 / 碼頭 / 去路`
- `#Keyword` 第一版會落在 `告示 / 招牌 / 路牌 / 城門 / 旗幟`
- `#Job` 第一版暫不新增；等真正要做跑腿、差役或渡口消息 loop 再補 job 與 runtime flow

## Suggested Layout

```text
荊襄大道方向
   |
[14201] 南城門 -- [14202] 盤查棚前 -- [14203] 入城主街 -- [14204] 城心十字 -- [14208] 北向大道
                                           |                    |
                                           |                    +-- east -- [14209] 官署前街 -- [14210] 榜文長廊 -- [14211] 東江路口 -- [14212] 東碼頭
                                           |
                                           +-- west -- [14205] 西市口 -- [14206] 客棧前街 -- [14207] 商旅街
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_xiangyang",
    "title": "襄陽城",
    "design_notes": "第一版 spec-first 草案。先固定南城門、主街十字、西市補給線與東側官署碼頭線，讓襄陽作為荊州門戶主城的辨識度在 runtime implementation 前先穩住。",
    "level_range": "35-45",
    "planned_vnum_range": "14201-14230",
    "reserved_room_block": "14201-14230",
    "theme": {
      "primary": "歷史城市",
      "secondary": "荊州門戶 / 軍旅樞紐"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 14201,
        "target_area": "jingxiang_road",
        "label": "荊襄大道"
      },
      {
        "direction": "north",
        "source_vnum": 14208,
        "target_area": "fort_fancheng",
        "target_room_vnum": 20101,
        "label": "樊城方向"
      },
      {
        "direction": "east",
        "source_vnum": 14212,
        "target_area": "wild_jiangxia_river",
        "label": "江夏水路"
      },
      {
        "direction": "west",
        "source_vnum": 14209,
        "target_area": "city_xinye",
        "label": "新野大道"
      }
    ],
    "clusters": [
      { "id": "south-gate", "label": "南城門帶" },
      { "id": "main-avenue", "label": "主街十字" },
      { "id": "market-quarter", "label": "西市補給線" },
      { "id": "yamen-quarter", "label": "官署榜文線" },
      { "id": "east-wharf", "label": "東碼頭線" }
    ]
  },
  "rooms": [
    {
      "vnum": 14201,
      "name": "南城門",
      "description": "襄陽南城門高而厚，門洞裡始終有兵卒與行旅擦肩而過。門外是大道風塵，門內卻已能嗅到城中炊煙與藥材味，讓人一踏進來便知道自己重新回到了有人情也有規矩的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 9301, "external": true },
        { "direction": "north", "to": 14202 }
      ],
      "enquires": ["城門", "去路"]
    },
    {
      "vnum": 14202,
      "name": "盤查棚前",
      "description": "門內立著臨時盤查棚，桌案、封泥與木牌排得整齊，顯示襄陽對往來消息並不鬆懈。城門守備不像虎牢關那般壓迫，卻仍讓人明白荊州門戶並不會任人隨意來去。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "order"],
      "exits": [
        { "direction": "south", "to": 14201 },
        { "direction": "north", "to": 14203 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "木板上貼著最近的稅糧、巡查與道路告示，看得出襄陽城內外的消息流得很快。"
        }
      ]
    },
    {
      "vnum": 14203,
      "name": "入城主街",
      "description": "主街一路往城心伸去，兩側店招與旗影在風裡互相搶著顏色。這裡不像戰地那樣每一步都要猜危險，而是要在紛雜聲響裡迅速讀懂哪裡能補給、哪裡能問路、哪裡能打探消息。",
      "sector_type": "SECT_CITY",
      "cluster": "main-avenue",
      "coord": [2, 0, 0],
      "labels": ["main-road", "orientation"],
      "exits": [
        { "direction": "south", "to": 14202 },
        { "direction": "north", "to": 14204 }
      ],
      "enquires": ["市集", "客棧", "官府"]
    },
    {
      "vnum": 14204,
      "name": "城心十字",
      "description": "襄陽城心的十字大路把人流自然分開，西側是市集與客棧，東側是官署與江路，往北則可再通往更靠近軍務與外城的大道。站在這裡，整座城的用途幾乎一眼就能看明白。",
      "sector_type": "SECT_CITY",
      "cluster": "main-avenue",
      "coord": [3, 0, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "south", "to": 14203 },
        { "direction": "north", "to": 14208 },
        { "direction": "west", "to": 14205 },
        { "direction": "east", "to": 14209 }
      ],
      "enquires": ["去路", "襄陽", "碼頭"]
    },
    {
      "vnum": 14205,
      "name": "西市口",
      "description": "西市口比主街更熱，也更擠，叫賣聲、討價聲與車輪聲交疊成一種只有大城才有的厚重雜音。人群一多，消息往往也流得更快，補給與傳聞在這裡常是同一回事。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [3, -1, 0],
      "labels": ["market-entry", "crowd"],
      "exits": [
        { "direction": "east", "to": 14204 },
        { "direction": "west", "to": 14206 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "木招牌一塊挨著一塊，高低不齊地伸出簷下，讓整條市口看起來既混亂又生氣勃勃。"
        }
      ],
      "enquires": ["市集", "買賣"]
    },
    {
      "vnum": 14206,
      "name": "客棧前街",
      "description": "這條街上的客棧、食鋪與行腳攤子靠得很近，走不了幾步就能聞到熱湯、酒氣與曬乾藥草混在一起的味道。對長途旅人來說，這種混雜本身就是一種安心訊號。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [3, -2, 0],
      "labels": ["inn-street", "supply"],
      "exits": [
        { "direction": "east", "to": 14205 },
        { "direction": "west", "to": 14207 },
        { "direction": "enter", "to": 14207 }
      ],
      "enquires": ["客棧", "食鋪", "休息"]
    },
    {
      "vnum": 14207,
      "name": "商旅街",
      "description": "更西一點的街面堆著行李、木箱與待裝車貨，像把整座襄陽城的外來與外送都壓縮在這一帶。若要看出這座城究竟連著多少地方，站在這裡往人和貨的方向看就夠了。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [3, -3, 0],
      "labels": ["trade", "storage"],
      "exits": [
        { "direction": "east", "to": 14206 },
        { "direction": "out", "to": 14206 }
      ],
      "enquires": ["商旅", "貨路"]
    },
    {
      "vnum": 14208,
      "name": "北向大道",
      "description": "往北的大道顯得比城中其他街道更寬，也更利於隊列通行，讓人一看就知道這裡承接著更偏軍務與外城的方向。如今大道盡頭已正式接到樊城南關，連風裡都帶著比城內更冷、更硬的北岸守備氣息。",
      "sector_type": "SECT_CITY",
      "cluster": "main-avenue",
      "coord": [4, 0, 0],
      "labels": ["north-link", "military-road"],
      "exits": [
        { "direction": "south", "to": 14204 },
        { "direction": "north", "to": 20101, "external": true }
      ],
      "enquires": ["北路", "樊城", "新野"]
    },
    {
      "vnum": 14209,
      "name": "官署前街",
      "description": "東側街道明顯安靜得多，差役與文書腳步快而短，與西市那種拖長的叫賣節奏完全不同。這裡沒有那麼多煙火氣，卻能讓人感覺到襄陽真正如何維持秩序與消息流通。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [3, 1, 0],
      "labels": ["official", "quiet"],
      "exits": [
        { "direction": "west", "to": 14204 },
        { "direction": "east", "to": 14210 }
      ],
      "enquires": ["官府", "差役"]
    },
    {
      "vnum": 14210,
      "name": "榜文長廊",
      "description": "一排長廊專門張貼城務、稅糧、巡防與失物榜文，紙頁新舊交錯，顯示消息在這座城裡從不真正停下。若懂得看榜，就能比單純問路更快知道城裡最近在忙些什麼。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [3, 2, 0],
      "labels": ["notice", "info"],
      "exits": [
        { "direction": "west", "to": 14209 },
        { "direction": "east", "to": 14211 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "路牌除了標示碼頭與南北大道，還特別寫著幾處渡口與外驛，可見襄陽對交通秩序極為看重。"
        }
      ],
      "enquires": ["榜文", "路牌", "碼頭"]
    },
    {
      "vnum": 14211,
      "name": "東江路口",
      "description": "越往東走，風裡的水氣就越明顯，連街面聲音都變得更空更亮。這裡像一條把城市重心慢慢推出城牆、推出陸路，再送到江面上的過渡帶。",
      "sector_type": "SECT_CITY",
      "cluster": "east-wharf",
      "coord": [3, 3, 0],
      "labels": ["river-road", "transition"],
      "exits": [
        { "direction": "west", "to": 14210 },
        { "direction": "east", "to": 14212 }
      ],
      "enquires": ["江路", "東邊"]
    },
    {
      "vnum": 14212,
      "name": "東碼頭",
      "description": "木棧沿水邊一段段伸出去，船纜、木桶與潮濕的木板氣味把這裡與城心完全區分開來。站在東碼頭時，襄陽不再只是一座城，而像整個荊州水陸往來暫時停靠的一個節點。",
      "sector_type": "SECT_CITY",
      "cluster": "east-wharf",
      "coord": [3, 4, 0],
      "labels": ["wharf", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 14301, "external": true },
        { "direction": "west", "to": 14211 }
      ],
      "enquires": ["碼頭", "江夏", "船路"]
    }
  ]
}
```
