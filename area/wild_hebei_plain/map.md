# 河北平原 (`wild_hebei_plain`)

## Area Intent

`wild_hebei_plain` 承接 `city_nanpi` 東向平原口，把玩家從河北城鎮帶進真正開闊的北地野外。這裡要讓人感受到視野變大、路徑變鬆、風聲與官道痕跡重新成為主角，並替之後往更南的營寨或其他北地節點留下清楚轉場。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `平原 / 官道`
- LevelRange: `24-36`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_hebei_plain",
    "title": "河北平原",
    "design_notes": "第一版 spec-first 草案。先固定西口平原道、官道中段、風碑地標與更南的營寨預留，讓南皮外帶正式變成可實作的河北 wild 節點。",
    "level_range": "24-36",
    "planned_vnum_range": "17501-17520",
    "reserved_room_block": "17501-17520",
    "theme": {
      "primary": "軍旅",
      "secondary": "平原 / 官道"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 17501,
        "target_area": "city_nanpi",
        "label": "南皮東口"
      },
      {
        "direction": "south",
        "source_vnum": 17508,
        "target_area": "fort_river_crossing",
        "label": "渡河營寨"
      }
    ],
    "clusters": [
      { "id": "west-entry", "label": "西口平原道" },
      { "id": "open-plain", "label": "主平原帶" },
      { "id": "landmark", "label": "風碑與岔台" },
      { "id": "south-route", "label": "南向營道" }
    ]
  },
  "rooms": [
    {
      "vnum": 17501,
      "name": "南皮東外道",
      "description": "一離開南皮東口，城牆與牌樓帶來的秩序感很快就被開闊平原沖淡。西邊仍能回望見城市輪廓，東南北卻只剩更長的風線與官道痕跡，像河北的真正幅員從這裡才開始展開。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 17408, "external": true },
        { "direction": "east", "to": 17502 }
      ],
      "enquires": ["南皮", "外道", "平原"]
    },
    {
      "vnum": 17502,
      "name": "官道平野",
      "description": "官道在平原上沒有太多遮蔽，只靠車轍與零散路標把方向維持住。走在這裡時，會很清楚感到自己已離開城市，卻還沒真正進入另一個據點，只能靠風向與地勢辨位。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-entry",
      "coord": [1, 0, 0],
      "labels": ["road", "open-way"],
      "exits": [
        { "direction": "west", "to": 17501 },
        { "direction": "east", "to": 17503 }
      ],
      "enquires": ["官道", "方向"]
    },
    {
      "vnum": 17503,
      "name": "平原中段",
      "description": "視野在這裡被拉得非常長，遠處任何人馬移動都很容易被先看見。這種毫不遮掩的空曠讓河北平原的風險感變得很直接，也讓整條路比城內更講究提早判斷去向。",
      "sector_type": "SECT_FIELD",
      "cluster": "open-plain",
      "coord": [2, 0, 0],
      "labels": ["plain", "visibility"],
      "exits": [
        { "direction": "west", "to": 17502 },
        { "direction": "east", "to": 17505 },
        { "direction": "north", "to": 17504 }
      ],
      "enquires": ["風", "平野", "去路"]
    },
    {
      "vnum": 17504,
      "name": "草高側線",
      "description": "稍高的草線把這裡和主道隔出一點距離，適合暫時停下腳步觀察前後動靜。雖然不算真正隱蔽，卻足夠讓旅人重新抓回對地勢的理解。",
      "sector_type": "SECT_FIELD",
      "cluster": "open-plain",
      "coord": [2, 1, 0],
      "labels": ["side-path", "watchpoint"],
      "exits": [
        { "direction": "south", "to": 17503 }
      ],
      "enquires": ["草叢", "觀望"]
    },
    {
      "vnum": 17505,
      "name": "風碑岔台",
      "description": "一座半斷的石碑立在岔台邊，像是替這片過分開闊的平原留下方向證據。站在這裡時，風聲總會比人聲更明顯，讓人自然把注意力放回路向、雲勢和遠處地形。",
      "sector_type": "SECT_FIELD",
      "cluster": "landmark",
      "coord": [3, 0, 0],
      "labels": ["landmark", "route-info"],
      "exits": [
        { "direction": "west", "to": 17503 },
        { "direction": "south", "to": 17506 }
      ],
      "enquires": ["風碑", "岔路"]
    },
    {
      "vnum": 17506,
      "name": "低坡草道",
      "description": "地勢在這裡略略往南傾，讓草道與車痕都變得更清楚一些。與其說這是顯眼的道路，不如說是一條被太多人走過、因此再也無法忽視的方向感。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-route",
      "coord": [3, -1, 0],
      "labels": ["slope", "southbound"],
      "exits": [
        { "direction": "north", "to": 17505 },
        { "direction": "south", "to": 17507 }
      ],
      "enquires": ["南路", "營寨"]
    },
    {
      "vnum": 17507,
      "name": "營道前帶",
      "description": "再往南走，路上的痕跡就不只屬於商旅或零散差人，而開始有更多軍用補給與駐行往返留下的重量。這裡像是在提醒你，平原並不是純然空曠，它同時也是軍路延伸的場域。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-route",
      "coord": [3, -2, 0],
      "labels": ["military-route", "transition"],
      "exits": [
        { "direction": "north", "to": 17506 },
        { "direction": "south", "to": 17508 }
      ],
      "enquires": ["軍路", "南邊"]
    },
    {
      "vnum": 17508,
      "name": "渡河營道口",
      "description": "官道在此繼續朝南推去，地面上的車印與駐行痕跡都變得更密。站在這裡時，南皮的城市氣息已經被風與土色沖淡，只剩更前方的營寨與渡河線在等待人靠近。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-route",
      "coord": [3, -3, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 17507 },
        { "direction": "south", "to": 17601, "external": true }
      ],
      "enquires": ["營寨", "渡河", "南路"]
    }
  ]
}
```
