# 裂谷心核 (`sec_rift_core`)

## Area Intent

`sec_rift_core` 承接 `sec_rift_below` 最深處的祕境沉門下方，把異象裂谷的「底層入口」進一步推成真正的心核區。這裡不再只是裂風與冷光交會的危險裂谷，而是整條地脈異象真正收束、脈動與失衡都變得具體可感的底層核心。

第一版目標先固定：

- 一條由沉門後前帶進入心核主廊的主線
- 一條偏向晶脈殘層與鎮界痕跡的支線
- 一條 `down/up` 的更深裂界非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、心核、封界與下層判讀

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `心核 / 裂谷底層`
- LevelRange: `36-50`
- Parent area: `sec_rift_below`
- ReservedRoomBlock: `9601-9620`
- World gap filled: 把異象裂谷下方的裂谷心核 stub 轉成真正可規劃的底層核心區，讓洛陽地下鏈在裂谷之後形成一個高風險核心節點

## Player Flow

1. 玩家從 `sec_rift_below/9512` 向下時，會先感受到裂谷的空曠風壓消失，取而代之的是像心跳般規律的地脈脈動。
2. 主線沿著沉門後前帶、心核主廊與脈動核心向內推進，逐步把裂谷探索轉成底層核心探索。
3. 支線透過晶脈殘層、鎮界台與回聲槽補 lore 線索與獎勵感。
4. 最深處的裂界下井以 `down` 預留更深層心核底井或裂界深層。

## Cluster Notes

### `gate-antechamber`

- 房間重點：沉門後前帶、回脈折道
- 玩家感受：剛離開裂谷沉門，退路仍在，但環境已變得過於安靜與規律
- 對外角色：承接 `sec_rift_below/9512`

### `core-mainline`

- 房間重點：脈動主廊、心核環橋、靜鳴晶庭
- 玩家感受：壓迫、稀有、像正走進地脈本身的心室
- 對外角色：作為裂谷心核主線探索帶

### `seal-side`

- 房間重點：回聲槽、鎮界台、碎界晶層、斷環觀座
- 玩家感受：高風險高回報、像過去有人在此勉強封住更深層的東西
- 對外角色：提供鎮壓痕跡、獎勵感與核心 lore

### `deep-boundary`

- 房間重點：裂界下井、底層封界
- 玩家感受：危險、沉重、像真正不能輕易開啟的更深層就在腳下
- 對外角色：作為未來心核底井 / 裂界深層入口 stub

## Planned World Links

- `up` from `9601`: planned link to `sec_rift_below` room `9512`
- `down` from `9612`: planned continuation to `心核底井 / 裂界深層`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在沉門後前帶、靜鳴晶庭、鎮界台與底層封界，讓玩家能問 `退路 / 心核 / 封界 / 下層`
- `#Keyword` 第一版會落在脈動、晶層、鎮界、封界、下井，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
異象裂谷祕境沉門(9512)
   |
[9601] 沉門後前帶 -- [9602] 回脈折道 -- [9603] 脈動主廊 -- [9604] 心核環橋 -- [9610] 裂界下井
                                                     |                                  |
                                                  [9605] 靜鳴晶庭 -- [9606] 回聲槽 -- [9607] 鎮界台 -- [9608] 碎界晶層 -- [9609] 斷環觀座
                                                                                         |
                                                                                      [9611] 下井浮磴 -- [9612] 底層封界

