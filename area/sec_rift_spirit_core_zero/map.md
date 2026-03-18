# 裂魄零界 (`sec_rift_spirit_core_zero`)

## Area Intent

`sec_rift_spirit_core_zero` 承接裂魄歸零最深的裂魄歸零座，再往下沉入裂魄零界與零界深井。此區定位為「零界深井」：讓玩家從零界落座、零界內庭與無痕偏廊之間，感受到魄壓已被抽離到連空白本身都開始失去邊界，並為更深裂魄空白區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄零界 / 零界深井`
- LevelRange: `98-114`
- Parent area: `sec_rift_spirit_core_null`
- ReservedRoomBlock: `11501-11520`

## Planned World Links

- `up` from `11501`: `sec_rift_spirit_core_null` room `11412`
- `down` from `11512`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_zero",
    "title": "裂魄零界",
    "design_notes": "裂魄歸零之下的零界深井，作為更深空白層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_null",
    "level_range": "98-114",
    "planned_vnum_range": "11501-11520",
    "reserved_room_block": "11501-11520",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄零界 / 零界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11501,
        "target_area": "sec_rift_spirit_core_null",
        "target_room_vnum": 11412,
        "label": "裂魄歸零座"
      },
      {
        "direction": "down",
        "source_vnum": 11512,
        "target_area": "sec_rift_spirit_core_blank",
        "label": "裂魄空白"
      }
    ],
    "clusters": [
      { "id": "zero-shelf", "label": "零界落座" },
      { "id": "zero-court", "label": "零界內庭" },
      { "id": "blank-annex", "label": "無痕偏廊" },
      { "id": "blank-threshold", "label": "空白前座" }
    ]
  },
  "rooms": [
    {"vnum":11501,"name":"零界落座","description":"落座像嵌在零界邊緣的一截淡白石影，腳下殘留的環紋已薄到近乎看不出先後，像整段歸零深庭之下連最後幾筆痕跡都開始失去順序。","sector_type":"SECT_INSIDE","cluster":"zero-shelf","coord":[0,0,-46],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11412,"external":true},{"direction":"east","to":11502}],"enquires":["退路","零界"]},
    {"vnum":11502,"name":"零界下階","description":"下階表面不再只是失去色澤，而像連材質本身都變得難以判定，讓每一步都像踩在一片剛剛才從空白裡被勉強拉出的薄殼上。","sector_type":"SECT_INSIDE","cluster":"zero-shelf","coord":[1,0,-46],"labels":["mainline"],"exits":[{"direction":"west","to":11501},{"direction":"east","to":11503}]},
    {"vnum":11503,"name":"零界內庭前緣","description":"前緣俯瞰整座向內沉陷的零界內庭，庭底沒有波紋、沒有白面，只剩一片讓目光無法久留的淡空，像更深處正把連空白都重新削成更薄的東西。","sector_type":"SECT_INSIDE","cluster":"zero-court","coord":[2,0,-46],"labels":["mainline"],"exits":[{"direction":"west","to":11502},{"direction":"east","to":11504},{"direction":"south","to":11507}]},
    {"vnum":11504,"name":"觀界鎮魄臺","description":"鎮魄臺旁的觀界碑已失去幾乎所有可辨認輪廓，只剩幾道朝中心內縮的淡痕，像連拿來分界的概念也在這裡被慢慢抽空。","sector_type":"SECT_INSIDE","cluster":"zero-court","coord":[3,0,-46],"labels":["lore"],"exits":[{"direction":"west","to":11503},{"direction":"east","to":11505}],"enquires":["觀界","鎮魄"]},
    {"vnum":11505,"name":"零界斷脈槽","description":"斷脈槽裡看不見任何流向，只剩一道近乎沒有厚度的淡灰裂線筆直向下，像所有被抹平的殘脈都在這裡被送往更深的空白井腹。","sector_type":"SECT_INSIDE","cluster":"zero-court","coord":[4,0,-46],"labels":["pressure"],"exits":[{"direction":"west","to":11504},{"direction":"east","to":11506},{"direction":"south","to":11509}],"keywords":[{"keyword":"斷脈","description":"槽壁封紋比歸零層更少也更冷，像這裡已不再處理殘流，只剩把一切界線直接送往空白深處的單向斷送。"}]},
    {"vnum":11506,"name":"聽白沉座","description":"沉座中央懸著一枚幾乎無法辨認邊緣的淡白長晶，晶體不再止於沉默，而像把所有可能留下痕跡的東西一起磨去，只剩一種薄得可怕的鎮壓感。","sector_type":"SECT_INSIDE","cluster":"zero-court","coord":[5,0,-46],"labels":["signal"],"exits":[{"direction":"west","to":11505}]},
    {"vnum":11507,"name":"無痕側階","description":"側階斜切進偏廊時，連腳下擦出的存在感都像被抽成極淡的一線，彷彿只要再往前一步，連你剛才踩過這裡的事也會一起被削掉。","sector_type":"SECT_INSIDE","cluster":"blank-annex","coord":[2,-1,-46],"labels":["annex"],"exits":[{"direction":"north","to":11503},{"direction":"east","to":11508}]},
    {"vnum":11508,"name":"無痕偏廊","description":"偏廊兩側嵌著成排近乎透明的導響殼片，殼面連凹痕都在淡去，只剩一種讓人不確定自己是否仍站在走廊裡的空白錯覺。","sector_type":"SECT_INSIDE","cluster":"blank-annex","coord":[3,-1,-46],"labels":["service"],"exits":[{"direction":"west","to":11507},{"direction":"east","to":11509}],"enquires":["無痕","偏廊"]},
    {"vnum":11509,"name":"零界逆廊","description":"逆廊中央只剩一道淡得快要消失的灰縫，縫底沒有深度、沒有重量，只有一種把所有尺度一併抹平的靜默下墜，讓人幾乎抓不到方向。","sector_type":"SECT_INSIDE","cluster":"blank-annex","coord":[4,-1,-46],"labels":["risk"],"exits":[{"direction":"north","to":11505},{"direction":"west","to":11508},{"direction":"east","to":11510}]},
    {"vnum":11510,"name":"空白前橋","description":"前橋橫跨在一段連空腔都難以成立的淡灰裂腹上方，橋面每次受力後都像什麼也沒發生，只剩一種被重新歸成空白的踏步感。","sector_type":"SECT_INSIDE","cluster":"blank-threshold","coord":[5,-1,-46],"labels":["bridge"],"exits":[{"direction":"west","to":11509},{"direction":"south","to":11511}]},
    {"vnum":11511,"name":"零界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘線已淡到只剩輪廓邊緣，像這裡就是所有界面最後還能勉強被稱為界面的地方。","sector_type":"SECT_INSIDE","cluster":"blank-threshold","coord":[5,-2,-46],"labels":["threshold"],"exits":[{"direction":"north","to":11510},{"direction":"down","to":11512}],"enquires":["井緣","柱座"]},
    {"vnum":11512,"name":"裂魄零界座","description":"零界座像整段零界深井最後一塊仍勉強還沒被削成空白的石影，腳下只剩一圈薄得近乎不存在的灰白環界，所有殘痕都在這裡被拖往更深的裂魄空白。","sector_type":"SECT_INSIDE","cluster":"blank-threshold","coord":[5,-2,-47],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11511}],"enquires":["零界座","深處"]}
  ]
}
```
