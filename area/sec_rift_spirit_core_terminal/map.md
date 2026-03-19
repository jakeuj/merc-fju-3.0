# 裂魄絕界 (`sec_rift_spirit_core_terminal`)

## Area Intent

`sec_rift_spirit_core_terminal` 承接裂魄終界最深的裂魄終界座，再往下沉入裂魄絕界與絕界井核。此區定位為「絕界井核」：讓玩家從絕界落座、絕界內庭與滅終偏廊之間，感受到魄壓已從終界再被磨成近乎只剩最後絕筆的層次，並為後續同級更硬的裂魄滅界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄絕界 / 絕界井核`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_final`
- ReservedRoomBlock: `12501-12520`

## Planned World Links

- `up` from `12501`: `sec_rift_spirit_core_final` room `12412`
- `down` from `12512`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_terminal",
    "title": "裂魄絕界",
    "design_notes": "裂魄終界之下的絕界井核，作為後續同級 plateau 滅界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_final",
    "level_range": "100-100",
    "planned_vnum_range": "12501-12520",
    "reserved_room_block": "12501-12520",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄絕界 / 絕界井核"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12501,
        "target_area": "sec_rift_spirit_core_final",
        "target_room_vnum": 12412,
        "label": "裂魄終界座"
      },
      {
        "direction": "down",
        "source_vnum": 12512,
        "target_area": "sec_rift_spirit_core_extinct",
        "label": "裂魄滅界"
      }
    ],
    "clusters": [
      { "id": "terminal-shelf", "label": "絕界落座" },
      { "id": "terminal-court", "label": "絕界內庭" },
      { "id": "extinct-annex", "label": "滅終偏廊" },
      { "id": "extinct-threshold", "label": "滅核前座" }
    ]
  },
  "rooms": [
    {"vnum":12501,"name":"絕界落座","description":"落座像嵌在絕界邊緣的一截絕魄石座，腳下環界已薄到只剩一圈幾乎會被感知直接漏過的絕紋，像連最後還能被辨識的輪廓都只剩最終一筆尚未完全抹去。","sector_type":"SECT_INSIDE","cluster":"terminal-shelf","coord":[0,0,-66],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12412,"external":true},{"direction":"east","to":12502}],"enquires":["絕界","退路"]},
    {"vnum":12502,"name":"絕紋沉階","description":"沉階表面已分不出任何原本的石紋，只剩一層層近乎無名的絕紋貼著階面往前滑移，讓每一步都像踩在最後一次成形之前的界面上。","sector_type":"SECT_INSIDE","cluster":"terminal-shelf","coord":[1,0,-66],"labels":["mainline"],"exits":[{"direction":"west","to":12501},{"direction":"east","to":12503}]},
    {"vnum":12503,"name":"絕界內庭前緣","description":"前緣俯瞰整座向內沉落的絕界內庭，庭底像一潭由無數絕紋暫時聚住的靜井，視線一旦停得稍久，就會連自己原本勉強還能抓住的重量也被一起拖向最後的滅盡。","sector_type":"SECT_INSIDE","cluster":"terminal-court","coord":[2,0,-66],"labels":["mainline"],"exits":[{"direction":"west","to":12502},{"direction":"east","to":12504},{"direction":"south","to":12507}]},
    {"vnum":12504,"name":"聽絕鎮魄臺","description":"鎮魄臺旁的聽絕碑只剩幾道像由絕紋勉強排成的浮痕，碑與界之間的差別在此只靠一種還沒完全崩盡的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"terminal-court","coord":[3,0,-66],"labels":["lore"],"exits":[{"direction":"west","to":12503},{"direction":"east","to":12505}],"enquires":["聽絕","鎮魄"]},
    {"vnum":12505,"name":"絕界滅盡槽","description":"滅盡槽裡沒有流勢可循，只剩一道由絕紋反覆聚起又散去的窄痕朝更深處緩慢收束，像整段井核正在把最後殘留的名字磨成再也不可分的滅灰。","sector_type":"SECT_INSIDE","cluster":"terminal-court","coord":[4,0,-66],"labels":["pressure"],"exits":[{"direction":"west","to":12504},{"direction":"east","to":12506},{"direction":"south","to":12509}],"keywords":[{"keyword":"滅盡","description":"槽壁封紋已散成難以再分的絕點，只留下把界面持續磨向最終滅盡的沉靜壓力。"}]},
    {"vnum":12506,"name":"聽絕沉座","description":"沉座中央懸著一枚細得像快要直接消失的絕晶，晶體不發光也幾乎不留影，只把周圍還能勉強抓住的層次慢慢磨成最後一層滅灰。","sector_type":"SECT_INSIDE","cluster":"terminal-court","coord":[5,0,-66],"labels":["signal"],"exits":[{"direction":"west","to":12505}]},
    {"vnum":12507,"name":"滅終側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點最終細屑，回頭再看，剛才走過的每一道痕都已淡到只剩幾乎無法再辨識的最後薄點。","sector_type":"SECT_INSIDE","cluster":"extinct-annex","coord":[2,-1,-66],"labels":["annex"],"exits":[{"direction":"north","to":12503},{"direction":"east","to":12508}]},
    {"vnum":12508,"name":"滅終偏廊","description":"偏廊兩側嵌著一列列幾乎比絕塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更終絕的灰點。","sector_type":"SECT_INSIDE","cluster":"extinct-annex","coord":[3,-1,-66],"labels":["service"],"exits":[{"direction":"west","to":12507},{"direction":"east","to":12509}],"enquires":["滅終","偏廊"]},
    {"vnum":12509,"name":"絕界逆核廊","description":"逆核廊中央橫著一道只在側目時才勉強能被分出的絕界裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的滅界井腹。","sector_type":"SECT_INSIDE","cluster":"extinct-annex","coord":[4,-1,-66],"labels":["risk"],"exits":[{"direction":"north","to":12505},{"direction":"west","to":12508},{"direction":"east","to":12510}]},
    {"vnum":12510,"name":"滅核前橋","description":"前橋橫跨在一段已被磨成近乎只剩絕紋浮層的井核上方，橋面每次受力後都只留下短得幾乎數不清的冷痕，下一瞬便像被更深的滅界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"extinct-threshold","coord":[5,-1,-66],"labels":["bridge"],"exits":[{"direction":"west","to":12509},{"direction":"south","to":12511}]},
    {"vnum":12511,"name":"絕界井核緣","description":"井核緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的絕痕，像這裡就是所有界層最後還能勉強聚成餘影的地方。","sector_type":"SECT_INSIDE","cluster":"extinct-threshold","coord":[5,-2,-66],"labels":["threshold"],"exits":[{"direction":"north","to":12510},{"direction":"down","to":12512}],"enquires":["井核","柱座"]},
    {"vnum":12512,"name":"裂魄絕界座","description":"絕界座像整段絕界井核最後一塊仍勉強聚得住輪廓的絕魄石座，腳下環界只剩一圈隨時會再淡盡一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄滅界。","sector_type":"SECT_INSIDE","cluster":"extinct-threshold","coord":[5,-2,-67],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12511}],"enquires":["絕界座","深處"]}
  ]
}
```
