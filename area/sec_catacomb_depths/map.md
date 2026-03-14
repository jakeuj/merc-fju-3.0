# 忘川地穴 (`sec_catacomb_depths`)

## Area Intent

`sec_catacomb_depths` 承接 `dng_royal_tomb` 最深處下層石階下方的更深秘境，讓玩家從帝王古墓的封墓秩序正式轉入帶有靈異異象、裂隙光紋與高風險高回報感的 secret zone。這裡已不再只是墓葬延伸，而像是古墓底下意外接上的另一層地脈異域。

第一版目標先固定：

- 一條由石階落點進入異象核心的主線
- 一條偏向秘壇與殘痕獎勵感的支線
- 一條 `down/up` 的更深裂谷非平面連線
- 以 `#Enquire` / `#Keyword` 暗示入口條件、裂隙、光紋與出口判讀

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `地穴 / 靈異`
- LevelRange: `25-35`
- Parent area: `dng_royal_tomb`
- World gap filled: 把帝王古墓底下的 deeper stub 轉成真正可探索的靈異地穴，讓洛陽地下鏈在古墓之後還能延伸出秘境型高風險節點

## Player Flow

1. 玩家從 `dng_royal_tomb/9490` 向下進入本區時，先感受到墓室沉重感被更冰冷、帶靈性回音的空氣取代。
2. 主線沿著裂階前帶與異象核廊向內推進，逐步把古墓探索轉成地脈異象探索。
3. 支線透過秘壇、殘燈與裂隙邊台提供秘境線索與獎勵感。
4. 最深處的裂谷石階以 `down/up` 預留更深層異象裂谷或秘境底層。

## Cluster Notes

### `descent-gate`

- 房間重點：裂階落點、寒霧前帶
- 玩家感受：剛離開古墓，退路仍在，但周圍規則感明顯改變
- 對外角色：承接 `dng_royal_tomb/9490`

### `anomaly-core`

- 房間重點：光紋廊道、異象核廳、回聲石橋
- 玩家感受：神祕、稀有、像正逼近某種地脈異常核心
- 對外角色：作為 secret zone 主線探索帶

### `altar-side`

- 房間重點：秘壇側室、殘燈石台、裂隙邊台
- 玩家感受：高風險高回報、像隨時能挖到重要線索
- 對外角色：提供試煉感、獎勵感與 lore 線索

### `rift-depth`

- 房間重點：異象裂口、下層裂谷階
- 玩家感受：危險、失衡、像真正的祕境底層還在更下方
- 對外角色：作為未來更深裂谷 / 秘境底層入口 stub

## Planned World Links

- `up` from `9491`: planned link to `dng_royal_tomb` room `9490`
- `down` from `9499`: planned continuation to `更深異象裂谷 / 秘境底層`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在裂階落點、異象核廳、秘壇側室與異象裂口，讓玩家能問 `異象 / 退路 / 裂隙 / 出口`
- `#Keyword` 第一版會落在光紋、裂隙、祭壇、殘燈、石橋，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
帝王古墓下層石階(9490)
   |
[9491] 裂階落點 -- [9492] 寒霧前帶 -- [9493] 光紋廊道 -- [9494] 異象核廳 -- [9498] 異象裂口
                                                          |                                |
                                                       [9495] 秘壇側室 -- [9496] 殘燈石台 -- [9497] 裂隙邊台
                                                                                           |
                                                                                        [9499] 下層裂谷階

