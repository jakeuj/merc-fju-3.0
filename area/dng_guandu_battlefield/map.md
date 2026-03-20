# 官渡古戰場 (`dng_guandu_battlefield`)

## Area Intent

`dng_guandu_battlefield` 承接 `wild_puyang_forest` 北向荒路之外的第一段真正戰地，讓玩家從戰前林野的風聲，正式走進壕溝、高塹、焚糧車列與殘旗高地交錯的官渡古戰場。

第一版目標先固定：

- 一條由南向北切入古戰場的主推進線
- 一條圍繞焚糧車與焦木坑的側線
- 一條 `up/down` 連到殘旗高地與壕溝底部的非平面軍旅支線
- 以 `#Enquire` / `#Keyword` 暗示官渡、糧車、鼓旗與死地前帶

這一版刻意讓玩家感受到：

- 戰場不是平面空地，而是由壕溝與土塹切開的危險地形
- 火攻與糧道崩壞後的痕跡仍然主宰這片空間
- 再往北就是更深、更狠的主陣死地，但第一版先把外圈壓力與辨識度做穩

## Theme Positioning

- Theme: `軍旅`
- Subtheme: `古戰場 / 官渡鏖兵`
- LevelRange: `24-34`
- Parent region: `兗州河北`
- World gap filled: 讓主世界 progression 從 `wild_puyang_forest` 的林野前帶自然推進到官渡鏖兵的戰地 dungeon

## Player Flow

1. 玩家由南向北越過前塹，立即感受到碎木、拒馬與戰地風聲。
2. 主線沿壕溝、土塹與斷戟泥地前進，逐步看見更完整的古戰場結構。
3. 焚糧車列側線讓玩家從火攻痕跡感受到官渡辨識度，而不只是一片 generic battlefield。
4. 殘旗高地透過 `up/down` 讓玩家從地勢上體會戰場視野差與伏擊壓力。
5. 北向死地前帶只作為下一區壓力預告，不在第一版就做滿整場鏖兵。

## Cluster Notes

### `south-approach`

- 房間重點：戰場前塹、破木拒馬、南入壕口
- 玩家感受：剛進戰場就被提醒這裡不是普通野外
- 對外角色：作為日後接 `wild_puyang_forest` 北向邊界的戰場入口

### `trench-line`

- 房間重點：壕溝、土塹、斷戟泥地
- 玩家感受：地勢切割、移動不再順暢、容易判斷錯誤
- 對外角色：作為全區主 dungeon 線骨幹

### `burned-wagons`

- 房間重點：焚糧車列、焦木坑、灰燼側帶
- 玩家感受：火攻後的殘酷與戰略餘味
- 對外角色：提供戰場辨識度與掉寶 / lore 側線空間

### `banner-ridge`

- 房間重點：鼓旗坡、殘旗高地、瞭望塹口
- 玩家感受：站高才能看見戰局，但也更容易暴露
- 對外角色：以非平面高差提供軍旅風格的移動壓力

### `north-deadground`

- 房間重點：死地前帶、散兵荒路、主陣深處預留口
- 玩家感受：空氣更冷更空，像真正的鏖兵核心就在前方
- 對外角色：作為未來更深戰場區的前帶

## Planned World Links

這些是世界層連接意圖；目前先固定在 spec，不提前建立 runtime 假邊界：

- `south` from `14001`: planned link to `wild_puyang_forest`
- `north` from `14012`: planned link to `fort_hulao`
- `east` from `14007`: planned link to `city_puyang`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在 `官渡 / 壕溝 / 糧車 / 鼓旗 / 去路`
- `#Keyword` 第一版會落在 `殘旗 / 斷戟 / 糧車 / 焦木 / 土塹`
- `#Job` 第一版暫不新增；等真正要做斥候、奪旗或搜殘糧 loop 再補 job 與 runtime flow

## Suggested Layout

