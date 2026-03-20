# 沉舟墓場 (`dng_boat_graveyard`)

## Area Intent

`dng_boat_graveyard` 承接 `wild_south_sea_route` 南航分水外側的渦潮沉舟帶，讓玩家從看風、看潮、看浮標的海路 wild，切進一段由殘桅、裂艙、錨鏈與沉鐘構成的封閉 wreck dungeon。

第一版目標先固定：

- 一條由渦潮入口往船腹深處推進的主下探線
- 一條往偏艙與掛橋延伸的側線
- 一條 `up/down` 連到錨鏈井口與更深沉艙的非平面下探線
- 以 `#Enquire` / `#Keyword` 暗示沉舟、錨鏈、沉鐘、退路與更深水府

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `沉舟 / 水鬼`
- LevelRange: `99-100`
- Parent region: `南境外海沉舟帶`
- World gap filled: 讓南海外航道外側正式出現第一層可進入的 wreck dungeon，為後續深海水府與外海群島題材建立遺跡前帶

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_boat_graveyard",
    "title": "沉舟墓場",
    "design_notes": "第一版 spec-first 草案。先固定渦潮裂口、破桅前廊、漏艙窄道、中艙殘庭、錨鏈井口與深艙鐘影，讓海路主線在真正遠離近岸前先經過一層更封閉的 wreck dungeon。",
    "level_range": "99-100",
    "planned_vnum_range": "15701-15730",
    "reserved_room_block": "15701-15730",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "沉舟 / 水鬼"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 15701,
        "target_area": "wild_south_sea_route",
        "label": "南航分水"
      },
      {
        "direction": "down",
        "source_vnum": 15710,
        "target_area": "sec_water_ruins",
        "label": "深海水府"
      },
      {
        "direction": "south",
        "source_vnum": 15712,
        "target_area": "sea_outer_isles",
        "label": "外海群島"
      }
    ],
    "clusters": [
      { "id": "maelstrom-entry", "label": "渦潮入口" },
      { "id": "broken-hull", "label": "破艙主線" },
      { "id": "bone-hold", "label": "偏艙殘骨" },
      { "id": "anchor-shaft", "label": "錨鏈井口" },
      { "id": "deep-bell", "label": "深艙鐘影" }
    ]
  },
  "rooms": [
    {
      "vnum": 15701,
      "name": "渦潮裂口",
      "description": "南航分水下方有一道被亂流與破船殘骨撕出的裂口，水聲從四周擠壓過來，像任何回頭的念頭都會被潮流先壓低一截。只要再往裡一步，海路的開闊感就會立刻被沉舟的陰影吞掉。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "maelstrom-entry",
      "coord": [0, 0, -1],
      "labels": ["entry", "up-link"],
      "exits": [
        { "direction": "up", "to": 15610, "external": true },
        { "direction": "south", "to": 15703 },
        { "direction": "east", "to": 15702 }
      ],
      "enquires": ["退路", "上面", "沉舟"]
    },
    {
      "vnum": 15702,
      "name": "破桅前廊",
      "description": "幾截斷裂船桅斜插在前廊邊，木紋和鏽釘都被海水泡得發黑，像一群還不肯完全倒下的殘兵。站在這裡時，連光線都像被船骨分割成破碎的幾段。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "maelstrom-entry",
      "coord": [1, 0, -1],
      "labels": ["mast", "foyer"],
      "exits": [
        { "direction": "west", "to": 15701 }
      ],
      "enquires": ["殘桅", "前面"]
    },
    {
      "vnum": 15703,
      "name": "漏艙窄道",
      "description": "窄道兩側艙壁不停滲著海水，腳邊偶爾還會被卷過來的碎木與海草擦過。這裡不像一條真正留給人走的路，卻偏偏仍保留著足夠讓人繼續深入的縫隙。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "broken-hull",
      "coord": [0, -1, -1],
      "labels": ["main-path", "hull"],
      "exits": [
        { "direction": "north", "to": 15701 },
        { "direction": "south", "to": 15704 },
        { "direction": "west", "to": 15705 }
      ],
      "enquires": ["艙道", "退路"]
    },
    {
      "vnum": 15704,
      "name": "沉索轉角",
      "description": "厚重濕索在轉角纏成一團，像有人當年急著想把整艘船拴住，最後卻只把絕望留在這裡。你每跨過一圈繩索，都像跨過一段失敗遠航留下的最後秩序。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "broken-hull",
      "coord": [0, -2, -1],
      "labels": ["rope", "turn"],
      "exits": [
        { "direction": "north", "to": 15703 },
        { "direction": "south", "to": 15708 },
        { "direction": "east", "to": 15707 }
      ],
      "enquires": ["繩索", "更深"]
    },
    {
      "vnum": 15705,
      "name": "潮骨偏艙",
      "description": "偏艙裡堆著被海水洗得發白的殘骨與器具，像船難後所有來不及記下名字的人都只剩下這種安靜。這裡不吵，卻讓人比任何吵鬧都更清楚地感到不安。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "bone-hold",
      "coord": [-1, -1, -1],
      "labels": ["side-room", "bones"],
      "exits": [
        { "direction": "east", "to": 15703 },
        { "direction": "south", "to": 15706 }
      ],
      "enquires": ["殘骨", "偏艙"]
    },
    {
      "vnum": 15706,
      "name": "斷槳台",
      "description": "幾支斷槳和折裂木座橫在一塊微微抬高的平台上，像整艘船最後還想保住一點向前的姿勢。可在這種地方，任何前進的象徵看起來都只剩下諷刺。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "bone-hold",
      "coord": [-1, -2, -1],
      "labels": ["oars", "platform"],
      "exits": [
        { "direction": "north", "to": 15705 },
        { "direction": "east", "to": 15708 }
      ],
      "enquires": ["斷槳", "方向"]
    },
    {
      "vnum": 15707,
      "name": "船鐘暗壁",
      "description": "一口撞裂的船鐘半陷在暗壁邊，潮聲一撞上金屬殘面，便會拖出低沉得像嘆息的回音。它不再報時，卻仍能把人在這艘船裡停留得過久這件事，提醒得分外清楚。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "bone-hold",
      "coord": [1, -2, -1],
      "labels": ["bell", "echo"],
      "exits": [
        { "direction": "west", "to": 15704 },
        { "direction": "south", "to": 15709 }
      ],
      "keywords": [
        {
          "keyword": "沉鐘",
          "description": "裂開的船鐘仍會在潮聲裡擠出低啞回音，像這艘船的最後一點規矩還不肯完全散掉。"
        }
      ],
      "enquires": ["沉鐘", "回音"]
    },
    {
      "vnum": 15708,
      "name": "中艙殘庭",
      "description": "這片原本該是船腹中央的開闊艙段，如今只剩被扯裂的木梁與向內傾斜的艙壁，把它變成一座扭曲又過於安靜的殘庭。從這裡再往前，深處的壓力已經開始不再只是水，而像某種更久遠的怨氣。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "broken-hull",
      "coord": [0, -3, -1],
      "labels": ["core", "midship"],
      "exits": [
        { "direction": "north", "to": 15704 },
        { "direction": "west", "to": 15706 },
        { "direction": "east", "to": 15709 },
        { "direction": "down", "to": 15711 }
      ],
      "enquires": ["中艙", "下面", "深處"]
    },
    {
      "vnum": 15709,
      "name": "錨鏈井口",
      "description": "粗重錨鏈從井口一路沉進黑得看不清底的船腹深處，鏈節彼此磨碰時發出的聲音，像有人正在下面慢慢整理另一種完全不屬於活人的秩序。這裡很明顯已經不是單純殘骸，而是深處真正開始接管人的地方。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "anchor-shaft",
      "coord": [1, -3, -1],
      "labels": ["anchor", "shaft"],
      "exits": [
        { "direction": "north", "to": 15707 },
        { "direction": "west", "to": 15708 },
        { "direction": "south", "to": 15710 }
      ],
      "enquires": ["錨鏈", "井口"]
    },
    {
      "vnum": 15710,
      "name": "墓場深艙",
      "description": "深艙裡的海水幾乎靜得異常，碎木、殘布與不知名影子都像被同一種沉默按在水面下。你站在這裡時，會很自然地理解，這艘船之所以還留著，不只是因為沒沉完，而是因為深處還有東西不肯讓它散掉。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "deep-bell",
      "coord": [1, -4, -2],
      "labels": ["deep-core", "down-link"],
      "exits": [
        { "direction": "north", "to": 15709 },
        { "direction": "west", "to": 15711 }
      ],
      "enquires": ["深處", "下面", "水府"]
    },
    {
      "vnum": 15711,
      "name": "浮屍掛橋",
      "description": "幾根斷裂橫梁和繩索勉強在更低一層搭出一段掛橋，橋下則是看不清深度的黑水。這裡最可怕的不是搖晃，而是你很難分辨那些在下方輕碰木梁的聲音，到底只是水還是別的東西。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "anchor-shaft",
      "coord": [0, -4, -2],
      "labels": ["bridge", "lower-deck"],
      "exits": [
        { "direction": "up", "to": 15708 },
        { "direction": "east", "to": 15710 },
        { "direction": "south", "to": 15712 }
      ],
      "enquires": ["掛橋", "退路"]
    },
    {
      "vnum": 15712,
      "name": "外海破舷",
      "description": "南側破舷已被海流徹底撕開，視線能穿過殘木看見更南方更開闊卻也更陌生的海面。這裡不像出口，更像整艘沉舟最後用殘骸指向外海的一道裂口。 ",
      "sector_type": "SECT_WATER_SWIM",
      "cluster": "deep-bell",
      "coord": [0, -5, -2],
      "labels": ["south-edge", "outer-sea"],
      "exits": [
        { "direction": "north", "to": 15711 }
      ],
      "enquires": ["外海", "南邊", "出去"]
    }
  ]
}
```
