# 陳留 (`city_chenliu`)

## Area Intent

`city_chenliu` 是主世界 queue reset 後的第一個正式主線城市 hub，用來把玩家節奏從洛陽周邊的早期區與晚期 spirit-core plateau 明確拉回三國地表世界。

第一版目標先固定：

- 一條可讀的城市主幹道骨架，讓玩家明確分得出 `西門 / 主街 / 北街 / 東街 / 南驛`
- 一條高密度服務支線，承接 `食堂 / 錢莊 / 武器店 / 防具店 / 打鐵舖 / 馬廄 / 鏢局`
- 一條軍旅與師父支線，承接 `太守衙門 / 義勇軍 / 虎豹騎 / 拳館`
- 一組 `enter/out` 的驛站室內轉場，讓城市不只是一張平面街圖

這一版刻意讓玩家感受到：

- 這裡是中原交通樞紐，不是另一個抽象地底井底
- 城內 NPC、店鋪、軍旅與江湖人物彼此交錯，形成明確的補給與學技 loop
- 每個方向都在提示後續主線世界的開展，而不是只剩下一條 `down`

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `中原樞紐城 / 軍旅與江湖中繼`
- LevelRange: `15-26`
- Parent region: `兗州河北`
- World gap filled: 讓主世界 progression 從 `洛陽` 推進到 `陳留 -> 濮陽 / 官渡 -> 虎牢 -> 襄陽 / 江夏`

## Player Flow

1. 玩家由西門入城，先感受到盤查、告示與回洛陽的退路。
2. 主街十字口提供整座城的導流中樞，讓玩家能快速理解北街、東街、南驛與服務巷的分工。
3. 服務區把補給、裝備、馬匹、金流與押運消息集中起來，成為 midgame 逗留點。
4. 軍旅區把太守衙門、義勇軍、虎豹騎與拳館整合起來，讓城市不是純商店集合，而是帶有曹魏地方武備壓力。
5. 南驛與驛站大堂透過 `enter/out` 顯示旅行轉場感，並為日後接許昌 / 徐州線預留具體出口語意。

## Cluster Notes

### `west-gate`

- 房間重點：西城門、門洞、盤查告示
- 玩家感受：秩序、盤查、回洛陽仍很近
- 對外角色：作為日後接 `road_chenliu_loyang` 的城市邊界

### `main-street`

- 房間重點：主街、西市十字、北街牌樓、東街路標
- 玩家感受：人流繁密、方向清楚、各種消息在此匯流
- 對外角色：作為全城的流量節點，分流到濮陽、徐州、南驛與服務區

### `service-quarter`

- 房間重點：春風食肆、兵甲作坊、錢莊馬市、鏢局旗埕
- 玩家感受：補給、金流、裝備與商旅消息密度高
- 對外角色：承接 midgame 玩家常用的補給與江湖 teacher/service loop

### `militia-quarter`

- 房間重點：太守衙門、義勇演武場、虎豹騎營前、震南山拳館
- 玩家感受：軍旗壓力、試武氛圍、地方武備森嚴
- 對外角色：承接徵募、試武、武學學習與地方勢力導流

### `south-station`

- 房間重點：南驛街、驛站前院、驛站大堂
- 玩家感受：車馬行李、旅人過站、離城與轉線感
- 對外角色：作為未來接 `district_chenliu_station` 與南向路網的具體過渡帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `west` from `13801`: planned link to `road_chenliu_loyang`
- `north` from `13809`: planned link to `wild_puyang_forest`
- `east` from `13810`: planned link to `city_xuzhou`
- `south` from `13816`: planned link to `district_chenliu_station`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `城門 / 太守衙門 / 食堂 / 拳館 / 驛站 / 去路`
- `#Keyword` 第一版會落在 `告示 / 招牌 / 城門 / 軍旗 / 路標`
- `#Job` 第一版暫不新增；等後續真的要做跑腿、押鏢或驛站差事，再補對應 job 與 runtime flow

## Suggested Layout

