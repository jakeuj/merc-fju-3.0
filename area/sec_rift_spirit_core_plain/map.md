# 裂魄素界 (`sec_rift_spirit_core_plain`)

## Area Intent

`sec_rift_spirit_core_plain` 承接裂魄白界最深的裂魄白界座，再往下沉入裂魄素界與素界深井。此區定位為「素界深井」：讓玩家從素界落座、素界內庭與澹痕偏廊之間，感受到魄壓已從素白進一步淡成近乎無質的底色，並為更深裂魄澹界區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄素界 / 素界深井`
- LevelRange: `104-120`
- Parent area: `sec_rift_spirit_core_white`
- ReservedRoomBlock: `11801-11820`

## Planned World Links

- `up` from `11801`: `sec_rift_spirit_core_white` room `11712`
- `down` from `11812`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_plain",
    "title": "裂魄素界",
    "design_notes": "裂魄白界之下的素界深井，作為更深澹界層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_white",
    "level_range": "104-120",
    "planned_vnum_range": "11801-11820",
    "reserved_room_block": "11801-11820",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄素界 / 素界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11801,
        "target_area": "sec_rift_spirit_core_white",
        "target_room_vnum": 11712,
        "label": "裂魄白界座"
      },
      {
        "direction": "down",
        "source_vnum": 11812,
        "target_area": "sec_rift_spirit_core_faint",
        "label": "裂魄澹界"
      }
    ],
    "clusters": [
      { "id": "plain-shelf", "label": "素界落座" },
      { "id": "plain-court", "label": "素界內庭" },
      { "id": "faint-annex", "label": "澹痕偏廊" },
      { "id": "faint-threshold", "label": "澹界前座" }
    ]
  },
  "rooms": [
    {"vnum":11801,"name":"素界落座","description":"落座像嵌在素界邊緣的一截淡素石影，腳下殘留的環界已薄到幾乎與四周同化，只剩一種勉強還能承住意識的底色，像連白意都在此被慢慢澹去。","sector_type":"SECT_INSIDE","cluster":"plain-shelf","coord":[0,0,-52],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11712,"external":true},{"direction":"east","to":11802}],"enquires":["素界","退路"]},
    {"vnum":11802,"name":"澹素下階","description":"下階表面沒有紋理，也幾乎不再保留顏色，只剩一層比霧更薄的素意沿著石面貼伏，讓每一步都像踩在剛被允許停留片刻的淡影上。","sector_type":"SECT_INSIDE","cluster":"plain-shelf","coord":[1,0,-52],"labels":["mainline"],"exits":[{"direction":"west","to":11801},{"direction":"east","to":11803}]},
    {"vnum":11803,"name":"素界內庭前緣","description":"前緣俯瞰整座向內沉落的素界內庭，庭底像一潭連白與灰都已不再重要的淡素空井，視線只要久停片刻，就會連觀察這件事本身都逐漸失去依據。","sector_type":"SECT_INSIDE","cluster":"plain-court","coord":[2,0,-52],"labels":["mainline"],"exits":[{"direction":"west","to":11802},{"direction":"east","to":11804},{"direction":"south","to":11807}]},
    {"vnum":11804,"name":"觀澹鎮魄臺","description":"鎮魄臺旁的觀澹碑幾乎看不出碑與空氣的分界，只剩幾道內收的淡痕在提醒人這裡曾經存在過可被辨識的層次。","sector_type":"SECT_INSIDE","cluster":"plain-court","coord":[3,0,-52],"labels":["lore"],"exits":[{"direction":"west","to":11803},{"direction":"east","to":11805}],"enquires":["觀澹","鎮魄"]},
    {"vnum":11805,"name":"素界澹層槽","description":"澹層槽裡沒有流動可循，只剩一道細到近乎無法追索的淡線朝更深處緩慢下沉，像整段深井正在把所有最後的界層都洗回更無名的澹底。","sector_type":"SECT_INSIDE","cluster":"plain-court","coord":[4,0,-52],"labels":["pressure"],"exits":[{"direction":"west","to":11804},{"direction":"east","to":11806},{"direction":"south","to":11809}],"keywords":[{"keyword":"澹層","description":"槽壁上殘留的封紋已幾乎不成圖樣，只剩一種把所有顏色與層次一併褪成淡底的冷靜意志。"}]},
    {"vnum":11806,"name":"聽澹沉座","description":"沉座中央懸著一枚像被洗去所有邊界的淡素長晶，晶體沒有光，也沒有影，只把周圍殘留的一切輪廓慢慢壓成更薄、更靜的底色。","sector_type":"SECT_INSIDE","cluster":"plain-court","coord":[5,0,-52],"labels":["signal"],"exits":[{"direction":"west","to":11805}]},
    {"vnum":11807,"name":"澹痕側階","description":"側階斜切進偏廊時，連腳下殘留的踏步感都像被磨成極輕的澹痕，回頭再看，幾乎已無法確定自己剛才究竟走過了哪一格。","sector_type":"SECT_INSIDE","cluster":"faint-annex","coord":[2,-1,-52],"labels":["annex"],"exits":[{"direction":"north","to":11803},{"direction":"east","to":11808}]},
    {"vnum":11808,"name":"澹痕偏廊","description":"偏廊兩側嵌著一排排近乎無色的導響殼片，殼面既不反光也不留影，只剩一種會把人的自述慢慢褪成空白前音的淡冷錯覺。","sector_type":"SECT_INSIDE","cluster":"faint-annex","coord":[3,-1,-52],"labels":["service"],"exits":[{"direction":"west","to":11807},{"direction":"east","to":11809}],"enquires":["澹痕","偏廊"]},
    {"vnum":11809,"name":"素界逆廊","description":"逆廊中央只剩一道淡得近乎不可見的素縫，縫底既無深度也無陰影，卻像能把所有殘留的名稱與重量慢慢拖向更深的澹界井腹。","sector_type":"SECT_INSIDE","cluster":"faint-annex","coord":[4,-1,-52],"labels":["risk"],"exits":[{"direction":"north","to":11805},{"direction":"west","to":11808},{"direction":"east","to":11810}]},
    {"vnum":11810,"name":"澹界前橋","description":"前橋橫跨在一段近乎已無色相可稱的淡腹上方，橋面每次受力後都只留下極短的靜冷餘響，下一瞬便像連那點餘響也被一起帶走。","sector_type":"SECT_INSIDE","cluster":"faint-threshold","coord":[5,-1,-52],"labels":["bridge"],"exits":[{"direction":"west","to":11809},{"direction":"south","to":11811}]},
    {"vnum":11811,"name":"素界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已褪到只剩幾道浮在淡底上的細線，像這裡就是所有界面最後還能被稱為痕的地方。","sector_type":"SECT_INSIDE","cluster":"faint-threshold","coord":[5,-2,-52],"labels":["threshold"],"exits":[{"direction":"north","to":11810},{"direction":"down","to":11812}],"enquires":["井緣","柱座"]},
    {"vnum":11812,"name":"裂魄素界座","description":"素界座像整段素界深井最後一塊仍勉強留住輪廓的淡素石影，腳下只剩一圈薄得與周圍幾乎無從區分的環界，所有殘痕都在這裡被拖往更深的裂魄澹界。","sector_type":"SECT_INSIDE","cluster":"faint-threshold","coord":[5,-2,-53],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11811}],"enquires":["素界座","深處"]}
  ]
}
```