```text
濮陽林野北向荒路
   |
[14001] 戰場前塹 -- [14002] 破木拒馬帶 -- [14003] 南入壕口 -- [14004] 斷戟泥地 -- [14005] 土塹彎線 -- [14012] 北向死地前帶
                                                                          |
                                                                          +-- east -- [14006] 焚糧車列 -- [14007] 焦木坑 -- [14008] 灰燼側帶
                                                                                                                |
                                                                                                             up
                                                                                                                |
                                                                                                             [14009] 鼓旗坡 -- [14010] 殘旗高地 -- [14011] 瞭望塹口
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_guandu_battlefield",
    "title": "官渡古戰場",
    "design_notes": "第一版 spec-first 草案。先固定官渡戰場前塹、壕溝主線、焚糧車側線與殘旗高地非平面軍旅支線，讓古戰場辨識度在 runtime implementation 前先穩住。",
    "level_range": "24-34",
    "planned_vnum_range": "14001-14030",
    "reserved_room_block": "14001-14030",
    "theme": {
      "primary": "軍旅",
      "secondary": "古戰場 / 官渡鏖兵"
    },
    "world_links": [
      {
        "direction": "south",
        "source_vnum": 14001,
        "target_area": "wild_puyang_forest",
        "label": "林野前帶"
      },
      {
        "direction": "north",
        "source_vnum": 14012,
        "target_area": "fort_hulao",
        "label": "主陣死地"
      },
      {
        "direction": "east",
        "source_vnum": 14007,
        "target_area": "city_puyang",
        "label": "濮陽糧道殘線"
      }
    ],
    "clusters": [
      { "id": "south-approach", "label": "南側前塹帶" },
      { "id": "trench-line", "label": "壕溝主線" },
      { "id": "burned-wagons", "label": "焚糧車側線" },
      { "id": "banner-ridge", "label": "殘旗高地線" },
      { "id": "north-deadground", "label": "北向死地前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 14001,
      "name": "戰場前塹",
      "description": "泥土在這裡被臨時掘成一道不深卻足以讓人放慢腳步的前塹，塹邊滿是朽木、破繩與被踩碎的箭桿。往南仍像從林野走來，向北卻已能清楚嗅到焦土與鐵鏽混在一起的戰場氣味。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "world-link-south"],
      "exits": [
        { "direction": "north", "to": 14002 }
      ],
      "enquires": ["官渡", "去路"]
    },
    {
      "vnum": 14002,
      "name": "破木拒馬帶",
      "description": "折斷的拒馬和燒黑的柵木橫在泥地上，逼得人只能在狹窄缺口間穿行。這裡不像仍有軍紀維持的營地，而像一場廝殺過後誰也沒空清理的邊角死帶。",
      "sector_type": "SECT_FIELD",
      "cluster": "south-approach",
      "coord": [1, 0, 0],
      "labels": ["obstacle", "battle-trace"],
      "exits": [
        { "direction": "south", "to": 14001 },
        { "direction": "north", "to": 14003 }
      ],
      "keywords": [
        {
          "keyword": "拒馬",
          "description": "拒馬木樁上還留著焦痕與刀斧裂口，顯然不是自然腐壞，而是被人硬生生打開缺口。"
        }
      ]
    },
    {
      "vnum": 14003,
      "name": "南入壕口",
      "description": "地面在這裡突然向內下凹，壕口兩側堆著不完整的沙包與泥牆殘角。往前走若不先看清高低差，很容易一腳踏進比預想更滑的泥底。",
      "sector_type": "SECT_FIELD",
      "cluster": "trench-line",
      "coord": [2, 0, -1],
      "labels": ["trench-entry", "risk"],
      "exits": [
        { "direction": "south", "to": 14002 },
        { "direction": "north", "to": 14004 }
      ],
      "enquires": ["壕溝", "前面"]
    },
    {
      "vnum": 14004,
      "name": "斷戟泥地",
      "description": "泥地裡斜插著數截斷戟與折矛，雨水和血泥早已混成同一種暗色。每走一步都像踩在別人來不及帶走的失敗上，讓人很難把這裡只當普通道路經過。",
      "sector_type": "SECT_FIELD",
      "cluster": "trench-line",
      "coord": [3, 0, -1],
      "labels": ["battlefield", "grim"],
      "exits": [
        { "direction": "south", "to": 14003 },
        { "direction": "north", "to": 14005 }
      ],
      "keywords": [
        {
          "keyword": "斷戟",
          "description": "幾截戟刃缺口方向一致，像是同一輪近身衝撞裡被硬生生折斷。"
        }
      ],
      "enquires": ["戰場", "死傷"]
    },
    {
      "vnum": 14005,
      "name": "土塹彎線",
      "description": "壕線在此向東外拐，內側是勉強立住的土塹，外側則散著碎甲與破盾。若說前面只是讓人知道這裡打過仗，那麼這裡便開始讓人意識到每一段地勢都曾是人命交換的位置。",
      "sector_type": "SECT_HILLS",
      "cluster": "trench-line",
      "coord": [4, 0, 1],
      "labels": ["junction", "earthwork"],
      "exits": [
        { "direction": "south", "to": 14004 },
        { "direction": "north", "to": 14012 },
        { "direction": "east", "to": 14006 }
      ],
      "keywords": [
        {
          "keyword": "土塹",
          "description": "土塹內側有明顯反覆踩踏留下的凹痕，顯示這裡曾被當成持久拉鋸的位置。"
        }
      ],
      "enquires": ["鼓旗", "糧車", "北邊"]
    },
    {
      "vnum": 14006,
      "name": "焚糧車列",
      "description": "數輛早被燒穿的糧車歪倒在一旁，木框和鐵箍扭成焦黑形狀，連地面都被烤出一條長長黑痕。站在這裡時，官渡的名字不再只是地圖上的標記，而像一種仍在發熱的歷史傷口。",
      "sector_type": "SECT_FIELD",
      "cluster": "burned-wagons",
      "coord": [5, 0, 0],
      "labels": ["iconic", "fire-scar"],
      "exits": [
        { "direction": "west", "to": 14005 },
        { "direction": "east", "to": 14007 }
      ],
      "keywords": [
        {
          "keyword": "糧車",
          "description": "糧車殘框內仍卡著幾片燒硬的穀殼與焦炭，像把火攻那一刻永遠留在了木頭裡。"
        }
      ],
      "enquires": ["糧車", "火攻", "官渡"]
    },
    {
      "vnum": 14007,
      "name": "焦木坑",
      "description": "地面在此向內塌成一圈灰黑色坑地，焦木、碎輪與半熔的鐵件堆在一起。風一吹，灰燼還會像活著似的飄起來，讓人很難分清哪一部分只是殘骸，哪一部分還在無聲燃燒。",
      "sector_type": "SECT_FIELD",
      "cluster": "burned-wagons",
      "coord": [6, 0, -1],
      "labels": ["pit", "ash"],
      "exits": [
        { "direction": "west", "to": 14006 },
        { "direction": "east", "to": 14008 }
      ],
      "keywords": [
        {
          "keyword": "焦木",
          "description": "焦木表面一碰就掉灰，裡層卻仍硬得像不肯承認自己早已燒盡。"
        }
      ],
      "enquires": ["灰燼", "東路"]
    },
    {
      "vnum": 14008,
      "name": "灰燼側帶",
      "description": "這條偏路覆著不自然厚的灰層，腳步聲會被吞掉大半，只剩甲片互撞的細響更清楚。若有人想在戰場上悄悄靠近別人，這大概是比正面壕線舒服得多的辦法。",
      "sector_type": "SECT_FIELD",
      "cluster": "burned-wagons",
      "coord": [7, 0, -1],
      "labels": ["side-route", "concealment"],
      "exits": [
        { "direction": "west", "to": 14007 },
        { "direction": "up", "to": 14009 }
      ]
    },
    {
      "vnum": 14009,
      "name": "鼓旗坡",
      "description": "坡面上還能看見鼓架拖行時留下的深槽，坡頂則插著幾根斷桿。從這裡往下看，壕線、焦坑與殘車像一張被撕裂卻仍看得出布局的戰場圖。",
      "sector_type": "SECT_HILLS",
      "cluster": "banner-ridge",
      "coord": [7, 1, 1],
      "labels": ["up-route", "command-view"],
      "exits": [
        { "direction": "down", "to": 14008 },
        { "direction": "east", "to": 14010 }
      ],
      "enquires": ["鼓旗", "高處"]
    },
    {
      "vnum": 14010,
      "name": "殘旗高地",
      "description": "高地邊緣插著幾面只剩布條的殘旗，旗面顏色幾乎辨不清，卻仍固執地在風裡拍打。站得越高，就越能感覺到這片戰場並未真正安靜，只是把聲音都埋進了土裡。",
      "sector_type": "SECT_HILLS",
      "cluster": "banner-ridge",
      "coord": [8, 1, 1],
      "labels": ["lookout", "banner"],
      "exits": [
        { "direction": "west", "to": 14009 },
        { "direction": "east", "to": 14011 }
      ],
      "keywords": [
        {
          "keyword": "殘旗",
          "description": "殘旗邊緣磨成鬚狀，卻還勉強保住原來的結法，像某種不肯退場的軍令。"
        }
      ],
      "enquires": ["殘旗", "戰況"]
    },
    {
      "vnum": 14011,
      "name": "瞭望塹口",
      "description": "高地下方另有一道向北開的塹口，位置既能俯視主線，又能迅速切回地面。這種設計不為好看，只為在最短時間裡把命令或埋伏送到最該出現的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "banner-ridge",
      "coord": [9, 1, 0],
      "labels": ["ridge-exit", "military-control"],
      "exits": [
        { "direction": "west", "to": 14010 },
        { "direction": "south", "to": 14012 }
      ],
      "enquires": ["瞭望", "塹口", "北線"]
    },
    {
      "vnum": 14012,
      "name": "北向死地前帶",
      "description": "再往北，地勢變得更空更硬，風裡不再有林氣與灰燼，而是純粹乾冷的塵土味。這裡像是一條把人送進真正主陣死地的門檻，讓你明白眼前看到的還只是官渡留下來的外圈傷痕。",
      "sector_type": "SECT_FIELD",
      "cluster": "north-deadground",
      "coord": [5, 1, 0],
      "labels": ["north-edge", "future-depth"],
      "exits": [
        { "direction": "south", "to": 14005 },
        { "direction": "north", "to": 14011 }
      ],
      "enquires": ["前線", "死地", "去路"]
    }
  ]
}
```