```text
洛陽 / 洛陳驛路方向
   |
[13801] 西城門外牌樓 -- [13802] 西門甬道 -- [13803] 陳留主街西段 -- [13804] 西市十字 -- [13809] 北街牌樓
                                                        |                    |
                                                        |                    +-- north (future: 濮陽 / 官渡)
                                                        |
                                                        +-- [13805] 春風食肆巷口 -- [13806] 兵甲作坊街 -- [13807] 錢莊馬市街 -- [13808] 鏢局旗埕
                                                        |
                                                        +-- [13810] 東街路標 (future: 徐州)
                                                        |
                                                        +-- [13811] 太守衙門前 -- [13812] 義勇演武場 -- [13813] 虎豹騎營前
                                                                                                     |
                                                                                                  [13814] 震南山拳館外
                                                        |
                                                        +-- [13815] 南驛街口 -- [13816] 陳留驛站前院 -- enter -- [13817] 驛站大堂
                                                                                  |
                                                                               south (future: 陳留驛站 / 許昌線)
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_chenliu",
    "title": "陳留",
    "design_notes": "第一版 spec-first 草案。先固定中原城市 hub 的主街、服務區、軍旅區與南驛轉場，讓城市玩法和晚期 spirit-core 深井明確分流。",
    "level_range": "15-26",
    "planned_vnum_range": "13801-13830",
    "reserved_room_block": "13801-13830",
    "theme": {
      "primary": "歷史城市",
      "secondary": "中原樞紐城 / 軍旅與江湖中繼"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 13801,
        "target_area": "road_chenliu_loyang",
        "label": "洛陳驛路"
      },
      {
        "direction": "north",
        "source_vnum": 13809,
        "target_area": "wild_puyang_forest",
        "label": "濮陽林路"
      },
      {
        "direction": "east",
        "source_vnum": 13810,
        "target_area": "city_xuzhou",
        "label": "徐州大道"
      },
      {
        "direction": "south",
        "source_vnum": 13816,
        "target_area": "district_chenliu_station",
        "label": "陳留驛站"
      }
    ],
    "clusters": [
      {
        "id": "west-gate",
        "label": "西門緩衝帶"
      },
      {
        "id": "main-street",
        "label": "主街與十字口"
      },
      {
        "id": "service-quarter",
        "label": "補給與商旅服務區"
      },
      {
        "id": "militia-quarter",
        "label": "官署與軍旅區"
      },
      {
        "id": "south-station",
        "label": "南驛轉接帶"
      }
    ]
  },
  "rooms": [
    {
      "vnum": 13801,
      "name": "西城門外牌樓",
      "description": "青灰城牆在身後筆直抬起，西城門外的牌樓下聚著等待盤查的旅人與車隊。再往西便是洛陳驛路，回首仍可看見一路趕來的塵煙，提醒你陳留不是盡頭，而是更大中原網路的中繼點。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, 0, 0],
      "labels": ["west-edge", "world-link-west", "entry"],
      "exits": [
        { "direction": "east", "to": 13802 }
      ],
      "keywords": [
        {
          "keyword": "城門",
          "description": "城門上方懸著「陳留」大字門匾，門洞兩側的鐵甲守卒正逐一核對旅人的來路。"
        }
      ],
      "enquires": ["洛陽", "城門", "回路"]
    },
    {
      "vnum": 13802,
      "name": "西門甬道",
      "description": "甬道內牆釘著官府新貼的告示與盤查條例，行人腳步進出不絕。門洞外是長路塵土，門洞內則是主街喧聲，陳留的秩序與煙火氣在這裡自然交界。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "west", "to": 13801 },
        { "direction": "east", "to": 13803 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "告示上除了城門盤查與夜禁時辰，還提到北路近來兵馬調動頻繁，行旅最好先問清楚去向。"
        }
      ],
      "enquires": ["告示", "盤查", "北路"]
    },
    {
      "vnum": 13803,
      "name": "陳留主街西段",
      "description": "寬闊石板街往東一路伸展，兩旁掛著新舊交錯的店招與布幌。行商、軍士、鏢客與江湖人擦肩而過，誰都像是路過，卻也都在這裡交換下一程消息。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [2, 0, 0],
      "labels": ["main-artery", "traffic"],
      "exits": [
        { "direction": "west", "to": 13802 },
        { "direction": "east", "to": 13804 }
      ]
    },
    {
      "vnum": 13804,
      "name": "西市十字",
      "description": "四條街路在此交會，吆喝聲、車輪聲與報價聲混成一片。北街通往軍旅與牌樓，南邊則漸漸轉入驛站人潮，若想在陳留久留或趕路，幾乎都得先經過這裡。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [3, 0, 0],
      "labels": ["junction", "city-core"],
      "exits": [
        { "direction": "west", "to": 13803 },
        { "direction": "north", "to": 13809 },
        { "direction": "east", "to": 13810 },
        { "direction": "south", "to": 13815 },
        { "direction": "enter", "to": 13805 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "十字口四面垂著不同店家的招牌，有酒旗、有布幌，也有畫著刀劍與鞍具的木牌。"
        }
      ],
      "enquires": ["去路", "北街", "南驛", "東街"]
    },
    {
      "vnum": 13805,
      "name": "春風食肆巷口",
      "description": "一轉進巷子便聞到熱湯與油香，春風閣的伙計正忙著招呼來往客商。巷口桌凳擺得外溢，總有人一面填飽肚子，一面聽別人講哪裡的路最近不太平。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [3, -1, 0],
      "labels": ["service", "food"],
      "exits": [
        { "direction": "out", "to": 13804 },
        { "direction": "east", "to": 13806 }
      ],
      "enquires": ["食堂", "春風閣", "熱湯"]
    },
    {
      "vnum": 13806,
      "name": "兵甲作坊街",
      "description": "鐵鎚敲擊與磨刀聲在這條街上此起彼落，武器店、防具店與打鐵舖都把貨架擺到門前。幾名想拜師學劍的年輕人不時朝內張望，像是在等那位傳聞中的十文字劍現身。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [4, -1, 0],
      "labels": ["service", "equipment", "teacher"],
      "exits": [
        { "direction": "west", "to": 13805 },
        { "direction": "east", "to": 13807 }
      ],
      "keywords": [
        {
          "keyword": "鐵砧",
          "description": "一旁鐵砧火花四濺，鐵匠剛替人收尾一柄重劍，還沒冷卻的鋒面映出紅光。"
        }
      ],
      "enquires": ["武器店", "防具店", "打鐵舖", "十文字劍", "華山劍法"]
    },
    {
      "vnum": 13807,
      "name": "錢莊馬市街",
      "description": "街北是錢莊厚重門面，街南則連著馬廄與幾家替行腳商整備韁具的小店。銀票、鞍具與遠路旅程在這裡同時被談價，空氣裡滿是銅錢、草料與牲口熱氣混雜的味道。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [5, -1, 0],
      "labels": ["service", "bank", "stable"],
      "exits": [
        { "direction": "west", "to": 13806 },
        { "direction": "east", "to": 13808 }
      ],
      "enquires": ["錢莊", "馬廄", "銀票", "車馬"]
    },
    {
      "vnum": 13808,
      "name": "鏢局旗埕",
      "description": "一面寫著鏢字的旗幟迎風拍打，埕上停著兩輛待發的貨車。鏢師、浪人與外地客商在這裡最容易搭上話頭，誰要往北、往東或往南，往往比官道告示還要先傳開。",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [6, -1, 0],
      "labels": ["escort", "rumor", "service"],
      "exits": [
        { "direction": "west", "to": 13807 }
      ],
      "keywords": [
        {
          "keyword": "鏢旗",
          "description": "鏢旗邊角磨得起毛，卻仍被洗得乾乾淨淨，顯示這家鏢局近來走鏢相當頻繁。"
        }
      ],
      "enquires": ["鏢局", "浪人", "風雲袖步", "押運"]
    },
    {
      "vnum": 13809,
      "name": "北街牌樓",
      "description": "北街牌樓下往來的多半不是尋常商旅，而是帶甲的兵卒、送文書的差人與準備北上的壯士。牌樓外的路勢逐漸開闊，像是把人慢慢送向濮陽與官渡的戰前地帶。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [3, 1, 0],
      "labels": ["north-edge", "world-link-north", "gate"],
      "exits": [
        { "direction": "south", "to": 13804 },
        { "direction": "east", "to": 13811 },
        { "direction": "north", "to": 13901, "external": true }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "路牌上刻著濮陽、官渡等方向，旁邊還多了幾筆兵站改道的臨時註記。"
        }
      ],
      "enquires": ["濮陽", "官渡", "北路"]
    },
    {
      "vnum": 13810,
      "name": "東街路標",
      "description": "東街較少豪奢喧鬧，多的是外地行商與抄寫地名的書吏。路標一面指向徐州，一面又寫著南轉驛站，像是在提醒旅人：陳留真正的價值，在於你能從這裡繼續走向更多地方。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [4, 0, 0],
      "labels": ["east-edge", "world-link-east", "route-node"],
      "exits": [
        { "direction": "west", "to": 13804 },
        { "direction": "east", "to": 16801, "external": true }
      ],
      "enquires": ["徐州", "東路", "去路"]
    },
    {
      "vnum": 13811,
      "name": "太守衙門前",
      "description": "衙門石階打掃得一塵不染，階前長戟與木牌把閒人自然而然隔在外圍。來此的人有的是遞狀紙，有的是打探軍報，也有人只是想看看北地兵馬調動是否又有新變化。",
      "sector_type": "SECT_CITY",
      "cluster": "militia-quarter",
      "coord": [4, 1, 0],
      "labels": ["authority", "service", "military-pressure"],
      "exits": [
        { "direction": "west", "to": 13809 },
        { "direction": "east", "to": 13812 }
      ],
      "keywords": [
        {
          "keyword": "官牌",
          "description": "門旁官牌寫著出入規矩與近日巡防安排，措辭平實，卻讓人看得出現在城中風聲不算鬆。"
        }
      ],
      "enquires": ["太守", "官府", "軍報"]
    },
    {
      "vnum": 13812,
      "name": "義勇演武場",
      "description": "場中木樁與兵器架排列整齊，偶爾有義勇軍在此對打試手。圍觀者之中既有想投軍的年輕人，也有盤算自己是否該先學些保命身法的旅人。",
      "sector_type": "SECT_CITY",
      "cluster": "militia-quarter",
      "coord": [5, 1, 0],
      "labels": ["training", "militia"],
      "exits": [
        { "direction": "west", "to": 13811 },
        { "direction": "east", "to": 13813 },
        { "direction": "south", "to": 13814 }
      ],
      "enquires": ["義勇軍", "測驗場", "試武"]
    },
    {
      "vnum": 13813,
      "name": "虎豹騎營前",
      "description": "營門前豎著黑底軍旗，值勤兵卒個個神情肅然。若只是路過商旅，多半會加快腳步；若是有意從軍的人，則難免在門外多看幾眼，衡量自己是否夠資格踏進這道門。",
      "sector_type": "SECT_CITY",
      "cluster": "militia-quarter",
      "coord": [6, 1, 0],
      "labels": ["recruitment", "military", "service"],
      "exits": [
        { "direction": "west", "to": 13812 }
      ],
      "keywords": [
        {
          "keyword": "軍旗",
          "description": "黑底軍旗在風裡繃得筆直，旗面邊緣繡著虎紋，像是連觀望的人都要先被它試上一回膽氣。"
        }
      ],
      "enquires": ["虎豹騎", "招募處", "從軍"]
    },
    {
      "vnum": 13814,
      "name": "震南山拳館外",
      "description": "拳館門前石磚被來往腳步磨得發亮，門內隱約傳出喝聲與落地聲。有人來此學拳腳，有人來問逃命身法，也有人只是想先探探那位震南山到底肯不肯見客。",
      "sector_type": "SECT_CITY",
      "cluster": "militia-quarter",
      "coord": [5, 0, 0],
      "labels": ["teacher", "jianghu", "training"],
      "exits": [
        { "direction": "north", "to": 13812 }
      ],
      "enquires": ["拳館", "震南山", "翦雲步", "金蟬脫殼", "flee"]
    },
    {
      "vnum": 13815,
      "name": "南驛街口",
      "description": "街面比主街更雜亂些，載貨車隊與牽馬的驛卒常在此交錯。再往南走，城中商旅喧聲開始被車輪、馬嘶與催程聲取代，像是整座陳留正在這裡把人送往下一段路。",
      "sector_type": "SECT_CITY",
      "cluster": "south-station",
      "coord": [3, -1, 0],
      "labels": ["travel", "junction", "southbound"],
      "exits": [
        { "direction": "north", "to": 13804 },
        { "direction": "south", "to": 13816 }
      ],
      "enquires": ["驛站", "許昌", "南路"]
    },
    {
      "vnum": 13816,
      "name": "陳留驛站前院",
      "description": "前院停著幾輛剛卸貨的車，馬槽邊堆滿草料與繩索。趕路的人在此問價、問時辰、問下一站，對真正長途奔波的人來說，這裡比太守衙門更像陳留的心口。",
      "sector_type": "SECT_CITY",
      "cluster": "south-station",
      "coord": [3, -2, 0],
      "labels": ["south-edge", "world-link-south", "travel-service"],
      "exits": [
        { "direction": "north", "to": 13815 },
        { "direction": "enter", "to": 13817 }
      ],
      "keywords": [
        {
          "keyword": "站牌",
          "description": "驛站站牌刻著往許昌、徐州與附近縣鄉的車馬時辰，邊角還壓著幾張鏢局與貨行的加貼紙條。"
        }
      ],
      "enquires": ["驛站", "許昌", "車馬", "去路"]
    },
    {
      "vnum": 13817,
      "name": "驛站大堂",
      "description": "堂內長案擺滿竹簡與行程簿，牆上掛著各地路引與時刻板。進門的人不是在討價還價，就是壓低聲音交換沿路情報；一座城市是否活著，往往看這樣的地方最清楚。",
      "sector_type": "SECT_INSIDE",
      "cluster": "south-station",
      "coord": [3, -2, 1],
      "labels": ["inside", "travel", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 13816 }
      ],
      "enquires": ["車次", "路引", "下一站"]
    }
  ]
}
```
