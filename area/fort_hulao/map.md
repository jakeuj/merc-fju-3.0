# 虎牢關 (`fort_hulao`)

## Area Intent

`fort_hulao` 承接 `dng_guandu_battlefield` 的軍旅主線，但把玩家從戰後殘局推進到一座仍在運作、仍有秩序與軍令壓力的戰略關隘。這裡的核心不是遍地焦土，而是厚門、甕城、營盤與望樓如何一起把交通變成可被控制的 choke point。

第一版目標先固定：

- 一條由西向東接近關門並穿過甕城的主推進線
- 一條從內關分出的軍營 / 軍需支線
- 一條 `up/down` 連到關樓與望樓的非平面守備線
- 以 `#Enquire` / `#Keyword` 暗示虎牢關、盤查、軍令與去路

這一版刻意讓玩家感受到：

- 這裡不是戰場餘波，而是仍有人在執行命令的軍事空間
- 關隘的壓力來自地形與制度同時存在，而不只是怪物更兇
- 一道關門、一段坡道、一座望樓就足以改變整段交通節奏

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `東都門戶 / 虎牢雄關`
- LevelRange: `28-36`
- Parent region: `中原西門戶`
- World gap filled: 讓主世界 progression 從官渡戰地推進到明確的軍事 choke point，不讓中段主線只剩抽象 world link

## Player Flow

1. 玩家從西向東接近關前道，先看見拒馬、盤查棚與逐步收窄的道路。
2. 外關門把節奏從「還能旅行」切成「必須被審視」的關卡感。
3. 甕城與內關道讓人意識到這座關不是單一大門，而是層層守備的軍事結構。
4. 軍營與軍需側線補足日常軍旅氛圍，讓關隘不像空殼場景。
5. 關樓與望樓透過 `up/down` 提供視野差，讓玩家從高處理解虎牢關控制道路的力量。

## Cluster Notes

### `west-approach`

- 房間重點：關前道、坡口、外拒馬
- 玩家感受：道路還存在，但自由移動感已被逐步壓縮
- 對外角色：作為未來接弘農與西向主線的關前入口

### `outer-gate`

- 房間重點：外寨、關門、盤查點
- 玩家感受：真正進入被守備制度包圍的空間
- 對外角色：作為全區最直接的 choke point 標誌

### `inner-bailey`

- 房間重點：甕城、軍令榜、內關通道
- 玩家感受：一道門之後還有一道秩序，壓力不是裝飾
- 對外角色：作為主線轉接與支線分流核心

### `barracks-line`

- 房間重點：軍營、軍需棚、換哨角
- 玩家感受：守軍不只是背景，而是有生活與輪值節奏的存在
- 對外角色：提供補給 / 情報 / 後續 runtime NPC 空間

### `watchtower-ridge`

- 房間重點：石階、關樓、望樓巡道
- 玩家感受：一旦站高，整條道路都變成被俯視與被控制的線
- 對外角色：以非平面高差完成關隘軍事辨識度

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `west` from `14101`: planned link to `city_hongnong`
- `east` from `14108`: planned link to `city_loyang`
- `south` from `14105`: planned link to `dng_guandu_battlefield`
- `north` from `14112`: planned link to `city_xiangyang`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `虎牢關 / 關門 / 軍令 / 去路 / 守兵`
- `#Keyword` 第一版會落在 `軍旗 / 柵門 / 拒馬 / 關樓 / 望樓`
- `#Job` 第一版暫不新增；等真正要做盤查、傳令或換哨 loop 再補 job 與 runtime flow

## Suggested Layout

