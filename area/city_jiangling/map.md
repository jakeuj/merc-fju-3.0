# 江陵 (`city_jiangling`)

## Area Intent

`city_jiangling` 承接 `wild_wuling` 北山舊道，把原本只靠車轍與山關痕跡暗示的出口，正式收束回一座會重新替旅人整理方向感的荊蜀轉接主城。這裡不靠山氣與岔路施壓，而是用南城門、西市、官署榜文與西關路口，讓玩家明顯感到自己重新回到有秩序、有補給、也有更大範圍交通骨架的地方。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `荊蜀轉接`
- LevelRange: `38-52`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "city_jiangling",
    "title": "江陵",
    "design_notes": "第一版 spec-first 草案。先固定南城門、入城大道、城心十字、西市補給線、官署榜文線與西關路口，把武陵山北出支線正式收束成可載入的荊蜀轉接城市 hub。",
    "level_range": "38-52",
    "planned_vnum_range": "19301-19320",
    "reserved_room_block": "19301-19320",
    "theme": {
      "primary": "歷史城市",
      "secondary": "荊蜀轉接"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 19301,
        "target_area": "wild_wuling",
        "target_room_vnum": 15011,
        "label": "北山關路"
      },
      {
        "direction": "west",
        "source_vnum": 19308,
        "target_area": "fort_yiling",
        "target_room_vnum": 19401,
        "label": "西關去路"
      }
    ],
    "clusters": [
      { "id": "south-gate", "label": "南城門帶" },
      { "id": "main-avenue", "label": "主街十字" },
      { "id": "market-quarter", "label": "西市補給線" },
      { "id": "yamen-quarter", "label": "官署榜文線" },
      { "id": "west-road", "label": "西關路口" }
    ]
  },
  "rooms": [
    {
      "vnum": 19301,
      "name": "南城門",
      "description": "江陵南城門不像邊關那樣壓得人喘不過氣，卻也不會讓剛出山的人誤以為自己已完全脫離盤查與秩序。門外還留著山路帶來的風土與草氣，門內卻已能聞到熱湯、藥材與木牌墨痕混在一起的城市味道。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 15011, "external": true },
        { "direction": "north", "to": 19302 }
      ],
      "enquires": ["城門", "北山", "去路"]
    },
    {
      "vnum": 19302,
      "name": "入城大道",
      "description": "入城大道兩旁的路牌、布旗與木棚把人流自然整理開來，讓剛離開深山的人很快就能重新讀懂哪些方向屬於補給、哪些方向屬於官務。這種一眼可辨的秩序，本身就是城市給旅人的第一種安定。",
      "sector_type": "SECT_CITY",
      "cluster": "south-gate",
      "coord": [0, 1, 0],
      "labels": ["approach", "orientation"],
      "exits": [
        { "direction": "south", "to": 19301 },
        { "direction": "north", "to": 19303 }
      ],
      "keywords": [
        {
          "keyword": "路牌",
          "description": "木牌上把西市、官署與西關路口都寫得很清楚，像是不想讓任何剛出山的人再在城裡迷一次路。"
        }
      ],
      "enquires": ["路牌", "西市", "官署"]
    },
    {
      "vnum": 19303,
      "name": "城心十字",
      "description": "城心十字把江陵的用途拆得很乾淨，西邊是行旅與補給，東邊是官署與榜文，往北則更接近出關與遠行的路。站在這裡時，整座城的節奏會一下子變得很好懂，像它本來就是拿來替人重新整理方向的。",
      "sector_type": "SECT_CITY",
      "cluster": "main-avenue",
      "coord": [0, 2, 0],
      "labels": ["junction", "hub"],
      "exits": [
        { "direction": "south", "to": 19302 },
        { "direction": "west", "to": 19304 },
        { "direction": "east", "to": 19306 },
        { "direction": "north", "to": 19308 }
      ],
      "enquires": ["江陵", "去路", "西關"]
    },
    {
      "vnum": 19304,
      "name": "西市口",
      "description": "西市口的人聲比城門更碎更密，叫賣、議價與遠路消息全擠在一起，聽久了幾乎分不清哪句是買賣、哪句是傳聞。對趕路人來說，這種雜而不亂的熱度反而最能證明自己真的回到了主世界的節奏裡。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-1, 2, 0],
      "labels": ["market", "crowd"],
      "exits": [
        { "direction": "east", "to": 19303 },
        { "direction": "west", "to": 19305 }
      ],
      "keywords": [
        {
          "keyword": "招牌",
          "description": "木招牌與布幌從屋簷下層層伸出，把整條西市口擠成一片熱鬧而熟練的補給帶。"
        }
      ],
      "enquires": ["市集", "補給", "客棧"]
    },
    {
      "vnum": 19305,
      "name": "行旅客棧前",
      "description": "客棧前街雖不算寬，卻堆滿了熱湯香氣、行囊、乾糧與準備再上路的木箱，看得出這裡常替剛進城的人把疲憊和方向一起安頓下來。比起單純住店，它更像一個把旅程重新接起來的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "market-quarter",
      "coord": [-2, 2, 0],
      "labels": ["inn", "supply", "rest"],
      "exits": [
        { "direction": "east", "to": 19304 }
      ],
      "enquires": ["客棧", "熱湯", "休息"]
    },
    {
      "vnum": 19306,
      "name": "官署前街",
      "description": "官署前街比主街安靜得多，靴聲、差役回報與偶爾翻動公文的聲響把整條街撐出一種乾燥而穩定的秩序。這裡提醒人，江陵不只是中繼城，也是會把邊地消息往更大地方送出去的節點。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [1, 2, 0],
      "labels": ["yamen", "order", "information"],
      "exits": [
        { "direction": "west", "to": 19303 },
        { "direction": "east", "to": 19307 }
      ],
      "enquires": ["官府", "差役", "榜文"]
    },
    {
      "vnum": 19307,
      "name": "榜文長廊",
      "description": "長廊一側掛著新舊榜文，從道路消息、盤查令到某些不願寫得太明白的地方異聞，全都在這裡留下過痕跡。若只想知道下一段該往哪裡去，這裡往往比街上更快給出答案。",
      "sector_type": "SECT_CITY",
      "cluster": "yamen-quarter",
      "coord": [2, 2, 0],
      "labels": ["bulletin", "rumor", "notice"],
      "exits": [
        { "direction": "west", "to": 19306 }
      ],
      "enquires": ["榜文", "消息", "西關"]
    },
    {
      "vnum": 19308,
      "name": "西關路口",
      "description": "再往北一點，街面開始收束成更偏軍務與遠行用途的路口，木柵、備馬處與西去路標都比城心十字更少煙火氣。站在這裡時，會很清楚地感覺到江陵既是城市，也是更大蜀荊主線重新分流的地方。",
      "sector_type": "SECT_CITY",
      "cluster": "west-road",
      "coord": [0, 3, 0],
      "labels": ["west-road", "future-link", "outer-route"],
      "exits": [
        { "direction": "south", "to": 19303 },
        { "direction": "west", "to": 19401, "external": true }
      ],
      "enquires": ["西關", "夷陵", "遠路"]
    }
  ]
}
```
