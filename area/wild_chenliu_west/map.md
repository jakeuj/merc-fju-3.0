# 陳留西郊 (`wild_chenliu_west`)

## Area Intent

`wild_chenliu_west` 承接 `city_chenliu` 的西城門外牌樓，把剛在城內被主街、師父、衙門與驛站重新收束起來的中原秩序，慢慢鬆開成茶亭、田埂、柳溝與流民營灰地交錯的城郊外帶。它不是立刻通往洛陽的整段長路，也不是單純給城門掛一個背景，而是一段讓玩家清楚感到「陳留的城牆還看得見，但灰色人流與郊邊耳語已經接手」的西郊母帶。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `西郊 / 茶亭`
- LevelRange: `14-24`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_chenliu_west",
    "title": "陳留西郊",
    "design_notes": "第一版 spec-first 草案。先固定西門郊道口、茶亭前坪、柳溝田埂、風碑岔地、樹叢側路與更西荒道，讓陳留西側正式展開成可載入的近郊 wild 骨架。",
    "level_range": "14-24",
    "planned_vnum_range": "20801-20820",
    "reserved_room_block": "20801-20820",
    "theme": {
      "primary": "江湖",
      "secondary": "西郊 / 茶亭"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 20801,
        "target_area": "city_chenliu",
        "target_room_vnum": 13801,
        "label": "西城門外牌樓"
      },
      {
        "direction": "west",
        "source_vnum": 20808,
        "target_area": "road_chenliu",
        "target_room_vnum": 20901,
        "label": "往陳留驛路"
      }
    ],
    "clusters": [
      { "id": "return-gate", "label": "回城外口" },
      { "id": "road-line", "label": "西郊官道" },
      { "id": "tea-stop", "label": "茶亭與田埂" },
      { "id": "wild-fringe", "label": "柳溝與灰地" },
      { "id": "west-track", "label": "更西荒道" }
    ]
  },
  "rooms": [
    {
      "vnum": 20801,
      "name": "西門郊道口",
      "description": "一離開陳留西城門外牌樓，腳下的整齊石地很快就鬆成帶著車痕與土灰的郊道口。回頭還能清楚看見城牆與門匾，往前卻已經只剩茶亭、田埂與路旁林影，像是陳留正把所有真正要上路的人慢慢交給西郊。",
      "sector_type": "SECT_FIELD",
      "cluster": "return-gate",
      "coord": [0, 0, 0],
      "labels": ["entry", "return-link", "city-edge"],
      "exits": [
        { "direction": "east", "to": 13801, "external": true },
        { "direction": "west", "to": 20802 },
        { "direction": "south", "to": 20803 }
      ],
      "enquires": ["回城", "城門", "郊道"]
    },
    {
      "vnum": 20802,
      "name": "陳西官道",
      "description": "官道在城外還保留著幾分被反覆踩實的硬度，卻已經沒有城門內那種處處被人看著的緊。商旅、差役與不太願意報姓名的路人都在這裡重新混成一股鬆散卻仍有方向的西郊節奏。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-1, 0, 0],
      "labels": ["main-road", "westward"],
      "exits": [
        { "direction": "east", "to": 20801 },
        { "direction": "west", "to": 20804 },
        { "direction": "south", "to": 20805 }
      ],
      "keywords": [
        {
          "keyword": "路碑",
          "description": "這塊路碑只簡單刻著回城與更西方向，字跡不算工整，卻明顯是留給真正要在外頭辨路的人看。"
        }
      ],
      "enquires": ["官道", "茶亭", "更西"]
    },
    {
      "vnum": 20803,
      "name": "茶亭前坪",
      "description": "一塊不大的前坪勉強容得下幾張長凳與卸貨包袱，對真正要上路的人來說，這裡的價值往往在熱水、閒話與別人不小心漏出的去向。比起城內整齊的食肆補給，這裡更像一種勉強卻可靠的城外人情。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [0, -1, 0],
      "labels": ["tea-stop", "rest", "service"],
      "exits": [
        { "direction": "north", "to": 20801 },
        { "direction": "west", "to": 20805 }
      ],
      "keywords": [
        {
          "keyword": "茶亭",
          "description": "這座茶亭只靠幾根老木柱與斜歪的棚布撐著，卻很穩地替西郊上的人留下一小塊能坐、能問、也能喘口氣的地方。"
        }
      ],
      "enquires": ["茶亭", "歇腳", "消息"]
    },
    {
      "vnum": 20804,
      "name": "風碑岔地",
      "description": "風碑邊的土路向西與向南慢慢分開，連車轍深淺都在提醒人這裡開始不再只有一條最正經的去路。站在這裡時，陳留還沒有遠到看不見，卻已經夠遠得讓灰色腳步與耳語有地方分流。",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [-2, 0, 0],
      "labels": ["marker", "fork", "road-choice"],
      "exits": [
        { "direction": "east", "to": 20802 },
        { "direction": "west", "to": 20808 },
        { "direction": "south", "to": 20806 }
      ],
      "enquires": ["風碑", "岔路", "去向"]
    },
    {
      "vnum": 20805,
      "name": "柳溝田埂",
      "description": "田埂沿著一條細窄柳溝往前拖去，泥氣、草味與牲口踏出的痕跡把官道邊緣洗得很有活路感。這裡沒有城內那種被整理好的邊界，只剩誰常走、誰想避人耳目，全慢慢留在土色與草影裡。",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-stop",
      "coord": [-1, -1, 0],
      "labels": ["farmland", "side-road", "canal-edge"],
      "exits": [
        { "direction": "north", "to": 20802 },
        { "direction": "east", "to": 20803 },
        { "direction": "west", "to": 20806 }
      ],
      "enquires": ["田埂", "柳溝", "巡邏"]
    },
    {
      "vnum": 20806,
      "name": "樹叢側路",
      "description": "樹叢貼著側路慢慢密起來，只要視線一離開土路，很快就會被低枝與陰影切斷。它還不算真正的深林，卻已經夠讓流民、藏貨，或者不想回應盤查的人，借著樹影躲上一陣子。",
      "sector_type": "SECT_FOREST",
      "cluster": "wild-fringe",
      "coord": [-2, -1, 0],
      "labels": ["forest-edge", "shade", "risk"],
      "exits": [
        { "direction": "north", "to": 20804 },
        { "direction": "east", "to": 20805 },
        { "direction": "south", "to": 20807 }
      ],
      "keywords": [
        {
          "keyword": "樹叢",
          "description": "幾叢低矮灌木被踩出不太乾淨的窄痕，像有人常在這裡停下來等官道上的腳步聲走遠。"
        }
      ],
      "enquires": ["樹叢", "流民", "腳步"]
    },
    {
      "vnum": 20807,
      "name": "流民營灰地",
      "description": "地上只剩一圈燒得不怎麼完整的火痕、破布與幾根折木，既像流民夜裡歇腳的痕跡，也像某些不願讓城門差役記住名字的人暫時留下的影子。這裡讓陳留西郊第一次真正露出秩序之外的灰色。",
      "sector_type": "SECT_FIELD",
      "cluster": "wild-fringe",
      "coord": [-2, -2, 0],
      "labels": ["campfire", "drifter", "gray-zone"],
      "exits": [
        { "direction": "north", "to": 20806 }
      ],
      "enquires": ["流民", "營火", "夜路"]
    },
    {
      "vnum": 20808,
      "name": "更西荒道",
      "description": "再往西去，陳留留下的牆影與牌樓都開始淡成一種只夠回頭辨位的背景，只剩荒道本身還替人勉強維持方向感。如今更前頭已隱約看得見被車轍壓實的驛路開口與棚燈痕影，顯示這裡不再只是抽象的遠路，而是真正開始把旅人交還給更長、更穩，也更講路規的中原驛道。",
      "sector_type": "SECT_FIELD",
      "cluster": "west-track",
      "coord": [-3, 0, 0],
      "labels": ["west-edge", "road-connection", "departure"],
      "exits": [
        { "direction": "east", "to": 20804 },
        { "direction": "west", "to": 20901, "external": true }
      ],
      "enquires": ["更西", "遠路", "荒道", "驛路"]
    }
  ]
}
```
