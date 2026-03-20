# 零陵 (`city_lingling`)

## Area Intent

`city_lingling` 承接 `city_changsha` 南向主線，讓玩家從武陵山前帶與荊南主城的節奏，再進一步收束到一座更有地方氣、也更帶山城奇聞的南境城市。

第一版目標先固定：

- 一條由北向南穿過城門、主街與南口的主探索線
- 一條往市集與補給區延伸的側線
- 一條 `up/down` 連到城樓或坡城望臺的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示零陵、長沙、城門、榜示與更南去路

## Theme Positioning

- Theme: `江湖`
- Subtheme: `山城主邑 / 奇聞與轉運`
- LevelRange: `84-94`
- Parent region: `荊南南段`
- World gap filled: 讓南線從長沙與武陵段繼續推進到新的山城 hub，為桂陽與更南區線建立穩定母城

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_lingling",
    "title": "零陵",
    "design_notes": "第一版 spec-first 草案。先固定北門、主街、市集、官署與南向出城骨架，讓荊南主線在零陵收束成更有地方氣的山城 hub。",
    "level_range": "84-94",
    "planned_vnum_range": "15101-15130",
    "reserved_room_block": "15101-15130",
    "theme": {
      "primary": "江湖",
      "secondary": "山城主邑 / 奇聞與轉運"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 15101,
        "target_area": "city_changsha",
        "label": "長沙北路"
      },
      {
        "direction": "south",
        "source_vnum": 15110,
        "target_area": "city_guiyang",
        "label": "桂陽官道"
      }
    ],
    "clusters": [
      { "id": "north-gate", "label": "北向城門" },
      { "id": "main-street", "label": "主街中心" },
      { "id": "market-quarter", "label": "市集補給區" },
      { "id": "yamen-quarter", "label": "官署與榜示區" },
      { "id": "south-road", "label": "南向出城區" }
    ]
  },
  "rooms": [
    {
      "vnum": 15101,
      "name": "北向城門",
      "description": "由長沙一路南下到此，城門與坡城石路把人慢慢從官道節奏收進零陵自己的步調。這裡不若大城那樣寬闊，卻有一種靠山而築、靠消息與人情維持秩序的厚實感。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-link"],
      "exits": [
        { "direction": "north", "to": 14910, "external": true },
        { "direction": "south", "to": 15103 },
        { "direction": "east", "to": 15102 },
        { "direction": "west", "to": 15105 }
      ],
      "enquires": ["長沙", "進城"]
    },
    {
      "vnum": 15102,
      "name": "北牌坡口",
      "description": "坡口邊立著幾面指向長沙與更南路線的舊木牌，字體不算工整，卻帶著地方城鎮才有的實用感。站在這裡時，很容易感覺到零陵不是帝都式的中心，而是南境真正靠熟路人維持運作的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [1, 0, 0],
      "labels": ["wayfinding", "slope"],
      "exits": [
        { "direction": "west", "to": 15101 },
        { "direction": "south", "to": 15104 }
      ],
      "enquires": ["路牌", "去路"]
    },
    {
      "vnum": 15103,
      "name": "零陵主街",
      "description": "主街不算特別寬，卻把城門、市集與官署穩穩串在一起，來往行人與沿街招牌都帶著地方生活的密度。和長沙相比，這裡更像一座把江湖傳聞與日常買賣混在同一條街上的山城。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [0, -1, 0],
      "labels": ["main-street", "hub"],
      "exits": [
        { "direction": "north", "to": 15101 },
        { "direction": "east", "to": 15104 },
        { "direction": "south", "to": 15106 }
      ],
      "enquires": ["零陵", "市集"]
    },
    {
      "vnum": 15104,
      "name": "主街十字",
      "description": "幾條街巷在這裡交會，榜示、店招與過路人的低聲議論讓零陵作為山城節點的性格一眼可辨。站在十字口時，你會直覺地知道哪裡能補給、哪裡能打聽消息、哪裡則會送你往更南。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, -1, 0],
      "labels": ["crossroads", "civic"],
      "exits": [
        { "direction": "north", "to": 15102 },
        { "direction": "west", "to": 15103 },
        { "direction": "east", "to": 15108 },
        { "direction": "south", "to": 15107 },
        { "direction": "up", "to": 15111 }
      ],
      "enquires": ["官府", "南邊", "奇聞"]
    },
    {
      "vnum": 15105,
      "name": "北巷轉角",
      "description": "這段北巷比主街安靜許多，卻仍能聽見遠處市聲與坡城馬蹄聲。牆角積著些許山霧帶來的潮氣，讓零陵的城與山始終像黏在一起，分也分不乾淨。",
      "sector_type": "SECT_CITY",
      "cluster": "north-gate",
      "coord": [-1, 0, 0],
      "labels": ["side-lane", "quiet"],
      "exits": [
        { "direction": "east", "to": 15101 }
      ],
      "enquires": ["巷子", "城門"]
    },
    {
      "vnum": 15106,
      "name": "南市口",
      "description": "市口把藥材、乾糧、布匹與些許奇特小物都集中在同一帶，像一座真正靠遠近行旅、地方傳聞與山路交易一起活著的城市。這裡不像大市那樣喧鬧，卻有種讓人不知不覺停下腳步的吸力。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [0, -2, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 15103 },
        { "direction": "east", "to": 15107 }
      ],
      "enquires": ["市集", "補給"]
    },
    {
      "vnum": 15107,
      "name": "藥鋪街角",
      "description": "幾家藥鋪與雜貨攤把街角擠得滿是草藥、桐油與乾貨味，像再遠的南路也總得先在這裡添齊東西才敢出發。比起長沙的官道補給，零陵這裡更像熟門熟路的人彼此照應的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [1, -2, 0],
      "labels": ["herbal", "service"],
      "exits": [
        { "direction": "north", "to": 15104 },
        { "direction": "west", "to": 15106 },
        { "direction": "south", "to": 15110 }
      ],
      "enquires": ["藥鋪", "南路"]
    },
    {
      "vnum": 15108,
      "name": "官署前街",
      "description": "官署前街收拾得相當齊整，卻不像大城那樣刻板，反而保留了一種地方主事者才有的靈活與人情。榜示貼得端正，路過的人也總會多看兩眼，像零陵的消息有時就藏在這些細節裡。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, -1, 0],
      "labels": ["yamen", "order"],
      "exits": [
        { "direction": "north", "to": 15109 },
        { "direction": "west", "to": 15104 },
        { "direction": "south", "to": 15112 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜示上除了例行巡查與徵調，也常夾著些地方上才懂的暗示與傳聞，讓人忍不住多看幾眼。"
        }
      ],
      "enquires": ["官府", "榜示"]
    },
    {
      "vnum": 15109,
      "name": "城巷偏院",
      "description": "偏院不大，卻收拾得頗有秩序，像是這座山城把日常雜務與地方消息暫時收進來整理的地方。比起熱鬧市口，這裡更容易讓人感覺到零陵真正的生活脈搏。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, 0, 0],
      "labels": ["side-yard", "quiet"],
      "exits": [
        { "direction": "south", "to": 15108 }
      ],
      "enquires": ["偏院", "消息"]
    },
    {
      "vnum": 15110,
      "name": "南門官道",
      "description": "南門外的官道沿著地勢一路往更深南境延去，路面上留著明顯車轍與山路磨痕。站在這裡時，你會很清楚地知道零陵不是終點，而是把人再往南送一段的重要山城中繼。 ",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [1, -3, 0],
      "labels": ["south-edge", "road"],
      "exits": [
        { "direction": "north", "to": 15107 },
        { "direction": "south", "to": 15201, "external": true }
      ],
      "enquires": ["桂陽", "南邊"]
    },
    {
      "vnum": 15111,
      "name": "坡城望樓",
      "description": "走上望樓後，能把北門、主街與坡道上的來路都收入眼底。從這裡俯看零陵，你會更明白這座城雖不巨大，卻有種把南境來路都收進眼中的穩定力量。 ",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [1, -1, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15104 }
      ],
      "enquires": ["望樓", "北門"]
    },
    {
      "vnum": 15112,
      "name": "南街路牌",
      "description": "路牌邊的木柱被歲月磨得發亮，卻仍牢牢指著更南的官道路線。它不像什麼大場面的地標，卻是每個繼續往下走的人都會本能停一下、重新確認方向的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "south-road",
      "coord": [2, -2, 0],
      "labels": ["marker", "south-link"],
      "exits": [
        { "direction": "north", "to": 15108 }
      ],
      "enquires": ["路牌", "去路", "南邊"]
    }
  ]
}
```
