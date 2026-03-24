# 胡營舊地 (`wild_barbarian_camp`)

## Area Intent

`wild_barbarian_camp` 承接 `wild_bailang` 東向荒徑，把玩家從白狼山的邊山傳說與裂風山脊，帶進一段更明顯帶著人為駐留、部族舊痕與敵意觀察感的北境 hostile wild。這裡不是單純再多一段山路，而是要讓 `白狼山 -> 胡營舊地 -> 襄平` 這條遼東前帶真正有一個會改變氣氛的中介節點。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `部族營地 / 邊地敵蹤`
- LevelRange: `34-46`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_barbarian_camp",
    "title": "胡營舊地",
    "design_notes": "第一版 spec-first 草案。先固定白狼山東荒徑、舊柵外帶、火堆空坪、巡望高臺與往襄平去的東向城路口，讓北境主線從邊山傳說切進更有人為敵蹤感的 hostile wild。",
    "level_range": "34-46",
    "planned_vnum_range": "18201-18220",
    "reserved_room_block": "18201-18220",
    "theme": {
      "primary": "軍旅",
      "secondary": "部族營地 / 邊地敵蹤"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 18201,
        "target_area": "wild_bailang",
        "target_room_vnum": 18007,
        "label": "白狼山東荒徑"
      },
      {
        "direction": "east",
        "source_vnum": 18208,
        "target_area": "city_xiangping",
        "label": "襄平城路"
      }
    ],
    "clusters": [
      { "id": "west-entry", "label": "西向荒口" },
      { "id": "outer-camp", "label": "外圍營痕帶" },
      { "id": "camp-core", "label": "火堆與破帳空坪" },
      { "id": "east-road", "label": "東向城路口" }
    ]
  },
  "rooms": [
    {
      "vnum": 18201,
      "name": "胡地西荒口",
      "description": "白狼山東荒徑在這裡慢慢收成更平、更乾硬的一段野地，地上卻已不只是風吹與獸蹄留下的痕跡，而開始混進人為踩踏與重物拖曳的舊印。站在這裡時，會明顯感覺東邊不再只是深山，而是一塊曾有人長時間盤踞的邊地。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 18007, "external": true },
        { "direction": "east", "to": 18202 }
      ],
      "enquires": ["白狼山", "胡營", "東邊"]
    },
    {
      "vnum": 18202,
      "name": "斷草營徑",
      "description": "原本的荒草在這裡被踏出一條較硬的窄徑，兩旁還能看見倒伏後沒再長整齊的草痕。這不是官道式的規整路線，卻比野獸走出的徑線更帶方向感，像有人曾經反覆把它用成接近營地的外帶。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "west-entry",
      "coord": [1, 0, 0],
      "labels": ["trail", "transition"],
      "exits": [
        { "direction": "west", "to": 18201 },
        { "direction": "east", "to": 18203 },
        { "direction": "north", "to": 18205 }
      ],
      "enquires": ["營徑", "草痕", "去路"]
    },
    {
      "vnum": 18203,
      "name": "風旗殘道",
      "description": "幾根殘破木桿斜插在路旁，桿頭還掛著被風撕碎的布條，讓這裡像是一段曾經刻意宣示地盤、如今卻只剩餘威的舊路。比起白狼山的傳說感，這裡更直接提醒人前方有過營地，也有過衝突。",
      "sector_type": "SECT_FIELD",
      "cluster": "outer-camp",
      "coord": [2, 0, 0],
      "labels": ["marker", "hostile-trace"],
      "exits": [
        { "direction": "west", "to": 18202 },
        { "direction": "east", "to": 18204 },
        { "direction": "south", "to": 18206 }
      ],
      "enquires": ["旗桿", "殘旗", "前面"]
    },
    {
      "vnum": 18204,
      "name": "舊柵外口",
      "description": "幾段半倒的木柵把這裡收成一個不再完整的營地外口，木頭裂面上還留著長久曝曬後的白痕。這地方不像正在守備，卻也不像完全荒廢，像有人隨時可能重新回到這片舊地，把邊地秩序再度拉緊。",
      "sector_type": "SECT_FIELD",
      "cluster": "outer-camp",
      "coord": [3, 0, 0],
      "labels": ["palisade", "outer-gate"],
      "exits": [
        { "direction": "west", "to": 18203 },
        { "direction": "east", "to": 18208 }
      ],
      "enquires": ["木柵", "舊營", "出口"]
    },
    {
      "vnum": 18205,
      "name": "獸骨火堆",
      "description": "火堆早已熄冷，只剩黑灰、碎炭與幾截沒清乾淨的獸骨散在地上。這裡最讓人不安的不是狼藉本身，而是它顯示出這地方曾經有人停留、進食、守夜，而且把一整套營地生活過得相當熟練。",
      "sector_type": "SECT_FIELD",
      "cluster": "camp-core",
      "coord": [1, 1, 0],
      "labels": ["campfire", "landmark"],
      "exits": [
        { "direction": "south", "to": 18202 },
        { "direction": "east", "to": 18206 }
      ],
      "enquires": ["火堆", "獸骨", "守夜"]
    },
    {
      "vnum": 18206,
      "name": "破帳空坪",
      "description": "空坪邊緣還釘著幾根繫帳樁，風一吹就會讓散落布片擦過地面，發出很輕卻很難忽略的響動。站在這裡時，會覺得這塊地方並未真正死去，它只是暫時空著，像隨時還能被誰重新占回來。",
      "sector_type": "SECT_FIELD",
      "cluster": "camp-core",
      "coord": [2, 1, 0],
      "labels": ["camp-yard", "core"],
      "exits": [
        { "direction": "west", "to": 18205 },
        { "direction": "north", "to": 18203 },
        { "direction": "east", "to": 18207 }
      ],
      "enquires": ["帳篷", "空地", "營心"]
    },
    {
      "vnum": 18207,
      "name": "巡望高臺",
      "description": "一小段土臺被人為墊高，站上去後能把西邊荒徑與東邊去路都看得更清楚。這裡沒有真正的箭樓，卻具備同樣的意義: 任何想通過這片舊地的人，都很容易先被看見。",
      "sector_type": "SECT_FIELD",
      "cluster": "camp-core",
      "coord": [3, 1, 0],
      "labels": ["watchpoint", "height"],
      "exits": [
        { "direction": "west", "to": 18206 }
      ],
      "enquires": ["高臺", "巡望", "遠處"]
    },
    {
      "vnum": 18208,
      "name": "東向城路口",
      "description": "再往東去，腳下的路痕開始比營地周邊更穩、更寬，像是零散邊地活動終究要重新匯進真正的人煙與城路。站在這個路口時，會很清楚感覺到胡營舊地不是終點，而只是抵達襄平前最後一段帶敵意記憶的外帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-road",
      "coord": [4, 0, 0],
      "labels": ["east-edge", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 18204 }
      ],
      "enquires": ["襄平", "城路", "東邊"]
    }
  ]
}
```
