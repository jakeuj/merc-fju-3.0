# Sample Map Spec

```mapmd-json
{
  "area": {
    "name": "sample_area",
    "title": "樣板區",
    "serial": 42,
    "design_notes": "示範 graph metadata 會被 parser 接受，但不會輸出到 .roo"
  },
  "rooms": [
    {
      "vnum": 9101,
      "name": "測試入口",
      "description": "這裡是測試區的入口。",
      "sector_type": "SECT_CITY",
      "flags": ["Safe", "NoFight"],
      "coord": [0, 0, 0],
      "cluster": "entry-ring",
      "labels": ["入口", "問路點"],
      "exits": [
        { "direction": "north", "to": 9102 },
        {
          "direction": "enter",
          "to": 9150,
          "exit_keyword": "gate",
          "exit_desc": "一道厚重的木門。",
          "flags": ["IsDoor", "Closed"]
        }
      ],
      "keywords": [
        {
          "keyword": "sign",
          "description": "牌子上寫著：往北前進可進入訓練區。"
        }
      ],
      "enquires": [
        { "keyword": "入口" },
        { "keyword": "測試區" }
      ]
    },
    {
      "vnum": 9102,
      "name": "北側通道",
      "description": "這裡是北側通道。",
      "sector_type": "SECT_CITY",
      "coord": [0, 1, 0],
      "cluster": "entry-ring",
      "exits": [
        { "direction": "south", "to": 9101 },
        { "direction": "north", "to": 9103 }
      ]
    },
    {
      "vnum": 9103,
      "name": "裂縫處",
      "description": "這裡有一道裂縫(hole)。",
      "sector_type": "SECT_CITY",
      "coord": [0, 2, 0],
      "cluster": "trial-route",
      "exits": [
        { "direction": "south", "to": 9102 }
      ],
      "keywords": [
        {
          "keyword": "hole",
          "description": "有個柔和的聲音驅使你要鑽(bore)過這個裂縫。"
        }
      ],
      "jobs": [
        {
          "keyword": "bore",
          "function": "job_bore_hole",
          "position": "POS_STANDING"
        }
      ]
    },
    {
      "vnum": 9150,
      "name": "門後小屋",
      "description": "這裡是門後的小屋。",
      "sector_type": "SECT_INSIDE",
      "flags": ["InDoors"],
      "coord": [1, 0, 0],
      "cluster": "gate-house",
      "exits": [
        {
          "direction": "out",
          "to": 9101,
          "exit_keyword": "gate",
          "exit_desc": "回到入口的木門。",
          "flags": ["IsDoor", "Closed"]
        }
      ]
    }
  ]
}
```
