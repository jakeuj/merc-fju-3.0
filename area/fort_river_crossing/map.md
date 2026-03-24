# 渡河營寨 (`fort_river_crossing`)

## Area Intent

`fort_river_crossing` 承接 `wild_hebei_plain` 南向營道，讓玩家從開闊平原正式走進有軍令壓迫與河渡戰略意味的 fort 區段。這裡要把節奏從平原風感收成關前道、關門、內營與望樓的層次感。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `河渡要地`
- LevelRange: `26-38`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_river_crossing",
    "title": "渡河營寨",
    "design_notes": "第一版 spec-first 草案。先固定關前道、寨門、內營、軍需棚與望樓，把河北平原南向營道正式收束成渡河要地的 fort 節點。",
    "level_range": "26-38",
    "planned_vnum_range": "17601-17620",
    "reserved_room_block": "17601-17620",
    "theme": {
      "primary": "軍旅",
      "secondary": "河渡要地"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 17601,
        "target_area": "wild_hebei_plain",
        "label": "平原營道"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "關前道" },
      { "id": "gate", "label": "寨門與關口" },
      { "id": "camp", "label": "內營與軍需棚" },
      { "id": "watch", "label": "望樓高位" }
    ]
  },
  "rooms": [
    {
      "vnum": 17601,
      "name": "關前營道",
      "description": "從河北平原一路南下到這裡時，開闊地形帶來的自由感會立刻被收緊。木柵、哨火與駐行痕跡讓人很清楚知道，前方已經不是單純路帶，而是一處會先盤問再放行的軍事要地。",
      "sector_type": "SECT_FIELD",
      "cluster": "approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-edge", "world-link-north"],
      "exits": [
        { "direction": "north", "to": 17508, "external": true },
        { "direction": "south", "to": 17602 }
      ],
      "enquires": ["營道", "寨門", "前方"]
    },
    {
      "vnum": 17602,
      "name": "寨前柵道",
      "description": "柵道兩旁的拒馬與木樁把人流壓成一道狹窄的進路，連腳步都會自然放慢。這裡最強烈的感覺不是熱鬧，而是任何往來都被軍令默默測量的壓迫。",
      "sector_type": "SECT_FIELD",
      "cluster": "approach",
      "coord": [0, -1, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "north", "to": 17601 },
        { "direction": "south", "to": 17603 }
      ],
      "enquires": ["拒馬", "盤查"]
    },
    {
      "vnum": 17603,
      "name": "渡河寨門",
      "description": "厚木寨門與兩側矮牆把整個營寨的重心都收在這裡，任何想進內營的人都得先穿過這道軍令氣息濃厚的門口。站在這裡時，會明顯感覺平原上的風感已經被營寨秩序壓住。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [0, -2, 0],
      "labels": ["gate", "chokepoint"],
      "exits": [
        { "direction": "north", "to": 17602 },
        { "direction": "south", "to": 17604 }
      ],
      "enquires": ["寨門", "進寨"]
    },
    {
      "vnum": 17604,
      "name": "內營主道",
      "description": "內營主道上人馬往返頻繁，但沒有城市市集那種鬆散人聲，更多是軍需、傳令與駐守輪替的秩序。這裡讓人很清楚感受到，營寨的一切都是圍著河渡與軍路而運作。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [0, -3, 0],
      "labels": ["main-road", "camp-flow"],
      "exits": [
        { "direction": "north", "to": 17603 },
        { "direction": "west", "to": 17605 },
        { "direction": "east", "to": 17606 },
        { "direction": "up", "to": 17607 }
      ],
      "enquires": ["內營", "軍需", "河渡"]
    },
    {
      "vnum": 17605,
      "name": "軍需棚外",
      "description": "軍需棚外堆著木箱、繩索與渡河用具，讓人一眼就看出這座營寨不只是守門，更是要把人與物真正送過河線的地方。這裡的秩序帶著很強的用途感。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-1, -3, 0],
      "labels": ["supply", "logistics"],
      "exits": [
        { "direction": "east", "to": 17604 }
      ],
      "enquires": ["軍需", "木箱", "渡具"]
    },
    {
      "vnum": 17606,
      "name": "渡河木台",
      "description": "木台邊可以看見更多與河渡有關的痕跡，連木板上的磨損方向都透露出駐行與器材搬運的固定節奏。站在這裡時，會很自然把注意力放到更前方的河線與水路上。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [1, -3, 0],
      "labels": ["platform", "river-focus"],
      "exits": [
        { "direction": "west", "to": 17604 }
      ],
      "enquires": ["木台", "河邊"]
    },
    {
      "vnum": 17607,
      "name": "望樓高位",
      "description": "從望樓往北看，平原上的動靜幾乎無所遁形；往南看，河渡帶來的壓力又會讓整座營寨顯得更像一枚釘在要道上的軍事節點。這種高度把營寨真正的戰略角色說得很明白。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, -3, 1],
      "labels": ["watchtower", "high-ground", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 17604 }
      ],
      "enquires": ["望樓", "高處", "遠望"]
    }
  ]
}
```
