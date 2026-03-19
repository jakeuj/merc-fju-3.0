# 裂魄粒界 (`sec_rift_spirit_core_grain`)

## Area Intent

`sec_rift_spirit_core_grain` 承接裂魄塵界最深的裂魄塵界座，再往下沉入裂魄粒界與粒界深井。此區定位為「粒界深井」：讓玩家從粒界落座、粒界內庭與末粒偏廊之間，感受到魄壓已從塵粒再被磨成近乎只能以末粒勉強聚住的層次，並為後續同級更硬的裂魄末界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄粒界 / 粒界深井`
- LevelRange: `99-100`
- Parent area: `sec_rift_spirit_core_mote`
- ReservedRoomBlock: `12201-12220`

## Planned World Links

- `up` from `12201`: `sec_rift_spirit_core_mote` room `12112`
- `down` from `12212`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_grain",
    "title": "裂魄粒界",
    "design_notes": "裂魄塵界之下的粒界深井，作為後續同級 plateau 末界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_mote",
    "level_range": "99-100",
    "planned_vnum_range": "12201-12220",
    "reserved_room_block": "12201-12220",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄粒界 / 粒界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12201,
        "target_area": "sec_rift_spirit_core_mote",
        "target_room_vnum": 12112,
        "label": "裂魄塵界座"
      },
      {
        "direction": "down",
        "source_vnum": 12212,
        "target_area": "sec_rift_spirit_core_last",
        "label": "裂魄末界"
      }
    ],
    "clusters": [
      { "id": "grain-shelf", "label": "粒界落座" },
      { "id": "grain-court", "label": "粒界內庭" },
      { "id": "last-annex", "label": "末粒偏廊" },
      { "id": "last-threshold", "label": "末界前座" }
    ]
  },
  "rooms": [
    {"vnum":12201,"name":"粒界落座","description":"落座像嵌在粒界邊緣的一截聚粒石影，腳下環界已碎成一圈幾乎要被感知漏掉的末粒薄紋，像連最後殘存的形跡都只剩微末粒點還勉強貼在一起。","sector_type":"SECT_INSIDE","cluster":"grain-shelf","coord":[0,0,-60],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":12112,"external":true},{"direction":"east","to":12202}],"enquires":["粒界","退路"]},
    {"vnum":12202,"name":"聚粒下階","description":"下階表面已分不出完整石紋，只剩一層層快要自行散掉的細粒貼著階面向前游移，讓每一步都像踩在即將碎到更細一層的界面上。","sector_type":"SECT_INSIDE","cluster":"grain-shelf","coord":[1,0,-60],"labels":["mainline"],"exits":[{"direction":"west","to":12201},{"direction":"east","to":12203}]},
    {"vnum":12203,"name":"粒界內庭前緣","description":"前緣俯瞰整座向內沉落的粒界內庭，庭底像一潭由無數細粒暫時聚住的靜井，視線一旦停得稍久，就會連自己原本還能握住的重量都被一起磨成更細的末點。","sector_type":"SECT_INSIDE","cluster":"grain-court","coord":[2,0,-60],"labels":["mainline"],"exits":[{"direction":"west","to":12202},{"direction":"east","to":12204},{"direction":"south","to":12207}]},
    {"vnum":12204,"name":"觀粒鎮魄臺","description":"鎮魄臺旁的觀粒碑只剩幾道像由細粒勉強排成的浮痕，碑與界之間的差別在此只靠一種仍未完全粉碎的秩序苦撐。","sector_type":"SECT_INSIDE","cluster":"grain-court","coord":[3,0,-60],"labels":["lore"],"exits":[{"direction":"west","to":12203},{"direction":"east","to":12205}],"enquires":["觀粒","鎮魄"]},
    {"vnum":12205,"name":"粒界聚粒槽","description":"聚粒槽裡沒有流勢可循，只剩一道由細粒反覆聚起又散去的窄痕朝更深處緩慢收束，像整段深井正在把最後殘留的名字磨成更末的一層粒霧。","sector_type":"SECT_INSIDE","cluster":"grain-court","coord":[4,0,-60],"labels":["pressure"],"exits":[{"direction":"west","to":12204},{"direction":"east","to":12206},{"direction":"south","to":12209}],"keywords":[{"keyword":"聚粒","description":"槽壁封紋已散成難以細分的粒點，只留下把界面持續磨落成更末細粒的沉靜壓力。"}]},
    {"vnum":12206,"name":"聽粒沉座","description":"沉座中央懸著一枚細得像快要自行裂散的粒晶，晶體不發光也幾乎不留影，只把周圍還能抓住的層次慢慢磨成更末細的粒點。","sector_type":"SECT_INSIDE","cluster":"grain-court","coord":[5,0,-60],"labels":["signal"],"exits":[{"direction":"west","to":12205}]},
    {"vnum":12207,"name":"末粒側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一點點更末的細粒，回頭再看，剛才走過的每一道痕都已淡到只剩一層幾乎無法再握住的末灰。","sector_type":"SECT_INSIDE","cluster":"last-annex","coord":[2,-1,-60],"labels":["annex"],"exits":[{"direction":"north","to":12203},{"direction":"east","to":12208}]},
    {"vnum":12208,"name":"末粒偏廊","description":"偏廊兩側嵌著一列列幾乎比末塵還輕的導響殼片，殼面已不再回應完整聲響，只會把人的念頭磨成一層層更末細的粒灰。","sector_type":"SECT_INSIDE","cluster":"last-annex","coord":[3,-1,-60],"labels":["service"],"exits":[{"direction":"west","to":12207},{"direction":"east","to":12209}],"enquires":["末粒","偏廊"]},
    {"vnum":12209,"name":"粒界逆廊","description":"逆廊中央橫著一道只在側目時才勉強能被分出的末細裂痕，縫底既沒有重量也沒有回聲，卻像能把最後還留得住的形名慢慢拖往更深的末界井腹。","sector_type":"SECT_INSIDE","cluster":"last-annex","coord":[4,-1,-60],"labels":["risk"],"exits":[{"direction":"north","to":12205},{"direction":"west","to":12208},{"direction":"east","to":12210}]},
    {"vnum":12210,"name":"末界前橋","description":"前橋橫跨在一段已被磨成近乎只剩末粒浮層的井腹上方，橋面每次受力後都只留下短得幾乎數不清的末點冷痕，下一瞬便像被更深的末界一併吞沒。","sector_type":"SECT_INSIDE","cluster":"last-threshold","coord":[5,-1,-60],"labels":["bridge"],"exits":[{"direction":"west","to":12209},{"direction":"south","to":12211}]},
    {"vnum":12211,"name":"粒界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈幾乎無法再細分的末粒點，像這裡就是所有界層最後還能勉強聚成粒點的地方。","sector_type":"SECT_INSIDE","cluster":"last-threshold","coord":[5,-2,-60],"labels":["threshold"],"exits":[{"direction":"north","to":12210},{"direction":"down","to":12212}],"enquires":["井緣","柱座"]},
    {"vnum":12212,"name":"裂魄粒界座","description":"粒界座像整段粒界深井最後一塊仍勉強聚得住輪廓的聚粒石座，腳下環界只剩一圈隨時會再碎末一層的細薄紋，所有殘痕都在這裡被拖往更深的裂魄末界。","sector_type":"SECT_INSIDE","cluster":"last-threshold","coord":[5,-2,-61],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12211}],"enquires":["粒界座","深處"]}
  ]
}
```
