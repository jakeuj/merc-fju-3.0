# 壽春田野 (`wild_shouchun_fields`)

## Area Intent

`wild_shouchun_fields` 承接 `city_shouchun` 的田野外口，把玩家從壽春城心的軍政秩序放回城外田埂、村舍與灌渠交錯的近郊帶。這裡不是遠離主線的荒野，而是一段讓壽春真正長出外城呼吸感的 wild：能問路、能辨位，也能為更南更深的江東路線保留自然延伸。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `田野 / 村舍`
- LevelRange: `22-34`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_shouchun_fields",
    "title": "壽春田野",
    "design_notes": "第一版 spec-first 草案。先固定壽春外口、田埂岔路、曬穀村舍與更南預留，讓壽春在主城 implementation 後自然展開成一段可辨位、可問路的近郊 wild。",
    "level_range": "22-34",
    "planned_vnum_range": "17101-17120",
    "reserved_room_block": "17101-17120",
    "theme": {
      "primary": "歷史城市",
      "secondary": "田野 / 村舍"
    },
    "world_links": [
      {
        "direction": "enter",
        "source_vnum": 17101,
        "target_area": "city_shouchun",
        "label": "壽春田野外口"
      },
      {
        "direction": "south",
        "source_vnum": 17108,
        "target_area": "city_jianye",
        "label": "建業北路"
      }
    ],
    "clusters": [
      { "id": "field-entry", "label": "城外田口" },
      { "id": "ridge-path", "label": "田埂與灌渠" },
      { "id": "hamlet-edge", "label": "村舍曬場" },
      { "id": "southern-track", "label": "南向路帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17101,
      "name": "田野外口",
      "description": "一出壽春外口，城牆與旗牌的壓力立刻退到身後，迎面換成被春泥與田氣撐開的視野。這裡仍看得見城門輪廓，卻已經是另一種節奏: 人不再被城裡的規矩推著走，而得自己分辨田埂、灌渠與遠村之間哪條路才算正途。",
      "sector_type": "SECT_FIELD",
      "cluster": "field-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "city-edge", "world-link-enter"],
      "exits": [
        { "direction": "enter", "to": 17008, "external": true },
        { "direction": "south", "to": 17102 },
        { "direction": "east", "to": 17103 }
      ],
      "enquires": ["壽春", "外口", "田野"]
    },
    {
      "vnum": 17102,
      "name": "田埂岔路",
      "description": "幾條窄田埂在此分開，踩上去時既不算真正的路，也不是能放心亂走的泥地。城裡的人多半只把這裡當外圍農路，可對行腳的人來說，正是從這裡開始，壽春的主城秩序慢慢被鄉野的方向感取代。",
      "sector_type": "SECT_FIELD",
      "cluster": "field-entry",
      "coord": [0, 1, 0],
      "labels": ["junction", "field-path"],
      "exits": [
        { "direction": "north", "to": 17101 },
        { "direction": "south", "to": 17104 }
      ],
      "enquires": ["岔路", "田埂", "去路"]
    },
    {
      "vnum": 17103,
      "name": "灌渠小橋",
      "description": "一條不寬的灌渠沿著田畦斜斜切過，小橋的木板因久曬而微微起翹。站在橋上時，能同時看見壽春外牆、近處耕地與更遠處的低矮村舍，像整片近郊的脈絡都在這條水線旁變得清楚了些。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [1, 0, 0],
      "labels": ["canal", "bridge"],
      "exits": [
        { "direction": "west", "to": 17101 },
        { "direction": "south", "to": 17105 }
      ],
      "enquires": ["灌渠", "小橋", "村舍"]
    },
    {
      "vnum": 17104,
      "name": "曬穀場前",
      "description": "幾片平整空地上攤著曬穀竹蓆，風一過便帶起細碎穀香。這種離城不遠、卻完全屬於農時的景象，正好提醒人壽春之所以能穩，靠的不只是官署與糧車，也靠城外這些看似平凡的田家勞作。",
      "sector_type": "SECT_FIELD",
      "cluster": "hamlet-edge",
      "coord": [0, 2, 0],
      "labels": ["hamlet", "grain-yard"],
      "exits": [
        { "direction": "north", "to": 17102 },
        { "direction": "east", "to": 17105 },
        { "direction": "south", "to": 17106 }
      ],
      "enquires": ["曬穀", "村舍", "農家"]
    },
    {
      "vnum": 17105,
      "name": "渠畔草路",
      "description": "草路沿著渠岸往南拖去，腳下雖仍是泥土與碎草，走起來卻比田埂穩得多。只是越往前，城門聲響越薄，取而代之的是田水聲、蟲鳴與一些說不清從哪個村落傳來的人語，讓人自然意識到自己正從主城邊緣滑進更廣的外郊。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [1, 1, 0],
      "labels": ["field-road", "canal-side"],
      "exits": [
        { "direction": "north", "to": 17103 },
        { "direction": "west", "to": 17104 },
        { "direction": "east", "to": 17107 }
      ],
      "enquires": ["草路", "渠岸", "南邊"]
    },
    {
      "vnum": 17106,
      "name": "村舍籬旁",
      "description": "幾戶低矮村舍靠著竹籬圍成一小片安靜角落，屋外還掛著剛洗過的布衫與農具。這裡沒有城中鋪面的熱鬧，也沒有遠野那種空曠危險，反而像主線旅途難得能看見的一段真正有人過日子的縫隙。",
      "sector_type": "SECT_FIELD",
      "cluster": "hamlet-edge",
      "coord": [0, 3, 0],
      "labels": ["hamlet", "shelter"],
      "exits": [
        { "direction": "north", "to": 17104 },
        { "direction": "east", "to": 17108 }
      ],
      "enquires": ["村舍", "籬笆", "借宿"]
    },
    {
      "vnum": 17107,
      "name": "田間望路臺",
      "description": "一處略高的土臺被踩成了天然望點，向北能回看壽春外口，向南則能看見道路慢慢從田地邊緣拉直。站在這裡最容易明白，壽春田野不是零散農地，而是一段正把主城與更南遠路安靜接起來的過渡地帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "southern-track",
      "coord": [2, 1, 0],
      "labels": ["lookout", "route-node"],
      "exits": [
        { "direction": "west", "to": 17105 },
        { "direction": "south", "to": 17108 }
      ],
      "enquires": ["望路", "南路", "建業"]
    },
    {
      "vnum": 17108,
      "name": "南向土道",
      "description": "土道在這裡終於脫離零碎田埂，慢慢收成一條能讓長途旅人放心辨認的南向道路。再往前，壽春的近郊氣息會一步步淡下去，取而代之的是更南主線的遠行感，因此這裡像整片田野留給旅人的最後一個明白路標。",
      "sector_type": "SECT_FIELD",
      "cluster": "southern-track",
      "coord": [1, 3, 0],
      "labels": ["south-link", "route-out"],
      "exits": [
        { "direction": "north", "to": 17107 },
        { "direction": "west", "to": 17106 }
      ],
      "enquires": ["南路", "土道", "遠行"]
    }
  ]
}
```

