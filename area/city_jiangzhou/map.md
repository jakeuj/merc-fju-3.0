# 江州 (`city_jiangzhou`)

## Area Intent

`city_jiangzhou` 承接 `fort_yongan` 西嶺堡口，把原本還停在堡門、上游山路與更西蜀中想像裡的遠行節奏，正式收束回一座有市聲、州府與行旅節點的上游港城。這裡不是單純讓人喘口氣的安全段，而是一個會把軍旅壓力重新翻譯成交通、榜示、補給與地方秩序的城市樞紐。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `上游港城 / 蜀中轉運`
- LevelRange: `36-50`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_jiangzhou",
    "title": "江州",
    "design_notes": "第一版 spec-first 草案。先固定東嶺城門、入城長街、江州十字、臨江市口、行旅客棧前、州府前街、貨棧長廊與西城官道口，把永安之西的上游主線正式收束成可載入的城市 hub。",
    "level_range": "36-50",
    "planned_vnum_range": "19601-19620",
    "reserved_room_block": "19601-19620",
    "theme": {
      "primary": "歷史城市",
      "secondary": "上游港城 / 蜀中轉運"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 19601,
        "target_area": "fort_yongan",
        "target_room_vnum": 19508,
        "label": "東嶺堡路"
      },
      {
        "direction": "west",
        "source_vnum": 19608,
        "target_area": "city_chengdu",
        "target_room_vnum": 19701,
        "label": "西向官道"
      }
    ],
    "clusters": [
      { "id": "east-gate", "label": "東門入口帶" },
      { "id": "main-street", "label": "主街十字" },
      { "id": "market-quarter", "label": "臨江市口與客棧線" },
      { "id": "yamen-quarter", "label": "州府與貨棧線" },
      { "id": "west-road", "label": "西城官道口" }
    ]
  },
  "rooms": [
    {
      "vnum": 19601,
      "name": "東嶺城門",
      "description": "剛離開永安的堡路走到這裡時，牆影與市聲會一起把人的心口鬆開半寸。東嶺城門仍保留了面向關道的盤查與秩序，可門內已能聞到熱湯、濕木與貨車麻繩混在一起的城氣，像是在告訴遠路人自己終於從堡寨節奏回到了真正有人生活的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "east-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 19508, "external": true },
        { "direction": "west", "to": 19602 }
      ],
      "enquires": ["永安", "東門", "堡路"]
    },
    {
      "vnum": 19602,
      "name": "入城長街",
      "description": "長街兩旁的布旗、貨挑與路牌把江州的用途寫得很清楚，東邊收人進城，西邊送人上路，支巷則把人分流到客棧與官署。這種不必大聲張揚卻人人都讀得懂的秩序，正是上游港城最可靠的安定感。",
      "sector_type": "SECT_CITY",
      "cluster": "east-gate",
      "coord": [-1, 0, 0],
      "labels": ["approach", "orientation"],
      "exits": [
        { "direction": "east", "to": 19601 },
        { "direction": "west", "to": 19603 },
        { "direction": "south", "to": 19605 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "木牌上把臨江市口、州府與西城官道都標得分明，像是專門替剛走出關路的人重新整理方向。"
        }
      ],
      "enquires": ["路牌", "市口", "州府"]
    },
    {
      "vnum": 19603,
      "name": "江州十字",
      "description": "站在江州十字時，城裡的節奏會突然變得很好懂，南邊是行旅歇腳，北邊是州府消息，西邊則是更深蜀中的官道去向。它不像江陵那樣帶著荊蜀交界的邊緣感，而更像一座真正把上游人流與地方秩序攏在手心裡的蜀地城市心臟。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [-2, 0, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "east", "to": 19602 },
        { "direction": "west", "to": 19604 },
        { "direction": "north", "to": 19606 }
      ],
      "enquires": ["江州", "十字", "成都"]
    },
    {
      "vnum": 19604,
      "name": "臨江市口",
      "description": "臨江市口的人聲帶著更重的水路與貨旅氣味，布幌、秤桿與船腳消息一起把這條街撐得繁而不亂。比起單純買賣，它更像一個會把江上與陸路消息先攪在一起，再分送往各條官道的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-3, 0, 0],
      "labels": ["market", "riverside", "trade"],
      "exits": [
        { "direction": "east", "to": 19603 },
        { "direction": "west", "to": 19608 },
        { "direction": "south", "to": 19607 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "沿街的招牌、木幌與價牌把江州最熱鬧的一段市口擠得滿滿當當，像連風都得先學會排隊才能穿過去。"
        }
      ],
      "enquires": ["市口", "貨船", "客商"]
    },
    {
      "vnum": 19605,
      "name": "行旅客棧前",
      "description": "客棧前堆著剛卸下的竹簍、熱湯木桶與還沒擦淨泥痕的行囊，看得出這裡經常替剛走完關路的人把疲憊和路程一起安頓下來。江州若說有哪一處最能把軍旅餘味慢慢洗成城市節奏，大概就是這裡。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-1, -1, 0],
      "labels": ["inn", "rest", "supply"],
      "exits": [
        { "direction": "north", "to": 19602 }
      ],
      "enquires": ["客棧", "熱湯", "歇腳"]
    },
    {
      "vnum": 19606,
      "name": "州府前街",
      "description": "州府前街的氣味比市口乾得多，靴聲、公文與差役回報的節奏把整條街撐出一種可靠又不近人的秩序。對旅人而言，這裡最重要的功能從來不只是管事，而是把四方消息整理成可理解、可依循的方向。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [-2, 1, 0],
      "labels": ["yamen", "order", "information"],
      "exits": [
        { "direction": "south", "to": 19603 }
      ],
      "enquires": ["州府", "差役", "告示"]
    },
    {
      "vnum": 19607,
      "name": "貨棧長廊",
      "description": "長廊一側堆著寫好去向的箱籠與封條，另一側則掛滿等著送往更西城道與更東堡路的行腳名冊。它不像官署那樣冷，也不像市口那樣鬧，卻最能讓人看懂江州真正的本事其實是替各路貨旅重新排好秩序。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [-3, -1, 0],
      "labels": ["warehouse", "dispatch", "corridor"],
      "exits": [
        { "direction": "north", "to": 19604 }
      ],
      "enquires": ["貨棧", "封條", "行腳"]
    },
    {
      "vnum": 19608,
      "name": "西城官道口",
      "description": "再往西去，街面開始慢慢收束成更長、更平穩的內陸官道氣味，遠遠不像東邊那樣還帶著堡寨壓力。西城官道口讓人明白江州既是遠路的終點，也是往成都與蜀中腹地重新啟程的起點。",
      "sector_type": "SECT_CITY",
      "cluster": "west-road",
      "coord": [-4, 0, 0],
      "labels": ["west-edge", "future-link", "forward"],
      "exits": [
        { "direction": "east", "to": 19604 },
        { "direction": "west", "to": 19701, "external": true }
      ],
      "enquires": ["西邊", "成都", "官道"]
    }
  ]
}
```
