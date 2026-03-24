# 北境邊道 (`road_north_border`)

## Area Intent

`road_north_border` 承接 `city_xiangping` 的北境邊道路口，把遼東邊城的整補與分流節奏，正式送上一段帶著驛牌、路亭與盤查氣味的北地軍旅 road。這裡不是再做一塊開闊 wild，而是一段讓玩家明顯感到自己正從襄平秩序走向更遠北境的長路 connector。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `往更北疆道`
- LevelRange: `34-46`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_north_border",
    "title": "北境邊道",
    "design_notes": "第一版 spec-first 草案。先固定襄平北境邊道路口外的驛牌、官道中段、盤查側棚、路亭歇腳點與更北坡口，讓襄平的第二條北向分流正式成形。",
    "level_range": "34-46",
    "planned_vnum_range": "18501-18520",
    "reserved_room_block": "18501-18520",
    "theme": {
      "primary": "軍旅",
      "secondary": "往更北疆道"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 18501,
        "target_area": "city_xiangping",
        "label": "襄平北境邊道路口"
      }
    ],
    "clusters": [
      { "id": "south-approach", "label": "襄平外邊道路口" },
      { "id": "midway-road", "label": "官道中段" },
      { "id": "rest-stop", "label": "路亭歇腳點" },
      { "id": "north-reach", "label": "更北邊道前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 18501,
      "name": "北境邊道路口",
      "description": "一離開襄平的北境邊道路口，城中的規矩與人聲就被拉成背後的依靠，而不是眼前的主體。這裡像一條真正往更北邊境送人的起點，讓人很清楚知道自己不再只是出城，而是正式踏上長路。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 18309, "external": true },
        { "direction": "north", "to": 18502 }
      ],
      "enquires": ["襄平", "邊道", "出城"]
    },
    {
      "vnum": 18502,
      "name": "驛牌木樁邊",
      "description": "一面驛牌和幾根磨損木樁把這裡標成常有人馬短停整裝的位置。與開闊平原不同，這條路更強調秩序、盤點與下一站的意識，像是在提醒你北境旅途從來不是隨便走走而已。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 1, 0],
      "labels": ["waypoint", "marker"],
      "exits": [
        { "direction": "south", "to": 18501 },
        { "direction": "north", "to": 18503 }
      ],
      "keywords": [
        {
          "keyword": "驛牌",
          "description": "驛牌上的墨字已被風砂磨淡，卻仍能看出這條路是往更北邊境去的正式官道。"
        }
      ],
      "enquires": ["驛牌", "木樁", "下一站"]
    },
    {
      "vnum": 18503,
      "name": "北境官道中段",
      "description": "官道在這裡被車痕和軍靴踩得更實，讓路本身像一道明確的秩序線穿過北地。走在這裡時，會感到襄平雖然還不算遠，但旅途的主角已經從城市生活換成路況、盤查和前方傳聞。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "northbound"],
      "exits": [
        { "direction": "south", "to": 18502 },
        { "direction": "north", "to": 18505 },
        { "direction": "east", "to": 18504 }
      ],
      "enquires": ["官道", "去路", "北邊"]
    },
    {
      "vnum": 18504,
      "name": "盤查側棚",
      "description": "道旁立著一處簡陋側棚，棚下有翻看的包袱痕和短暫盤問後留下的凌亂腳印。這裡讓整條邊道更像一條帶著軍務戒心的路，而不是單純方便旅人往返的通道。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["side-line", "inspection"],
      "exits": [
        { "direction": "west", "to": 18503 }
      ],
      "enquires": ["盤查", "側棚", "過客"]
    },
    {
      "vnum": 18505,
      "name": "路亭前坪",
      "description": "路亭前坪稍微把長路上的硬氣收住一些，讓驛卒、押貨人和要往北去的旅人能在這裡交換消息。人聲不多，但每一句談話幾乎都和前方天候、路況或可疑動靜有關。",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "south", "to": 18503 },
        { "direction": "enter", "to": 18506 },
        { "direction": "north", "to": 18507 }
      ],
      "enquires": ["路亭", "歇腳", "消息"]
    },
    {
      "vnum": 18506,
      "name": "路亭內",
      "description": "亭內擺著長凳、粗茶桶和掛在壁上的舊木牌，給人一種勉強足夠的安穩。這裡不是要讓人久留，而是讓人把腳步、方向和膽氣重新整好，再決定是否繼續往更北的邊道走。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 18505 }
      ],
      "enquires": ["木牌", "茶水"]
    },
    {
      "vnum": 18507,
      "name": "北風哨坡",
      "description": "地勢在這裡稍稍抬高，讓前方道路與更北的空線都被拉得更清楚。風裡常夾著比襄平更硬冷的味道，使人明白這條邊道再往前走，就真的會逐漸遠離邊城的庇護。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-reach",
      "coord": [0, 4, 0],
      "labels": ["northbound", "lookout"],
      "exits": [
        { "direction": "south", "to": 18505 },
        { "direction": "north", "to": 18508 }
      ],
      "enquires": ["北風", "前面", "坡口"]
    },
    {
      "vnum": 18508,
      "name": "更北邊道口",
      "description": "道面在這裡繼續往更北方舒展出去，車痕和行腳印都證明這不是一條偶然的土路，而是一條還會把人送得更遠的正式邊道。它像一個未完的承諾，提醒你襄平之北還有更大的邊境世界等待落成。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-reach",
      "coord": [0, 5, 0],
      "labels": ["north-edge", "forward"],
      "exits": [
        { "direction": "south", "to": 18507 }
      ],
      "enquires": ["更北", "邊境", "去向"]
    }
  ]
}
```
