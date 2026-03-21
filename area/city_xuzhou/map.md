# 徐州 (`city_xuzhou`)

## Area Intent

`city_xuzhou` 承接 `city_chenliu` 東街路標，把玩家從中原樞紐城正式帶進東線州府，讓 `陳留 -> 徐州 -> 壽春 / 建業` 這條陸路主線重新有一個可回補、可問路、也能明確感受到州城秩序與商旅流動的城市 hub。

第一版目標先固定：

- 一條從西城門進州城的主街骨架，讓玩家明確感受到從陳留東路進城的節奏收束
- 一條市集與糧行支線，承接補給、驛路消息與東線貨物流動
- 一條州府前街與書吏 / 差役支線，強化徐州作為州城而不只是一般商鎮的辨識度
- 一組 `enter/out` 的驛舍轉場，為後續接 `road_shouchun_xuzhou` 保留具體南向出口語意

這一版刻意讓玩家感受到：

- 這裡是中原向江東北段推進的州府樞紐，不是沿海秘境的延伸
- 城內秩序、貨運與州府消息同時運作，形成穩定的回補與問路 loop
- 往西可回陳留，往南則能自然過渡到壽春與更深東線陸路

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `東線州府 / 商旅樞紐`
- LevelRange: `20-32`

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `west` from `16801`: planned link to `city_chenliu`
- `south` from `16808`: planned link to `road_shouchun_xuzhou`

## Suggested Layout

