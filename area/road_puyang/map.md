# 往濮陽官道 (`road_puyang`)

## Area Intent

`road_puyang` 承接 `city_puyang` 南驛牌口，把前沿城氣慢慢拉回中原官道的長路節奏。這裡不追求複雜戰地，而是讓玩家感受到從濮陽離城後，消息、旅貨與差役沿著一條真正可辨認的北行大道反覆往返，逐步把前線壓力送回後方。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `官道 / 北行`
- LevelRange: `8-18`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_puyang",
    "title": "往濮陽官道",
    "design_notes": "第一版 spec-first 草案。先固定洛陽北出驛口、官道中段、路亭歇腳點與濮陽南驛前帶，把中原北行長路正式接成可實作的 road 節點。",
    "level_range": "8-18",
    "planned_vnum_range": "17301-17320",
    "reserved_room_block": "17301-17320",
    "theme": {
      "primary": "軍旅",
      "secondary": "官道 / 北行"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 17301,
        "target_area": "city_loyang",
        "label": "洛陽北門"
      },
      {
        "direction": "north",
        "source_vnum": 17308,
        "target_area": "city_puyang",
        "label": "濮陽南驛"
      }
    ],
    "clusters": [
      { "id": "south-approach", "label": "洛陽北出口" },
      { "id": "midway-road", "label": "官道中段" },
      { "id": "rest-stop", "label": "路亭與盤查點" },
      { "id": "north-approach", "label": "濮陽南驛前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 17301,
      "name": "洛陽北郊驛口",
      "description": "一離開洛陽北門，城內的喧鬧就被官道上的風聲和車轍聲慢慢沖淡。這裡仍看得見最後整理行裝的旅人與準備北上的差役，像所有真正要往濮陽去的人，都會先在這裡把城內節奏換成長路節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 508, "external": true },
        { "direction": "north", "to": 17302 }
      ],
      "enquires": ["洛陽", "北路", "出城"]
    },
    {
      "vnum": 17302,
      "name": "官道木樁邊",
      "description": "路邊一排木樁被纜繩與馬索磨得發亮，顯示這裡長年都是人馬整裝的固定停手點。再往北，路感會愈來愈強，讓人很難再把自己當成仍在城門附近徘徊。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 1, 0],
      "labels": ["waypoint", "roadside"],
      "exits": [
        { "direction": "south", "to": 17301 },
        { "direction": "north", "to": 17303 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁上的新舊繩痕纏在一起，看得出這條官道多年來一直都承擔著穩定的南北旅運。"
        }
      ],
      "enquires": ["木樁", "旅隊"]
    },
    {
      "vnum": 17303,
      "name": "北行大道中段",
      "description": "官道在這裡筆直舒展，路面上層層疊疊的車痕把方向感拉得非常明白。你很容易在這段路上意識到，自己已經離洛陽有一小段距離，卻還遠沒進入濮陽的前沿氣氛。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [0, 2, 0],
      "labels": ["main-road", "open-way"],
      "exits": [
        { "direction": "south", "to": 17302 },
        { "direction": "north", "to": 17305 },
        { "direction": "east", "to": 17304 }
      ],
      "enquires": ["官道", "濮陽", "去路"]
    },
    {
      "vnum": 17304,
      "name": "路牌石旁",
      "description": "一座低矮的路牌石立在道旁，表面被風雨磨蝕後仍能辨出洛陽與濮陽的方向字樣。對長途旅人來說，這種石頭不只是記路，更像替整條官道留住不會走失的秩序。",
      "sector_type": "SECT_FIELD",
      "cluster": "midway-road",
      "coord": [1, 2, 0],
      "labels": ["marker", "route-info"],
      "exits": [
        { "direction": "west", "to": 17303 }
      ],
      "enquires": ["路牌", "方向"]
    },
    {
      "vnum": 17305,
      "name": "路亭前坪",
      "description": "官道在此稍微放寬，形成讓車馬與步客都能歇上一口氣的前坪。有人在這裡換水囊、有人低聲打聽北邊傳來的消息，讓整個地方像一個把前後兩座城短暫接在一起的縫口。",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [0, 3, 0],
      "labels": ["rest-stop", "rumor"],
      "exits": [
        { "direction": "south", "to": 17303 },
        { "direction": "enter", "to": 17306 },
        { "direction": "north", "to": 17307 }
      ],
      "enquires": ["路亭", "歇腳", "消息"]
    },
    {
      "vnum": 17306,
      "name": "路亭內",
      "description": "亭內擺著長凳、粗茶桶與幾只磨得發亮的木碗，牆邊還掛著簡單的驛訊木牌。這裡給人的不是安逸，而是一種只夠休一口氣、再把腳步重新放回路上的短暫安穩。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [0, 3, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 17305 }
      ],
      "enquires": ["木牌", "茶水"]
    },
    {
      "vnum": 17307,
      "name": "盤查坡口",
      "description": "坡口旁的地面被人馬踩得相當結實，顯示這裡常有驛卒與巡差暫停盤問來往過客。再往北，濮陽的前沿空氣會越來越明顯，因此不少人都會在這裡最後整理衣裝與說詞。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 4, 0],
      "labels": ["checkpoint", "northbound"],
      "exits": [
        { "direction": "south", "to": 17305 },
        { "direction": "north", "to": 17308 }
      ],
      "enquires": ["盤查", "差役", "濮陽"]
    },
    {
      "vnum": 17308,
      "name": "濮陽南驛道口",
      "description": "官道在此繼續往北伸去，路面上的車痕與兵履印記都明顯重了起來，像是在提醒你濮陽已經不只是普通城鎮，而是前線壓力會真正落地的地方。站在這裡時，中原長路與河北前沿之間只剩最後一步。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-approach",
      "coord": [0, 5, 0],
      "labels": ["north-edge", "world-link-north"],
      "exits": [
        { "direction": "south", "to": 17307 },
        { "direction": "north", "to": 17207, "external": true }
      ],
      "enquires": ["濮陽", "南驛", "前線"]
    }
  ]
}
```
