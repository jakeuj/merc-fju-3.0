# 裂界禁牢 (`sec_rift_nadir`)

## Area Intent

`sec_rift_nadir` 承接 `sec_rift_abyss` 最深處的禁底界井下方，將前段禁底探索推進成更深層的禁牢封印帶。這裡不再只是能感受到地脈脈動的底層核心，而是舊封印結構、裂界回音與被鎮住的異常存在同時留下痕跡的深層界域。

第一版目標先固定：

- 一條由界井落點進入封印回廊的主線
- 一條偏向禁制殘壇與鎮鎖痕跡的支線
- 一條 `down/up` 的更深裂界非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、封印、界井與禁牢判讀

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂界 / 深層封印`
- LevelRange: `52-66`
- Parent area: `sec_rift_abyss`
- ReservedRoomBlock: `9901-9920`
- World gap filled: 把裂界禁底下方的深層封印 stub 轉成真正可規劃的裂界禁牢區，讓洛陽地下鏈在禁底之後形成更明確的深層禁制節點

## Player Flow

1. 玩家從 `sec_rift_abyss/9812` 向下時，會先感受到原本規律的心核脈動被拉長成沉重回響，像整座裂界正在更深處緩慢應答。
2. 主線沿著界井落點、封印回廊與鎮鎖主帶向內推進，逐步把底層核心探索轉成真正的深層禁制探索。
3. 支線透過殘壇、鎖痕與觀界側室補 lore 線索與高風險獎勵感。
4. 最深處的禁牢界井以 `down` 預留更深層裂界禁牢或封印核心。

## Cluster Notes

### `well-descent`

- 房間重點：界井落點、回音石棧
- 玩家感受：剛穿過底層封界，退路尚可辨識，但環境已帶有明顯的禁制壓迫感
- 對外角色：承接 `sec_rift_abyss/9812`

### `seal-corridor`

- 房間重點：封印回廊、裂律長橋、界鳴內庭
- 玩家感受：壓迫、稀有、像走進一條仍在勉力運作的古老鎮界系統
- 對外角色：作為深層封印主線探索帶

### `forbidden-side`

- 房間重點：殘壇側室、鎮鎖壁、觀界偏座、禁紋裂面
- 玩家感受：高風險高回報、像過去有人持續監看並修補更深處的封印
- 對外角色：提供封印 lore、風險提示與獎勵感

### `abyss-boundary`

- 房間重點：墜界斷台、禁牢界井
- 玩家感受：危險、沉重、像真正不能被輕易喚醒的東西就鎮在更下方
- 對外角色：作為未來裂界禁牢 / 封印核心入口 stub

## Planned World Links

- `up` from `9901`: planned link to `sec_rift_abyss` room `9812`
- `down` from `9912`: planned continuation to `裂界禁牢 / 封印核心`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在界井落點、界鳴內庭、殘壇側室與禁牢界井，讓玩家能問 `退路 / 封印 / 鎮界 / 下層`
- `#Keyword` 第一版會落在鎖紋、殘壇、界井、裂面、禁紋，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
裂界禁底界井(9812)
   |
[9901] 界井落點 -- [9902] 回音石棧 -- [9903] 封印回廊 -- [9904] 裂律長橋 -- [9910] 墜界斷台
                                                     |                                  |
                                                  [9905] 界鳴內庭 -- [9906] 殘壇側室 -- [9907] 鎮鎖壁 -- [9908] 禁紋裂面 -- [9909] 觀界偏座
                                                                                         |
                                                                                       down
                                                                                         |
                                                                                      [9911] 井緣浮階
                                                                                         |
                                                                                       down
                                                                                         |
                                                                                      [9912] 禁牢界井

