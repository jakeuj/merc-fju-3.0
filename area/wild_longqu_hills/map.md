# 龍渠丘陵 (`wild_longqu_hills`)

## Area Intent

`wild_longqu_hills` 承接 `loyang_outskirts` 東側丘陵巡路之後的真正野外區段，讓玩家從「仍受官道秩序保護的近郊」進一步進入視線遮蔽、地勢起伏、帶有古老遺跡痕跡的探索帶。

第一版目標先固定：

- 一條由西向東深入丘陵的主探索線
- 一條偏向獵戶與採集節奏的南側支線
- 一條 `down/up` 的裂縫石階非平面連線
- 以 `#Enquire` / `#Keyword` 暗示山路、地標與遺跡痕跡

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `仙俠風`
- LevelRange: `8-18`
- Parent area: `loyang_outskirts`
- World gap filled: 把洛陽東郊與更外圈野外之間的丘陵段做成可探索區，讓 `龍渠丘陵` 不再只是一個文字邊界

## Player Flow

1. 玩家從 `loyang_outskirts/7510` 東行離開近郊巡路，先看見丘陵入口與逐漸變稀的官道痕跡。
2. 主線沿著風蝕坡與岔石路向東深入，途中透過石碑、舊祭壇與獵戶痕跡提供探索動機。
3. 南側支線讓玩家接觸較生活化的補給與傳聞節點，避免整區只剩單純打怪。
4. 深處裂縫石階以下探形式預留下一層地下遺跡或機關秘境。

## Cluster Notes

### `west-entry`

- 房間重點：丘陵東口、風蝕坡道
- 玩家感受：剛離開官道，安全感還沒完全消失
- 對外角色：承接 `loyang_outskirts/7510`

### `ridge-route`

- 房間重點：岔石路、斷碑荒坡、龍渠高脊
- 玩家感受：視野拉開、方向判讀變重要、遺跡感開始浮現
- 對外角色：作為主線探索與未來 deeper wild 連接基礎

### `hunter-south`

- 房間重點：野獵土徑、獵戶歇腳岩
- 玩家感受：人類活動痕跡仍在，但已不屬於官道秩序
- 對外角色：提供補給、問路與失蹤傳聞

### `ruin-fissure`

- 房間重點：埋石祭壇、裂縫前台、裂縫石階
- 玩家感受：不安、潮氣、像有更深層的祕密在地下
- 對外角色：作為未來地下遺跡 / 機關區入口 stub

## Planned World Links

- `west` from `9401`: planned link to `loyang_outskirts` room `7510`
- `down` beyond `9410`: planned continuation to `地下遺跡 / 機關秘境`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在入口坡道、岔石路、獵戶歇腳岩與裂縫前台，讓玩家能問 `洛陽 / 山路 / 地標 / 裂縫`
- `#Keyword` 第一版會落在斷碑、獸跡、祭壇、裂縫邊緣，讓探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先避免重用現有硬編碼 room job

## Suggested Layout

