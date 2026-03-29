# 成都近郊 (`wild_chengdu_outer`)

## Area Intent

`wild_chengdu_outer` 承接 `city_chengdu` 西郊城關，把剛剛在蜀漢都城裡被規矩壓緊的節奏重新鬆開成官道、茶亭、圩田與路旁林地交錯的近郊外帶。這裡不是另一座城，也不是深山秘境，而是一段會讓人明顯感到「成都的目光還在背後，但真正的遠路又已經開始」的城外過渡帶。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `郊外 / 農田`
- LevelRange: `30-42`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_chengdu_outer",
    "title": "成都近郊",
    "design_notes": "第一版 spec-first 草案。先固定城關外坡、西郊官道、茶亭前坪、圩田路肩、路旁林地、破亭營火與更西官道，讓成都正式向外展開成可載入的近郊 wild 骨架。",
    "level_range": "30-42",
    "planned_vnum_range": "19801-19820",
    "reserved_room_block": "19801-19820",
    "theme": {
      "primary": "江湖",
      "secondary": "郊外 / 農田"
    },
    "world_links": [
      {
        "direction": "enter",
        "source_vnum": 19801,
        "target_area": "city_chengdu",
        "target_room_vnum": 19708,
        "label": "西郊城關"
      }
    ],
    "clusters": [
      { "id": "return-slope", "label": "回城坡口" },
      { "id": "road-line", "label": "西郊官道" },
      { "id": "tea-stop", "label": "茶亭與圩田" },
      { "id": "wild-fringe", "label": "林地與流民帶" },
      { "id": "west-road", "label": "更西官道" }
    ]
  },
  "rooms": [
    {
      "vnum": 19801,
      "name": "城關外坡",
      "description": "一離開成都西郊城關，腳下的石地便很快鬆成帶土氣的坡路，連風裡的聲音都比城內散得開。回頭仍看得見城牆與旗影，往前卻已經是會把人慢慢交給官道與郊野的真正城外。",
      "sector_type": "SECT_FIELD",
      "cluster": "return-slope",
      "coord": [0, 0, 0],
      "labels": ["entry", "return-link", "city-edge"],
      "exits": [
        { "direction": "enter", "to": 19708, "external": true },
        { "direction": "west", "to": 19802 },
        { "direction": "south", "to": 19803 }
      ],
      "enquires": ["回城", "城關", "出城"]
    },
    {
      "vnum": 19802,
      "name": "西郊官道",
      "description": "官道在成都外帶仍維持著筆直和寬整，卻已經沒有城內那種處處被秩序扶正的壓力。行旅、巡哨和趕車的人流從這裡重新混成真正的遠路節奏，讓人明白都城只是在背後，不再包辦你的每一步。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-1, 0, 0],
      "labels": ["main-road", "westward"],
      "exits": [
        { "direction": "east", "to": 19801 },
        { "direction": "west", "to": 19804 },
        { "direction": "south", "to": 19805 }
      ],
      "keywords": [
        {
          "keyword": "路碑",
          "description": "立在官道旁的路碑把茶亭、田路與更西去向標得很簡單，像是在提醒離城之後真正重要的是辨位，而不是排場。"
        }
      ],
      "enquires": ["官道", "茶亭", "西邊"]
    },
    {
      "vnum": 19803,
      "name": "茶亭前坪",
      "description": "茶亭前的小坪地不大，卻剛好夠趕路人卸下肩上的急促，換一口熱水再問一句前路。比起成都城內講究分寸的客舍，這裡更像城外世界給旅人留下的第一分人情與喘息。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [0, -1, 0],
      "labels": ["tea-stop", "rest", "service"],
      "exits": [
        { "direction": "north", "to": 19801 },
        { "direction": "west", "to": 19805 }
      ],
      "keywords": [
        {
          "keyword": "茶亭",
          "description": "這座茶亭靠幾根老木柱勉強撐住，卻仍穩穩替路人擋下一點日頭、雨氣和從城裡帶出來的緊繃。"
        }
      ],
      "enquires": ["茶亭", "商旅", "歇腳"]
    },
    {
      "vnum": 19804,
      "name": "郊外岔碑",
      "description": "岔路邊的石碑被風吹得發白，碑字不再講究體面，只求讓人知道哪一條回成都、哪一條去更西的農路與長道。站在這裡時，會很清楚感到城外生活早就不靠都城替它整理出每個答案。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-2, 0, 0],
      "labels": ["marker", "fork", "road-choice"],
      "exits": [
        { "direction": "east", "to": 19802 },
        { "direction": "west", "to": 19808 },
        { "direction": "south", "to": 19806 }
      ],
      "enquires": ["路碑", "岔口", "郊外"]
    },
    {
      "vnum": 19805,
      "name": "圩田路肩",
      "description": "路肩貼著圩田斜斜往外展開，泥氣、水痕和低聲交談把官道邊緣洗得很有人活著的痕跡。這裡沒有都城的氣派，卻更像真正托住成都日常的土地與人手。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [-1, -1, 0],
      "labels": ["farmland", "shoulder-road"],
      "exits": [
        { "direction": "north", "to": 19802 },
        { "direction": "east", "to": 19803 },
        { "direction": "west", "to": 19806 }
      ],
      "enquires": ["圩田", "田路", "巡邏"]
    },
    {
      "vnum": 19806,
      "name": "路旁林地",
      "description": "林地貼著官道南側慢慢密起來，讓視線一離開大路就會被草木和陰影截斷。它還不算深，也還沒真正脫離成都外帶，但已經足夠讓流民、藏物和不願被盤問的人躲進去喘一口氣。",
      "sector_type": "SECT_FOREST",
      "cluster": "wild-fringe",
      "coord": [-2, -1, 0],
      "labels": ["forest-edge", "shade", "risk"],
      "exits": [
        { "direction": "north", "to": 19804 },
        { "direction": "east", "to": 19805 },
        { "direction": "south", "to": 19807 }
      ],
      "keywords": [
        {
          "keyword": "樹叢",
          "description": "幾叢壓低的灌木被踩出不太乾淨的小痕，像有人常在這裡停、躲，或是等著確認官道上的腳步是不是已經走遠。"
        }
      ],
      "enquires": ["林地", "樹叢", "流民"]
    },
    {
      "vnum": 19807,
      "name": "破亭營火",
      "description": "破亭只剩半邊歪木和一圈燒得不怎麼乾淨的火痕，既像流民夜裡借住的落腳點，也像某些不願讓官道看見的人暫時留下的影子。這裡讓成都近郊第一次露出一點秩序之外的灰色。",
      "sector_type": "SECT_FIELD",
      "cluster": "wild-fringe",
      "coord": [-2, -2, 0],
      "labels": ["campfire", "drifter", "gray-zone"],
      "exits": [
        { "direction": "north", "to": 19806 }
      ],
      "enquires": ["流民", "營火", "夜路"]
    },
    {
      "vnum": 19808,
      "name": "更西官道",
      "description": "再往西去，成都留下的牆影與旗號都開始淡成背景，只剩官道習慣還替旅人勉強維持方向感。這裡不像真正的終點，卻已經是都城正式把人交還給郊外與長路的地方。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-road",
      "coord": [-3, 0, 0],
      "labels": ["west-edge", "future-road", "departure"],
      "exits": [
        { "direction": "east", "to": 19804 }
      ],
      "enquires": ["更西", "遠路", "農路"]
    }
  ]
}
```
