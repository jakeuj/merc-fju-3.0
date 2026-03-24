# 北方哨樓 (`fort_northern_watch`)

## Area Intent

`fort_northern_watch` 承接 `fort_yijing` 的北望樓，把北境軍鎮再往上一層推成更純粹的哨站與狼煙 watch fort。這裡不是另一座完整軍城，而是一處讓玩家明顯感到自己正站在更高、更冷、也更靠近前線的位置上的北方哨樓。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `哨站 / 狼煙`
- LevelRange: `36-48`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_northern_watch",
    "title": "北方哨樓",
    "design_notes": "第一版 spec-first 草案。先固定易京北望樓上方的升梯接臺、哨樓外臺、北哨柵門、主層木廊、軍令木案、糧箭棚與狼煙高臺，讓北境 watch fort 正式成形。",
    "level_range": "36-48",
    "planned_vnum_range": "18601-18620",
    "reserved_room_block": "18601-18620",
    "theme": {
      "primary": "軍旅",
      "secondary": "哨站 / 狼煙"
    },
    "world_links": [
      {
        "direction": "down",
        "source_vnum": 18601,
        "target_area": "fort_yijing",
        "label": "易京北望樓"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "升梯與外臺" },
      { "id": "gate", "label": "北哨柵門" },
      { "id": "core", "label": "主層與軍令帶" },
      { "id": "watch", "label": "狼煙高臺" }
    ]
  },
  "rooms": [
    {
      "vnum": 18601,
      "name": "升梯接臺",
      "description": "自易京北望樓再往上攀，腳下木梯與風聲很快就把人和下方軍鎮拉開距離。站上接臺時，最先感受到的不是視野，而是前線 watch fort 那種不容鬆懈的空氣。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 0, 1],
      "labels": ["entry", "down-edge", "world-link-down", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 17907, "external": true },
        { "direction": "north", "to": 18602 }
      ],
      "enquires": ["易京", "下去", "哨樓"]
    },
    {
      "vnum": 18602,
      "name": "哨樓外臺",
      "description": "外臺比下方望樓更窄，也更直接暴露在北風裡，讓每一步都像是在提醒你這裡不是給人久站觀景的地方。真正留在此處的人，多半都有明確的軍務或巡望責任。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 1, 1],
      "labels": ["outer-platform", "wind"],
      "exits": [
        { "direction": "south", "to": 18601 },
        { "direction": "north", "to": 18603 }
      ],
      "enquires": ["外臺", "北風"]
    },
    {
      "vnum": 18603,
      "name": "北哨柵門",
      "description": "一道較矮卻更厚實的柵門把哨樓真正的內外分開，讓任何踏進來的人都像被迫接受一次無聲盤查。這裡的壓力不是來自人多，而是來自每一件設施都只為戒備而存在。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [0, 2, 1],
      "labels": ["gate", "checkpoint"],
      "exits": [
        { "direction": "south", "to": 18602 },
        { "direction": "north", "to": 18604 }
      ],
      "enquires": ["柵門", "盤查", "放行"]
    },
    {
      "vnum": 18604,
      "name": "哨樓主層",
      "description": "主層木廊把軍令、糧箭與巡望動線全都收在一起，形成一種高處 watch fort 特有的緊湊秩序。站在這裡時，會很清楚感到這座哨樓的存在目的只有一個：比下方更早看見邊境變化。",
      "sector_type": "SECT_CITY",
      "cluster": "core",
      "coord": [0, 3, 1],
      "labels": ["core", "military-flow"],
      "exits": [
        { "direction": "south", "to": 18603 },
        { "direction": "west", "to": 18605 },
        { "direction": "east", "to": 18606 },
        { "direction": "up", "to": 18607 }
      ],
      "enquires": ["主層", "軍令", "狼煙"]
    },
    {
      "vnum": 18605,
      "name": "軍令木案側",
      "description": "厚木案上壓著巡望簿、交接木牌與幾封待命的軍令，使這裡比想像中更安靜，也更有一種不能出錯的冷硬感。很多真正改變前線動向的命令，在這裡看起來都只是幾行字。",
      "sector_type": "SECT_CITY",
      "cluster": "core",
      "coord": [-1, 3, 1],
      "labels": ["orders", "briefing"],
      "exits": [
        { "direction": "east", "to": 18604 }
      ],
      "enquires": ["軍令", "簿冊", "交接"]
    },
    {
      "vnum": 18606,
      "name": "糧箭棚",
      "description": "箭壺、乾糧與燈油被整整齊齊地收在棚下，每一樣都在告訴人這裡雖然狹窄，卻必須能獨自撐住一段時間。哨樓的壓力有一部分就來自這種對持久戒備的預設。 ",
      "sector_type": "SECT_CITY",
      "cluster": "core",
      "coord": [1, 3, 1],
      "labels": ["supply", "reserve"],
      "exits": [
        { "direction": "west", "to": 18604 }
      ],
      "enquires": ["糧箭", "燈油", "備料"]
    },
    {
      "vnum": 18607,
      "name": "狼煙高臺",
      "description": "登上高臺後，風勢與視野都不再允許人保有半點鬆懈。這裡是整座哨樓真正的心臟，狼煙、旗號與遠處動靜都會先在此被看見，再決定要不要把緊張往下方軍鎮壓回去。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, 3, 2],
      "labels": ["watchtower", "high-ground", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 18604 },
        { "direction": "north", "to": 18608 }
      ],
      "enquires": ["狼煙", "高臺", "遠處"]
    },
    {
      "vnum": 18608,
      "name": "北望風口",
      "description": "更靠北的風口把整片前線氣息直接送到眼前，讓這裡幾乎像站在未落成邊境的門檻上。它不像一個終點，更像是在提醒人們：真正的北方壓力還在更遠處等著被補成下一個節點。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, 4, 2],
      "labels": ["north-edge", "forward", "nonplanar"],
      "exits": [
        { "direction": "south", "to": 18607 }
      ],
      "enquires": ["北邊", "風口", "前線"]
    }
  ]
}
```
