# 建業西郊 (`wild_jianye_west`)

## Area Intent

`wild_jianye_west` 承接 `city_jianye` 西向城郊出口，把玩家從都城主街與港區服務節奏，切回一段帶水氣、帶農圩和茶亭過路感的江東城郊外帶。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `郊野 / 水鄉`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_jianye_west",
    "title": "建業西郊",
    "design_notes": "第一版 spec-first 草案。先固定回城路口、官道主線、水圳茶亭、蘆岸支徑與更西村路，讓建業主城正式向西展開成可探索的城郊外帶。",
    "level_range": "100-100",
    "planned_vnum_range": "16201-16230",
    "reserved_room_block": "16201-16230",
    "theme": {
      "primary": "江湖",
      "secondary": "郊野 / 水鄉"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 16201,
        "target_area": "city_jianye",
        "label": "建業西門"
      },
      {
        "direction": "south",
        "source_vnum": 16210,
        "target_area": "wild_mountain_pass",
        "label": "會稽山道"
      },
      {
        "direction": "west",
        "source_vnum": 16208,
        "target_area": "river_villages",
        "label": "水鄉村路"
      }
    ],
    "clusters": [
      { "id": "gate-return", "label": "回城口" },
      { "id": "road-line", "label": "官道主線" },
      { "id": "tea-rest", "label": "茶亭水圳" },
      { "id": "reed-bank", "label": "蘆岸支徑" },
      { "id": "west-fork", "label": "更西村路" }
    ]
  },
  "rooms": [
    {
      "vnum": 16201,
      "name": "西門回道",
      "description": "離開建業西門後，最先迎上來的是官道邊帶水氣的風和比城內鬆得多的腳步節奏。這裡仍貼著都城，但已經能明顯感到人聲和規矩都開始往郊外稀釋開去。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "gate-return",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-link"],
      "exits": [
        { "direction": "east", "to": 16009, "external": true },
        { "direction": "west", "to": 16203 },
        { "direction": "south", "to": 16202 }
      ],
      "enquires": ["回城", "西門", "官道"]
    },
    {
      "vnum": 16202,
      "name": "水圳旁徑",
      "description": "一道貼著水圳的旁徑往南繞開主道，路面雖窄，卻顯然常有人拿來避開車流與城門口的眼睛。這種看似不起眼的小路，往往才最能說明城郊真正的生活方式。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "gate-return",
      "coord": [0, -1, 0],
      "labels": ["waterway", "side-path"],
      "exits": [
        { "direction": "north", "to": 16201 }
      ],
      "enquires": ["水圳", "小路"]
    },
    {
      "vnum": 16203,
      "name": "西郊官道",
      "description": "官道往西平平伸開，路旁既有田圩也有行人，像都城的力量還沒完全退去，卻也已經開始讓位給真正屬於郊野的節奏。走在這裡時，很容易感受到建業其實是被這些外帶一圈圈托住的。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "road-line",
      "coord": [1, 0, 0],
      "labels": ["main-road", "westward"],
      "exits": [
        { "direction": "east", "to": 16201 },
        { "direction": "west", "to": 16204 },
        { "direction": "south", "to": 16205 }
      ],
      "enquires": ["官道", "西邊", "茶亭"]
    },
    {
      "vnum": 16204,
      "name": "路碑岔口",
      "description": "岔口邊立著被風雨磨鈍字跡的路碑，一邊指回建業，一邊則指向更遠的鄉里與山道。這裡不像真正的終點，卻已經很清楚地把城內和城外分成兩種不同的生活。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fork",
      "coord": [2, 0, 0],
      "labels": ["marker", "fork"],
      "exits": [
        { "direction": "east", "to": 16203 },
        { "direction": "west", "to": 16208 },
        { "direction": "south", "to": 16206 }
      ],
      "enquires": ["路碑", "岔口", "村路"]
    },
    {
      "vnum": 16205,
      "name": "茶亭前坪",
      "description": "茶亭前的空坪不算大，卻總有一點歇腳、換氣和交換消息的意思。和城裡那些被制度撐起的秩序相比，這裡的平靜更像人與路長久磨出來的默契。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-rest",
      "coord": [1, -1, 0],
      "labels": ["tea-house", "rest"],
      "exits": [
        { "direction": "north", "to": 16203 },
        { "direction": "east", "to": 16207 }
      ],
      "enquires": ["茶亭", "歇腳", "消息"]
    },
    {
      "vnum": 16206,
      "name": "蘆岸小堤",
      "description": "小堤沿著蘆岸往南壓低，走起來比官道安靜得多，只有水聲和草葉摩擦提醒你這裡已經很接近更鬆散也更真實的鄉野生活。若要離開建業的目光，這裡顯然是個好方向。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-bank",
      "coord": [2, -1, 0],
      "labels": ["reed", "bank"],
      "exits": [
        { "direction": "north", "to": 16204 },
        { "direction": "west", "to": 16207 },
        { "direction": "south", "to": 16210 }
      ],
      "enquires": ["蘆岸", "南邊", "小堤"]
    },
    {
      "vnum": 16207,
      "name": "圩田側路",
      "description": "側路在圩田間收得很窄，卻有一種比大路更貼近水鄉地氣的穩定。這裡不適合大張旗鼓地趕路，卻很適合真正想看清一座城外帶是怎麼活著的人慢慢走。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "tea-rest",
      "coord": [2, -1, 0],
      "labels": ["fields", "side-lane"],
      "exits": [
        { "direction": "west", "to": 16205 },
        { "direction": "east", "to": 16206 }
      ],
      "enquires": ["圩田", "側路"]
    },
    {
      "vnum": 16208,
      "name": "更西村路",
      "description": "再往西去，建業留下的痕跡便越來越薄，只剩官道習慣還在勉強維持方向感。這裡很明顯已經是城郊真正準備把旅人交出去的地方。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "west-fork",
      "coord": [3, 0, 0],
      "labels": ["west-link", "villages"],
      "exits": [
        { "direction": "east", "to": 16204 }
      ],
      "enquires": ["村路", "更西", "離城"]
    },
    {
      "vnum": 16210,
      "name": "南去坡口",
      "description": "坡口邊的土路明顯更朝山勢和遠行方向傾去，像只要再往前，水鄉的柔和就會慢慢被山道的逼仄和高低起伏接手。這裡不像危險本身，卻像所有真正離城旅程的開始。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "reed-bank",
      "coord": [2, -2, 0],
      "labels": ["south-link", "mountain-road"],
      "exits": [
        { "direction": "north", "to": 16206 }
      ],
      "enquires": ["南邊", "山道", "遠路"]
    }
  ]
}
```
