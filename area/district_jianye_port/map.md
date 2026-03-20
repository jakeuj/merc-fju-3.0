# 建業港區 (`district_jianye_port`)

## Area Intent

`district_jianye_port` 承接 `city_jianye` 東向港向街口，把玩家從都城主街真正帶進港務、貨棚、泊位與船行交錯的商港分區。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `碼頭 / 商港`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "district_jianye_port",
    "title": "建業港區",
    "design_notes": "第一版 spec-first 草案。先固定港向街口、碼頭主道、貨棚泊位、船行牌坊與外向商船棧，把建業主城的對外航運服務正式細化成港區分區。",
    "level_range": "100-100",
    "planned_vnum_range": "16101-16130",
    "reserved_room_block": "16101-16130",
    "theme": {
      "primary": "歷史城市",
      "secondary": "碼頭 / 商港"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 16101,
        "target_area": "city_jianye",
        "label": "港向街口"
      },
      {
        "direction": "south",
        "source_vnum": 16110,
        "target_area": "sea_trade_route",
        "label": "商船航路"
      },
      {
        "direction": "east",
        "source_vnum": 16109,
        "target_area": "district_shipyards",
        "label": "造船區"
      }
    ],
    "clusters": [
      { "id": "street-entry", "label": "港向入口" },
      { "id": "main-dock", "label": "碼頭主道" },
      { "id": "cargo-yard", "label": "貨棚泊位" },
      { "id": "guild-row", "label": "船行牌坊" },
      { "id": "outer-pier", "label": "外向棧道" }
    ]
  },
  "rooms": [
    {
      "vnum": 16101,
      "name": "港向街口",
      "description": "離開建業主城後，街面上的節奏很快就被貨聲、叫價和纜繩摩擦木樁的聲音接手。這裡仍屬於建業，但已經明顯不是內城治理的節奏，而是對外往來真正開始湧動的地方。 ",
      "sector_type": "SECT_CITY",
      "cluster": "street-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-link"],
      "exits": [
        { "direction": "west", "to": 16010, "external": true },
        { "direction": "east", "to": 16103 },
        { "direction": "south", "to": 16102 }
      ],
      "enquires": ["港區", "主城", "去路"]
    },
    {
      "vnum": 16102,
      "name": "綁纜側棚",
      "description": "側棚下堆著纜繩、木樁和各種補修雜物，讓人一看就知道這裡真正重視的不是好看，而是任何一艘靠岸的船都得立刻能被接住。港埠的秩序往往就是從這種不起眼的地方開始。 ",
      "sector_type": "SECT_CITY",
      "cluster": "street-entry",
      "coord": [0, -1, 0],
      "labels": ["ropes", "side-shed"],
      "exits": [
        { "direction": "north", "to": 16101 }
      ],
      "enquires": ["纜繩", "棚子"]
    },
    {
      "vnum": 16103,
      "name": "碼頭主道",
      "description": "主道比城內街巷更寬，也更願意讓車輪和人潮同時擠出自己的聲量。走在這裡時，很難不感覺整個港區真正的心跳正在腳下這條道上往復奔忙。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-dock",
      "coord": [1, 0, 0],
      "labels": ["mainline", "dock-road"],
      "exits": [
        { "direction": "west", "to": 16101 },
        { "direction": "east", "to": 16104 },
        { "direction": "south", "to": 16105 }
      ],
      "enquires": ["碼頭", "貨棚"]
    },
    {
      "vnum": 16104,
      "name": "船行牌坊",
      "description": "幾座掛滿船行招牌與航線木牌的牌坊把港區最精明、也最世故的一面清楚亮了出來。這裡的每一塊字牌都像在說，遠方再遠，也得先經過這些人手裡的秤與帳。 ",
      "sector_type": "SECT_CITY",
      "cluster": "guild-row",
      "coord": [2, 0, 0],
      "labels": ["guilds", "trade-signs"],
      "exits": [
        { "direction": "west", "to": 16103 },
        { "direction": "south", "to": 16108 },
        { "direction": "east", "to": 16109 }
      ],
      "enquires": ["船行", "航路", "牌坊"]
    },
    {
      "vnum": 16105,
      "name": "貨棚泊位",
      "description": "貨棚和泊位在這裡直接接在一起，讓裝卸、盤點和搬運幾乎沒有空隙。港區真正讓人佩服的地方不是熱鬧，而是這種熱鬧居然還能維持成秩序。 ",
      "sector_type": "SECT_CITY",
      "cluster": "cargo-yard",
      "coord": [1, -1, 0],
      "labels": ["cargo", "berth"],
      "exits": [
        { "direction": "north", "to": 16103 },
        { "direction": "east", "to": 16108 }
      ],
      "enquires": ["貨棚", "泊位"]
    },
    {
      "vnum": 16108,
      "name": "外港號棚",
      "description": "號棚立在主泊位和外棧之間，專管喊價、點貨與安排船期，像整個港區所有最喧嘩的聲音最後都得在這裡變成真正能執行的次序。這裡不是城門，卻同樣掌著出入。 ",
      "sector_type": "SECT_CITY",
      "cluster": "main-dock",
      "coord": [2, -1, 0],
      "labels": ["signal", "booking"],
      "exits": [
        { "direction": "west", "to": 16105 },
        { "direction": "north", "to": 16104 },
        { "direction": "south", "to": 16110 }
      ],
      "enquires": ["號棚", "船期", "南邊"]
    },
    {
      "vnum": 16109,
      "name": "東向工棧",
      "description": "幾座工棧和木料堆把港區更偏技術與製造的一面露了出來，像再往東去，節奏就不只是裝卸和交易，而會更靠近造船、修補和長線準備本身。 ",
      "sector_type": "SECT_CITY",
      "cluster": "guild-row",
      "coord": [3, 0, 0],
      "labels": ["east-link", "workyards"],
      "exits": [
        { "direction": "west", "to": 16104 }
      ],
      "enquires": ["東邊", "工棧", "造船"]
    },
    {
      "vnum": 16110,
      "name": "商船外棧",
      "description": "外棧邊停著的多是準備往更遠水路去的商船，和城內可預期的節奏相比，這裡更像建業把手真正伸向外面的地方。只要再往南去，城市的庇護感就會迅速被航線本身接手。 ",
      "sector_type": "SECT_CITY",
      "cluster": "outer-pier",
      "coord": [2, -2, 0],
      "labels": ["south-link", "trade-route"],
      "exits": [
        { "direction": "north", "to": 16108 }
      ],
      "enquires": ["商船", "南邊", "航路"]
    }
  ]
}
```
