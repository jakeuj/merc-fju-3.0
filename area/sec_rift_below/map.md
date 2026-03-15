# 異象裂谷 (`sec_rift_below`)

## Area Intent

`sec_rift_below` 承接 `sec_catacomb_depths` 最深處裂谷石階的下方，把忘川地穴的「祕境入口」進一步推成真正的裂谷探索帶。這裡不再是帶有古墓殘痕的靈異地穴，而是地脈已經徹底失衡、風聲與冷光像有意識般沿裂壁流動的異象秘境。

第一版目標先固定：

- 一條由裂谷著階往深井沉門推進的主線
- 一條偏向祭痕石棧與晶槽殘痕的支線
- 一條 `down/up` 的更深秘境底層非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、裂風、深井與沉門判讀

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂谷 / 異象秘境`
- LevelRange: `30-42`
- Parent area: `sec_catacomb_depths`
- ReservedRoomBlock: `9501-9520`
- World gap filled: 把忘川地穴下方的更深異象裂谷 stub 轉成真正可規劃的第二層 secret zone，讓洛陽地下鏈在祕境入口之後還能延伸到更危險的裂谷深處

## Player Flow

1. 玩家從 `sec_catacomb_depths/9499` 向下時，會先感受到裂谷由「可辨識的階道」轉成必須貼壁下行的失衡路徑。
2. 主線沿著風脊、裂潭與深井口向內推進，逐步把靈異地穴探索轉成真正的異象裂谷探索。
3. 支線透過祭痕石棧、晶槽與觀台補 lore 線索與高風險獎勵感。
4. 深井沉門以下以 `down` 預留更深層裂谷心核或祕境底層。

## Cluster Notes

### `entry-descent`

- 房間重點：裂谷著階、回音落橋
- 玩家感受：剛離開忘川地穴，退路仍在，但空間感已完全失衡
- 對外角色：承接 `sec_catacomb_depths/9499`

### `rift-mainline`

- 房間重點：浮紋風脊、冷光裂潭、懸磴岔壁
- 玩家感受：危險、空曠、像正在穿過有意志的裂谷主脈
- 對外角色：作為 deeper secret zone 主線探索帶

### `ritual-ledge`

- 房間重點：霧瀑背廊、祭痕石棧、斷脈晶槽、裂風觀台
- 玩家感受：高風險高回報、像有人曾在裂谷中試圖控制異象
- 對外角色：提供獎勵感、線索感與秘境 lore

### `abyss-gate`

- 房間重點：異鳴深井口、井下浮階、祕境沉門
- 玩家感受：壓迫、稀有、像祕境真正底層仍在更下方
- 對外角色：作為未來裂谷心核 / 祕境底層入口 stub

## Planned World Links

- `up` from `9501`: planned link to `sec_catacomb_depths` room `9499`
- `down` from `9512`: planned continuation to `裂谷心核 / 祕境底層`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在裂谷著階、冷光裂潭、祭痕石棧與祕境沉門，讓玩家能問 `退路 / 裂風 / 深井 / 下方`
- `#Keyword` 第一版會落在風脊、裂潭、祭痕、晶槽、沉門，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
忘川地穴下層裂谷階(9499)
   |
[9501] 裂谷著階 -- [9502] 回音落橋 -- [9503] 浮紋風脊 -- [9504] 冷光裂潭 -- [9510] 異鳴深井口
                                                     |                                  |
                                                  [9505] 懸磴岔壁 -- [9506] 霧瀑背廊 -- [9507] 祭痕石棧 -- [9508] 斷脈晶槽 -- [9509] 裂風觀台
                                                                                                                |
                                                                                                             [9511] 井下浮階 -- [9512] 祕境沉門

