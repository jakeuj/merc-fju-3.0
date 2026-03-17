# 裂界本核 (`sec_rift_true_core`)

## Area Intent

`sec_rift_true_core` 承接鎮封底座最深縱井，讓玩家踏入封印體系真正的裂界本核。這一層不再是維護廊帶，而是失穩封圈、導脈井道與核心井場交疊的高壓區；每一步都處在封印與裂界拉扯的臨界線上。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂界本核 / 失穩封圈`
- LevelRange: `62-78`
- Parent area: `sec_rift_underseal_dais`
- ReservedRoomBlock: `10201-10220`

## Planned World Links

- `up` from `10201`: `sec_rift_underseal_dais` room `10112`
- `down` from `10212`: future deeper rift-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_true_core",
    "title": "裂界本核",
    "design_notes": "鎮封底座下方的本核主區，聚焦失穩封圈與核心井場的高壓推進。",
    "parent_area": "sec_rift_underseal_dais",
    "level_range": "62-78",
    "planned_vnum_range": "10201-10220",
    "reserved_room_block": "10201-10220",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂界本核 / 失穩封圈"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10201,
        "target_area": "sec_rift_underseal_dais",
        "target_room_vnum": 10112,
        "label": "鎮封縱井"
      },
      {
        "direction": "down",
        "source_vnum": 10212,
        "target_area": "sec_rift_core_below",
        "target_room_vnum": 10301,
        "label": "裂核深井"
      }
    ],
    "clusters": [
      { "id": "descent-well", "label": "本核落井" },
      { "id": "fracture-ring", "label": "失穩封圈" },
      { "id": "pulse-annex", "label": "導脈偏廊" },
      { "id": "heart-dais", "label": "核心井場" }
    ]
  },
  "rooms": [
    {"vnum":10201,"name":"本核落井","description":"落井底部是一圈半熔化石臺，頭頂縱井仍有碎光垂落，腳下卻已能聽見更深處規律而沉重的裂核脈動。","sector_type":"SECT_INSIDE","cluster":"descent-well","coord":[0,0,-20],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10112,"external":true},{"direction":"east","to":10202}],"enquires":["退路","井道"]},
    {"vnum":10202,"name":"鎮裂前臺","description":"前臺的鎮紋圈早已出現大片斷痕，仍勉強把外洩脈流導向四周石槽，讓本核沒有立刻崩塌。","sector_type":"SECT_INSIDE","cluster":"descent-well","coord":[1,0,-20],"labels":["ring"],"exits":[{"direction":"west","to":10201},{"direction":"east","to":10203}]},
    {"vnum":10203,"name":"失穩環廊","description":"環廊沿著巨大空腔邊緣展開，地面每隔幾步就能看到補封失敗後留下的焦黑方印。","sector_type":"SECT_INSIDE","cluster":"fracture-ring","coord":[2,0,-20],"labels":["mainline"],"exits":[{"direction":"west","to":10202},{"direction":"east","to":10204},{"direction":"south","to":10206}]},
    {"vnum":10204,"name":"裂縫觀測臺","description":"觀測臺外側是一整片翻湧黑紅霧幕，霧幕裡偶爾浮現巨大裂紋影像，像有什麼正在另一側反覆撞擊封界。","sector_type":"SECT_INSIDE","cluster":"fracture-ring","coord":[3,0,-20],"labels":["lore","danger"],"exits":[{"direction":"west","to":10203},{"direction":"east","to":10205}],"enquires":["裂紋","觀測"]},
    {"vnum":10205,"name":"外環鎮柱帶","description":"鎮柱帶排列著高低不一的石柱，柱身符線持續明滅，像在彼此分攤同一道快要超限的壓力。","sector_type":"SECT_INSIDE","cluster":"fracture-ring","coord":[4,0,-20],"labels":["pressure"],"exits":[{"direction":"west","to":10204},{"direction":"south","to":10210}],"keywords":[{"keyword":"鎮柱","description":"石柱底部可見多層加固痕跡，顯示守印者曾反覆替同一批鎮柱續命。"}]},
    {"vnum":10206,"name":"導脈轉廊","description":"轉廊牆面刻滿導脈紋道，細光沿紋路高速流動，將多餘的裂壓導向本核旁廊。","sector_type":"SECT_INSIDE","cluster":"pulse-annex","coord":[2,-1,-20],"labels":["annex"],"exits":[{"direction":"north","to":10203},{"direction":"east","to":10207}],"enquires":["導脈","封紋"]},
    {"vnum":10207,"name":"偏廊監點","description":"監點留下大量測壓刻線與手寫註記，部分數值已高到超出刻板原先量程。","sector_type":"SECT_INSIDE","cluster":"pulse-annex","coord":[3,-1,-20],"labels":["service"],"exits":[{"direction":"west","to":10206},{"direction":"east","to":10208}]},
    {"vnum":10208,"name":"餘壓匯室","description":"匯室中央槽池不斷翻出紅黑氣泡，牆邊放著碎裂的鎮印器具，顯示此處已多次超載。","sector_type":"SECT_INSIDE","cluster":"pulse-annex","coord":[4,-1,-20],"labels":["risk"],"exits":[{"direction":"west","to":10207},{"direction":"east","to":10209}]},
    {"vnum":10209,"name":"封紋備修間","description":"備修間堆著不同年代的補紋石版，有些版面只刻了一半就被高熱燒蝕。","sector_type":"SECT_INSIDE","cluster":"pulse-annex","coord":[5,-1,-20],"labels":["supply","lore"],"exits":[{"direction":"west","to":10208}]},
    {"vnum":10210,"name":"核心前橋","description":"前橋跨過一道垂直裂隙，橋面傳來規律震顫，彷彿每一次脈動都在測試這座橋還能撐多久。","sector_type":"SECT_INSIDE","cluster":"heart-dais","coord":[4,-2,-20],"labels":["bridge","threshold"],"exits":[{"direction":"north","to":10205},{"direction":"south","to":10211}]},
    {"vnum":10211,"name":"核心井緣","description":"井緣石臺圍著一道深不見底的黑紅井口，井壁殘留大片玻化層與剝落鎮紋。","sector_type":"SECT_INSIDE","cluster":"heart-dais","coord":[4,-3,-20],"labels":["well"],"exits":[{"direction":"north","to":10210},{"direction":"down","to":10212}],"enquires":["本核","風險"]},
    {"vnum":10212,"name":"裂界核心臺","description":"核心臺幾乎懸在空中，四周封圈只剩殘片。腳下傳來深井脈動，沿井壁已可辨認出通往下層的承臺微光。","sector_type":"SECT_INSIDE","cluster":"heart-dais","coord":[4,-3,-21],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10211},{"direction":"down","to":10301,"external":true}],"enquires":["深層","核心"]}
  ]
}
```
