# 江夏 (`city_jiangxia`)

## Area Intent

`city_jiangxia` 承接 `wild_jiangxia_river` 東向渡口前帶之後的第一座真正江港主城，讓玩家從蘆葦、泥岸與水寨殘樁之間的江路壓力，重新回到一座以碼頭秩序、港務差役、水軍哨棚與市集補給共同運作的荊州東岸重鎮。

第一版目標先固定：

- 一條由西向東穿過渡口外門、港前木棧與主街的主探索線
- 一條向南折進補給市集與藥鋪雜貨的城市服務側線
- 一條 `up/down` 連到堤岸望臺與水軍哨棚的非平面軍務支線
- 以 `#Enquire` / `#Keyword` 暗示碼頭、官府、水軍、柴桑與雲夢方向

這一版刻意讓玩家感受到：

- 從江岸野外進城後，第一個改變不是建築更密，而是秩序、標示與人聲重新回來
- 江夏的城市辨識度來自港口與水軍，而不是單純複製襄陽的主街模型
- 這裡既是補給點，也是往柴桑與雲夢再度分流的水陸節點

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `江港水軍 / 荊州東岸重鎮`
- LevelRange: `45-55`
- Parent region: `荊州東岸`
- World gap filled: 讓主世界 progression 從襄陽外水路正式進入江夏港城，並為後續柴桑與雲夢鏈建立主城 hub

## Player Flow

1. 玩家從候船路牌與外港木棧踏進江夏西側渡口，先感受到驗貨、繫纜與巡查帶來的城市秩序。
2. 港前街把水路旅程收束成一條清晰主線，重新接回可問路、可補給的城市節奏。
3. 市集側線提供藥品、乾糧、船具與雜貨的服務辨識，讓江港城市真正有停留價值。
4. 水軍官署與堤上望臺讓人看出這裡不只是通商碼頭，也是監控船路與兵船調動的重鎮。
5. 東向主街先把柴桑吸力立起來，南向巷口則為雲夢方向預留更潮濕、更多變的後續路線。

## Cluster Notes

### `west-ferry-gate`

- 房間重點：渡口外門、驗貨棚、進城牌坊
- 玩家感受：剛離開江岸野外，就被城市秩序重新接住
- 對外角色：作為接 `wild_jiangxia_river` 的正式西向邊界

### `harbor-front`

- 房間重點：外港木棧、纜樁、候工棚
- 玩家感受：人與貨開始匯流，江港節奏正式成形
- 對外角色：作為全區主探索線與港務辨識骨幹

### `main-street`

- 房間重點：主街、路牌、榜文牆、東向幹道
- 玩家感受：重新回到能辨位、能問路、能補給的主城中心
- 對外角色：把西側渡口與東向主線串成清晰 hub

### `market-yard`

- 房間重點：藥鋪、乾糧攤、船具棚、雜貨鋪
- 玩家感受：這座城市是真的靠船路與旅人吃飯
- 對外角色：提供日後 runtime 服務 NPC 的自然落點

### `naval-yamen`

- 房間重點：港務官署、水軍營棚、堤上望臺
- 玩家感受：港口背後有制度與兵力，不只是熱鬧商街
- 對外角色：強化三國江港與水軍題材辨識度

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `west` from `14401`: planned link to `wild_jiangxia_river`
- `east` from `14412`: planned link to `city_chaisang`
- `south` from `14407`: planned link to `wild_yunmeng`
- `north` from `14410`: planned link to `jingxiang_road`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `碼頭 / 主街 / 市集 / 官府 / 水軍 / 柴桑`
- `#Keyword` 第一版會落在 `路牌 / 榜文 / 纜樁 / 帆索 / 船鐘`
- `#Job` 第一版暫不新增；等真正要做港務跑腿、船單傳遞或水軍巡防 loop 再補 job 與 runtime flow

## Suggested Layout

