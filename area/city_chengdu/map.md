# 成都 (`city_chengdu`)

## Area Intent

`city_chengdu` 承接 `city_jiangzhou` 西城官道口，把原本還停在上游城帶、貨旅名冊與更西官道想像裡的主線節奏，正式收束回蜀漢都城。這裡不再是只替人整理方向的中繼點，而是一個會把遠路、官務、市聲與母城規模一起壓進秩序裡的首都核心。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `蜀漢都城`
- LevelRange: `34-48`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_chengdu",
    "title": "成都",
    "design_notes": "第一版 spec-first 草案。先固定東城門、入城御道、錦城十字、市樓牌坊、行旅客舍、學舍外街、蜀府前廊與西郊城關，把江州之西的主線正式收束成蜀漢都城母區。",
    "level_range": "34-48",
    "planned_vnum_range": "19701-19720",
    "reserved_room_block": "19701-19720",
    "theme": {
      "primary": "歷史城市",
      "secondary": "蜀漢都城"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 19701,
        "target_area": "city_jiangzhou",
        "target_room_vnum": 19608,
        "label": "東來官道"
      },
      {
        "direction": "east",
        "source_vnum": 19704,
        "target_area": "district_chengdu_market",
        "label": "市井分區"
      },
      {
        "direction": "north",
        "source_vnum": 19706,
        "target_area": "district_chengdu_scholar",
        "label": "學舍街"
      },
      {
        "direction": "out",
        "source_vnum": 19708,
        "target_area": "wild_chengdu_outer",
        "target_room_vnum": 19801,
        "label": "西郊去路"
      }
    ],
    "clusters": [
      { "id": "east-gate", "label": "東門入口帶" },
      { "id": "main-street", "label": "御道與十字" },
      { "id": "market-quarter", "label": "市樓與客舍帶" },
      { "id": "official-quarter", "label": "學舍與府衙帶" },
      { "id": "west-road", "label": "西郊城關" }
    ]
  },
  "rooms": [
    {
      "vnum": 19701,
      "name": "東城門",
      "description": "自江州再一路西來到這裡時，官道的塵氣會先撞上更厚的牆影與更整齊的旗號。東城門不像上游城帶那樣忙著分流，而更像一座真正的大城在確認你是否已經來到它的秩序之內。站在這裡時，遠路感會第一次明顯被都城規模壓住。",
      "sector_type": "SECT_CITY",
      "cluster": "east-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 19608, "external": true },
        { "direction": "west", "to": 19702 }
      ],
      "enquires": ["江州", "東門", "官道"]
    },
    {
      "vnum": 19702,
      "name": "入城御道",
      "description": "御道比沿途任何一段城路都更寬也更穩，連路旗、車痕與巡行腳步都像被一種看不見的手重新排過。這種不需大聲宣示就能讓人自動放慢聲音的秩序，正是都城與一般城鎮最直接的差別。",
      "sector_type": "SECT_CITY",
      "cluster": "east-gate",
      "coord": [-1, 0, 0],
      "labels": ["approach", "order"],
      "exits": [
        { "direction": "east", "to": 19701 },
        { "direction": "west", "to": 19703 },
        { "direction": "south", "to": 19705 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "立在御道邊的路牌把市樓、學舍與西郊門都標得清清楚楚，像是整座成都連問路都嫌太吵。"
        }
      ],
      "enquires": ["路牌", "市樓", "學舍"]
    },
    {
      "vnum": 19703,
      "name": "錦城十字",
      "description": "錦城十字把成都的節奏全攤在眼前，南邊有行旅歇腳，北邊是讀書與官務，西邊則通向更廣的都城外帶。它不像江州那樣偏重轉運，而更像一個天生用來吸納四方、再把所有事情都安排回體面的中心點。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [-2, 0, 0],
      "labels": ["junction", "capital-core"],
      "exits": [
        { "direction": "east", "to": 19702 },
        { "direction": "south", "to": 19704 },
        { "direction": "north", "to": 19706 },
        { "direction": "west", "to": 19708 }
      ],
      "enquires": ["成都", "十字", "蜀都"]
    },
    {
      "vnum": 19704,
      "name": "市樓牌坊",
      "description": "市樓牌坊下的人聲、木幌與布色都比上游城市更繁更穩，熱鬧卻沒有半點倉促，像整條街早已習慣接住來自四方的貨與人。這裡讓人一眼就懂成都不只是大，而是早就學會把大城的吵雜收進秩序裡。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-2, -1, 0],
      "labels": ["market", "archway", "future-district"],
      "exits": [
        { "direction": "north", "to": 19703 },
        { "direction": "south", "to": 19707 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "一層又一層伸出的招牌和市幌幾乎把牌坊後的視線切碎，卻也讓人清楚知道這裡就是成都最會吞吐人潮的一帶。"
        }
      ],
      "enquires": ["市樓", "市集", "牌坊"]
    },
    {
      "vnum": 19705,
      "name": "行旅客舍",
      "description": "客舍前的木箱、熱食與換洗水盆看起來都比一般客棧更講究，彷彿連休息這件事在成都也得被照看得體面些。對剛從東來官道進城的人而言，這裡最像都城給遠路人的第一份安穩。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-1, -1, 0],
      "labels": ["inn", "rest", "capital-service"],
      "exits": [
        { "direction": "north", "to": 19702 }
      ],
      "enquires": ["客舍", "熱食", "歇息"]
    },
    {
      "vnum": 19706,
      "name": "學舍外街",
      "description": "外街比主十字安靜許多，卻不冷清，紙墨、木簡與低聲議論把空氣撐出一種都城才有的知性秩序。它讓人很清楚知道，成都不只靠市聲與官威立城，也靠這些讀書與議論的氣味把整座都城撐得更厚。",
      "sector_type": "SECT_CITY",
      "cluster": "official-quarter",
      "coord": [-2, 1, 0],
      "labels": ["scholar", "quiet", "future-district"],
      "exits": [
        { "direction": "south", "to": 19703 }
      ],
      "enquires": ["學舍", "書院", "讀書人"]
    },
    {
      "vnum": 19707,
      "name": "蜀府前廊",
      "description": "前廊下的差役、榜示與往來文書把這一帶撐得比市樓更乾更穩，連腳步聲都像被地面收得俐落。比起單純管事，這裡更像成都把四方消息整理成國都秩序的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "official-quarter",
      "coord": [-2, -2, 0],
      "labels": ["office", "notice", "state-order"],
      "exits": [
        { "direction": "north", "to": 19704 }
      ],
      "enquires": ["官府", "榜示", "差役"]
    },
    {
      "vnum": 19708,
      "name": "西郊城關",
      "description": "西郊城關不像東門那樣帶著入城壓力，而更像都城緩緩把秩序往外推送的邊界。站在這裡時，能明顯感到成都的厚度還沒有結束，只是開始把人送往更廣的郊外與蜀地腹心。",
      "sector_type": "SECT_CITY",
      "cluster": "west-road",
      "coord": [-3, 0, 0],
      "labels": ["west-edge", "future-link", "capital-outgate"],
      "exits": [
        { "direction": "east", "to": 19703 },
        { "direction": "out", "to": 19801, "external": true }
      ],
      "enquires": ["西邊", "近郊", "出城"]
    }
  ]
}
```
