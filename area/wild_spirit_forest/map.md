# 靈木森林 (`wild_spirit_forest`)

## Area Intent

`wild_spirit_forest` 承接 `wild_wuling` 山腹下方的東岔靈林，把原本只是山路支線暗示的密林岔口，正式展成一段會吞掉聲音、扭亂方向感、也更讓人意識到武陵靈氣不是只停在主路旁邊的深山 wild。這裡不靠谷地開闊或墓道封閉施壓，而是用靈木、妖藤、倒木、濕地與高根觀位，讓玩家明顯感到自己正被一片活著的森林慢慢引離熟悉的辨位方式。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `靈木 / 妖藤`
- LevelRange: `42-56`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_spirit_forest",
    "title": "靈木森林",
    "design_notes": "第一版 spec-first 草案。先固定靈林岔入口、藤影小徑、古碑風根地、靈木空場、伏苔低窪、根橋下灣、懸藤高台與青燐深處，把武陵山東側的靈木支線正式展成可載入 wild。",
    "level_range": "42-56",
    "planned_vnum_range": "19201-19220",
    "reserved_room_block": "19201-19220",
    "theme": {
      "primary": "仙俠",
      "secondary": "靈木 / 妖藤"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 19201,
        "target_area": "wild_wuling",
        "target_room_vnum": 15012,
        "label": "東岔靈林"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "岔入口帶" },
      { "id": "trail", "label": "藤影林徑" },
      { "id": "hollow", "label": "低窪濕地" },
      { "id": "canopy", "label": "高根與深處" }
    ]
  },
  "rooms": [
    {
      "vnum": 19201,
      "name": "靈林岔入口",
      "description": "一踏進這段往東偏去的林路，山腹主徑的風聲就像被身後那些更高、更密的樹影整片截住。路還算看得見，卻已經不像給外人走的通道，而像森林只暫時允許你從邊上摸進來看看。",
      "sector_type": "SECT_FOREST",
      "cluster": "entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 15012, "external": true },
        { "direction": "east", "to": 19202 },
        { "direction": "north", "to": 19203 }
      ],
      "enquires": ["靈林", "武陵", "來路"]
    },
    {
      "vnum": 19202,
      "name": "藤影小徑",
      "description": "小徑被垂藤切成一段段狹窄的視線，腳邊卻還留著零散的舊足跡，像有人曾反覆進出這裡，只是不願意替後來的人把路講明。走在這裡時，會開始懷疑森林是不是故意把主路和支路混成一種東西。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "trail",
      "coord": [1, 0, 0],
      "labels": ["trail", "vines", "main-route"],
      "exits": [
        { "direction": "west", "to": 19201 },
        { "direction": "east", "to": 19204 },
        { "direction": "south", "to": 19205 }
      ],
      "enquires": ["藤", "小徑", "足跡"]
    },
    {
      "vnum": 19203,
      "name": "古碑風根地",
      "description": "一塊半埋的舊碑斜卡在糾結樹根之間，碑面文字大多被潮氣與苔色吃掉，只剩零星筆畫像還想勉強提醒誰曾在這裡立過界。可真正先讓人停下腳步的，反而是那些從碑腳一路伸出去的根脈，像整片森林都在借這塊石頭記路。",
      "sector_type": "SECT_FOREST",
      "cluster": "entry",
      "coord": [0, 1, 0],
      "labels": ["landmark", "stele", "roots"],
      "exits": [
        { "direction": "south", "to": 19201 },
        { "direction": "down", "to": 19205 }
      ],
      "keywords": [
        {
          "keyword": "石碑",
          "description": "碑面殘紋早已難辨全句，只看得出它本來並不是替觀景立的，而是替辨路與立界留下的舊記。"
        }
      ],
      "enquires": ["石碑", "界", "根"]
    },
    {
      "vnum": 19204,
      "name": "靈木空場",
      "description": "林子忽然在這裡鬆出一小塊空場，幾株老木的樹皮裂紋裡卻透著近乎溫潤的亮色，像這裡的氣息一直比周圍濃厚半分。這不是誇張到像祕境開口的景象，但已足夠讓人確信，武陵的靈氣在這裡不是傳聞。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "trail",
      "coord": [2, 0, 0],
      "labels": ["spirit-wood", "clearing", "hub"],
      "exits": [
        { "direction": "west", "to": 19202 },
        { "direction": "south", "to": 19206 },
        { "direction": "north", "to": 19207 },
        { "direction": "east", "to": 19208 }
      ],
      "enquires": ["靈木", "空場", "異樣"]
    },
    {
      "vnum": 19205,
      "name": "伏苔低窪",
      "description": "低窪地帶積著一層看似柔軟的濕苔，踩下去卻會立刻知道底下還藏著碎枝、細石和不太穩的泥水。這裡不像真正的陷阱，更像森林用自己的方式提醒你，離主路愈遠，腳底的誠實就愈重要。",
      "sector_type": "SECT_FOREST",
      "cluster": "hollow",
      "coord": [1, -1, -1],
      "labels": ["low-ground", "moss", "wet"],
      "exits": [
        { "direction": "north", "to": 19202 },
        { "direction": "east", "to": 19206 },
        { "direction": "up", "to": 19203 }
      ],
      "enquires": ["低處", "濕苔", "退路"]
    },
    {
      "vnum": 19206,
      "name": "根橋下灣",
      "description": "幾段粗根從坡面橫跨過來，剛好在這片下灣上方搭出像天然木橋的陰影，讓人一時分不清自己是在樹下穿行，還是在被什麼古老東西俯看。四周沒有真正封死，可每一步都像會被林子多記住一點。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "hollow",
      "coord": [2, -1, -1],
      "labels": ["root-bridge", "shade", "crossing"],
      "exits": [
        { "direction": "west", "to": 19205 },
        { "direction": "north", "to": 19204 },
        { "direction": "up", "to": 19207 }
      ],
      "enquires": ["樹根", "下灣", "上面"]
    },
    {
      "vnum": 19207,
      "name": "懸藤高台",
      "description": "高台其實只是樹根與土層自然拱起的一塊突地，可垂落的藤影和略高的視野，仍讓人第一次能把前面幾段林路重新串回成一條完整線。也正因如此，你才更容易看出更東邊那片林影不是出口，而是另一層更深的招引。",
      "sector_type": "SECT_FOREST",
      "cluster": "canopy",
      "coord": [2, 1, 1],
      "labels": ["high-ground", "vantage", "up"],
      "exits": [
        { "direction": "south", "to": 19204 },
        { "direction": "down", "to": 19206 },
        { "direction": "north", "to": 19208 }
      ],
      "enquires": ["高處", "藤", "東邊"]
    },
    {
      "vnum": 19208,
      "name": "青燐深處",
      "description": "更深處的樹影間偶爾會浮出一點近乎青燐的冷光，既不像燈，也不像單純的月色反射。站在這裡時，真正令人不安的不是看見了什麼，而是你開始分不清那些微光究竟在更裡面，還是其實一直就在自己身邊。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "canopy",
      "coord": [3, 0, 0],
      "labels": ["deep-forest", "glow", "furthest"],
      "exits": [
        { "direction": "west", "to": 19204 },
        { "direction": "south", "to": 19207 }
      ],
      "enquires": ["青光", "深處", "去路"]
    }
  ]
}
```
