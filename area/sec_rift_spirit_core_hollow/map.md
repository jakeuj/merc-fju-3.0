# 魄核空井 (`sec_rift_spirit_core_hollow`)

## Area Intent

`sec_rift_spirit_core_hollow` 承接魄淵深井最深的魄核沉座，再往下沉入魄核空井與空腹暗層。此區定位為「空腹暗層」：讓玩家從空井落臺、空腹環脈與失響偏廊之間，感受到魄壓已不再只是回盪，而是開始在空腹井層內形成真正的抽離旋渦，並為更深裂魄空心區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `魄核空井 / 空腹暗層`
- LevelRange: `90-106`
- Parent area: `sec_rift_core_spirit_abyss`
- ReservedRoomBlock: `11101-11120`

## Planned World Links

- `up` from `11101`: `sec_rift_core_spirit_abyss` room `11012`
- `down` from `11112`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_hollow",
    "title": "魄核空井",
    "design_notes": "魄淵深井之下的空腹井層，作為更深裂魄空心區前的過渡主段。",
    "parent_area": "sec_rift_core_spirit_abyss",
    "level_range": "90-106",
    "planned_vnum_range": "11101-11120",
    "reserved_room_block": "11101-11120",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "魄核空井 / 空腹暗層"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11101,
        "target_area": "sec_rift_core_spirit_abyss",
        "target_room_vnum": 11012,
        "label": "魄核沉座"
      },
      {
        "direction": "down",
        "source_vnum": 11112,
        "target_area": "sec_rift_spirit_core_void",
        "label": "裂魄空心"
      }
    ],
    "clusters": [
      { "id": "entry-shelf", "label": "空井落臺" },
      { "id": "hollow-ring", "label": "空腹環脈" },
      { "id": "mute-annex", "label": "失響偏廊" },
      { "id": "void-threshold", "label": "裂魄前座" }
    ]
  },
  "rooms": [
    {"vnum":11101,"name":"空井落臺","description":"落臺嵌在空井內壁的一截石脣上，腳下石層正被某種無形吸力緩慢往下拖曳，像整座空腹井層都在默默吞走最後殘留的魄壓。","sector_type":"SECT_INSIDE","cluster":"entry-shelf","coord":[0,0,-38],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11012,"external":true},{"direction":"east","to":11102}],"enquires":["退路","空井"]},
    {"vnum":11102,"name":"空腹下階","description":"下階表面像被反覆剝離過，石面泛著異常平滑的幽灰光澤，每走一步都彷彿踩進被抽空後留下的餘響陰影。","sector_type":"SECT_INSIDE","cluster":"entry-shelf","coord":[1,0,-38],"labels":["mainline"],"exits":[{"direction":"west","to":11101},{"direction":"east","to":11103}]},
    {"vnum":11103,"name":"空腹環脈前緣","description":"前緣俯視整圈空腹環脈，環壁紋路像被向內牽扯般一圈圈收束，彷彿更深處正持續把外層留下的魄流拉向井腹中心。","sector_type":"SECT_INSIDE","cluster":"hollow-ring","coord":[2,0,-38],"labels":["mainline"],"exits":[{"direction":"west","to":11102},{"direction":"east","to":11104},{"direction":"south","to":11107}]},
    {"vnum":11104,"name":"觀空鎮魄座","description":"鎮魄座周圍豎著幾面向井腹微傾的觀空碑，碑面只映得出一層層往內凹陷的暗紅影紋，像所有光都在這裡先被折走。","sector_type":"SECT_INSIDE","cluster":"hollow-ring","coord":[3,0,-38],"labels":["lore"],"exits":[{"direction":"west","to":11103},{"direction":"east","to":11105}],"enquires":["觀空","鎮魄"]},
    {"vnum":11105,"name":"空腹引魄槽","description":"引魄槽沿著井腹邊緣慢慢把殘餘魄流送往更深處，槽底偶爾浮起一道無聲白痕，像深井深處正以看不見的方式回應這裡。","sector_type":"SECT_INSIDE","cluster":"hollow-ring","coord":[4,0,-38],"labels":["pressure"],"exits":[{"direction":"west","to":11104},{"direction":"east","to":11106},{"direction":"south","to":11109}],"keywords":[{"keyword":"引魄","description":"引魄槽內壁佈滿向內彎折的封紋，顯然此地設計的目的並非排壓，而是把所有殘流都拖向更深的空腹中心。"}]},
    {"vnum":11106,"name":"聽空沉座","description":"沉座中央懸著一枚細長黑魄晶，晶體並不發聲，卻讓整座空腹環脈在每次震動後都留下更長更空的回盪。","sector_type":"SECT_INSIDE","cluster":"hollow-ring","coord":[5,0,-38],"labels":["signal"],"exits":[{"direction":"west","to":11105}]},
    {"vnum":11107,"name":"失響側階","description":"側階通往偏廊時幾乎沒有任何腳步回聲，只剩一陣微弱寒意沿石縫倒流，像這裡連聲音都已經被抽空。","sector_type":"SECT_INSIDE","cluster":"mute-annex","coord":[2,-1,-38],"labels":["annex"],"exits":[{"direction":"north","to":11103},{"direction":"east","to":11108}]},
    {"vnum":11108,"name":"絕響偏廊","description":"偏廊兩側嵌著幾排失去光澤的導響片，片面雖已黯淡，卻仍在陰影裡留下一道道晚到的暗紅殘紋。","sector_type":"SECT_INSIDE","cluster":"mute-annex","coord":[3,-1,-38],"labels":["service"],"exits":[{"direction":"west","to":11107},{"direction":"east","to":11109}],"enquires":["絕響","偏廊"]},
    {"vnum":11109,"name":"裂響逆廊","description":"逆廊中央張開一道內縮的裂縫，縫底沒有聲音，只有一股帶著灼意的暗流不時往外翻湧，像更深處正在把什麼撕成真空。","sector_type":"SECT_INSIDE","cluster":"mute-annex","coord":[4,-1,-38],"labels":["risk"],"exits":[{"direction":"north","to":11105},{"direction":"west","to":11108},{"direction":"east","to":11110}]},
    {"vnum":11110,"name":"裂魄前橋","description":"前橋跨在一道近乎看不見底的空井上方，橋面每次震動後都會留下一段異常漫長的靜默，像橋下有某種更重的存在正在逼近。","sector_type":"SECT_INSIDE","cluster":"void-threshold","coord":[5,-1,-38],"labels":["bridge"],"exits":[{"direction":"west","to":11109},{"direction":"south","to":11111}]},
    {"vnum":11111,"name":"空腹井緣","description":"井緣外圍著一圈向內坍陷的封魄柱座，柱座殘光在井腹邊緣慢慢滑落，像在標示最後一段仍屬於外層空腹區的邊界。","sector_type":"SECT_INSIDE","cluster":"void-threshold","coord":[5,-2,-38],"labels":["threshold"],"exits":[{"direction":"north","to":11110},{"direction":"down","to":11112}],"enquires":["井緣","柱座"]},
    {"vnum":11112,"name":"裂魄沉井座","description":"沉井座像整段空腹井層最後一塊仍能站穩的陰影邊界，腳下只剩一圈持續向下抽離的暗紅空環，所有殘音都在這裡被拖往更深的裂魄空心。","sector_type":"SECT_INSIDE","cluster":"void-threshold","coord":[5,-2,-39],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11111}],"enquires":["裂魄","深處"]}
  ]
}
```
