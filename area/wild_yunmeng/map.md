# 雲夢大澤 (`wild_yunmeng`)

## Area Intent

`wild_yunmeng` 承接 `city_jiangxia` 南向水巷之外的第一段真正濕地前帶，讓玩家從有路牌、榜文與水軍巡視的江港秩序，正式滑進一片由蘆霧、泥灘、浮木與半沉石碑主導節奏的大澤探索區。

第一版目標先固定：

- 一條由北向南穿過濕地邊樁、蘆灘與霧中高埠的主探索線
- 一條向東偏折的草洲 / 倒木側線，用來提供短暫辨位與錯路風險
- 一條 `up/down` 連到高埠與半沉祭壇的非平面異聞支線
- 以 `#Enquire` / `#Keyword` 暗示江夏去路、大澤地標、下探入口與失蹤傳聞

這一版刻意讓玩家感受到：

- 一離開江夏城牆與港口，濕氣、霧聲與泥腳感就重新支配了所有路線判斷
- 這裡的壓力不是人更多，而是每條路都更像臨時生成、隨時可能消失
- 更深的詭異與沉陷遺跡正在地景裡慢慢浮出來，但還不急著把 dungeon 全部揭開

## Theme Positioning

- Theme: `詭異民俗`
- Subtheme: `雲夢大澤 / 迷霧濕地`
- LevelRange: `50-60`
- Parent region: `荊州南濕地`
- World gap filled: 讓主世界 progression 從江夏港城正式推進到雲夢濕地探索帶，並為更深沉沒遺跡或 swamp dungeon 建立前帶

## Player Flow

1. 玩家由江夏南向水巷踏入濕地邊樁，先感受到地面變軟、氣味變濕、聲音變散。
2. 蘆牆岔路與泥灘主線把城市節奏切碎成必須記地標的濕地探索節奏。
3. 草洲與倒木側線提供短暫喘息，也同時增加走錯方向的風險。
4. 半沉石碑與祭壇斷臺讓人看出這片大澤不只是自然地形，而是曾吞沒過人造痕跡的地方。
5. 霧中高埠與深沼前帶只把更深探索的吸力立起來，先不把沉沒神廟或密穴完全做滿。

## Cluster Notes

### `north-water-edge`

- 房間重點：水巷出口、濕地邊樁、第一段泥道
- 玩家感受：剛離開城市，還記得來路，但腳下已不再可靠
- 對外角色：作為接 `city_jiangxia` 南向邊界的正式入口

### `mist-marsh`

- 房間重點：迷霧泥灘、蘆牆岔路、積水窪口
- 玩家感受：視線變短、路感變弱，記憶地標比記方向更重要
- 對外角色：作為全區主探索線骨幹

### `reed-islet`

- 房間重點：半乾草洲、倒木短徑、舊棚殘架
- 玩家感受：像找到一口氣，卻不確定是不是正路
- 對外角色：提供濕地中的辨位點與支線節奏

### `sunken-marker`

- 房間重點：半沉石碑、祭壇斷臺、泥下磚痕
- 玩家感受：濕地裡有比自然更古老的東西正在被慢慢吞沒
- 對外角色：強化詭異民俗與下探 dungeon 的前置信號

### `deep-bog-front`

- 房間重點：霧心高埠、深沼入口、下探前帶
- 玩家感受：再往前，路就不只是濕地，而會真正沉進未知裡
- 對外角色：作為未來接 `dng_yunmeng_swamp` 的前帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `north` from `14501`: planned link to `city_jiangxia`
- `down` from `14512`: planned link to `dng_yunmeng_swamp`
- `south` from `14510`: planned link to `city_changsha`
- `east` from `14508`: planned link to `city_chaisang`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `去路 / 石碑 / 霧路 / 江夏 / 大澤`
- `#Keyword` 第一版會落在 `蘆葦 / 浮木 / 泥痕 / 石碑 / 祭壇`
- `#Job` 第一版暫不新增；等真正要做採集、尋人或追跡 loop 再補 job 與 runtime flow

## Suggested Layout

