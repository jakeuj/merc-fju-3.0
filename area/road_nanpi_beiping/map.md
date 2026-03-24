# 河北北道 (`road_nanpi_beiping`)

## Area Intent

`road_nanpi_beiping` 承接 `city_nanpi` 北道牌樓，把河北主城節奏重新放長成往北平去的官道旅程。這裡不是另一座城市，也不是純野外，而是一段帶著路亭、驛牌與北地旅訊流動感的長路 connector。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `往北平官道`
- LevelRange: `24-36`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_nanpi_beiping",
    "title": "河北北道",
    "design_notes": "第一版 spec-first 草案。先固定南口北道、官道路段、里程石側線、路亭歇腳點與更北的北平方向，把南皮的北路正式接成可實作的 road 節點。",
    "level_range": "24-36",
    "planned_vnum_range": "17701-17720",
    "reserved_room_block": "17701-17720",
    "theme": {
      "primary": "歷史城市",
      "secondary": "往北平官道"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 17701,
        "target_area": "city_nanpi",
        "label": "南皮北道口"
      },
      {
        "direction": "north",
        "source_vnum": 17708,
        "target_area": "city_beiping",
        "label": "北平方向"
      }
    ],
    "clusters": [
      { "id": "south-approach", "label": "南口北道" },
      { "id": "midway-road", "label": "官道中段" },
      { "id": "rest-stop", "label": "路亭歇腳點" },
      { "id": "north-approach", "label": "北向延伸帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17701,
      "name": "南皮北道口",
      "description": "一離開南皮北道牌樓，城市的煙火氣就慢慢被北地長路的空闊感取代。這裡仍留著地方主城的秩序餘韻，卻已經更像一段真正會把人送往更北之地的起點。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 17409, "external": true },
        { "direction": "north", "to": 17702 }
      ],
      "enquires": ["南皮", "北道", "出城"]
    },
    {
      "vnum": 17702,
      "name": "官道木樁旁",
      "description": "木樁與馬索痕把這裡標成長年有人馬整裝的固定停手點。再往北走，路感會愈來愈明顯，讓人很難再把自己當成只是站在南皮城外打轉。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 1, 0],
      "labels": ["waypoint", "roadside"],
      "exits": [
        { "direction": "south", "to": 17701 },
        { "direction": "north", "to": 17703 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁被繩索反覆磨亮，看得出這條北道長久以來一直都是車馬北行的重要停整點。"
        }
      ],
      "enquires": ["木樁", "旅隊"]
    },
    {
      "vnum": 17703,
      "name": "河北北道中段",
      "description": "官道在這裡筆直向前延展，兩側地勢與風線都讓方向感變得更加單純也更加漫長。走在這裡時，會清楚知道自己已經離開南皮的城市節奏，真正進入北地旅途。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "open-way"],
      "exits": [
        { "direction": "south", "to": 17702 },
        { "direction": "north", "to": 17705 },
        { "direction": "east", "to": 17704 }
      ],
      "enquires": ["官道", "北平", "下一站"]
    },
    {
      "vnum": 17704,
      "name": "里程石側線",
      "description": "一座略顯斑駁的里程石立在道旁，石面上的字跡被風磨得有些發淺，卻仍保留著指向北平的方向感。對長路旅人來說，這類石頭就是能讓心神穩住的證據。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["marker", "route-info"],
      "exits": [
        { "direction": "west", "to": 17703 }
      ],
      "enquires": ["里程石", "方向"]
    },
    {
      "vnum": 17705,
      "name": "路亭前坪",
      "description": "路亭前坪把長路上的緊繃稍微鬆開一點，讓驛卒、旅客與押貨人都能在這裡調整腳步。有人低聲談論更北邊的天候與路況，使這裡像是把整條北道消息暫時收束起來的節點。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "south", "to": 17703 },
        { "direction": "enter", "to": 17706 },
        { "direction": "north", "to": 17707 }
      ],
      "enquires": ["路亭", "歇腳", "消息"]
    },
    {
      "vnum": 17706,
      "name": "路亭內",
      "description": "亭內擺著長凳、粗茶桶與掛在牆上的驛牌，給人一種薄薄的安穩感。這裡不是停留很久的地方，卻足夠讓人重新把方向和心緒都整好，再繼續往北。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 17705 }
      ],
      "enquires": ["驛牌", "茶水"]
    },
    {
      "vnum": 17707,
      "name": "北向坡口",
      "description": "地勢在這裡微微往北抬起，讓路上的視線也跟著拉長。站在這裡時，會覺得南皮已經成了後方的支點，而更北的城鎮與邊地消息才是現在真正要接近的方向。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 4, 0],
      "labels": ["northbound", "staging"],
      "exits": [
        { "direction": "south", "to": 17705 },
        { "direction": "north", "to": 17708 }
      ],
      "enquires": ["北邊", "去路", "坡口"]
    },
    {
      "vnum": 17708,
      "name": "北行官道口",
      "description": "官道在此繼續往北舒展，路面的車痕和行腳痕跡讓人很清楚知道，這並不是一條偶然被踩出來的小路，而是一條持續把人送往更北城市的正式路線。站在這裡時，旅途感比任何時候都更強。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 5, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 17707 },
        { "direction": "north", "to": 9059, "external": true }
      ],
      "enquires": ["北路", "北平", "去向"]
    }
  ]
}
```
