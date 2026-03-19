# 裂魄空白 (`sec_rift_spirit_core_blank`)

## Area Intent

`sec_rift_spirit_core_blank` 承接裂魄零界最深的裂魄零界座，再往下沉入裂魄空白與空白深井。此區定位為「空白深井」：讓玩家從空白落座、空白內庭與失序偏廊之間，感受到魄壓已被抽離到連界面本身都難以自證存在，並為更深裂魄白界區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄空白 / 空白深井`
- LevelRange: `94-97`
- Parent area: `sec_rift_spirit_core_zero`
- ReservedRoomBlock: `11601-11620`

## Planned World Links

- `up` from `11601`: `sec_rift_spirit_core_zero` room `11512`
- `down` from `11612`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_blank",
    "title": "裂魄空白",
    "design_notes": "裂魄零界之下的空白深井，作為更深白界層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_zero",
    "level_range": "94-97",
    "planned_vnum_range": "11601-11620",
    "reserved_room_block": "11601-11620",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄空白 / 空白深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11601,
        "target_area": "sec_rift_spirit_core_zero",
        "target_room_vnum": 11512,
        "label": "裂魄零界座"
      },
      {
        "direction": "down",
        "source_vnum": 11612,
        "target_area": "sec_rift_spirit_core_white",
        "label": "裂魄白界"
      }
    ],
    "clusters": [
      { "id": "blank-shelf", "label": "空白落座" },
      { "id": "blank-court", "label": "空白內庭" },
      { "id": "pale-annex", "label": "失序偏廊" },
      { "id": "white-threshold", "label": "白界前座" }
    ]
  },
  "rooms": [
    {"vnum":11601,"name":"空白落座","description":"落座像嵌在空白邊緣的一截淡灰石影，腳下殘留的環界已薄到幾乎無法辨認先後，像整段零界深井之下連最後幾筆可稱為界面的痕跡都開始失去依據。","sector_type":"SECT_INSIDE","cluster":"blank-shelf","coord":[0,0,-48],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11512,"external":true},{"direction":"east","to":11602}],"enquires":["退路","空白"]},
    {"vnum":11602,"name":"空白下階","description":"下階表面像被削去所有可供辨識的紋理，只剩一種連材質本身都難以成立的淡灰觸感，讓每一步都像踩在剛被空白暫時容許存在的薄殼上。","sector_type":"SECT_INSIDE","cluster":"blank-shelf","coord":[1,0,-48],"labels":["mainline"],"exits":[{"direction":"west","to":11601},{"direction":"east","to":11603}]},
    {"vnum":11603,"name":"空白內庭前緣","description":"前緣俯瞰整座向內沉落的空白內庭，庭底沒有光影、沒有灰面，只剩一片令視線無法長留的淡失序，像更深處正把連空白都重新磨回無可稱述的原點。","sector_type":"SECT_INSIDE","cluster":"blank-court","coord":[2,0,-48],"labels":["mainline"],"exits":[{"direction":"west","to":11602},{"direction":"east","to":11604},{"direction":"south","to":11607}]},
    {"vnum":11604,"name":"觀白鎮魄臺","description":"鎮魄臺旁的觀白碑只剩幾道朝中心慢慢收束的淡痕，像連用來辨識失序與留白的概念都在這裡被一層層磨成更薄的空殼。","sector_type":"SECT_INSIDE","cluster":"blank-court","coord":[3,0,-48],"labels":["lore"],"exits":[{"direction":"west","to":11603},{"direction":"east","to":11605}],"enquires":["觀白","鎮魄"]},
    {"vnum":11605,"name":"空白斷界槽","description":"斷界槽裡看不見任何流動，只剩一道淡得幾乎無厚度的灰白裂線筆直向下，像所有殘留界面都在這裡被送往更深的白界井腹。","sector_type":"SECT_INSIDE","cluster":"blank-court","coord":[4,0,-48],"labels":["pressure"],"exits":[{"direction":"west","to":11604},{"direction":"east","to":11606},{"direction":"south","to":11609}],"keywords":[{"keyword":"斷界","description":"槽壁封紋比零界層更少也更淡，像這裡已不再整理殘痕，只剩把一切界面直接送往更深空白的單向斷送。"}]},
    {"vnum":11606,"name":"聽白沉座","description":"沉座中央懸著一枚幾乎無法分出邊界的灰白長晶，晶體不再止於寂靜，而像把所有可能留下輪廓的事物一併磨去，只剩一種薄得駭人的鎮壓感。","sector_type":"SECT_INSIDE","cluster":"blank-court","coord":[5,0,-48],"labels":["signal"],"exits":[{"direction":"west","to":11605}]},
    {"vnum":11607,"name":"失序側階","description":"側階斜切進偏廊時，連腳下擦出的存在感都像被抽成極淡的一線，彷彿只要再往前一步，連你曾經踏過這裡的順序都會一起被削掉。","sector_type":"SECT_INSIDE","cluster":"pale-annex","coord":[2,-1,-48],"labels":["annex"],"exits":[{"direction":"north","to":11603},{"direction":"east","to":11608}]},
    {"vnum":11608,"name":"失序偏廊","description":"偏廊兩側嵌著成排近乎透明的導響殼片，殼面連凹痕都在淡去，只剩一種讓人分不清自己是否仍站在走廊裡的失序錯覺。","sector_type":"SECT_INSIDE","cluster":"pale-annex","coord":[3,-1,-48],"labels":["service"],"exits":[{"direction":"west","to":11607},{"direction":"east","to":11609}],"enquires":["失序","偏廊"]},
    {"vnum":11609,"name":"空白逆廊","description":"逆廊中央只剩一道淡得快要消失的灰白細縫，縫底沒有深度、沒有重量，只剩一種把所有尺度一併抹平的靜默下墜，讓人幾乎抓不到仍可依附的方向。","sector_type":"SECT_INSIDE","cluster":"pale-annex","coord":[4,-1,-48],"labels":["risk"],"exits":[{"direction":"north","to":11605},{"direction":"west","to":11608},{"direction":"east","to":11610}]},
    {"vnum":11610,"name":"白界前橋","description":"前橋橫跨在一段連空腔都難以成立的淡白裂腹上方，橋面每次受力後都像什麼也沒發生，只剩一種被重新歸成空白的踏步感。","sector_type":"SECT_INSIDE","cluster":"white-threshold","coord":[5,-1,-48],"labels":["bridge"],"exits":[{"direction":"west","to":11609},{"direction":"south","to":11611}]},
    {"vnum":11611,"name":"空白井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘線已淡到只剩輪廓邊緣，像這裡就是所有界面最後還能勉強被稱為界面的地方。","sector_type":"SECT_INSIDE","cluster":"white-threshold","coord":[5,-2,-48],"labels":["threshold"],"exits":[{"direction":"north","to":11610},{"direction":"down","to":11612}],"enquires":["井緣","柱座"]},
    {"vnum":11612,"name":"裂魄空白座","description":"空白座像整段空白深井最後一塊仍勉強還沒被磨成素白的石影，腳下只剩一圈薄得近乎不存在的灰白環界，所有殘痕都在這裡被拖往更深的裂魄白界。","sector_type":"SECT_INSIDE","cluster":"white-threshold","coord":[5,-2,-49],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11611}],"enquires":["空白座","深處"]}
  ]
}
```
