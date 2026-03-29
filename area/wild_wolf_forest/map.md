# 狼林 (`wild_wolf_forest`)

## Area Intent

`wild_wolf_forest` 承接 `wild_bailang` 的北狼隘口，把白狼山之後的北境山林正式轉成更封閉、更濕冷、也更帶失蹤傳聞與狼群壓力的深林 wild。這裡不再像山前那樣依賴脊線與風口辨位，而是讓玩家明顯感到自己正被松針、霧痕與錯亂岔路慢慢吞進去。

## Theme Positioning

- Theme: `詭異民俗`
- Subtheme: `林區 / 狼群`
- LevelRange: `40-52`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_wolf_forest",
    "title": "狼林",
    "design_notes": "第一版 spec-first 草案。先固定南隘林口、枯針松徑、狼骨岔路、霧痕林腹、獵戶歇棚、狼爪石碑、失蹤者舊營與月嚎空地，讓白狼山北向預留正式落成為帶狼群與失蹤傳聞的深林節點。",
    "level_range": "40-52",
    "planned_vnum_range": "18701-18720",
    "reserved_room_block": "18701-18720",
    "theme": {
      "primary": "詭異民俗",
      "secondary": "林區 / 狼群"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 18701,
        "target_area": "wild_bailang",
        "target_room_vnum": 18008,
        "label": "北狼隘口"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "南隘入口帶" },
      { "id": "routes", "label": "松徑與岔路" },
      { "id": "landmark", "label": "石碑與歇棚" },
      { "id": "deep", "label": "舊營與月嚎空地" }
    ]
  },
  "rooms": [
    {
      "vnum": 18701,
      "name": "南隘林口",
      "description": "一踏過北狼隘口，裸露山風就立刻被更低沉的樹聲接手。腳下仍留著從白狼山北脊延進來的舊路，可那條路一進林便不再像軍旅路線，而像某種只靠記憶與膽氣勉強維持的邊地小徑。",
      "sector_type": "SECT_FOREST",
      "cluster": "entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 18008, "external": true },
        { "direction": "north", "to": 18702 }
      ],
      "enquires": ["白狼山", "林口", "回去"]
    },
    {
      "vnum": 18702,
      "name": "枯針松徑",
      "description": "厚厚松針把路聲壓得很低，只剩偶爾踩斷枯枝時才提醒人自己仍在前進。林中風向不再像山脊那樣坦白，連遠處狼嚎聽起來都像故意從錯的方向傳來。",
      "sector_type": "SECT_FOREST",
      "cluster": "routes",
      "coord": [0, 1, 0],
      "labels": ["path", "pine-needle"],
      "exits": [
        { "direction": "south", "to": 18701 },
        { "direction": "north", "to": 18704 },
        { "direction": "east", "to": 18703 }
      ],
      "enquires": ["松徑", "風聲", "狼嚎"]
    },
    {
      "vnum": 18703,
      "name": "狼骨岔路",
      "description": "兩三截發白獸骨被有意無意地插在泥地旁，把原本就難辨的岔路硬是添上一層更不吉利的指引意味。無論那是警告還是標記，都讓人很難再把這裡當成普通山林。",
      "sector_type": "SECT_FOREST",
      "cluster": "routes",
      "coord": [1, 1, 0],
      "labels": ["junction", "bones", "ominous"],
      "exits": [
        { "direction": "west", "to": 18702 },
        { "direction": "north", "to": 18706 }
      ],
      "enquires": ["狼骨", "岔路", "標記"]
    },
    {
      "vnum": 18704,
      "name": "霧痕林腹",
      "description": "林腹的樹幹上留著一層像水氣又像手痕的淡白霧印，讓整段道路都像剛被什麼看不見的東西沿途摸過。走進來之後，最明顯的變化不是更暗，而是更難相信自己的方向感。",
      "sector_type": "SECT_FOREST",
      "cluster": "routes",
      "coord": [0, 2, 0],
      "labels": ["core", "mist", "unsettling"],
      "exits": [
        { "direction": "south", "to": 18702 },
        { "direction": "north", "to": 18707 },
        { "direction": "west", "to": 18705 }
      ],
      "enquires": ["霧痕", "林腹", "方向"]
    },
    {
      "vnum": 18705,
      "name": "獵戶歇棚",
      "description": "一座被苔與松脂半吞掉的小歇棚倚在樹根旁，裡頭還留著乾柴、舊皮囊與幾件顯然是給急行旅人應急的東西。它提供的不是安全，只是一種前人也曾在這裡勉強撐過去的證據。",
      "sector_type": "SECT_FOREST",
      "cluster": "landmark",
      "coord": [-1, 2, 0],
      "labels": ["shelter", "supply", "rest"],
      "exits": [
        { "direction": "east", "to": 18704 }
      ],
      "enquires": ["歇棚", "獵戶", "補給"]
    },
    {
      "vnum": 18706,
      "name": "狼爪石碑",
      "description": "林中的殘石碑被劃出幾道深長痕跡，遠看像舊字，近看又更像狼爪在濕石上反覆磨出的印子。這塊石碑不像單純地標，反而像某種提醒外人不該再往前的邊界。",
      "sector_type": "SECT_FOREST",
      "cluster": "landmark",
      "coord": [1, 2, 0],
      "labels": ["stone-marker", "warning"],
      "exits": [
        { "direction": "south", "to": 18703 },
        { "direction": "north", "to": 18708 }
      ],
      "enquires": ["石碑", "爪痕", "警告"]
    },
    {
      "vnum": 18707,
      "name": "失蹤者舊營",
      "description": "兩頂塌掉的舊帳與一圈快被泥土吃回去的火痕留在這裡，像是有人曾在林腹深處短暫停留，卻沒能把故事完整地帶出去。最不舒服的地方，是周圍幾乎看不見任何慌亂逃離的痕跡。",
      "sector_type": "SECT_FOREST",
      "cluster": "deep",
      "coord": [0, 3, 0],
      "labels": ["camp", "missing", "deep"],
      "exits": [
        { "direction": "south", "to": 18704 },
        { "direction": "east", "to": 18708 }
      ],
      "enquires": ["失蹤", "舊營", "火痕"]
    },
    {
      "vnum": 18708,
      "name": "月嚎空地",
      "description": "樹冠在這片空地忽然張開，讓上方月色與下方潮泥一起把狼嚎放大得過於清楚。它不像一個終點，更像整片狼林真正開始回頭看你的地方，彷彿再往前就會進到不該被輕易說穿的北境異聞裡。",
      "sector_type": "SECT_FOREST",
      "cluster": "deep",
      "coord": [1, 3, 0],
      "labels": ["clearing", "wolf-howl", "north-edge"],
      "exits": [
        { "direction": "south", "to": 18706 },
        { "direction": "west", "to": 18707 }
      ],
      "enquires": ["月色", "狼嚎", "前面"]
    }
  ]
}
```
