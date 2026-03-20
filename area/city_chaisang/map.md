# 柴桑 (`city_chaisang`)

## Area Intent

`city_chaisang` 承接 `city_jiangxia` 東向幹道之後的江岸主線，讓玩家從雲夢與沉沒古廟的濕重壓迫，重新回到一座由江岸街市、渡運秩序、城務榜牌與南向轉場共同構成的江東入口城市。

第一版目標先固定：

- 一條由西向東穿過江岸外門、主街與市集的主探索線
- 一條向南折入城務 / 補給與長沙方向轉場的側線
- 一條 `up/down` 連到城樓或江岸望臺的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示柴桑、江夏、長沙、赤壁與碼頭秩序

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `江岸城鎮 / 江東門戶`
- LevelRange: `62-72`
- Parent region: `江岸東口`
- World gap filled: 讓主世界 progression 從江夏與雲夢段重新回到東進江岸的城市 hub，並為荊南與赤壁支線建立穩定轉場點

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_chaisang",
    "title": "柴桑",
    "design_notes": "第一版 spec-first 草案。先固定西向城門、主街、市集補給與南向轉場骨架，讓江岸東進主線在柴桑收束成城市 hub。",
    "level_range": "62-72",
    "planned_vnum_range": "14701-14730",
    "reserved_room_block": "14701-14730",
    "theme": {
      "primary": "歷史城市",
      "secondary": "江岸城鎮 / 江東門戶"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 14701,
        "target_area": "city_jiangxia",
        "label": "江夏水路"
      },
      {
        "direction": "west",
        "source_vnum": 14702,
        "target_area": "wild_reed_bank",
        "label": "蘆洲外帶"
      },
      {
        "direction": "south",
        "source_vnum": 14710,
        "target_area": "city_changsha",
        "label": "荊南大道"
      },
      {
        "direction": "south",
        "source_vnum": 14712,
        "target_area": "sec_chibi_battlefield",
        "label": "赤壁舊戰場"
      }
    ],
    "clusters": [
      { "id": "west-gate", "label": "西向江門" },
      { "id": "harbor-street", "label": "江岸主街" },
      { "id": "market-quarter", "label": "市集補給區" },
      { "id": "yamen-quarter", "label": "城務官署區" },
      { "id": "south-turn", "label": "南向轉場區" }
    ]
  },
  "rooms": [
    {
      "vnum": 14701,
      "name": "西向江門",
      "description": "江岸城門迎著來自江夏方向的風聲與腳步，門下地面因長年潮氣而顯得微黑，卻仍維持著城市該有的整齊與秩序。剛從濕地與古廟回來的人，多半會在這裡第一次真正鬆下肩膀。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 14412, "external": true },
        { "direction": "east", "to": 14703 },
        { "direction": "south", "to": 14702 }
      ],
      "enquires": ["江夏", "進城"]
    },
    {
      "vnum": 14702,
      "name": "蘆洲外牌",
      "description": "城門外側另一角立著一面指往蘆洲與外帶渡岸的舊木牌，牌面雖被風吹得發白，字跡卻仍能讓常走江岸的人一眼辨出方向。這裡像在提醒旅人，柴桑雖是城，卻仍和外側水路綁得很緊。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, -1, 0],
      "labels": ["outer-sign", "branch-link"],
      "exits": [
        { "direction": "north", "to": 14701 }
      ],
      "enquires": ["蘆洲", "去路"]
    },
    {
      "vnum": 14703,
      "name": "江岸主街",
      "description": "主街沿著江岸往城內拉開，路邊既有做水路生意的鋪面，也有專門招呼行旅與搬貨客的棚攤。這裡的熱鬧不像大都城那樣擁擠，而是一種總和渡運、補給與消息綁在一起的實用秩序。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-street",
      "coord": [1, 0, 0],
      "labels": ["main-street", "harbor"],
      "exits": [
        { "direction": "west", "to": 14701 },
        { "direction": "east", "to": 14704 },
        { "direction": "south", "to": 14705 }
      ],
      "enquires": ["主街", "碼頭"]
    },
    {
      "vnum": 14704,
      "name": "主街十字",
      "description": "幾條街巷在這裡交會，榜牌、店招與城務告示把柴桑作為轉場城市的角色寫得清清楚楚。站在十字口時，你會很自然地明白哪裡能補給、哪裡能問路、哪裡則會把你再送回更危險的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-street",
      "coord": [2, 0, 0],
      "labels": ["hub", "crossroads"],
      "exits": [
        { "direction": "west", "to": 14703 },
        { "direction": "east", "to": 14708 },
        { "direction": "south", "to": 14709 },
        { "direction": "up", "to": 14711 }
      ],
      "enquires": ["柴桑", "官府", "長沙"]
    },
    {
      "vnum": 14705,
      "name": "水行市集",
      "description": "這一帶的市集把乾糧、油布、水囊、粗繩與臨時替換的小器具都擺得很近，像是專為剛從遠路回來、又或即將再度出發的人準備。即使只是經過，也很難不被其中某樣實用物什拖住腳步。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [1, -1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 14703 },
        { "direction": "east", "to": 14706 }
      ],
      "enquires": ["市集", "補給"]
    },
    {
      "vnum": 14706,
      "name": "藥材棚下",
      "description": "棚下掛滿乾燥藥材與驅濕香包，空氣裡混著草藥、桐油與潮氣，聞起來既像藥鋪，也像渡岸工人常來補命的一角。和江夏相比，這裡更像一座習慣把長途水路當日常的城市。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [2, -1, 0],
      "labels": ["herbal", "service"],
      "exits": [
        { "direction": "west", "to": 14705 },
        { "direction": "east", "to": 14707 }
      ],
      "enquires": ["藥鋪", "水路"]
    },
    {
      "vnum": 14707,
      "name": "南轉巷口",
      "description": "巷子在這裡向南敞開，牆邊路牌把長沙與赤壁方向分得一清二楚。這不像一條多麼威風的大道，卻是柴桑真正作為轉場城市最重要的證明之一。",
      "sector_type": "SECT_CITY",
      "cluster": "south-turn",
      "coord": [3, -1, 0],
      "labels": ["south-turn", "routing"],
      "exits": [
        { "direction": "west", "to": 14706 },
        { "direction": "south", "to": 14710 }
      ],
      "enquires": ["長沙", "赤壁", "去路"]
    },
    {
      "vnum": 14708,
      "name": "榜牌前街",
      "description": "一面大榜牌立在街側，貼滿近期船路、糧價與城務盤查的告示。行人經過時都會下意識掃上一眼，彷彿這面榜牌就是柴桑這座城保持順暢運作的節奏器。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [3, 0, 0],
      "labels": ["notice", "civic"],
      "exits": [
        { "direction": "west", "to": 14704 },
        { "direction": "south", "to": 14712 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜牌上的字跡密密麻麻，卻整理得極有條理，讓人一眼就能看出這座城對人流與船路的重視。"
        }
      ],
      "enquires": ["官府", "榜牌"]
    },
    {
      "vnum": 14709,
      "name": "城務前院",
      "description": "前院不算宏大，卻收拾得格外利落，進出的人要不是差役，就是有事來報的行腳客。這裡不像單純辦公的地方，更像整座柴桑把水路、城路與南向支線重新整理在一起的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, -1, 0],
      "labels": ["yamen", "order"],
      "exits": [
        { "direction": "north", "to": 14704 }
      ],
      "enquires": ["官府", "差役"]
    },
    {
      "vnum": 14710,
      "name": "荊南南牌",
      "description": "南口牌樓把長沙方向的去路立得很明確，牌腳則堆著幾捆剛綁好的布袋與行裝，像總有人準備從這裡再往南走很遠。站在牌樓下時，柴桑作為中繼城市的性格就再明顯不過了。",
      "sector_type": "SECT_CITY",
      "cluster": "south-turn",
      "coord": [3, -2, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 14707 }
      ],
      "enquires": ["長沙", "南邊"]
    },
    {
      "vnum": 14711,
      "name": "江樓望臺",
      "description": "沿著短階走上望臺後，江岸街屋、碼頭棚影與外側水路都盡收眼底。這樣的高度不只是為了景色，更像是讓城裡始終有人能提早看清哪一批船正靠近、哪一條路又要開始忙起來。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, 1, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 14704 }
      ],
      "enquires": ["望臺", "江岸"]
    },
    {
      "vnum": 14712,
      "name": "赤壁路標",
      "description": "路標比別處更舊，木面上卻仍能清楚看見指往赤壁戰場舊地的方向。它不像一般城中告示那樣只講日常，反而替柴桑多添了一層離歷史戰痕很近的氣味。",
      "sector_type": "SECT_CITY",
      "cluster": "south-turn",
      "coord": [4, -1, 0],
      "labels": ["battle-link", "marker"],
      "exits": [
        { "direction": "north", "to": 14708 },
        { "direction": "south", "to": 14801, "external": true }
      ],
      "enquires": ["赤壁", "戰場", "去路"]
    }
  ]
}
```
