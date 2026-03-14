# 帝王古墓 (`dng_royal_tomb`)

## Area Intent

`dng_royal_tomb` 承接 `dng_sewer_depths` 最深處下沉井口之下的裂井空間，讓玩家從深層水道正式轉入帝王古墓前帶。這裡不再只是潮濕與黑水，而是開始出現封墓石門、陪葬側室、殘破銅燈與機關鎮壓痕跡交疊的古墓探索感。

第一版目標先固定：

- 一條由裂井落點通往石門主廊的主墓道
- 一條偏向陪葬側室與守墓遺物的支線
- 一條 `down/up` 的更深封墓井非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、石門、墓志與鎮壓機關

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `古墓 / 機關`
- LevelRange: `18-30`
- Parent area: `dng_sewer_depths`
- World gap filled: 把深層水道下方的古墓深井做成真正可探索的遺跡前帶，讓洛陽地下鏈從水道系轉入古墓與機關探索

## Player Flow

1. 玩家從 `dng_sewer_depths/9470` 向下進入本區時，先感受到黑水腐氣逐漸被陳封土氣與金屬冷味取代。
2. 主線沿著裂井前廳、石門墓道與鎮機主廊推進，逐步增加墓葬壓迫感與機關戒備感。
3. 側室支線提供陪葬痕跡、殘碑與遺物線索，讓古墓區不只是直線衝刺。
4. 最深處的封墓井以 `down/up` 預留更深墓室群與地底埋葬層，保留地下鏈下一段延伸空間。

## Cluster Notes

### `shaft-vestibule`

- 房間重點：裂井前廳、落井石台
- 玩家感受：剛離開深渠，退路仍可辨識，但空氣與材質感已完全改變
- 對外角色：承接 `dng_sewer_depths/9470`

### `stone-corridor`

- 房間重點：石門墓道、鎮機主廊、青燈門檻
- 玩家感受：壓抑、肅穆、開始明顯感到墓葬秩序與機關威脅
- 對外角色：作為古墓主線探索帶

### `burial-side`

- 房間重點：陪葬側室、殘碑耳室、銅匣角間
- 玩家感受：靜止、神秘、像能挖出古墓用途與守墓線索
- 對外角色：提供支線探索與 lore 線索

### `sealed-well`

- 房間重點：封墓前台、封墓井口、下層石階
- 玩家感受：危險、未知、像真正的核心墓室仍在更底下
- 對外角色：作為未來更深墓室群 / 埋葬層入口 stub

## Planned World Links

- `up` from `9481`: planned link to `dng_sewer_depths` room `9470`
- `down` from `9490`: planned continuation to `更深墓室群 / 地底埋葬層`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在裂井前廳、石門墓道、封墓前台與封墓井口，讓玩家能問 `退路 / 石門 / 深處 / 古墓`
- `#Keyword` 第一版會落在墓志、銅燈、鎖柱、石階、陪葬匣，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
地下深渠下沉井口(9470)
   |
[9481] 裂井前廳 -- [9482] 落井石台 -- [9483] 石門墓道 -- [9484] 青燈門檻 -- [9488] 封墓前台
                                         |                                  |
                                      [9485] 陪葬側室 -- [9486] 殘碑耳室 -- [9487] 銅匣角間
                                                                                           |
                                                                                        [9489] 封墓井口
                                                                                           |
                                                                                        [9490] 下層石階

