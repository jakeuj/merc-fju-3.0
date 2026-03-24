# 遼東平原 (`wild_liaodong_plain`)

## Area Intent

`wild_liaodong_plain` 承接 `city_xiangping` 北原牌樓，把玩家從邊城整補、驛站與官府秩序，重新送進一段視野大開、風勢直接、馬跡與軍路同時存在的遼東平原前帶。這裡不是再複製一般官道，而是要讓 `襄平 -> 遼東平原` 真的成為一段從城內秩序切進開闊北地的主線轉場。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `草原 / 騎兵前帶`
- LevelRange: `32-44`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_liaodong_plain",
    "title": "遼東平原",
    "design_notes": "第一版 spec-first 草案。先固定襄平北原牌樓外的草坡官跡、風草臺、牧馬低帶與更北平原分流，讓遼東邊城之外的開闊 wild 正式成形。",
    "level_range": "32-44",
    "planned_vnum_range": "18401-18420",
    "reserved_room_block": "18401-18420",
    "theme": {
      "primary": "軍旅",
      "secondary": "草原 / 騎兵前帶"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 18401,
        "target_area": "city_xiangping",
        "target_room_vnum": 18308,
        "label": "襄平北原牌樓"
      }
    ],
    "clusters": [
      { "id": "south-entry", "label": "南向平原入口" },
      { "id": "open-plain", "label": "開闊平野帶" },
      { "id": "landmark", "label": "風草與馬跡地標" },
      { "id": "north-reach", "label": "更北平原前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 18401,
      "name": "北原外坡",
      "description": "一離開襄平北原牌樓，城牆與人聲很快就被風勢拉遠，只剩腳下較緩的土坡把人送進真正開闊的遼東平原。從這裡開始，辨位不再靠街巷與牌樓，而是靠地勢、草色與遠處動靜。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 18308, "external": true },
        { "direction": "north", "to": 18402 }
      ],
      "enquires": ["襄平", "平原", "回城"]
    },
    {
      "vnum": 18402,
      "name": "草痕官跡",
      "description": "平原上的草痕被反覆踩出幾條隱約的官跡，沒有真正修成硬路，卻明顯看得出往來人馬總會沿著這一線走。比起城市裡的路，這裡更像是一種被長年使用出來的方向共識。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-entry",
      "coord": [0, 1, 0],
      "labels": ["road-trace", "transition"],
      "exits": [
        { "direction": "south", "to": 18401 },
        { "direction": "north", "to": 18403 },
        { "direction": "east", "to": 18405 }
      ],
      "enquires": ["官跡", "草痕", "去路"]
    },
    {
      "vnum": 18403,
      "name": "遼東平野",
      "description": "視野在這裡徹底打開，草浪與風線幾乎沒有遮蔽，遠處任何移動都會先成為視覺裡的一小個訊號。遼東平原真正的壓力不在於地形複雜，而在於它讓每一個判斷都變得更早、更直接。",
      "sector_type": "SECT_FIELD",
      "cluster": "open-plain",
      "coord": [0, 2, 0],
      "labels": ["open-field", "visibility"],
      "exits": [
        { "direction": "south", "to": 18402 },
        { "direction": "north", "to": 18404 },
        { "direction": "west", "to": 18406 }
      ],
      "enquires": ["平野", "北邊", "風"]
    },
    {
      "vnum": 18404,
      "name": "北風草臺",
      "description": "略高的草臺讓風在這裡總比別處更急一些，也讓人更容易看清地勢和遠方的馬跡。站在這裡時，會覺得襄平已經退到背後，而更北的遼東腹地才正要開始露出自己的尺度。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-reach",
      "coord": [0, 3, 0],
      "labels": ["height", "lookout"],
      "exits": [
        { "direction": "south", "to": 18403 }
      ],
      "enquires": ["北風", "遠處", "草臺"]
    },
    {
      "vnum": 18405,
      "name": "側線牧痕",
      "description": "偏離主要草痕後，地面上開始混進更散、更淺的牧痕與蹄印，像有人把這片平野同時當成通路與生活空間。這裡讓遼東平原不像單純軍路，而更像一塊仍在呼吸的北地前帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "landmark",
      "coord": [1, 1, 0],
      "labels": ["side-path", "hoofprint"],
      "exits": [
        { "direction": "west", "to": 18402 },
        { "direction": "north", "to": 18407 }
      ],
      "enquires": ["馬跡", "側線", "牧地"]
    },
    {
      "vnum": 18406,
      "name": "風折路標",
      "description": "一根被風折得有些斜的舊路標立在這裡，字跡早已模糊，卻仍像在努力證明這片平野並非無人來去。它最有價值的地方不是文字，而是提醒你在如此開闊的地帶，任何人為標記都值得再看一眼。",
      "sector_type": "SECT_FIELD",
      "cluster": "landmark",
      "coord": [-1, 2, 0],
      "labels": ["landmark", "route-info"],
      "exits": [
        { "direction": "east", "to": 18403 }
      ],
      "enquires": ["路標", "方向", "舊字"]
    },
    {
      "vnum": 18407,
      "name": "牧馬低帶",
      "description": "地勢在這裡稍稍往下收，草色也更深，讓整片低帶看起來像長久有人放馬停留的地方。這裡既有生活痕跡，也有一種若敵騎突然從遠處逼近就會來不及回頭的開闊風險。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-reach",
      "coord": [1, 2, -1],
      "labels": ["lowland", "pasture"],
      "exits": [
        { "direction": "south", "to": 18405 },
        { "direction": "north", "to": 18408 }
      ],
      "enquires": ["牧馬", "低地", "前面"]
    },
    {
      "vnum": 18408,
      "name": "更北平原口",
      "description": "再往北走，草地與風勢像還要繼續無止境地展開出去，讓這裡明顯不像終點，只像遼東更大區域真正開始的門口。襄平在身後提供秩序，而這裡則把人重新交還給北地本身。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-reach",
      "coord": [1, 3, -1],
      "labels": ["north-edge", "forward"],
      "exits": [
        { "direction": "south", "to": 18407 }
      ],
      "enquires": ["北邊", "更遠", "平原口"]
    }
  ]
}
```
