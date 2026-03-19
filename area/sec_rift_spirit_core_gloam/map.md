# 裂魄微寥 (`sec_rift_spirit_core_gloam`)

## Area Intent

`sec_rift_spirit_core_gloam` 承接裂魄寥界最深的裂魄寥界座，再往下沉入裂魄微寥與微寥井腹。此區定位為「微寥井腹」：讓玩家從微寥落座、微寥內庭與晦微偏廊之間，感受到魄壓已從寥界再被磨成近乎只剩最後一點薄黯輪廓的層次，並為後續同級更硬的裂魄晦界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄微寥 / 微寥井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_dim`
- ReservedRoomBlock: `12901-12920`

## Planned World Links

- `up` from `12901`: `sec_rift_spirit_core_dim` room `12812`
- `down` from `12912`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_gloam",
    "title": "裂魄微寥",
    "design_notes": "裂魄寥界之下的微寥井腹，作為後續同級 plateau 晦界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_dim",
    "level_range": "100-100",
    "planned_vnum_range": "12901-12920",
    "reserved_room_block": "12901-12920",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄微寥 / 微寥井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12901,
        "target_area": "sec_rift_spirit_core_dim",
        "target_room_vnum": 12812,
        "label": "裂魄寥界座"
      },
      {
        "direction": "down",
        "source_vnum": 12912,
        "target_area": "sec_rift_spirit_core_umbral",
        "label": "裂魄晦界"
      }
    ],
    "clusters": [
      { "id": "gloam-shelf", "label": "微寥落座" },
      { "id": "gloam-court", "label": "微寥內庭" },
      { "id": "umbral-annex", "label": "晦微偏廊" },
      { "id": "umbral-threshold", "label": "晦核前座" }
    ]
  },
  "rooms": [
    {"vnum":12901,"name":"微寥落座","description":"落座像嵌在微寥邊緣的一截微寥石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的微紋，像連最後還能被辨識的輪廓都只剩薄寥一筆尚未完全抹去。","sector_type":"SECT_INSIDE","cluster":"gloam-shelf","coord":[0,0,-74],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12812,"external":true},{"direction":"east","to":12902}],"enquires":["微寥","退路"]},
    {"vnum":12902,"name":"微紋沉階","description":"沉階表面已分不出任何原本的石紋，只剩一層層近乎無名的微紋貼著階面往前滑移，讓每一步都像踩在最後一次黯淡之前的界面上。","sector_type":"SECT_INSIDE","cluster":"gloam-shelf","coord":[1,0,-74],"labels":["mainline"],"exits":[{"direction":"west","to":12901},{"direction":"east","to":12903}]},
    {"vnum":12903,"name":"微寥內庭前緣","description":"前緣俯瞰整座向內沉落的微寥內庭，庭底像一潭由無數微紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一起拖向最後的薄晦。","sector_type":"SECT_INSIDE","cluster":"gloam-court","coord":[2,0,-74],"labels":["mainline"],"exits":[{"direction":"west","to":12902},{"direction":"east","to":12904},{"direction":"south","to":12907}]},
    {"vnum":12904,"name":"聽微鎮魄臺","description":"鎮魄臺旁的聽微碑只剩幾道像由微紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全崩盡的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"gloam-court","coord":[3,0,-74],"labels":["lore"],"exits":[{"direction":"west","to":12903},{"direction":"east","to":12905}],"enquires":["聽微","鎮魄"]},
    {"vnum":12905,"name":"微寥薄晦槽","description":"薄晦槽裡沒有流勢可循，只剩一道由微紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的晦灰。","sector_type":"SECT_INSIDE","cluster":"gloam-court","coord":[4,0,-74],"labels":["pressure"],"exits":[{"direction":"west","to":12904},{"direction":"east","to":12906},{"direction":"south","to":12909}],"keywords":[{"keyword":"薄晦","description":"槽壁封紋已散成難以再分的微點，只留下把界面持續磨向最終薄晦的沉靜壓力。"}]},
    {"vnum":12906,"name":"聽微沉座","description":"沉座中央懸著一枚細得像快要直接消失的微晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層晦灰。","sector_type":"SECT_INSIDE","cluster":"gloam-court","coord":[5,0,-74],"labels":["signal"],"exits":[{"direction":"west","to":12905}]},
    {"vnum":12907,"name":"晦微側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點微寥細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後薄點。","sector_type":"SECT_INSIDE","cluster":"umbral-annex","coord":[2,-1,-74],"labels":["annex"],"exits":[{"direction":"north","to":12903},{"direction":"east","to":12908}]},
    {"vnum":12908,"name":"晦微偏廊","description":"偏廊兩側嵌著一列列幾乎比微塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更薄晦的灰點。","sector_type":"SECT_INSIDE","cluster":"umbral-annex","coord":[3,-1,-74],"labels":["service"],"exits":[{"direction":"west","to":12907},{"direction":"east","to":12909}],"enquires":["晦微","偏廊"]},
    {"vnum":12909,"name":"微寥逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的微寥裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的晦界井腹。","sector_type":"SECT_INSIDE","cluster":"umbral-annex","coord":[4,-1,-74],"labels":["risk"],"exits":[{"direction":"north","to":12905},{"direction":"west","to":12908},{"direction":"east","to":12910}]},
    {"vnum":12910,"name":"晦核前橋","description":"前橋橫跨在一段已被磨成近乎只剩微紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的晦界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"umbral-threshold","coord":[5,-1,-74],"labels":["bridge"],"exits":[{"direction":"west","to":12909},{"direction":"south","to":12911}]},
    {"vnum":12911,"name":"微寥井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的微痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"umbral-threshold","coord":[5,-2,-74],"labels":["threshold"],"exits":[{"direction":"north","to":12910},{"direction":"down","to":12912}],"enquires":["井腹","柱座"]},
    {"vnum":12912,"name":"裂魄微寥座","description":"微寥座像整段微寥井腹最後一塊仍勉強聚得住輪廓的微魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄晦界。","sector_type":"SECT_INSIDE","cluster":"umbral-threshold","coord":[5,-2,-75],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12911}],"enquires":["微寥座","深處"]}
  ]
}
```
