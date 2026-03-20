# 濮陽林野 (`wild_puyang_forest`)

## Area Intent

`wild_puyang_forest` 承接 `city_chenliu` 北路之外的第一段真正野外，讓玩家從中原城市的補給與軍旅秩序，轉入林蔭遮蔽、舊哨荒廢、濕地失序與戰前耳語漸濃的探索帶。

第一版目標先固定：

- 一條由南向北穿越林野的主探索線
- 一條向東下探濕窪與獵徑的側線
- 一條 `up/down` 連到舊哨土塍的非平面軍旅支線
- 以 `#Enquire` / `#Keyword` 暗示樵夫消息、哨線遺跡與官渡前帶

這一版刻意讓玩家感受到：

- 離開 `city_chenliu` 後，秩序與情報開始變得不完整
- 林野不是單純的交通 connector，而是會吞掉視線與節奏的戰前緩衝帶
- 官渡還沒到，但戰場的氣味已經先透過殘旗、舊哨與荒路吹過來

## Theme Positioning

- Theme: `探險`
- Subtheme: `中原林野 / 官渡前哨外圍`
- LevelRange: `20-30`
- Parent region: `兗州河北`
- World gap filled: 讓主世界 progression 從 `city_chenliu` 自然推進到 `濮陽 / 官渡` 主線，不讓城市北路只停在抽象 world link

## Player Flow

1. 玩家由南向北離開陳留城外秩序，先經過仍看得見路牌的林口緩衝帶。
2. 林間主徑逐步變窄，倒木、彎路與樵棚傳聞讓人感受到真正進入中段野外。
3. 濕窪側線提供較隱蔽、較危險也較像埋伏點的支路節奏。
4. 舊哨土塍透過 `up/down` 形成軍旅遺跡感，讓玩家從地勢上先感受到戰前偵巡壓力。
5. 北向荒路不直接進戰場，而是把官渡風聲留在更前面的下一區。

## Cluster Notes

### `south-threshold`

- 房間重點：北路林口、最後清楚路牌、離城緩衝帶
- 玩家感受：還記得城市秩序，但保護感正在退去
- 對外角色：作為日後接 `city_chenliu` 北向邊界的野外入口

### `forest-road`

- 房間重點：林蔭主徑、倒木彎道、樵夫歇棚
- 玩家感受：視線受阻、消息破碎、真正進入林野
- 對外角色：作為全區主探索線與練功導流骨幹

### `wet-hollow`

- 房間重點：枯池濕窪、蘆草泥路、下陷獵徑
- 玩家感受：地勢濕黏、容易迷路、像天然埋伏點
- 對外角色：提供主線之外的地形變化與風險分流

### `old-scout-line`

- 房間重點：舊哨木梯、斥候土塍、殘旗監看點
- 玩家感受：戰前偵巡感、軍旅痕跡、上高處才看得見遠方壓力
- 對外角色：為官渡古戰場主題預熱，不直接提早變成 battlefield

### `north-warfront`

- 房間重點：北向荒路、前沿風聲、官渡前帶
- 玩家感受：空氣變乾、風聲更冷、往北就像一步步靠近大事發生處
- 對外角色：作為未來接 `dng_guandu_battlefield` 的野外前帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `south` from `13901`: planned link to `city_chenliu`
- `north` from `13912`: planned link to `dng_guandu_battlefield`
- `east` from `13906`: planned link to `city_puyang`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `去路 / 樵棚 / 枯池 / 舊哨 / 官渡`
- `#Keyword` 第一版會落在 `路牌 / 倒木 / 枯池 / 殘旗 / 哨樓`
- `#Job` 第一版暫不新增；等真正需要斥候、護路或傳信 loop 再補 job 與 runtime flow

## Suggested Layout

