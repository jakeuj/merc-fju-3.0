# 白狼靈峰 (`sec_spirit_peak`)

## Area Intent

`sec_spirit_peak` 承接 `dng_ancient_cave` 的靈峰裂井，把白狼山地下遺跡之上的冷光與封印痕跡正式翻成一段更明亮、更稀有、也更帶祭壇與天象回聲的高處 secret。這裡不再像洞窟那樣靠回音與黑暗壓迫人，而是讓玩家感受到自己正踏進一個仍被古老祭天秩序勉強撐住的北境祕境。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `靈峰 / 祭天`
- LevelRange: `44-56`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_spirit_peak",
    "title": "白狼靈峰",
    "design_notes": "第一版 spec-first 草案。先固定靈峰井口、風祭石階、雲裂祭坪、狼紋天壇、祈霧側壇、裂光峰脊、靈泉祭井與天熒觀台，把古洞裂井之上的高處祕境正式展成可載入的北境 secret。",
    "level_range": "44-56",
    "planned_vnum_range": "18801-18820",
    "reserved_room_block": "18801-18820",
    "theme": {
      "primary": "仙俠",
      "secondary": "靈峰 / 祭天"
    },
    "world_links": [
      {
        "direction": "down",
        "source_vnum": 18801,
        "target_area": "dng_ancient_cave",
        "target_room_vnum": 18108,
        "label": "靈峰裂井"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "裂井入口帶" },
      { "id": "ritual", "label": "祭階與祭坪" },
      { "id": "altar", "label": "天壇與側壇" },
      { "id": "summit", "label": "峰脊與觀台" }
    ]
  },
  "rooms": [
    {
      "vnum": 18801,
      "name": "靈峰井口",
      "description": "從古洞的裂井一路往上攀到這裡時，最先撞上的不是山風，而是一種帶著光意的高處靜壓。井口四周的石面像被很久以前的祭火燒亮過，讓人很難把這裡只當成地下出口。",
      "sector_type": "SECT_HILLS",
      "cluster": "entry",
      "coord": [0, 0, 1],
      "labels": ["entry", "down-edge", "world-link-down", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 18108, "external": true },
        { "direction": "north", "to": 18802 }
      ],
      "enquires": ["下面", "井口", "古洞"]
    },
    {
      "vnum": 18802,
      "name": "風祭石階",
      "description": "一段被長年山風磨白的石階一路往上收，踏面上還能隱約辨出早已淡去的祭行刻痕。每往上一步，都會更清楚感到這裡曾是某種把天象與山勢一起納進秩序的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "ritual",
      "coord": [0, 1, 1],
      "labels": ["stairs", "ritual-route"],
      "exits": [
        { "direction": "south", "to": 18801 },
        { "direction": "north", "to": 18803 },
        { "direction": "east", "to": 18805 }
      ],
      "enquires": ["石階", "祭路", "山風"]
    },
    {
      "vnum": 18803,
      "name": "雲裂祭坪",
      "description": "祭坪正好卡在雲勢最容易被山脊撕開的位置，讓上方天光與下方陰影像在這裡反覆交手。站在坪上時，最容易產生的念頭不是抬頭看風景，而是懷疑這片空地原本就不是給凡常人停留的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "ritual",
      "coord": [0, 2, 1],
      "labels": ["plaza", "skybreak"],
      "exits": [
        { "direction": "south", "to": 18802 },
        { "direction": "east", "to": 18804 },
        { "direction": "up", "to": 18806 }
      ],
      "enquires": ["祭坪", "雲裂", "光"]
    },
    {
      "vnum": 18804,
      "name": "狼紋天壇",
      "description": "天壇石面上還殘著像狼紋又像星軌的圓環刻痕，把整座高臺的古怪感壓得很實。它不像單純祭壇，更像一處曾拿來對照山、狼與天象異動的核心場所。",
      "sector_type": "SECT_HILLS",
      "cluster": "altar",
      "coord": [1, 2, 1],
      "labels": ["altar", "wolf-mark", "core"],
      "exits": [
        { "direction": "west", "to": 18803 }
      ],
      "enquires": ["天壇", "狼紋", "異象"]
    },
    {
      "vnum": 18805,
      "name": "祈霧側壇",
      "description": "側壇比主祭坪更小，也更像是留給真正懂儀式的人短暫停步調息的地方。石邊還擺著幾件不知何時留下的祭器殘件，讓人相信這片靈峰並不是只有一條進退路。",
      "sector_type": "SECT_HILLS",
      "cluster": "altar",
      "coord": [1, 1, 1],
      "labels": ["side-altar", "rest", "ritual"],
      "exits": [
        { "direction": "west", "to": 18802 },
        { "direction": "north", "to": 18807 }
      ],
      "enquires": ["側壇", "祭器", "霧"]
    },
    {
      "vnum": 18806,
      "name": "裂光峰脊",
      "description": "峰脊把天光切成一道道偏白的裂線，讓整條山脊像正被更高處某種看不見的秩序重新描過。這裡的危險不來自狹窄本身，而來自一種越往前越難確定自己是否仍站在凡間地勢上的不穩感。",
      "sector_type": "SECT_HILLS",
      "cluster": "summit",
      "coord": [0, 2, 2],
      "labels": ["ridge", "light", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 18803 },
        { "direction": "north", "to": 18808 }
      ],
      "enquires": ["峰脊", "裂光", "前面"]
    },
    {
      "vnum": 18807,
      "name": "靈泉祭井",
      "description": "一口清冷得近乎沒有聲音的祭井嵌在側壇後方，井邊水痕卻不帶半點俗世濕氣，反而像把整片靈峰的亮度都收進去了。很多關於祭天與啟路的傳聞，在這裡看起來都突然有了實感。",
      "sector_type": "SECT_HILLS",
      "cluster": "summit",
      "coord": [1, 2, 0],
      "labels": ["well", "ritual-water", "low"],
      "exits": [
        { "direction": "south", "to": 18805 },
        { "direction": "east", "to": 18808 }
      ],
      "enquires": ["靈泉", "祭井", "水"]
    },
    {
      "vnum": 18808,
      "name": "天熒觀台",
      "description": "觀台上方的天色比正常高處更亮，像整片山與雲都在這裡默默把光聚成一口看不見的火。站在這裡時，很難分清自己看到的是遠景、異象，還是某種只願意短暫讓人窺見的舊秩序殘影。",
      "sector_type": "SECT_HILLS",
      "cluster": "summit",
      "coord": [1, 3, 2],
      "labels": ["observatory", "summit", "high"],
      "exits": [
        { "direction": "south", "to": 18806 },
        { "direction": "west", "to": 18807 }
      ],
      "enquires": ["觀台", "天光", "遠處"]
    }
  ]
}
```