[9612] down -> future core well / deeper boundary
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core",
    "title": "裂谷心核",
    "design_notes": "第一版 spec-first 草案。先固定異象裂谷下方的心核主線、鎮界支線與底層封界入口。",
    "parent_area": "sec_rift_below",
    "level_range": "36-50",
    "planned_vnum_range": "9601-9620",
    "theme": {
      "primary": "仙俠",
      "secondary": "心核 / 裂谷底層"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9601,
        "target_area": "sec_rift_below",
        "target_room_vnum": 9512,
        "label": "祕境沉門"
      },
      {
        "direction": "down",
        "source_vnum": 9612,
        "target_area": "sec_rift_deeps",
        "label": "心核底井"
      }
    ],
    "clusters": [
      { "id": "gate-antechamber", "label": "沉門後前帶" },
      { "id": "core-mainline", "label": "心核主線" },
      { "id": "seal-side", "label": "鎮界支線" },
      { "id": "deep-boundary", "label": "下井與封界" }
    ]
  },
  "rooms": [
    {
      "vnum": 9601,
      "name": "沉門後前帶",
      "description": "沉門後方不是想像中的黑暗甬道，而是一段過於平整的石帶，地面每隔片刻便會傳出一次像心跳般的微震。回頭仍能看見上方沉門的狹細門縫，但前方空氣已像被某種規律緩慢牽引。",
      "sector_type": "SECT_INSIDE",
      "cluster": "gate-antechamber",
      "coord": [0, 0, -11],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9512, "external": true },
        { "direction": "east", "to": 9602 }
      ],
      "enquires": ["退路", "心核"]
    },
    {
      "vnum": 9602,
      "name": "回脈折道",
      "description": "折道兩側石壁布滿一圈圈向內收束的細紋，像整段通道都在替更深處的脈動回收外散的力量。走在這裡時，連呼吸都會不自覺跟著某種拍點放慢。",
      "sector_type": "SECT_INSIDE",
      "cluster": "gate-antechamber",
      "coord": [1, 0, -11],
      "labels": ["corridor", "pulse"],
      "exits": [
        { "direction": "west", "to": 9601 },
        { "direction": "east", "to": 9603 }
      ]
    },
    {
      "vnum": 9603,
      "name": "脈動主廊",
      "description": "主廊中央每隔幾步就有一道向上微鼓的石脊，像有看不見的搏動正從地底一節節傳上來。廊內沒有風，卻總有細小晶塵在半空緩慢偏移，彷彿整片空間都被心核脈流輕輕推動。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core-mainline",
      "coord": [2, 0, -11],
      "labels": ["mainline", "pulse"],
      "exits": [
        { "direction": "west", "to": 9602 },
        { "direction": "east", "to": 9604 },
        { "direction": "south", "to": 9605 }
      ],
      "keywords": [
        {
          "keyword": "脈動",
          "description": "這股脈動不像自然地震，更像某種活著的核心正在用極慢的節奏呼吸。"
        }
      ],
      "enquires": ["心核", "前路"]
    },
    {
      "vnum": 9604,
      "name": "心核環橋",
      "description": "環橋繞著一座看不見底的中空井心盤旋，橋下只有一層層被冷光照亮的霧。每當脈動傳到此處，整座橋面便會浮出一瞬即逝的淡紋，像橋本身也只是心核外層的一部分。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core-mainline",
      "coord": [3, 0, -11],
      "labels": ["bridge", "core"],
      "exits": [
        { "direction": "west", "to": 9603 },
        { "direction": "east", "to": 9610 }
      ],
      "enquires": ["心核", "下層"]
    },
    {
      "vnum": 9605,
      "name": "靜鳴晶庭",
      "description": "晶庭中豎著幾根不再發亮的細長晶柱，柱面卻仍不時泛起極淡的環紋。這裡安靜得近乎異常，唯有把手掌貼近晶柱時，才會感到一股像遠鐘尾音般的低微回鳴。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-side",
      "coord": [2, -1, -11],
      "labels": ["crystal", "side"],
      "exits": [
        { "direction": "north", "to": 9603 },
        { "direction": "east", "to": 9606 }
      ],
      "keywords": [
        {
          "keyword": "晶柱",
          "description": "晶柱表面布滿細緻裂痕，像它們原本承受過遠比現在更猛烈的脈流。"
        }
      ]
    },
    {
      "vnum": 9606,
      "name": "回聲槽",
      "description": "牆邊嵌著數道半圓形槽溝，像是專門用來導走某種聲波或脈流的舊裝置。當核心脈動經過時，槽內會先後亮起細光，像在替更深處的封界計算某種仍未停下的節律。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-side",
      "coord": [3, -1, -11],
      "labels": ["echo", "lore"],
      "exits": [
        { "direction": "west", "to": 9605 },
        { "direction": "east", "to": 9607 }
      ]
    },
    {
      "vnum": 9607,
      "name": "鎮界台",
      "description": "台面邊緣刻著彼此咬合的鎮界刻紋，中央則留有一圈早已空掉的安置槽。看起來像有人曾把某件關鍵器物放在這裡，強行維持底層封界不至於立刻鬆脫。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-side",
      "coord": [4, -1, -11],
      "labels": ["seal", "reward-hint"],
      "exits": [
        { "direction": "west", "to": 9606 },
        { "direction": "east", "to": 9608 }
      ],
      "keywords": [
        {
          "keyword": "鎮界",
          "description": "鎮界刻紋殘缺卻仍維持著某種秩序，顯示這裡的封印從未真正完全失效。"
        }
      ],
      "enquires": ["封界", "鎮界"]
    },
    {
      "vnum": 9608,
      "name": "碎界晶層",
      "description": "大片半透明晶層像被外力硬生生剝離後又重新凝住，層面之間夾著細碎黑線，像更深處某種東西曾試圖從這裡往上推開世界的邊界。每一道裂紋都在冷光下顯得過分清楚。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-side",
      "coord": [5, -1, -11],
      "labels": ["fracture", "risk"],
      "exits": [
        { "direction": "west", "to": 9607 },
        { "direction": "east", "to": 9609 },
        { "direction": "north", "to": 9611 }
      ],
      "keywords": [
        {
          "keyword": "晶層",
          "description": "晶層切面過於平整，像它們不是自然生長，而是曾被某種規律強迫排列成封界的一部分。"
        }
      ]
    },
    {
      "vnum": 9609,
      "name": "斷環觀座",
      "description": "觀座原本應該是一座完整環台，如今只剩半圈還附著在壁面上。從這裡往外看去，可以同時看到心核環橋與晶層裂面，像過去曾有人專門在此監看整個底層核心的穩定度。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-side",
      "coord": [6, -1, -11],
      "labels": ["view", "lore"],
      "exits": [
        { "direction": "west", "to": 9608 }
      ],
      "enquires": ["封界", "下層"]
    },
    {
      "vnum": 9610,
      "name": "裂界下井",
      "description": "主線盡頭是一座向下筆直收束的井道，井壁內側偶爾會浮出一道像門框又像裂縫的暗紋。每當核心脈動傳到這裡，井下便會回傳更沉、更慢的一次震鳴，像有另一重心跳埋在更深處。",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-boundary",
      "coord": [4, 0, -11],
      "labels": ["shaft", "boundary"],
      "exits": [
        { "direction": "west", "to": 9604 },
        { "direction": "down", "to": 9611 }
      ],
      "enquires": ["下層", "裂界"]
    },
    {
      "vnum": 9611,
      "name": "下井浮磴",
      "description": "井道內側浮著幾塊彼此錯落的石磴，像只在脈動穩定時才會短暫顯出形體。每往下踩一步，都能感到腳底傳來比上層更沉的反震，彷彿你正在靠近某條被勉強壓住的界線。",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-boundary",
      "coord": [4, 0, -12],
      "labels": ["vertical", "stairs"],
      "exits": [
        { "direction": "up", "to": 9610 },
        { "direction": "east", "to": 9612 },
        { "direction": "south", "to": 9608 }
      ]
    },
    {
      "vnum": 9612,
      "name": "底層封界",
      "description": "封界像一整面沉在黑暗裡的石幕，表面沒有任何完整文字，只有一圈圈彼此交疊的斷紋與極淡冷芒。站在它前面時，會清楚感到更深處正有某種東西持續拍擊這道邊界，只是還沒真正突破出來。",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-boundary",
      "coord": [5, 0, -12],
      "labels": ["gate", "deep-link"],
      "exits": [
        { "direction": "west", "to": 9611 }
      ],
      "keywords": [
        {
          "keyword": "封界",
          "description": "這道封界不像門，也不像牆，更像有人把整段深層邊界本身硬生生留在了這裡。"
        }
      ],
      "enquires": ["封界", "下層", "出口"]
    }
  ]
}
```
