# 濮陽 (`city_puyang`)

## Area Intent

`city_puyang` 用來補上目前兗州河北鏈裡一個很實際的空缺：我們已經有 `wild_puyang_forest` 的林野前帶，也有 `dng_guandu_battlefield` 的官渡戰場，但兩者之間還缺一座真正能把河北前線消息、補給與軍旅節奏收束起來的前沿主城。這裡要讓玩家感受到濮陽不是純後方，也不是直接進戰場，而是一座隨時能聞到前線風聲的軍政樞紐。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `河北前沿 / 糧道與軍政中繼`
- LevelRange: `20-32`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_puyang",
    "title": "濮陽",
    "design_notes": "第一版 spec-first 草案。先固定西向林外路口、主街十字、市集補給與東向官渡糧道，讓濮陽把林野與戰場之間缺掉的前沿主城節點補起來。",
    "level_range": "20-32",
    "planned_vnum_range": "17201-17220",
    "reserved_room_block": "17201-17220",
    "theme": {
      "primary": "軍旅",
      "secondary": "河北前沿 / 糧道與軍政中繼"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 17201,
        "target_area": "wild_puyang_forest",
        "label": "濮陽林外路"
      },
      {
        "direction": "east",
        "source_vnum": 17208,
        "target_area": "dng_guandu_battlefield",
        "label": "官渡糧道殘線"
      },
      {
        "direction": "south",
        "source_vnum": 17207,
        "target_area": "road_puyang",
        "label": "南驛官道"
      },
      {
        "direction": "north",
        "source_vnum": 17209,
        "target_area": "city_nanpi",
        "label": "河北北路"
      }
    ],
    "clusters": [
      { "id": "west-gate", "label": "西門前帶" },
      { "id": "main-street", "label": "主街與城心" },
      { "id": "market-yard", "label": "市集補給帶" },
      { "id": "military-lane", "label": "軍務與糧道帶" },
      { "id": "north-link", "label": "北路分流帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17201,
      "name": "西門林外口",
      "description": "從林野邊路走到這裡時，濮陽西門的輪廓並不帶來純然安定，反而更像一道把散亂消息重新收進城裡的關口。門外還沾著林泥與濕草氣，門內卻已經能聞到糧車、兵甲與市聲混成的前沿城氣。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-edge", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 13906, "external": true },
        { "direction": "east", "to": 17202 }
      ],
      "enquires": ["濮陽", "西門", "林外"]
    },
    {
      "vnum": 17202,
      "name": "西門甬道",
      "description": "甬道兩側的木牌與盤查名冊讓剛進城的人立刻明白，濮陽雖有煙火氣，卻不是能隨便鬆懈的地方。越靠近官渡，連一座城怎麼看人、怎麼留人，都會多出幾分軍務緊張。",
      "sector_type": "SECT_CITY",
      "cluster": "west-gate",
      "coord": [1, 0, 0],
      "labels": ["checkpoint", "transition"],
      "exits": [
        { "direction": "west", "to": 17201 },
        { "direction": "east", "to": 17203 }
      ],
      "enquires": ["盤查", "路引"]
    },
    {
      "vnum": 17203,
      "name": "濮陽主街",
      "description": "主街上來往的人不算少，卻沒有大城那種純商旅喧鬧，反而總透著一股『任何人都可能跟前線有關』的氣息。糧商、差役、押車人與臨時徵調的腳夫混在一起，讓整條街都像在替更遠的戰事運作。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [2, 0, 0],
      "labels": ["main-road", "city-flow"],
      "exits": [
        { "direction": "west", "to": 17202 },
        { "direction": "east", "to": 17204 },
        { "direction": "south", "to": 17205 }
      ],
      "enquires": ["主街", "市集", "官渡"]
    },
    {
      "vnum": 17204,
      "name": "城心十字",
      "description": "城心十字把濮陽的真正性格都攤在眼前：一邊是補給與人煙，一邊是軍務與糧道，再往北還有河北各路傳來的消息。站在這裡時最能感覺到濮陽不是單純前線，而是把整個前線壓力整理成可運作秩序的樞紐。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [3, 0, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "west", "to": 17203 },
        { "direction": "south", "to": 17206 },
        { "direction": "east", "to": 17208 },
        { "direction": "north", "to": 17209 }
      ],
      "enquires": ["去路", "糧道", "北路"]
    },
    {
      "vnum": 17205,
      "name": "前街市集",
      "description": "牌樓與攤棚把這裡撐出一塊比戰線稍微鬆口氣的空間，卻依然能從貨色看出濮陽的前沿性格: 乾糧、水囊、燈油、繩索都比精巧玩物多得多。這裡賣的不是悠閒，而是讓人再走一段的把握。",
      "sector_type": "SECT_CITY",
      "cluster": "market-yard",
      "coord": [2, -1, 0],
      "labels": ["market", "supplies"],
      "exits": [
        { "direction": "north", "to": 17203 }
      ],
      "enquires": ["市集", "補給", "糧行"]
    },
    {
      "vnum": 17206,
      "name": "軍務前街",
      "description": "這條街比主街安靜得多，糧冊、文牘與巡令卻比人聲更有存在感。濮陽能在河北前沿站穩，不只是因為有牆有兵，也因為所有通往官渡與北路的消息，都會先在這裡被整理、核對與分派。",
      "sector_type": "SECT_CITY",
      "cluster": "military-lane",
      "coord": [3, -1, 0],
      "labels": ["office", "military"],
      "exits": [
        { "direction": "north", "to": 17204 },
        { "direction": "south", "to": 17207 }
      ],
      "enquires": ["軍務", "官府", "糧冊"]
    },
    {
      "vnum": 17207,
      "name": "南驛牌口",
      "description": "往南的驛路牌口把濮陽和更後方的城市聯繫收得很緊，像任何離城的人都會被提醒，前線所需的一切仍得靠這條路反覆輸送。站在這裡時，才會真正理解濮陽和純戰地之間最大的差別，就是它還保有一條能把秩序往後送的命脈。",
      "sector_type": "SECT_CITY",
      "cluster": "military-lane",
      "coord": [3, -2, 0],
      "labels": ["south-link", "route-node"],
      "exits": [
        { "direction": "north", "to": 17206 }
      ],
      "enquires": ["南路", "驛站", "後方"]
    },
    {
      "vnum": 17208,
      "name": "東糧道口",
      "description": "東向糧道口比城中其他地方都更能感到壓力堆積，車轍、泥灰與換馬聲把『官渡不遠』這件事說得非常明白。再往東，濮陽的城市氣息會很快讓位給戰場留下的焦痕與殘線，因此這裡像是一道把城市秩序送進戰地的門檻。",
      "sector_type": "SECT_CITY",
      "cluster": "military-lane",
      "coord": [4, 0, 0],
      "labels": ["east-link", "war-route"],
      "exits": [
        { "direction": "west", "to": 17204 },
        { "direction": "east", "to": 14007, "external": true }
      ],
      "enquires": ["糧道", "官渡", "東邊"]
    },
    {
      "vnum": 17209,
      "name": "北路牌樓",
      "description": "北路牌樓把濮陽往河北深處的氣息慢慢拉直，與東邊官渡的壓力相比，這裡更多的是長線行旅與邊地消息的感覺。可即使方向不同，那股前沿城市特有的緊繃仍在，像任何一條路都不是純粹平靜的出城路。",
      "sector_type": "SECT_CITY",
      "cluster": "north-link",
      "coord": [3, 1, 0],
      "labels": ["north-link", "gate-road"],
      "exits": [
        { "direction": "south", "to": 17204 }
      ],
      "enquires": ["北路", "南皮", "去路"]
    }
  ]
}
```