```text
江岸水路方向
   |
[14401] 渡口外門 -- [14402] 驗貨棚前 -- [14403] 外港木棧 -- [14404] 港前街口 -- [14408] 主街十字 -- [14412] 東向幹道
                                             |                                   |
                                             |                                   +-- up -- [14409] 堤上望臺 -- [14410] 水軍哨棚
                                             |
                                             +-- south -- [14405] 乾貨市集 -- [14406] 藥鋪前巷 -- [14407] 南向水巷
                                                                                                  |
                                                                                               east
                                                                                                  |
                                                                                               [14411] 港務官署
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_jiangxia",
    "title": "江夏",
    "design_notes": "第一版 spec-first 草案。先固定西渡口、港前主街、市集補給與水軍官署高差，讓江夏能作為襄陽之後的第一座江港主城。",
    "level_range": "45-55",
    "planned_vnum_range": "14401-14430",
    "reserved_room_block": "14401-14430",
    "theme": {
      "primary": "歷史城市",
      "secondary": "江港水軍 / 荊州東岸重鎮"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 14401,
        "target_area": "wild_jiangxia_river",
        "label": "江岸渡口"
      },
      {
        "direction": "east",
        "source_vnum": 14412,
        "target_area": "city_chaisang",
        "label": "柴桑水路"
      },
      {
        "direction": "south",
        "source_vnum": 14407,
        "target_area": "wild_yunmeng",
        "label": "雲夢水巷"
      },
      {
        "direction": "north",
        "source_vnum": 14410,
        "target_area": "jingxiang_road",
        "label": "北向官道"
      }
    ],
    "clusters": [
      { "id": "west-ferry-gate", "label": "西向渡口外門" },
      { "id": "harbor-front", "label": "港前外沿" },
      { "id": "main-street", "label": "主街中心" },
      { "id": "market-yard", "label": "市集補給區" },
      { "id": "naval-yamen", "label": "水軍官署區" }
    ]
  },
  "rooms": [
    {
      "vnum": 14401,
      "name": "渡口外門",
      "description": "粗木牌坊立在江夏西側渡口外，門下不斷有挑貨的人與下船的旅人交錯而過。和蘆葦濕灘那種風裡藏事的感覺不同，這裡連呼喝與腳步都顯得有秩序許多，像整座城先用規矩把江水擋在門外。",
      "sector_type": "SECT_CITY",
      "cluster": "west-ferry-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 14312, "external": true },
        { "direction": "east", "to": 14402 }
      ],
      "enquires": ["碼頭", "進城"]
    },
    {
      "vnum": 14402,
      "name": "驗貨棚前",
      "description": "幾座臨時木棚沿路一字排開，棚下堆著魚簍、麻袋與待驗的貨箱。差役偶爾掀開封布看上一眼，再把旅人與船工分流往不同方向，引得整段路都帶著一股忙碌卻不混亂的港口節奏。",
      "sector_type": "SECT_CITY",
      "cluster": "west-ferry-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "west", "to": 14401 },
        { "direction": "east", "to": 14403 }
      ],
      "enquires": ["驗貨", "主街"]
    },
    {
      "vnum": 14403,
      "name": "外港木棧",
      "description": "木棧沿著港前水線層層伸展，纜繩、木樁與曬網架把江夏的生氣全掛在岸邊。耳邊除了水聲，還有船工拉索時的吆喝與船鐘偶爾敲響的悶音，讓人一聽就知道這裡不是內陸城鎮。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-front",
      "coord": [2, 0, 0],
      "labels": ["harbor", "nautical"],
      "exits": [
        { "direction": "west", "to": 14402 },
        { "direction": "east", "to": 14404 },
        { "direction": "south", "to": 14405 }
      ],
      "keywords": [
        {
          "keyword": "纜樁",
          "description": "粗大的纜樁表面被水氣與繩索磨得發亮，樁腳附近還堆著剛換下來的舊麻索。"
        }
      ],
      "enquires": ["碼頭", "市集"]
    },
    {
      "vnum": 14404,
      "name": "港前街口",
      "description": "從外港木棧再往內一步，木板地很快讓位給踩得平整的石地與街面。臨街的幌子、路牌與公告牆一樣樣出現，像城市正在把水路的凌亂重新整理成可以理解的秩序。",
      "sector_type": "SECT_CITY",
      "cluster": "harbor-front",
      "coord": [3, 0, 0],
      "labels": ["street-mouth", "orientation"],
      "exits": [
        { "direction": "west", "to": 14403 },
        { "direction": "east", "to": 14408 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "路牌上把主街、市集、官署與東向碼頭幹道分得很清楚，讓外地旅人一進城就不至於找不到方向。"
        }
      ]
    },
    {
      "vnum": 14405,
      "name": "乾貨市集",
      "description": "這一帶滿是曬魚、鹽袋、乾糧與草藥混在一起的味道，攤棚彼此挨得很近，叫賣聲卻又像各守各的地盤。水路上的旅人到了這裡，多半都會先停下來補一輪真正適合上船與長途攜帶的東西。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [2, -1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 14403 },
        { "direction": "south", "to": 14406 }
      ],
      "enquires": ["市集", "乾糧"]
    },
    {
      "vnum": 14406,
      "name": "藥鋪前巷",
      "description": "小巷比主街安靜許多，只聽得見藥鋪裡搗藥的細碎聲響和外頭木桶偶爾碰撞的回音。門外掛著的藥草束、包紮布與驅濕香料，都明白告訴來往船工這裡懂得處理江風與濕氣帶來的麻煩。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [2, -2, 0],
      "labels": ["clinic", "alley"],
      "exits": [
        { "direction": "north", "to": 14405 },
        { "direction": "east", "to": 14407 }
      ],
      "enquires": ["藥鋪", "南邊"]
    },
    {
      "vnum": 14407,
      "name": "南向水巷",
      "description": "巷子往南越走越潮，牆邊堆著木桶、竹簍與幾片剛曬到一半的船帆，像再往前就會重新碰上濕地與水路。這裡仍在城裡，卻已把雲夢方向那種更散、更濕的氣味先帶了進來。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [3, -2, 0],
      "labels": ["south-edge", "future-link-south"],
      "exits": [
        { "direction": "west", "to": 14406 },
        { "direction": "east", "to": 14411 },
        { "direction": "south", "to": 14501, "external": true }
      ],
      "enquires": ["雲夢", "去路"]
    },
    {
      "vnum": 14408,
      "name": "主街十字",
      "description": "江夏主街在這裡與幾條側路交會，旅人、差役、船工與小販各自朝不同方向流動，卻又像都知道自己在這座城裡該占哪一條線。榜文牆前時不時有人駐足，顯得這裡既是城心，也是消息匯流之處。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [4, 0, 0],
      "labels": ["hub", "crossroads"],
      "exits": [
        { "direction": "west", "to": 14404 },
        { "direction": "east", "to": 14412 },
        { "direction": "south", "to": 14411 },
        { "direction": "up", "to": 14409 }
      ],
      "enquires": ["主街", "官府", "柴桑"]
    },
    {
      "vnum": 14409,
      "name": "堤上望臺",
      "description": "沿著石階走上堤頂後，江港、水線與主街都收進視野裡，連哪條巷子最忙、哪一段木棧剛靠船都看得一清二楚。站在這裡，會很明白江夏不是順著江邊長出來的散市，而是刻意看守船路的城。",
      "sector_type": "SECT_CITY",
      "cluster": "naval-yamen",
      "coord": [4, 1, 1],
      "labels": ["high-path", "overview"],
      "exits": [
        { "direction": "down", "to": 14408 },
        { "direction": "east", "to": 14410 }
      ],
      "enquires": ["望臺", "水軍"]
    },
    {
      "vnum": 14410,
      "name": "水軍哨棚",
      "description": "堤上哨棚用粗梁與厚布搭得結實，棚下掛著號角、船鉤與幾面尚未完全收起的旗號。守在這裡的人不必很多，光是這片視野和器具，就足夠說明誰在掌握江夏一帶的船路動靜。",
      "sector_type": "SECT_CITY",
      "cluster": "naval-yamen",
      "coord": [5, 1, 1],
      "labels": ["watch-post", "future-link-north"],
      "exits": [
        { "direction": "west", "to": 14409 }
      ],
      "keywords": [
        {
          "keyword": "船鐘",
          "description": "青銅船鐘掛在棚角，外表被風吹得發暗，敲起來卻能把聲音送得很遠。"
        }
      ],
      "enquires": ["北路", "水軍"]
    },
    {
      "vnum": 14411,
      "name": "港務官署",
      "description": "官署前庭不算華麗，卻收拾得格外整齊，牆邊立著船籍牌與幾張剛換上的通告。無論是貨、船還是人，只要與江上往來有關，多半都得在這座院子附近留下某種痕跡。",
      "sector_type": "SECT_CITY",
      "cluster": "naval-yamen",
      "coord": [4, -1, 0],
      "labels": ["yamen", "civic-order"],
      "exits": [
        { "direction": "west", "to": 14407 },
        { "direction": "north", "to": 14408 }
      ],
      "keywords": [
        {
          "keyword": "榜文",
          "description": "榜文上除了例行告示，還夾著幾條與近期船路、盤查和南向濕地異聞有關的短訊。"
        }
      ],
      "enquires": ["官府", "榜文"]
    },
    {
      "vnum": 14412,
      "name": "東向幹道",
      "description": "主街在這裡往東漸漸拉直，沿路店招與堤牆一起把視線推向更遠的江東水路。站在這段幹道上，會感覺江夏既是一座城，也是更大一串港口與船路的起點，而柴桑的名字已經開始在路牌與行人口中反覆出現。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [5, 0, 0],
      "labels": ["east-edge", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 14408 },
        { "direction": "east", "to": 14701, "external": true }
      ],
      "keywords": [
        {
          "keyword": "帆索",
          "description": "沿街架上晾著幾綹剛修過的帆索，麻線與桐油味把這條東向幹道也染上了濃濃的船路氣息。"
        }
      ],
      "enquires": ["柴桑", "東邊", "去路"]
    }
  ]
}
```
