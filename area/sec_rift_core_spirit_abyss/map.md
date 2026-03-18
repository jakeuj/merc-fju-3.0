# 魄淵深井 (`sec_rift_core_spirit_abyss`)

## Area Intent

`sec_rift_core_spirit_abyss` 承接核心魄淵最深的魄淵座，再往下沉入魄井暗層與空響回廊。此區定位為「暗層沉降」：讓玩家從魄井落層、深井環脈與空響偏廊之間，感受到魄壓已不只外洩，而是開始在更深空井內自行迴盪，並為更深魄核空井區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `魄淵深井 / 暗層沉降`
- LevelRange: `88-104`
- Parent area: `sec_rift_core_spirit_nadir`
- ReservedRoomBlock: `11001-11020`

## Planned World Links

- `up` from `11001`: `sec_rift_core_spirit_nadir` room `10912`
- `down` from `11012`: future deeper core-spirit extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core_spirit_abyss",
    "title": "魄淵深井",
    "design_notes": "核心魄淵之下的魄井暗層，作為更深魄核空井區前的過渡主段。",
    "parent_area": "sec_rift_core_spirit_nadir",
    "level_range": "88-104",
    "planned_vnum_range": "11001-11020",
    "reserved_room_block": "11001-11020",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "魄淵深井 / 暗層沉降"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11001,
        "target_area": "sec_rift_core_spirit_nadir",
        "target_room_vnum": 10912,
        "label": "核心魄淵座"
      },
      {
        "direction": "down",
        "source_vnum": 11012,
        "target_area": "sec_rift_spirit_core_hollow",
        "label": "魄核空井"
      }
    ],
    "clusters": [
      { "id": "entry-well", "label": "魄井落層" },
      { "id": "abyss-ring", "label": "深井環脈" },
      { "id": "echo-annex", "label": "空響偏廊" },
      { "id": "hollow-threshold", "label": "魄核前座" }
    ]
  },
  "rooms": [
    {"vnum":11001,"name":"魄井落層臺","description":"落層臺貼著深井內壁伸出，腳下石層微微顫動，像更深空井正以某種無聲節奏把魄壓一圈圈抽離下去。","sector_type":"SECT_INSIDE","cluster":"entry-well","coord":[0,0,-36],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10912,"external":true},{"direction":"east","to":11002}],"enquires":["退路","深井"]},
    {"vnum":11002,"name":"沉響下階","description":"下階滿佈細密裂紋，裂縫裡不時滲出像餘音般的幽亮氣絲，彷彿每一步都在踩著尚未散盡的魄鳴回聲。","sector_type":"SECT_INSIDE","cluster":"entry-well","coord":[1,0,-36],"labels":["mainline"],"exits":[{"direction":"west","to":11001},{"direction":"east","to":11003}]},
    {"vnum":11003,"name":"深井環脈前緣","description":"前緣俯視整圈深井環脈，環壁上的幽赤紋路時聚時散，像在替更深層空井收束那些尚未完全離體的魄壓。","sector_type":"SECT_INSIDE","cluster":"abyss-ring","coord":[2,0,-36],"labels":["mainline"],"exits":[{"direction":"west","to":11002},{"direction":"east","to":11004},{"direction":"south","to":11007}]},
    {"vnum":11004,"name":"鎮響觀魄座","description":"觀魄座周圍立著幾面向內傾斜的鎮響碑，碑面並不映人，只映得出更深處一道道延遲極長的暗紅回光。","sector_type":"SECT_INSIDE","cluster":"abyss-ring","coord":[3,0,-36],"labels":["lore"],"exits":[{"direction":"west","to":11003},{"direction":"east","to":11005}],"enquires":["鎮響","觀魄"]},
    {"vnum":11005,"name":"魄潮引脈槽","description":"引脈槽把幾股魄潮慢慢導向更深井腹，槽底偶爾會跳起一道蒼白裂光，像有什麼更大的存在正在井底反覆試探外層。","sector_type":"SECT_INSIDE","cluster":"abyss-ring","coord":[4,0,-36],"labels":["pressure"],"exits":[{"direction":"west","to":11004},{"direction":"east","to":11006},{"direction":"south","to":11009}],"keywords":[{"keyword":"引脈","description":"引脈槽內壁刻滿反覆補寫的鎮壓紋，顯然這裡承接的魄潮從來沒有真正穩定過。"}]},
    {"vnum":11006,"name":"聽響沉井座","description":"沉井座中央垂著一枚細長黑晶，晶體每隔片刻便傳出一記低沉空響，像深井底部有更深魄核正在緩慢回應。","sector_type":"SECT_INSIDE","cluster":"abyss-ring","coord":[5,0,-36],"labels":["signal"],"exits":[{"direction":"west","to":11005}]},
    {"vnum":11007,"name":"空響側階","description":"側階往偏廊斜切時幾乎聽不見腳步，只剩石面裡傳出的遲滯回聲，像所有聲息都被更深處先吞進去再慢慢吐回。","sector_type":"SECT_INSIDE","cluster":"echo-annex","coord":[2,-1,-36],"labels":["annex"],"exits":[{"direction":"north","to":11003},{"direction":"east","to":11008}]},
    {"vnum":11008,"name":"離響偏廊","description":"偏廊兩側嵌著一排碎裂導響片，碎片仍在陰影裡斷續亮起，像在替每一次魄壓外洩留下難以抹平的空響痕跡。","sector_type":"SECT_INSIDE","cluster":"echo-annex","coord":[3,-1,-36],"labels":["service"],"exits":[{"direction":"west","to":11007},{"direction":"east","to":11009}],"enquires":["導響","偏廊"]},
    {"vnum":11009,"name":"逆響裂廊","description":"裂廊中央張開一道深不見底的暗縫，偶爾會向外吐出帶著長尾回音的熱流，把整條走道烘得像在顫抖。","sector_type":"SECT_INSIDE","cluster":"echo-annex","coord":[4,-1,-36],"labels":["risk"],"exits":[{"direction":"north","to":11005},{"direction":"west","to":11008},{"direction":"east","to":11010}]},
    {"vnum":11010,"name":"魄核前橋","description":"前橋橫跨在更深井腹上方，橋面每一次震動都伴著極慢回響，像橋下有某個更重更遠的存在正在持續向上撞擊。","sector_type":"SECT_INSIDE","cluster":"hollow-threshold","coord":[5,-1,-36],"labels":["bridge"],"exits":[{"direction":"west","to":11009},{"direction":"south","to":11011}]},
    {"vnum":11011,"name":"空井井緣","description":"井緣外圍著一圈向內扭折的封魄柱基，柱基殘光一路往井腹深處滑落，像在標示最後一段仍屬於外層封印的邊界。","sector_type":"SECT_INSIDE","cluster":"hollow-threshold","coord":[5,-2,-36],"labels":["threshold"],"exits":[{"direction":"north","to":11010},{"direction":"down","to":11012}],"enquires":["空井","井緣"]},
    {"vnum":11012,"name":"魄核沉座","description":"沉座像整條深井最後一塊能立足的陰影，腳下只剩持續向下凹陷的幽赤暗環，所有聲音都在這裡被拖往更深的魄核空井。","sector_type":"SECT_INSIDE","cluster":"hollow-threshold","coord":[5,-2,-37],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11011}],"enquires":["魄核","深處"]}
  ]
}
```
