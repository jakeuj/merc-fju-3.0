# 古洞遺跡 (`dng_ancient_cave`)

## Area Intent

`dng_ancient_cave` 承接 `wild_bailang` 的裂縫洞口，把白狼山前帶從山前 wild 正式切進濕冷、封印與遺物感更重的洞窟 dungeon。這裡不只是白狼山下方再多一層黑洞，而是要讓玩家清楚感受到自己從風裂山徑掉進了更舊、更封閉、也更帶秘密壓力的地下遺跡。

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `洞窟遺封`
- LevelRange: `35-48`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_ancient_cave",
    "title": "古洞遺跡",
    "design_notes": "第一版 spec-first 草案。先固定裂縫落台、潮濕前廳、斷紋甬道、偏廊石室、殘碑暗井、石門前廊、封印主室與靈峰裂井，把白狼山下方的地下遺跡正式展成可落地的 dungeon 節點。",
    "level_range": "35-48",
    "planned_vnum_range": "18101-18120",
    "reserved_room_block": "18101-18120",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "洞窟遺封"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 18101,
        "target_area": "wild_bailang",
        "target_room_vnum": 18006,
        "label": "裂縫洞口"
      },
      {
        "direction": "up",
        "source_vnum": 18108,
        "target_area": "sec_spirit_peak",
        "target_room_vnum": 18801,
        "label": "白狼靈峰預留"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "落井入口帶" },
      { "id": "corridor", "label": "主甬道" },
      { "id": "side-room", "label": "偏廊與殘碑" },
      { "id": "sealed-core", "label": "封印核心帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 18101,
      "name": "裂縫落台",
      "description": "從白狼山的裂縫口滑落到這裡時，外頭的風聲像被石壁一層層壓遠，只剩冷濕的回音還留在耳邊。腳下石台不大，卻明確告訴人自己已經不在山前地表，而進入了更舊的地下空間。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 18006, "external": true },
        { "direction": "east", "to": 18102 }
      ],
      "enquires": ["上面", "退路", "洞口"]
    },
    {
      "vnum": 18102,
      "name": "潮濕前廳",
      "description": "前廳的石面被長年滲水磨得發亮，牆角還堆著辨不清年代的碎瓦與殘骨。這裡既像天然洞廳，又像曾被人刻意修整成某種入口前帶。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry",
      "coord": [1, 0, 0],
      "labels": ["foyer", "transition"],
      "exits": [
        { "direction": "west", "to": 18101 },
        { "direction": "east", "to": 18103 },
        { "direction": "south", "to": 18104 }
      ],
      "enquires": ["入口", "潮氣", "前面"]
    },
    {
      "vnum": 18103,
      "name": "斷紋甬道",
      "description": "甬道兩側殘留著一圈圈被切斷的紋路，像是某種封印曾經沿著石壁完整流動，卻在很久以前被硬生生打斷。越往裡走，洞中的回聲就越像壓低聲音的警告。",
      "sector_type": "SECT_INSIDE",
      "cluster": "corridor",
      "coord": [2, 0, 0],
      "labels": ["corridor", "seal-trace"],
      "exits": [
        { "direction": "west", "to": 18102 },
        { "direction": "east", "to": 18106 }
      ],
      "enquires": ["符文", "甬道", "深處"]
    },
    {
      "vnum": 18104,
      "name": "偏廊石室",
      "description": "偏廊旁的石室不算寬闊，卻留著不少被搬動過的痕跡，像有人曾把這裡當作暫時存放或躲藏之處。牆上的刮痕和地上的碎片都讓人懷疑這裡曾發生過倉促離去。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-room",
      "coord": [1, -1, 0],
      "labels": ["side-room", "debris"],
      "exits": [
        { "direction": "north", "to": 18102 },
        { "direction": "south", "to": 18105 }
      ],
      "enquires": ["石室", "痕跡", "碎片"]
    },
    {
      "vnum": 18105,
      "name": "殘碑暗井",
      "description": "暗井邊立著半截殘碑，碑面上的字早被水痕與青苔磨得難以辨讀，只剩幾筆像在反覆提醒後人不要再往下驚動什麼。這裡的靜比黑暗本身更有壓力。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-room",
      "coord": [1, -2, 0],
      "labels": ["well", "warning"],
      "exits": [
        { "direction": "north", "to": 18104 }
      ],
      "enquires": ["殘碑", "暗井", "警告"]
    },
    {
      "vnum": 18106,
      "name": "石門前廊",
      "description": "前廊盡頭的石門沒有真正關死，卻讓人很自然放慢腳步。門縫滲出的冷氣和石門周圍留下的刻痕，像是在共同守著後頭那個不該被輕率打開的核心。",
      "sector_type": "SECT_INSIDE",
      "cluster": "corridor",
      "coord": [3, 0, 0],
      "labels": ["anteroom", "threshold"],
      "exits": [
        { "direction": "west", "to": 18103 },
        { "direction": "east", "to": 18107 }
      ],
      "enquires": ["石門", "前廊", "裡面"]
    },
    {
      "vnum": 18107,
      "name": "封印主室",
      "description": "主室中央的地面與牆面交會處還能看見一圈圈殘破封紋，把這裡的空氣都壓得比外面更沉。即使封印早已不完整，留下的秩序感仍然強到像有人還在暗處守著它。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-core",
      "coord": [4, 0, 0],
      "labels": ["core", "sealed-room"],
      "exits": [
        { "direction": "west", "to": 18106 },
        { "direction": "north", "to": 18108 }
      ],
      "enquires": ["封印", "主室", "符紋"]
    },
    {
      "vnum": 18108,
      "name": "靈峰裂井",
      "description": "裂井一路往上收成一線極窄的冷光，讓人分不清那到底是地表的天光，還是更高處某種異樣空間的反照。站在井下時，會很自然感覺自己離普通洞窟已經不只一步之遙。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-core",
      "coord": [4, 1, 0],
      "labels": ["shaft", "world-link-up"],
      "exits": [
        { "direction": "south", "to": 18107 },
        { "direction": "up", "to": 18801, "external": true }
      ],
      "enquires": ["井口", "上方", "靈峰"]
    }
  ]
}
```
