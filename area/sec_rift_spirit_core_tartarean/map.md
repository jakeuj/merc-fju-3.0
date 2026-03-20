# 裂魄冥淵 (`sec_rift_spirit_core_tartarean`)

## Area Intent

`sec_rift_spirit_core_tartarean` 承接裂魄玄幽最深的裂魄玄幽座，再往下沉入裂魄冥淵與冥淵井腹。此區定位為「冥淵井腹」：讓玩家從冥淵落座、冥淵內庭與淵冥偏廊之間，感受到魄壓已從玄幽再被磨成近乎只剩最後一層冥闇輪廓的層次，並為後續同級更硬的裂魄冥獄層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄冥淵 / 冥淵井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_abysmal`
- ReservedRoomBlock: `13501-13520`

## Planned World Links

- `up` from `13501`: `sec_rift_spirit_core_abysmal` room `13412`
- `down` from `13512`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_tartarean",
    "title": "裂魄冥淵",
    "design_notes": "裂魄玄幽之下的冥淵井腹，作為後續同級 plateau 冥獄層區前的主段。",
    "parent_area": "sec_rift_spirit_core_abysmal",
    "level_range": "100-100",
    "planned_vnum_range": "13501-13520",
    "reserved_room_block": "13501-13520",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄冥淵 / 冥淵井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13501,
        "target_area": "sec_rift_spirit_core_abysmal",
        "target_room_vnum": 13412,
        "label": "裂魄玄幽座"
      },
      {
        "direction": "down",
        "source_vnum": 13512,
        "target_area": "sec_rift_spirit_core_infernal",
        "label": "裂魄冥獄"
      }
    ],
    "clusters": [
      { "id": "tartarean-shelf", "label": "冥淵落座" },
      { "id": "tartarean-court", "label": "冥淵內庭" },
      { "id": "infernal-annex", "label": "淵冥偏廊" },
      { "id": "infernal-threshold", "label": "冥獄前座" }
    ]
  },
  "rooms": [
    {"vnum":13501,"name":"冥淵落座","description":"落座像嵌在冥淵邊緣的一截冥魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的冥紋，像連最後還能被辨識的輪廓都被更深處的冥獄慢慢磨成冷闇一筆。","sector_type":"SECT_INSIDE","cluster":"tartarean-shelf","coord":[0,0,-86],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13412,"external":true},{"direction":"east","to":13502}],"enquires":["冥淵","退路"]},
    {"vnum":13502,"name":"冥紋沉階","description":"沉階表面已分不出任何原本的石理，只剩一層層近乎無名的冥紋貼著階面往前滑移，讓每一步都像踩在最後一次沉墜之前仍勉強保持形體的界面上。","sector_type":"SECT_INSIDE","cluster":"tartarean-shelf","coord":[1,0,-86],"labels":["mainline"],"exits":[{"direction":"west","to":13501},{"direction":"east","to":13503}]},
    {"vnum":13503,"name":"冥淵內庭前緣","description":"前緣俯瞰整座向內沉落的冥淵內庭，庭底像一潭由無數冥紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一併拖向更深的冥闇。","sector_type":"SECT_INSIDE","cluster":"tartarean-court","coord":[2,0,-86],"labels":["mainline"],"exits":[{"direction":"west","to":13502},{"direction":"east","to":13504},{"direction":"south","to":13507}]},
    {"vnum":13504,"name":"聽淵鎮魄臺","description":"鎮魄臺旁的聽淵碑只剩幾道像由冥紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全墜盡的秩序苦撐，像再深一步就會整片改寫成純粹冥獄。","sector_type":"SECT_INSIDE","cluster":"tartarean-court","coord":[3,0,-86],"labels":["lore"],"exits":[{"direction":"west","to":13503},{"direction":"east","to":13505}],"enquires":["聽淵","鎮魄"]},
    {"vnum":13505,"name":"冥淵沉黯槽","description":"沉黯槽裡沒有流勢可循，只剩一道由冥紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井腹正在把最後殘留的名字磨成再也不可分的冥灰。","sector_type":"SECT_INSIDE","cluster":"tartarean-court","coord":[4,0,-86],"labels":["pressure"],"exits":[{"direction":"west","to":13504},{"direction":"east","to":13506},{"direction":"south","to":13509}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已散成難以再分的冥點，只留下把界面持續磨向更深冥闇的沉靜壓力。"}]},
    {"vnum":13506,"name":"聽淵沉座","description":"沉座中央懸著一枚細得像快要直接消失的冥晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層冥灰。","sector_type":"SECT_INSIDE","cluster":"tartarean-court","coord":[5,0,-86],"labels":["signal"],"exits":[{"direction":"west","to":13505}]},
    {"vnum":13507,"name":"淵冥側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點冥闇細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後冷點。","sector_type":"SECT_INSIDE","cluster":"infernal-annex","coord":[2,-1,-86],"labels":["annex"],"exits":[{"direction":"north","to":13503},{"direction":"east","to":13508}]},
    {"vnum":13508,"name":"淵冥偏廊","description":"偏廊兩側嵌著一列列幾乎比冥塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更沉的冥灰。","sector_type":"SECT_INSIDE","cluster":"infernal-annex","coord":[3,-1,-86],"labels":["service"],"exits":[{"direction":"west","to":13507},{"direction":"east","to":13509}],"enquires":["淵冥","偏廊"]},
    {"vnum":13509,"name":"冥淵逆腹廊","description":"逆腹廊中央橫著一道只在側目時才勉強能被分出的冥淵裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的冥淵井腹。","sector_type":"SECT_INSIDE","cluster":"infernal-annex","coord":[4,-1,-86],"labels":["risk"],"exits":[{"direction":"north","to":13505},{"direction":"west","to":13508},{"direction":"east","to":13510}]},
    {"vnum":13510,"name":"冥獄前橋","description":"前橋橫跨在一段已被磨成近乎只剩冥紋浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的冥獄一併吞沒。","sector_type":"SECT_INSIDE","cluster":"infernal-threshold","coord":[5,-1,-86],"labels":["bridge"],"exits":[{"direction":"west","to":13509},{"direction":"south","to":13511}]},
    {"vnum":13511,"name":"冥淵井腹緣","description":"井腹緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的冥痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"infernal-threshold","coord":[5,-2,-86],"labels":["threshold"],"exits":[{"direction":"north","to":13510},{"direction":"down","to":13512}],"enquires":["井腹","柱座"]},
    {"vnum":13512,"name":"裂魄冥淵座","description":"冥淵座像整段冥淵井腹最後一塊仍勉強聚得住輪廓的冥魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄冥紋，所有殘痕都在這裡被拖往更深的裂魄冥獄。","sector_type":"SECT_INSIDE","cluster":"infernal-threshold","coord":[5,-2,-87],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13511}],"enquires":["冥淵座","深處"]}
  ]
}
```
