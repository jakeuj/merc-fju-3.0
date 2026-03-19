# 裂魄末界 (`sec_rift_spirit_core_last`)

## Area Intent

`sec_rift_spirit_core_last` 承接裂魄粒界最深的裂魄粒界座，再往下沉入裂魄末界與末界深井。此區定位為「末界深井」：讓玩家從末界落座、末界內庭與終塵偏廊之間，感受到魄壓已從末粒再被磨成近乎只剩最末餘點的層次，並為後續同級更硬的裂魄終界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄末界 / 末界深井`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_grain`
- ReservedRoomBlock: `12301-12320`

## Planned World Links

- `up` from `12301`: `sec_rift_spirit_core_grain` room `12212`
- `down` from `12312`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_last",
    "title": "裂魄末界",
    "design_notes": "裂魄粒界之下的末界深井，作為後續同級 plateau 終界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_grain",
    "level_range": "100-100",
    "planned_vnum_range": "12301-12320",
    "reserved_room_block": "12301-12320",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄末界 / 末界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12301,
        "target_area": "sec_rift_spirit_core_grain",
        "target_room_vnum": 12212,
        "label": "裂魄粒界座"
      },
      {
        "direction": "down",
        "source_vnum": 12312,
        "target_area": "sec_rift_spirit_core_final",
        "label": "裂魄終界"
      }
    ],
    "clusters": [
      { "id": "last-shelf", "label": "末界落座" },
      { "id": "last-court", "label": "末界內庭" },
      { "id": "final-annex", "label": "終塵偏廊" },
      { "id": "final-threshold", "label": "終界前座" }
    ]
  },
  "rooms": [
    {"vnum":12301,"name":"末界落座","description":"落座像嵌在末界邊緣的一截末影石座，腳下環界已薄到只剩一圈幾乎要被感知直接漏過的終末細紋，像連最後殘存的形跡都只剩最末的灰點還勉強黏在一起。","sector_type":"SECT_INSIDE","cluster":"last-shelf","coord":[0,0,-62],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12212,"external":true},{"direction":"east","to":12302}],"enquires":["末界","退路"]},
    {"vnum":12302,"name":"末影下階","description":"下階表面已分不出原本的石紋，只剩一層層快要自行散滅的末影貼著階面向前挪移，讓每一步都像踩在即將被徹底磨盡的界面上。","sector_type":"SECT_INSIDE","cluster":"last-shelf","coord":[1,0,-62],"labels":["mainline"],"exits":[{"direction":"west","to":12301},{"direction":"east","to":12303}]},
    {"vnum":12303,"name":"末界內庭前緣","description":"前緣俯瞰整座向內沉落的末界內庭，庭底像一潭由無數終末灰點暫時聚住的靜井，視線一旦停得稍久，就會連自己原本還能辨認的重量也被一起拖向最後的寂薄。","sector_type":"SECT_INSIDE","cluster":"last-court","coord":[2,0,-62],"labels":["mainline"],"exits":[{"direction":"west","to":12302},{"direction":"east","to":12304},{"direction":"south","to":12307}]},
    {"vnum":12304,"name":"觀末鎮魄臺","description":"鎮魄臺旁的觀末碑只剩幾道像由末點勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全湮滅的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"last-court","coord":[3,0,-62],"labels":["lore"],"exits":[{"direction":"west","to":12303},{"direction":"east","to":12305}],"enquires":["觀末","鎮魄"]},
    {"vnum":12305,"name":"末界凝盡槽","description":"凝盡槽裡沒有流勢可循，只剩一道由末點反覆聚起又散去的窄痕朝更深處緩慢收束，像整段深井正在把最後殘留的名字磨成再也不可分的終灰。","sector_type":"SECT_INSIDE","cluster":"last-court","coord":[4,0,-62],"labels":["pressure"],"exits":[{"direction":"west","to":12304},{"direction":"east","to":12306},{"direction":"south","to":12309}],"keywords":[{"keyword":"凝盡","description":"槽壁封紋已散成難以再分的末點，只留下把界面持續磨向終末寂盡的沉靜壓力。"}]},
    {"vnum":12306,"name":"聽末沉座","description":"沉座中央懸著一枚細得像快要直接消失的末晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層暗灰。","sector_type":"SECT_INSIDE","cluster":"last-court","coord":[5,0,-62],"labels":["signal"],"exits":[{"direction":"west","to":12305}]},
    {"vnum":12307,"name":"終塵側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點終末細塵，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後灰點。","sector_type":"SECT_INSIDE","cluster":"final-annex","coord":[2,-1,-62],"labels":["annex"],"exits":[{"direction":"north","to":12303},{"direction":"east","to":12308}]},
    {"vnum":12308,"name":"終塵偏廊","description":"偏廊兩側嵌著一列列幾乎比末塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層最後殘存的灰點。","sector_type":"SECT_INSIDE","cluster":"final-annex","coord":[3,-1,-62],"labels":["service"],"exits":[{"direction":"west","to":12307},{"direction":"east","to":12309}],"enquires":["終塵","偏廊"]},
    {"vnum":12309,"name":"末界逆廊","description":"逆廊中央橫著一道只在側目時才勉強能被分出的終末裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的終界井腹。","sector_type":"SECT_INSIDE","cluster":"final-annex","coord":[4,-1,-62],"labels":["risk"],"exits":[{"direction":"north","to":12305},{"direction":"west","to":12308},{"direction":"east","to":12310}]},
    {"vnum":12310,"name":"終界前橋","description":"前橋橫跨在一段已被磨成近乎只剩終末浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的終點冷痕，下一瞬便像被更深的終界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"final-threshold","coord":[5,-1,-62],"labels":["bridge"],"exits":[{"direction":"west","to":12309},{"direction":"south","to":12311}]},
    {"vnum":12311,"name":"末界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的終末點，像這裡就是所有界層最後還能勉強聚成餘點的地方。","sector_type":"SECT_INSIDE","cluster":"final-threshold","coord":[5,-2,-62],"labels":["threshold"],"exits":[{"direction":"north","to":12310},{"direction":"down","to":12312}],"enquires":["井緣","柱座"]},
    {"vnum":12312,"name":"裂魄末界座","description":"末界座像整段末界深井最後一塊仍勉強聚得住輪廓的終末石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄終界。","sector_type":"SECT_INSIDE","cluster":"final-threshold","coord":[5,-2,-63],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12311}],"enquires":["末界座","深處"]}
  ]
}
```