```text
洛陽東郊丘陵巡路(7510)
   |
[9401] 丘陵東口 -- [9402] 風蝕坡道 -- [9403] 岔石路 -- [9404] 斷碑荒坡 -- [9408] 裂縫前台
                                      |                                |
                                   [9405] 野獵土徑 -- [9406] 獵戶歇腳岩 -- [9407] 龍渠高脊 -- [9409] 埋石祭壇
                                                                       |
                                                                    [9408] 裂縫前台
                                                                       |
                                                                     down
                                                                       |
                                                                    [9410] 裂縫石階
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_longqu_hills",
    "title": "龍渠丘陵",
    "design_notes": "第一版 spec-first 草案。先固定洛陽東郊東向邊界後的丘陵主線、獵戶支線與裂縫石階非平面入口。",
    "parent_area": "loyang_outskirts",
    "level_range": "8-18",
    "planned_vnum_range": "9401-9410",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "仙俠風"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 9401,
        "target_area": "loyang_outskirts",
        "target_room_vnum": 7510,
        "label": "丘陵巡路"
      },
      {
        "direction": "down",
        "source_vnum": 9410,
        "target_area": "ruin_machine_depths",
        "label": "地下遺跡"
      }
    ],
    "clusters": [
      { "id": "west-entry", "label": "丘陵入口帶" },
      { "id": "ridge-route", "label": "丘陵主線與高脊" },
      { "id": "hunter-south", "label": "獵戶南支線" },
      { "id": "ruin-fissure", "label": "遺跡裂縫前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 9401,
      "name": "丘陵東口",
      "description": "官道留下的車轍在這裡徹底碎成亂石與黃土坡，向西仍能隱約望見洛陽東郊巡路的旗影，向東則只剩連綿起伏的丘脊與被風磨白的石面。",
      "sector_type": "SECT_HILLS",
      "cluster": "west-entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-west"],
      "exits": [
        { "direction": "west", "to": 7510, "external": true },
        { "direction": "east", "to": 9402 }
      ],
      "enquires": ["洛陽", "回路"]
    },
    {
      "vnum": 9402,
      "name": "風蝕坡道",
      "description": "坡道兩側裸露著被風雨削薄的黃土層，腳下碎石一踩就滑。沿坡往上時，城郊的喧聲被風聲取代，只剩遠處偶爾傳來鳥鳴與獸類奔竄的回響。",
      "sector_type": "SECT_HILLS",
      "cluster": "west-entry",
      "coord": [1, 0, 0],
      "labels": ["slope", "transition"],
      "exits": [
        { "direction": "west", "to": 9401 },
        { "direction": "east", "to": 9403 }
      ],
      "enquires": ["山路", "入口"]
    },
    {
      "vnum": 9403,
      "name": "岔石路",
      "description": "幾塊巨大亂石把山路分成數股細徑，石縫間還看得見舊時車輪硬壓出的痕跡。若不熟地勢，很容易在這裡把正路與野徑弄混。",
      "sector_type": "SECT_HILLS",
      "cluster": "ridge-route",
      "coord": [2, 0, 0],
      "labels": ["junction", "enquire"],
      "exits": [
        { "direction": "west", "to": 9402 },
        { "direction": "east", "to": 9404 },
        { "direction": "south", "to": 9405 }
      ],
      "keywords": [
        {
          "keyword": "石縫",
          "description": "石縫裡卡著幾片破布與乾掉的草繩，像是有人曾在此臨時做過方向記號。"
        }
      ],
      "enquires": ["地標", "岔路", "山路"]
    },
    {
      "vnum": 9404,
      "name": "斷碑荒坡",
      "description": "荒坡中央立著半截殘碑，碑面文字早被風沙磨平，只剩幾道像山川又像符記的刻痕。站在這裡往東北看去，丘陵線像一道又一道掩住視線的波浪。",
      "sector_type": "SECT_HILLS",
      "cluster": "ridge-route",
      "coord": [3, 0, 0],
      "labels": ["landmark", "ruin-hint"],
      "exits": [
        { "direction": "west", "to": 9403 },
        { "direction": "east", "to": 9408 }
      ],
      "keywords": [
        {
          "keyword": "斷碑",
          "description": "斷碑底部殘留著不屬於官府里程碑的紋路，看起來更像某種祭祀或鎮壓用的遺物。"
        }
      ],
      "enquires": ["石碑", "前路"]
    },
    {
      "vnum": 9405,
      "name": "野獵土徑",
      "description": "這條土徑比主路狹窄許多，沿途可見獸蹄、箭尾與粗略搭起的陷索。它不像正規道路，卻顯然有人長期往返其間。",
      "sector_type": "SECT_FIELD",
      "cluster": "hunter-south",
      "coord": [2, -1, 0],
      "labels": ["side-path", "hunter-route"],
      "exits": [
        { "direction": "north", "to": 9403 },
        { "direction": "east", "to": 9406 }
      ],
      "keywords": [
        {
          "keyword": "獸跡",
          "description": "泥面上的獸跡深淺不一，有些像山麂，有些卻大得不太尋常，讓人分不清是野獸還是被什麼拖行過。"
        }
      ]
    },
    {
      "vnum": 9406,
      "name": "獵戶歇腳岩",
      "description": "一塊向外突出的平岩剛好能避風，岩下擱著熄掉的火盆與兩只半空的水囊。熟悉山路的人多半會在這裡歇腳、交換哪段坡最近不太安穩的消息。",
      "sector_type": "SECT_FIELD",
      "cluster": "hunter-south",
      "coord": [3, -1, 0],
      "labels": ["rest-stop", "enquire"],
      "exits": [
        { "direction": "west", "to": 9405 },
        { "direction": "east", "to": 9407 }
      ],
      "enquires": ["獵戶", "山路", "失蹤者"]
    },
    {
      "vnum": 9407,
      "name": "龍渠高脊",
      "description": "高脊一側可遠望洛陽平野，另一側則是層層丘壑和被霧氣吞掉的低谷。站在此處，已幾乎看不見官道秩序留下的任何痕跡，只有地形本身在決定你能走到哪裡。",
      "sector_type": "SECT_HILLS",
      "cluster": "ridge-route",
      "coord": [4, -1, 0],
      "labels": ["high-ground", "survey"],
      "exits": [
        { "direction": "west", "to": 9406 },
        { "direction": "east", "to": 9409 }
      ]
    },
    {
      "vnum": 9408,
      "name": "裂縫前台",
      "description": "斷裂岩層在此向內凹出一片避風的平台，岩壁邊緣隱約可見向下延伸的窄口裂縫。地面散著乾掉的草繩與碎裂木樁，像曾有人試圖封住下方的入口。",
      "sector_type": "SECT_HILLS",
      "cluster": "ruin-fissure",
      "coord": [4, 0, 0],
      "labels": ["fissure", "nonplanar-entry"],
      "exits": [
        { "direction": "west", "to": 9404 },
        { "direction": "south", "to": 9409 },
        { "direction": "down", "to": 9410 }
      ],
      "keywords": [
        {
          "keyword": "裂縫",
          "description": "裂縫邊緣帶著潮氣，底下不時送上冷風，像有一條更深的石道正等著人下去。"
        }
      ],
      "enquires": ["裂縫", "下方"]
    },
    {
      "vnum": 9409,
      "name": "埋石祭壇",
      "description": "幾塊被泥沙半掩的石塊圍出簡陋圓形，中間殘留灰燼與風化符痕。它不像官府設施，也不像山民隨手堆起的記號，更像早被遺忘的山祭遺址。",
      "sector_type": "SECT_HILLS",
      "cluster": "ruin-fissure",
      "coord": [5, -1, 0],
      "labels": ["ruin", "ritual"],
      "exits": [
        { "direction": "north", "to": 9408 },
        { "direction": "west", "to": 9407 }
      ],
      "keywords": [
        {
          "keyword": "祭壇",
          "description": "祭壇中央只有一圈淡得快看不出的刻痕，像某種本該鎮住地底之物的舊禁制。"
        }
      ],
      "enquires": ["祭壇", "遺跡"]
    },
    {
      "vnum": 9410,
      "name": "裂縫石階",
      "description": "石階緊貼岩壁向下盤旋，腳邊積著濕冷泥水與碎裂石片。再往深處看去，只剩一片吞光的黑暗，像是丘陵底下另有不屬於地表的世界。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ruin-fissure",
      "coord": [4, 0, -1],
      "labels": ["cellar", "future-depth"],
      "exits": [
        { "direction": "up", "to": 9408 }
      ],
      "enquires": ["出口", "地底"]
    }
  ]
}
```
