# 蛇神殿 (`dng_serpent_temple`)

## Area Intent

`dng_serpent_temple` 承接 `wild_nanman_jungle` 的林下祠痕，讓玩家從仍有退路感的密林前帶，一步踏進更封閉、更幽深、也更帶血祭壓力的蛇神殿。

第一版目標先固定：

- 一條由上而下穿過前廳、甬道與祭槽偏殿的主下探線
- 一條往殘骨儲室與封紋側室延伸的側線
- 一條 `up/down` 連到更深井口與封印內殿的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示蛇殿、密林、退路、封印與更深地宮

## Theme Positioning

- Theme: `詭異民俗`
- Subtheme: `蛇殿 / 血祭`
- LevelRange: `98-100`
- Parent region: `南蠻林下遺構`
- World gap filled: 讓南蠻密林的林下古祠正式延伸成可進入的蛇神殿 dungeon，為後續更深 jungle ruins 與秘殿支線建立封閉型下探起點

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_serpent_temple",
    "title": "蛇神殿",
    "design_notes": "第一版 spec-first 草案。先固定林下祠痕之下的潮濕前廳、蛇紋甬道、祭槽偏殿、封紋內殿與深井入口，讓南蠻支線由開放密林切進封閉 dungeon。",
    "level_range": "98-100",
    "planned_vnum_range": "15401-15430",
    "reserved_room_block": "15401-15430",
    "theme": {
      "primary": "詭異民俗",
      "secondary": "蛇殿 / 血祭"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 15401,
        "target_area": "wild_nanman_jungle",
        "label": "林下祠痕"
      },
      {
        "direction": "down",
        "source_vnum": 15411,
        "target_area": "sec_jungle_ruins",
        "label": "深封地宮"
      },
      {
        "direction": "enter",
        "source_vnum": 15410,
        "target_area": "dng_serpent_sanctum",
        "label": "內祭殿"
      }
    ],
    "clusters": [
      { "id": "entry-hall", "label": "潮濕前廳" },
      { "id": "serpent-corridor", "label": "蛇紋甬道" },
      { "id": "ritual-chamber", "label": "祭槽偏殿" },
      { "id": "sealed-core", "label": "封紋內殿" },
      { "id": "deep-shaft", "label": "深井入口" }
    ]
  },
  "rooms": [
    {
      "vnum": 15401,
      "name": "潮濕前廳",
      "description": "沿著林下石階往下，最先抵達的是一座潮氣沉重得近乎貼在皮膚上的前廳。外頭密林的雜聲在這裡像被石壁整片壓住，只剩滴水與空殿回音提醒你，上面的世界還沒有完全消失。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-hall",
      "coord": [0, 0, 0],
      "labels": ["entry", "up-link"],
      "exits": [
        { "direction": "up", "to": 15311, "external": true },
        { "direction": "south", "to": 15403 },
        { "direction": "east", "to": 15402 }
      ],
      "enquires": ["密林", "退路"]
    },
    {
      "vnum": 15402,
      "name": "側壁殘龕",
      "description": "牆邊幾座半毀石龕只剩模糊輪廓，像裡頭曾放過什麼被人刻意挖走或砸碎的祭物。即使不懂這座蛇殿過去的規矩，也看得出這裡曾有一段不容旁人插手的秩序。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-hall",
      "coord": [1, 0, 0],
      "labels": ["side-alcove", "remains"],
      "exits": [
        { "direction": "west", "to": 15401 }
      ],
      "enquires": ["石龕", "前廳"]
    },
    {
      "vnum": 15403,
      "name": "蛇紋甬道",
      "description": "甬道兩側的石壁刻滿彼此纏繞的蛇紋，燭火若亮起時，大概會讓那些線條看起來像正在牆上滑動。走在這裡時，方向感不像在密林裡那樣會散掉，反而會被逼著一直往更深處集中。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "serpent-corridor",
      "coord": [0, -1, 0],
      "labels": ["main-corridor", "serpent-mark"],
      "exits": [
        { "direction": "north", "to": 15401 },
        { "direction": "south", "to": 15404 },
        { "direction": "west", "to": 15405 }
      ],
      "enquires": ["蛇殿", "深處"]
    },
    {
      "vnum": 15404,
      "name": "滴血祭槽",
      "description": "地面中央凹下一道長槽，邊緣堆著暗沉發黑的痕跡，讓人很難不往血祭方向聯想。這裡沒有聲音，也沒有主持儀式的人，卻比任何熱鬧場面更能讓人理解這座殿真正信奉的是什麼。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-chamber",
      "coord": [0, -2, 0],
      "labels": ["ritual", "mainline"],
      "exits": [
        { "direction": "north", "to": 15403 },
        { "direction": "east", "to": 15407 },
        { "direction": "south", "to": 15408 }
      ],
      "keywords": [
        {
          "keyword": "血槽",
          "description": "石槽邊緣的暗痕一層壓著一層，像這裡曾長久重複某種把生命送入深處的儀式。"
        }
      ],
      "enquires": ["祭槽", "血祭"]
    },
    {
      "vnum": 15405,
      "name": "殘骨儲室",
      "description": "側室裡散著不知來自獸類還是人的舊骨，牆邊還殘留幾個被鐵鍊拖磨過的固定孔。比起恐怖，這裡更讓人感受到一種被制度化保存下來的殘酷。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-chamber",
      "coord": [-1, -1, 0],
      "labels": ["bones", "side-room"],
      "exits": [
        { "direction": "east", "to": 15403 }
      ],
      "enquires": ["殘骨", "側室"]
    },
    {
      "vnum": 15406,
      "name": "封鍊轉角",
      "description": "幾條仍釘在牆裡的粗鍊沿著轉角往更裡側拖去，彷彿曾有什麼龐大又不甘被困的東西在這裡掙扎過。你不確定它現在還在不在，但光是痕跡就足以讓人下意識放輕腳步。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "serpent-corridor",
      "coord": [-1, -2, 0],
      "labels": ["chains", "turn"],
      "exits": [
        { "direction": "south", "to": 15410 }
      ],
      "enquires": ["鎖鍊", "轉角"]
    },
    {
      "vnum": 15407,
      "name": "符燼偏室",
      "description": "偏室角落仍積著一些燒完後發灰的符紙與細沙，像有人曾試圖用另一套規則對抗這座蛇殿原本的力量。可惜從眼前剩下的結果看來，那場對抗沒有真正把它封死。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-chamber",
      "coord": [1, -2, 0],
      "labels": ["runes", "side-room"],
      "exits": [
        { "direction": "west", "to": 15404 }
      ],
      "enquires": ["符文", "偏室"]
    },
    {
      "vnum": 15408,
      "name": "封紋內殿",
      "description": "內殿比前面的房間更高，石面上層層重疊的蛇紋與封紋像還在彼此爭奪主導權。站在這裡時，會明顯感覺到上面的密林只是門面，真正不肯輕易示人的東西一直都沉在這更下方。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-core",
      "coord": [0, -3, 0],
      "labels": ["core", "sealed"],
      "exits": [
        { "direction": "north", "to": 15404 },
        { "direction": "west", "to": 15410 },
        { "direction": "south", "to": 15411 },
        { "direction": "up", "to": 15409 }
      ],
      "enquires": ["封印", "內殿"]
    },
    {
      "vnum": 15409,
      "name": "裂頂窺臺",
      "description": "沿著殿側崩裂的石階上到這裡後，可以從頂部裂隙看見一點極遠的綠光，像密林世界還隔著許多層岩壁對你留了一絲證明。這樣的高度並不帶來安全，只會讓人更清楚自己陷得多深。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-core",
      "coord": [0, -3, 1],
      "labels": ["up", "lookback"],
      "exits": [
        { "direction": "down", "to": 15408 }
      ],
      "enquires": ["上面", "裂隙"]
    },
    {
      "vnum": 15410,
      "name": "內祭石門",
      "description": "一道厚重石門卡在內殿西側，門縫裡透出的不是風，而是一種像被壓住太久的悶熱與腥味。你幾乎不用打開它，就知道門後不會只是普通祭室。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-core",
      "coord": [-1, -3, 0],
      "labels": ["enter-link", "stone-door"],
      "exits": [
        { "direction": "north", "to": 15406 },
        { "direction": "east", "to": 15408 }
      ],
      "enquires": ["石門", "內祭殿"]
    },
    {
      "vnum": 15411,
      "name": "深井入口",
      "description": "內殿更下方裂開一道被石欄半圈住的井口，冷氣與水聲從底下不斷往上翻。這裡不像單純的地洞，更像整座蛇神殿真正把秘密收起來的喉口。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-shaft",
      "coord": [0, -4, -1],
      "labels": ["down-link", "shaft"],
      "exits": [
        { "direction": "north", "to": 15408 },
        { "direction": "east", "to": 15412 }
      ],
      "enquires": ["下方", "井口"]
    },
    {
      "vnum": 15412,
      "name": "井邊退台",
      "description": "井口側邊有一塊較平的退台，像是讓人暫時檢查繩索、火把或膽量的最後位置。站在這裡時，會很自然地重新確認一次自己是否真的準備好把退路留在身後。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-shaft",
      "coord": [1, -4, -1],
      "labels": ["ledge", "last-stop"],
      "exits": [
        { "direction": "west", "to": 15411 }
      ],
      "enquires": ["退路", "準備"]
    }
  ]
}
```
