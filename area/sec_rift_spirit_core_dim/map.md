# 裂魄寥界 (`sec_rift_spirit_core_dim`)

## Area Intent

`sec_rift_spirit_core_dim` 承接裂魄寂界最深的裂魄寂界座，再往下沉入裂魄寥界與寥界井腹。此區定位為「寥界井腹」：讓玩家從寥界落座、寥界內庭與微寥偏廊之間，感受到魄壓已從寂界再被磨成近乎只剩最後薄淡輪廓的層次，並為後續同級更硬的裂魄微寥層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄寥界 / 寥界井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_silent`
- ReservedRoomBlock: `12801-12820`

## Planned World Links

- `up` from `12801`: `sec_rift_spirit_core_silent` room `12712`
- `down` from `12812`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_dim",
    "title": "裂魄寥界",
    "design_notes": "裂魄寂界之下的寥界井腹，作為後續同級 plateau 微寥層區前的主段。",
    "parent_area": "sec_rift_spirit_core_silent",
    "level_range": "100-100",
    "planned_vnum_range": "12801-12820",
    "reserved_room_block": "12801-12820",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄寥界 / 寥界井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12801,
        "target_area": "sec_rift_spirit_core_silent",
        "target_room_vnum": 12712,
        "label": "裂魄寂界座"
      },
      {
        "direction": "down",
        "source_vnum": 12812,
        "target_area": "sec_rift_spirit_core_gloam",
        "label": "裂魄微寥"
      }
    ],
    "clusters": [
      { "id": "dim-shelf", "label": "寥界落座" },
      { "id": "dim-court", "label": "寥界內庭" },
      { "id": "gloam-annex", "label": "微寥偏廊" },
      { "id": "gloam-threshold", "label": "微寥前座" }
    ]
  },
  "rooms": [
    {"vnum":12801,"name":"寥界落座","description":"落座像嵌在寥界邊緣的一截寥魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的寥紋，像連最後還能被辨識的輪廓都只剩薄寥一筆尚未完全抹去。","sector_type":"SECT_INSIDE","cluster":"dim-shelf","coord":[0,0,-72],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12712,"external":true},{"direction":"east","to":12802}],"enquires":["寥界","退路"]},
    {"vnum":12802,"name":"寥紋沉階","description":"沉階表面已分不出任何原本的石紋，只剩一層層近乎無名的寥紋貼著階面往前滑移，讓每一步都像踩在最後一次黯淡之前的界面上。","sector_type":"SECT_INSIDE","cluster":"dim-shelf","coord":[1,0,-72],"labels":["mainline"],"exits":[{"direction":"west","to":12801},{"direction":"east","to":12803}]},
    {"vnum":12803,"name":"寥界內庭前緣","description":"前緣俯瞰整座向內沉落的寥界內庭，庭底像一潭由無數寥紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一起拖向最後的薄黯。","sector_type":"SECT_INSIDE","cluster":"dim-court","coord":[2,0,-72],"labels":["mainline"],"exits":[{"direction":"west","to":12802},{"direction":"east","to":12804},{"direction":"south","to":12807}]},
    {"vnum":12804,"name":"聽寥鎮魄臺","description":"鎮魄臺旁的聽寥碑只剩幾道像由寥紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全崩盡的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"dim-court","coord":[3,0,-72],"labels":["lore"],"exits":[{"direction":"west","to":12803},{"direction":"east","to":12805}],"enquires":["聽寥","鎮魄"]},
    {"vnum":12805,"name":"寥界薄黯槽","description":"薄黯槽裡沒有流勢可循，只剩一道由寥紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的黯灰。","sector_type":"SECT_INSIDE","cluster":"dim-court","coord":[4,0,-72],"labels":["pressure"],"exits":[{"direction":"west","to":12804},{"direction":"east","to":12806},{"direction":"south","to":12809}],"keywords":[{"keyword":"薄黯","description":"槽壁封紋已散成難以再分的寥點，只留下把界面持續磨向最終薄黯的沉靜壓力。"}]},
    {"vnum":12806,"name":"聽寥沉座","description":"沉座中央懸著一枚細得像快要直接消失的寥晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層黯灰。","sector_type":"SECT_INSIDE","cluster":"dim-court","coord":[5,0,-72],"labels":["signal"],"exits":[{"direction":"west","to":12805}]},
    {"vnum":12807,"name":"微寥側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點薄寥細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後薄點。","sector_type":"SECT_INSIDE","cluster":"gloam-annex","coord":[2,-1,-72],"labels":["annex"],"exits":[{"direction":"north","to":12803},{"direction":"east","to":12808}]},
    {"vnum":12808,"name":"微寥偏廊","description":"偏廊兩側嵌著一列列幾乎比寥塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更薄黯的灰點。","sector_type":"SECT_INSIDE","cluster":"gloam-annex","coord":[3,-1,-72],"labels":["service"],"exits":[{"direction":"west","to":12807},{"direction":"east","to":12809}],"enquires":["微寥","偏廊"]},
    {"vnum":12809,"name":"寥界逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的寥界裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的微寥井腹。","sector_type":"SECT_INSIDE","cluster":"gloam-annex","coord":[4,-1,-72],"labels":["risk"],"exits":[{"direction":"north","to":12805},{"direction":"west","to":12808},{"direction":"east","to":12810}]},
    {"vnum":12810,"name":"微寥前橋","description":"前橋橫跨在一段已被磨成近乎只剩寥紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的微寥一併吞沒。","sector_type":"SECT_INSIDE","cluster":"gloam-threshold","coord":[5,-1,-72],"labels":["bridge"],"exits":[{"direction":"west","to":12809},{"direction":"south","to":12811}]},
    {"vnum":12811,"name":"寥界井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的寥痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"gloam-threshold","coord":[5,-2,-72],"labels":["threshold"],"exits":[{"direction":"north","to":12810},{"direction":"down","to":12812}],"enquires":["井腹","柱座"]},
    {"vnum":12812,"name":"裂魄寥界座","description":"寥界座像整段寥界井腹最後一塊仍勉強聚得住輪廓的寥魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄微寥。","sector_type":"SECT_INSIDE","cluster":"gloam-threshold","coord":[5,-2,-73],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12811}],"enquires":["寥界座","深處"]}
  ]
}
```