[9512] down -> future rift core / secret floor
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_below",
    "title": "異象裂谷",
    "design_notes": "第一版 spec-first 草案。先固定忘川地穴下方的裂谷主線、祭痕支線與深井沉門入口。",
    "parent_area": "sec_catacomb_depths",
    "level_range": "30-42",
    "planned_vnum_range": "9501-9520",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂谷 / 異象秘境"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9501,
        "target_area": "sec_catacomb_depths",
        "target_room_vnum": 9499,
        "label": "下層裂谷階"
      },
      {
        "direction": "down",
        "source_vnum": 9512,
        "target_area": "sec_rift_core",
        "label": "裂谷心核"
      }
    ],
    "clusters": [
      { "id": "entry-descent", "label": "著階與回音落橋" },
      { "id": "rift-mainline", "label": "裂谷主線" },
      { "id": "ritual-ledge", "label": "祭痕與晶槽支線" },
      { "id": "abyss-gate", "label": "深井與沉門" }
    ]
  },
  "rooms": [
    {
      "vnum": 9501,
      "name": "裂谷著階",
      "description": "石階在這裡徹底失去規矩，變成貼著裂壁勉強延伸的窄階。頭頂還能隱約看見忘川地穴的冷光線影，但下方風聲已像從更深井口倒灌上來，帶著讓人胸口發緊的低鳴。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-descent",
      "coord": [0, 0, -9],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9499, "external": true },
        { "direction": "east", "to": 9502 }
      ],
      "enquires": ["退路", "下方"]
    },
    {
      "vnum": 9502,
      "name": "回音落橋",
      "description": "斷裂石橋只剩中段還勉強連著兩側崖壁，腳步一落下，聲音就會被裂谷深處一層層反送回來。每一道回音都比上一道更陌生，像有別的東西在模仿你的步伐。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-descent",
      "coord": [1, 0, -9],
      "labels": ["bridge", "echo"],
      "exits": [
        { "direction": "west", "to": 9501 },
        { "direction": "east", "to": 9503 }
      ],
      "keywords": [
        {
          "keyword": "回音",
          "description": "回音不是單純延遲的聲波，更像裂谷本身正用另一種節奏把聲音吐還回來。"
        }
      ]
    },
    {
      "vnum": 9503,
      "name": "浮紋風脊",
      "description": "一道貼壁延伸的狹長風脊懸在裂谷之中，石面上浮著像水紋般不斷位移的淡色紋路。風沿著紋路滑過時，會帶起細小冷光，像整條路正在被某種力量暫時托住。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rift-mainline",
      "coord": [2, 0, -9],
      "labels": ["wind", "mainline"],
      "exits": [
        { "direction": "west", "to": 9502 },
        { "direction": "east", "to": 9504 },
        { "direction": "south", "to": 9505 }
      ],
      "keywords": [
        {
          "keyword": "風脊",
          "description": "風脊像被風與地脈共同磨成的一道細梁，細得令人懷疑它隨時會被下一陣異風削斷。"
        }
      ],
      "enquires": ["裂風", "前路"]
    },
    {
      "vnum": 9504,
      "name": "冷光裂潭",
      "description": "裂壁在這裡內凹成一座半封閉石潭，潭中沒有水，只有一層像液體般緩慢起伏的淡色冷光。站得越久，越難分辨那光是在潭底流動，還是正從更深處往上滲出。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rift-mainline",
      "coord": [3, 0, -9],
      "labels": ["pool", "anomaly"],
      "exits": [
        { "direction": "west", "to": 9503 },
        { "direction": "east", "to": 9510 }
      ],
      "enquires": ["冷光", "裂谷"]
    },
    {
      "vnum": 9505,
      "name": "懸磴岔壁",
      "description": "岔壁間垂著幾段不完整的石磴，像是有人曾想在裂谷中鑿出可長行的支路，卻只留下半截可踩的突緣。風從下方抽過時，這些石磴會一起發出極輕的顫聲。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-ledge",
      "coord": [2, -1, -9],
      "labels": ["branch", "ledge"],
      "exits": [
        { "direction": "north", "to": 9503 },
        { "direction": "east", "to": 9506 }
      ]
    },
    {
      "vnum": 9506,
      "name": "霧瀑背廊",
      "description": "一層極細的白霧自上方裂壁無聲垂落，像瀑卻不見水勢，從背後望去只能看見霧幕後有幾道殘破刻痕若隱若現。走近時，皮膚會感到像細針般的冷麻。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-ledge",
      "coord": [3, -1, -9],
      "labels": ["mist", "corridor"],
      "exits": [
        { "direction": "west", "to": 9505 },
        { "direction": "east", "to": 9507 }
      ],
      "keywords": [
        {
          "keyword": "霧瀑",
          "description": "白霧不像單純濕氣，更像裂谷把冷意磨成了看得見的薄幕。"
        }
      ]
    },
    {
      "vnum": 9507,
      "name": "祭痕石棧",
      "description": "石棧邊緣刻著一圈圈早已磨損的祭痕，像有人曾在這裡試圖向裂谷深處獻上什麼。刻痕之間仍卡著細碎晶粉，每當風壓改變，就會閃出一瞬間幾乎看不見的淡芒。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-ledge",
      "coord": [4, -1, -9],
      "labels": ["ritual", "reward-hint"],
      "exits": [
        { "direction": "west", "to": 9506 },
        { "direction": "east", "to": 9508 }
      ],
      "keywords": [
        {
          "keyword": "祭痕",
          "description": "祭痕不像宗廟儀式留下的工整刻線，更像臨時在危險之地匆忙劃出的鎮壓與祈求符記。"
        }
      ],
      "enquires": ["祭痕", "裂谷"]
    },
    {
      "vnum": 9508,
      "name": "斷脈晶槽",
      "description": "數條細長晶槽嵌在石壁中，原本應該導引某種穩定流向，如今卻只剩斷續流竄的冷色微芒。每一道光在槽內折返時，都像在試圖尋找已經消失的出口。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-ledge",
      "coord": [5, -1, -9],
      "labels": ["crystal", "lore"],
      "exits": [
        { "direction": "west", "to": 9507 },
        { "direction": "east", "to": 9509 },
        { "direction": "north", "to": 9511 }
      ],
      "keywords": [
        {
          "keyword": "晶槽",
          "description": "晶槽切面平整得過於人工，讓人懷疑裂谷裡曾有某種真正成形的引流設施。"
        }
      ]
    },
    {
      "vnum": 9509,
      "name": "裂風觀台",
      "description": "觀台懸在裂谷外側，腳下就是深不見底的黑空。每次裂風掠過時，遠方幾道冷光會短暫勾出下層輪廓，像某座更大的門扉正沉在黑暗深處等待再次開啟。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-ledge",
      "coord": [6, -1, -9],
      "labels": ["view", "risk"],
      "exits": [
        { "direction": "west", "to": 9508 }
      ],
      "enquires": ["裂風", "下方"]
    },
    {
      "vnum": 9510,
      "name": "異鳴深井口",
      "description": "主線在此收束成一道筆直向下的深井，井壁每隔片刻就會傳出極低的共鳴，像下方有巨大空腔正緩慢呼吸。井口周圍的石面布滿被風與冷光共同侵蝕出的細密溝痕。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-gate",
      "coord": [4, 0, -9],
      "labels": ["shaft", "threshold"],
      "exits": [
        { "direction": "west", "to": 9504 },
        { "direction": "down", "to": 9511 }
      ],
      "enquires": ["深井", "下方"]
    },
    {
      "vnum": 9511,
      "name": "井下浮階",
      "description": "井壁內側浮著一圈圈彼此錯落的石階，像不是砌成，而是被下方異象一層層托起。每走一步，都能感到腳下傳來極輕的震動，彷彿更深處有什麼正在持續脈動。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-gate",
      "coord": [4, 0, -10],
      "labels": ["downstairs", "vertical"],
      "exits": [
        { "direction": "up", "to": 9510 },
        { "direction": "east", "to": 9512 },
        { "direction": "south", "to": 9508 }
      ]
    },
    {
      "vnum": 9512,
      "name": "祕境沉門",
      "description": "沉門半埋在裂谷底部石層之中，門面沒有紋飾，只有一道像被黑夜壓縮後留下的狹細門縫。冷光到了這裡反而變得稀薄，彷彿真正該發亮的東西全被門後吞了進去。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-gate",
      "coord": [5, 0, -10],
      "labels": ["gate", "deep-link"],
      "exits": [
        { "direction": "west", "to": 9511 }
      ],
      "keywords": [
        {
          "keyword": "沉門",
          "description": "沉門不像人工打造的陵墓門扉，更像裂谷最深處自行凝成的一道邊界。"
        }
      ],
      "enquires": ["沉門", "下方", "出口"]
    }
  ]
}
```
