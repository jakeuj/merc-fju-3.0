# 往宛官道 (`road_wan`)

## Area Intent

`road_wan` 承接 `loyang` 的津陽門，把玩家從帝都城門的秩序與傳聞正式送上往宛的南行官道。這裡不是另一段單純的地表通路，而是一條會讓人從木樁、里程石、路亭與盤查坡口裡感到「離開洛陽、還沒進宛」的真正旅程，負責把 `洛陽 -> 宛` 的 world link 落成可經過、可停下、也可打聽去路的 road 節點。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `官道 / 南行`
- LevelRange: `8-18`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_wan",
    "title": "往宛官道",
    "design_notes": "第一版 spec-first 草案。先固定津陽門南驛口、南行官道中段、路亭歇腳點與宛北官道路口，把洛陽往宛的長路正式接成可實作的 road 節點。",
    "level_range": "8-18",
    "planned_vnum_range": "20501-20520",
    "reserved_room_block": "20501-20520",
    "theme": {
      "primary": "江湖",
      "secondary": "官道 / 南行"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 20501,
        "target_area": "loyang",
        "target_room_vnum": 593,
        "label": "津陽門"
      },
      {
        "direction": "south",
        "source_vnum": 20508,
        "target_area": "city_wan",
        "target_room_vnum": 20407,
        "label": "宛北門官道口"
      }
    ],
    "clusters": [
      { "id": "north-approach", "label": "津陽門南驛口" },
      { "id": "midway-road", "label": "南行官道中段" },
      { "id": "rest-stop", "label": "路亭歇腳點" },
      { "id": "south-approach", "label": "宛北官道路口" }
    ]
  },
  "rooms": [
    {
      "vnum": 20501,
      "name": "津陽門南驛口",
      "description": "一離開津陽門，洛陽城內那股壓得分明的帝都秩序就被官道上的風聲與車轍聲慢慢拉散。這裡仍看得見最後整理衣裝的旅人與準備南下的差役，像所有真正要往宛去的人，都會先在這裡把城內節奏換成長路節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "north-edge", "world-link-north"],
      "exits": [
        { "direction": "north", "to": 593, "external": true },
        { "direction": "south", "to": 20502 }
      ],
      "enquires": ["洛陽", "津陽門", "南路"]
    },
    {
      "vnum": 20502,
      "name": "官道木樁旁",
      "description": "路旁一排木樁被纜繩與馬索磨得發亮，顯示這裡長年都是人馬整裝的固定停手點。再往南，路感會愈來愈強，讓人很難再把自己當成仍在洛陽城門附近徘徊。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 1, 0],
      "labels": ["roadside", "waypoint"],
      "exits": [
        { "direction": "north", "to": 20501 },
        { "direction": "south", "to": 20503 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁上的新舊繩痕一層層纏在一起，看得出這條官道多年來一直穩穩承擔著往宛的南北旅運。"
        }
      ],
      "enquires": ["木樁", "旅隊"]
    },
    {
      "vnum": 20503,
      "name": "南行官道中段",
      "description": "官道在這裡筆直舒展，兩側田色與低樹把視線拉得很長。走在這裡時，你會很清楚自己已經離開洛陽，卻還沒真正進入宛的城門秩序，只能靠路感、天色與偶爾經過的旅隊判斷節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "open-way"],
      "exits": [
        { "direction": "north", "to": 20502 },
        { "direction": "south", "to": 20505 },
        { "direction": "east", "to": 20504 }
      ],
      "enquires": ["官道", "宛", "去路"]
    },
    {
      "vnum": 20504,
      "name": "里程石側線",
      "description": "一座低矮的里程石立在道旁，石面經風雨磨蝕後仍還能辨出洛陽與宛的方向字樣。對真正趕遠路的人來說，這種石頭不只是記路，更像替整條官道留下不會走失的秩序。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["marker", "route-info"],
      "exits": [
        { "direction": "west", "to": 20503 }
      ],
      "enquires": ["里程石", "距離"]
    },
    {
      "vnum": 20505,
      "name": "路亭前坪",
      "description": "官道在此稍微放寬，形成讓車馬與步客都能歇上一口氣的前坪。有人在這裡換水囊、有人低聲打聽南邊宛城的消息，讓整個地方像一個把帝都與內陸轉接城短暫縫在一起的停手點。",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "north", "to": 20503 },
        { "direction": "enter", "to": 20506 },
        { "direction": "south", "to": 20507 }
      ],
      "enquires": ["路亭", "歇腳", "消息"]
    },
    {
      "vnum": 20506,
      "name": "路亭內",
      "description": "亭內擺著長凳、粗茶桶與幾只磨得發亮的木碗，牆邊還掛著替旅人記路的簡單木牌。這裡給人的不是安逸，而是一種只夠休一口氣、再把腳步重新放回南行長路上的短暫安穩。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 20505 }
      ],
      "enquires": ["木牌", "茶水"]
    },
    {
      "vnum": 20507,
      "name": "盤查坡口",
      "description": "坡口旁的地面被人馬踩得相當結實，顯示這裡常有驛卒與巡差暫停盤問來往過客。再往南，宛的官道節奏會愈來愈明顯，因此不少人都會在這裡最後整理行囊與說詞。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 4, 0],
      "labels": ["checkpoint", "southbound"],
      "exits": [
        { "direction": "north", "to": 20505 },
        { "direction": "south", "to": 20508 }
      ],
      "enquires": ["盤查", "差役", "宛"]
    },
    {
      "vnum": 20508,
      "name": "宛北官道路口",
      "description": "官道在此繼續往南收進宛城北門的城廓與里程石影裡，路面上的車痕與人聲也明顯比前段更密。站在這裡時，洛陽已成了背後那座遙遠卻仍在發力的帝都，而宛則成了真正正在逼近的下一站。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 5, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 20507 },
        { "direction": "south", "to": 20407, "external": true }
      ],
      "enquires": ["宛", "北門", "去路"]
    }
  ]
}
```