[9912] down -> future rift prison core
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_nadir",
    "title": "裂界禁牢",
    "design_notes": "第一版 spec-first 草案。先固定裂界禁底下方的禁牢封印主線、禁制支線與禁牢界井入口。",
    "parent_area": "sec_rift_abyss",
    "level_range": "52-66",
    "planned_vnum_range": "9901-9920",
    "reserved_room_block": "9901-9920",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂界 / 深層封印"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9901,
        "target_area": "sec_rift_abyss",
        "target_room_vnum": 9812,
        "label": "底層封界"
      },
      {
        "direction": "down",
        "source_vnum": 9912,
        "target_area": "future_rift_prison_core",
        "label": "禁牢界井"
      }
    ],
    "clusters": [
      { "id": "well-descent", "label": "界井前帶" },
      { "id": "seal-corridor", "label": "封印主線" },
      { "id": "forbidden-side", "label": "禁制支線" },
      { "id": "abyss-boundary", "label": "禁牢界井" }
    ]
  },
  "rooms": [
    {
      "vnum": 9901,
      "name": "界井落點",
      "description": "自上方封界落下後，腳下是一片由黑灰石板拼出的狹窄井臺，周圍霧氣不再流動，而像被某種沉重法則壓在原地。抬頭仍能看見細細一線冷光垂落，但下方與前方都已被更深的回音包圍。",
      "sector_type": "SECT_INSIDE",
      "cluster": "well-descent",
      "coord": [0, 0, -13],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9812, "external": true },
        { "direction": "east", "to": 9902 }
      ],
      "enquires": ["退路", "封印"]
    },
    {
      "vnum": 9902,
      "name": "回音石棧",
      "description": "石棧像貼著裂壁硬生生削出的一線走道，腳步聲會在下方空洞裡被拖得極長，最後變成不像自己的回響。壁面佈滿細小環紋，像每一次回音都會被某種禁制重新收束。",
      "sector_type": "SECT_INSIDE",
      "cluster": "well-descent",
      "coord": [1, 0, -13],
      "labels": ["corridor", "echo"],
      "exits": [
        { "direction": "west", "to": 9901 },
        { "direction": "east", "to": 9903 }
      ]
    },
    {
      "vnum": 9903,
      "name": "封印回廊",
      "description": "回廊兩側立著半埋入石中的殘柱，每根柱面都還留著彼此呼應的封印紋。那些紋路明明已缺損，卻仍會在遠處界井微震時依序亮起，像一座龐大的鎮界系統仍在勉強運行。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-corridor",
      "coord": [2, 0, -13],
      "labels": ["mainline", "seal"],
      "exits": [
        { "direction": "west", "to": 9902 },
        { "direction": "east", "to": 9904 },
        { "direction": "south", "to": 9905 }
      ],
      "keywords": [
        {
          "keyword": "封印紋",
          "description": "紋路彼此銜接成完整迴路，顯示這裡原本就是為了把更深處的異常長久鎖在下方。"
        }
      ],
      "enquires": ["封印", "前路"]
    },
    {
      "vnum": 9904,
      "name": "裂律長橋",
      "description": "長橋跨在看不見底的裂口上方，橋面每隔數步便嵌著一道細窄金屬鎖條。它們隨著遠處低鳴不時微微收縮，像橋本身不只是道路，而是整座深層封印的一節鎮鎖。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-corridor",
      "coord": [3, 0, -13],
      "labels": ["bridge", "seal"],
      "exits": [
        { "direction": "west", "to": 9903 },
        { "direction": "east", "to": 9910 }
      ],
      "enquires": ["鎮界", "下層"]
    },
    {
      "vnum": 9905,
      "name": "界鳴內庭",
      "description": "內庭中央立著一座已開裂的圓形石盤，盤面上的紋圈會在低鳴傳來時緩慢浮亮。周圍空氣沉得像水，連呼吸都像被迫順著某種古老節律進行，讓人不自覺想知道更深處到底鎮著什麼。",
      "sector_type": "SECT_INSIDE",
      "cluster": "seal-corridor",
      "coord": [2, -1, -13],
      "labels": ["core", "lore"],
      "exits": [
        { "direction": "north", "to": 9903 },
        { "direction": "east", "to": 9906 }
      ],
      "keywords": [
        {
          "keyword": "石盤",
          "description": "石盤邊緣刻著層層收束的界紋，像是用來聆聽並校正整座封印的回應。"
        }
      ],
      "enquires": ["封印", "鎮界"]
    },
    {
      "vnum": 9906,
      "name": "殘壇側室",
      "description": "側室裡只剩半座塌損祭壇，壇面還能看見被反覆替換過器物的痕跡。四周散落的石片都刻著相近的禁紋，彷彿過去一直有人在此維持封印，直到某次再也沒有回來。",
      "sector_type": "SECT_INSIDE",
      "cluster": "forbidden-side",
      "coord": [3, -1, -13],
      "labels": ["altar", "reward-hint"],
      "exits": [
        { "direction": "west", "to": 9905 },
        { "direction": "east", "to": 9907 }
      ],
      "keywords": [
        {
          "keyword": "祭壇",
          "description": "祭壇中段被高熱與巨力同時摧裂，留下的痕跡不像單純祭祀，更像一次倉促的鎮壓。"
        }
      ],
      "enquires": ["祭壇", "封印"]
    },
    {
      "vnum": 9907,
      "name": "鎮鎖壁",
      "description": "整面石壁被數十道粗細不一的鎖條釘入裂縫，鎖條盡頭還連著深埋於地面的鐵樁。每當界井深處傳來沉響，這些鎖條便會齊齊顫鳴，像在承受下方某種東西持續而緩慢的掙動。",
      "sector_type": "SECT_INSIDE",
      "cluster": "forbidden-side",
      "coord": [4, -1, -13],
      "labels": ["seal", "risk"],
      "exits": [
        { "direction": "west", "to": 9906 },
        { "direction": "east", "to": 9908 }
      ],
      "keywords": [
        {
          "keyword": "鎖條",
          "description": "鎖條表面覆著古舊符漆，顯示它們不只是物理束縛，也是封印的一部分。"
        }
      ],
      "enquires": ["鎮界", "鎖鏈"]
    },
    {
      "vnum": 9908,
      "name": "禁紋裂面",
      "description": "裂面原本應是一道完整石幕，如今卻被自內而外撕出數條不規則開口，邊緣仍殘留焦黑的禁紋。透過裂隙往內看，只能見到比夜色更沉的黑影層層疊在更深處，讓人本能地不願久望。",
      "sector_type": "SECT_INSIDE",
      "cluster": "forbidden-side",
      "coord": [5, -1, -13],
      "labels": ["fracture", "danger"],
      "exits": [
        { "direction": "west", "to": 9907 },
        { "direction": "east", "to": 9909 },
        { "direction": "down", "to": 9911 }
      ],
      "keywords": [
        {
          "keyword": "裂面",
          "description": "石幕上的裂口筆直而深，像有某種力量曾自下而上撞擊過這道封界。"
        }
      ]
    },
    {
      "vnum": 9909,
      "name": "觀界偏座",
      "description": "偏座像半嵌在石壁內的觀測平台，前方仍留有幾道朝向裂面的狹長視口。坐在此處時，可以同時看見主橋鎖條的收縮與裂面暗影的翻動，像這裡本來就是專門監看封印狀態的地方。",
      "sector_type": "SECT_INSIDE",
      "cluster": "forbidden-side",
      "coord": [6, -1, -13],
      "labels": ["observation", "lore"],
      "exits": [
        { "direction": "west", "to": 9908 }
      ],
      "enquires": ["觀界", "裂面"]
    },
    {
      "vnum": 9910,
      "name": "墜界斷台",
      "description": "長橋盡頭是一座被截斷的方形石台，台邊原本應有完整護欄，如今只剩斷裂基座。台面中央向下開著一口幽暗井口，井內沒有風，卻不斷送上比石壁還冷的沉重氣息。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-boundary",
      "coord": [4, 0, -13],
      "labels": ["well", "depth"],
      "exits": [
        { "direction": "west", "to": 9904 },
        { "direction": "south", "to": 9911 }
      ],
      "enquires": ["界井", "下層"]
    },
    {
      "vnum": 9911,
      "name": "井緣浮階",
      "description": "幾塊懸離石面的浮階沿著井壁蜿蜒下沉，每一級都刻著早已模糊的壓界文字。站在這裡時，會清楚聽見下方傳來有節律卻不似人聲的回應，像深井本身在等待誰繼續下探。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-boundary",
      "coord": [4, -1, -14],
      "labels": ["stairs", "boundary"],
      "exits": [
        { "direction": "north", "to": 9910 },
        { "direction": "up", "to": 9908 },
        { "direction": "down", "to": 9912 }
      ],
      "enquires": ["界井", "退路"]
    },
    {
      "vnum": 9912,
      "name": "禁牢界井",
      "description": "井底並非實地，而是一圈勉強懸住的黑石井臺，四周刻滿層層交錯的古老禁文。正中央的井心只有一片看不見底的黯黑，偶爾會有極微弱的紅光像眼瞼般一閃即逝，讓人確信更深處仍有什麼被鎮在下方。",
      "sector_type": "SECT_INSIDE",
      "cluster": "abyss-boundary",
      "coord": [4, -2, -15],
      "labels": ["world-link-down", "boss-threshold"],
      "exits": [
        { "direction": "up", "to": 9911 }
      ],
      "keywords": [
        {
          "keyword": "禁文",
          "description": "禁文層層相扣，不像單純束縛，更像在延後某種無法正面對抗的甦醒。"
        }
      ],
      "enquires": ["封印", "下層"]
    }
  ]
}
```
