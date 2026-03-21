# 水底遺跡 (`sec_water_ruins`)

## Area Intent

`sec_water_ruins` 承接 `wild_pirate_islands` 外礁深灘下方的水府裂井，把玩家從外海群島的風、鹽與礁浪正式帶進一段更安靜、更壓迫也更帶異象感的水底殘宮。這裡不是單純的深水地形，而是把海路 wild 重新收束成需辨識光紋、裂井與沉殿節奏的江東 secret。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `水府遺跡 / 裂井殘宮`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_water_ruins",
    "title": "水底遺跡",
    "design_notes": "第一版 spec-first 草案。先固定裂井入口、沉殿甬道、光紋偏廊與殘宮核心，讓江東海路在群島 wild 之後轉入高風險水底 secret。",
    "level_range": "100-100",
    "planned_vnum_range": "16701-16730",
    "reserved_room_block": "16701-16730",
    "theme": {
      "primary": "仙俠",
      "secondary": "水府遺跡 / 裂井殘宮"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 16701,
        "target_area": "wild_pirate_islands",
        "label": "水府裂井"
      }
    ],
    "clusters": [
      { "id": "rift-entry", "label": "裂井入口" },
      { "id": "sunken-way", "label": "沉殿甬道" },
      { "id": "glyph-wing", "label": "光紋偏廊" },
      { "id": "core-sanctum", "label": "殘宮核心" }
    ]
  },
  "rooms": [
    {
      "vnum": 16701,
      "name": "裂井落點",
      "description": "從外礁深灘下沉後，最先看見的不是無盡黑水，而是一口被暗光照出的裂井落點。井壁像被某種古老力量從內側撐裂，讓人明白這裡雖在海底，卻不是自然形成的水穴。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "rift-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "up-link"],
      "exits": [
        { "direction": "up", "to": 15810, "external": true },
        { "direction": "south", "to": 16703 },
        { "direction": "east", "to": 16702 }
      ],
      "enquires": ["裂井", "上面", "去路"]
    },
    {
      "vnum": 16702,
      "name": "沉壁光痕",
      "description": "井壁旁殘著幾道像魚骨又像符篆的光痕，在水流裡一明一滅。它們不只照亮落點，也像在提醒後來者，真正的路不是看水勢，而是看這些還未完全熄去的古老指引。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "rift-entry",
      "coord": [1, 0, 0],
      "labels": ["glyph", "wall"],
      "exits": [
        { "direction": "west", "to": 16701 }
      ],
      "enquires": ["光痕", "井壁"]
    },
    {
      "vnum": 16703,
      "name": "沉殿前甬",
      "description": "水流在這條前甬裡忽然變得很慢，像整片海都到了這裡先收聲。前方石構仍看得出殿廊輪廓，只是所有棱角都被歲月和水壓磨得像一段已經不太肯開口的記憶。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "sunken-way",
      "coord": [0, 1, 0],
      "labels": ["hallway", "ante"],
      "exits": [
        { "direction": "north", "to": 16701 },
        { "direction": "south", "to": 16705 },
        { "direction": "west", "to": 16704 }
      ],
      "enquires": ["甬道", "沉殿", "前面"]
    },
    {
      "vnum": 16704,
      "name": "裂磚側穴",
      "description": "側穴裡滿是被水壓推倒的殘磚與碎柱，卻也因此讓人更容易發現這座遺跡並不是單層結構。很多不屬於主殿的痕跡都被推擠到這裡，像整個殘宮最不肯消失的旁證。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "glyph-wing",
      "coord": [-1, 1, 0],
      "labels": ["side-room", "debris"],
      "exits": [
        { "direction": "east", "to": 16703 },
        { "direction": "south", "to": 16706 }
      ],
      "enquires": ["裂磚", "側穴"]
    },
    {
      "vnum": 16705,
      "name": "殘宮迴水廊",
      "description": "一道半塌的迴廊把水流切成緩慢旋轉的暗帶，讓人分不清眼前是通路、屏風，還是某種仍在運作的古老守勢。站在這裡時，方向感比勇氣更像一種珍貴資源。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "sunken-way",
      "coord": [0, 2, 0],
      "labels": ["corridor", "current"],
      "exits": [
        { "direction": "north", "to": 16703 },
        { "direction": "east", "to": 16706 },
        { "direction": "south", "to": 16708 }
      ],
      "enquires": ["迴廊", "水流", "深處"]
    },
    {
      "vnum": 16706,
      "name": "光紋偏廊",
      "description": "偏廊地面還留著連成一線的光紋，像某種早已沉睡的儀式路徑仍在水底微微呼吸。它不像正門那樣顯眼，卻更像真正懂路的人會選擇的地方。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "glyph-wing",
      "coord": [1, 2, 0],
      "labels": ["glyph-path", "wing"],
      "exits": [
        { "direction": "west", "to": 16705 },
        { "direction": "north", "to": 16704 }
      ],
      "enquires": ["光紋", "偏廊"]
    },
    {
      "vnum": 16708,
      "name": "殘宮核心",
      "description": "核心空間已看不出完整殿制，只剩斷柱、沉座與一道像祭壇又像封口的中樞殘構。海水在這裡安靜得近乎不自然，像整座遺跡真正想留下的東西，都還藏在這片靜壓裡。",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "core-sanctum",
      "coord": [0, 3, 0],
      "labels": ["core", "sanctum"],
      "exits": [
        { "direction": "north", "to": 16705 }
      ],
      "enquires": ["核心", "祭壇", "殘宮"]
    }
  ]
}
```