[9499] down -> future deeper anomaly rift
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_catacomb_depths",
    "title": "忘川地穴",
    "design_notes": "第一版 spec-first 草案。先固定古墓之下的靈異地穴主線、秘壇支線與裂谷石階非平面入口。",
    "parent_area": "dng_royal_tomb",
    "level_range": "25-35",
    "planned_vnum_range": "9491-9499",
    "theme": {
      "primary": "仙俠",
      "secondary": "地穴 / 靈異"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9491,
        "target_area": "dng_royal_tomb",
        "target_room_vnum": 9490,
        "label": "下層石階"
      },
      {
        "direction": "down",
        "source_vnum": 9499,
        "target_area": "sec_rift_below",
        "label": "更深異象裂谷"
      }
    ],
    "clusters": [
      { "id": "descent-gate", "label": "裂階與寒霧前帶" },
      { "id": "anomaly-core", "label": "異象核心主線" },
      { "id": "altar-side", "label": "秘壇與裂隙支線" },
      { "id": "rift-depth", "label": "裂口與下層裂谷" }
    ]
  },
  "rooms": [
    {
      "vnum": 9491,
      "name": "裂階落點",
      "description": "石階在這裡斷成一片向外張開的裂石平台，腳邊冷霧緩慢往上翻湧，像整個地穴都在呼吸。抬頭仍能看見古墓石階殘影，往內則是一片帶著淡青光紋的幽暗通道。",
      "sector_type": "SECT_INSIDE",
      "cluster": "descent-gate",
      "coord": [0, 0, -7],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9490, "external": true },
        { "direction": "east", "to": 9492 }
      ],
      "enquires": ["退路", "異象"]
    },
    {
      "vnum": 9492,
      "name": "寒霧前帶",
      "description": "前帶地面覆著一層不貼地流動的寒霧，踩上去時會像踏進極薄水面般微微下陷。石壁沒有墓葬紋飾，只剩天然裂理與若隱若現的淡光。",
      "sector_type": "SECT_INSIDE",
      "cluster": "descent-gate",
      "coord": [1, 0, -7],
      "labels": ["mist", "transition"],
      "exits": [
        { "direction": "west", "to": 9491 },
        { "direction": "east", "to": 9493 }
      ],
      "keywords": [
        {
          "keyword": "寒霧",
          "description": "寒霧不像單純濕氣，更像被某種地脈異象長期困在這裡的冷意。"
        }
      ]
    },
    {
      "vnum": 9493,
      "name": "光紋廊道",
      "description": "廊道石面被一道道淡青色光紋切開，紋路沿著地面與牆邊不規則延伸，像某種古老陣式已被地脈重新喚醒。走在這裡時，連自己的腳步聲都變得陌生。",
      "sector_type": "SECT_INSIDE",
      "cluster": "anomaly-core",
      "coord": [2, 0, -7],
      "labels": ["glyph", "junction"],
      "exits": [
        { "direction": "west", "to": 9492 },
        { "direction": "east", "to": 9494 },
        { "direction": "south", "to": 9495 }
      ],
      "keywords": [
        {
          "keyword": "光紋",
          "description": "光紋既像刻痕又像流動液光，讓人很難判斷它究竟是機關、符陣，還是地穴本身的異變。"
        }
      ],
      "enquires": ["光紋", "前路"]
    },
    {
      "vnum": 9494,
      "name": "異象核廳",
      "description": "核廳中央懸著一團看不清邊界的淡色光暈，四周空氣都被它扭得微微顫動。站得越近，越能感到古墓的沉重規則正在這裡被另一種更古怪的力量改寫。",
      "sector_type": "SECT_INSIDE",
      "cluster": "anomaly-core",
      "coord": [3, 0, -7],
      "labels": ["core", "anomaly"],
      "exits": [
        { "direction": "west", "to": 9493 },
        { "direction": "east", "to": 9498 }
      ],
      "enquires": ["異象", "核心"]
    },
    {
      "vnum": 9495,
      "name": "秘壇側室",
      "description": "側室中央立著一座形制古怪的低壇，壇面不是供奉器具，而是刻滿像計量地脈流向的細痕。壇腳邊散著碎裂石片與燒黑灰印，像曾有人在此做過某種試煉或引導。",
      "sector_type": "SECT_INSIDE",
      "cluster": "altar-side",
      "coord": [2, -1, -7],
      "labels": ["altar", "side-room"],
      "exits": [
        { "direction": "north", "to": 9493 },
        { "direction": "east", "to": 9496 }
      ],
      "keywords": [
        {
          "keyword": "祭壇",
          "description": "祭壇邊緣刻痕不像單純祭祀圖樣，更像某種校準異象或測試通行資格的裝置。"
        }
      ],
      "enquires": ["祭壇", "入口條件"]
    },
    {
      "vnum": 9496,
      "name": "殘燈石台",
      "description": "幾座細長石台沿牆排開，每座台面都放著熄滅已久的殘燈與細小骨灰般的灰粉。燈芯雖死，台面下方卻仍隱隱透出與核廳相近的淡色冷光。",
      "sector_type": "SECT_INSIDE",
      "cluster": "altar-side",
      "coord": [3, -1, -7],
      "labels": ["lamp", "reward-hint"],
      "exits": [
        { "direction": "west", "to": 9495 },
        { "direction": "east", "to": 9497 }
      ],
      "keywords": [
        {
          "keyword": "殘燈",
          "description": "殘燈油槽早已乾透，卻還殘留著一層薄得不正常的幽光，好像燈火從未真正熄滅。"
        }
      ]
    },
    {
      "vnum": 9497,
      "name": "裂隙邊台",
      "description": "邊台外側就是一道向下延伸的黑色裂隙，裂壁間不時閃過像星點般的微弱光芒。這裡的空氣既冷又輕，站久了會讓人產生自己正慢慢被拉向更深處的錯覺。",
      "sector_type": "SECT_INSIDE",
      "cluster": "altar-side",
      "coord": [4, -1, -7],
      "labels": ["rift", "risk"],
      "exits": [
        { "direction": "west", "to": 9496 },
        { "direction": "north", "to": 9498 }
      ],
      "keywords": [
        {
          "keyword": "裂隙",
          "description": "裂隙邊緣平滑得不自然，像不是天然崩裂，而是被某種力量長期撐開成通道。"
        }
      ],
      "enquires": ["裂隙", "出口"]
    },
    {
      "vnum": 9498,
      "name": "異象裂口",
      "description": "核廳之外的地面在此突然斷開，裂口深處泛著與上方光紋相呼應的淡色光帶。每當冷風自下吹上時，整片地穴都會跟著發出像遠鐘般的低鳴。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rift-depth",
      "coord": [4, 0, -7],
      "labels": ["chasm", "threshold"],
      "exits": [
        { "direction": "west", "to": 9494 },
        { "direction": "south", "to": 9497 },
        { "direction": "down", "to": 9499 }
      ],
      "enquires": ["出口", "深處", "異象"]
    },
    {
      "vnum": 9499,
      "name": "下層裂谷階",
      "description": "石階貼著裂谷內壁向下盤旋，腳邊偶爾會掠過一絲像流光又像霧影的淡線。再往更下方看去，只剩被冷光吞掉的深黑空間，像祕境真正的底層仍遠未結束。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rift-depth",
      "coord": [4, 0, -8],
      "labels": ["vertical", "future-depth"],
      "exits": [
        { "direction": "up", "to": 9498 }
      ],
      "enquires": ["退路", "下方"]
    }
  ]
}
```
