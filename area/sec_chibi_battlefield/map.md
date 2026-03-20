# 赤壁古戰場 (`sec_chibi_battlefield`)

## Area Intent

`sec_chibi_battlefield` 承接 `city_chaisang` 南向赤壁路標之後的戰場支線，讓玩家從江岸城市的補給與秩序，一腳踏進滿是焦木、殘艦、灰燼與舊戰意回聲的古戰場祕區。

第一版目標先固定：

- 一條由北向南穿過戰場邊緣、灰坡與焦土主陣的主探索線
- 一條沿江殘艦與壕溝分流的側線
- 一條 `up/down` 連到灰坡望火臺與壕溝落差的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示赤壁、柴桑、戰火、殘艦與祭火遺痕

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `江岸古戰場 / 戰痕幻境`
- LevelRange: `68-78`
- Parent region: `柴桑南緣`
- World gap filled: 讓 `city_chaisang` 已預留的南向戰場支線成為正式 spec-first 祕區，為後續江東主線與更深事件區保留高辨識度切口

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_chibi_battlefield",
    "title": "赤壁古戰場",
    "design_notes": "第一版 spec-first 草案。先固定由柴桑南標切入的古戰場邊緣、灰坡、殘艦灘與祭火高地骨架，讓城市補給節奏能自然切入戰場祕區。",
    "level_range": "68-78",
    "planned_vnum_range": "14801-14830",
    "reserved_room_block": "14801-14830",
    "theme": {
      "primary": "軍旅",
      "secondary": "江岸古戰場 / 戰痕幻境"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 14801,
        "target_area": "city_chaisang",
        "label": "柴桑赤壁路標"
      },
      {
        "direction": "south",
        "source_vnum": 14810,
        "target_area": "wild_old_battlefield",
        "label": "江岸焦土外帶"
      },
      {
        "direction": "east",
        "source_vnum": 14812,
        "target_area": "river_crossing",
        "label": "殘艦浮橋"
      }
    ],
    "clusters": [
      { "id": "north-marker", "label": "北向路標邊界" },
      { "id": "ash-slope", "label": "灰燼坡帶" },
      { "id": "burned-flotilla", "label": "殘艦灘帶" },
      { "id": "ember-line", "label": "焦土主陣" },
      { "id": "ritual-rise", "label": "祭火高地" }
    ]
  },
  "rooms": [
    {
      "vnum": 14801,
      "name": "赤壁北標",
      "description": "由柴桑一路南行到此，路牌與江風一起把人送進這片明顯不再屬於城鎮秩序的地帶。地面摻著灰黑色碎炭，遠處還能看到燒成歪影的木樁與斷旗，像戰火雖已遠去，餘意卻還黏在風裡。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-marker",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-north"],
      "exits": [
        { "direction": "north", "to": 14712, "external": true },
        { "direction": "south", "to": 14802 },
        { "direction": "east", "to": 14803 }
      ],
      "enquires": ["柴桑", "赤壁", "戰場"]
    },
    {
      "vnum": 14802,
      "name": "灰燼緩坡",
      "description": "坡面覆著一層被踩碎的灰燼與燒裂木片，每走一步都會帶起細碎黑屑。這裡不像真正的山坡，更像曾有大量帳棚、器械與火線在此聚集，等一切燒過之後，只留下高低起伏的灰色地脈。",
      "sector_type": "SECT_FIELD",
      "cluster": "ash-slope",
      "coord": [0, -1, 0],
      "labels": ["slope", "ash"],
      "exits": [
        { "direction": "north", "to": 14801 },
        { "direction": "south", "to": 14805 },
        { "direction": "down", "to": 14804 }
      ],
      "enquires": ["焦土", "灰燼"]
    },
    {
      "vnum": 14803,
      "name": "斷旗壕口",
      "description": "幾支斷得只剩半截的旗杆插在壕口邊，旗面早被燒得不成樣子，卻仍保留著曾經指向陣線的姿態。站在這裡時，你會直覺地覺得往前不是單純探路，而是在跨進某種仍未散盡的交鋒記憶。",
      "sector_type": "SECT_FIELD",
      "cluster": "ash-slope",
      "coord": [1, 0, 0],
      "labels": ["trench-mouth", "marker"],
      "exits": [
        { "direction": "west", "to": 14801 },
        { "direction": "south", "to": 14806 }
      ],
      "keywords": [
        {
          "keyword": "斷旗",
          "description": "旗杆焦黑而傾斜，布面只剩幾縷黏在木刺上，像還記得當年曾指向哪一支軍勢。"
        }
      ],
      "enquires": ["陣線", "戰火"]
    },
    {
      "vnum": 14804,
      "name": "灰坑壕溝",
      "description": "壕溝裡積著一層混了泥與炭的冷灰，踩下去比地表更軟，彷彿這裡曾長時間承受燃燒與重踏。壕底的視線被兩側灰坡壓低，會讓人很快失去對整片戰場方位的掌握。",
      "sector_type": "SECT_FIELD",
      "cluster": "ash-slope",
      "coord": [0, -2, -1],
      "labels": ["trench", "down"],
      "exits": [
        { "direction": "up", "to": 14802 },
        { "direction": "east", "to": 14805 }
      ],
      "enquires": ["壕溝", "退路"]
    },
    {
      "vnum": 14805,
      "name": "焦木坡面",
      "description": "坡面斜斜朝主戰場展開，幾截被燒空的木柱從灰裡探出頭來，像一排早已倒下的拒馬骨架。視野在這裡開始往南拉開，戰場的開闊與危險也同時變得更真切。",
      "sector_type": "SECT_FIELD",
      "cluster": "ember-line",
      "coord": [0, -2, 0],
      "labels": ["main-approach", "battlefield"],
      "exits": [
        { "direction": "north", "to": 14802 },
        { "direction": "west", "to": 14804 },
        { "direction": "east", "to": 14806 },
        { "direction": "south", "to": 14808 },
        { "direction": "up", "to": 14811 }
      ],
      "enquires": ["主陣", "江風"]
    },
    {
      "vnum": 14806,
      "name": "殘艦灘口",
      "description": "江岸這一帶堆著燒裂船板、斷槳與被火熏黑的纜繩，殘骸在潮聲裡撞擊出乾硬聲響。比起一般水邊，這裡更像一段被水留住、卻始終沒被水真正洗乾淨的戰敗遺面。",
      "sector_type": "SECT_FIELD",
      "cluster": "burned-flotilla",
      "coord": [1, -1, 0],
      "labels": ["shore", "wreckage"],
      "exits": [
        { "direction": "north", "to": 14803 },
        { "direction": "west", "to": 14805 },
        { "direction": "south", "to": 14807 }
      ],
      "enquires": ["殘艦", "江岸"]
    },
    {
      "vnum": 14807,
      "name": "裂舟泊處",
      "description": "半截破船卡在淺灘邊，船身焦黑卻還保留了勉強可辨的舷緣輪廓。靠近時，能看到船板裡外都留下猛烈火舌舔過的痕跡，讓人難以不去想像這裡曾經如何亂成一片。",
      "sector_type": "SECT_FIELD",
      "cluster": "burned-flotilla",
      "coord": [1, -2, 0],
      "labels": ["wreck", "shoreline"],
      "exits": [
        { "direction": "north", "to": 14806 },
        { "direction": "west", "to": 14808 },
        { "direction": "east", "to": 14812 }
      ],
      "keywords": [
        {
          "keyword": "殘艦",
          "description": "燒焦船板上仍有鐵釘與纜孔，說明它曾是真正負載軍士與火勢的戰船，而不是普通民舟。"
        }
      ],
      "enquires": ["船火", "水戰"]
    },
    {
      "vnum": 14808,
      "name": "火痕主陣",
      "description": "這裡的地面比別處更黑，灰層下還露出被高溫燒裂的泥紋，像整片土地都曾被迫記住那場火。站在主陣中央，四周風聲與殘木摩擦聲混在一起，會讓人一時分不清自己聽見的是現在還是往昔。",
      "sector_type": "SECT_FIELD",
      "cluster": "ember-line",
      "coord": [0, -3, 0],
      "labels": ["core", "ember-line"],
      "exits": [
        { "direction": "north", "to": 14805 },
        { "direction": "east", "to": 14807 },
        { "direction": "south", "to": 14810 },
        { "direction": "west", "to": 14809 }
      ],
      "enquires": ["赤壁", "主陣", "戰痕"]
    },
    {
      "vnum": 14809,
      "name": "斷戟散地",
      "description": "地上散著斷裂戟尖、燒彎箭鏃與碎裂甲片，像有人在混亂中把整場交鋒的殘痕都抖落在這一小片灰地上。這裡不算廣，卻比任何地方都更像戰鬥真正貼身發生過的證據。",
      "sector_type": "SECT_FIELD",
      "cluster": "ember-line",
      "coord": [-1, -3, 0],
      "labels": ["debris", "side-pocket"],
      "exits": [
        { "direction": "east", "to": 14808 }
      ],
      "keywords": [
        {
          "keyword": "斷戟",
          "description": "戟刃與槍鐏散得毫無章法，卻正因如此，更顯得這裡曾不是排演，而是真正的死戰。"
        }
      ],
      "enquires": ["兵器", "殘痕"]
    },
    {
      "vnum": 14810,
      "name": "南緣焦土",
      "description": "再往南去，焦土地帶漸漸往更遠處散開，像這片古戰場的傷口其實還沒在這裡結束。邊界不像城門那樣明確，反而是一種只要再多走幾步，就會完全脫離目前可辨地標的危險提示。",
      "sector_type": "SECT_FIELD",
      "cluster": "ember-line",
      "coord": [0, -4, 0],
      "labels": ["south-edge", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 14808 }
      ],
      "enquires": ["南邊", "焦土"]
    },
    {
      "vnum": 14811,
      "name": "望火高臺",
      "description": "高臺本來也許只是陣地裡較高的一角，如今卻成了俯瞰整片灰坡與殘艦灘最清楚的地方。站在這裡向北望去，能看見柴桑方向的生氣仍在遠處，而腳下這片地則像被兩種時間硬生生割開。",
      "sector_type": "SECT_FIELD",
      "cluster": "ritual-rise",
      "coord": [0, -2, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 14805 },
        { "direction": "south", "to": 14812 }
      ],
      "enquires": ["高臺", "柴桑"]
    },
    {
      "vnum": 14812,
      "name": "祭火殘臺",
      "description": "石臺一半傾倒在岸邊碎石與焦木之間，另一半仍保留著被煙熏黑的紋路。它看起來不像普通軍營用具，更像戰後有人曾在此停留、祭告、或試圖替這片地留下某種能被記住的意義。",
      "sector_type": "SECT_FIELD",
      "cluster": "ritual-rise",
      "coord": [1, -2, 1],
      "labels": ["altar", "east-link"],
      "exits": [
        { "direction": "north", "to": 14811 },
        { "direction": "west", "to": 14807 }
      ],
      "keywords": [
        {
          "keyword": "祭臺",
          "description": "石面紋路已被煙火熏得模糊，仍能看出它不是自然形成，而是帶著某種儀式意圖所立。"
        }
      ],
      "enquires": ["祭火", "異象", "出口"]
    }
  ]
}
```

## Editing Notes

- `14801` 預留與 `city_chaisang/14712` 的正式北向 runtime boundary
- `14810` 與 `14812` 先保留南向、東向延伸 stub，等後續 queue 決定再落成雙向 runtime link
- 第一版先讓古戰場是可辨位的主線加兩條支線，不急著擴成整片大型 event map
- 後續 implementation milestone 可優先補 `殘艦守望者 / 戰後拾遺人 / 焦土巡兵 / 祭火殘靈` 一類最小 runtime 骨架
