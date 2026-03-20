# 水軍大營 (`fort_naval_base`)

## Area Intent

`fort_naval_base` 承接 `wild_pirate_islands` 東向暗棧，把玩家從碎島與海寇殘留秩序，拉進一段由軍門、棧寨、軍需棚、望樓與內港碼頭構成的東吳水軍關卡。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `東吳水軍`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_naval_base",
    "title": "水軍大營",
    "design_notes": "第一版 spec-first 草案。先固定外海暗棧、棧門柵關、補給棚區、望樓高位與內港碼頭，把群島海路正式收束成受軍令控制的海防關卡。",
    "level_range": "100-100",
    "planned_vnum_range": "15901-15930",
    "reserved_room_block": "15901-15930",
    "theme": {
      "primary": "軍旅",
      "secondary": "東吳水軍"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 15901,
        "target_area": "wild_pirate_islands",
        "label": "東向暗棧"
      },
      {
        "direction": "north",
        "source_vnum": 15910,
        "target_area": "city_jianye",
        "label": "建業水門"
      },
      {
        "direction": "south",
        "source_vnum": 15912,
        "target_area": "sea_naval_patrol",
        "label": "外海巡防"
      }
    ],
    "clusters": [
      { "id": "outer-pier", "label": "外棧入口" },
      { "id": "gate-line", "label": "棧門柵關" },
      { "id": "supply-yard", "label": "軍需棚區" },
      { "id": "watch-rise", "label": "望樓高位" },
      { "id": "inner-dock", "label": "內港碼頭" }
    ]
  },
  "rooms": [
    {
      "vnum": 15901,
      "name": "外棧關口",
      "description": "暗棧盡頭的木板忽然被加厚、釘鐵與柵柱接手，像群島那頭還講求膽量與眼色，到了這裡則完全改由誰能發令來決定。光是站在關口前，你就能感覺到海風都像被軍規收緊了幾分。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-pier",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-link"],
      "exits": [
        { "direction": "west", "to": 15812, "external": true },
        { "direction": "east", "to": 15903 },
        { "direction": "south", "to": 15902 }
      ],
      "enquires": ["關口", "西邊", "水軍"]
    },
    {
      "vnum": 15902,
      "name": "巡纜側道",
      "description": "一道沿著纜樁與外牆延伸的側道讓巡兵能快速查看外棧和繩索狀況，路不寬，卻處處是為了效率而留下的乾脆痕跡。這裡不像給人閒晃的地方，而像連停步都得有理由。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-pier",
      "coord": [0, -1, 0],
      "labels": ["side-lane", "ropes"],
      "exits": [
        { "direction": "north", "to": 15901 }
      ],
      "enquires": ["巡邏", "纜繩"]
    },
    {
      "vnum": 15903,
      "name": "棧門柵關",
      "description": "幾層粗木與鐵條構成的柵關把海上的隨意感徹底截住，只留下受控通行的一條正道。站在這裡時，你會很明白這座水軍營不是為了歡迎人，而是為了篩掉不該靠近的人。 ",
      "sector_type": "SECT_CITY",
      "cluster": "gate-line",
      "coord": [1, 0, 0],
      "labels": ["gate", "checkpoint"],
      "exits": [
        { "direction": "west", "to": 15901 },
        { "direction": "east", "to": 15904 }
      ],
      "enquires": ["柵門", "通行"]
    },
    {
      "vnum": 15904,
      "name": "前營通道",
      "description": "通道兩旁插著軍旗與告示板，步距、轉角和視線都像被事先算過，讓人走在其中時很難不跟著營內節奏一起變得更拘束。這裡沒有任何多餘的東西，因為多餘本身就是問題。 ",
      "sector_type": "SECT_CITY",
      "cluster": "gate-line",
      "coord": [2, 0, 0],
      "labels": ["mainline", "flags"],
      "exits": [
        { "direction": "west", "to": 15903 },
        { "direction": "east", "to": 15908 },
        { "direction": "north", "to": 15906 },
        { "direction": "south", "to": 15905 }
      ],
      "enquires": ["軍旗", "內營"]
    },
    {
      "vnum": 15905,
      "name": "補給棚前",
      "description": "幾座臨海棚架把乾糧、淡水、燈具與繩索分門別類收得整整齊齊，像這座大營真正的力量不只在兵刃，也在它有能力讓整個海防節奏一直轉下去。這裡比群島上的任何藏貨點都更讓人明白什麼叫後勤。 ",
      "sector_type": "SECT_CITY",
      "cluster": "supply-yard",
      "coord": [1, -1, 0],
      "labels": ["supplies", "yard"],
      "exits": [
        { "direction": "north", "to": 15904 }
      ],
      "enquires": ["補給", "乾糧"]
    },
    {
      "vnum": 15906,
      "name": "望樓梯口",
      "description": "梯口邊的木牌與鐵鉤都在提醒人這裡不是隨便能上的地方，但也正因如此，更能看出這座營寨對視野與預警有多重視。只要往上走，整條海路與群島都會被重新解讀成軍事情勢。 ",
      "sector_type": "SECT_CITY",
      "cluster": "watch-rise",
      "coord": [2, 1, 0],
      "labels": ["stairs", "watch"],
      "exits": [
        { "direction": "south", "to": 15904 },
        { "direction": "up", "to": 15911 }
      ],
      "enquires": ["望樓", "上面"]
    },
    {
      "vnum": 15908,
      "name": "內營號台",
      "description": "號台立在前營與內港之間，既能讓軍令往前推，也能讓戰報往裡收，像整座水軍大營真正的心跳都在這種不容拖延的傳遞裡。你站在這裡時，很難不被那股被命令驅動的節奏一起帶快。 ",
      "sector_type": "SECT_CITY",
      "cluster": "inner-dock",
      "coord": [3, 0, 0],
      "labels": ["signal", "core"],
      "exits": [
        { "direction": "west", "to": 15904 },
        { "direction": "east", "to": 15910 }
      ],
      "enquires": ["號台", "軍令", "南邊"]
    },
    {
      "vnum": 15910,
      "name": "內港水門",
      "description": "內港水門後方的水道比外海平穩得多，但那平穩不是天生，而是被整座軍營硬生生管出來的。這裡既像回到文明，也像更深入權力真正駐紮的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "inner-dock",
      "coord": [3, -1, 0],
      "labels": ["north-link", "dock"],
      "exits": [
        { "direction": "north", "to": 16001, "external": true },
        { "direction": "west", "to": 15908 },
        { "direction": "south", "to": 15912 }
      ],
      "enquires": ["建業", "水門", "北邊"]
    },
    {
      "vnum": 15911,
      "name": "外海望樓",
      "description": "站上望樓後，群島、沉舟帶與更遠的外海都被納進一種軍事視角裡，連原本看似自由的航線也只剩下可守、可巡或可疑三種判讀。這種高度讓人不是更放鬆，而是更清楚自己正處在誰的視線裡。 ",
      "sector_type": "SECT_CITY",
      "cluster": "watch-rise",
      "coord": [2, 1, 1],
      "labels": ["tower", "lookout"],
      "exits": [
        { "direction": "down", "to": 15906 }
      ],
      "enquires": ["外海", "望樓", "旗號"]
    },
    {
      "vnum": 15912,
      "name": "南巡碼頭",
      "description": "碼頭南側繫著幾艘隨時能放出的巡防快船，木板被軍靴與海水磨得發亮，像這裡每一天都在準備下一次出巡。和群島那種半野的漂流感比起來，這裡連海浪都像被納進了值勤表。 ",
      "sector_type": "SECT_CITY",
      "cluster": "inner-dock",
      "coord": [4, -1, 0],
      "labels": ["south-edge", "patrol"],
      "exits": [
        { "direction": "north", "to": 15910 }
      ],
      "enquires": ["巡防", "南邊", "碼頭"]
    }
  ]
}
```