```text
陳留北路方向
   |
[13901] 北路林口 -- [13902] 林蔭官道 -- [13903] 倒木彎道 -- [13904] 樵夫歇棚 -- [13905] 荒藤岔徑 -- [13912] 北向荒路
                                                      |                    |
                                                      |                    +-- up -- [13910] 舊哨木梯 -- [13911] 斥候土塍
                                                      |
                                                      +-- east -- [13906] 枯池濕窪 -- [13907] 蘆草泥路 -- [13908] 下陷獵徑
                                                                                                          |
                                                                                                       north
                                                                                                          |
                                                                                                       [13909] 殘旗監看點
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_puyang_forest",
    "title": "濮陽林野",
    "design_notes": "第一版 spec-first 草案。先固定陳留北向野外承接帶、濕窪側線與舊哨土塍非平面軍旅支線，讓官渡前帶的壓力在進戰場前就開始累積。",
    "level_range": "20-30",
    "planned_vnum_range": "13901-13930",
    "reserved_room_block": "13901-13930",
    "theme": {
      "primary": "探險",
      "secondary": "中原林野 / 官渡前哨外圍"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 13901,
        "target_area": "city_chenliu",
        "label": "陳留北路"
      },
      {
        "direction": "north",
        "source_vnum": 13912,
        "target_area": "dng_guandu_battlefield",
        "label": "官渡前帶"
      },
      {
        "direction": "east",
        "source_vnum": 13906,
        "target_area": "city_puyang",
        "label": "濮陽林外路"
      }
    ],
    "clusters": [
      { "id": "south-threshold", "label": "南側離城帶" },
      { "id": "forest-road", "label": "林間主徑" },
      { "id": "wet-hollow", "label": "濕窪側線" },
      { "id": "old-scout-line", "label": "舊哨土塍線" },
      { "id": "north-warfront", "label": "北向前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 13901,
      "name": "北路林口",
      "description": "陳留北出的最後一段寬路在這裡被林影吞去一半，路旁木牌仍寫著往北行旅須防盜匪與亂兵。再往南還像在城外，向北卻已像把人慢慢送進一片不再由城門管束的地帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-threshold",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 13902 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "木牌上的字跡被風吹雨打得有些模糊，仍能看出濮陽與官渡方向，只是警語比地名更醒目。"
        }
      ],
      "enquires": ["陳留", "去路", "北路"]
    },
    {
      "vnum": 13902,
      "name": "林蔭官道",
      "description": "道路仍勉強保有官道的寬度，但兩側樹蔭已把天光切成碎片。偶爾可見車轍印入泥地，卻看不見車隊本身，只剩風從林上掠過，像在替更遠的消息遮掩聲音。",
      "sector_type": "SECT_FOREST",
      "cluster": "south-threshold",
      "coord": [1, 0, 0],
      "labels": ["road", "threshold"],
      "exits": [
        { "direction": "south", "to": 13901 },
        { "direction": "north", "to": 13903 }
      ],
      "enquires": ["林道", "路況"]
    },
    {
      "vnum": 13903,
      "name": "倒木彎道",
      "description": "巨木橫倒在彎道一側，迫使行人從較窄的泥邊繞過。枝枒與藤蔓把視線切得支離破碎，若真有人伏在林後等路過的人，這裡大概會是最舒服的位置。",
      "sector_type": "SECT_FOREST",
      "cluster": "forest-road",
      "coord": [2, 0, 0],
      "labels": ["bend", "ambush-hint"],
      "exits": [
        { "direction": "south", "to": 13902 },
        { "direction": "north", "to": 13904 }
      ],
      "keywords": [
        {
          "keyword": "倒木",
          "description": "倒木表面仍殘留刀斧削過的痕跡，像是有人曾想清出道路，卻又半途停手。"
        }
      ]
    },
    {
      "vnum": 13904,
      "name": "樵夫歇棚",
      "description": "簡陋木棚靠著老樹搭起，棚下留著熄滅的柴火與兩三束尚未綁緊的柴薪。這裡仍有人類活動痕跡，但久留的人說話都壓低聲音，像怕把林裡更遠的東西喚醒。",
      "sector_type": "SECT_FOREST",
      "cluster": "forest-road",
      "coord": [3, 0, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "south", "to": 13903 },
        { "direction": "north", "to": 13905 },
        { "direction": "east", "to": 13906 }
      ],
      "enquires": ["樵棚", "濮陽", "亂兵", "官渡"]
    },
    {
      "vnum": 13905,
      "name": "荒藤岔徑",
      "description": "往北的主徑仍可勉強辨認，另一條被荒藤纏住的舊徑則沿著高土塍往上。地上散著零碎馬蹄印與斷裂草繩，像有人不久前才匆忙從這裡分流。",
      "sector_type": "SECT_FOREST",
      "cluster": "forest-road",
      "coord": [4, 0, 0],
      "labels": ["junction", "military-hint"],
      "exits": [
        { "direction": "south", "to": 13904 },
        { "direction": "north", "to": 13912 },
        { "direction": "up", "to": 13910 }
      ],
      "enquires": ["岔路", "北邊", "高處"]
    },
    {
      "vnum": 13906,
      "name": "枯池濕窪",
      "description": "原本像是池塘的低地只剩半乾泥水與大片發黑蘆草，地面踩下去會慢半拍才把水滲上來。若從林道暫時失去方向，這片濕窪足以讓人越走越覺得四周都長得一樣。",
      "sector_type": "SECT_SWAMP",
      "cluster": "wet-hollow",
      "coord": [4, -1, 0],
      "labels": ["wetland", "world-link-east"],
      "exits": [
        { "direction": "west", "to": 13904 },
        { "direction": "east", "to": 13907 }
      ],
      "keywords": [
        {
          "keyword": "枯池",
          "description": "池底龜裂與積水並存，說不清是季節使然，還是曾有人刻意引水又棄置。"
        }
      ],
      "enquires": ["枯池", "濕地", "東路"]
    },
    {
      "vnum": 13907,
      "name": "蘆草泥路",
      "description": "蘆草高過肩頭，泥路被踩出一道道深淺不一的凹痕。風吹過時，草浪遮住人影，讓人很難判斷前方究竟只是空路，還是有人正沿著另一側悄悄跟著你走。",
      "sector_type": "SECT_SWAMP",
      "cluster": "wet-hollow",
      "coord": [5, -1, 0],
      "labels": ["concealment", "side-route"],
      "exits": [
        { "direction": "west", "to": 13906 },
        { "direction": "east", "to": 13908 }
      ]
    },
    {
      "vnum": 13908,
      "name": "下陷獵徑",
      "description": "這條小徑像被兩側泥土慢慢擠壓成溝，走在其中時視線會比地表低上一截。路邊可見折斷木箭與被踩進泥裡的皮繩，讓人分不清這裡究竟是獵人常走的近路，還是某種更不安穩的通道。",
      "sector_type": "SECT_SWAMP",
      "cluster": "wet-hollow",
      "coord": [6, -1, -1],
      "labels": ["sunken", "risk"],
      "exits": [
        { "direction": "west", "to": 13907 },
        { "direction": "north", "to": 13909 }
      ]
    },
    {
      "vnum": 13909,
      "name": "殘旗監看點",
      "description": "幾根折斷木樁斜插在高一點的硬地上，其中一根仍掛著破爛布旗。站在這裡可以勉強越過蘆草頂端遠望北邊荒路，風一吹，殘布拍打聲像極了遠處行軍前某種不願明說的預兆。",
      "sector_type": "SECT_FIELD",
      "cluster": "old-scout-line",
      "coord": [6, 0, 0],
      "labels": ["lookout", "war-hint"],
      "exits": [
        { "direction": "south", "to": 13908 },
        { "direction": "west", "to": 13911 }
      ],
      "keywords": [
        {
          "keyword": "殘旗",
          "description": "旗布顏色幾乎褪盡，只剩邊角仍能看出它曾屬於某支行伍。"
        }
      ],
      "enquires": ["官渡", "殘旗", "北邊"]
    },
    {
      "vnum": 13910,
      "name": "舊哨木梯",
      "description": "沿土塍側邊架起的舊木梯早已發黑發脆，踩上去時會發出不太讓人安心的聲音。梯邊留著碎裂的瞭望欄木，顯示這裡曾是用來觀望林外動靜的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "old-scout-line",
      "coord": [4, 1, 1],
      "labels": ["up-route", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 13905 },
        { "direction": "east", "to": 13911 }
      ],
      "keywords": [
        {
          "keyword": "哨樓",
          "description": "哨樓本體早已不存，只剩木梯、斷樁與被風磨裂的地基。"
        }
      ]
    },
    {
      "vnum": 13911,
      "name": "斥候土塍",
      "description": "高土塍把林線與北向荒路切開一道微妙高差，站在這裡可以看見林子如何慢慢往北退去。若說前面的濕地像自然形成的阻礙，這裡就更像人為留下的戰前視線控制點。",
      "sector_type": "SECT_HILLS",
      "cluster": "old-scout-line",
      "coord": [5, 1, 1],
      "labels": ["high-ground", "scout-line"],
      "exits": [
        { "direction": "west", "to": 13910 },
        { "direction": "east", "to": 13909 }
      ],
      "enquires": ["舊哨", "斥候", "前線"]
    },
    {
      "vnum": 13912,
      "name": "北向荒路",
      "description": "林木到這裡開始稀疏，泥地上混進更多舊車轍與凌亂馬蹄印。北風從空曠處直接灌來，帶著比林內更乾、更硬的塵土味，像在提醒你再往前一步，就不只是探路，而是要開始碰見真正的戰前世界。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-warfront",
      "coord": [5, 0, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 13905 }
      ],
      "enquires": ["官渡", "前線", "去路"]
    }
  ]
}
```
