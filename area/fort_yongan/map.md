# 永安 (`fort_yongan`)

## Area Intent

`fort_yongan` 承接 `fort_yiling` 的西向關坪，把蜀荊主線從外緣咽喉再往內推成一座更厚、更穩、更像真正堡寨內環的險關。這裡不再只是放行與盤查的門口，而是一個會把斥候、軍械、命令與西進城帶節奏都一起壓進堡牆裡的地方。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `險關 / 堡壘`
- LevelRange: `40-54`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_yongan",
    "title": "永安",
    "design_notes": "第一版 spec-first 草案。先固定夷陵西向關坪外的堡前入口、永安柵道、永安堡門、堡門內道、斥候木棚、軍械棚區與關樓望台，讓蜀漢上游前的堡壘關口正式落地。",
    "level_range": "40-54",
    "planned_vnum_range": "19501-19520",
    "reserved_room_block": "19501-19520",
    "theme": {
      "primary": "軍旅",
      "secondary": "險關 / 堡壘"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 19501,
        "target_area": "fort_yiling",
        "target_room_vnum": 19408,
        "label": "夷陵西關"
      },
      {
        "direction": "west",
        "source_vnum": 19508,
        "target_area": "city_jiangzhou",
        "target_room_vnum": 19601,
        "label": "上游城路"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "堡前入口帶" },
      { "id": "gate", "label": "堡門與內道" },
      { "id": "camp", "label": "斥候與軍械帶" },
      { "id": "watch", "label": "關樓與西向堡口" }
    ]
  },
  "rooms": [
    {
      "vnum": 19501,
      "name": "東向堡前",
      "description": "自夷陵西關再走到這裡後，路面的風聲和牆影都變得更厚，像整條西進關道終於把人送進了真正的堡寨前層。東向堡前不像單純的關坪，更像一道把外緣軍旅壓力重新收進蜀漢內部秩序的門檻。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 19408, "external": true },
        { "direction": "west", "to": 19502 }
      ],
      "enquires": ["夷陵", "東邊", "堡前"]
    },
    {
      "vnum": 19502,
      "name": "永安柵道",
      "description": "永安柵道比夷陵那段更沉更直，木柵和地樁都像是為了逼迫來者在尚未看見堡門前就先放慢腳步。這種不容迴避的收束感，讓人一站上來就知道這裡不是路過，而是接受一座堡壘重新安排你的動線。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [-1, 0, 0],
      "labels": ["approach", "control-line"],
      "exits": [
        { "direction": "east", "to": 19501 },
        { "direction": "west", "to": 19503 },
        { "direction": "south", "to": 19505 }
      ],
      "enquires": ["柵道", "盤關", "守兵"]
    },
    {
      "vnum": 19503,
      "name": "永安堡門",
      "description": "厚重堡門比前一道夷陵關門更像真正的內層邊界，木鐵結構和牆影一起把外頭旅路與裡頭軍務分得十分清楚。站在這裡時，會明顯感到自己正從邊地咽喉進一步走進蜀漢上游的堡寨腹地。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [-2, 0, 0],
      "labels": ["gate", "fortress-threshold"],
      "exits": [
        { "direction": "east", "to": 19502 },
        { "direction": "west", "to": 19504 }
      ],
      "enquires": ["堡門", "放行", "關防"]
    },
    {
      "vnum": 19504,
      "name": "堡門內道",
      "description": "一進內道，整座永安的節奏就不再是對外盤查，而更像為了持久防守與軍令調度而存在的緊密秩序。短短一段內道卻把軍械棚、望樓和更西的上游去路都壓在同一條視線裡，讓堡壘的厚度變得很具體。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [-3, 0, 0],
      "labels": ["core", "fortress-flow"],
      "exits": [
        { "direction": "east", "to": 19503 },
        { "direction": "west", "to": 19508 },
        { "direction": "south", "to": 19506 },
        { "direction": "up", "to": 19507 }
      ],
      "enquires": ["內道", "軍械", "望樓"]
    },
    {
      "vnum": 19505,
      "name": "斥候木棚",
      "description": "木棚下掛著風乾披風、行圖板和換班木牌，看得出這裡更偏向長路回報與關外視線整理，而不是臨時歇腳。堡壘真正的前線感，往往就是從這種看似不起眼的斥候節奏慢慢堆起來的。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-1, -1, 0],
      "labels": ["scout", "report-line"],
      "exits": [
        { "direction": "north", "to": 19502 }
      ],
      "enquires": ["斥候", "回報", "地圖"]
    },
    {
      "vnum": 19506,
      "name": "軍械棚區",
      "description": "軍械棚裡整齊堆著槍桿、弓匣、燈油和備用皮囊，每一樣都像是為了告訴人這座堡壘預設自己要撐很久。比起夷陵的軍需更替，永安這裡多了一層真正為長守而準備的厚重感。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-3, -1, 0],
      "labels": ["arms", "supply"],
      "exits": [
        { "direction": "north", "to": 19504 }
      ],
      "enquires": ["軍械", "糧草", "備守"]
    },
    {
      "vnum": 19507,
      "name": "關樓望台",
      "description": "望台把東來關道、西去城路與堡門內外的動靜一口氣收進視線裡，讓人幾乎能感覺到命令如何從這裡往下壓。它不像夷陵那種偏外線的前哨高點，而更像一座堡壘真正管住節奏的眼睛。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [-3, 0, 1],
      "labels": ["watchtower", "orders", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 19504 }
      ],
      "enquires": ["望台", "旗號", "軍令"]
    },
    {
      "vnum": 19508,
      "name": "西嶺堡口",
      "description": "再往西去，路勢開始鬆開成更像通往上游城帶的山嶺堡口，與東側那種純粹盤關的壓力有了明顯差別。站在這裡會知道永安不只是防守的結束點，也是把人正式送往江州與蜀中腹地的軍旅前口。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [-4, 0, 0],
      "labels": ["west-edge", "future-link", "forward"],
      "exits": [
        { "direction": "east", "to": 19504 },
        { "direction": "west", "to": 19601, "external": true }
      ],
      "enquires": ["江州", "西邊", "上游"]
    }
  ]
}
```
