# 裂魄冥界 (`sec_rift_spirit_core_nether`)

## Area Intent

`sec_rift_spirit_core_nether` 承接裂魄晦界最深的裂魄晦界座，再往下沉入裂魄冥界與冥界井腹。此區定位為「冥界井腹」：讓玩家從冥界落座、冥界內庭與幽冥偏廊之間，感受到魄壓已從晦界再被磨成近乎只剩最後一層陰冥輪廓的層次，並為後續同級更硬的裂魄玄冥層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄冥界 / 冥界井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_umbral`
- ReservedRoomBlock: `13101-13120`

## Planned World Links

- `up` from `13101`: `sec_rift_spirit_core_umbral` room `13012`
- `down` from `13112`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_nether",
    "title": "裂魄冥界",
    "design_notes": "裂魄晦界之下的冥界井腹，作為後續同級 plateau 玄冥層區前的主段。",
    "parent_area": "sec_rift_spirit_core_umbral",
    "level_range": "100-100",
    "planned_vnum_range": "13101-13120",
    "reserved_room_block": "13101-13120",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄冥界 / 冥界井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13101,
        "target_area": "sec_rift_spirit_core_umbral",
        "target_room_vnum": 13012,
        "label": "裂魄晦界座"
      },
      {
        "direction": "down",
        "source_vnum": 13112,
        "target_area": "sec_rift_spirit_core_stygian",
        "label": "裂魄玄冥"
      }
    ],
    "clusters": [
      { "id": "nether-shelf", "label": "冥界落座" },
      { "id": "nether-court", "label": "冥界內庭" },
      { "id": "stygian-annex", "label": "幽冥偏廊" },
      { "id": "stygian-threshold", "label": "玄冥前座" }
    ]
  },
  "rooms": [
    {"vnum":13101,"name":"冥界落座","description":"落座像嵌在冥界邊緣的一截陰魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的冥紋，像連最後還能被辨識的輪廓都被更深處的玄冥慢慢磨成冷薄一筆。","sector_type":"SECT_INSIDE","cluster":"nether-shelf","coord":[0,0,-78],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13012,"external":true},{"direction":"east","to":13102}],"enquires":["冥界","退路"]},
    {"vnum":13102,"name":"冥紋沉階","description":"沉階表面已分不出任何原本的石理，只剩一層層近乎無名的冥紋貼著階面往前滑移，讓每一步都像踩在最後一次沉滅之前仍勉強保持形體的界面上。","sector_type":"SECT_INSIDE","cluster":"nether-shelf","coord":[1,0,-78],"labels":["mainline"],"exits":[{"direction":"west","to":13101},{"direction":"east","to":13103}]},
    {"vnum":13103,"name":"冥界內庭前緣","description":"前緣俯瞰整座向內沉落的冥界內庭，庭底像一潭由無數冥紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一併拖向更深的陰冥。","sector_type":"SECT_INSIDE","cluster":"nether-court","coord":[2,0,-78],"labels":["mainline"],"exits":[{"direction":"west","to":13102},{"direction":"east","to":13104},{"direction":"south","to":13107}]},
    {"vnum":13104,"name":"聽冥鎮魄臺","description":"鎮魄臺旁的聽冥碑只剩幾道像由冥紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全墜盡的秩序苦撐，像再深一步就會整片改寫成純粹玄冥。","sector_type":"SECT_INSIDE","cluster":"nether-court","coord":[3,0,-78],"labels":["lore"],"exits":[{"direction":"west","to":13103},{"direction":"east","to":13105}],"enquires":["聽冥","鎮魄"]},
    {"vnum":13105,"name":"冥界沉黯槽","description":"沉黯槽裡沒有流勢可循，只剩一道由冥紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的陰灰。","sector_type":"SECT_INSIDE","cluster":"nether-court","coord":[4,0,-78],"labels":["pressure"],"exits":[{"direction":"west","to":13104},{"direction":"east","to":13106},{"direction":"south","to":13109}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已散成難以再分的冥點，只留下把界面持續磨向更深陰冥的沉靜壓力。"}]},
    {"vnum":13106,"name":"聽冥沉座","description":"沉座中央懸著一枚細得像快要直接消失的冥晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層陰灰。","sector_type":"SECT_INSIDE","cluster":"nether-court","coord":[5,0,-78],"labels":["signal"],"exits":[{"direction":"west","to":13105}]},
    {"vnum":13107,"name":"幽冥側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點陰冥細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後冷點。","sector_type":"SECT_INSIDE","cluster":"stygian-annex","coord":[2,-1,-78],"labels":["annex"],"exits":[{"direction":"north","to":13103},{"direction":"east","to":13108}]},
    {"vnum":13108,"name":"幽冥偏廊","description":"偏廊兩側嵌著一列列幾乎比冥塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更沉的陰灰。","sector_type":"SECT_INSIDE","cluster":"stygian-annex","coord":[3,-1,-78],"labels":["service"],"exits":[{"direction":"west","to":13107},{"direction":"east","to":13109}],"enquires":["幽冥","偏廊"]},
    {"vnum":13109,"name":"冥界逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的冥界裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的冥界井腹。","sector_type":"SECT_INSIDE","cluster":"stygian-annex","coord":[4,-1,-78],"labels":["risk"],"exits":[{"direction":"north","to":13105},{"direction":"west","to":13108},{"direction":"east","to":13110}]},
    {"vnum":13110,"name":"玄冥前橋","description":"前橋橫跨在一段已被磨成近乎只剩冥紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的玄冥一併吞沒。","sector_type":"SECT_INSIDE","cluster":"stygian-threshold","coord":[5,-1,-78],"labels":["bridge"],"exits":[{"direction":"west","to":13109},{"direction":"south","to":13111}]},
    {"vnum":13111,"name":"冥界井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的冥痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"stygian-threshold","coord":[5,-2,-78],"labels":["threshold"],"exits":[{"direction":"north","to":13110},{"direction":"down","to":13112}],"enquires":["井腹","柱座"]},
    {"vnum":13112,"name":"裂魄冥界座","description":"冥界座像整段冥界井腹最後一塊仍勉強聚得住輪廓的陰魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄冥紋，所有殘痕都在這裡被拖往更深的裂魄玄冥。","sector_type":"SECT_INSIDE","cluster":"stygian-threshold","coord":[5,-2,-79],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13111}],"enquires":["冥界座","深處"]}
  ]
}
```
