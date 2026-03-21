# 建業 (`city_jianye`)

## Area Intent

`city_jianye` 承接 `fort_naval_base` 北向內港水門，把玩家從海防關卡正式帶回江東都城，讓節奏從軍門與哨樓切回主街、市集、官署與城政服務。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `江東都城`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_jianye",
    "title": "建業",
    "design_notes": "第一版 spec-first 草案。先固定水門入口、主街中軸、市集補給、官署前街與東向港區，把海路主線正式收束到江東主城 hub。",
    "level_range": "100-100",
    "planned_vnum_range": "16001-16030",
    "reserved_room_block": "16001-16030",
    "theme": {
      "primary": "歷史城市",
      "secondary": "江東都城"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 16001,
        "target_area": "fort_naval_base",
        "label": "建業水門"
      },
      {
        "direction": "east",
        "source_vnum": 16010,
        "target_area": "district_jianye_port",
        "label": "建業港區"
      },
      {
        "direction": "west",
        "source_vnum": 16007,
        "target_area": "wild_jianye_west",
        "label": "建業西坊"
      }
    ],
    "clusters": [
      { "id": "water-gate", "label": "水門入口" },
      { "id": "main-street", "label": "主街中軸" },
      { "id": "market-yard", "label": "市集補給" },
      { "id": "office-lane", "label": "官署前街" },
      { "id": "east-ward", "label": "東坊港向" }
    ]
  },
  "rooms": [
    {
      "vnum": 16001,
      "name": "建業水門",
      "description": "穿過內港水門後，海防大營的鐵硬節奏忽然被更厚重也更穩定的城牆秩序接手。這裡不像前線，卻仍保留著水路都城特有的警醒，像任何進城的人都還在被建業先看上一眼。 ",
      "sector_type": "SECT_CITY",
      "cluster": "water-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-link"],
      "exits": [
        { "direction": "south", "to": 15910, "external": true },
        { "direction": "north", "to": 16003 },
        { "direction": "east", "to": 16002 }
      ],
      "enquires": ["水門", "城裡", "建業"]
    },
    {
      "vnum": 16002,
      "name": "水門值房",
      "description": "值房內外擺著筆架、燈座與簡短告示，讓人一看就知道這裡既管通行，也管消息。和軍營相比，這裡的壓力少了殺氣，多了制度本身的穩定重量。 ",
      "sector_type": "SECT_CITY",
      "cluster": "water-gate",
      "coord": [1, 0, 0],
      "labels": ["guardhouse", "registry"],
      "exits": [
        { "direction": "west", "to": 16001 }
      ],
      "enquires": ["值房", "告示"]
    },
    {
      "vnum": 16003,
      "name": "建業南街",
      "description": "街面寬闊而乾淨，來往行人、差役與商旅把都城氣息一層層疊了起來。站在這裡時，你會立刻明白建業的秩序不是靠關卡撐住，而是靠這種日常運作本身維持。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 1, 0],
      "labels": ["main-road", "south-street"],
      "exits": [
        { "direction": "south", "to": 16001 },
        { "direction": "north", "to": 16004 },
        { "direction": "west", "to": 16005 }
      ],
      "enquires": ["主街", "市集"]
    },
    {
      "vnum": 16004,
      "name": "建業中街",
      "description": "這段中街把都城的節奏推得更清楚了些，招牌、人聲、腳步和車輪聲不再彼此搶奪，而像被一座大城自然編進同一條脈動裡。海路帶來的緊繃，在這裡終於能稍微放下。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 2, 0],
      "labels": ["center", "city-core"],
      "exits": [
        { "direction": "south", "to": 16003 },
        { "direction": "north", "to": 16008 },
        { "direction": "east", "to": 16006 }
      ],
      "enquires": ["中街", "官署", "港區"]
    },
    {
      "vnum": 16005,
      "name": "市集牌樓",
      "description": "牌樓下掛滿商鋪招牌和指路木牌，讓補給、交易與打聽消息都變得比海上世界理所當然得多。這裡的繁忙不是混亂，而是一種只有主城才養得起的厚實流動。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "east", "to": 16003 },
        { "direction": "north", "to": 16007 }
      ],
      "enquires": ["市集", "補給", "招牌"]
    },
    {
      "vnum": 16006,
      "name": "官署前街",
      "description": "官署前街比主街安靜得多，但那種安靜反而讓往來差役與文吏顯得更有分量。這裡不是用來放鬆的地方，而是讓一座城真正把命令、文書與秩序落下來的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-lane",
      "coord": [1, 2, 0],
      "labels": ["office", "yamen"],
      "exits": [
        { "direction": "west", "to": 16004 },
        { "direction": "north", "to": 16009 }
      ],
      "enquires": ["官署", "差役"]
    },
    {
      "vnum": 16007,
      "name": "西坊橫街",
      "description": "橫街上滿是往返搬貨和補貨的人影，讓西坊不只像市集後場，也像整座都城真正把人潮往城郊導出去的邊帶。走過這裡時，很容易感受到建業的厚實秩序正開始向外鬆開，準備把旅人交還給城外的官道與水鄉。 ",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [-1, 2, 0],
      "labels": ["west-ward", "shops"],
      "exits": [
        { "direction": "south", "to": 16005 },
        { "direction": "east", "to": 16008 },
        { "direction": "west", "to": 16201, "external": true }
      ],
      "enquires": ["西坊", "西郊", "補給"]
    },
    {
      "vnum": 16008,
      "name": "都城前庭",
      "description": "前庭像把主街、市集與官署三股節奏都收在同一處交會點上，任何人只要站在這裡，就能看出建業不是單靠城牆偉大，而是靠整個體系一起在運作。這種厚度正是都城和普通城鎮最大的差別。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, 3, 0],
      "labels": ["hub", "front-court"],
      "exits": [
        { "direction": "south", "to": 16004 },
        { "direction": "west", "to": 16007 },
        { "direction": "east", "to": 16009 },
        { "direction": "north", "to": 16010 }
      ],
      "enquires": ["前庭", "去路", "都城"]
    },
    {
      "vnum": 16009,
      "name": "東坊路口",
      "description": "東坊路口的行人和車流明顯更偏向水路與商務，像整座城在這裡開始把視線往港區和對外往來轉去。比起前線的守備，這裡更像建業真正把外海變成資源的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "east-ward",
      "coord": [1, 3, 0],
      "labels": ["east-ward", "trade"],
      "exits": [
        { "direction": "west", "to": 16008 },
        { "direction": "south", "to": 16006 }
      ],
      "enquires": ["東坊", "港區"]
    },
    {
      "vnum": 16010,
      "name": "港向街口",
      "description": "再往東去，空氣裡就會更明顯地混進港埠、船貨與水路消息的味道。這裡像是建業主城節奏正式向外海與商路展開的一道街口，不再只是城內，而是整個江東對外的臉面之一。 ",
      "sector_type": "SECT_CITY",
      "cluster": "east-ward",
      "coord": [0, 4, 0],
      "labels": ["east-link", "port-road"],
      "exits": [
        { "direction": "south", "to": 16008 },
        { "direction": "east", "to": 16101, "external": true }
      ],
      "enquires": ["港區", "東邊", "船"]
    }
  ]
}
```
