# 星墜天坑 (`sec_starfall_crater`)

## Area Intent

`sec_starfall_crater` 承接 `wild_bailang` 風蝕石壇上方的異樣天光，把原本只像山民傳聞的墜星痕跡正式落成一塊焦黑、發亮、又讓地勢失去常理的北境祕境。這裡不靠祭天秩序撐場，而是讓玩家感覺自己正走進一個曾被天外之物硬生生砸開、至今仍沒完全冷卻的異象坑洞。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `天坑 / 隕石`
- LevelRange: `46-60`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_starfall_crater",
    "title": "星墜天坑",
    "design_notes": "第一版 spec-first 草案。先固定墜星入口、焦痕坑緣、裂星斜坡、星核碎坪、熾紋祭壇、墜火環壁、殞光裂庭與天隕觀缺，把白狼山高處的墜星異坑正式展成可載入的北境 secret。",
    "level_range": "46-60",
    "planned_vnum_range": "18901-18920",
    "reserved_room_block": "18901-18920",
    "theme": {
      "primary": "仙俠",
      "secondary": "天坑 / 隕石"
    },
    "world_links": [
      {
        "direction": "down",
        "source_vnum": 18901,
        "target_area": "wild_bailang",
        "target_room_vnum": 18005,
        "label": "風蝕石壇"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "坑緣入口帶" },
      { "id": "rim", "label": "焦痕坑緣" },
      { "id": "core", "label": "星核異象區" },
      { "id": "deep", "label": "裂庭與觀缺" }
    ]
  },
  "rooms": [
    {
      "vnum": 18901,
      "name": "墜星入口",
      "description": "從風蝕石壇再往上踏出的那一步，地勢忽然不再像普通山坡，而像被某種巨力掀開後又勉強凝住的斷層邊。腳下石色一半灰白一半焦黑，讓人很難相信這裡只是白狼山的更高處。",
      "sector_type": "SECT_HILLS",
      "cluster": "entry",
      "coord": [0, 0, 1],
      "labels": ["entry", "down-edge", "world-link-down", "nonplanar"],
      "exits": [
        { "direction": "down", "to": 18005, "external": true },
        { "direction": "north", "to": 18902 }
      ],
      "enquires": ["下面", "石壇", "天坑"]
    },
    {
      "vnum": 18902,
      "name": "焦痕坑緣",
      "description": "坑緣一圈都留著像火燒又像被光硬刻過的焦痕，連風從這裡掠過時都帶著不太像山氣的乾裂味。往內望去，整個天坑不像天然塌陷，更像某顆東西直接從天上嵌進了山裡。",
      "sector_type": "SECT_HILLS",
      "cluster": "rim",
      "coord": [0, 1, 1],
      "labels": ["rim", "burn-mark"],
      "exits": [
        { "direction": "south", "to": 18901 },
        { "direction": "north", "to": 18903 },
        { "direction": "east", "to": 18905 }
      ],
      "enquires": ["焦痕", "坑緣", "裡面"]
    },
    {
      "vnum": 18903,
      "name": "裂星斜坡",
      "description": "斜坡上滿是被撞裂後又高溫熔黏過的石紋，踩起來既脆又滑，像一整片地面都還記得那場墜落。越往下走，四周的光色越不穩，讓人連距離感都開始失真。",
      "sector_type": "SECT_HILLS",
      "cluster": "rim",
      "coord": [0, 2, 0],
      "labels": ["slope", "broken-star"],
      "exits": [
        { "direction": "south", "to": 18902 },
        { "direction": "east", "to": 18904 },
        { "direction": "down", "to": 18906 }
      ],
      "enquires": ["斜坡", "裂紋", "光"]
    },
    {
      "vnum": 18904,
      "name": "星核碎坪",
      "description": "碎坪中央散著幾塊還保留奇異冷亮的隕片，周圍地面卻像被反覆灼燒過一樣發黑。這裡最讓人不安的不是安靜，而是那些隕片像仍在默默牽動整個坑底的光線走向。",
      "sector_type": "SECT_HILLS",
      "cluster": "core",
      "coord": [1, 2, 0],
      "labels": ["core", "meteor-shard", "anomaly"],
      "exits": [
        { "direction": "west", "to": 18903 },
        { "direction": "north", "to": 18908 }
      ],
      "enquires": ["隕片", "星核", "碎坪"]
    },
    {
      "vnum": 18905,
      "name": "熾紋祭壇",
      "description": "祭壇像是在天坑形成之後才被人補築上去，壇面沿著裂紋嵌了一圈早已黯淡卻仍能映光的金石紋路。它讓人懷疑後來的人不是來祭天，而是想試著和坑底那股力量談條件。",
      "sector_type": "SECT_HILLS",
      "cluster": "core",
      "coord": [1, 1, 1],
      "labels": ["altar", "glow-mark", "ritual"],
      "exits": [
        { "direction": "west", "to": 18902 },
        { "direction": "north", "to": 18907 }
      ],
      "enquires": ["祭壇", "熾紋", "誰"]
    },
    {
      "vnum": 18906,
      "name": "墜火環壁",
      "description": "環壁內側保留著一道道向外翻卷的熔痕，像是墜下來的火先撞穿地勢，再沿壁面朝四周濺開。站在這裡時，任何抬頭動作都會讓人本能地去想像當年那一擊究竟有多大。",
      "sector_type": "SECT_HILLS",
      "cluster": "deep",
      "coord": [0, 2, -1],
      "labels": ["wall", "impact", "deep"],
      "exits": [
        { "direction": "up", "to": 18903 },
        { "direction": "east", "to": 18907 }
      ],
      "enquires": ["環壁", "熔痕", "當年"]
    },
    {
      "vnum": 18907,
      "name": "殞光裂庭",
      "description": "裂庭像是環壁與祭壇之間被硬撕出來的一段過渡帶，地上光紋忽明忽暗，彷彿整片坑底的殘火都在這裡換氣。這裡沒有真正安全的落腳點，只有相對沒那麼容易被異象拖住的地方。",
      "sector_type": "SECT_HILLS",
      "cluster": "deep",
      "coord": [1, 2, -1],
      "labels": ["court", "light-rift", "unstable"],
      "exits": [
        { "direction": "south", "to": 18905 },
        { "direction": "west", "to": 18906 },
        { "direction": "up", "to": 18908 }
      ],
      "enquires": ["裂庭", "殞光", "安全"]
    },
    {
      "vnum": 18908,
      "name": "天隕觀缺",
      "description": "觀缺位在坑內最高、卻也最不完整的一段斷臺上，像有人曾試著從這裡觀測墜星後殘留下來的天象規律。可真正站穩後才會發現，這地方更像一處被異象反過來觀察人的缺口。",
      "sector_type": "SECT_HILLS",
      "cluster": "deep",
      "coord": [1, 3, 1],
      "labels": ["observatory", "fracture", "high"],
      "exits": [
        { "direction": "south", "to": 18904 },
        { "direction": "down", "to": 18907 }
      ],
      "enquires": ["觀缺", "天隕", "上面"]
    }
  ]
}
```
