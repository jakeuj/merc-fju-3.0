# 封印核心 (`sec_rift_prison_core`)

## Area Intent

`sec_rift_prison_core` 承接 `sec_rift_nadir` 最深處的禁牢界井下方，將前段禁牢探索推進成真正承受封印主體反衝的核心鎮封帶。這裡已不只是能看見封印痕跡的深界禁牢，而是整座裂界最重要的鎮壓結構、維持者遺痕與下方本核回應同時匯聚的深層心獄。

第一版目標先固定：

- 一條由井心落點進入鎮封主廊的主線
- 一條偏向護印旁室與監封裂壇的支線
- 一條 `down/up` 的更深鎮封非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、封印、心獄與井心判讀

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `禁牢 / 封印核心`
- LevelRange: `56-70`
- Parent area: `sec_rift_nadir`
- ReservedRoomBlock: `10001-10020`
- World gap filled: 把裂界禁牢下方的封印核心 stub 轉成真正可規劃的心獄區，讓洛陽地下鏈在禁牢之後形成更明確的核心鎮封節點

## Player Flow

1. 玩家從 `sec_rift_nadir/9912` 向下時，會先感受到原本沉重的禁文低鳴被壓縮成近乎心跳的震動，像整座裂界真正的核心正在腳下緩慢起伏。
2. 主線沿著井臺、鎮封主廊與裂橋向內推進，逐步把禁牢探索轉成直面封印本體的核心探索。
3. 支線透過護印旁室、血紋鎮壁與監封裂壇補 lore 線索與高風險獎勵感。
4. 最深處的封印井心以 `down` 預留更深層鎮封底座或裂界本核。

## Cluster Notes

### `core-threshold`

- 房間重點：灰黯井臺、鎮鏈斜道
- 玩家感受：剛穿過禁牢界井，退路尚可辨識，但空氣像被整層封印壓成極重的靜止
- 對外角色：承接 `sec_rift_nadir/9912`

### `seal-mainline`

- 房間重點：心獄前廊、鎮脈直橋、崩印觀臺
- 玩家感受：壓迫、稀有、像正走進一座仍勉力維持運轉的核心鎮封機構
- 對外角色：作為封印核心主線探索帶

### `ward-annex`

- 房間重點：界鎖圓庭、護印旁室、血紋鎮壁、灰燼裂壇、觀獄側座
- 玩家感受：高風險高回報、像過去長年有人在此監封、修補並承擔反衝
- 對外角色：提供封印 lore、風險提示與深層監牢感

### `heart-boundary`

- 房間重點：沉鎖井階、封印井心
- 玩家感受：危險、沉重、像真正的裂界本核已近在腳下
- 對外角色：作為未來鎮封底座 / 裂界本核入口 stub

## Planned World Links

- `up` from `10001`: planned link to `sec_rift_nadir` room `9912`
- `down` from `10012`: planned continuation to `鎮封底座 / 裂界本核`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在灰黯井臺、界鎖圓庭、崩印觀臺與封印井心，讓玩家能問 `退路 / 封印 / 心獄 / 下層`
- `#Keyword` 第一版會落在鎮鏈、界鎖、血紋、裂壇、井心，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
裂界禁牢界井(9912)
   |
[10001] 灰黯井臺 -- [10002] 鎮鏈斜道 -- [10003] 心獄前廊 -- [10004] 鎮脈直橋 -- [10010] 崩印觀臺
                                                       |
                                                    [10005] 界鎖圓庭 -- [10006] 護印旁室 -- [10007] 血紋鎮壁 -- [10008] 灰燼裂壇 -- [10009] 觀獄側座
                                                                                                                                       |
                                                                                                                                     down
                                                                                                                                       |
                                                                                                                                    [10011] 沉鎖井階
                                                                                                                                       |
                                                                                                                                     down
                                                                                                                                       |
                                                                                                                                    [10012] 封印井心

