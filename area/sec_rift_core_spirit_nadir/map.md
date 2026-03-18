# 核心魄淵 (`sec_rift_core_spirit_nadir`)

## Area Intent

`sec_rift_core_spirit_nadir` 承接封心核心最深的封心深座，再往下沉入核心已近乎失去外殼約束的魄壓暗層。此區定位為「心魄沉座」：讓玩家從魄座落井、沉環壓脈與失魄偏廊之間，感受到裂核主體從心跳轉為魄鳴的危險轉折，並為更深核心魄淵區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `核心魄淵 / 心魄沉座`
- LevelRange: `86-102`
- Parent area: `sec_rift_sealed_core_heart`
- ReservedRoomBlock: `10901-10920`

## Planned World Links

- `up` from `10901`: `sec_rift_sealed_core_heart` room `10812`
- `down` from `10912`: future deeper core-spirit extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core_spirit_nadir",
    "title": "核心魄淵",
    "design_notes": "封心核心之下的魄壓暗層，作為更深核心魄淵區前的過渡主段。",
    "parent_area": "sec_rift_sealed_core_heart",
    "level_range": "86-102",
    "planned_vnum_range": "10901-10920",
    "reserved_room_block": "10901-10920",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "核心魄淵 / 心魄沉座"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10901,
        "target_area": "sec_rift_sealed_core_heart",
        "target_room_vnum": 10812,
        "label": "封心深座"
      },
      {
        "direction": "down",
        "source_vnum": 10912,
        "target_area": "sec_rift_core_spirit_abyss",
        "label": "魄淵深井"
      }
    ],
    "clusters": [
      { "id": "entry-drop", "label": "魄座落井" },
      { "id": "spirit-ring", "label": "核心沉環" },
      { "id": "shatter-annex", "label": "失魄偏廊" },
      { "id": "abyss-threshold", "label": "魄淵前座" }
    ]
  },
  "rooms": [
    {"vnum":10901,"name":"魄座落井臺","description":"落井臺嵌在深座底下的弧形石唇上，四周不再傳來完整心跳，只剩像殘魂低鳴般的暗震沿壁面往下滲流。","sector_type":"SECT_INSIDE","cluster":"entry-drop","coord":[0,0,-34],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10812,"external":true},{"direction":"east","to":10902}],"enquires":["退路","深井"]},
    {"vnum":10902,"name":"沉魄下階","description":"下階表面覆著一層暗紅薄霜，每踩一步都會有極輕的魄鳴從石隙裡滲出，像整段階道正替更深處分擔震幅。","sector_type":"SECT_INSIDE","cluster":"entry-drop","coord":[1,0,-34],"labels":["mainline"],"exits":[{"direction":"west","to":10901},{"direction":"east","to":10903}]},
    {"vnum":10903,"name":"核心沉環前緣","description":"前緣俯看整圈沉環，環壁上的幽赤紋理像被無形力量強行拉成環流，勉強把四散的魄壓收束在這一層。","sector_type":"SECT_INSIDE","cluster":"spirit-ring","coord":[2,0,-34],"labels":["mainline"],"exits":[{"direction":"west","to":10902},{"direction":"east","to":10904},{"direction":"south","to":10907}]},
    {"vnum":10904,"name":"觀魄鎮座","description":"鎮座周圍豎著數面殘缺觀魄碑，碑面偶爾映出不屬於此地的模糊輪廓，隨即又被沉環赤光撕碎吞沒。","sector_type":"SECT_INSIDE","cluster":"spirit-ring","coord":[3,0,-34],"labels":["lore"],"exits":[{"direction":"west","to":10903},{"direction":"east","to":10905}],"enquires":["觀魄","鎮座"]},
    {"vnum":10905,"name":"伏魄引槽","description":"引槽把各股魄壓導向更深主井，槽底不時有亮白裂絲一閃即滅，像核心正試圖掙開這裡最後一道收束。","sector_type":"SECT_INSIDE","cluster":"spirit-ring","coord":[4,0,-34],"labels":["pressure"],"exits":[{"direction":"west","to":10904},{"direction":"east","to":10906},{"direction":"south","to":10909}],"keywords":[{"keyword":"引槽","description":"引槽內壁刻滿逆向封紋，顯然不是為了鎮住表面波動，而是為了延遲更深層魄壓衝上來的速度。"}]},
    {"vnum":10906,"name":"聽魄沉座","description":"沉座中央懸著一枚裂痕密布的玄黑石核，石核每隔片刻便發出短促低鳴，像真正的魄源正在更深處回應。","sector_type":"SECT_INSIDE","cluster":"spirit-ring","coord":[5,0,-34],"labels":["signal"],"exits":[{"direction":"west","to":10905}]},
    {"vnum":10907,"name":"失魄側階","description":"側階向偏廊傾斜下切，石面殘留的灰白碎屑一踩即散，像曾經附著其上的魂屑早被下方氣流反覆剝離。","sector_type":"SECT_INSIDE","cluster":"shatter-annex","coord":[2,-1,-34],"labels":["annex"],"exits":[{"direction":"north","to":10903},{"direction":"east","to":10908}]},
    {"vnum":10908,"name":"離魄偏廊","description":"偏廊兩壁嵌著一列早已失穩的維魄片，碎片仍在陰影裡忽明忽滅，像在記錄每一次未能被封住的魄壓外洩。","sector_type":"SECT_INSIDE","cluster":"shatter-annex","coord":[3,-1,-34],"labels":["service"],"exits":[{"direction":"west","to":10907},{"direction":"east","to":10909}],"enquires":["維魄","偏廊"]},
    {"vnum":10909,"name":"逆魄裂廊","description":"裂廊中央張開一道細長暗縫，縫底不見光，只偶爾向外噴出一股帶著嗚咽聲的熱流，把整條通道燙得微微顫抖。","sector_type":"SECT_INSIDE","cluster":"shatter-annex","coord":[4,-1,-34],"labels":["risk"],"exits":[{"direction":"north","to":10905},{"direction":"west","to":10908},{"direction":"east","to":10910}]},
    {"vnum":10910,"name":"魄淵前橋","description":"前橋跨在一道近乎垂直下墜的暗井上方，橋面每次震動都帶著延遲極長的回響，像深淵底部仍有更慢卻更重的鼓動。","sector_type":"SECT_INSIDE","cluster":"abyss-threshold","coord":[5,-1,-34],"labels":["bridge"],"exits":[{"direction":"west","to":10909},{"direction":"south","to":10911}]},
    {"vnum":10911,"name":"沉魄井緣","description":"井緣外圍著數根向內扭折的封魄柱，柱身殘光一路向深井腹地墜去，像在替來者標示最後一段仍可回頭的高度。","sector_type":"SECT_INSIDE","cluster":"abyss-threshold","coord":[5,-2,-34],"labels":["threshold"],"exits":[{"direction":"north","to":10910},{"direction":"down","to":10912}],"enquires":["井緣","封魄柱"]},
    {"vnum":10912,"name":"核心魄淵座","description":"魄淵座像整個核心外層最後的立足邊界，腳下只剩持續向下抽離的幽赤暗潮，任何聲音落下去都像被更深層存在慢慢吞沒。","sector_type":"SECT_INSIDE","cluster":"abyss-threshold","coord":[5,-2,-35],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10911}],"enquires":["魄淵","深處"]}
  ]
}
```