```text
弘農方向
   |
[14101] 關前坡道 -- [14102] 外拒馬線 -- [14103] 盤查棚前 -- [14104] 厚門關口 -- [14105] 甕城石地 -- [14108] 內關東道
                                                                                     |                       |
                                                                                     |                       +-- east --> 洛陽方向
                                                                                     |
                                                                                     +-- south -- [14106] 軍需棚 -- [14107] 換哨營盤
                                                                                     |
                                                                                     up
                                                                                     |
                                                                                  [14109] 關樓石階 -- [14110] 關樓高台 -- [14111] 望樓巡道 -- [14112] 北望高角
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_hulao",
    "title": "虎牢關",
    "design_notes": "第一版 spec-first 草案。先固定關前坡道、外關門、甕城、軍營支線與關樓高差，讓虎牢關作為主世界軍事 choke point 的辨識度在 runtime implementation 前先穩住。",
    "level_range": "28-36",
    "planned_vnum_range": "14101-14120",
    "reserved_room_block": "14101-14120",
    "theme": {
      "primary": "軍旅",
      "secondary": "東都門戶 / 虎牢雄關"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 14101,
        "target_area": "city_hongnong",
        "label": "弘農關前道"
      },
      {
        "direction": "east",
        "source_vnum": 14108,
        "target_area": "city_loyang",
        "label": "洛陽門戶"
      },
      {
        "direction": "south",
        "source_vnum": 14105,
        "target_area": "dng_guandu_battlefield",
        "label": "戰場餘線"
      },
      {
        "direction": "north",
        "source_vnum": 14112,
        "target_area": "city_xiangyang",
        "label": "北向軍道"
      }
    ],
    "clusters": [
      { "id": "west-approach", "label": "西向關前道" },
      { "id": "outer-gate", "label": "外關門帶" },
      { "id": "inner-bailey", "label": "甕城內關帶" },
      { "id": "barracks-line", "label": "軍營軍需線" },
      { "id": "watchtower-ridge", "label": "關樓望樓線" }
    ]
  },
  "rooms": [
    {
      "vnum": 14101,
      "name": "關前坡道",
      "description": "西來官道在這裡抬升成一道長坡，坡頂隱約可見旗影與門樓輪廓。道路尚未完全被堵死，但拒馬與旗槍已讓人清楚知道，再往前就不是任人來去的普通路段。",
      "sector_type": "SECT_HILLS",
      "cluster": "west-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-west"],
      "exits": [
        { "direction": "east", "to": 14102 }
      ],
      "enquires": ["虎牢關", "去路"]
    },
    {
      "vnum": 14102,
      "name": "外拒馬線",
      "description": "厚重木樁交錯架成第一道外拒馬線，木上包著鐵條與舊繩，顯然不是臨時擺放的阻礙，而是長久維持的防線。兩側坡石被踩得發亮，顯見守兵在這裡反覆巡走。",
      "sector_type": "SECT_HILLS",
      "cluster": "west-approach",
      "coord": [1, 0, 0],
      "labels": ["obstacle", "military-line"],
      "exits": [
        { "direction": "west", "to": 14101 },
        { "direction": "east", "to": 14103 }
      ],
      "keywords": [
        {
          "keyword": "拒馬",
          "description": "木樁間距刻意留得很窄，足夠放慢車馬，也足夠讓守兵看清每個想靠近的人。"
        }
      ]
    },
    {
      "vnum": 14103,
      "name": "盤查棚前",
      "description": "一座厚帆盤查棚立在門前外側，棚下桌案、木牌與封泥箱擺得井井有條。這裡的空氣沒有戰場那種失控感，反而像每一口呼吸都被軍紀整齊切分。",
      "sector_type": "SECT_CITY",
      "cluster": "outer-gate",
      "coord": [2, 0, 0],
      "labels": ["checkpoint", "order"],
      "exits": [
        { "direction": "west", "to": 14102 },
        { "direction": "east", "to": 14104 }
      ],
      "enquires": ["守兵", "軍令", "通行"]
    },
    {
      "vnum": 14104,
      "name": "厚門關口",
      "description": "兩扇包鐵厚門嵌在石牆之間，門上的鉚釘與補鐵痕跡一層壓一層，像多年來無數次被修補、加固、再修補。站在門下時，任何人的腳步都顯得比平地時更小聲。",
      "sector_type": "SECT_CITY",
      "cluster": "outer-gate",
      "coord": [3, 0, 0],
      "labels": ["gate", "pressure"],
      "exits": [
        { "direction": "west", "to": 14103 },
        { "direction": "east", "to": 14105 }
      ],
      "keywords": [
        {
          "keyword": "柵門",
          "description": "厚門後方還能看見可落下的柵門槽痕，顯示這道關口設計時就沒打算給人輕易硬闖。"
        }
      ],
      "enquires": ["關門", "盤查"]
    },
    {
      "vnum": 14105,
      "name": "甕城石地",
      "description": "穿過關門後，眼前並不是開闊大路，而是一片被高牆包起來的甕城石地。牆上旗影交錯，地上磨痕縱橫，像在提醒每個走到這裡的人，真正的關卡其實才剛開始。",
      "sector_type": "SECT_CITY",
      "cluster": "inner-bailey",
      "coord": [4, 0, 0],
      "labels": ["bailey", "junction"],
      "exits": [
        { "direction": "west", "to": 14104 },
        { "direction": "east", "to": 14108 },
        { "direction": "down", "to": 14106 },
        { "direction": "up", "to": 14109 }
      ],
      "enquires": ["虎牢關", "去路", "軍令"]
    },
    {
      "vnum": 14106,
      "name": "軍需棚",
      "description": "甕城側下方搭著一列軍需棚，木箱、箭囊、麻繩和未分發的乾糧被歸得極整。比起戰地殘跡，這裡更讓人理解一座關隘要長久守得住，靠的不只是一扇門，而是一整套不斷補上的後勤。",
      "sector_type": "SECT_INSIDE",
      "cluster": "barracks-line",
      "coord": [4, 1, -1],
      "labels": ["supply", "service"],
      "exits": [
        { "direction": "up", "to": 14105 },
        { "direction": "east", "to": 14107 }
      ],
      "keywords": [
        {
          "keyword": "軍旗",
          "description": "幾面摺好的軍旗整齊靠在木架邊，尚未展開也能感覺出其中那股不容懈怠的壓力。"
        }
      ]
    },
    {
      "vnum": 14107,
      "name": "換哨營盤",
      "description": "木床、甲架與水桶排在營盤內側，牆角還掛著記錄值更次序的木牌。這裡沒有大聲喧嘩，只有一種每一輪換哨都會準時發生的沉著秩序，讓人知道守關從不是靠一時血勇。",
      "sector_type": "SECT_INSIDE",
      "cluster": "barracks-line",
      "coord": [5, 1, -1],
      "labels": ["barracks", "rotation"],
      "exits": [
        { "direction": "west", "to": 14106 }
      ],
      "enquires": ["守兵", "換哨"]
    },
    {
      "vnum": 14108,
      "name": "內關東道",
      "description": "穿出甕城後，東向道路重新展開，但高牆與樓影仍把視線牢牢夾住。這條路不再像自由通向遠方的官道，而像一條被虎牢關暫時借給行旅使用的通行線。",
      "sector_type": "SECT_CITY",
      "cluster": "inner-bailey",
      "coord": [5, 0, 0],
      "labels": ["east-link", "controlled-road"],
      "exits": [
        { "direction": "west", "to": 14105 }
      ],
      "enquires": ["洛陽", "東路"]
    },
    {
      "vnum": 14109,
      "name": "關樓石階",
      "description": "石階貼著內牆往上盤去，腳步聲在牆間來回撞響，連呼吸都像被放大。每往上一層，地面的人聲便更遠一分，而守備與視野則更近一分。",
      "sector_type": "SECT_CITY",
      "cluster": "watchtower-ridge",
      "coord": [4, 0, 1],
      "labels": ["stairs", "vertical"],
      "exits": [
        { "direction": "down", "to": 14105 },
        { "direction": "up", "to": 14110 }
      ]
    },
    {
      "vnum": 14110,
      "name": "關樓高台",
      "description": "高台橫跨厚門上方，能直接俯瞰外拒馬線與甕城石地。站在這裡時，人才真正理解虎牢關最可怕的地方不只是門厚，而是每一道門、每一段牆都被安排在能互相照看的位置。",
      "sector_type": "SECT_CITY",
      "cluster": "watchtower-ridge",
      "coord": [4, 0, 2],
      "labels": ["high-ground", "overview"],
      "exits": [
        { "direction": "down", "to": 14109 },
        { "direction": "east", "to": 14111 }
      ],
      "keywords": [
        {
          "keyword": "關樓",
          "description": "樓台邊緣磨得平亮，顯然常有值守者在此久站、巡望與傳遞手勢。"
        }
      ]
    },
    {
      "vnum": 14111,
      "name": "望樓巡道",
      "description": "巡道沿著牆脊往北延去，欄木與旗杆把風切成斷續低鳴。從這裡往西看是來路，往東看是去路，而向下望去，整座關隘像一只專門收緊人流的鐵手。",
      "sector_type": "SECT_CITY",
      "cluster": "watchtower-ridge",
      "coord": [5, 0, 2],
      "labels": ["watch-line", "ridge"],
      "exits": [
        { "direction": "west", "to": 14110 },
        { "direction": "north", "to": 14112 }
      ],
      "keywords": [
        {
          "keyword": "望樓",
          "description": "望樓屋角下掛著風鐸與小旗，風吹時聲音不大，卻足夠提醒所有人這裡始終有人看著。"
        }
      ]
    },
    {
      "vnum": 14112,
      "name": "北望高角",
      "description": "高角伸向更北側的軍道與山線，遠遠能看見道路被地勢切成一段又一段。這裡像整座虎牢關最安靜的一角，卻也最能讓人理解，為何一座關足以替整片中原決定來往與生死。",
      "sector_type": "SECT_CITY",
      "cluster": "watchtower-ridge",
      "coord": [5, 1, 2],
      "labels": ["north-lookout", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 14111 }
      ],
      "enquires": ["北邊", "軍道", "守關"]
    }
  ]
}
```
