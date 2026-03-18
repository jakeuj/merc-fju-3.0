# 裂魄澹界 (`sec_rift_spirit_core_faint`)

## Area Intent

`sec_rift_spirit_core_faint` 承接裂魄素界最深的裂魄素界座，再往下沉入裂魄澹界與澹界深井。此區定位為「澹界深井」：讓玩家從澹界落座、澹界內庭與微痕偏廊之間，感受到魄壓已從淡素進一步褪成近乎只剩餘意的層次，並為更深裂魄微界區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄澹界 / 澹界深井`
- LevelRange: `106-120`
- Parent area: `sec_rift_spirit_core_plain`
- ReservedRoomBlock: `11901-11920`

## Planned World Links

- `up` from `11901`: `sec_rift_spirit_core_plain` room `11812`
- `down` from `11912`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_faint",
    "title": "裂魄澹界",
    "design_notes": "裂魄素界之下的澹界深井，作為更深微界層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_plain",
    "level_range": "106-120",
    "planned_vnum_range": "11901-11920",
    "reserved_room_block": "11901-11920",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄澹界 / 澹界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11901,
        "target_area": "sec_rift_spirit_core_plain",
        "target_room_vnum": 11812,
        "label": "裂魄素界座"
      },
      {
        "direction": "down",
        "source_vnum": 11912,
        "target_area": "sec_rift_spirit_core_trace",
        "label": "裂魄微界"
      }
    ],
    "clusters": [
      { "id": "faint-shelf", "label": "澹界落座" },
      { "id": "faint-court", "label": "澹界內庭" },
      { "id": "trace-annex", "label": "微痕偏廊" },
      { "id": "trace-threshold", "label": "微界前座" }
    ]
  },
  "rooms": [
    {"vnum":11901,"name":"澹界落座","description":"落座像嵌在澹界邊緣的一截餘淡石影，腳下環界已不再明確分出內外，只剩一種勉強還能承住意識餘波的微淡底意，像連最後那點素色都在此繼續退遠。","sector_type":"SECT_INSIDE","cluster":"faint-shelf","coord":[0,0,-54],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11812,"external":true},{"direction":"east","to":11902}],"enquires":["澹界","退路"]},
    {"vnum":11902,"name":"餘淡下階","description":"下階表面不再保留可稱為色澤的東西，只剩一層極薄的淡意貼著石面向前延展，讓每一步都像踩在一段剛要從記憶裡退去的痕上。","sector_type":"SECT_INSIDE","cluster":"faint-shelf","coord":[1,0,-54],"labels":["mainline"],"exits":[{"direction":"west","to":11901},{"direction":"east","to":11903}]},
    {"vnum":11903,"name":"澹界內庭前緣","description":"前緣俯瞰整座向內沉落的澹界內庭，庭底像一潭連淡與空都快分不出的餘井，視線停得久了，連自己為何在看都會慢慢變得不再重要。","sector_type":"SECT_INSIDE","cluster":"faint-court","coord":[2,0,-54],"labels":["mainline"],"exits":[{"direction":"west","to":11902},{"direction":"east","to":11904},{"direction":"south","to":11907}]},
    {"vnum":11904,"name":"觀微鎮魄臺","description":"鎮魄臺旁的觀微碑幾乎只剩幾道難以捕捉的微痕在空氣裡浮現，像提醒來者這裡曾經還能說得清什麼是碑、什麼是界。","sector_type":"SECT_INSIDE","cluster":"faint-court","coord":[3,0,-54],"labels":["lore"],"exits":[{"direction":"west","to":11903},{"direction":"east","to":11905}],"enquires":["觀微","鎮魄"]},
    {"vnum":11905,"name":"澹界退層槽","description":"退層槽裡沒有流聲，也沒有下墜感，只剩一道隨時像要從視野裡抽離的微淡細線向更深處退去，像整段深井正在把所有殘餘界層一層層放回無名。","sector_type":"SECT_INSIDE","cluster":"faint-court","coord":[4,0,-54],"labels":["pressure"],"exits":[{"direction":"west","to":11904},{"direction":"east","to":11906},{"direction":"south","to":11909}],"keywords":[{"keyword":"退層","description":"槽壁封紋已幾乎只剩不穩的微線，留下的是一種把所有界層繼續退成更淡餘意的沉靜力道。"}]},
    {"vnum":11906,"name":"聽微沉座","description":"沉座中央懸著一枚像隨時會從目光裡退場的微淡長晶，晶體沒有亮度，也沒有陰影，只把周圍最後還能辨識的層次慢慢壓回更輕的餘意。","sector_type":"SECT_INSIDE","cluster":"faint-court","coord":[5,0,-54],"labels":["signal"],"exits":[{"direction":"west","to":11905}]},
    {"vnum":11907,"name":"微痕側階","description":"側階斜切進偏廊時，連腳下的踏步感都像只剩一縷快要消失的微痕，回頭看去，那些剛剛還在的痕跡已經淡到像從未真正落在此處。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[2,-1,-54],"labels":["annex"],"exits":[{"direction":"north","to":11903},{"direction":"east","to":11908}]},
    {"vnum":11908,"name":"微痕偏廊","description":"偏廊兩側嵌著一排排幾乎與空氣無異的導響殼片，殼面不再回應光與影，只剩一種會把人的念頭也慢慢淡成餘音的冷靜錯覺。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[3,-1,-54],"labels":["service"],"exits":[{"direction":"west","to":11907},{"direction":"east","to":11909}],"enquires":["微痕","偏廊"]},
    {"vnum":11909,"name":"澹界逆廊","description":"逆廊中央只剩一道時隱時現的微淡素縫，縫底既無深度也無重量，卻像能把最後仍可被感知的餘痕慢慢拖向更深的微界井腹。","sector_type":"SECT_INSIDE","cluster":"trace-annex","coord":[4,-1,-54],"labels":["risk"],"exits":[{"direction":"north","to":11905},{"direction":"west","to":11908},{"direction":"east","to":11910}]},
    {"vnum":11910,"name":"微界前橋","description":"前橋橫跨在一段近乎已退成純粹餘意的淡腹上方，橋面每次受力後都只留下幾乎抓不住的靜冷回聲，下一瞬便又從感知裡退去。","sector_type":"SECT_INSIDE","cluster":"trace-threshold","coord":[5,-1,-54],"labels":["bridge"],"exits":[{"direction":"west","to":11909},{"direction":"south","to":11911}]},
    {"vnum":11911,"name":"澹界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已退到只剩幾道微不可察的浮線，像這裡就是所有界面最後還能勉強被稱為痕影的地方。","sector_type":"SECT_INSIDE","cluster":"trace-threshold","coord":[5,-2,-54],"labels":["threshold"],"exits":[{"direction":"north","to":11910},{"direction":"down","to":11912}],"enquires":["井緣","柱座"]},
    {"vnum":11912,"name":"裂魄澹界座","description":"澹界座像整段澹界深井最後一塊仍勉強留有餘形的淡影石座，腳下只剩一圈薄得近乎被感知漏過的環界，所有殘痕都在這裡被拖往更深的裂魄微界。","sector_type":"SECT_INSIDE","cluster":"trace-threshold","coord":[5,-2,-55],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11911}],"enquires":["澹界座","深處"]}
  ]
}
```
