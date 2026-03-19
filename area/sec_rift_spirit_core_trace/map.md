# 裂魄微界 (`sec_rift_spirit_core_trace`)

## Area Intent

`sec_rift_spirit_core_trace` 承接裂魄澹界最深的裂魄澹界座，再往下沉入裂魄微界與微界深井。此區定位為「微界深井」：讓玩家從微界落座、微界內庭與細痕偏廊之間，感受到魄壓已從餘意再被壓縮到只剩極細痕粒，並為後續同級更硬的裂魄塵界層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄微界 / 微界深井`
- LevelRange: `98-100`
- Parent area: `sec_rift_spirit_core_faint`
- ReservedRoomBlock: `12001-12020`

## Planned World Links

- `up` from `12001`: `sec_rift_spirit_core_faint` room `11912`
- `down` from `12012`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_trace",
    "title": "裂魄微界",
    "design_notes": "裂魄澹界之下的微界深井，作為後續同級 plateau 塵界層區前的主段。",
    "parent_area": "sec_rift_spirit_core_faint",
    "level_range": "98-100",
    "planned_vnum_range": "12001-12020",
    "reserved_room_block": "12001-12020",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄微界 / 微界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 12001,
        "target_area": "sec_rift_spirit_core_faint",
        "target_room_vnum": 11912,
        "label": "裂魄澹界座"
      },
      {
        "direction": "down",
        "source_vnum": 12012,
        "target_area": "sec_rift_spirit_core_mote",
        "label": "裂魄塵界"
      }
    ],
    "clusters": [
      { "id": "trace-shelf", "label": "微界落座" },
      { "id": "trace-court", "label": "微界內庭" },
      { "id": "trace-annex", "label": "細痕偏廊" },
      { "id": "mote-threshold", "label": "塵界前座" }
    ]
  },
  "rooms": [
    {"vnum":12001,"name":"微界落座","description":"落座像嵌在微界邊緣的一截細痕石影，腳下環界已收縮到只剩一圈幾乎要漏過感知的薄紋，像連最後那點餘意都在此被磨成極細的粒痕。","sector_type":"SECT_INSIDE","cluster":"trace-shelf","coord":[0,0,-56],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11912,"external":true},{"direction":"east","to":12002}],"enquires":["微界","退路"]},
    {"vnum":12002,"name":"細痕下階","description":"下階表面已看不出完整石紋，只剩一道道幾乎會在視線剛碰到時就散開的細痕貼著階面延伸，讓每一步都像踩在快要被抹去的界線上。","sector_type":"SECT_INSIDE","cluster":"trace-shelf","coord":[1,0,-56],"labels":["mainline"],"exits":[{"direction":"west","to":12001},{"direction":"east","to":12003}]},
    {"vnum":12003,"name":"微界內庭前緣","description":"前緣俯瞰整座向內沉落的微界內庭，庭底像一潭由無數極細痕粒暫時聚住的靜井，視線只要停得稍久，連自己原本握住的輪廓都像會被一起削薄。","sector_type":"SECT_INSIDE","cluster":"trace-court","coord":[2,0,-56],"labels":["mainline"],"exits":[{"direction":"west","to":12002},{"direction":"east","to":12004},{"direction":"south","to":12007}]},
    {"vnum":12004,"name":"觀痕鎮魄臺","description":"鎮魄臺旁的觀痕碑只剩幾道細到像從空氣裡縫出來的浮痕，碑與界之間的差別在此已不再靠形體，而只靠一種還沒完全崩散的秩序。","sector_type":"SECT_INSIDE","cluster":"trace-court","coord":[3,0,-56],"labels":["lore"],"exits":[{"direction":"west","to":12003},{"direction":"east","to":12005}],"enquires":["觀痕","鎮魄"]},
    {"vnum":12005,"name":"微界碎痕槽","description":"碎痕槽裡沒有流勢，也沒有明確下沉的邊界，只剩一道由極細裂痕聚起又散去的窄線朝更深處收束，像整段深井正在把最後殘留的形名磨成微粒。","sector_type":"SECT_INSIDE","cluster":"trace-court","coord":[4,0,-56],"labels":["pressure"],"exits":[{"direction":"west","to":12004},{"direction":"east","to":12006},{"direction":"south","to":12009}],"keywords":[{"keyword":"碎痕","description":"槽壁封紋已碎成近乎不可辨識的細痕，只留下把界面持續磨薄、磨細的沉靜壓力。"}]},
    {"vnum":12006,"name":"聽痕沉座","description":"沉座中央懸著一枚比髮絲還細的痕晶，晶體不發光也幾乎不投影，只把周圍殘留的層次慢慢拉成更細、更冷的直線。","sector_type":"SECT_INSIDE","cluster":"trace-court","coord":[5,0,-56],"labels":["signal"],"exits":[{"direction":"west","to":12005}]},
    {"vnum":12007,"name":"細痕側階","description":"側階斜切進偏廊時，腳下的踏步感像被拆成一段段更細的碎線，回頭再看，剛才走過的每一道痕都已淡到只剩勉強能被記住的輪廓。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[2,-1,-56],"labels":["annex"],"exits":[{"direction":"north","to":12003},{"direction":"east","to":12008}]},
    {"vnum":12008,"name":"細痕偏廊","description":"偏廊兩側嵌著一列列幾乎比呼吸還輕的導響殼片，殼面已不再回應完整的聲音，只會把人的念頭刮成一束束極薄的痕線。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[3,-1,-56],"labels":["service"],"exits":[{"direction":"west","to":12007},{"direction":"east","to":12009}],"enquires":["細痕","偏廊"]},
    {"vnum":12009,"name":"微界逆廊","description":"逆廊中央橫著一道近乎只有在側目時才看得見的細裂縫，縫底既沒有深度也沒有重量，卻像能把最後還留得住的形跡慢慢拖往更深的塵界井腹。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[4,-1,-56],"labels":["risk"],"exits":[{"direction":"north","to":12005},{"direction":"west","to":12008},{"direction":"east","to":12010}]},
    {"vnum":12010,"name":"塵界前橋","description":"前橋橫跨在一段已被磨成近乎無形塵霧的井腹上方，橋面每次受力後都只留下極短的一縷冷痕，下一瞬便像被更深的細塵一併吞沒。","sector_type":"SECT_INSIDE","cluster":"mote-threshold","coord":[5,-1,-56],"labels":["bridge"],"exits":[{"direction":"west","to":12009},{"direction":"south","to":12011}]},
    {"vnum":12011,"name":"微界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已磨成一圈圈若有若無的細點，像這裡就是所有界層最後還能勉強被數出痕粒的地方。","sector_type":"SECT_INSIDE","cluster":"mote-threshold","coord":[5,-2,-56],"labels":["threshold"],"exits":[{"direction":"north","to":12010},{"direction":"down","to":12012}],"enquires":["井緣","柱座"]},
    {"vnum":12012,"name":"裂魄微界座","description":"微界座像整段微界深井最後一塊仍勉強聚得住形的細痕石座，腳下環界只剩一圈幾乎會被漏看的微粒薄紋，所有殘痕都在這裡被拖往更深的裂魄塵界。","sector_type":"SECT_INSIDE","cluster":"mote-threshold","coord":[5,-2,-57],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":12011}],"enquires":["微界座","深處"]}
  ]
}
```
