# 北平郊區 (`beiping_outskirts`)

## Area Intent

`beiping_outskirts` 是 `beiping` 的第一圈北側外郊，承接玩家從主城前往北境邊線的第一段過渡帶。

第一輪落地目標：

- 城外哨卡與驛道主線
- 河灘補給支線
- 北境/白狼山方向的後續邊界預留

## Theme Positioning

- Theme: `軍旅風`
- Subtheme: `歷史城市風`
- LevelRange: `8-18`
- Parent area: `beiping`

## Suggested Layout

```text
北平獨樂寺(9001)
   |
[9101] 北門外哨卡 -- [9102] 驛道石坊 -- [9103] 旗亭路口 -- [9104] 永定河堤 -- [9108] 北境丘坡
                                         |
                                      [9106] 河灘貨棧
                                         |
                                      [9107] 河灘蘆葦帶

[9105] 邊關整隊場  (由 9103 往 north)
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "beiping_outskirts",
    "title": "北平郊區",
    "parent_area": "beiping",
    "design_notes": "北平北門外的軍旅驛道過渡區，先落地主線、補給支線與兩條後續 world link 邊界點。",
    "level_range": "8-18",
    "planned_vnum_range": "9101-9108",
    "theme": {
      "primary": "軍旅風",
      "secondary": "歷史城市風"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 9101,
        "target_area": "beiping",
        "target_room_vnum": 9001,
        "label": "獨樂寺"
      },
      {
        "direction": "north",
        "source_vnum": 9105,
        "target_area": "yijing_road",
        "label": "易京官道"
      },
      {
        "direction": "east",
        "source_vnum": 9108,
        "target_area": "bailang_mountain",
        "label": "白狼山前哨"
      }
    ],
    "clusters": [
      { "id": "gate-road", "label": "北門驛道主線" },
      { "id": "riverbank", "label": "永定河灘補給線" },
      { "id": "frontier", "label": "北境邊線前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 9101,
      "name": "北門外哨卡",
      "description": "厚實木柵與拒馬沿著城外官道排開，幾名北平守卒正輪流盤查出城行旅。南側還看得見獨樂寺的飛簷輪廓，往北則是筆直延伸的驛道，風裡帶著邊關塵土味。",
      "sector_type": "SECT_CITY",
      "cluster": "gate-road",
      "coord": [0, 0, 0],
      "labels": ["city-edge", "checkpoint", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 9001, "external": true },
        { "direction": "north", "to": 9102 }
      ],
      "enquires": ["回城", "北平"]
    },
    {
      "vnum": 9102,
      "name": "驛道石坊",
      "description": "官道旁立著一座舊石坊，坊額上仍能辨識出北境驛道四字。馬蹄與車轍在地面留下深淺不一的痕跡，顯示這條路白日從不停歇。",
      "sector_type": "SECT_CITY",
      "cluster": "gate-road",
      "coord": [0, 1, 0],
      "labels": ["main-road"],
      "exits": [
        { "direction": "south", "to": 9101 },
        { "direction": "north", "to": 9103 }
      ]
    },
    {
      "vnum": 9103,
      "name": "旗亭路口",
      "description": "一座高桿旗亭立在路口中央，紅黑兩色旗幟標示著邊哨方向與河堤支線。旅人通常在此決定是繼續北上，還是先往東補給再走。",
      "sector_type": "SECT_CITY",
      "cluster": "gate-road",
      "coord": [0, 2, 0],
      "labels": ["junction", "enquire"],
      "exits": [
        { "direction": "south", "to": 9102 },
        { "direction": "north", "to": 9105 },
        { "direction": "east", "to": 9104 }
      ],
      "enquires": ["易京", "河堤"]
    },
    {
      "vnum": 9104,
      "name": "永定河堤",
      "description": "河堤由夯土與碎石層層壘成，遠處可見渡船與拉纜木樁。水聲壓過人語，讓這裡比官道顯得更濕冷也更空曠。",
      "sector_type": "SECT_FIELD",
      "cluster": "riverbank",
      "coord": [1, 2, 0],
      "labels": ["riverbank"],
      "exits": [
        { "direction": "west", "to": 9103 },
        { "direction": "east", "to": 9108 },
        { "direction": "south", "to": 9106 }
      ]
    },
    {
      "vnum": 9105,
      "name": "邊關整隊場",
      "description": "一片被反覆踩實的土場供巡隊整隊換班，長矛架與拒馬整齊排在北緣。再往前就是更偏遠的邊境官道，許多傳聞都從那頭吹進北平。",
      "sector_type": "SECT_FIELD",
      "cluster": "frontier",
      "coord": [0, 3, 0],
      "labels": ["frontier", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 9103 }
      ],
      "enquires": ["邊關", "官道"]
    },
    {
      "vnum": 9106,
      "name": "河灘貨棧",
      "description": "幾間臨時搭起的木棚靠在河灘高處，堆著鹽包、草料與粗麻袋。看守貨棧的老兵一邊記帳，一邊盯著過往可疑身影。",
      "sector_type": "SECT_FIELD",
      "cluster": "riverbank",
      "coord": [1, 1, 0],
      "labels": ["supply"],
      "exits": [
        { "direction": "north", "to": 9104 },
        { "direction": "south", "to": 9107 }
      ]
    },
    {
      "vnum": 9107,
      "name": "河灘蘆葦帶",
      "description": "濕地裡長滿半人高的蘆葦，泥地踩下去會發出黏滯的聲響。偶爾有黑影在蘆葦深處閃動，像是躲避巡檢的流匪或偷渡客。",
      "sector_type": "SECT_FIELD",
      "cluster": "riverbank",
      "coord": [1, 0, 0],
      "labels": ["ambush"],
      "exits": [
        { "direction": "north", "to": 9106 }
      ]
    },
    {
      "vnum": 9108,
      "name": "北境丘坡",
      "description": "地勢在這裡抬升成起伏丘坡，碎石路往東延伸到更荒涼的山前地帶。站在坡頂回望，北平城郭只剩一條模糊灰線。",
      "sector_type": "SECT_HILLS",
      "cluster": "frontier",
      "coord": [2, 2, 0],
      "labels": ["hills", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 9104 }
      ],
      "enquires": ["白狼山"]
    }
  ]
}
```
