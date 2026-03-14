# 洛陽地下水區 (`dng_loyang_sewer`)

## Area Intent

`dng_loyang_sewer` 承接 `loyang_outskirts` 暗井下方的檢修道，讓玩家從城郊地表一路下探到真正的地下水路前帶。這裡不是單純的下水道，而是混合了舊時水利設施、殘破封印與不知名活動痕跡的潮濕地下區。

第一版目標先固定：

- 一條由入口往深處延伸的主地下通道
- 一條偏向側渠與失物堆積的支線
- 一條 `down/up` 的 deeper sewer 非平面連線
- 以 `#Enquire` / `#Keyword` 暗示入口、水門、符痕與退路

## Theme Positioning

- Theme: `仙俠風`
- Subtheme: `詭異民俗風`
- LevelRange: `12-22`
- Parent area: `loyang_outskirts`
- World gap filled: 把洛陽東郊暗井入口之後的真正地下水區做成可探索區，讓地表與 deeper sewer 之間多一層地下前哨

## Player Flow

1. 玩家從 `loyang_outskirts/7512` 向下進入本區時，先感受到檢修道轉成真正地下水路的節奏變化。
2. 主線沿著石拱匯流道與封印前廊往深處推進，逐步加重潮氣、異響與封印感。
3. 側渠支線提供失物、傳聞與較生活化的人為痕跡，讓地下區不只剩戰鬥。
4. 最深處的沉井與鐵梯以 `down/up` 預留更深層 sewer / 地底機關區。

## Cluster Notes

### `entry-drain`

- 房間重點：入口水門、潮濕檢修渠
- 玩家感受：剛離開地表，退路仍清楚，但壓迫感已經開始
- 對外角色：承接 `loyang_outskirts/7512`

### `main-flow`

- 房間重點：石拱匯流道、黑水沉井
- 玩家感受：空間變深、回音變重、真正地下探索開始
- 對外角色：作為更深地下區的主線前帶

### `side-sluice`

- 房間重點：生鏽側渠、碎欄積水間、失物堆積室
- 玩家感受：雜亂、潮濕、有人來過但不該久留
- 對外角色：提供支線探索與失物 / 線索感

### `sealed-gate`

- 房間重點：封印泵室前廊、殘符水門、深井鐵梯
- 玩家感受：詭異、神秘、像還有更深一層被刻意封住
- 對外角色：作為未來 deeper sewer / 地底機關區入口 stub

## Planned World Links

- `up` from `9451`: planned link to `loyang_outskirts` room `7512`
- `down` from `9454`: planned continuation to `deeper sewer / 地底機關區`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在入口水門、匯流道、封印前廊與深井鐵梯，讓玩家能問 `入口 / 退路 / 深處 / 水門`
- `#Keyword` 第一版會落在符痕、水痕、鐵梯、失物堆，讓地下探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
洛陽東郊井下檢修道(7512)
   |
[9451] 入口水門 -- [9452] 潮濕檢修渠 -- [9453] 石拱匯流道 -- [9454] 黑水沉井
                                      |                                 |
                                   [9455] 生鏽側渠 -- [9456] 碎欄積水間 -- [9457] 封印泵室前廊 -- [9458] 殘符水門
                                                                                               |
                                                                                            [9459] 失物堆積室
                                                                                               |
                                                                                            [9460] 深井鐵梯

