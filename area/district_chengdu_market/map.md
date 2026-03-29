# 成都市井 (`district_chengdu_market`)

## Area Intent

`district_chengdu_market` 承接 `city_chengdu` 的市樓牌坊，把都城主街旁原本只被看見、尚未真正走進的人潮與店鋪聲，正式展成有糧行、布招、茶食街棚、民居窄巷與告示口的市場腹地。這裡不是單純補給點，而是一段會讓玩家清楚感到「成都真正的日常、傳聞與地方人情，都在這些街棚與窄巷裡流動」的城市分區。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `市井 / 商街`
- LevelRange: `34-46`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "district_chengdu_market",
    "title": "成都市井",
    "design_notes": "第一版 spec-first 草案。先固定東牌坊口、市井主街、糧行棚廊、錦布招街、茶食街棚、民居窄巷、差役告示口與東市尾棚，讓成都市場腹地正式成為可載入的 district 骨架。",
    "level_range": "34-46",
    "planned_vnum_range": "19901-19920",
    "reserved_room_block": "19901-19920",
    "theme": {
      "primary": "歷史城市",
      "secondary": "市井 / 商街"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 19901,
        "target_area": "city_chengdu",
        "target_room_vnum": 19704,
        "label": "市樓牌坊"
      }
    ],
    "clusters": [
      { "id": "arch-entry", "label": "牌坊入口" },
      { "id": "main-street", "label": "市井主街" },
      { "id": "trade-row", "label": "糧行與茶棚" },
      { "id": "side-lanes", "label": "布招與民居巷" },
      { "id": "east-tail", "label": "告示與東市尾" }
    ]
  },
  "rooms": [
    {
      "vnum": 19901,
      "name": "東牌坊口",
      "description": "一穿過市樓牌坊，成都的熱鬧便不再只是遠遠望見，而是立刻化成迎面壓來的人聲、木幌、肩挑與討價還價。這裡依舊有都城該有的秩序，卻比主街更貼近真正維持城市呼吸的日常流動。",
      "sector_type": "SECT_CITY",
      "cluster": "arch-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "west-link", "market-threshold"],
      "exits": [
        { "direction": "west", "to": 19704, "external": true },
        { "direction": "east", "to": 19902 },
        { "direction": "south", "to": 19903 }
      ],
      "enquires": ["牌坊", "市井", "主街"]
    },
    {
      "vnum": 19902,
      "name": "市井主街",
      "description": "主街把各色招牌、人潮與喊價聲全攏成一股穩穩往前推的熱氣，讓人一眼就懂成都真正會吞吐四方貨流的，不是官道，而是這些被市聲撐滿的街面。即使再熱鬧，腳步和生意仍像被都城習慣梳理得不至於亂掉。",
      "sector_type": "SECT_CITY",
      "cluster": "main-street",
      "coord": [1, 0, 0],
      "labels": ["mainline", "trade-flow", "market-core"],
      "exits": [
        { "direction": "west", "to": 19901 },
        { "direction": "east", "to": 19904 },
        { "direction": "south", "to": 19905 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "布莊、糧行、茶棚與小鋪的招牌一層疊一層地伸出來，幾乎把天光都切成了細碎的市聲。"
        }
      ],
      "enquires": ["招牌", "糧行", "茶棚"]
    },
    {
      "vnum": 19903,
      "name": "糧行棚廊",
      "description": "棚廊下堆著米袋、秤盤與草繩，連空氣都像混著穀氣與木板被拖磨過的乾響。比起主街的表面熱鬧，這裡更像成都把真正民生與補給撐起來的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "trade-row",
      "coord": [0, -1, 0],
      "labels": ["grain-row", "stores", "supply"],
      "exits": [
        { "direction": "north", "to": 19901 },
        { "direction": "east", "to": 19905 },
        { "direction": "south", "to": 19906 }
      ],
      "enquires": ["糧行", "米袋", "採買"]
    },
    {
      "vnum": 19904,
      "name": "錦布招街",
      "description": "布色從棚沿一路垂到行人肩頭，讓這條招街比別處更亮、更密，也更容易讓人一腳放慢。成都的體面與富庶不是只寫在官府牆外，更多時候其實就被這些柔亮布面與熟練眼光靜靜撐著。",
      "sector_type": "SECT_CITY",
      "cluster": "side-lanes",
      "coord": [2, 0, 0],
      "labels": ["cloth-row", "bright-signs", "busy"],
      "exits": [
        { "direction": "west", "to": 19902 },
        { "direction": "south", "to": 19907 }
      ],
      "enquires": ["布莊", "錦布", "裁縫"]
    },
    {
      "vnum": 19905,
      "name": "茶食街棚",
      "description": "熱湯、薄餅與剛出爐的香氣把街棚撐成一段專門收留腳步的地帶，許多話題在這裡被端上桌，又在下一口熱氣裡變成新的傳聞。對外來人而言，這裡往往是市井最容易開口、也最容易聽見消息的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "trade-row",
      "coord": [1, -1, 0],
      "labels": ["tea-stalls", "rest", "rumor"],
      "exits": [
        { "direction": "north", "to": 19902 },
        { "direction": "west", "to": 19903 },
        { "direction": "east", "to": 19907 }
      ],
      "keywords": [
        {
          "keyword": "街棚",
          "description": "幾座臨時又熟練的棚架把熱湯、蒸氣與低聲閒談全攏在一起，讓整條巷口像永遠有故事正在煨著。"
        }
      ],
      "enquires": ["茶食", "傳聞", "問路"]
    },
    {
      "vnum": 19906,
      "name": "民居窄巷",
      "description": "巷子一窄下來，市聲便被壓成更貼牆、更近人的細碎聲響，晾衣、木桶和門牌把這一帶的生活氣息全攤在眼前。這裡提醒人，成都的市井並不只是做買賣，也同時養著真正住在這裡的人家。",
      "sector_type": "SECT_CITY",
      "cluster": "side-lanes",
      "coord": [0, -2, 0],
      "labels": ["residential", "narrow-lane", "local-life"],
      "exits": [
        { "direction": "north", "to": 19903 },
        { "direction": "east", "to": 19908 }
      ],
      "keywords": [
        {
          "keyword": "門牌",
          "description": "斑駁門牌被掛得很低，像是專替熟門熟路的人辨認，不特地向陌生人解釋。"
        }
      ],
      "enquires": ["民居", "巷子", "住戶"]
    },
    {
      "vnum": 19907,
      "name": "差役告示口",
      "description": "幾張新舊不一的榜示貼在牆邊，旁邊總有差役、行腳人和順路停下來看熱鬧的人。這裡不像官府前廊那樣嚴整，卻更接近地方消息真正被散出去、再被各色人等接住的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "east-tail",
      "coord": [2, -1, 0],
      "labels": ["notice", "bailiff", "quest-hook"],
      "exits": [
        { "direction": "north", "to": 19904 },
        { "direction": "west", "to": 19905 },
        { "direction": "south", "to": 19908 }
      ],
      "keywords": [
        {
          "keyword": "告示",
          "description": "榜紙上有尋人、有催繳、有臨時徵工，也有看起來像故意留給膽子大的人去接的模糊委託。"
        }
      ],
      "enquires": ["告示", "差役", "委託"]
    },
    {
      "vnum": 19908,
      "name": "東市尾棚",
      "description": "走到市尾後，人潮終於鬆開些，喧嘩仍在，卻更像被長街慢慢拉成了尾音。這裡不像真正的出口，反而像成都市場還能再往更深處展開的暗示，提醒人眼前這一段仍只是都城腹地的第一層。",
      "sector_type": "SECT_CITY",
      "cluster": "east-tail",
      "coord": [1, -2, 0],
      "labels": ["east-tail", "future-depth", "market-fringe"],
      "exits": [
        { "direction": "north", "to": 19907 },
        { "direction": "west", "to": 19906 }
      ],
      "enquires": ["市尾", "東邊", "深巷"]
    }
  ]
}
```