[10012] down -> future underseal dais / rift true core
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_prison_core",
    "title": "封印核心",
    "design_notes": "第一版 spec-first 草案。先固定裂界禁牢下方的封印核心主線、護印支線與井心入口。",
    "parent_area": "sec_rift_nadir",
    "level_range": "56-70",
    "planned_vnum_range": "10001-10020",
    "reserved_room_block": "10001-10020",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "禁牢 / 封印核心"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10001,
        "target_area": "sec_rift_nadir",
        "target_room_vnum": 9912,
        "label": "禁牢界井"
      },
      {
        "direction": "down",
        "source_vnum": 10012,
        "target_area": "future_rift_underseal",
        "label": "封印井心"
      }
    ],
    "clusters": [
      { "id": "core-threshold", "label": "井心前帶" },
      { "id": "seal-mainline", "label": "鎮封主線" },
      { "id": "ward-annex", "label": "護印支線" },
      { "id": "heart-boundary", "label": "井心邊界" }
    ]
  },
  "rooms": [
    {
      "vnum": 10001,
      "name": "灰黯井臺",
      "description": "落點是一圈被黯灰石塊勉強托住的井臺，腳下每一道裂縫都滲出極淡紅光，像地底有心脈正透過石層緩慢搏動。抬頭只能看見上方界井留下的一線黑影，四周卻早已被更深層的靜壓包住。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core-threshold",
      "coord": [0, 0, -16],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9912, "external": true },
        { "direction": "east", "to": 10002 }
      ],
      "enquires": ["退路", "封印"]
    },
    {
      "vnum": 10002,
      "name": "鎮鏈斜道",
      "description": "斜道沿著井壁緩緩往前延展，兩側嵌著粗重鎮鏈與斷裂鐵環，像原本是用來承受更劇烈震動的固定結構。每當腳步落下，整條斜道都會回傳一陣沉悶震顫，像某種更深的力量正隔著石壁回應。",
      "sector_type": "SECT_INSIDE",
      "cluster": "core-threshold",
      "coord": [1, 0, -16],
      "labels": ["corridor", "chain"],
      "exits": [
        { "direction": "west", "to": 10001 },
        { "direction": "east", "to": 10003 }
      ],
      "keywords": [
        {
          "keyword": "鎮鏈",
          "description": "鎮鏈表面佈滿深刻磨痕，顯示它們長年在承受超出常理的拉扯。"
        }
      ]
    },
    {
      "vnum": 10003,
      "name": "心獄前廊",
      "description": "前廊兩側排列著殘缺的界柱，柱面刻紋彼此相扣，把整條通道壓成一種近乎無聲的狀態。站在此處，能感覺到呼吸與心跳都被迫順著深處傳來的脈律慢慢對齊，像這裡本來就不容任何雜音存在。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-mainline",
      "coord": [2, 0, -16],
      "labels": ["mainline", "seal"],
      "exits": [
        { "direction": "west", "to": 10002 },
        { "direction": "east", "to": 10004 },
        { "direction": "south", "to": 10005 }
      ],
      "enquires": ["封印", "前路"]
    },
    {
      "vnum": 10004,
      "name": "鎮脈直橋",
      "description": "直橋橫跨一道看不見底的黑縫，橋面每隔數步就嵌著仍在微亮的鎮脈石釘。它們不像普通橋梁構件，更像整條橋本身就是某個巨大鎮封陣的一節筋骨，正在勉強維持下方不被撕開。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-mainline",
      "coord": [3, 0, -16],
      "labels": ["bridge", "core"],
      "exits": [
        { "direction": "west", "to": 10003 },
        { "direction": "east", "to": 10010 }
      ],
      "enquires": ["鎮脈", "下層"]
    },
    {
      "vnum": 10005,
      "name": "界鎖圓庭",
      "description": "圓庭中央是一座層層下陷的石盤，盤面刻滿對稱界紋，四周則留著許多曾被替換過器具的痕跡。那些痕跡凌亂卻不慌亂，像過去的守印者在這裡反覆校正封印，直到再也沒有餘力回來。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ward-annex",
      "coord": [2, -1, -16],
      "labels": ["lore", "seal"],
      "exits": [
        { "direction": "north", "to": 10003 },
        { "direction": "east", "to": 10006 }
      ],
      "keywords": [
        {
          "keyword": "界鎖",
          "description": "盤面中央的界鎖紋彼此牽連，顯示這裡不是普通祭壇，而是鎮封主體的一個調律節點。"
        }
      ],
      "enquires": ["封印", "心獄"]
    },
    {
      "vnum": 10006,
      "name": "護印旁室",
      "description": "旁室靠牆留著整齊的石櫃與空缺支架，還能看見補給與器物曾被仔細分類的痕跡。牆上的灰痕一層壓一層，像有人在漫長歲月裡反覆回到這裡休整，再獨自走回更深的井心。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ward-annex",
      "coord": [3, -1, -16],
      "labels": ["supply", "guide"],
      "exits": [
        { "direction": "west", "to": 10005 },
        { "direction": "east", "to": 10007 }
      ],
      "keywords": [
        {
          "keyword": "石櫃",
          "description": "石櫃邊角佈滿被重物長期拖放的磨痕，顯示這裡原本就是守印者的補給與整備處。"
        }
      ],
      "enquires": ["補給", "退路"]
    },
    {
      "vnum": 10007,
      "name": "血紋鎮壁",
      "description": "高壁被一層層深紅紋痕覆住，像有人曾以自身精血硬把禁紋補上。那些痕跡如今早已乾硬發黑，卻仍能在深處震動傳來時泛起微光，讓人不寒而慄地意識到封印能維持至今代價極大。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ward-annex",
      "coord": [4, -1, -16],
      "labels": ["risk", "seal"],
      "exits": [
        { "direction": "west", "to": 10006 },
        { "direction": "east", "to": 10008 }
      ],
      "keywords": [
        {
          "keyword": "血紋",
          "description": "血紋早已凝成石色的一部分，顯示當年的補封不是短暫權宜，而是拿命換來的延續。"
        }
      ],
      "enquires": ["血紋", "封印"]
    },
    {
      "vnum": 10008,
      "name": "灰燼裂壇",
      "description": "裂壇像被一股無法承受的衝擊從中央炸開，壇面與地面堆滿暗灰碎屑。碎屑下仍可辨認出繁複鎮印輪廓，彷彿這裡原本是最後一道監封程序的施作點，只是某次再也沒有撐住。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ward-annex",
      "coord": [5, -1, -16],
      "labels": ["altar", "danger"],
      "exits": [
        { "direction": "west", "to": 10007 },
        { "direction": "east", "to": 10009 }
      ],
      "keywords": [
        {
          "keyword": "裂壇",
          "description": "壇面裂口深得不像自然崩壞，更像有某種來自下方的力量直接穿透了鎮印。"
        }
      ],
      "enquires": ["裂壇", "鎮印"]
    },
    {
      "vnum": 10009,
      "name": "觀獄側座",
      "description": "側座嵌在石壁內側，前方保留著幾道能俯看井心前帶的狹長視口。坐在這裡時，可以同時看到鎮壁血紋的明滅與深處井階的微動，像這裡原本就是專門觀測封印是否即將失守的地方。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ward-annex",
      "coord": [6, -1, -16],
      "labels": ["observation", "lore"],
      "exits": [
        { "direction": "west", "to": 10008 },
        { "direction": "down", "to": 10011 }
      ],
      "enquires": ["觀獄", "井心"]
    },
    {
      "vnum": 10010,
      "name": "崩印觀臺",
      "description": "觀臺原本應是監看主橋與井心的高點，如今邊緣卻被撕裂出大片缺口，只剩斷裂欄座與傾斜石板。站在此處，能清楚感覺整片地面都在隨著下方某種巨大存在的起伏而極緩地顫動。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-mainline",
      "coord": [4, 0, -16],
      "labels": ["well", "depth"],
      "exits": [
        { "direction": "west", "to": 10004 },
        { "direction": "south", "to": 10011 }
      ],
      "enquires": ["井心", "下層"]
    },
    {
      "vnum": 10011,
      "name": "沉鎖井階",
      "description": "井階沿著井壁盤旋下沉，每一階都壓著粗重鎖環與失色符片，腳下像踩在某種仍勉強有效的鎮壓程序上。越往下走，周圍空氣越像被看不見的力量向內壓縮，讓人連呼吸都得放得極慢。",
      "sector_type": "SECT_INSIDE",
      "cluster": "heart-boundary",
      "coord": [4, -1, -17],
      "labels": ["stairs", "boundary"],
      "exits": [
        { "direction": "north", "to": 10010 },
        { "direction": "up", "to": 10009 },
        { "direction": "down", "to": 10012 }
      ],
      "enquires": ["退路", "井心"]
    },
    {
      "vnum": 10012,
      "name": "封印井心",
      "description": "井心是一片像被整座深界硬壓出來的圓形空場，中央懸著一團近乎靜止的暗紅光核，周圍則環繞著數十道忽明忽滅的斷裂鎮印。它不像單純的封印節點，更像某種巨大存在被迫縮束後留下的表面，任何注視都會讓人誤以為那團光核也正在回望。",
      "sector_type": "SECT_INSIDE",
      "cluster": "heart-boundary",
      "coord": [4, -2, -18],
      "labels": ["world-link-down", "boss-threshold"],
      "exits": [
        { "direction": "up", "to": 10011 }
      ],
      "keywords": [
        {
          "keyword": "井心",
          "description": "井心並不平靜，那種近乎停止的脈動反而更像被極端力量強行按住後留下的餘波。"
        }
      ],
      "enquires": ["封印", "下層"]
    }
  ]
}
```
