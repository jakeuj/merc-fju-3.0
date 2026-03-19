# 裂魄幽玄 (`sec_rift_spirit_core_chthonic`)

## Area Intent

`sec_rift_spirit_core_chthonic` 承接裂魄玄冥最深的裂魄玄冥座，再往下沉入裂魄幽玄與幽玄井腹。此區定位為「幽玄井腹」：讓玩家從幽玄落座、幽玄內庭與冥幽偏廊之間，感受到魄壓已從玄冥再被磨成近乎只剩最後一層幽寂輪廓的層次，並為後續同級更硬的裂魄玄幽層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄幽玄 / 幽玄井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_stygian`
- ReservedRoomBlock: `13301-13320`

## Planned World Links

- `up` from `13301`: `sec_rift_spirit_core_stygian` room `13212`
- `down` from `13312`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_chthonic",
    "title": "裂魄幽玄",
    "design_notes": "裂魄玄冥之下的幽玄井腹，作為後續同級 plateau 玄幽層區前的主段。",
    "parent_area": "sec_rift_spirit_core_stygian",
    "level_range": "100-100",
    "planned_vnum_range": "13301-13320",
    "reserved_room_block": "13301-13320",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄幽玄 / 幽玄井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13301,
        "target_area": "sec_rift_spirit_core_stygian",
        "target_room_vnum": 13212,
        "label": "裂魄玄冥座"
      },
      {
        "direction": "down",
        "source_vnum": 13312,
        "target_area": "sec_rift_spirit_core_abysmal",
        "label": "裂魄玄幽"
      }
    ],
    "clusters": [
      { "id": "chthonic-shelf", "label": "幽玄落座" },
      { "id": "chthonic-court", "label": "幽玄內庭" },
      { "id": "abysmal-annex", "label": "冥幽偏廊" },
      { "id": "abysmal-threshold", "label": "玄幽前座" }
    ]
  },
  "rooms": [
    {"vnum":13301,"name":"幽玄落座","description":"落座像嵌在幽玄邊緣的一截幽魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的幽紋，像連最後還能被辨識的輪廓都被更深處的玄幽慢慢磨成冷寂一筆。","sector_type":"SECT_INSIDE","cluster":"chthonic-shelf","coord":[0,0,-82],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13212,"external":true},{"direction":"east","to":13302}],"enquires":["幽玄","退路"]},
    {"vnum":13302,"name":"幽紋沉階","description":"沉階表面已分不出任何原本的石理，只剩一層層近乎無名的幽紋貼著階面往前滑移，讓每一步都像踩在最後一次沉寂之前仍勉強保持形體的界面上。","sector_type":"SECT_INSIDE","cluster":"chthonic-shelf","coord":[1,0,-82],"labels":["mainline"],"exits":[{"direction":"west","to":13301},{"direction":"east","to":13303}]},
    {"vnum":13303,"name":"幽玄內庭前緣","description":"前緣俯瞰整座向內沉落的幽玄內庭，庭底像一潭由無數幽紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一併拖向更深的幽寂。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[2,0,-82],"labels":["mainline"],"exits":[{"direction":"west","to":13302},{"direction":"east","to":13304},{"direction":"south","to":13307}]},
    {"vnum":13304,"name":"聽幽鎮魄臺","description":"鎮魄臺旁的聽幽碑只剩幾道像由幽紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全墜盡的秩序苦撐，像再深一步就會整片改寫成純粹玄幽。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[3,0,-82],"labels":["lore"],"exits":[{"direction":"west","to":13303},{"direction":"east","to":13305}],"enquires":["聽幽","鎮魄"]},
    {"vnum":13305,"name":"幽玄沉黯槽","description":"沉黯槽裡沒有流勢可循，只剩一道由幽紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的幽灰。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[4,0,-82],"labels":["pressure"],"exits":[{"direction":"west","to":13304},{"direction":"east","to":13306},{"direction":"south","to":13309}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已散成難以再分的幽點，只留下把界面持續磨向更深幽寂的沉靜壓力。"}]},
    {"vnum":13306,"name":"聽幽沉座","description":"沉座中央懸著一枚細得像快要直接消失的幽晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層幽灰。","sector_type":"SECT_INSIDE","cluster":"chthonic-court","coord":[5,0,-82],"labels":["signal"],"exits":[{"direction":"west","to":13305}]},
    {"vnum":13307,"name":"冥幽側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點幽寂細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後冷點。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[2,-1,-82],"labels":["annex"],"exits":[{"direction":"north","to":13303},{"direction":"east","to":13308}]},
    {"vnum":13308,"name":"冥幽偏廊","description":"偏廊兩側嵌著一列列幾乎比幽塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更沉的幽灰。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[3,-1,-82],"labels":["service"],"exits":[{"direction":"west","to":13307},{"direction":"east","to":13309}],"enquires":["冥幽","偏廊"]},
    {"vnum":13309,"name":"幽玄逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的幽玄裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的幽玄井腹。","sector_type":"SECT_INSIDE","cluster":"abysmal-annex","coord":[4,-1,-82],"labels":["risk"],"exits":[{"direction":"north","to":13305},{"direction":"west","to":13308},{"direction":"east","to":13310}]},
    {"vnum":13310,"name":"玄幽前橋","description":"前橋橫跨在一段已被磨成近乎只剩幽紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的玄幽一併吞沒。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-1,-82],"labels":["bridge"],"exits":[{"direction":"west","to":13309},{"direction":"south","to":13311}]},
    {"vnum":13311,"name":"幽玄井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的幽痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-2,-82],"labels":["threshold"],"exits":[{"direction":"north","to":13310},{"direction":"down","to":13312}],"enquires":["井腹","柱座"]},
    {"vnum":13312,"name":"裂魄幽玄座","description":"幽玄座像整段幽玄井腹最後一塊仍勉強聚得住輪廓的幽魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄幽紋，所有殘痕都在這裡被拖往更深的裂魄玄幽。","sector_type":"SECT_INSIDE","cluster":"abysmal-threshold","coord":[5,-2,-83],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13311}],"enquires":["幽玄座","深處"]}
  ]
}
```