[9454] down -> future deeper sewer
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_loyang_sewer",
    "title": "洛陽地下水區",
    "design_notes": "第一版 spec-first 草案。先固定暗井下方的地下水路主線、側渠支線與 deeper sewer 垂直入口。",
    "parent_area": "loyang_outskirts",
    "level_range": "12-22",
    "planned_vnum_range": "9451-9460",
    "theme": {
      "primary": "仙俠風",
      "secondary": "詭異民俗風"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9451,
        "target_area": "loyang_outskirts",
        "target_room_vnum": 7512,
        "label": "井下檢修道"
      },
      {
        "direction": "down",
        "source_vnum": 9454,
        "target_area": "dng_sewer_depths",
        "label": "更深水道"
      }
    ],
    "clusters": [
      { "id": "entry-drain", "label": "入口排水前帶" },
      { "id": "main-flow", "label": "主匯流通道" },
      { "id": "side-sluice", "label": "側渠與積水支線" },
      { "id": "sealed-gate", "label": "封印水門前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 9451,
      "name": "入口水門",
      "description": "狹窄檢修道在這裡銜接上一道半開的舊水門，門軸因長年受潮而發出低沉摩擦聲。往上還能辨出井口傳來的微弱天光，往裡則只剩水聲與石壁反覆回響。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-drain",
      "coord": [0, 0, -1],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 7512, "external": true },
        { "direction": "east", "to": 9452 }
      ],
      "enquires": ["入口", "退路"]
    },
    {
      "vnum": 9452,
      "name": "潮濕檢修渠",
      "description": "石渠兩側貼著濕滑青苔，腳邊薄水不斷沿坡緩慢流向更深處。這裡仍看得出人工整修的痕跡，但越往前，那些規整線條就越像被什麼東西啃掉了。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-drain",
      "coord": [1, 0, -1],
      "labels": ["channel", "transition"],
      "exits": [
        { "direction": "west", "to": 9451 },
        { "direction": "east", "to": 9453 },
        { "direction": "south", "to": 9455 }
      ],
      "keywords": [
        {
          "keyword": "水痕",
          "description": "石壁上的水痕分成新舊兩層，舊痕幾乎高過你的胸口，讓人很難不去想像暴雨時這裡會變成什麼模樣。"
        }
      ]
    },
    {
      "vnum": 9453,
      "name": "石拱匯流道",
      "description": "幾道地下水脈在這裡匯進石拱通道，水聲混在一起後變得難以判讀方向。頭頂拱壁還留著模糊記號，像是以前維修人員用來區分支渠的標誌。",
      "sector_type": "SECT_INSIDE",
      "cluster": "main-flow",
      "coord": [2, 0, -1],
      "labels": ["junction", "enquire"],
      "exits": [
        { "direction": "west", "to": 9452 },
        { "direction": "east", "to": 9454 },
        { "direction": "south", "to": 9456 }
      ],
      "enquires": ["深處", "水門", "匯流"]
    },
    {
      "vnum": 9454,
      "name": "黑水沉井",
      "description": "通道盡頭陷成一口向下延伸的沉井，黑色水面反射不出任何清楚影像。井壁邊緣釘著舊鐵環與斷裂繩索，像曾有人頻繁在這裡上下。",
      "sector_type": "SECT_INSIDE",
      "cluster": "main-flow",
      "coord": [3, 0, -1],
      "labels": ["deep-well", "world-link-down"],
      "exits": [
        { "direction": "west", "to": 9453 },
        { "direction": "down", "to": 9460 }
      ],
      "keywords": [
        {
          "keyword": "鐵環",
          "description": "鐵環上佈滿鏽色與刮痕，表示這口沉井不只是自然形成，而是被長期拿來當作通往更深處的節點。"
        }
      ],
      "enquires": ["沉井", "下方"]
    },
    {
      "vnum": 9455,
      "name": "生鏽側渠",
      "description": "側渠比主水路低矮得多，兩側卡滿腐朽木板與鏽掉的鐵柵。水流在這裡變慢，夾雜著地表沖落的雜物與早該消失的生活痕跡。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-sluice",
      "coord": [1, -1, -1],
      "labels": ["side-branch"],
      "exits": [
        { "direction": "north", "to": 9452 },
        { "direction": "east", "to": 9456 }
      ]
    },
    {
      "vnum": 9456,
      "name": "碎欄積水間",
      "description": "一道斷裂木欄把積水困成幾處淺池，池底沉著難辨原貌的碎物與泥沙。這裡像是被匆忙棄置的暫存點，卻又有人時不時回來翻找。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-sluice",
      "coord": [2, -1, -1],
      "labels": ["junk-room", "search"],
      "exits": [
        { "direction": "west", "to": 9455 },
        { "direction": "north", "to": 9453 },
        { "direction": "east", "to": 9457 }
      ],
      "keywords": [
        {
          "keyword": "碎欄",
          "description": "木欄斷面上有新舊不一的劈痕，像是有人故意把封住的側間重新撬開。"
        }
      ]
    },
    {
      "vnum": 9457,
      "name": "封印泵室前廊",
      "description": "前廊兩側石壁刻滿半殘符痕，地面還嵌著幾條導水槽。這裡本該是單純的泵室前帶，現在卻像同時肩負著壓水與鎮壓某種東西的用途。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-gate",
      "coord": [3, -1, -1],
      "labels": ["sealed-hall", "ritual-hint"],
      "exits": [
        { "direction": "west", "to": 9456 },
        { "direction": "east", "to": 9458 },
        { "direction": "south", "to": 9459 }
      ],
      "enquires": ["符痕", "前廊", "退路"]
    },
    {
      "vnum": 9458,
      "name": "殘符水門",
      "description": "厚重水門上殘留著大片剝落符墨，只剩零碎線條仍在潮氣中勉強辨形。門後不斷傳來低沉水擊聲，像更深處還有另一套水路在運作。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-gate",
      "coord": [4, -1, -1],
      "labels": ["gate", "landmark"],
      "exits": [
        { "direction": "west", "to": 9457 }
      ],
      "keywords": [
        {
          "keyword": "符痕",
          "description": "符痕一部分像道門符咒，一部分又像水利標記，混在一起時反而更讓人不安。"
        }
      ],
      "enquires": ["水門", "符文"]
    },
    {
      "vnum": 9459,
      "name": "失物堆積室",
      "description": "角落堆著破布包、碎陶片與被水泡爛的木牌，像多年來被水流和人手一起推來這裡的殘渣。偶爾還能看出一兩件屬於地表旅人的遺失物，讓這裡多了幾分不祥。",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-sluice",
      "coord": [3, -2, -1],
      "labels": ["loot-hint", "rumor"],
      "exits": [
        { "direction": "north", "to": 9457 }
      ],
      "keywords": [
        {
          "keyword": "失物",
          "description": "失物裡混著市井常見的小東西，證明地表早就有人因各種理由摸到這片地下水區。"
        }
      ],
      "enquires": ["失物", "來路"]
    },
    {
      "vnum": 9460,
      "name": "深井鐵梯",
      "description": "沉井內側釘著向下延伸的鐵梯，濕冷鐵鏽味幾乎蓋過一切。再往井底下望去，只有更黑、更深、更安靜的空間在等人下探。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-gate",
      "coord": [3, 0, -2],
      "labels": ["vertical", "future-depth"],
      "exits": [
        { "direction": "up", "to": 9454 }
      ],
      "enquires": ["出口", "深處"]
    }
  ]
}
```
