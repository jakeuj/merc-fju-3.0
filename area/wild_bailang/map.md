# 白狼山 (`wild_bailang`)

## Area Intent

`wild_bailang` 承接 `fort_yijing` 的東側寨牆，把北境軍鎮外的視野正式打開成更冷、更荒、也更帶異族與傳說氣味的山前野外。這裡不該只是易京外再多一段路，而是要把節奏從軍令秩序切換成風裂山徑、狼煙岔脊、可疑裂縫與更深山帶預留交錯的探險型 wild 節點。

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `山前異域`
- LevelRange: `30-42`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_bailang",
    "title": "白狼山",
    "design_notes": "第一版 spec-first 草案。先固定山前出牆口、碎石坡、風裂石徑、狼煙岔脊、風蝕石壇、裂縫洞口、東向荒徑與北狼隘口，把易京東界正式展成白狼山前帶的 wild 節點。",
    "level_range": "30-42",
    "planned_vnum_range": "18001-18020",
    "reserved_room_block": "18001-18020",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "山前異域"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 18001,
        "target_area": "fort_yijing",
        "target_room_vnum": 17908,
        "label": "東側寨牆"
      },
      {
        "direction": "north",
        "source_vnum": 18008,
        "target_area": "wild_wolf_forest",
        "target_room_vnum": 18701,
        "label": "狼林方向"
      },
      {
        "direction": "down",
        "source_vnum": 18006,
        "target_area": "dng_ancient_cave",
        "label": "古洞遺跡"
      },
      {
        "direction": "east",
        "source_vnum": 18007,
        "target_area": "wild_barbarian_camp",
        "target_room_vnum": 18201,
        "label": "胡營舊地方向"
      },
      {
        "direction": "up",
        "source_vnum": 18005,
        "target_area": "sec_starfall_crater",
        "label": "星墜天坑預留"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "山前入口帶" },
      { "id": "ridge", "label": "風裂山脊" },
      { "id": "landmark", "label": "石壇與裂縫" },
      { "id": "frontier", "label": "更深北東前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 18001,
      "name": "山前出牆口",
      "description": "一離開易京東側寨牆，腳下的土色與風感就立刻變了。軍鎮的秩序還在背後撐著膽氣，可眼前已經是更荒更冷的山前地帶，連空氣都像在提醒人別把這裡當普通郊野。",
      "sector_type": "SECT_HILLS",
      "cluster": "entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 17908, "external": true },
        { "direction": "east", "to": 18002 }
      ],
      "enquires": ["易京", "白狼山", "回去"]
    },
    {
      "vnum": 18002,
      "name": "山前碎石坡",
      "description": "碎石坡被冷風一層層削過，踩起來既鬆又響，讓人很難在這裡藏住腳步。往北可見更高的脊線，往東則是更像被風長年撕裂過的山徑。",
      "sector_type": "SECT_HILLS",
      "cluster": "entry",
      "coord": [1, 0, 0],
      "labels": ["slope", "transition"],
      "exits": [
        { "direction": "west", "to": 18001 },
        { "direction": "east", "to": 18003 },
        { "direction": "north", "to": 18004 }
      ],
      "enquires": ["山路", "風", "前面"]
    },
    {
      "vnum": 18003,
      "name": "風裂石徑",
      "description": "石徑邊緣裂出一道道乾硬縫隙，像是多年北風吹出來的傷口。站在這裡時，軍鎮留下的安全感已經退到背後，只剩山裡的未知慢慢往前壓。",
      "sector_type": "SECT_HILLS",
      "cluster": "ridge",
      "coord": [2, 0, 0],
      "labels": ["stone-path", "exposed"],
      "exits": [
        { "direction": "west", "to": 18002 },
        { "direction": "east", "to": 18007 },
        { "direction": "south", "to": 18006 }
      ],
      "enquires": ["石徑", "裂縫", "東邊"]
    },
    {
      "vnum": 18004,
      "name": "狼煙岔脊",
      "description": "脊線上還留著早年燃過狼煙的黑痕，讓這裡既像古老警點，又像邊地傳說會停下來回頭看人的地方。從這裡往北看去，山勢與林帶都顯得更深。",
      "sector_type": "SECT_HILLS",
      "cluster": "ridge",
      "coord": [1, 1, 0],
      "labels": ["junction", "northbound"],
      "exits": [
        { "direction": "south", "to": 18002 },
        { "direction": "north", "to": 18008 },
        { "direction": "west", "to": 18005 }
      ],
      "enquires": ["狼煙", "北邊", "岔路"]
    },
    {
      "vnum": 18005,
      "name": "風蝕石壇",
      "description": "一座被風蝕得稜角模糊的石壇立在坡脊旁，壇面上殘留的刻痕不像中原軍物，也不像尋常山民會留下的東西。這裡有一種讓人想多看兩眼又不太敢久留的古怪感。",
      "sector_type": "SECT_HILLS",
      "cluster": "landmark",
      "coord": [0, 1, 0],
      "labels": ["landmark", "world-link-up"],
      "exits": [
        { "direction": "east", "to": 18004 }
      ],
      "enquires": ["石壇", "刻痕", "天上"]
    },
    {
      "vnum": 18006,
      "name": "裂縫洞口",
      "description": "地面上的裂痕在這裡忽然收成一道真正的洞口，冷風從下方往外滲，帶著明顯不是地表該有的濕冷氣味。站在邊上時，會很自然懷疑下面還藏著更舊的東西。",
      "sector_type": "SECT_HILLS",
      "cluster": "landmark",
      "coord": [2, -1, 0],
      "labels": ["cave-mouth", "world-link-down"],
      "exits": [
        { "direction": "north", "to": 18003 },
        { "direction": "down", "to": 18101, "external": true }
      ],
      "enquires": ["洞口", "下面", "古洞"]
    },
    {
      "vnum": 18007,
      "name": "東向荒徑",
      "description": "荒徑朝東延去，路跡不像官道那樣清楚，卻能從踩踏痕與斷草方向看出仍有人在往那頭走。那種不是軍隊、也不像一般旅人的去向，讓東邊多了一層異樣感。",
      "sector_type": "SECT_HILLS",
      "cluster": "frontier",
      "coord": [3, 0, 0],
      "labels": ["east-edge", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 18003 },
        { "direction": "east", "to": 18201, "external": true }
      ],
      "enquires": ["東邊", "胡營", "荒徑"]
    },
    {
      "vnum": 18008,
      "name": "北狼隘口",
      "description": "脊線在這裡收成一道狹窄隘口，風從更北邊的林帶與坡谷一路灌進來，帶著狼群與深山都還沒完全露面的消息。這裡不像終點，更像真正進入白狼山深處前的最後提醒。",
      "sector_type": "SECT_HILLS",
      "cluster": "frontier",
      "coord": [1, 2, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 18004 },
        { "direction": "north", "to": 18701, "external": true }
      ],
      "enquires": ["狼林", "隘口", "北路"]
    }
  ]
}
```
