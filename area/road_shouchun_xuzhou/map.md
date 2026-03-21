# 淮東官道 (`road_shouchun_xuzhou`)

## Area Intent

`road_shouchun_xuzhou` 承接 `city_xuzhou` 南門驛口，把玩家從州城秩序與驛舍時刻正式送上南下壽春的淮東官道。這裡不是普通平路，而是一段帶著路亭、換馬、分岔與旅貨消息的交通帶，負責把 `徐州 -> 壽春` 的 world link 落成真正可經過的旅程。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `淮東官道 / 驛路轉場`
- LevelRange: `20-32`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_shouchun_xuzhou",
    "title": "淮東官道",
    "design_notes": "第一版 spec-first 草案。先固定北口驛道、路亭中段、換馬歇腳點與南下官道，把徐州州城正式接向壽春方向。",
    "level_range": "20-32",
    "planned_vnum_range": "16901-16920",
    "reserved_room_block": "16901-16920",
    "theme": {
      "primary": "歷史城市",
      "secondary": "淮東官道 / 驛路轉場"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 16901,
        "target_area": "city_xuzhou",
        "label": "徐州南門"
      },
      {
        "direction": "south",
        "source_vnum": 16908,
        "target_area": "city_shouchun",
        "label": "壽春官道"
      }
    ],
    "clusters": [
      { "id": "north-approach", "label": "北口驛道" },
      { "id": "midway-road", "label": "官道中段" },
      { "id": "rest-stop", "label": "路亭歇腳點" },
      { "id": "south-fork", "label": "南下岔路" }
    ]
  },
  "rooms": [
    {
      "vnum": 16901,
      "name": "徐州南口驛道",
      "description": "一離開徐州南門，城牆後方的喧聲很快就被官道上的車轍與風聲取代。這裡仍看得見驛卒、換馬人與最後回頭看州城的旅客，像是在提醒你真正的南路現在才剛開始。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 0, 0],
      "labels": ["north-edge", "world-link-north", "entry"],
      "exits": [
        { "direction": "south", "to": 16902 }
      ],
      "enquires": ["徐州", "回城", "南路"]
    },
    {
      "vnum": 16902,
      "name": "官道木樁旁",
      "description": "官道旁立著一排磨舊的木樁，上頭留著無數繩結與馬索痕跡。這裡不像正式驛站那樣忙，卻總有人在此停一下，把水囊繫緊、把貨繩重打，然後才真正踏上較長的一段南下路。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 1, 0],
      "labels": ["road", "waypoint"],
      "exits": [
        { "direction": "north", "to": 16901 },
        { "direction": "south", "to": 16903 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁被繩索磨得光亮，看得出這段路多年來一直都是車馬南北往返的固定歇手點。"
        }
      ],
      "enquires": ["木樁", "車馬"]
    },
    {
      "vnum": 16903,
      "name": "淮東官道中段",
      "description": "這段官道筆直開闊，兩旁田色與低樹把視線拉得很長。走在這裡時，你會清楚感受到自己已不在州城之內，卻也還沒真正進入下一座城，只能靠路感、天色與偶爾經過的旅隊判斷節奏。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "open-way"],
      "exits": [
        { "direction": "north", "to": 16902 },
        { "direction": "south", "to": 16905 },
        { "direction": "east", "to": 16904 }
      ],
      "enquires": ["官道", "壽春", "下一站"]
    },
    {
      "vnum": 16904,
      "name": "里程石旁",
      "description": "一座半人高的里程石立在道旁，石面上的刻字經風雨磨蝕後依然還能辨出徐州與壽春的字樣。對趕路的人來說，這種石頭不只是記里數，更像在替長路留下能抓住方向感的證據。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["marker", "route-info"],
      "exits": [
        { "direction": "west", "to": 16903 }
      ],
      "enquires": ["里程石", "距離"]
    },
    {
      "vnum": 16905,
      "name": "路亭前坪",
      "description": "官道在這裡稍稍放寬，讓車馬與步客都能在路亭前歇一口氣。棚下總有人談論南邊糧價、壽春消息，或猜測下一批從州城趕下來的差人究竟帶著什麼急文。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "north", "to": 16903 },
        { "direction": "enter", "to": 16906 },
        { "direction": "south", "to": 16907 }
      ],
      "enquires": ["路亭", "歇腳", "消息"]
    },
    {
      "vnum": 16906,
      "name": "路亭內",
      "description": "路亭裡擺著長凳、茶桶與幾只被磨得發亮的木碗，牆上還釘著供旅人記路的簡單木牌。這裡給人的安全感很薄，卻也正因如此，任何一句打聽到的消息都顯得格外實用。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 16905 }
      ],
      "enquires": ["木牌", "茶水"]
    },
    {
      "vnum": 16907,
      "name": "換馬坡口",
      "description": "坡口旁留著一片被馬蹄踩得結實的土面，顯示很多長途差人與鏢客都會在此做最後一次整理。再往南，路勢就會更加明顯地把人送向壽春，不再像前半段那樣還能回頭望見州城餘影。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "south-fork",
      "coord": [0, 4, 0],
      "labels": ["staging", "southbound"],
      "exits": [
        { "direction": "north", "to": 16905 },
        { "direction": "south", "to": 16908 }
      ],
      "enquires": ["換馬", "壽春", "坡口"]
    },
    {
      "vnum": 16908,
      "name": "南下官道口",
      "description": "官道在此繼續往南舒展，路面上的車痕比北段更深，像整條路都在催促旅人不要在這裡停太久。站在這裡時，徐州已經成了背後的支點，而壽春則成了真正正在逼近的下一站。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "south-fork",
      "coord": [0, 5, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 16907 }
      ],
      "enquires": ["南邊", "壽春", "去路"]
    }
  ]
}
```
