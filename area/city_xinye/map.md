# 新野 (`city_xinye`)

## Area Intent

`city_xinye` 承接 `city_xiangyang` 官署前街外那條內陸去路，把原本只停在「往新野」路牌語意上的地方支線，正式展開成一座有酒旗、榜牆、義舍、西田路牌與北門路口的小型邊鎮。這裡不是另一座像襄陽那樣的州府大城，而是一個會讓人從腳步、招呼與街面尺度就感到「消息靠人情流動、方向靠熟路人指點」的地方城市。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `邊鎮 / 義士`
- LevelRange: `18-30`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_xinye",
    "title": "新野",
    "design_notes": "第一版 spec-first 草案。先固定東來牌門、入鎮石街、義市十字、酒旗街、榜牆前街、義舍小院、西田路牌與北門路口，把襄陽內陸支線正式落成為可載入的新野邊鎮骨架，並把西向郊野田路正式接到新野外圍。",
    "level_range": "18-30",
    "planned_vnum_range": "20201-20220",
    "reserved_room_block": "20201-20220",
    "theme": {
      "primary": "江湖",
      "secondary": "邊鎮 / 義士"
    },
    "world_links": [
      {
        "direction": "enter",
        "source_vnum": 20201,
        "target_area": "city_xiangyang",
        "target_room_vnum": 14209,
        "label": "襄陽內陸去路"
      },
      {
        "direction": "north",
        "source_vnum": 20207,
        "target_area": "city_wan",
        "target_room_vnum": 20401,
        "label": "宛道"
      },
      {
        "direction": "west",
        "source_vnum": 20205,
        "target_area": "wild_xinye_fields",
        "target_room_vnum": 20301,
        "label": "郊野田路"
      }
    ],
    "clusters": [
      { "id": "east-gate", "label": "東來牌門" },
      { "id": "main-street", "label": "入鎮石街" },
      { "id": "market-quarter", "label": "酒旗與集棚" },
      { "id": "notice-quarter", "label": "榜牆與官驛" },
      { "id": "north-road", "label": "北門與義舍" }
    ]
  },
  "rooms": [
    {
      "vnum": 20201,
      "name": "東來牌門",
      "description": "從襄陽方向轉進來後，路口先經過一座不算高大的木牌門，門板上寫著新野二字，筆劃不華美，卻有種一眼就能讓人放鬆幾分的熟地方氣。這裡沒有州府那種逼人的門威，反而更像一座替遠路人重新收拾心情的小鎮入口。",
      "sector_type": "SECT_CITY",
      "cluster": "east-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "inland-link", "world-link-enter"],
      "exits": [
        { "direction": "enter", "to": 14209, "external": true },
        { "direction": "west", "to": 20202 }
      ],
      "enquires": ["襄陽", "來路", "新野"]
    },
    {
      "vnum": 20202,
      "name": "入鎮石街",
      "description": "石街不寬，卻收拾得乾淨，兩側店面、矮牆與過路人之間始終留著剛好不擁擠也不冷清的距離。跟襄陽那種一眼看出官府秩序的節奏不同，新野的方向感更像是被人聲、酒氣和熟路腳步慢慢帶出來的。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [-1, 0, 0],
      "labels": ["approach", "orientation"],
      "exits": [
        { "direction": "east", "to": 20201 },
        { "direction": "west", "to": 20203 }
      ],
      "keywords": [
        {
          "keyword": "牌門",
          "description": "木牌門後方掛著幾條舊布幡，看得出這座鎮子不靠威勢撐場，而是靠來來往往的人把名氣活出來。"
        }
      ],
      "enquires": ["酒肆", "榜牆", "義舍"]
    },
    {
      "vnum": 20203,
      "name": "義市十字",
      "description": "街心十字把新野的用途分得很直接，西邊是酒旗和集棚，南邊是榜牆與官驛，北邊則是更安靜也更像熟人聚腳的義舍路。這裡不像大城那樣靠建築壓出秩序，而是讓你從每條岔口的人味和步調自己讀懂該往哪裡去。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [-2, 0, 0],
      "labels": ["junction", "hub", "town-core"],
      "exits": [
        { "direction": "east", "to": 20202 },
        { "direction": "west", "to": 20204 },
        { "direction": "south", "to": 20206 },
        { "direction": "north", "to": 20207 }
      ],
      "enquires": ["去路", "義士", "宛道"]
    },
    {
      "vnum": 20204,
      "name": "酒旗街",
      "description": "一排酒旗在屋簷下晃得很近，讓整條街先聞到熱湯、舊酒和行囊上的路灰。新野的熱鬧不靠大鋪面，而是靠這種能讓人停下腳、順手換一口吃食再多打聽兩句的邊鎮熟絡感。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-3, 0, 0],
      "labels": ["market", "food", "rest"],
      "exits": [
        { "direction": "east", "to": 20203 },
        { "direction": "west", "to": 20205 }
      ],
      "keywords": [
        {
          "keyword": "酒旗",
          "description": "布旗被風和油煙磨得有些舊，反倒讓人更相信這裡確實是熟客和遠路人都願意停腳的老地方。"
        }
      ],
      "enquires": ["酒肆", "歇腳", "熱湯"]
    },
    {
      "vnum": 20205,
      "name": "西田路牌",
      "description": "再往西一點，街面慢慢鬆成帶土氣的路肩，旁邊豎著寫往郊野田路的舊木牌。如今順著牌指前行，已能真正走進新野外圍的田地與村路，讓人明白這座邊鎮始終牢牢貼著那些不在官圖上寫得太清楚的小路生活。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-4, 0, 0],
      "labels": ["west-edge", "field-road", "world-link-west"],
      "exits": [
        { "direction": "east", "to": 20204 },
        { "direction": "west", "to": 20301, "external": true }
      ],
      "enquires": ["郊野", "田路", "西邊"]
    },
    {
      "vnum": 20206,
      "name": "榜牆前街",
      "description": "南邊這條街比酒旗街安靜得多，榜牆、驛牌和幾名差役把地方消息牢牢釘在視線裡。若說西邊是拿來讓人補氣歇腳的，那這裡就是新野把人、貨與傳聞重新整理清楚的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "notice-quarter",
      "coord": [-2, 1, 0],
      "labels": ["notice", "post", "information"],
      "exits": [
        { "direction": "north", "to": 20203 },
        { "direction": "west", "to": 20208 }
      ],
      "keywords": [
        {
          "keyword": "榜牆",
          "description": "榜牆上既有官面消息，也夾著不少地方人私下補寫的路況與找人字條，看得出這座鎮子的資訊從不只走一種路子。"
        }
      ],
      "enquires": ["榜文", "驛牌", "消息"]
    },
    {
      "vnum": 20207,
      "name": "北門路口",
      "description": "北門路口沒有大城那種遠遠就逼來的城威，卻能從備馬樁、舊路痕與行人眼神裡看出這裡確實連著更遠的宛道。如今順著北門再往上走，已能真正進入宛城，使這裡更明顯成了把新野交給下一段內陸城市節奏的轉接點。",
      "sector_type": "SECT_CITY",
      "cluster": "north-road",
      "coord": [-2, -1, 0],
      "labels": ["north-edge", "departure", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 20203 },
        { "direction": "north", "to": 20401, "external": true }
      ],
      "enquires": ["宛", "北門", "遠路"]
    },
    {
      "vnum": 20208,
      "name": "義舍小院",
      "description": "小院不大，卻收得很整齊，牆邊有水缸、舊木架與幾張留給熟路人暫坐的長凳。這裡不像客棧那樣熱鬧，反而更像新野真正的人情腹地，很多去路、很多消息，也常是在這種院裡被低聲講明白的。",
      "sector_type": "SECT_CITY",
      "cluster": "north-road",
      "coord": [-3, 1, 0],
      "labels": ["courtyard", "guide", "human-loop"],
      "exits": [
        { "direction": "east", "to": 20206 }
      ],
      "enquires": ["義舍", "義士", "問路"]
    }
  ]
}
```
