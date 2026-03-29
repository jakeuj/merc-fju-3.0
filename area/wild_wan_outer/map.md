# 宛城外道 (`wild_wan_outer`)

## Area Intent

`wild_wan_outer` 承接 `city_wan` 的西城牌樓，把剛在宛城內被榜牌、驛舍與官道口重新收束起來的秩序，慢慢鬆成茶棚、田埂、樹叢與更西土道交錯的城郊外帶。這裡不是另一條主線官道，也不是立刻墜進更深秘境，而是一段會讓人清楚感到「宛城的目光還在背後，但灰色人流與郊邊風氣已經開始接手」的近郊 wild。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `郊道 / 茶棚`
- LevelRange: `14-24`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_wan_outer",
    "title": "宛城外道",
    "design_notes": "第一版 spec-first 草案。先固定西城外道口、宛西郊道、茶棚前坪、風碑岔路、田埂側路、路旁樹叢、流民營火與更西土道，讓宛城西側正式展開成可載入的近郊 wild 骨架。",
    "level_range": "14-24",
    "planned_vnum_range": "20601-20620",
    "reserved_room_block": "20601-20620",
    "theme": {
      "primary": "江湖",
      "secondary": "郊道 / 茶棚"
    },
    "world_links": [
      {
        "direction": "enter",
        "source_vnum": 20601,
        "target_area": "city_wan",
        "target_room_vnum": 20408,
        "label": "西城牌樓"
      }
    ],
    "clusters": [
      { "id": "return-gate", "label": "回城外口" },
      { "id": "road-line", "label": "宛西郊道" },
      { "id": "tea-stop", "label": "茶棚與田埂" },
      { "id": "wild-fringe", "label": "樹叢與灰帶" },
      { "id": "west-track", "label": "更西土道" }
    ]
  },
  "rooms": [
    {
      "vnum": 20601,
      "name": "西城外道口",
      "description": "一踏出宛城西城牌樓，腳下石地很快鬆成帶著土氣與車痕的外道口，城牆後方那股講規矩的秩序也跟著退成背景。回頭仍能借城影辨位，往前卻已經是茶棚、田埂與樹叢把人慢慢交給外圍世界的真正城外。",
      "sector_type": "SECT_FIELD",
      "cluster": "return-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "return-link", "city-edge"],
      "exits": [
        { "direction": "enter", "to": 20408, "external": true },
        { "direction": "west", "to": 20602 },
        { "direction": "south", "to": 20603 }
      ],
      "enquires": ["回城", "牌樓", "出城"]
    },
    {
      "vnum": 20602,
      "name": "宛西郊道",
      "description": "郊道在城外還保留著幾分筆直與踩實的痕跡，卻已經沒有城門內那種處處被人看著的緊。商旅、差役與不太願意報姓名的路人都在這裡重新混成一股鬆散卻有方向的外城節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-1, 0, 0],
      "labels": ["main-road", "westward"],
      "exits": [
        { "direction": "east", "to": 20601 },
        { "direction": "west", "to": 20604 },
        { "direction": "south", "to": 20605 }
      ],
      "keywords": [
        {
          "keyword": "路碑",
          "description": "道旁這塊路碑只簡單寫著回城與更西土道的方向，看得出它不是替官面排場設的，而是專門給真正要辨位趕路的人看的。"
        }
      ],
      "enquires": ["郊道", "茶棚", "更西"]
    },
    {
      "vnum": 20603,
      "name": "茶棚前坪",
      "description": "小小一塊前坪剛好夠讓旅人卸下包袱、換口熱水，再順手打聽城外最近是不是又有人鬧事。比起宛城內整齊的補給節點，這裡更像一種不保證太多、卻足夠讓人接著往下走的城外人情。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [0, -1, 0],
      "labels": ["tea-stop", "rest", "service"],
      "exits": [
        { "direction": "north", "to": 20601 },
        { "direction": "west", "to": 20605 }
      ],
      "keywords": [
        {
          "keyword": "茶棚",
          "description": "這座茶棚並不講究，只靠幾根木柱和舊篷布勉強撐著，卻很穩地替外道上的人留下一小塊能坐、能問、也能稍微喘口氣的地方。"
        }
      ],
      "enquires": ["茶棚", "歇腳", "消息"]
    },
    {
      "vnum": 20604,
      "name": "風碑岔路",
      "description": "風碑邊的土路向西與向南慢慢分開，連車轍深淺都在提醒人這裡開始不再只有一條最正經的去路。站在這裡時，宛城還沒有遠到看不見，卻已經夠遠得讓灰色腳步與耳語有地方分流。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-2, 0, 0],
      "labels": ["marker", "fork", "road-choice"],
      "exits": [
        { "direction": "east", "to": 20602 },
        { "direction": "west", "to": 20608 },
        { "direction": "south", "to": 20606 }
      ],
      "enquires": ["風碑", "岔路", "去向"]
    },
    {
      "vnum": 20605,
      "name": "田埂側路",
      "description": "側路沿著田埂外緣斜斜地往前拖去，泥水、草氣與人踩出的窄痕把官道邊緣洗得很有活路感。這裡沒有城裡那種被整理好的邊界，只有誰常走、誰不願被人看見，全慢慢留在土色裡。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [-1, -1, 0],
      "labels": ["farmland", "side-road"],
      "exits": [
        { "direction": "north", "to": 20602 },
        { "direction": "east", "to": 20603 },
        { "direction": "west", "to": 20606 }
      ],
      "enquires": ["田埂", "側路", "巡邏"]
    },
    {
      "vnum": 20606,
      "name": "路旁樹叢",
      "description": "樹叢貼著側路慢慢密起來，只要視線一離開土路，很快就會被低枝與陰影切斷。它還不算真正的野林，卻已經夠讓流民、藏物，或者不想回應盤問的人，借著樹影躲上一陣子。",
      "sector_type": "SECT_FOREST",
      "cluster": "wild-fringe",
      "coord": [-2, -1, 0],
      "labels": ["forest-edge", "shade", "risk"],
      "exits": [
        { "direction": "north", "to": 20604 },
        { "direction": "east", "to": 20605 },
        { "direction": "south", "to": 20607 }
      ],
      "keywords": [
        {
          "keyword": "樹叢",
          "description": "幾叢矮灌木被踩出不太乾淨的窄痕，像有人常在這裡停下來等官道上的腳步聲走遠。"
        }
      ],
      "enquires": ["樹叢", "流民", "腳步"]
    },
    {
      "vnum": 20607,
      "name": "流民營火",
      "description": "地上只剩一圈燒得不怎麼完整的火痕與幾根折木，既像流民夜裡歇腳的痕跡，也像某些不願讓宛城差役知道的人暫時留下的影子。這裡讓宛城外道第一次真正露出秩序之外的灰色。",
      "sector_type": "SECT_FIELD",
      "cluster": "wild-fringe",
      "coord": [-2, -2, 0],
      "labels": ["campfire", "drifter", "gray-zone"],
      "exits": [
        { "direction": "north", "to": 20606 }
      ],
      "enquires": ["流民", "營火", "夜路"]
    },
    {
      "vnum": 20608,
      "name": "更西土道",
      "description": "再往西去，宛城留下的牆影與牌樓都開始淡成一種只夠回頭辨位的背景，只剩土道本身還替人勉強維持方向感。這裡不像真正的盡頭，卻很清楚是宛把旅人正式交還給更寬、更雜，也更難完全被管住的外圍世界之處。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-track",
      "coord": [-3, 0, 0],
      "labels": ["west-edge", "future-road", "departure"],
      "exits": [
        { "direction": "east", "to": 20604 }
      ],
      "enquires": ["更西", "遠路", "土道"]
    }
  ]
}
```