[9490] down -> future deeper royal tomb chambers
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_royal_tomb",
    "title": "帝王古墓",
    "design_notes": "第一版 spec-first 草案。先固定深渠之下的古墓前帶、陪葬支線與封墓井非平面入口。",
    "parent_area": "dng_sewer_depths",
    "level_range": "18-30",
    "planned_vnum_range": "9481-9490",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "古墓 / 機關"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9481,
        "target_area": "dng_sewer_depths",
        "target_room_vnum": 9470,
        "label": "下沉井口"
      },
      {
        "direction": "down",
        "source_vnum": 9490,
        "target_area": "sec_catacomb_depths",
        "label": "更深墓室群"
      }
    ],
    "clusters": [
      { "id": "shaft-vestibule", "label": "裂井與前廳帶" },
      { "id": "stone-corridor", "label": "石門墓道主線" },
      { "id": "burial-side", "label": "陪葬與耳室支線" },
      { "id": "sealed-well", "label": "封墓前台與下層井" }
    ]
  },
  "rooms": [
    {
      "vnum": 9481,
      "name": "裂井前廳",
      "description": "裂井落點在這裡擴成一小片石砌前廳，牆面滿是被潮氣喚醒的舊刻痕。抬頭還能望見上方井口殘留的一線濕黑光影，往內則只剩冷硬石壁與沉封土氣。",
      "sector_type": "SECT_INSIDE",
      "cluster": "shaft-vestibule",
      "coord": [0, 0, -5],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9470, "external": true },
        { "direction": "east", "to": 9482 }
      ],
      "enquires": ["退路", "古墓"]
    },
    {
      "vnum": 9482,
      "name": "落井石台",
      "description": "石台表面刻著一道早被磨損的環形紋，像是專門接應自上方落下之人的緩衝台。周圍散著幾片裂開的銅扣與石屑，顯示古墓防護曾在這裡啟動過。",
      "sector_type": "SECT_INSIDE",
      "cluster": "shaft-vestibule",
      "coord": [1, 0, -5],
      "labels": ["landing", "transition"],
      "exits": [
        { "direction": "west", "to": 9481 },
        { "direction": "east", "to": 9483 }
      ],
      "keywords": [
        {
          "keyword": "銅扣",
          "description": "銅扣表面佈滿細小榫孔，像是原本配合某種墜落或封門機關使用的構件。"
        }
      ]
    },
    {
      "vnum": 9483,
      "name": "石門墓道",
      "description": "墓道兩側站著半身沒入石牆的鎮墓武士浮雕，前方則是一道已被推開些許的厚重石門。空氣裡幾乎沒有水氣，只剩陳土與金屬冷味慢慢滲進肺裡。",
      "sector_type": "SECT_INSIDE",
      "cluster": "stone-corridor",
      "coord": [2, 0, -5],
      "labels": ["gate", "junction"],
      "exits": [
        { "direction": "west", "to": 9482 },
        { "direction": "east", "to": 9484 },
        { "direction": "south", "to": 9485 }
      ],
      "keywords": [
        {
          "keyword": "石門",
          "description": "石門邊緣留下被強行推移過的磨痕，顯示古墓曾有人從外側進入，也曾有人試圖再度封上。"
        }
      ],
      "enquires": ["石門", "前路"]
    },
    {
      "vnum": 9484,
      "name": "青燈門檻",
      "description": "門檻兩側各立著一座銅燈座，燈芯早已熄滅，卻仍散著淡淡焦苦味。越往前走，地面石紋越工整，也越像在提醒你正一步步靠近真正重要的墓室。",
      "sector_type": "SECT_INSIDE",
      "cluster": "stone-corridor",
      "coord": [3, 0, -5],
      "labels": ["threshold", "grave-hint"],
      "exits": [
        { "direction": "west", "to": 9483 },
        { "direction": "east", "to": 9488 }
      ],
      "keywords": [
        {
          "keyword": "銅燈",
          "description": "銅燈座表面覆著青綠鏽層，內壁還殘留一圈乾硬油痕，像有人曾長期維持這裡的照明。"
        }
      ],
      "enquires": ["深處", "墓道"]
    },
    {
      "vnum": 9485,
      "name": "陪葬側室",
      "description": "側室四角擺著破損木架與傾倒陶甕，牆邊則堆著幾件包覆麻布的長形器物。它們多半已被時間毀壞，但仍能看出這裡曾被用來陳列某些重要陪葬品。",
      "sector_type": "SECT_INSIDE",
      "cluster": "burial-side",
      "coord": [2, -1, -5],
      "labels": ["side-room", "burial"],
      "exits": [
        { "direction": "north", "to": 9483 },
        { "direction": "east", "to": 9486 }
      ],
      "keywords": [
        {
          "keyword": "麻布",
          "description": "麻布早已脆裂，卻仍勉強包住器物輪廓，像怕有人一眼看出裡面原本藏的是什麼。"
        }
      ]
    },
    {
      "vnum": 9486,
      "name": "殘碑耳室",
      "description": "耳室牆邊斜靠著一塊裂成兩半的墓碑殘片，碑文大半剝落，只剩幾個與封號、葬制有關的字樣仍可辨識。這裡不像主墓室，卻像記錄整座古墓身份的備份角落。",
      "sector_type": "SECT_INSIDE",
      "cluster": "burial-side",
      "coord": [3, -1, -5],
      "labels": ["tablet", "lore"],
      "exits": [
        { "direction": "west", "to": 9485 },
        { "direction": "east", "to": 9487 }
      ],
      "keywords": [
        {
          "keyword": "殘碑",
          "description": "殘碑上仍可見幾筆肅穆端正的墓志字形，像在提醒你這裡埋葬的身分遠高於一般豪強。"
        }
      ],
      "enquires": ["墓志", "碑文"]
    },
    {
      "vnum": 9487,
      "name": "銅匣角間",
      "description": "角間裡散著幾個翻倒的銅匣與斷裂木盒，匣內大多空了，卻還留著細碎金屬片與乾硬絹布。這些遺物不像單純遭竊，更像曾有人急著從這裡帶走某些核心物件。",
      "sector_type": "SECT_INSIDE",
      "cluster": "burial-side",
      "coord": [4, -1, -5],
      "labels": ["relic", "search"],
      "exits": [
        { "direction": "west", "to": 9486 },
        { "direction": "north", "to": 9488 }
      ],
      "keywords": [
        {
          "keyword": "銅匣",
          "description": "銅匣內壁還留著細密鎖孔與卡槽，顯示它們曾用來收納不只金銀，還可能是某種印信或機關鑰件。"
        }
      ]
    },
    {
      "vnum": 9488,
      "name": "封墓前台",
      "description": "前台中央有一道向下凹陷的封墓井，井緣圍著四根帶鎖槽的石柱。四周牆面刻滿被磨蝕的鎮壓紋路，讓人一眼便知真正重要的墓室還在更底下。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-well",
      "coord": [4, 0, -5],
      "labels": ["sealed", "threshold"],
      "exits": [
        { "direction": "west", "to": 9484 },
        { "direction": "south", "to": 9487 },
        { "direction": "east", "to": 9489 }
      ],
      "enquires": ["封墓", "退路", "古墓"]
    },
    {
      "vnum": 9489,
      "name": "封墓井口",
      "description": "井口周圍留著明顯拖鍊痕與碎裂石楔，像曾有一套能把整個井口重新封死的重型機關。低頭往下看時，只見石階與黑暗一圈圈往更深處盤去。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-well",
      "coord": [5, 0, -5],
      "labels": ["pit", "vertical-entry"],
      "exits": [
        { "direction": "west", "to": 9488 },
        { "direction": "down", "to": 9490 }
      ],
      "keywords": [
        {
          "keyword": "石柱",
          "description": "石柱上的鎖槽和鐵鍊痕一一對位，顯示這口封墓井曾被設計成可開可閉的重機關。"
        }
      ],
      "enquires": ["井口", "下方"]
    },
    {
      "vnum": 9490,
      "name": "下層石階",
      "description": "石階緊貼井壁向下盤旋，階面鋪滿積灰與碎石，卻仍保有整齊得近乎刻意的角度。越往下望去，越能感覺到更深層墓室像把整片空氣都壓得更沉。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-well",
      "coord": [5, 0, -6],
      "labels": ["vertical", "future-depth"],
      "exits": [
        { "direction": "up", "to": 9489 }
      ],
      "enquires": ["出口", "深處"]
    }
  ]
}
```
