# 江夏水道 (`wild_jiangxia_river`)

## Area Intent

`wild_jiangxia_river` 承接 `city_xiangyang` 東碼頭之外的第一段真正水路野外，讓玩家從主城的主街、榜文與碼頭秩序，正式走進一條由江風、蘆葦、棧橋與水寨殘樁主導節奏的江岸前帶。

第一版目標先固定：

- 一條由西向東沿江推進的主探索線
- 一條向南下沉到蘆葦濕灘的側線
- 一條 `up/down` 連到堤岸高處與渡口棧橋的非平面水路支線
- 以 `#Enquire` / `#Keyword` 暗示江路、水寨、碼頭與江夏方向

這一版刻意讓玩家感受到：

- 一離開襄陽東碼頭，秩序與視野就開始被江岸地形重新切開
- 水路野外的壓力不是怪物更滿，而是去路更濕、更滑、更難看清
- 三國水軍與江港節奏應先透過地景與殘跡出現，再慢慢推進到更大的水軍主城

## Theme Positioning

- Theme: `探險`
- Subtheme: `江夏水道 / 水軍河岸`
- LevelRange: `40-50`
- Parent region: `荊州江岸`
- World gap filled: 讓主世界 progression 從襄陽主城自然推進到江夏與柴桑方向的水路外野

## Player Flow

1. 玩家由襄陽東碼頭外路踏上離城木棧，先感受到城市聲音被水聲與風聲慢慢取代。
2. 沿江土道與繫船樁把主線從陸路節奏轉成水路節奏。
3. 蘆葦濕灘側線提供視線破碎、容易埋伏也容易迷向的支路壓力。
4. 水寨殘樁與舊哨棚讓人看出這一帶曾被當作軍事水路，而不只是普通河岸。
5. 東向渡口前帶只把江夏主線吸力立起來，先不直接做成完整水軍城。

## Cluster Notes

### `west-wharf-edge`

- 房間重點：離城木棧、江岸起點、回望城影
- 玩家感受：仍看得到城，但已不在城裡
- 對外角色：作為日後接 `city_xiangyang` 東碼頭邊界的水路入口

### `riverbank-trail`

- 房間重點：沿江土道、繫船樁、河汊木橋
- 玩家感受：道路開始被潮痕與水聲重新定義
- 對外角色：作為全區主探索線骨幹

### `reed-marsh`

- 房間重點：蘆葦濕灘、泥岸、下陷汊口
- 玩家感受：視線受阻、腳步不穩、天然伏擊感
- 對外角色：提供江岸野外與主線不同的風險分流

### `waterfort-remains`

- 房間重點：水寨殘樁、舊哨棚、斷旗木臺
- 玩家感受：水軍與河防曾在這裡留下秩序，如今只剩殘痕
- 對外角色：強化三國水路辨識度，而不只是 generic river trail

### `east-ferry-front`

- 房間重點：東向渡口、候船路牌、江夏前帶
- 玩家感受：再往前，水路節奏就會正式轉入更大的江港與水軍世界
- 對外角色：作為未來接 `city_jiangxia` 的前帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `west` from `14301`: planned link to `city_xiangyang`
- `east` from `14312`: planned link to `city_jiangxia`
- `south` from `14307`: planned link to `wild_yunmeng_marsh`
- `north` from `14310`: planned link to `fort_river_fort`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `碼頭 / 江路 / 水寨 / 去路 / 江夏`
- `#Keyword` 第一版會落在 `蘆葦 / 棧橋 / 繫船樁 / 漁網 / 水旗`
- `#Job` 第一版暫不新增；等真正要做渡口傳信、護船或水寨巡線 loop 再補 job 與 runtime flow

## Suggested Layout

