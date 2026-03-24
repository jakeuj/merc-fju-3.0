# 易京 (`fort_yijing`)

## Area Intent

`fort_yijing` 承接 `road_yijing` 的易京前路口，把北平外圍一路北推的軍旅節奏正式收束成有關門、內營、軍需棚與望樓層次的北境關隘。這裡不只是抽象的 `Fort` 節點，而是一處會讓旅人明顯感受到袁紹勢力壓迫、軍令秩序與更北方邊線正在逼近的 choke point。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `北境軍鎮`
- LevelRange: `26-38`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_yijing",
    "title": "易京",
    "design_notes": "第一版 spec-first 草案。先固定前寨口、關前柵道、易京關門、內營主道、將令案側、軍需棚與北望樓，把易京前帶正式收束成可載入的北境 fort 節點。",
    "level_range": "26-38",
    "planned_vnum_range": "17901-17920",
    "reserved_room_block": "17901-17920",
    "theme": {
      "primary": "軍旅",
      "secondary": "北境軍鎮"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 17901,
        "target_area": "road_yijing",
        "target_room_vnum": 17808,
        "label": "易京前路口"
      },
      {
        "direction": "up",
        "source_vnum": 17907,
        "target_area": "fort_northern_watch",
        "label": "北方哨樓"
      },
      {
        "direction": "east",
        "source_vnum": 17908,
        "target_area": "wild_bailang",
        "label": "白狼山方向"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "關前道" },
      { "id": "gate", "label": "關門與前寨" },
      { "id": "camp", "label": "內營與軍需" },
      { "id": "watch", "label": "望樓與東側寨牆" }
    ]
  },
  "rooms": [
    {
      "vnum": 17901,
      "name": "易京前寨口",
      "description": "官道在此被木柵、拒馬與整隊痕跡收成一道真正的寨口，讓人一腳踏進來就明白自己已經離開單純旅路，開始進入北境軍鎮的勢力邊線。南邊還能看見易京前路口的車痕，往內則是更明確的軍令秩序。",
      "sector_type": "SECT_FIELD",
      "cluster": "approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 17808, "external": true },
        { "direction": "north", "to": 17902 }
      ],
      "enquires": ["易京", "寨口", "前面"]
    },
    {
      "vnum": 17902,
      "name": "關前柵道",
      "description": "狹長柵道把往來人流壓成一條不得不放慢的進路，兩側木樁與拒馬都留著反覆加固過的痕跡。站在這裡時，很難不去注意每一道目光都在默默盤點你的來意。",
      "sector_type": "SECT_FIELD",
      "cluster": "approach",
      "coord": [0, 1, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "south", "to": 17901 },
        { "direction": "north", "to": 17903 }
      ],
      "enquires": ["盤查", "拒馬"]
    },
    {
      "vnum": 17903,
      "name": "易京關門",
      "description": "厚木關門與兩側柵牆把整座軍鎮的重心收在這個窄口上，任何想真正進入易京的人都得先穿過這裡。風一吹過門樓，就會把更北方的冷意和軍鎮壓迫一起帶下來。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [0, 2, 0],
      "labels": ["gate", "chokepoint"],
      "exits": [
        { "direction": "south", "to": 17902 },
        { "direction": "north", "to": 17904 }
      ],
      "enquires": ["關門", "放行", "軍令"]
    },
    {
      "vnum": 17904,
      "name": "內營主道",
      "description": "進了關門之後，腳下道路雖然還算寬敞，氣氛卻不再像外路那樣可隨意停留。傳令、換班與搬運在這裡形成一種緊繃但穩定的節奏，整座易京的軍事用途也因此顯得更具體。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [0, 3, 0],
      "labels": ["main-road", "camp-flow"],
      "exits": [
        { "direction": "south", "to": 17903 },
        { "direction": "west", "to": 17905 },
        { "direction": "east", "to": 17906 },
        { "direction": "up", "to": 17907 }
      ],
      "enquires": ["內營", "軍需", "將令"]
    },
    {
      "vnum": 17905,
      "name": "將令木案側",
      "description": "一張厚實木案靠在寨牆內側，上頭壓著巡路簿冊與幾封未送出的軍令。這裡不像軍需棚那樣雜亂，反而更有一種任何調度都會先在此定下的冷靜壓力。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [-1, 3, 0],
      "labels": ["orders", "briefing"],
      "exits": [
        { "direction": "east", "to": 17904 }
      ],
      "enquires": ["將令", "簿冊", "巡路"]
    },
    {
      "vnum": 17906,
      "name": "軍需棚前",
      "description": "軍需棚前堆著草料、皮囊、燈油與打包妥當的巡路物資，看得出易京不是單純守門，而是一處會持續把兵與補給往更北邊推送出去的軍鎮節點。這裡的忙碌帶著明確用途感。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [1, 3, 0],
      "labels": ["supply", "logistics"],
      "exits": [
        { "direction": "west", "to": 17904 },
        { "direction": "east", "to": 17908 }
      ],
      "enquires": ["軍需", "草料", "補給"]
    },
    {
      "vnum": 17907,
      "name": "北望樓",
      "description": "站上望樓後，南面的官道起伏與北面的邊地風勢都變得一覽無遺。這種高度讓人很容易理解，易京真正的作用並不是收人停留，而是盯住更遠方的邊境變化並及時把消息壓回關內。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, 3, 1],
      "labels": ["watchtower", "high-ground", "world-link-up", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 17904 }
      ],
      "enquires": ["望樓", "高處", "北方"]
    },
    {
      "vnum": 17908,
      "name": "東側寨牆",
      "description": "東側寨牆比主門一帶更安靜，卻能清楚看見牆外地勢逐漸轉成更荒、更冷的山前前帶。站在這裡時，白狼山方向的壓力不像傳聞那麼遙遠，反而像隨時會從風裡逼近。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [2, 3, 0],
      "labels": ["east-edge", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 17906 }
      ],
      "enquires": ["白狼山", "東邊", "寨牆"]
    }
  ]
}
```
