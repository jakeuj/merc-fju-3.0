# 南蠻密林 (`wild_nanman_jungle`)

## Area Intent

`wild_nanman_jungle` 承接 `city_guiyang` 西向外徑，讓玩家從桂陽邊地城鎮再往外走時，立刻感受到官道秩序被濕熱樹影、藤路、圖騰與獸徑迅速取代。

第一版目標先固定：

- 一條由東向西穿過藤門外徑、圖騰林口與濕根主路的主探索線
- 一條往泥窪低帶與獵骨歇點延伸的側線
- 一條 `up/down` 連到根台高處與林下古祠入口的非平面辨位線
- 以 `#Enquire` / `#Keyword` 暗示南蠻、桂陽、密林、圖騰與更深古祠

## Theme Positioning

- Theme: `探險`
- Subtheme: `南蠻密林 / 部族邊徑`
- LevelRange: `94-100`
- Parent region: `荊南西南邊林`
- World gap filled: 讓桂陽西向外徑正式延伸成南蠻密林前帶，為後續更深密林與林下神殿建立第一層 world-facing wild

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_nanman_jungle",
    "title": "南蠻密林",
    "design_notes": "第一版 spec-first 草案。先固定桂陽西岔外的藤門邊徑、圖騰林口、濕根主路、泥窪低帶與根台高處，讓南境主線在母城之後自然切回高壓密林 wild。",
    "level_range": "94-100",
    "planned_vnum_range": "15301-15330",
    "reserved_room_block": "15301-15330",
    "theme": {
      "primary": "探險",
      "secondary": "南蠻密林 / 部族邊徑"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 15301,
        "target_area": "city_guiyang",
        "label": "桂陽西岔"
      },
      {
        "direction": "down",
        "source_vnum": 15311,
        "target_area": "dng_nanman_temple",
        "label": "林下古祠"
      },
      {
        "direction": "west",
        "source_vnum": 15310,
        "target_area": "wild_nanman_deeps",
        "label": "更深林帶"
      }
    ],
    "clusters": [
      { "id": "east-entry", "label": "東向林口" },
      { "id": "vine-path", "label": "藤路主徑" },
      { "id": "totem-grove", "label": "圖騰林帶" },
      { "id": "marsh-pocket", "label": "泥窪低帶" },
      { "id": "canopy-ridge", "label": "根台高處" }
    ]
  },
  "rooms": [
    {
      "vnum": 15301,
      "name": "藤門外徑",
      "description": "從桂陽西岔再往外走不久，木路牌與城鎮氣味就被藤結與濕熱樹影吞掉大半。這條外徑還算能辨認，卻已經很明白地提醒你，從這裡開始，方向感將不再由官道替你保證。",
      "sector_type": "SECT_FOREST",
      "cluster": "east-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-link"],
      "exits": [
        { "direction": "east", "to": 15212, "external": true },
        { "direction": "west", "to": 15303 },
        { "direction": "north", "to": 15302 }
      ],
      "enquires": ["桂陽", "入口"]
    },
    {
      "vnum": 15302,
      "name": "獵骨歇點",
      "description": "幾截曬白的獸骨和被削平的木樁散在樹下，像有人長期把這裡當作短暫歇腳與辨位的地方。它沒有真正的安全感，卻能讓人意識到這片密林裡還是存在一些只屬於熟路人的秩序。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "east-entry",
      "coord": [0, 1, 0],
      "labels": ["rest", "side-mark"],
      "exits": [
        { "direction": "south", "to": 15301 }
      ],
      "enquires": ["歇腳", "獵戶"]
    },
    {
      "vnum": 15303,
      "name": "濕根主路",
      "description": "粗大的樹根從泥地裡抬出一條勉強能行的主路，腳踩上去時總會伴著潮水與落葉被擠碎的聲音。它像是密林願意留給外來者的最基本善意，但那份善意隨時可能在下一個轉角收回。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "vine-path",
      "coord": [-1, 0, 0],
      "labels": ["main-path", "wet-root"],
      "exits": [
        { "direction": "east", "to": 15301 },
        { "direction": "west", "to": 15304 },
        { "direction": "south", "to": 15305 }
      ],
      "enquires": ["密林", "出口"]
    },
    {
      "vnum": 15304,
      "name": "圖騰林口",
      "description": "幾根被煙燻過的木柱半藏在藤影之間，柱面刻痕不像官府文字，卻有一種被人長久重複觸碰後留下的莊重感。這裡讓密林突然多出一點人的氣息，但那並不是能讓外人放鬆的氣息。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "totem-grove",
      "coord": [-2, 0, 0],
      "labels": ["totem", "threshold"],
      "exits": [
        { "direction": "east", "to": 15303 },
        { "direction": "west", "to": 15307 },
        { "direction": "up", "to": 15309 }
      ],
      "keywords": [
        {
          "keyword": "圖騰",
          "description": "木柱上的刻痕像部族用來辨界、祭告或警示的記號，雖然你看不懂全部意思，卻能感覺到它不是隨意立在這裡的。"
        }
      ],
      "enquires": ["圖騰", "部族"]
    },
    {
      "vnum": 15305,
      "name": "泥窪低帶",
      "description": "路面突然陷進一片長滿薄草與積水的低帶，鞋底很容易被泥水拖住半拍。這裡不是明顯的陷阱，但每一步都會提醒你，南蠻密林真正消耗人的方式，是慢慢把節奏與判斷一起磨鈍。 ",
      "sector_type": "SECT_SWAMP",
      "cluster": "marsh-pocket",
      "coord": [-1, -1, -1],
      "labels": ["low-ground", "mud"],
      "exits": [
        { "direction": "north", "to": 15303 },
        { "direction": "west", "to": 15306 }
      ],
      "enquires": ["泥地", "退路"]
    },
    {
      "vnum": 15306,
      "name": "伏藤窄口",
      "description": "幾道粗藤貼著地面和樹幹交錯，逼得人只能側身從窄口穿過。風很難吹進來，四周安靜得只剩水珠滴落與林葉摩擦的聲音，像整片林子都在等你決定要不要再往深處送一步。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "marsh-pocket",
      "coord": [-2, -1, -1],
      "labels": ["narrow-pass", "vines"],
      "exits": [
        { "direction": "east", "to": 15305 },
        { "direction": "west", "to": 15308 }
      ],
      "enquires": ["藤路", "深處"]
    },
    {
      "vnum": 15307,
      "name": "祭柱空地",
      "description": "林間難得空出一小塊地，幾根矮柱與燒黑土圈讓人看得出這裡曾反覆被拿來做某種儀式。它沒有真正的火光與人聲，卻比許多熱鬧地方更讓人不敢輕舉妄動。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "totem-grove",
      "coord": [-3, 0, 0],
      "labels": ["ritual", "open-ground"],
      "exits": [
        { "direction": "east", "to": 15304 },
        { "direction": "south", "to": 15308 },
        { "direction": "north", "to": 15311 }
      ],
      "enquires": ["祭柱", "空地"]
    },
    {
      "vnum": 15308,
      "name": "根台高徑",
      "description": "幾層盤結巨根把地面抬成一段較高的徑道，站上去後能短暫看見周圍林帶的高低與霧氣流向。這種高度不是為了風景，而是讓人終於能把剛才一路的混亂重新拼回一點方向感。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "canopy-ridge",
      "coord": [-3, -1, 0],
      "labels": ["high-route", "ridge"],
      "exits": [
        { "direction": "north", "to": 15307 },
        { "direction": "east", "to": 15306 },
        { "direction": "west", "to": 15310 },
        { "direction": "down", "to": 15312 }
      ],
      "enquires": ["高處", "去路", "密林"]
    },
    {
      "vnum": 15309,
      "name": "樹冠望根",
      "description": "沿著側枝與盤根爬上來後，視野終於能越過底下那層濕重樹影，勉強看出桂陽方向的光色還留在哪一邊。這裡讓人暫時找回判斷，卻也更清楚地看見自己其實已經離城很遠。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "canopy-ridge",
      "coord": [-2, 0, 1],
      "labels": ["lookout", "up"],
      "exits": [
        { "direction": "down", "to": 15304 }
      ],
      "enquires": ["桂陽", "樹上"]
    },
    {
      "vnum": 15310,
      "name": "深林西線",
      "description": "再往西去，地面痕跡開始被更厚的落葉與獸徑分裂成許多互不相讓的小路。這裡不像真正的終點，反而像密林在你面前把更深、更不講理的世界微微掀開一角。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "canopy-ridge",
      "coord": [-4, -1, 0],
      "labels": ["west-edge", "deep-link"],
      "exits": [
        { "direction": "east", "to": 15308 }
      ],
      "enquires": ["西邊", "深林"]
    },
    {
      "vnum": 15311,
      "name": "林下祠痕",
      "description": "一段被根鬚包住的石階往更低處沉去，石面上還殘留著香灰與細小刻紋，像某座被林子半吞沒的古祠仍在底下維持著不完全熄滅的存在。站在這裡時，會很自然想到下面不會只是普通林地。 ",
      "sector_type": "SECT_FOREST",
      "cluster": "totem-grove",
      "coord": [-3, 1, 0],
      "labels": ["down-link", "temple-threshold"],
      "exits": [
        { "direction": "south", "to": 15307 }
      ],
      "enquires": ["古祠", "下方"]
    },
    {
      "vnum": 15312,
      "name": "霧泥凹地",
      "description": "高徑下方是一小片積霧凹地，泥水比上面的路更冷、更黏，也更容易把聲音整個吸住。你很難在這裡久待，卻會記住它像是密林故意留給入侵者的一道壓力測試。 ",
      "sector_type": "SECT_SWAMP",
      "cluster": "marsh-pocket",
      "coord": [-3, -2, -1],
      "labels": ["down", "mist-pocket"],
      "exits": [
        { "direction": "up", "to": 15308 }
      ],
      "enquires": ["霧", "低地"]
    }
  ]
}
```
