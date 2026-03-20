# 長沙 (`city_changsha`)

## Area Intent

`city_changsha` 承接 `city_chaisang` 南向主線，讓玩家從江岸轉場與赤壁戰痕的壓力，重新回到一座更偏內陸、更有荊南主城秩序感的城市 hub。

第一版目標先固定：

- 一條由北向南穿過城門、主街與南口的主探索線
- 一條往市集與補給區延伸的側線
- 一條 `up/down` 連到城樓或望臺的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示長沙、柴桑、驛站、官府與更南去路

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `荊南主城 / 南境轉運 hub`
- LevelRange: `72-82`
- Parent region: `荊南北口`
- World gap filled: 讓主世界從柴桑與赤壁支線重新收束到荊南主城，為零陵、武陵與更南主線建立穩定母城

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_changsha",
    "title": "長沙",
    "design_notes": "第一版 spec-first 草案。先固定北門、主街、市集補給、官署與南向出城骨架，讓荊南主線在長沙重新收束成內陸城市 hub。",
    "level_range": "72-82",
    "planned_vnum_range": "14901-14930",
    "reserved_room_block": "14901-14930",
    "theme": {
      "primary": "歷史城市",
      "secondary": "荊南主城 / 南境轉運 hub"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 14901,
        "target_area": "city_chaisang",
        "label": "柴桑北路"
      },
      {
        "direction": "south",
        "source_vnum": 14910,
        "target_area": "city_lingling",
        "label": "零陵官道"
      },
      {
        "direction": "west",
        "source_vnum": 14912,
        "target_area": "wild_wuling",
        "label": "武陵山路"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北向城門" },
      { "id": "main-street", "label": "主街中心" },
      { "id": "market-quarter", "label": "市集補給區" },
      { "id": "yamen-quarter", "label": "官署與驛站區" },
      { "id": "south-road", "label": "南向出城區" }
    ]
  },
  "rooms": [
    {
      "vnum": 14901,
      "name": "北向城門",
      "description": "北路官道一路把旅人送到長沙城門前，門下石面雖被南來北往的車馬磨得發亮，城門內外仍維持著一座荊南主城該有的穩定秩序。和柴桑相比，這裡少了江風，多了內陸大城把四方來路收束起來的厚重感。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "north", "to": 14710, "external": true },
        { "direction": "south", "to": 14903 },
        { "direction": "east", "to": 14902 },
        { "direction": "west", "to": 14905 }
      ],
      "enquires": ["柴桑", "進城"]
    },
    {
      "vnum": 14902,
      "name": "北驛牌亭",
      "description": "牌亭邊掛著幾面指往柴桑、零陵與武陵的舊木牌，字跡被風吹雨打得微白，卻仍看得出這裡長年是南線轉運的重要節點。即使只是稍停，也能感受到消息與人流都會先在這裡打個照面。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["wayfinding", "post"],
      "exits": [
        { "direction": "west", "to": 14901 },
        { "direction": "south", "to": 14904 }
      ],
      "enquires": ["驛站", "去路"]
    },
    {
      "vnum": 14903,
      "name": "長沙主街",
      "description": "主街把北門、市集與官署穩穩串成一條線，街旁店招、車聲與行人談話都帶著主城才有的規模感。這裡不像碼頭邊那樣急促，而是一種能把南境消息慢慢匯進來、再重新分出去的厚實節奏。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, -1, 0],
      "labels": ["main-street", "hub"],
      "exits": [
        { "direction": "north", "to": 14901 },
        { "direction": "east", "to": 14904 },
        { "direction": "south", "to": 14906 }
      ],
      "enquires": ["長沙", "市集"]
    },
    {
      "vnum": 14904,
      "name": "主街十字",
      "description": "幾條街道在此交會，榜示、店招與差役巡行讓長沙作為南境主城的節奏一眼可辨。站在十字口時，你會很自然地明白哪裡能補給、哪裡能問路、哪裡則會把你送向更遠的南境。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, -1, 0],
      "labels": ["crossroads", "civic"],
      "exits": [
        { "direction": "north", "to": 14902 },
        { "direction": "west", "to": 14903 },
        { "direction": "east", "to": 14908 },
        { "direction": "south", "to": 14907 },
        { "direction": "up", "to": 14911 }
      ],
      "enquires": ["官府", "南邊", "武陵"]
    },
    {
      "vnum": 14905,
      "name": "北城偏巷",
      "description": "偏巷比主街安靜，卻仍能聽見遠處市聲與驛馬踏石的聲音。這裡像專供熟門熟路的人穿行，沒有太多排場，卻讓整座城顯得更有深度與日常呼吸。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [-1, 0, 0],
      "labels": ["side-lane", "quiet"],
      "exits": [
        { "direction": "east", "to": 14901 }
      ],
      "enquires": ["巷子", "城門"]
    },
    {
      "vnum": 14906,
      "name": "南市口",
      "description": "市口把藥材、乾糧、布匹與各路雜貨都堆在最順手的位置，像專門替長途行旅與差役補上一口氣。和柴桑的江岸補給不同，這裡更像一座內陸主城把整片南境日常都壓縮進同一個街角。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [0, -2, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 14903 },
        { "direction": "east", "to": 14907 }
      ],
      "enquires": ["市集", "補給"]
    },
    {
      "vnum": 14907,
      "name": "藥材街角",
      "description": "幾家藥鋪與雜行把街角擠得滿是草藥與桐油氣味，來往的人不是提著包袱，就是正要替更遠的行程添上幾樣必需品。這裡不喧嘩，卻總讓人覺得沒有哪條遠路是真的脫離了長沙的照應。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [1, -2, 0],
      "labels": ["herbal", "service"],
      "exits": [
        { "direction": "north", "to": 14904 },
        { "direction": "west", "to": 14906 },
        { "direction": "south", "to": 14910 }
      ],
      "enquires": ["藥鋪", "南路"]
    },
    {
      "vnum": 14908,
      "name": "官署前街",
      "description": "官署前街收拾得格外齊整，榜示、差役與來報事的人讓這一帶始終維持著有條理的忙碌感。這裡不只是辦事所在，更像長沙這座城把四方消息重新整理與派發出去的心臟地帶。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, -1, 0],
      "labels": ["yamen", "order"],
      "exits": [
        { "direction": "north", "to": 14909 },
        { "direction": "west", "to": 14904 },
        { "direction": "south", "to": 14912 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜示一張張貼得端正，從巡查、徵調到驛路消息都分得清清楚楚，看得出這座主城對秩序的執著。"
        }
      ],
      "enquires": ["官府", "榜示"]
    },
    {
      "vnum": 14909,
      "name": "驛站偏院",
      "description": "偏院裡停著幾匹待換的馬，牆邊堆著備用草料與包袱。和熱鬧市口相比，這裡像主城真正用來把遠路接力下去的後勤核心，安靜得更有力量。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, 0, 0],
      "labels": ["post-yard", "relay"],
      "exits": [
        { "direction": "south", "to": 14908 }
      ],
      "enquires": ["驛站", "馬匹"]
    },
    {
      "vnum": 14910,
      "name": "南門官道",
      "description": "南門外的官道把長沙往更深南境送去，地面上清楚可見長年車馬壓出的兩道深痕。站在這裡時，你會很自然地明白長沙不是終點，而是所有更南旅程真正開始被整理好的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [1, -3, 0],
      "labels": ["south-edge", "road"],
      "exits": [
        { "direction": "north", "to": 14907 }
      ],
      "enquires": ["零陵", "南邊"]
    },
    {
      "vnum": 14911,
      "name": "北城望樓",
      "description": "走上望樓後，能把北門、主街與遠處官道都收入眼底。這樣的高度不只是為了守望，也像在提醒城中每一條消息與每一次轉場，最終都會先被長沙這座主城看見。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [1, -1, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 14904 }
      ],
      "enquires": ["望樓", "北門"]
    },
    {
      "vnum": 14912,
      "name": "武陵西牌",
      "description": "西牌邊立著指往武陵山路的木標，字體深而穩，像常有人在這裡停下腳步判斷下一段究竟該往城內還是往山裡。它替長沙添上一層不只管官道，也能把人送往更偏遠支線的氣味。",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [2, -2, 0],
      "labels": ["west-link", "marker"],
      "exits": [
        { "direction": "north", "to": 14908 }
      ],
      "enquires": ["武陵", "山路", "去路"]
    }
  ]
}
```
