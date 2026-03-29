# 新野郊野 (`wild_xinye_fields`)

## Area Intent

`wild_xinye_fields` 承接 `city_xinye` 西田路牌外那條郊野田路，把原本仍停在「往西是田地與村落」語意上的邊鎮外帶，正式展開成田埂、灌渠、村口茶棚與西野風碑交錯的近郊 wild。這裡不是深山，也不是另一座城，而是一段會讓人明顯感到「新野的人情還沒完全退遠，但辨位已經開始要靠地勢、水路和熟地方痕跡」的外野帶。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `田野 / 村落`
- LevelRange: `18-28`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_xinye_fields",
    "title": "新野郊野",
    "design_notes": "第一版 spec-first 草案。先固定田路出口、田埂岔路、灌渠木橋、村口茶棚、稻田路肩、籬旁曬場、獵戶石堆與西野風碑，讓新野西側正式展開成可載入的近郊田野骨架。",
    "level_range": "18-28",
    "planned_vnum_range": "20301-20320",
    "reserved_room_block": "20301-20320",
    "theme": {
      "primary": "江湖",
      "secondary": "田野 / 村落"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 20301,
        "target_area": "city_xinye",
        "target_room_vnum": 20205,
        "label": "西田路牌"
      }
    ],
    "clusters": [
      { "id": "entry-lane", "label": "田路入口" },
      { "id": "field-lanes", "label": "田埂與灌渠" },
      { "id": "village-edge", "label": "村口茶棚" },
      { "id": "west-fringe", "label": "西野邊帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 20301,
      "name": "田路出口",
      "description": "一離開新野西田路牌，腳下石地便很快鬆成帶著土粒與草根的田路。回頭仍看得到鎮邊屋影與舊木牌，往前卻已經是得靠田埂、水聲與腳印自己辨方向的外圍生活帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "entry-lane",
      "coord": [0, 0, 0],
      "labels": ["entry", "return-link", "field-road"],
      "exits": [
        { "direction": "east", "to": 20205, "external": true },
        { "direction": "west", "to": 20302 },
        { "direction": "south", "to": 20303 }
      ],
      "enquires": ["新野", "回鎮", "田路"]
    },
    {
      "vnum": 20302,
      "name": "田埂岔路",
      "description": "幾條踩得發實的田埂在這裡分成不同方向，沒有城裡那種把去路寫得清清楚楚的體面，卻有種只要問對人、看對地勢就不會走丟的鄉間熟路感。站在這裡時，會很清楚感到自己已經離開鎮內那種靠招牌辨位的節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "field-lanes",
      "coord": [-1, 0, 0],
      "labels": ["junction", "field-core", "orientation"],
      "exits": [
        { "direction": "east", "to": 20301 },
        { "direction": "west", "to": 20304 },
        { "direction": "south", "to": 20305 }
      ],
      "keywords": [
        {
          "keyword": "路樁",
          "description": "路邊木樁只刻了幾筆很簡單的方向記號，像是留給熟地方的人自己意會，不打算替陌生人把每條去路都講明白。"
        }
      ],
      "enquires": ["岔路", "村口", "水路"]
    },
    {
      "vnum": 20303,
      "name": "灌渠木橋",
      "description": "細窄木橋跨在灌渠上，水聲不大，卻替整片田路帶出一種離鎮後才會慢慢聽清楚的生活節奏。這裡沒有大路的排場，只有一點點夠人會車、夠人停腳看水勢的鄉間實用感。",
      "sector_type": "SECT_FIELD",
      "cluster": "field-lanes",
      "coord": [0, -1, 0],
      "labels": ["bridge", "waterway", "field-service"],
      "exits": [
        { "direction": "north", "to": 20301 },
        { "direction": "west", "to": 20305 }
      ],
      "enquires": ["木橋", "灌渠", "水路"]
    },
    {
      "vnum": 20304,
      "name": "村口茶棚",
      "description": "茶棚靠著村口樹蔭搭起，棚下擺著幾張不怎麼講究卻夠實用的矮桌凳。比起新野鎮中的酒旗街，這裡更像外圍生活替遠路人留下的一口熱水、一句方向與一點不必多問來歷的歇腳情分。",
      "sector_type": "SECT_FIELD",
      "cluster": "village-edge",
      "coord": [-2, 0, 0],
      "labels": ["tea-stop", "village-edge", "rest"],
      "exits": [
        { "direction": "east", "to": 20302 },
        { "direction": "south", "to": 20306 },
        { "direction": "west", "to": 20307 }
      ],
      "keywords": [
        {
          "keyword": "茶棚",
          "description": "棚頂蓋得不高，卻剛好能替趕田路的人擋下一點日頭與塵氣，也讓路過的人自然慢下來問一句前頭好不好走。"
        }
      ],
      "enquires": ["茶水", "村口", "歇腳"]
    },
    {
      "vnum": 20305,
      "name": "稻田路肩",
      "description": "路肩緊貼著一片片矮水田，泥氣、秧苗和腳印把這裡的方向感都染得很實。它不像官道那樣替人把步伐整理乾淨，卻更能讓人明白新野外圍真正托住城鎮日常的，其實就是這樣一段段不起眼的田路。",
      "sector_type": "SECT_FIELD",
      "cluster": "field-lanes",
      "coord": [-1, -1, 0],
      "labels": ["paddy-edge", "field-shoulder", "rural-life"],
      "exits": [
        { "direction": "north", "to": 20302 },
        { "direction": "east", "to": 20303 },
        { "direction": "west", "to": 20306 },
        { "direction": "south", "to": 20307 }
      ],
      "enquires": ["稻田", "田埂", "腳印"]
    },
    {
      "vnum": 20306,
      "name": "籬旁曬場",
      "description": "幾道低籬把曬場和田路勉強分開，場上留著竹篩、舊木架與有人常來常去的生活痕跡。這裡不像真正的村內腹地，卻已經足夠讓外路人感到自己正從新野邊鎮的街面，走進更貼近地方人手與收成節奏的世界。",
      "sector_type": "SECT_FIELD",
      "cluster": "village-edge",
      "coord": [-2, -1, 0],
      "labels": ["drying-yard", "village-work", "transition"],
      "exits": [
        { "direction": "north", "to": 20304 },
        { "direction": "east", "to": 20305 },
        { "direction": "south", "to": 20308 }
      ],
      "enquires": ["曬場", "村舍", "獵戶"]
    },
    {
      "vnum": 20307,
      "name": "獵戶石堆",
      "description": "路旁堆著一小圈石塊與折斷的木樁，看得出是獵戶或巡看的鄉人留下的簡單落腳點。它沒有什麼能稱作景色的排場，卻讓人意識到再往外走，腳步就得同時注意地勢、痕跡與那些不一定想讓陌生人太快看懂的地方規矩。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fringe",
      "coord": [-1, -2, 0],
      "labels": ["hunter-mark", "trail-watch", "gray-edge"],
      "exits": [
        { "direction": "north", "to": 20305 },
        { "direction": "east", "to": 20304 },
        { "direction": "west", "to": 20308 }
      ],
      "enquires": ["獵戶", "石堆", "外路"]
    },
    {
      "vnum": 20308,
      "name": "西野風碑",
      "description": "風碑立在更西一點的高些處，碑面早被風雨磨淡，只剩幾個還勉強看得清的方向字樣。站在這裡時，新野的屋影已經退成背景，眼前只剩更深的田野與還沒完全寫進地圖的小路，像是在提醒旅人這片郊野往後仍有更多空白要自己走出來。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fringe",
      "coord": [-2, -2, 0],
      "labels": ["west-edge", "marker", "future-road"],
      "exits": [
        { "direction": "north", "to": 20306 },
        { "direction": "east", "to": 20307 }
      ],
      "enquires": ["風碑", "西野", "去路"]
    }
  ]
}
```