```text
襄陽東碼頭方向
   |
[14301] 離城木棧 -- [14302] 江岸起道 -- [14303] 繫船樁旁 -- [14304] 河汊木橋 -- [14308] 東向渡口前帶 -- [14312] 候船路牌
                                             |                                     |
                                             |                                     +-- up -- [14309] 堤岸高徑 -- [14310] 舊哨棚
                                             |
                                             +-- south -- [14305] 蘆葦濕灘 -- [14306] 泥岸窪口 -- [14307] 下陷汊口
                                                                                                   |
                                                                                                east
                                                                                                   |
                                                                                                [14311] 水寨殘樁
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_jiangxia_river",
    "title": "江夏水道",
    "design_notes": "第一版 spec-first 草案。先固定襄陽東碼頭外的江岸主線、蘆葦濕灘側線與水寨殘樁支線，讓主線從城市自然轉入荊州水路野外。",
    "level_range": "40-50",
    "planned_vnum_range": "14301-14330",
    "reserved_room_block": "14301-14330",
    "theme": {
      "primary": "探險",
      "secondary": "江夏水道 / 水軍河岸"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 14301,
        "target_area": "city_xiangyang",
        "label": "襄陽東碼頭"
      },
      {
        "direction": "east",
        "source_vnum": 14312,
        "target_area": "city_jiangxia",
        "label": "江夏水路"
      },
      {
        "direction": "south",
        "source_vnum": 14307,
        "target_area": "wild_yunmeng_marsh",
        "label": "雲夢濕澤"
      },
      {
        "direction": "north",
        "source_vnum": 14310,
        "target_area": "fort_river_fort",
        "label": "上游哨渡"
      }
    ],
    "clusters": [
      { "id": "west-wharf-edge", "label": "西向碼頭外沿" },
      { "id": "riverbank-trail", "label": "沿江主道" },
      { "id": "reed-marsh", "label": "蘆葦濕灘" },
      { "id": "waterfort-remains", "label": "水寨殘跡線" },
      { "id": "east-ferry-front", "label": "東向渡口前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 14301,
      "name": "離城木棧",
      "description": "木棧從襄陽東碼頭外緣一路伸到江岸邊的濕地木樁上，腳下木板仍殘留城市搬運留下的磨痕。回頭還能看見城影與桅杆，往前卻只剩風裡越來越重的水氣與蘆葉聲。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-wharf-edge",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 14212, "external": true },
        { "direction": "east", "to": 14302 }
      ],
      "enquires": ["碼頭", "去路"]
    },
    {
      "vnum": 14302,
      "name": "江岸起道",
      "description": "木棧在這裡改接成沿江土道，左手是潮痕斑駁的水線，右手則是高低不一的草灘與蘆影。再往前走，襄陽城裡那種整齊的人聲已被水拍木樁的聲音慢慢吞掉。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-wharf-edge",
      "coord": [1, 0, 0],
      "labels": ["road", "transition"],
      "exits": [
        { "direction": "west", "to": 14301 },
        { "direction": "east", "to": 14303 }
      ],
      "enquires": ["江路", "東邊"]
    },
    {
      "vnum": 14303,
      "name": "繫船樁旁",
      "description": "幾根粗大的繫船樁歪斜插在泥地裡，樁身一圈圈纏著舊麻繩與潮水留下的深痕。這裡既像臨時停泊點，也像曾有人故意守著誰該靠岸、誰不該靠岸的位置。",
      "sector_type": "SECT_FIELD",
      "cluster": "riverbank-trail",
      "coord": [2, 0, 0],
      "labels": ["river-node", "nautical"],
      "exits": [
        { "direction": "west", "to": 14302 },
        { "direction": "east", "to": 14304 },
        { "direction": "south", "to": 14305 }
      ],
      "keywords": [
        {
          "keyword": "繫船樁",
          "description": "繫船樁上的舊麻繩被水浸得發黑，卻看得出不久前還有人在這裡重新打過結。"
        }
      ],
      "enquires": ["停船", "江路"]
    },
    {
      "vnum": 14304,
      "name": "河汊木橋",
      "description": "一座簡陋木橋橫跨淺汊，木板在潮濕中發出細小嘎響，像每一步都在提醒你這裡不是為了舒服通行而修。橋下水色不深，卻被蘆葦與陰影遮得難以看清。",
      "sector_type": "SECT_FIELD",
      "cluster": "riverbank-trail",
      "coord": [3, 0, 0],
      "labels": ["bridge", "risk"],
      "exits": [
        { "direction": "west", "to": 14303 },
        { "direction": "east", "to": 14308 }
      ],
      "keywords": [
        {
          "keyword": "棧橋",
          "description": "橋板邊緣磨得發滑，顯示船工與行腳人都把這裡當作最省力的一段短捷徑。"
        }
      ]
    },
    {
      "vnum": 14305,
      "name": "蘆葦濕灘",
      "description": "蘆葦在這片濕灘長得極密，風一過便整片伏倒又立起，像有看不見的人從裡面悄悄穿行。腳下泥地吸著鞋跟，讓人每一步都很難走得乾脆。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-marsh",
      "coord": [2, -1, 0],
      "labels": ["marsh", "concealment"],
      "exits": [
        { "direction": "north", "to": 14303 },
        { "direction": "south", "to": 14306 }
      ],
      "keywords": [
        {
          "keyword": "蘆葦",
          "description": "蘆葉邊緣割手，風吹時聲音又足夠蓋住細碎腳步，實在像天生為埋伏準備的地方。"
        }
      ],
      "enquires": ["濕地", "南邊"]
    },
    {
      "vnum": 14306,
      "name": "泥岸窪口",
      "description": "泥岸在這裡凹成一道半隱的窪口，積水混著漂來的木片與舊網線，散出一股濕冷腥味。若不是刻意往下探，主路上的人多半不會知道這裡還藏著另一條能貼著江邊走的偏線。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-marsh",
      "coord": [2, -2, -1],
      "labels": ["depression", "side-route"],
      "exits": [
        { "direction": "north", "to": 14305 },
        { "direction": "east", "to": 14307 }
      ],
      "enquires": ["泥岸", "偏路"]
    },
    {
      "vnum": 14307,
      "name": "下陷汊口",
      "description": "小汊口在這裡向更南方的濕地陷去，水面上浮著斷芒、殘木與幾截被潮水泡白的竹竿。這裡看起來不值得久留，卻也正因如此，最容易藏住不想讓主路看見的東西。",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-marsh",
      "coord": [3, -2, -1],
      "labels": ["south-edge", "hidden"],
      "exits": [
        { "direction": "west", "to": 14306 },
        { "direction": "east", "to": 14311 }
      ],
      "enquires": ["去路", "南邊"]
    },
    {
      "vnum": 14308,
      "name": "東向渡口前帶",
      "description": "江岸在這裡變得稍寬，地上多了拖船留下的深槽與一些臨時搭棚的痕跡。雖還沒真正到渡口，但人與貨都像在這裡先稍作整理，再決定是繼續向東還是等船南下。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-ferry-front",
      "coord": [4, 0, 0],
      "labels": ["frontier", "ferry-prep"],
      "exits": [
        { "direction": "west", "to": 14304 },
        { "direction": "east", "to": 14312 },
        { "direction": "south", "to": 14311 },
        { "direction": "up", "to": 14309 }
      ],
      "enquires": ["渡口", "江夏", "前面"]
    },
    {
      "vnum": 14309,
      "name": "堤岸高徑",
      "description": "順著堤岸往上走後，江風忽然變得更直更冷，連蘆葦擺動的方向都一目了然。從這裡看下去，主路、濕灘與水線交錯成數條可選又可伏的線，讓人明白這片江岸從來不是單純給旅人通過。",
      "sector_type": "SECT_HILLS",
      "cluster": "east-ferry-front",
      "coord": [4, 1, 1],
      "labels": ["high-path", "overview"],
      "exits": [
        { "direction": "down", "to": 14308 },
        { "direction": "east", "to": 14310 }
      ],
      "enquires": ["高處", "江岸"]
    },
    {
      "vnum": 14310,
      "name": "舊哨棚",
      "description": "一座臨江舊哨棚還勉強立著，棚頂被風掀去一角，木樑上卻仍殘留著掛旗與掛燈的鐵鉤。這地方顯然曾被用來盯著江面與來路，如今雖荒，視野卻依舊是整段江岸最好的一處。",
      "sector_type": "SECT_HILLS",
      "cluster": "waterfort-remains",
      "coord": [5, 1, 1],
      "labels": ["watch-post", "future-link-north"],
      "exits": [
        { "direction": "west", "to": 14309 }
      ],
      "keywords": [
        {
          "keyword": "水旗",
          "description": "旗杆底部還留著幾縷被風吹爛的藍黑布條，像是某支水軍早已退去，只把顏色丟在了江風裡。"
        }
      ]
    },
    {
      "vnum": 14311,
      "name": "水寨殘樁",
      "description": "數排木樁半沒在淺水與泥灘間，排列看似凌亂，仔細看卻像曾是某種水寨外沿的防線。如今木樁斷得參差，仍足以讓人想像當年船隻若硬闖進來，會先撞得多狼狽。",
      "sector_type": "SECT_FIELD",
      "cluster": "waterfort-remains",
      "coord": [4, -1, 0],
      "labels": ["ruin", "military-trace"],
      "exits": [
        { "direction": "west", "to": 14307 },
        { "direction": "north", "to": 14308 }
      ],
      "enquires": ["水寨", "舊哨"]
    },
    {
      "vnum": 14312,
      "name": "候船路牌",
      "description": "渡口旁立著一面被潮氣熏得發暗的路牌，上頭勉強還看得出江夏與更東幾處水路地名。走到這裡時，江岸野外的味道已經足夠濃，而更前方顯然正等著一個真正靠水吃飯、靠水守城的世界。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-ferry-front",
      "coord": [5, 0, 0],
      "labels": ["east-edge", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 14308 }
      ],
      "keywords": [
        {
          "keyword": "漁網",
          "description": "幾張半乾的漁網被捲在木柱邊，看似平常，卻和候船的人、待搬的貨一起把渡口氣味先鋪滿了周圍。"
        }
      ],
      "enquires": ["江夏", "候船", "去路"]
    }
  ]
}
```
