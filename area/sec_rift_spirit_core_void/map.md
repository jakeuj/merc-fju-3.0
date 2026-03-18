# 裂魄空心 (`sec_rift_spirit_core_void`)

## Area Intent

`sec_rift_spirit_core_void` 承接魄核空井最深的裂魄沉井座，再往下沉入裂魄空心與虛腹暗層。此區定位為「虛腹暗層」：讓玩家從虛井落臺、裂腹環脈與寂響偏廊之間，感受到魄壓已被抽離到幾乎只剩空腔震痕，並為更深裂魄真空區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄空心 / 虛腹暗層`
- LevelRange: `92-108`
- Parent area: `sec_rift_spirit_core_hollow`
- ReservedRoomBlock: `11201-11220`

## Planned World Links

- `up` from `11201`: `sec_rift_spirit_core_hollow` room `11112`
- `down` from `11212`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_void",
    "title": "裂魄空心",
    "design_notes": "魄核空井之下的虛腹井層，作為更深裂魄真空區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_hollow",
    "level_range": "92-108",
    "planned_vnum_range": "11201-11220",
    "reserved_room_block": "11201-11220",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄空心 / 虛腹暗層"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11201,
        "target_area": "sec_rift_spirit_core_hollow",
        "target_room_vnum": 11112,
        "label": "裂魄沉井座"
      },
      {
        "direction": "down",
        "source_vnum": 11212,
        "target_area": "sec_rift_spirit_core_vacuum",
        "label": "裂魄真空"
      }
    ],
    "clusters": [
      { "id": "entry-ledge", "label": "虛井落臺" },
      { "id": "void-ring", "label": "裂腹環脈" },
      { "id": "silent-annex", "label": "寂響偏廊" },
      { "id": "vacuum-threshold", "label": "真空前座" }
    ]
  },
  "rooms": [
    {"vnum":11201,"name":"虛井落臺","description":"落臺嵌在虛井內壁的一截石脣上，腳下石層像被長久抽離過般發出沉悶空震，彷彿整座井腹正默默把最後殘存的魄流拖向更深黑空。","sector_type":"SECT_INSIDE","cluster":"entry-ledge","coord":[0,0,-40],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11112,"external":true},{"direction":"east","to":11202}],"enquires":["退路","虛井"]},
    {"vnum":11202,"name":"虛腹下階","description":"下階表面佈滿被抽蝕過的細密痕紋，每走一步都像踩進被掏空後留下的殘響薄膜，連腳步都變得遲鈍。","sector_type":"SECT_INSIDE","cluster":"entry-ledge","coord":[1,0,-40],"labels":["mainline"],"exits":[{"direction":"west","to":11201},{"direction":"east","to":11203}]},
    {"vnum":11203,"name":"裂腹環脈前緣","description":"前緣俯視整圈裂腹環脈，環壁上的暗紅紋路正向內一層層塌陷，像深處仍有某個空心核心在持續拉扯一切殘流。","sector_type":"SECT_INSIDE","cluster":"void-ring","coord":[2,0,-40],"labels":["mainline"],"exits":[{"direction":"west","to":11202},{"direction":"east","to":11204},{"direction":"south","to":11207}]},
    {"vnum":11204,"name":"觀虛鎮魄座","description":"鎮魄座旁立著數面觀虛碑，碑面並不反光，只留下層層向內內陷的暗紋，像連光影都被深處悄悄折盡。","sector_type":"SECT_INSIDE","cluster":"void-ring","coord":[3,0,-40],"labels":["lore"],"exits":[{"direction":"west","to":11203},{"direction":"east","to":11205}],"enquires":["觀虛","鎮魄"]},
    {"vnum":11205,"name":"虛腹引流槽","description":"引流槽沿著井腹邊緣慢慢把殘餘魄流拖往更深處，槽底偶爾浮起一道幾乎看不見的白痕，像深井深處正以無聲方式回應。","sector_type":"SECT_INSIDE","cluster":"void-ring","coord":[4,0,-40],"labels":["pressure"],"exits":[{"direction":"west","to":11204},{"direction":"east","to":11206},{"direction":"south","to":11209}],"keywords":[{"keyword":"引流","description":"引流槽內壁刻滿向內折返的封紋，顯然此地不是為了散壓，而是為了把一切殘流繼續拖向更深的虛腹中心。"}]},
    {"vnum":11206,"name":"聽虛沉座","description":"沉座中央懸著一枚細長黑晶，晶體幾乎沒有回應，卻讓整座裂腹環脈在每次震動後留下更久更深的空白。","sector_type":"SECT_INSIDE","cluster":"void-ring","coord":[5,0,-40],"labels":["signal"],"exits":[{"direction":"west","to":11205}]},
    {"vnum":11207,"name":"寂響側階","description":"側階往偏廊斜切時幾乎沒有任何回聲，只剩一陣微弱寒意從石縫中倒流，像這裡連餘響都已經被深處抽走。","sector_type":"SECT_INSIDE","cluster":"silent-annex","coord":[2,-1,-40],"labels":["annex"],"exits":[{"direction":"north","to":11203},{"direction":"east","to":11208}]},
    {"vnum":11208,"name":"寂響偏廊","description":"偏廊兩側嵌著幾排失去色澤的導響片，片面雖然黯淡，卻仍殘留一絲晚到的暗紅痕影。","sector_type":"SECT_INSIDE","cluster":"silent-annex","coord":[3,-1,-40],"labels":["service"],"exits":[{"direction":"west","to":11207},{"direction":"east","to":11209}],"enquires":["寂響","偏廊"]},
    {"vnum":11209,"name":"虛裂逆廊","description":"逆廊中央裂開一道內縮暗縫，縫底無聲無光，只偶爾往外翻出一股帶著灼意的暗流，像深處正在把一切擠向真空。","sector_type":"SECT_INSIDE","cluster":"silent-annex","coord":[4,-1,-40],"labels":["risk"],"exits":[{"direction":"north","to":11205},{"direction":"west","to":11208},{"direction":"east","to":11210}]},
    {"vnum":11210,"name":"真空前橋","description":"前橋跨在一道近乎看不見底的黑井空腔上方，橋面每次震動後都留下一段異常漫長的靜止，像橋下有更重的存在正慢慢逼近。","sector_type":"SECT_INSIDE","cluster":"vacuum-threshold","coord":[5,-1,-40],"labels":["bridge"],"exits":[{"direction":"west","to":11209},{"direction":"south","to":11211}]},
    {"vnum":11211,"name":"虛腹井緣","description":"井緣外圍著一圈向內坍陷的封魄柱臺，柱臺殘光在井腹邊緣慢慢滑落，像在標示最後一段仍屬於裂腹外層的界線。","sector_type":"SECT_INSIDE","cluster":"vacuum-threshold","coord":[5,-2,-40],"labels":["threshold"],"exits":[{"direction":"north","to":11210},{"direction":"down","to":11212}],"enquires":["井緣","柱臺"]},
    {"vnum":11212,"name":"裂魄虛座","description":"虛座像整段虛腹井層最後一塊仍能立足的陰影邊界，腳下只剩一圈持續向下抽離的暗紅空環，所有殘痕都在這裡被拖往更深的裂魄真空。","sector_type":"SECT_INSIDE","cluster":"vacuum-threshold","coord":[5,-2,-41],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11211}],"enquires":["虛座","深處"]}
  ]
}
```