```text
陳留 / 徐州大道方向
   |
[16801] 西城門外 -- [16802] 西門甬道 -- [16803] 徐州主街西段 -- [16804] 州府十字 -- [16807] 東街書肆口
                                                    |                    |
                                                    |                    +-- [16806] 州府前街
                                                    |
                                                    +-- [16805] 市集牌樓
                                                    |
                                                    +-- [16808] 南門驛口 -- enter -- [16809] 驛舍大堂
                                                              |
                                                           south (future: 淮東官道 / 壽春)
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_xuzhou",
    "title": "徐州",
    "design_notes": "第一版 spec-first 草案。先固定西門入口、主街十字、市集補給、州府前街與南門驛口，讓陳留東路正式收束成東線州府 hub。",
    "level_range": "20-32",
    "planned_vnum_range": "16801-16820",
    "reserved_room_block": "16801-16820",
    "theme": {
      "primary": "歷史城市",
      "secondary": "東線州府 / 商旅樞紐"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 16801,
        "target_area": "city_chenliu",
        "label": "徐州大道"
      },
      {
        "direction": "south",
        "source_vnum": 16808,
        "target_area": "road_shouchun_xuzhou",
        "label": "淮東官道"
      }
    ],
    "clusters": [
      {
        "id": "west-gate",
        "label": "西門緩衝帶"
      },
      {
        "id": "main-street",
        "label": "主街與州府十字"
      },
      {
        "id": "market-yard",
        "label": "市集與糧行帶"
      },
      {
        "id": "office-lane",
        "label": "州府前街"
      },
      {
        "id": "south-station",
        "label": "南門驛帶"
      }
    ]
  },
  "rooms": [
    {
      "vnum": 16801,
      "name": "西城門外",
      "description": "高大的徐州西門把東線塵路與州城秩序切成兩種截然不同的節奏。門外還留著遠路商旅的車轍與風塵，門內卻已經能聽見城中市聲與差役喝問，像是在提醒你這裡不是普通路站，而是一座真正承接州郡消息的城。 ",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "east", "to": 16802 }
      ],
      "enquires": ["徐州", "城門", "陳留"]
    },
    {
      "vnum": 16802,
      "name": "西門甬道",
      "description": "甬道牆上貼著通商、盤查與巡夜條例，往來旅人都會在這裡下意識放慢腳步。比起陳留那種中原樞紐的四面消息，徐州的門洞更像把東線貨流與州城制度一道一道收進來。 ",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "west", "to": 16801 },
        { "direction": "east", "to": 16803 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "告示上除了通商時辰與夜禁規矩，還特別提到南路驛馬吃緊，勸旅人提早問清楚行程。"
        }
      ],
      "enquires": ["告示", "盤查", "南路"]
    },
    {
      "vnum": 16803,
      "name": "徐州主街西段",
      "description": "寬闊街道沿著城心筆直向東伸去，布幌、藥材箱、糧袋與驛馬行李在街邊堆出一種東線州城特有的忙碌。這裡不像邊關那樣劍拔弩張，卻也比普通城鎮更能讓人感覺到各方消息正不斷流進流出。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [2, 0, 0],
      "labels": ["main-road", "traffic"],
      "exits": [
        { "direction": "west", "to": 16802 },
        { "direction": "east", "to": 16804 }
      ]
    },
    {
      "vnum": 16804,
      "name": "州府十字",
      "description": "四條街路在州府十字交會，往北偏靜、往南偏忙、往東則更多書吏與抄手走動。若說徐州是一張把中原與江東北段重新編起來的路網，那麼這裡就是線頭與線頭彼此纏住又分開的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [3, 0, 0],
      "labels": ["junction", "city-core"],
      "exits": [
        { "direction": "west", "to": 16803 },
        { "direction": "south", "to": 16808 },
        { "direction": "east", "to": 16807 },
        { "direction": "enter", "to": 16805 },
        { "direction": "north", "to": 16806 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "路牌一面指著陳留大道，一面指著淮東官道與南門驛舍，還有幾筆急就章似的補註寫著近日換馬與糧價。"
        }
      ],
      "enquires": ["去路", "州府", "南門", "市集"]
    },
    {
      "vnum": 16805,
      "name": "市集牌樓",
      "description": "一進牌樓，米糧、藥材、燈油與旅貨的氣味立刻混成一股飽滿的州城市聲。這裡不只賣東西，更像整座徐州把外來消息過一道手的地方，常有人一邊採買，一邊聽掌櫃講哪條路最近比較通。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [3, -1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "out", "to": 16804 }
      ],
      "enquires": ["市集", "糧行", "補給", "掌櫃"]
    },
    {
      "vnum": 16806,
      "name": "州府前街",
      "description": "州府前街的步調明顯比主街更穩，差役、抄手與來報公文的人說話都壓低了幾分。站在這裡時，你很容易感受到徐州不是只靠商旅熱鬧撐起來，它真正的重量還在於州郡秩序本身。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-lane",
      "coord": [3, 1, 0],
      "labels": ["office", "authority"],
      "exits": [
        { "direction": "south", "to": 16804 }
      ],
      "keywords": [
        {
          "keyword": "州府",
          "description": "州府門前木牌列著近日本城糧運、巡夜與驛路調度，看得出這裡最關心的是如何讓整個東線不要亂了節奏。"
        }
      ],
      "enquires": ["州府", "差役", "公文"]
    },
    {
      "vnum": 16807,
      "name": "東街書肆口",
      "description": "這一帶比市集少了些叫賣，多了抄寫文書、記錄貨單與整理路引的書肆氣味。幾名書吏正對著卷冊核對地名與車次，讓人一眼就明白徐州為何總能把四面八方的旅人重新安頓進正確的路上。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [4, 0, 0],
      "labels": ["records", "travel-info"],
      "exits": [
        { "direction": "west", "to": 16804 }
      ],
      "enquires": ["書肆", "路引", "地名"]
    },
    {
      "vnum": 16808,
      "name": "南門驛口",
      "description": "南門一帶滿是換馬、整索與重新綁緊行囊的聲音，整座徐州像在這裡把人與貨推往更南的淮東官道。這種忙碌和主街不同，不是逗留，而是準備再度上路。 ",
      "sector_type": "SECT_CITY",
      "cluster": "south-station",
      "coord": [3, -2, 0],
      "labels": ["south-edge", "world-link-south", "travel"],
      "exits": [
        { "direction": "north", "to": 16804 },
        { "direction": "enter", "to": 16809 }
      ],
      "enquires": ["南門", "壽春", "官道", "驛馬"]
    },
    {
      "vnum": 16809,
      "name": "驛舍大堂",
      "description": "大堂裡的長案排著車次、換馬與路引記錄，掌事人說話不快，卻總能在幾句之間把旅人的路重新排清楚。比起豪華或熱鬧，這裡更讓人感受到一座州城真正的可靠，是它能把下一段路準備得有條有理。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "south-station",
      "coord": [3, -2, 1],
      "labels": ["inside", "travel", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 16808 }
      ],
      "enquires": ["車次", "路引", "換馬"]
    }
  ]
}
```
