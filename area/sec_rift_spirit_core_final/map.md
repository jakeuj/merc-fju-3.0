# 裂魄終界 (`sec_rift_spirit_core_final`)

## Area Intent

`sec_rift_spirit_core_final` 承接裂魄末界最深的裂魄末界座，再往下沉入裂魄終界與終界井腹。此區定位為「終界井腹」：讓玩家從終界落座、終界內庭與極終偏廊之間，感受到魄壓已從末界再被磨成近乎只剩最終一筆輪廓的層次，並為後續同級更硬的裂魄絕界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄終界 / 終界井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_last`
- ReservedRoomBlock: `12401-12420`

## Planned World Links

- `up` from `12401`: `sec_rift_spirit_core_last` room `12312`
- `down` from `12412`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_final",
    "title": "裂魄終界",
    "design_notes": "裂魄末界之下的終界井腹，作為後續同級 plateau 絕界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_last",
    "level_range": "100-100",
    "planned_vnum_range": "12401-12420",
    "reserved_room_block": "12401-12420",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄終界 / 終界井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12401,
        "target_area": "sec_rift_spirit_core_last",
        "target_room_vnum": 12312,
        "label": "裂魄末界座"
      },
      {
        "direction": "down",
        "source_vnum": 12412,
        "target_area": "sec_rift_spirit_core_terminal",
        "label": "裂魄絕界"
      }
    ],
    "clusters": [
      { "id": "final-shelf", "label": "終界落座" },
      { "id": "final-court", "label": "終界內庭" },
      { "id": "terminal-annex", "label": "極終偏廊" },
      { "id": "terminal-threshold", "label": "終核前座" }
    ]
  },
  "rooms": [
    {"vnum":12401,"name":"終界落座","description":"落座像嵌在終界邊緣的一截終魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的終紋，像連最後還能被辨識的輪廓都只剩最終一筆尚未完全抹去。","sector_type":"SECT_INSIDE","cluster":"final-shelf","coord":[0,0,-64],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12312,"external":true},{"direction":"east","to":12402}],"enquires":["終界","退路"]},
    {"vnum":12402,"name":"終紋沉階","description":"沉階表面已分不出任何原本的石紋，只剩一層層近乎無名的終紋貼著階面往前滑移，讓每一步都像踩在最後一次成形之前的界面上。","sector_type":"SECT_INSIDE","cluster":"final-shelf","coord":[1,0,-64],"labels":["mainline"],"exits":[{"direction":"west","to":12401},{"direction":"east","to":12403}]},
    {"vnum":12403,"name":"終界內庭前緣","description":"前緣俯瞰整座向內沉落的終界內庭，庭底像一潭由無數終紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一起拖向最後的歸盡。","sector_type":"SECT_INSIDE","cluster":"final-court","coord":[2,0,-64],"labels":["mainline"],"exits":[{"direction":"west","to":12402},{"direction":"east","to":12404},{"direction":"south","to":12407}]},
    {"vnum":12404,"name":"聽終鎮魄臺","description":"鎮魄臺旁的聽終碑只剩幾道像由終紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全崩盡的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"final-court","coord":[3,0,-64],"labels":["lore"],"exits":[{"direction":"west","to":12403},{"direction":"east","to":12405}],"enquires":["聽終","鎮魄"]},
    {"vnum":12405,"name":"終界歸盡槽","description":"歸盡槽裡沒有流勢可循，只剩一道由終紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的終灰。","sector_type":"SECT_INSIDE","cluster":"final-court","coord":[4,0,-64],"labels":["pressure"],"exits":[{"direction":"west","to":12404},{"direction":"east","to":12406},{"direction":"south","to":12409}],"keywords":[{"keyword":"歸盡","description":"槽壁封紋已散成難以再分的終點，只留下把界面持續磨向最終寂盡的沉靜壓力。"}]},
    {"vnum":12406,"name":"聽終沉座","description":"沉座中央懸著一枚細得像快要直接消失的終晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層冷灰。","sector_type":"SECT_INSIDE","cluster":"final-court","coord":[5,0,-64],"labels":["signal"],"exits":[{"direction":"west","to":12405}]},
    {"vnum":12407,"name":"極終側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點最終細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後薄點。","sector_type":"SECT_INSIDE","cluster":"terminal-annex","coord":[2,-1,-64],"labels":["annex"],"exits":[{"direction":"north","to":12403},{"direction":"east","to":12408}]},
    {"vnum":12408,"name":"極終偏廊","description":"偏廊兩側嵌著一列列幾乎比終塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更終末的灰點。","sector_type":"SECT_INSIDE","cluster":"terminal-annex","coord":[3,-1,-64],"labels":["service"],"exits":[{"direction":"west","to":12407},{"direction":"east","to":12409}],"enquires":["極終","偏廊"]},
    {"vnum":12409,"name":"終界逆井廊","description":"逆井廊中央橫著一道只在側目時才勉強能被分出的終界裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的絕界井腹。","sector_type":"SECT_INSIDE","cluster":"terminal-annex","coord":[4,-1,-64],"labels":["risk"],"exits":[{"direction":"north","to":12405},{"direction":"west","to":12408},{"direction":"east","to":12410}]},
    {"vnum":12410,"name":"終核前橋","description":"前橋橫跨在一段已被磨成近乎只剩終紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的絕界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"terminal-threshold","coord":[5,-1,-64],"labels":["bridge"],"exits":[{"direction":"west","to":12409},{"direction":"south","to":12411}]},
    {"vnum":12411,"name":"終界井心緣","description":"井心緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的終痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"terminal-threshold","coord":[5,-2,-64],"labels":["threshold"],"exits":[{"direction":"north","to":12410},{"direction":"down","to":12412}],"enquires":["井心","柱座"]},
    {"vnum":12412,"name":"裂魄終界座","description":"終界座像整段終界井腹最後一塊仍勉強聚得住輪廓的終魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄絕界。","sector_type":"SECT_INSIDE","cluster":"terminal-threshold","coord":[5,-2,-65],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12411}],"enquires":["終界座","深處"]}
  ]
}
```
