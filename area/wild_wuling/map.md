# 武陵山 (`wild_wuling`)

## Area Intent

`wild_wuling` 承接 `city_changsha` 西向山路，讓玩家從荊南主城的穩定秩序，切進一段以山風、古樹、石碑、獵徑與谷地高差構成的武陵山前帶。

第一版目標先固定：

- 一條由東向西穿過山腳岔口、石碑路與靈木坡的主探索線
- 一條往谷地與獵徑偏帶延伸的側線
- 一條 `up/down` 連到山腹高地與霧帶谷口的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示武陵、長沙、山路、靈木與更深谷地

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `山路野外 / 靈木深山`
- LevelRange: `78-88`
- Parent region: `荊南西麓`
- World gap filled: 讓長沙西向支線正式化為主世界山區 wild，為後續更深武陵山谷與秘境預留穩定入口

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_wuling",
    "title": "武陵山",
    "design_notes": "第一版 spec-first 草案。先固定長沙西牌外的山腳岔口、石碑路、靈木坡與霧帶谷口骨架，讓主城節奏自然切進深山野外。",
    "level_range": "78-88",
    "planned_vnum_range": "15001-15030",
    "reserved_room_block": "15001-15030",
    "theme": {
      "primary": "仙俠",
      "secondary": "山路野外 / 靈木深山"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 15001,
        "target_area": "city_changsha",
        "label": "長沙西牌"
      },
      {
        "direction": "west",
        "source_vnum": 15010,
        "target_area": "wild_hidden_valley",
        "target_room_vnum": 19001,
        "label": "隱谷獵徑"
      },
      {
        "direction": "north",
        "source_vnum": 15011,
        "target_area": "city_jiangling",
        "target_room_vnum": 19301,
        "label": "北山關路"
      },
      {
        "direction": "east",
        "source_vnum": 15012,
        "target_area": "wild_spirit_forest",
        "target_room_vnum": 19201,
        "label": "東岔靈林"
      }
    ],
    "clusters": [
      { "id": "east-entry", "label": "東向山腳入口" },
      { "id": "stone-way", "label": "石碑山路" },
      { "id": "spirit-grove", "label": "靈木坡帶" },
      { "id": "ridge-path", "label": "山腹高徑" },
      { "id": "mist-hollow", "label": "霧帶谷口" }
    ]
  },
  "rooms": [
    {
      "vnum": 15001,
      "name": "山腳岔口",
      "description": "離開長沙西牌後，官道很快就被山腳碎石與樹影吃去一半，眼前這個岔口像在提醒旅人，從這裡開始已不再是主城的節奏。風裡帶著潮潤山氣，也帶著一點讓人想停下來重新辨位的警覺。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-link"],
      "exits": [
        { "direction": "east", "to": 14912, "external": true },
        { "direction": "west", "to": 15003 },
        { "direction": "north", "to": 15002 }
      ],
      "enquires": ["長沙", "山路"]
    },
    {
      "vnum": 15002,
      "name": "獵戶棚邊",
      "description": "幾根老木搭成的歇腳棚靠在坡邊，棚角還掛著乾藤與舊繩，像常有熟門熟路的人在這裡短暫停腳。比起主城的驛站，這裡更像山路自己的規矩，只供真正懂山的人使用。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-entry",
      "coord": [0, 1, 0],
      "labels": ["rest-shed", "side-path"],
      "exits": [
        { "direction": "south", "to": 15001 }
      ],
      "enquires": ["獵戶", "歇腳"]
    },
    {
      "vnum": 15003,
      "name": "石碑山路",
      "description": "山路邊立著半斜的舊石碑，碑面被風雨磨得發白，卻仍能看出曾有人試著替來路與去路留下秩序。踩在石礫路面上時，會明顯感覺到這條路既是通道，也是把人一點點送離主城保護的邊線。",
      "sector_type": "SECT_FIELD",
      "cluster": "stone-way",
      "coord": [-1, 0, 0],
      "labels": ["main-path", "landmark"],
      "exits": [
        { "direction": "east", "to": 15001 },
        { "direction": "west", "to": 15004 },
        { "direction": "south", "to": 15005 }
      ],
      "enquires": ["石碑", "出口"]
    },
    {
      "vnum": 15004,
      "name": "古藤坡道",
      "description": "坡道沿著老樹根與垂藤往上拉開，路不算難走，卻總讓人覺得四周正在慢慢把聲音吞掉。這裡像是武陵山真正開始有自己脾氣的地方，走得越深，越不容易再用主城的習慣去判斷它。",
      "sector_type": "SECT_FIELD",
      "cluster": "spirit-grove",
      "coord": [-2, 0, 0],
      "labels": ["slope", "grove"],
      "exits": [
        { "direction": "east", "to": 15003 },
        { "direction": "west", "to": 15007 },
        { "direction": "up", "to": 15009 }
      ],
      "enquires": ["靈木", "坡道"]
    },
    {
      "vnum": 15005,
      "name": "谷口碎徑",
      "description": "碎徑往下斜切進一段較低的谷口，兩旁濕苔與散岩把路壓得狹而長。你不一定會立刻覺得危險，但會很清楚地明白，這裡一旦走錯，回頭就不會像在主街轉個身那麼簡單。",
      "sector_type": "SECT_FIELD",
      "cluster": "mist-hollow",
      "coord": [-1, -1, -1],
      "labels": ["valley", "down"],
      "exits": [
        { "direction": "north", "to": 15003 },
        { "direction": "west", "to": 15006 }
      ],
      "enquires": ["谷地", "退路"]
    },
    {
      "vnum": 15006,
      "name": "霧帶窄口",
      "description": "一層薄霧總在這段窄口盤著不散，讓視線永遠像被留了一點餘地。風從谷裡吹上來時，會帶著草木與濕土混雜的味道，像在暗示前面還有更深、更難辨位的山腹區域。",
      "sector_type": "SECT_FIELD",
      "cluster": "mist-hollow",
      "coord": [-2, -1, -1],
      "labels": ["mist", "narrow-pass"],
      "exits": [
        { "direction": "east", "to": 15005 },
        { "direction": "west", "to": 15008 }
      ],
      "enquires": ["霧", "深處"]
    },
    {
      "vnum": 15007,
      "name": "靈木坡面",
      "description": "坡面上幾株老樹枝幹扭曲，樹皮裂紋裡卻透著異樣乾淨的木色，像整片山氣都在這裡停得比較久。這不是誇張得像秘境的景象，卻足夠讓人意識到武陵山和普通獵場終究不是一回事。",
      "sector_type": "SECT_FIELD",
      "cluster": "spirit-grove",
      "coord": [-3, 0, 0],
      "labels": ["spirit-wood", "wild-core"],
      "exits": [
        { "direction": "east", "to": 15004 },
        { "direction": "south", "to": 15008 },
        { "direction": "north", "to": 15011 }
      ],
      "keywords": [
        {
          "keyword": "靈木",
          "description": "老樹的裂痕與紋理都比尋常山林更醒目，像樹本身也記得這片山長久積下的氣息。"
        }
      ],
      "enquires": ["武陵", "古樹"]
    },
    {
      "vnum": 15008,
      "name": "山腹高徑",
      "description": "高徑沿著山腹橫出去，左側是林坡，右側則能隱約望見霧帶低谷。站在這裡時，前後左右都不像完全封死，卻也沒有哪一條路會讓人真的放鬆，這正是深山路最磨人的地方。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [-3, -1, 0],
      "labels": ["ridge", "crossing"],
      "exits": [
        { "direction": "north", "to": 15007 },
        { "direction": "east", "to": 15006 },
        { "direction": "west", "to": 15010 },
        { "direction": "down", "to": 15012 }
      ],
      "enquires": ["山腹", "岔路", "出口"]
    },
    {
      "vnum": 15009,
      "name": "高坡望石",
      "description": "一塊突出的望石卡在坡頂邊，從這裡能看見來時山路如何一段段縮回長沙方向。這樣的高度讓人暫時恢復方向感，卻也更明白再往西走，就會慢慢離開所有還算熟悉的邊界。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [-2, 0, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15004 }
      ],
      "enquires": ["望石", "長沙"]
    },
    {
      "vnum": 15010,
      "name": "隱谷西徑",
      "description": "再往西去，山路開始被更深的樹影與谷風分成幾股不太好辨的細線，像任何一步都可能讓人正式踏進另一片更不熟的山域。這裡不像終點，更像武陵山真正打開深處的門縫。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [-4, -1, 0],
      "labels": ["west-edge", "deep-link"],
      "exits": [
        { "direction": "east", "to": 15008 },
        { "direction": "west", "to": 19001, "external": true }
      ],
      "enquires": ["隱谷", "西邊"]
    },
    {
      "vnum": 15011,
      "name": "北山關痕",
      "description": "一段較舊的山道往北側斜出去，地上仍能看見久遠車轍與修路痕跡，像它曾經不只是獵人走的小道，而是更大範圍交通的一部分。這種痕跡讓武陵山顯得更厚，也更像真正接在世界骨架上的山區。",
      "sector_type": "SECT_FIELD",
      "cluster": "ridge-path",
      "coord": [-3, 1, 0],
      "labels": ["north-link", "old-road"],
      "exits": [
        { "direction": "south", "to": 15007 },
        { "direction": "north", "to": 19301, "external": true }
      ],
      "enquires": ["北路", "舊道"]
    },
    {
      "vnum": 15012,
      "name": "東岔靈林",
      "description": "一道往東偏去的林間岔路藏在山腹下方，樹影比來路更密，連地上的痕跡也細得幾乎只剩熟人能看懂。它像在提醒你，武陵山這一帶真正的複雜，往往不是眼前主路，而是那些看似安靜的小分叉。",
      "sector_type": "SECT_FIELD",
      "cluster": "mist-hollow",
      "coord": [-3, -2, -1],
      "labels": ["east-branch", "forest-link"],
      "exits": [
        { "direction": "up", "to": 15008 },
        { "direction": "east", "to": 19201, "external": true }
      ],
      "enquires": ["靈林", "岔路", "去路"]
    }
  ]
}
```
