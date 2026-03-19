# 裂魄玄幽 (`sec_rift_spirit_core_abysmal`)

## Area Intent

`sec_rift_spirit_core_abysmal` 承接裂魄幽玄最深的裂魄幽玄座，再往下沉入裂魄玄幽與玄幽井腹。此區定位為「玄幽井腹」：讓玩家從玄幽落座、玄幽內庭與幽冥偏廊之間，感受到魄壓已從幽玄再被磨成近乎只剩最後一層玄黯輪廓的層次，並為後續同級更硬的裂魄冥淵層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄玄幽 / 玄幽井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_chthonic`
- ReservedRoomBlock: `13401-13420`

## Planned World Links

- `up` from `13401`: `sec_rift_spirit_core_chthonic` room `13312`
- `down` from `13412`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_abysmal",
    "title": "裂魄玄幽",
    "design_notes": "裂魄幽玄之下的玄幽井腹，作為後續同級 plateau 冥淵層區前的主段。",
    "parent_area": "sec_rift_spirit_core_chthonic",
    "level_range": "100-100",
    "planned_vnum_range": "13401-13420",
    "reserved_room_block": "13401-13420",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄玄幽 / 玄幽井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13401,
        "target_area": "sec_rift_spirit_core_chthonic",
        "target_room_vnum": 13312,
        "label": "裂魄幽玄座"
      },
      {
        "direction": "down",
        "source_vnum": 13412,
        "target_area": "sec_rift_spirit_core_tartarean",
        "label": "裂魄冥淵"
      }
    ],
    "clusters": [
      { "id": "chthonic-shelf", "label": "玄幽落座" },
      { "id": "chthonic-court", "label": "玄幽內庭" },
      { "id": "abysmal-annex", "label": "幽冥偏廊" },
      { "id": "abysmal-threshold", "label": "玄幽前座" }
    ]
  },
  "rooms": [
    {"vnum":13401,"name":"玄幽落座","description":"落座像嵌在玄幽邊緣的一截玄魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的玄紋，像連最後還能被辨識的輪廓都被更深處的冥淵慢慢磨成冷寂一筆。","sector_type":"SECT_INSIDE","cluster":"chthonic-shelf","coord":[0,0,-84],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13312,"external":true},{"direction":"east","to":13402}],"enquires":["玄幽","退路"]},
    {"vnum":13402,"name":"幽紋沉階","description":"沉階表面已分不出任何原本的石理，只剩一層層近乎無名的幽紋貼著階面往前滑移，讓每一步都像踩在最後一次沉寂之前仍勉強保持形體的界面上。","sector_type":"SECT_INSIDE","cluster":"chthonic-shelf","coord":[1,0,-82],"labels":["mainline"],"exits":[{"direction":"west","to":13401},{"direction":"east","to":13403}]},
    {"vnum":13403,"name":"玄幽內庭前緣","description":"前緣俯瞰整座向內沉落的玄幽內庭，庭底像一潭由無數幽紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一併拖向更深的幽寂。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[2,0,-82],"labels":["mainline"],"exits":[{"direction":"west","to":13402},{"direction":"east","to":13404},{"direction":"south","to":13407}]},
    {"vnum":13404,"name":"聽幽鎮魄臺","description":"鎮魄臺旁的聽幽碑只剩幾道像由幽紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全墜盡的秩序苦撐，像再深一步就會整片改寫成純粹玄幽。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[3,0,-82],"labels":["lore"],"exits":[{"direction":"west","to":13403},{"direction":"east","to":13405}],"enquires":["聽幽","鎮魄"]},
    {"vnum":13405,"name":"玄幽沉黯槽","description":"沉黯槽裡沒有流勢可循，只剩一道由幽紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的幽灰。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[4,0,-82],"labels":["pressure"],"exits":[{"direction":"west","to":13404},{"direction":"east","to":13406},{"direction":"south","to":13409}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已散成難以再分的幽點，只留下把界面持續磨向更深幽寂的沉靜壓力。"}]},
    {"vnum":13406,"name":"聽幽沉座","description":"沉座中央懸著一枚細得像快要直接消失的幽晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層幽灰。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[5,0,-82],"labels":["signal"],"exits":[{"direction":"west","to":13405}]},
    {"vnum":13407,"name":"幽冥側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點幽寂細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後冷點。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[2,-1,-82],"labels":["annex"],"exits":[{"direction":"north","to":13403},{"direction":"east","to":13408}]},
    {"vnum":13408,"name":"幽冥偏廊","description":"偏廊兩側嵌著一列列幾乎比幽塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更沉的幽灰。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[3,-1,-82],"labels":["service"],"exits":[{"direction":"west","to":13407},{"direction":"east","to":13409}],"enquires":["幽冥","偏廊"]},
    {"vnum":13409,"name":"玄幽逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的玄幽裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的玄幽井腹。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[4,-1,-82],"labels":["risk"],"exits":[{"direction":"north","to":13405},{"direction":"west","to":13408},{"direction":"east","to":13410}]},
    {"vnum":13410,"name":"玄幽前橋","description":"前橋橫跨在一段已被磨成近乎只剩幽紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的玄幽一併吞沒。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-1,-82],"labels":["bridge"],"exits":[{"direction":"west","to":13409},{"direction":"south","to":13411}]},
    {"vnum":13411,"name":"玄幽井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的幽痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-2,-82],"labels":["threshold"],"exits":[{"direction":"north","to":13410},{"direction":"down","to":13412}],"enquires":["井腹","柱座"]},
    {"vnum":13412,"name":"裂魄玄幽座","description":"玄幽座像整段玄幽井腹最後一塊仍勉強聚得住輪廓的玄魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄玄紋，所有殘痕都在這裡被拖往更深的裂魄冥淵。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-2,-85],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13411}],"enquires":["玄幽座","深處"]}
  ]
}
```