```text
江夏方向
   |
[14501] 水巷盡頭 -- [14502] 濕地邊樁 -- [14503] 蘆牆泥道 -- [14504] 迷霧岔灘 -- [14508] 霧中高埠 -- [14512] 深沼前帶
                                             |                                      |
                                             |                                      +-- down -- future dungeon
                                             |
                                             +-- east -- [14505] 半乾草洲 -- [14506] 倒木短徑 -- [14507] 舊棚殘架
                                                                                                    |
                                                                                                 south
                                                                                                    |
                                                                                                 [14511] 半沉祭壇

                                          [14509] 石碑泥潭 -- [14510] 南向蘆口
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_yunmeng",
    "title": "雲夢大澤",
    "design_notes": "第一版 spec-first 草案。先固定江夏南向水巷外的濕地入口、霧沼主線、草洲側線與半沉祭壇支線，讓主線從江港城市自然轉入詭異濕地探索。",
    "level_range": "50-60",
    "planned_vnum_range": "14501-14530",
    "reserved_room_block": "14501-14530",
    "theme": {
      "primary": "詭異民俗",
      "secondary": "雲夢大澤 / 迷霧濕地"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 14501,
        "target_area": "city_jiangxia",
        "label": "江夏南巷"
      },
      {
        "direction": "down",
        "source_vnum": 14512,
        "target_area": "dng_yunmeng_swamp",
        "label": "深沼裂口"
      },
      {
        "direction": "south",
        "source_vnum": 14510,
        "target_area": "city_changsha",
        "label": "荊南蘆口"
      },
      {
        "direction": "east",
        "source_vnum": 14508,
        "target_area": "city_chaisang",
        "label": "東澤水路"
      }
    ],
    "clusters": [
      { "id": "north-water-edge", "label": "北向濕地外沿" },
      { "id": "mist-marsh", "label": "迷霧主沼" },
      { "id": "reed-islet", "label": "蘆洲側線" },
      { "id": "sunken-marker", "label": "沉沒地標線" },
      { "id": "deep-bog-front", "label": "深沼前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 14501,
      "name": "水巷盡頭",
      "description": "江夏南向水巷在這裡終於收成一條被泥水吞咬的窄路，腳邊不再是整齊石地，而是一層一層被踩爛的濕草與水痕。回頭仍能辨出城裡的牆影，往前卻只剩蘆聲與霧氣慢慢把視線吞薄。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-water-edge",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-north"],
      "exits": [
        { "direction": "north", "to": 14407, "external": true },
        { "direction": "south", "to": 14502 }
      ],
      "enquires": ["江夏", "去路"]
    },
    {
      "vnum": 14502,
      "name": "濕地邊樁",
      "description": "幾根被水浸黑的木樁插在泥地邊，像是早有人想替這片濕地劃出一條能走的入口，只是如今樁與樁之間的界線早被霧和積水模糊得差不多了。再往前一步，地面就不像城外那樣肯老實承受人的重量。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-water-edge",
      "coord": [0, -1, 0],
      "labels": ["threshold", "mudline"],
      "exits": [
        { "direction": "north", "to": 14501 },
        { "direction": "south", "to": 14503 }
      ],
      "enquires": ["大澤", "前面"]
    },
    {
      "vnum": 14503,
      "name": "蘆牆泥道",
      "description": "蘆葦在兩側長得像牆一樣高，泥道被夾在中間，窄得只能容人專心看著腳下。偶爾有不知是鳥還是獸的聲音在霧後一閃而過，讓這條路既像有人帶過，又像從來沒真正屬於任何人。",
      "sector_type": "SECT_FIELD",
      "cluster": "mist-marsh",
      "coord": [0, -2, 0],
      "labels": ["main-route", "mist"],
      "exits": [
        { "direction": "north", "to": 14502 },
        { "direction": "south", "to": 14504 },
        { "direction": "east", "to": 14505 }
      ],
      "keywords": [
        {
          "keyword": "蘆葦",
          "description": "蘆葉上盡是潮珠，貼身擦過時帶來一種又冷又癢的濕意，像大澤正在用最細碎的方式記住每個闖進來的人。"
        }
      ],
      "enquires": ["霧路", "東邊"]
    },
    {
      "vnum": 14504,
      "name": "迷霧岔灘",
      "description": "地勢在這裡散成幾條濕灘和淺水交錯的岔路，哪一條像正路、哪一條像死路，往往要走進霧裡兩三步後才分得出來。泥面上留下的腳印也不像可靠指引，因為你很難確定那到底是人的，還是別的什麼。",
      "sector_type": "SECT_FIELD",
      "cluster": "mist-marsh",
      "coord": [0, -3, 0],
      "labels": ["fork", "uncertain"],
      "exits": [
        { "direction": "north", "to": 14503 },
        { "direction": "south", "to": 14508 },
        { "direction": "west", "to": 14509 }
      ],
      "keywords": [
        {
          "keyword": "泥痕",
          "description": "泥面上的痕跡有深有淺，有的像人踩過，有的卻更像什麼拖著濕重身子從霧裡慢慢滑過。"
        }
      ],
      "enquires": ["岔路", "石碑"]
    },
    {
      "vnum": 14505,
      "name": "半乾草洲",
      "description": "一小片略高於周圍泥面的草洲像在霧裡勉強浮著，雖不能算真正乾燥，至少比主沼的泥水更像能讓人站穩一口氣。草叢裡還留著些被踩歪的細枝，像不久前才有人在這裡短暫停過腳。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-islet",
      "coord": [1, -2, 0],
      "labels": ["islet", "breather"],
      "exits": [
        { "direction": "west", "to": 14503 },
        { "direction": "east", "to": 14506 }
      ],
      "enquires": ["草洲", "歇腳"]
    },
    {
      "vnum": 14506,
      "name": "倒木短徑",
      "description": "幾根橫倒的朽木恰好搭成一條勉強能踏的短徑，走在上面時木心發出空悶聲，彷彿底下全是更深的水與泥。這條路不像正式修成的橋，卻又明顯是走過的人不願再踩進泥裡時留下的選擇。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-islet",
      "coord": [2, -2, 0],
      "labels": ["fallen-log", "side-route"],
      "exits": [
        { "direction": "west", "to": 14505 },
        { "direction": "east", "to": 14507 }
      ],
      "keywords": [
        {
          "keyword": "浮木",
          "description": "這些木頭表面滑得厲害，邊緣還纏著藻絲，像是從更深處漂來後被人硬留在這裡充路。"
        }
      ]
    },
    {
      "vnum": 14507,
      "name": "舊棚殘架",
      "description": "幾根斜歪的棚柱從蘆霧裡突了出來，破蓆與碎繩還掛在柱頭，讓人看不出這裡曾是漁棚、獵棚，還是誰臨時搭來躲霧的地方。真正讓人在意的是，這殘架明明該荒了很久，卻又像最近才被誰碰過。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-islet",
      "coord": [3, -2, 0],
      "labels": ["shelter", "ominous"],
      "exits": [
        { "direction": "west", "to": 14506 },
        { "direction": "south", "to": 14511 }
      ],
      "enquires": ["失蹤", "棚子"]
    },
    {
      "vnum": 14508,
      "name": "霧中高埠",
      "description": "這一處地勢比周圍稍高，腳下泥意忽然薄了一層，讓人第一次能抬頭看清霧頂的走向。從這裡望出去，整片大澤像一層層灰白色的布往外鋪開，既讓人覺得終於能辨位，又更清楚意識到深處其實還有更沉、更黑的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "deep-bog-front",
      "coord": [0, -4, 1],
      "labels": ["high-ground", "outlook"],
      "exits": [
        { "direction": "north", "to": 14504 },
        { "direction": "down", "to": 14512 },
        { "direction": "east", "to": 14510 },
        { "direction": "west", "to": 14511 }
      ],
      "enquires": ["高處", "大澤", "東邊"]
    },
    {
      "vnum": 14509,
      "name": "石碑泥潭",
      "description": "半截石碑斜斜插在泥潭裡，碑面被水紋與青苔蓋得難以辨字，卻仍能看出它原本不該立在這種地方。四周泥水安靜得過分，連霧都像在繞著碑身走，讓人很難不把這裡當成某種刻意留下的記號。",
      "sector_type": "SECT_FIELD",
      "cluster": "sunken-marker",
      "coord": [-1, -3, 0],
      "labels": ["marker", "ruin"],
      "exits": [
        { "direction": "east", "to": 14504 },
        { "direction": "south", "to": 14510 }
      ],
      "keywords": [
        {
          "keyword": "石碑",
          "description": "碑角已被泥水磨圓，碑身卻還殘留幾道像祭刻或地名的舊痕，讓人覺得它或許曾為一條更早以前的路指過方向。"
        }
      ],
      "enquires": ["石碑", "地標"]
    },
    {
      "vnum": 14510,
      "name": "南向蘆口",
      "description": "蘆牆在這裡裂出一道更長、更暗的南向開口，風從裡頭吹來時夾著一股更厚的泥腥與水草味。這道去路不像通往正常官道，倒更像把人慢慢引進一整片不願被地圖記清的地方。",
      "sector_type": "SECT_FIELD",
      "cluster": "sunken-marker",
      "coord": [1, -4, 0],
      "labels": ["south-edge", "future-link-south"],
      "exits": [
        { "direction": "north", "to": 14509 },
        { "direction": "west", "to": 14508 }
      ],
      "enquires": ["南邊", "去路"]
    },
    {
      "vnum": 14511,
      "name": "半沉祭壇",
      "description": "幾塊被泥水吞到只剩稜角的石臺在這裡勉強拼出一個圓形輪廓，中央則陷成更黑的一潭。你很難說這是祭壇、舊祠基，還是某種被故意掩埋的入口，但站在旁邊時，總會覺得腳下的泥比別處更像在慢慢往下拉人。",
      "sector_type": "SECT_FIELD",
      "cluster": "sunken-marker",
      "coord": [-1, -4, -1],
      "labels": ["ritual", "downward-pull"],
      "exits": [
        { "direction": "east", "to": 14508 },
        { "direction": "north", "to": 14507 },
        { "direction": "up", "to": 14512 }
      ],
      "keywords": [
        {
          "keyword": "祭壇",
          "description": "石臺邊緣刻痕早被泥與水磨平，唯獨中央的下陷處仍像保留著某種不想完全露面的形狀。"
        }
      ],
      "enquires": ["祭壇", "下面"]
    },
    {
      "vnum": 14512,
      "name": "深沼前帶",
      "description": "高埠下方的霧在這裡聚成一團更濃的灰白，連腳下積水都黑得像沒有底。四周聲音忽然變少，只剩偶爾一聲從泥底或霧心傳來的悶響，提醒你再往前一步，走的就不再只是大澤表面了。",
      "sector_type": "SECT_FIELD",
      "cluster": "deep-bog-front",
      "coord": [0, -5, 0],
      "labels": ["deep-edge", "world-link-down"],
      "exits": [
        { "direction": "up", "to": 14508 },
        { "direction": "down", "to": 14511 }
      ],
      "enquires": ["深處", "下面", "去路"]
    }
  ]
}
```
