# 襄平 (`city_xiangping`)

## Area Intent

`city_xiangping` 承接 `wild_barbarian_camp` 東向城路口，把玩家從白狼山與胡營舊地那種邊地壓力、敵蹤記憶與 hostile wild 節奏，重新收束進一座真正帶秩序、補給、訓練與地方勢力流動感的遼東邊城。這裡不只是北境鏈上的下一個名字，而是要讓 `白狼山 -> 胡營舊地 -> 襄平` 這條主線第一次回到能整補、問路、學技與重新分流的城市 hub。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `遼東邊城 / 驛站與服務樞紐`
- LevelRange: `34-46`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_xiangping",
    "title": "襄平",
    "design_notes": "第一版 spec-first 草案。先固定西向城路、主街十字、驛站補給、太守府前街、藥材行與北向雙分流，讓襄平成為北境主線回城整補與繼續往遼東深處推進的城市 hub。",
    "level_range": "34-46",
    "planned_vnum_range": "18301-18330",
    "reserved_room_block": "18301-18330",
    "theme": {
      "primary": "軍旅",
      "secondary": "遼東邊城 / 驛站與服務樞紐"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 18301,
        "target_area": "wild_barbarian_camp",
        "label": "胡營舊地方向"
      },
      {
        "direction": "north",
        "source_vnum": 18308,
        "target_area": "wild_liaodong_plain",
        "label": "遼東平原"
      },
      {
        "direction": "north",
        "source_vnum": 18309,
        "target_area": "road_north_border",
        "label": "北境邊道"
      }
    ],
    "clusters": [
      { "id": "west-gate", "label": "西向城門帶" },
      { "id": "main-street", "label": "主街與城心" },
      { "id": "service-quarter", "label": "驛站與補給帶" },
      { "id": "office-quarter", "label": "太守府與教導帶" },
      { "id": "north-splits", "label": "北向分流帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 18301,
      "name": "西城路口",
      "description": "胡營舊地帶來的緊繃感在這裡被城牆、門洞與守望秩序慢慢收住，像一路從邊地荒痕走來的人終於被重新放回人煙裡。西城路口讓人第一眼就明白，襄平不是更大的營地，而是一座能把北境消息和旅人重新整進規矩的邊城。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 18208, "external": true },
        { "direction": "east", "to": 18302 }
      ],
      "enquires": ["胡營", "進城", "襄平"]
    },
    {
      "vnum": 18302,
      "name": "襄平西街",
      "description": "西街把外來人先從門口的打量，慢慢帶進有生意、有差役、有驛務來往的城市節奏裡。即使還能聞到邊地塵土，這裡也已經開始是襄平自己的秩序，而不是荒外帶進來的規矩。 ",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [1, 0, 0],
      "labels": ["street", "transition"],
      "exits": [
        { "direction": "west", "to": 18301 },
        { "direction": "east", "to": 18303 }
      ],
      "enquires": ["西街", "城裡"]
    },
    {
      "vnum": 18303,
      "name": "襄平主街",
      "description": "主街上的聲音很雜，卻不是混亂，而是把商旅、差役、教導者和遠路消息混成一種只有邊城才有的節奏。站在這裡時，會明顯感到襄平真正的價值不只在守邊，更在於它能把四面來的人都重新編入可運作的城市網。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [2, 0, 0],
      "labels": ["main-road", "city-flow"],
      "exits": [
        { "direction": "west", "to": 18302 },
        { "direction": "east", "to": 18304 },
        { "direction": "north", "to": 18305 }
      ],
      "enquires": ["主街", "消息", "去處"]
    },
    {
      "vnum": 18304,
      "name": "城心十字",
      "description": "城心十字把襄平的邊城功能攤開在眼前：西邊是進城與出城的過渡，北邊是更遠遼東的分流，南北兩側則各自聚著補給、教導與官府秩序。這裡不像內地大城那樣繁富，但每一條去路都帶著明顯用途。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [3, 0, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "west", "to": 18303 },
        { "direction": "north", "to": 18308 },
        { "direction": "south", "to": 18306 },
        { "direction": "east", "to": 18309 }
      ],
      "enquires": ["驛站", "太守府", "北路"]
    },
    {
      "vnum": 18305,
      "name": "驛站前街",
      "description": "驛站前街比城門口更忙，馬匹、差票與短暫停腳的人把這裡撐出一種實用而不拖泥帶水的熱鬧。對長路上的玩家來說，這裡最像一個真正能重新整理狀態、問清去向再上路的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [2, 1, 0],
      "labels": ["station", "service"],
      "exits": [
        { "direction": "south", "to": 18303 },
        { "direction": "east", "to": 18307 }
      ],
      "enquires": ["驛站", "補給", "倫直"]
    },
    {
      "vnum": 18306,
      "name": "藥材行前",
      "description": "藥香和乾草氣在這條前街混得很濃，讓人一靠近就知道這裡不只是補藥的地方，也可能碰上更講究門道的邊城技藝。與前線營地相比，襄平真正厲害的地方，往往就在這些能把生存手段變成服務節點的店面。 ",
      "sector_type": "SECT_CITY",
      "cluster": "service-quarter",
      "coord": [3, -1, 0],
      "labels": ["shop", "supply"],
      "exits": [
        { "direction": "north", "to": 18304 }
      ],
      "enquires": ["藥材行", "抹毒", "藥"]
    },
    {
      "vnum": 18307,
      "name": "太守府前街",
      "description": "越靠近太守府，街上的氣氛就越像從旅路與市聲裡抽出一條更安靜的秩序線。這裡不只代表官府，也代表那些在邊城裡真正掌握知識、訓練與消息分配的人，讓襄平不只是守邊，更是能培養與篩選人的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "office-quarter",
      "coord": [3, 1, 0],
      "labels": ["office", "training"],
      "exits": [
        { "direction": "west", "to": 18305 }
      ],
      "enquires": ["太守府", "訓練", "玉霖"]
    },
    {
      "vnum": 18308,
      "name": "北原牌樓",
      "description": "北原牌樓把視線從城心重新放向更開闊的遼東平原，出城的人多半不是只想碰碰運氣，而是有明確目的地與補給計畫。站在這裡時，襄平的角色就很清楚: 它是北境長路前最後一個真正像樣的城市整補點。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-splits",
      "coord": [3, 2, 0],
      "labels": ["north-link", "plain-route"],
      "exits": [
        { "direction": "south", "to": 18304 }
      ],
      "enquires": ["平原", "北原", "遼東"]
    },
    {
      "vnum": 18309,
      "name": "北境邊道路口",
      "description": "這條路口比北原牌樓更帶軍務與長途色彩，連看路的人都更像在算距離與風險，而不是單純問去哪裡。它把襄平和更北更遠的邊道真正接起來，也讓這座城市的邊城屬性在此顯得格外明確。 ",
      "sector_type": "SECT_CITY",
      "cluster": "north-splits",
      "coord": [4, 0, 0],
      "labels": ["north-link", "border-road"],
      "exits": [
        { "direction": "west", "to": 18304 }
      ],
      "enquires": ["邊道", "北路", "出關"]
    }
  ]
}
```
