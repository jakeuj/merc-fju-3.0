# 樊城 (`fort_fancheng`)

## Area Intent

`fort_fancheng` 承接 `city_xiangyang` 北向大道，把原本還停在路標、想像與問路線索裡的北岸城防，正式落成一座真正會收束人流、盤查去路、分配軍令與穩住北路節奏的軍事關隘。這裡不是襄陽那種能讓人先補給、先打聽再慢慢決定去向的主城，而是一個一踏進去就會明顯感到自己正站在守備壓力、軍令層級與邊界秩序中的地方。

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `北岸城防 / 軍令關門`
- LevelRange: `38-52`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "fort_fancheng",
    "title": "樊城",
    "design_notes": "第一版 spec-first 草案。先固定南關坡口、前柵、北岸關門、甕城軍道、披甲校場、糧甲棚區、旗樓望臺與北堤望口，讓襄陽北側的軍事 choke point 正式落地。",
    "level_range": "38-52",
    "planned_vnum_range": "20101-20120",
    "reserved_room_block": "20101-20120",
    "theme": {
      "primary": "軍旅",
      "secondary": "北岸城防 / 軍令關門"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 20101,
        "target_area": "city_xiangyang",
        "target_room_vnum": 14208,
        "label": "襄陽北大道"
      }
    ],
    "clusters": [
      { "id": "approach", "label": "南關前帶" },
      { "id": "gate", "label": "關門與甕城" },
      { "id": "camp", "label": "校場與糧甲棚" },
      { "id": "watch", "label": "旗樓與北堤望口" }
    ]
  },
  "rooms": [
    {
      "vnum": 20101,
      "name": "南關坡口",
      "description": "自襄陽北向大道一路走到這裡後，原本屬於城市內部的寬整節奏會立刻被收成更硬、更直的軍事秩序。坡口上的木柵、土牆與輪值兵視線一起把人流壓成一條不容猶疑的前帶，讓人很清楚知道自己已從主城邊界踏進真正的北岸城防。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "south-edge", "world-link-south"],
      "exits": [
        { "direction": "south", "to": 14208, "external": true },
        { "direction": "north", "to": 20102 }
      ],
      "enquires": ["襄陽", "南路", "關前"]
    },
    {
      "vnum": 20102,
      "name": "樊城前柵",
      "description": "前柵把來者的步伐自然壓慢，兩側削尖木樁與掛旗交替排列，讓這段短路本身就像一種篩選。它不像真正交鋒中的戰地那樣混亂，卻比襄陽任何一條街都更能讓人立刻感覺到自己正接受關防的判定。",
      "sector_type": "SECT_CITY",
      "cluster": "approach",
      "coord": [0, 1, 0],
      "labels": ["checkpoint", "approach"],
      "exits": [
        { "direction": "south", "to": 20101 },
        { "direction": "north", "to": 20103 },
        { "direction": "east", "to": 20105 }
      ],
      "enquires": ["盤查", "守兵", "軍旗"]
    },
    {
      "vnum": 20103,
      "name": "北岸關門",
      "description": "厚重關門把內外空氣切得十分明白，門外仍帶著襄陽往來的煙塵與人聲，門內卻只剩更偏軍務、傳令與備戰的冷硬節拍。站在這裡時，很難再把樊城看成普通城鎮，它更像是專門用來判定誰應該被放進北路的門檻。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [0, 2, 0],
      "labels": ["gate", "threshold"],
      "exits": [
        { "direction": "south", "to": 20102 },
        { "direction": "north", "to": 20104 }
      ],
      "enquires": ["關門", "放行", "軍令"]
    },
    {
      "vnum": 20104,
      "name": "甕城軍道",
      "description": "甕城把關防壓力再收得更緊，短短一段軍道上卻同時能看見校場、糧甲棚與旗樓視線交錯。比起單純防禦，它更像一個把北上與南回動線先壓縮、再重新分配的軍事節點，整座樊城的節奏幾乎都由這裡重新點發。",
      "sector_type": "SECT_CITY",
      "cluster": "gate",
      "coord": [0, 3, 0],
      "labels": ["core", "military-flow"],
      "exits": [
        { "direction": "south", "to": 20103 },
        { "direction": "north", "to": 20108 },
        { "direction": "east", "to": 20106 },
        { "direction": "up", "to": 20107 }
      ],
      "enquires": ["甕城", "校場", "旗樓"]
    },
    {
      "vnum": 20105,
      "name": "披甲校場",
      "description": "校場上的甲片碰撞聲不大，卻始終不斷，像整座樊城關防在這裡以最直接的方式維持體溫。和襄陽的街市相比，這裡沒有多少可供停步的煙火氣，只有訓練、整隊與隨時準備北出的壓力。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [1, 1, 0],
      "labels": ["drill-yard", "discipline"],
      "exits": [
        { "direction": "west", "to": 20102 }
      ],
      "enquires": ["校場", "操演", "整隊"]
    },
    {
      "vnum": 20106,
      "name": "糧甲棚區",
      "description": "糧袋、甲片、燈油與補釘繩整整齊齊地分成數排，連空氣都像帶著倉儲與皮革混合的乾硬氣味。若說關門是樊城的臉，那麼這裡就是它真正的筋骨，因為整個北岸守備能否持久，多半就靠這些看似不起眼的供給撐著。",
      "sector_type": "SECT_CITY",
      "cluster": "camp",
      "coord": [1, 3, 0],
      "labels": ["supply", "service"],
      "exits": [
        { "direction": "west", "to": 20104 }
      ],
      "enquires": ["軍需", "糧草", "燈油"]
    },
    {
      "vnum": 20107,
      "name": "旗樓望臺",
      "description": "望臺上不只看得見南面來路，也能把甕城、校場與棚區的節奏一口氣收進眼底。木案上的旗號記錄與換班名冊讓這裡比下方任何地方都更冷，也更像真正決定樊城心跳速度的高點。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, 3, 1],
      "labels": ["watchtower", "orders", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 20104 }
      ],
      "enquires": ["旗樓", "望臺", "旗號"]
    },
    {
      "vnum": 20108,
      "name": "北堤望口",
      "description": "再往北走，視野會忽然拉得很長，連風裡的氣味都變得更冷更薄。北堤望口不像真正出關那樣把人直接送出去，卻已足夠讓人感到北路壓力就在前方，樊城在這裡不只是守門，也是在替整條荊州北界把節奏先收緊一層。",
      "sector_type": "SECT_CITY",
      "cluster": "watch",
      "coord": [0, 4, 0],
      "labels": ["north-front", "forward"],
      "exits": [
        { "direction": "south", "to": 20104 }
      ],
      "enquires": ["北邊", "北路", "前線"]
    }
  ]
}
```
