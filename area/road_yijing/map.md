# 易京官道 (`road_yijing`)

## Area Intent

`road_yijing` 承接 `beiping_outskirts` 的邊關整隊場，把北平外緣的官道正式推進成更有軍旅與邊境換班氣味的北方驛道。這裡不再只是一般長路，而是一段讓旅人、巡隊與押運者都逐漸意識到自己正在靠近北境據點的軍旅 connector。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `北方驛道`
- LevelRange: `22-32`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_yijing",
    "title": "易京官道",
    "design_notes": "第一版 spec-first 草案。先固定北平外緣的整隊場、石坊驛道、換班坡口、路亭歇腳點與更北的易京方向，把 beiping_outskirts 的北向 world link 正式展成可實作的軍旅 road 節點。",
    "level_range": "22-32",
    "planned_vnum_range": "17801-17820",
    "reserved_room_block": "17801-17820",
    "theme": {
      "primary": "軍旅",
      "secondary": "北方驛道"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 17801,
        "target_area": "beiping_outskirts",
        "label": "邊關整隊場"
      },
      {
        "direction": "north",
        "source_vnum": 17808,
        "target_area": "fort_yijing",
        "label": "易京方向"
      }
    ],
    "clusters": [
      { "id": "south-approach", "label": "北境起行帶" },
      { "id": "midway-road", "label": "驛道路段" },
      { "id": "rest-stop", "label": "路亭歇腳點" },
      { "id": "north-approach", "label": "易京前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17801,
      "name": "北境整隊口",
      "description": "一離開北平郊區的整隊場，官道上的氣味就明顯變了。這裡還看得見巡隊踩出的硬土地痕，卻已經更像一段真正會把人送往北境據點的起行口。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 17802 }
      ],
      "enquires": ["北平", "整隊", "出發"]
    },
    {
      "vnum": 17802,
      "name": "驛道石坊",
      "description": "一座舊石坊立在道旁，坊角被多年風雪磨鈍，卻仍撐著北境驛道的門面。從這裡開始，旅人與差役都會自然把腳步收成更適合長程軍路的節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 1, 0],
      "labels": ["waypoint", "marker"],
      "exits": [
        { "direction": "south", "to": 17801 },
        { "direction": "north", "to": 17803 }
      ],
      "enquires": ["石坊", "驛道"]
    },
    {
      "vnum": 17803,
      "name": "北地驛道中段",
      "description": "驛道在這裡拉得筆直，兩側地勢開闊卻不再像單純平野。風裡常夾著巡隊換班的動靜與北邊傳來的零散消息，讓人清楚知道自己正一步步往邊境靠近。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "open-way"],
      "exits": [
        { "direction": "south", "to": 17802 },
        { "direction": "north", "to": 17805 },
        { "direction": "east", "to": 17804 }
      ],
      "enquires": ["去路", "易京", "北邊"]
    },
    {
      "vnum": 17804,
      "name": "換班木樁旁",
      "description": "幾根磨損的木樁立在側線旁，看得出巡隊與驛馬常在這裡短暫換手整裝。木樁本身不起眼，卻像是整條路能一直維持秩序流動的小證據。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["side-line", "relay"],
      "exits": [
        { "direction": "west", "to": 17803 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁上留著馬索與繩結磨出的痕跡，顯示這裡長期被拿來作為換班與整裝的小停點。"
        }
      ],
      "enquires": ["木樁", "換班"]
    },
    {
      "vnum": 17805,
      "name": "路亭前坪",
      "description": "路亭前坪讓長路上的緊繃稍微鬆開一些，幾名驛卒與行旅正低聲交換路況和北境傳聞。這裡不像大城驛站那樣熱鬧，卻更有一種真正邊線前帶的實用氣味。",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "south", "to": 17803 },
        { "direction": "enter", "to": 17806 },
        { "direction": "north", "to": 17807 }
      ],
      "enquires": ["路亭", "消息", "歇腳"]
    },
    {
      "vnum": 17806,
      "name": "路亭內",
      "description": "亭內擺著長凳、粗布帳與掛在牆邊的舊路牌，讓人能在這裡稍微把風寒擋掉一點。留在這裡的人大多只是歇口氣，很少有人會把這裡當成真正安心的停留處。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 17805 }
      ],
      "enquires": ["路牌", "帳布"]
    },
    {
      "vnum": 17807,
      "name": "北向坡口",
      "description": "地勢在這裡微微抬升，讓前方的道路和更遠的北地輪廓都變得更清楚。越過這段坡口之後，官道的氣味就不再只是旅路，而更像正式進入軍鎮前帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 4, 0],
      "labels": ["northbound", "staging"],
      "exits": [
        { "direction": "south", "to": 17805 },
        { "direction": "north", "to": 17808 }
      ],
      "enquires": ["坡口", "前面", "易京"]
    },
    {
      "vnum": 17808,
      "name": "易京前路口",
      "description": "官道在此繼續往北伸展，地面上更密的車痕和巡隊腳印提醒人們，前方已經不是單純旅人往來之地，而是更接近軍鎮與勢力前線的路口。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 5, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 17807 }
      ],
      "enquires": ["易京", "北路", "前線"]
    }
  ]
}
```
