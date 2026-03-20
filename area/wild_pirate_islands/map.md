# 海盜群島 (`wild_pirate_islands`)

## Area Intent

`wild_pirate_islands` 承接 `dng_boat_graveyard` 南界外的破舷裂口，讓玩家從沉舟遺跡重新踏回外海，但面對的已不再是港城可理解的航道，而是一段由碎島、礁灣、舊海寇寨與風化棧橋構成的高風險群島 wild。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `群島 / 海寇`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_pirate_islands",
    "title": "海盜群島",
    "design_notes": "第一版 spec-first 草案。先固定破舷登岸點、礁灣主線、海寇舊寨、風旗高脊與外礁灘，把沉舟之後的海路節奏重新打開成外海群島 wild。",
    "level_range": "100-100",
    "planned_vnum_range": "15801-15830",
    "reserved_room_block": "15801-15830",
    "theme": {
      "primary": "江湖",
      "secondary": "群島 / 海寇"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 15801,
        "target_area": "dng_boat_graveyard",
        "label": "外海破舷"
      },
      {
        "direction": "down",
        "source_vnum": 15810,
        "target_area": "sec_water_ruins",
        "label": "水府裂井"
      },
      {
        "direction": "east",
        "source_vnum": 15812,
        "target_area": "fort_naval_base",
        "label": "海寇前哨"
      }
    ],
    "clusters": [
      { "id": "wreck-exit", "label": "破舷登岸" },
      { "id": "reef-lane", "label": "礁灣主線" },
      { "id": "pirate-cove", "label": "海寇舊寨" },
      { "id": "signal-ridge", "label": "風旗高脊" },
      { "id": "outer-shoal", "label": "外礁灘" }
    ]
  },
  "rooms": [
    {
      "vnum": 15801,
      "name": "破舷登岸點",
      "description": "從沉舟裂口脫身後，最先踩上的不是穩固碼頭，而是一塊被潮水與碎木反覆磨蝕的斜礁。站穩腳步的瞬間，你就會明白這裡雖然終於離開沉艙，卻也正式進入外海真正不講理的地帶。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "wreck-exit",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "north", "to": 15712, "external": true },
        { "direction": "south", "to": 15803 },
        { "direction": "east", "to": 15802 }
      ],
      "enquires": ["北邊", "沉舟", "群島"]
    },
    {
      "vnum": 15802,
      "name": "碎木潮棚",
      "description": "幾片勉強還能遮風的棚面用碎木與舊帆拼成，像任何在群島上活得夠久的人，最後都學會先替自己向海風偷一點陰影。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "wreck-exit",
      "coord": [1, 0, 0],
      "labels": ["shed", "rest"],
      "exits": [
        { "direction": "west", "to": 15801 }
      ],
      "enquires": ["棚子", "歇腳"]
    },
    {
      "vnum": 15803,
      "name": "礁灣主徑",
      "description": "一條被腳印、繩痕與礁石磨出的主徑沿著海灣向南轉去，路況並不整齊，卻看得出長年有人在這裡來往。這種秩序不像官道，倒更像一種只有海寇和倖存者才認得的默契。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "reef-lane",
      "coord": [0, -1, 0],
      "labels": ["main-path", "reef"],
      "exits": [
        { "direction": "north", "to": 15801 },
        { "direction": "south", "to": 15804 },
        { "direction": "west", "to": 15805 }
      ],
      "enquires": ["礁灣", "去路"]
    },
    {
      "vnum": 15804,
      "name": "破旗灣口",
      "description": "灣口斜插著幾支早被鹽風扯碎的舊旗桿，剩下的布條在風裡拍出一種既像示警又像招呼的聲音。這裡明顯曾有人想把群島劃成自己的地盤，只是海從來不太認帳。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "pirate-cove",
      "coord": [0, -2, 0],
      "labels": ["cove", "flags"],
      "exits": [
        { "direction": "north", "to": 15803 },
        { "direction": "south", "to": 15808 },
        { "direction": "east", "to": 15807 }
      ],
      "enquires": ["海寇", "灣口"]
    },
    {
      "vnum": 15805,
      "name": "低潮礁橋",
      "description": "退潮時露出的礁橋像一道勉強能走的灰白背脊，把幾塊小島暫時縫在一起。這種路最危險的地方不是難走，而是它永遠只暫時屬於你。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "reef-lane",
      "coord": [-1, -1, 0],
      "labels": ["bridge", "low-tide"],
      "exits": [
        { "direction": "east", "to": 15803 },
        { "direction": "south", "to": 15806 }
      ],
      "enquires": ["退潮", "礁橋"]
    },
    {
      "vnum": 15806,
      "name": "裂礁側灘",
      "description": "裂開的礁面在側灘邊排成一道道不規則陰影，像一群蹲伏著等海色變化的人。你若不仔細看，很容易把能落腳的地方和下一步就會滑進海裡的地方混在一起。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "outer-shoal",
      "coord": [-1, -2, 0],
      "labels": ["shoal", "side-bank"],
      "exits": [
        { "direction": "north", "to": 15805 },
        { "direction": "east", "to": 15808 }
      ],
      "enquires": ["裂礁", "退路"]
    },
    {
      "vnum": 15807,
      "name": "舊寨外棧",
      "description": "幾段搭在礁邊的外棧還保留著海寇寨留下的粗糙手法，繩結打得結實，木板卻全憑膽子撐著。這裡不像正規碼頭，卻很明顯曾是某種人常年靠船、卸貨與藏身的地方。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "pirate-cove",
      "coord": [1, -2, 0],
      "labels": ["pier", "raider"],
      "exits": [
        { "direction": "west", "to": 15804 },
        { "direction": "north", "to": 15812 }
      ],
      "enquires": ["舊寨", "棧橋"]
    },
    {
      "vnum": 15808,
      "name": "海寇舊寨",
      "description": "石牆、碎桶與半塌棚架把這裡拼成一座勉強還看得出輪廓的舊寨，像主人雖然早就不在，規矩卻還留在每條小徑與每個藏風口裡。這裡比海面更危險，因為有人曾經把它當成家。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "pirate-cove",
      "coord": [0, -3, 0],
      "labels": ["camp", "core"],
      "exits": [
        { "direction": "north", "to": 15804 },
        { "direction": "west", "to": 15806 },
        { "direction": "south", "to": 15810 },
        { "direction": "up", "to": 15811 }
      ],
      "enquires": ["寨子", "南邊", "上面"]
    },
    {
      "vnum": 15810,
      "name": "外礁深灘",
      "description": "再往南去，礁石之間的水色忽然轉深，像整片海面都在提醒你這裡不只是群島邊緣，還是更深水域真正開始張口的地方。站在這裡時，往回和往下都像一樣需要膽量。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "outer-shoal",
      "coord": [0, -4, 0],
      "labels": ["south-edge", "deep-water"],
      "exits": [
        { "direction": "north", "to": 15808 }
      ],
      "enquires": ["深水", "下面", "南邊"]
    },
    {
      "vnum": 15811,
      "name": "風旗高脊",
      "description": "站上高脊後，整片碎島、舊寨、礁灣和外灘都被海風吹得像一張隨時會改寫的圖。這種高度暫時給了人判斷力，也讓外海真正有多大這件事變得更刺眼。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "signal-ridge",
      "coord": [0, -3, 1],
      "labels": ["ridge", "lookout"],
      "exits": [
        { "direction": "down", "to": 15808 }
      ],
      "enquires": ["風旗", "望路"]
    },
    {
      "vnum": 15812,
      "name": "東向暗棧",
      "description": "一道偏窄的暗棧往東延出，棧上釘痕和藏鉤都說明它從來不是替普通旅人準備的。只要再往東走，節奏就會更偏向前哨、看守與真正有人佔地盤的世界。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "signal-ridge",
      "coord": [2, -1, 0],
      "labels": ["east-link", "hidden-pier"],
      "exits": [
        { "direction": "south", "to": 15807 }
      ],
      "enquires": ["東邊", "前哨", "棧橋"]
    }
  ]
}
```
