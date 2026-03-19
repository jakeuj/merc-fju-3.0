# 裂魄塵界 (`sec_rift_spirit_core_mote`)

## Area Intent

`sec_rift_spirit_core_mote` 承接裂魄微界最深的裂魄微界座，再往下沉入裂魄塵界與塵界深井。此區定位為「塵界深井」：讓玩家從塵界落座、塵界內庭與塵粒偏廊之間，感受到魄壓已從細痕進一步磨成近乎只能以塵粒勉強聚住的層次，並為後續同級更硬的裂魄粒界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄塵界 / 塵界深井`
- LevelRange: `99-100`
- Parent area: `sec_rift_spirit_core_trace`
- ReservedRoomBlock: `12101-12120`

## Planned World Links

- `up` from `12101`: `sec_rift_spirit_core_trace` room `12012`
- `down` from `12112`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_mote",
    "title": "裂魄塵界",
    "design_notes": "裂魄微界之下的塵界深井，作為後續同級 plateau 粒界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_trace",
    "level_range": "99-100",
    "planned_vnum_range": "12101-12120",
    "reserved_room_block": "12101-12120",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄塵界 / 塵界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12101,
        "target_area": "sec_rift_spirit_core_trace",
        "target_room_vnum": 12012,
        "label": "裂魄微界座"
      },
      {
        "direction": "down",
        "source_vnum": 12112,
        "target_area": "sec_rift_spirit_core_grain",
        "label": "裂魄粒界"
      }
    ],
    "clusters": [
      { "id": "mote-shelf", "label": "塵界落座" },
      { "id": "mote-court", "label": "塵界內庭" },
      { "id": "grain-annex", "label": "塵粒偏廊" },
      { "id": "grain-threshold", "label": "粒界前座" }
    ]
  },
  "rooms": [
    {"vnum":12101,"name":"塵界落座","description":"落座像嵌在塵界邊緣的一截聚塵石影，腳下環界已碎成一圈幾乎要被風感吹散的微細塵紋，像連最後殘存的形跡都只剩塵粒還勉強黏在一起。","sector_type":"SECT_INSIDE","cluster":"mote-shelf","coord":[0,0,-58],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12012,"external":true},{"direction":"east","to":12102}],"enquires":["塵界","退路"]},
    {"vnum":12102,"name":"聚塵下階","description":"下階表面已分不出原本的石紋，只剩一層層快要自動散開的聚塵貼著階面向前滑移，讓每一步都像踩在即將重新崩散的界面上。","sector_type":"SECT_INSIDE","cluster":"mote-shelf","coord":[1,0,-58],"labels":["mainline"],"exits":[{"direction":"west","to":12101},{"direction":"east","to":12103}]},
    {"vnum":12103,"name":"塵界內庭前緣","description":"前緣俯瞰整座向內沉落的塵界內庭，庭底像一潭由無數灰細塵點暫時聚住的靜井，視線一旦停得稍久，就會連自己原本還能辨認的重量都被一起削輕。","sector_type":"SECT_INSIDE","cluster":"mote-court","coord":[2,0,-58],"labels":["mainline"],"exits":[{"direction":"west","to":12102},{"direction":"east","to":12104},{"direction":"south","to":12107}]},
    {"vnum":12104,"name":"觀塵鎮魄臺","description":"鎮魄臺旁的觀塵碑只剩幾道像由細灰塵點勉強排出的浮痕，碑與界之間的差別在此只靠一種仍未完全鬆散的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"mote-court","coord":[3,0,-58],"labels":["lore"],"exits":[{"direction":"west","to":12103},{"direction":"east","to":12105}],"enquires":["觀塵","鎮魄"]},
    {"vnum":12105,"name":"塵界聚塵槽","description":"聚塵槽裡沒有流勢可循，只剩一道由細塵反覆聚起又散去的窄痕朝更深處緩慢收束，像整段深井正在把最後殘留的名字磨成一層更細的灰。","sector_type":"SECT_INSIDE","cluster":"mote-court","coord":[4,0,-58],"labels":["pressure"],"exits":[{"direction":"west","to":12104},{"direction":"east","to":12106},{"direction":"south","to":12109}],"keywords":[{"keyword":"聚塵","description":"槽壁封紋已散成難以計數的灰點，只留下把界面持續磨落成更細塵粒的沉靜壓力。"}]},
    {"vnum":12106,"name":"聽塵沉座","description":"沉座中央懸著一枚細得像快要自行崩散的塵晶，晶體不發光也幾乎不留影，只把周圍還能抓得住的層次慢慢磨成更細的灰點。","sector_type":"SECT_INSIDE","cluster":"mote-court","coord":[5,0,-58],"labels":["signal"],"exits":[{"direction":"west","to":12105}]},
    {"vnum":12107,"name":"塵粒側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點更細的灰粒，回頭再看，剛才走過的每一道痕都已淡到只剩一層幾乎握不住的灰。","sector_type":"SECT_INSIDE","cluster":"grain-annex","coord":[2,-1,-58],"labels":["annex"],"exits":[{"direction":"north","to":12103},{"direction":"east","to":12108}]},
    {"vnum":12108,"name":"塵粒偏廊","description":"偏廊兩側嵌著一列列幾乎比塵息還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層極細的灰粒。","sector_type":"SECT_INSIDE","cluster":"grain-annex","coord":[3,-1,-58],"labels":["service"],"exits":[{"direction":"west","to":12107},{"direction":"east","to":12109}],"enquires":["塵粒","偏廊"]},
    {"vnum":12109,"name":"塵界逆廊","description":"逆廊中央橫著一道只在側目時才勉強能被分出的灰細裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的粒界井腹。","sector_type":"SECT_INSIDE","cluster":"grain-annex","coord":[4,-1,-58],"labels":["risk"],"exits":[{"direction":"north","to":12105},{"direction":"west","to":12108},{"direction":"east","to":12110}]},
    {"vnum":12110,"name":"粒界前橋","description":"前橋橫跨在一段已被磨成近乎只剩灰粒浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的細點冷痕，下一瞬便像被更深的粒界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"grain-threshold","coord":[5,-1,-58],"labels":["bridge"],"exits":[{"direction":"west","to":12109},{"direction":"south","to":12111}]},
    {"vnum":12111,"name":"塵界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的灰點，像這裡就是所有界層最後還能勉強聚成塵粒的地方。","sector_type":"SECT_INSIDE","cluster":"grain-threshold","coord":[5,-2,-58],"labels":["threshold"],"exits":[{"direction":"north","to":12110},{"direction":"down","to":12112}],"enquires":["井緣","柱座"]},
    {"vnum":12112,"name":"裂魄塵界座","description":"塵界座像整段塵界深井最後一塊仍勉強聚得住輪廓的聚塵石座，腳下環界只剩一圈隨時會再碎細一層的灰薄紋，所有殘痕都在這裡被拖往更深的裂魄粒界。","sector_type":"SECT_INSIDE","cluster":"grain-threshold","coord":[5,-2,-59],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12111}],"enquires":["塵界座","深處"]}
  ]
}
```
