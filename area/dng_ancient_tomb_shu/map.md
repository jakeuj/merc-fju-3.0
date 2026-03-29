# 蜀漢古墓 (`dng_ancient_tomb_shu`)

## Area Intent

`dng_ancient_tomb_shu` 承接 `wild_hidden_valley` 的沉陵坳口，把深谷地勢裡原本只像陰口與沉陷痕的地方，正式展成一段可載入的古墓前帶。這裡不再靠谷地空曠感或山路岔徑製造壓力，而是用更人工、更封閉、也更像被故意藏起來的石門與墓道，讓玩家明顯感到自己跨進了另一套秩序。

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `古墓 / 石門`
- LevelRange: `48-62`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_ancient_tomb_shu",
    "title": "蜀漢古墓",
    "design_notes": "第一版 spec-first 草案。先固定沉陵落階、前廳石券、斷燈墓道、偏室石櫃、封紋中庭、殘兵耳室、沉門前廊與內槨石門，把隱谷之下的蜀漢古墓正式展成可載入 dungeon。",
    "level_range": "48-62",
    "planned_vnum_range": "19101-19120",
    "reserved_room_block": "19101-19120",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "古墓 / 石門"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 19101,
        "target_area": "wild_hidden_valley",
        "target_room_vnum": 19008,
        "label": "沉陵坳口"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "落階入口帶" },
      { "id": "corridor", "label": "墓道主線" },
      { "id": "side", "label": "偏室與耳室" },
      { "id": "core", "label": "封紋與內槨前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 19101,
      "name": "沉陵落階",
      "description": "從沉陵坳口往下踏入時，地勢很快就從泥石與根痕轉成刻意修出的狹長石階。這裡最令人不安的不是陰暗，而是那種「有人早就預料會有人從上面找到這裡」的設計感。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry",
      "coord": [0, 0, -1],
      "labels": ["entry", "up-edge", "world-link-up", "nonplanar"],
      "exits": [
        { "direction": "up", "to": 19008, "external": true },
        { "direction": "north", "to": 19102 }
      ],
      "enquires": ["上面", "石階", "入口"]
    },
    {
      "vnum": 19102,
      "name": "前廳石券",
      "description": "前廳頂上的石券拱得很低，逼得來人很難完全抬頭，只能先專注在腳下與前方那幾步。牆面殘留的刻紋像曾有過完整的墓誌與警語，只是現在大半都故意看不清了。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry",
      "coord": [0, 1, -1],
      "labels": ["hall", "arch", "warning"],
      "exits": [
        { "direction": "south", "to": 19101 },
        { "direction": "north", "to": 19103 },
        { "direction": "east", "to": 19105 }
      ],
      "enquires": ["前廳", "石券", "刻紋"]
    },
    {
      "vnum": 19103,
      "name": "斷燈墓道",
      "description": "墓道兩側還能看見早年燈座留下的黑痕，可真正的燈火與守墓秩序早已退去，只剩石壁把聲音一層層往前送。越往裡走，越會覺得這地方不是廢棄，而是在長時間等待某種重新開啟。",
      "sector_type": "SECT_INSIDE",
      "cluster": "corridor",
      "coord": [0, 2, -1],
      "labels": ["corridor", "dark", "main-route"],
      "exits": [
        { "direction": "south", "to": 19102 },
        { "direction": "north", "to": 19106 },
        { "direction": "west", "to": 19104 }
      ],
      "enquires": ["墓道", "燈", "前面"]
    },
    {
      "vnum": 19104,
      "name": "偏室石櫃",
      "description": "這間偏室被一座半裂石櫃與幾件翻倒器具佔住大半空間，看得出曾有人試著在這裡搜找或搬動什麼。可越是這樣，越讓人懷疑真正重要的東西早就不在表面。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side",
      "coord": [-1, 2, -1],
      "labels": ["side-room", "coffer", "searched"],
      "exits": [
        { "direction": "east", "to": 19103 }
      ],
      "enquires": ["石櫃", "偏室", "器具"]
    },
    {
      "vnum": 19105,
      "name": "殘兵耳室",
      "description": "耳室裡靠牆散著幾件早已鏽死的殘兵與破甲片，像這座古墓在封起來之前曾經短暫拿來藏過更倉促、更世俗的東西。這種不合典禮的痕跡，反而讓整座墓顯得更真實也更難測。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side",
      "coord": [1, 1, -1],
      "labels": ["ear-room", "weapons", "uneasy"],
      "exits": [
        { "direction": "west", "to": 19102 },
        { "direction": "north", "to": 19107 }
      ],
      "enquires": ["殘兵", "耳室", "誰"]
    },
    {
      "vnum": 19106,
      "name": "封紋中庭",
      "description": "中庭不像真正開闊，反而像墓道刻意在這裡鬆一口氣，好讓來人先看見地面那圈被磨得發白的封紋。那些紋路沒有完全失效，只是正在用更安靜、更陰冷的方式提醒人這裡不該被輕易跨過。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core",
      "coord": [0, 3, -1],
      "labels": ["courtyard", "seal", "core"],
      "exits": [
        { "direction": "south", "to": 19103 },
        { "direction": "east", "to": 19107 },
        { "direction": "north", "to": 19108 }
      ],
      "enquires": ["封紋", "中庭", "下面"]
    },
    {
      "vnum": 19107,
      "name": "沉門前廊",
      "description": "前廊盡頭那扇沉門比前段石券都更厚，像不是防賊，而是防某種已經在墓裡待太久的東西回到外側。站在這裡時，會很清楚地感覺到自己離真正的核心只差最後一層隔絕。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core",
      "coord": [1, 3, -1],
      "labels": ["anteroom", "heavy-door", "threshold"],
      "exits": [
        { "direction": "west", "to": 19106 },
        { "direction": "south", "to": 19105 }
      ],
      "enquires": ["沉門", "前廊", "核心"]
    },
    {
      "vnum": 19108,
      "name": "內槨石門",
      "description": "石門表面幾乎看不見多餘裝飾，只在靠近時才會發現門緣有一圈極細卻完整的縫紋，像它從未真正敞開過。這裡不像終點，更像整座古墓真正開始閉口不言的地方。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core",
      "coord": [0, 4, -1],
      "labels": ["inner-gate", "sealed", "deepest"],
      "exits": [
        { "direction": "south", "to": 19106 }
      ],
      "enquires": ["石門", "裡面", "封印"]
    }
  ]
}
```
