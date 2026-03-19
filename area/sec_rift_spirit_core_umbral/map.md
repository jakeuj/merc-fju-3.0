# 裂魄晦界 (`sec_rift_spirit_core_umbral`)

## Area Intent

`sec_rift_spirit_core_umbral` 承接裂魄微寥最深的裂魄微寥座，再往下沉入裂魄晦界與晦界井腹。此區定位為「晦界井腹」：讓玩家從晦界落座、晦界內庭與冥晦偏廊之間，感受到魄壓已從微寥再被磨成近乎只剩最後一點沉黯輪廓的層次，並為後續同級更硬的裂魄冥界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄晦界 / 晦界井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_gloam`
- ReservedRoomBlock: `13001-13020`

## Planned World Links

- `up` from `13001`: `sec_rift_spirit_core_gloam` room `12912`
- `down` from `13012`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_umbral",
    "title": "裂魄晦界",
    "design_notes": "裂魄微寥之下的晦界井腹，作為後續同級 plateau 冥界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_gloam",
    "level_range": "100-100",
    "planned_vnum_range": "13001-13020",
    "reserved_room_block": "13001-13020",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄晦界 / 晦界井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13001,
        "target_area": "sec_rift_spirit_core_gloam",
        "target_room_vnum": 12912,
        "label": "裂魄微寥座"
      },
      {
        "direction": "down",
        "source_vnum": 13012,
        "target_area": "sec_rift_spirit_core_nether",
        "label": "裂魄冥界"
      }
    ],
    "clusters": [
      { "id": "umbral-shelf", "label": "晦界落座" },
      { "id": "umbral-court", "label": "晦界內庭" },
      { "id": "nether-annex", "label": "冥晦偏廊" },
      { "id": "nether-threshold", "label": "冥核前座" }
    ]
  },
  "rooms": [
    {"vnum":13001,"name":"晦界落座","description":"落座像嵌在晦界邊緣的一截晦魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的晦紋，像連最後還能被辨識的輪廓都只剩薄晦一筆尚未完全抹去。","sector_type":"SECT_INSIDE","cluster":"umbral-shelf","coord":[0,0,-76],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12912,"external":true},{"direction":"east","to":13002}],"enquires":["晦界","退路"]},
    {"vnum":13002,"name":"晦紋沉階","description":"沉階表面已分不出任何原本的石紋，只剩一層層近乎無名的晦紋貼著階面往前滑移，讓每一步都像踩在最後一次晦滅之前的界面上。","sector_type":"SECT_INSIDE","cluster":"umbral-shelf","coord":[1,0,-76],"labels":["mainline"],"exits":[{"direction":"west","to":13001},{"direction":"east","to":13003}]},
    {"vnum":13003,"name":"晦界內庭前緣","description":"前緣俯瞰整座向內沉落的晦界內庭，庭底像一潭由無數晦紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一起拖向最後的沉晦。","sector_type":"SECT_INSIDE","cluster":"umbral-court","coord":[2,0,-76],"labels":["mainline"],"exits":[{"direction":"west","to":13002},{"direction":"east","to":13004},{"direction":"south","to":13007}]},
    {"vnum":13004,"name":"聽晦鎮魄臺","description":"鎮魄臺旁的聽晦碑只剩幾道像由晦紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全崩盡的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"umbral-court","coord":[3,0,-76],"labels":["lore"],"exits":[{"direction":"west","to":13003},{"direction":"east","to":13005}],"enquires":["聽晦","鎮魄"]},
    {"vnum":13005,"name":"晦界沉黯槽","description":"沉黯槽裡沒有流勢可循，只剩一道由晦紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的冥灰。","sector_type":"SECT_INSIDE","cluster":"umbral-court","coord":[4,0,-76],"labels":["pressure"],"exits":[{"direction":"west","to":13004},{"direction":"east","to":13006},{"direction":"south","to":13009}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已散成難以再分的晦點，只留下把界面持續磨向最終沉黯的沉靜壓力。"}]},
    {"vnum":13006,"name":"聽晦沉座","description":"沉座中央懸著一枚細得像快要直接消失的晦晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層冥灰。","sector_type":"SECT_INSIDE","cluster":"umbral-court","coord":[5,0,-76],"labels":["signal"],"exits":[{"direction":"west","to":13005}]},
    {"vnum":13007,"name":"冥晦側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點晦微細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後薄點。","sector_type":"SECT_INSIDE","cluster":"nether-annex","coord":[2,-1,-76],"labels":["annex"],"exits":[{"direction":"north","to":13003},{"direction":"east","to":13008}]},
    {"vnum":13008,"name":"冥晦偏廊","description":"偏廊兩側嵌著一列列幾乎比晦塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更沉晦的灰點。","sector_type":"SECT_INSIDE","cluster":"nether-annex","coord":[3,-1,-76],"labels":["service"],"exits":[{"direction":"west","to":13007},{"direction":"east","to":13009}],"enquires":["冥晦","偏廊"]},
    {"vnum":13009,"name":"晦界逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的晦界裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的冥界井腹。","sector_type":"SECT_INSIDE","cluster":"nether-annex","coord":[4,-1,-76],"labels":["risk"],"exits":[{"direction":"north","to":13005},{"direction":"west","to":13008},{"direction":"east","to":13010}]},
    {"vnum":13010,"name":"冥核前橋","description":"前橋橫跨在一段已被磨成近乎只剩晦紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的冥界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"nether-threshold","coord":[5,-1,-76],"labels":["bridge"],"exits":[{"direction":"west","to":13009},{"direction":"south","to":13011}]},
    {"vnum":13011,"name":"晦界井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的晦痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"nether-threshold","coord":[5,-2,-76],"labels":["threshold"],"exits":[{"direction":"north","to":13010},{"direction":"down","to":13012}],"enquires":["井腹","柱座"]},
    {"vnum":13012,"name":"裂魄晦界座","description":"晦界座像整段晦界井腹最後一塊仍勉強聚得住輪廓的晦魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄冥界。","sector_type":"SECT_INSIDE","cluster":"nether-threshold","coord":[5,-2,-77],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13011}],"enquires":["晦界座","深處"]}
  ]
}
```
