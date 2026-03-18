# 裂魄歸零 (`sec_rift_spirit_core_null`)

## Area Intent

`sec_rift_spirit_core_null` 承接裂魄真空最深的裂魄真空座，再往下沉入裂魄歸零與歸零深庭。此區定位為「歸零深庭」：讓玩家從歸零落座、歸零沉庭與空滅偏廊之間，感受到魄壓已被抽離到連形體與回音都近乎失去依附，並為更深裂魄零界區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄歸零 / 歸零深庭`
- LevelRange: `96-112`
- Parent area: `sec_rift_spirit_core_vacuum`
- ReservedRoomBlock: `11401-11420`

## Planned World Links

- `up` from `11401`: `sec_rift_spirit_core_vacuum` room `11312`
- `down` from `11412`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_null",
    "title": "裂魄歸零",
    "design_notes": "裂魄真空之下的歸零深庭，作為更深零界層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_vacuum",
    "level_range": "96-112",
    "planned_vnum_range": "11401-11420",
    "reserved_room_block": "11401-11420",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄歸零 / 歸零深庭"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11401,
        "target_area": "sec_rift_spirit_core_vacuum",
        "target_room_vnum": 11312,
        "label": "裂魄真空座"
      },
      {
        "direction": "down",
        "source_vnum": 11412,
        "target_area": "sec_rift_spirit_core_zero",
        "label": "裂魄零界"
      }
    ],
    "clusters": [
      { "id": "zero-seat", "label": "歸零落座" },
      { "id": "null-court", "label": "歸零沉庭" },
      { "id": "hush-annex", "label": "空滅偏廊" },
      { "id": "zero-threshold", "label": "零界前座" }
    ]
  },
  "rooms": [
    {"vnum":11401,"name":"歸零落座","description":"落座像嵌在深庭邊緣的一截灰白石影，腳下原本還能辨認的環紋正一圈圈淡去，像整段真空之下只剩最後幾筆尚未完全抹平的痕跡。","sector_type":"SECT_INSIDE","cluster":"zero-seat","coord":[0,0,-44],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11312,"external":true},{"direction":"east","to":11402}],"enquires":["退路","歸零"]},
    {"vnum":11402,"name":"歸零下階","description":"下階表面不再反射任何冷痕，只剩一種近乎被掏空的灰白質地，讓每一步都像踩在一層即將失去名字的薄殼上。","sector_type":"SECT_INSIDE","cluster":"zero-seat","coord":[1,0,-44],"labels":["mainline"],"exits":[{"direction":"west","to":11401},{"direction":"east","to":11403}]},
    {"vnum":11403,"name":"歸零沉庭前緣","description":"前緣俯瞰整座向內凹陷的歸零沉庭，庭底沒有波紋、沒有暗環，只剩一片近乎純白的靜默面，像更深處正把一切殘存定義緩慢抽空。","sector_type":"SECT_INSIDE","cluster":"null-court","coord":[2,0,-44],"labels":["mainline"],"exits":[{"direction":"west","to":11402},{"direction":"east","to":11404},{"direction":"south","to":11407}]},
    {"vnum":11404,"name":"觀零鎮魄臺","description":"鎮魄臺旁的觀零碑已失去多數稜角，只剩幾道朝中心收束的白痕，彷彿連封印用來命名異象的文字也在此被歸零。","sector_type":"SECT_INSIDE","cluster":"null-court","coord":[3,0,-44],"labels":["lore"],"exits":[{"direction":"west","to":11403},{"direction":"east","to":11405}],"enquires":["觀零","鎮魄"]},
    {"vnum":11405,"name":"歸零滅脈槽","description":"滅脈槽裡沒有流動、沒有顫動，只剩一道幾乎看不出厚度的淡白裂線筆直向下，像所有被抽離的餘波都在這裡改以沉默的形式繼續墜落。","sector_type":"SECT_INSIDE","cluster":"null-court","coord":[4,0,-44],"labels":["pressure"],"exits":[{"direction":"west","to":11404},{"direction":"east","to":11406},{"direction":"south","to":11409}],"keywords":[{"keyword":"滅脈","description":"槽壁封紋比真空層更短更冷，像這裡已不再處理壓力，只剩把一切殘脈直接送往歸零深庭的單向斷流。"}]},
    {"vnum":11406,"name":"聽空沉座","description":"沉座中央懸著一枚近乎透明的灰白長晶，晶體不再止於無聲，而像把所有可能形成回音的東西一併磨去，只留下徹底空白的鎮壓感。","sector_type":"SECT_INSIDE","cluster":"null-court","coord":[5,0,-44],"labels":["signal"],"exits":[{"direction":"west","to":11405}]},
    {"vnum":11407,"name":"空滅側階","description":"側階斜切進偏廊時，連腳下摩擦出的存在感都像被削薄，只剩一絲極淡的觸感提示你尚未與深庭一同被抹成空白。","sector_type":"SECT_INSIDE","cluster":"hush-annex","coord":[2,-1,-44],"labels":["annex"],"exits":[{"direction":"north","to":11403},{"direction":"east","to":11408}]},
    {"vnum":11408,"name":"空滅偏廊","description":"偏廊兩側嵌著成排導響片殘殼，殼面連白影都快要褪盡，只剩細微凹痕提醒這裡曾經也是能夠回收聲響的地方。","sector_type":"SECT_INSIDE","cluster":"hush-annex","coord":[3,-1,-44],"labels":["service"],"exits":[{"direction":"west","to":11407},{"direction":"east","to":11409}],"enquires":["空滅","偏廊"]},
    {"vnum":11409,"name":"歸零逆廊","description":"逆廊中央留著一條纖細得近乎斷掉的白縫，縫底沒有深淵感，只有某種把深與淺一併抹平的靜止下墜，讓人幾乎失去方向判斷。","sector_type":"SECT_INSIDE","cluster":"hush-annex","coord":[4,-1,-44],"labels":["risk"],"exits":[{"direction":"north","to":11405},{"direction":"west","to":11408},{"direction":"east","to":11410}]},
    {"vnum":11410,"name":"零界前橋","description":"前橋橫跨在一段連空洞都難以描述的淡白裂腔上方，橋面每次受力後都不再留下白痕，只像剛剛那次踏步從未真正發生過。","sector_type":"SECT_INSIDE","cluster":"zero-threshold","coord":[5,-1,-44],"labels":["bridge"],"exits":[{"direction":"west","to":11409},{"direction":"south","to":11411}]},
    {"vnum":11411,"name":"歸零井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘留的白線正一條條變得難以辨認，像這裡就是所有形體最後還能勉強自稱為形體的邊界。","sector_type":"SECT_INSIDE","cluster":"zero-threshold","coord":[5,-2,-44],"labels":["threshold"],"exits":[{"direction":"north","to":11410},{"direction":"down","to":11412}],"enquires":["井緣","柱座"]},
    {"vnum":11412,"name":"裂魄歸零座","description":"歸零座像整段歸零深庭最後一塊仍勉強沒有被抹盡的石影，腳下只剩一圈快要分不出明暗的空白環界，所有殘痕都在這裡被拖往更深的裂魄零界。","sector_type":"SECT_INSIDE","cluster":"zero-threshold","coord":[5,-2,-45],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11411}],"enquires":["歸零座","深處"]}
  ]
}
```
