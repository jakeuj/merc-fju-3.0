# 裂核深層 (`sec_rift_core_below_deeps`)

## Area Intent

`sec_rift_core_below_deeps` 承接裂核下層最底端的落脈臺，將探索重心帶入脈潮長期堆積的渦腹地帶。此區定位為「深層承接區」：讓玩家在高壓脈流、逆灌裂潮與半失效鎮紋之間維持推進路線，並為後續更深裂核渦核區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂核深層 / 底脈渦腹`
- LevelRange: `68-84`
- Parent area: `sec_rift_core_below`
- ReservedRoomBlock: `10401-10420`

## Planned World Links

- `up` from `10401`: `sec_rift_core_below` room `10312`
- `down` from `10412`: future deeper core-vein abyss extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core_below_deeps",
    "title": "裂核深層",
    "design_notes": "裂核下層之下的底脈渦腹，作為更深裂核渦核區前的第二段承接層。",
    "parent_area": "sec_rift_core_below",
    "level_range": "68-84",
    "planned_vnum_range": "10401-10420",
    "reserved_room_block": "10401-10420",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂核深層 / 底脈渦腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10401,
        "target_area": "sec_rift_core_below",
        "target_room_vnum": 10312,
        "label": "裂核底脈臺"
      },
      {
        "direction": "down",
        "source_vnum": 10412,
        "target_area": "sec_rift_core_vein_abyss",
        "label": "渦核深淵"
      }
    ],
    "clusters": [
      { "id": "arrival-dais", "label": "落脈承臺" },
      { "id": "vortex-mainline", "label": "渦腹主脈" },
      { "id": "seal-aux-lane", "label": "鎮紋旁廊" },
      { "id": "deep-throat", "label": "底潮封口" }
    ]
  },
  "rooms": [
    {"vnum":10401,"name":"落脈承臺","description":"承臺懸在翻騰脈霧上方，抬頭仍可見上層底脈臺若隱若現，腳下則是無法看透的黑紅渦潮。","sector_type":"SECT_INSIDE","cluster":"arrival-dais","coord":[0,0,-24],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10312,"external":true},{"direction":"east","to":10402}],"enquires":["渦潮","退路"]},
    {"vnum":10402,"name":"脈渦踏道","description":"踏道以層層斷石拼補而成，石縫間滲出高熱脈液，踩上去時能感到整段結構在低頻震動。","sector_type":"SECT_INSIDE","cluster":"arrival-dais","coord":[1,0,-24],"labels":["mainline"],"exits":[{"direction":"west","to":10401},{"direction":"east","to":10403}]},
    {"vnum":10403,"name":"渦腹前脈","description":"前脈走廊沿著井壁繞行，牆面殘留多層封紋覆寫痕跡，顯示這裡曾被反覆加固。","sector_type":"SECT_INSIDE","cluster":"vortex-mainline","coord":[2,0,-24],"labels":["mainline"],"exits":[{"direction":"west","to":10402},{"direction":"east","to":10404},{"direction":"south","to":10406}]},
    {"vnum":10404,"name":"逆流觀測臺","description":"觀測臺正對渦腹中心，黑紅潮流時而逆卷向上，像有巨物在下層緩慢翻身。","sector_type":"SECT_INSIDE","cluster":"vortex-mainline","coord":[3,0,-24],"labels":["lore"],"exits":[{"direction":"west","to":10403},{"direction":"east","to":10405}],"enquires":["逆流","巨影"]},
    {"vnum":10405,"name":"渦壓節脈臺","description":"節脈臺周圍立著數圈鎮壓石環，石環邊緣被磨出大量新裂紋，仍勉強維持壓差平衡。","sector_type":"SECT_INSIDE","cluster":"vortex-mainline","coord":[4,0,-24],"labels":["pressure"],"exits":[{"direction":"west","to":10404},{"direction":"south","to":10410}],"keywords":[{"keyword":"石環","description":"石環內圈刻有不同年代修補署記，最新一圈的刻痕已明顯顫裂。"}]},
    {"vnum":10406,"name":"鎮紋側廊","description":"側廊地面佈滿導紋槽，微弱光流沿槽道奔行，把主脈溢散的壓流分送至封口區。","sector_type":"SECT_INSIDE","cluster":"seal-aux-lane","coord":[2,-1,-24],"labels":["annex"],"exits":[{"direction":"north","to":10403},{"direction":"east","to":10407}],"enquires":["鎮紋","導流"]},
    {"vnum":10407,"name":"測壓窄廊","description":"窄廊牆上密布刻線，最新記錄已超出原始刻度上限，旁邊散著折斷的量測針。","sector_type":"SECT_INSIDE","cluster":"seal-aux-lane","coord":[3,-1,-24],"labels":["service"],"exits":[{"direction":"west","to":10406},{"direction":"east","to":10408}]},
    {"vnum":10408,"name":"餘潮卸放室","description":"卸放室中央槽池翻湧著黏稠脈潮，牆邊堆滿半融鎮印片，空氣中混著灼鐵與藥灰味。","sector_type":"SECT_INSIDE","cluster":"seal-aux-lane","coord":[4,-1,-24],"labels":["risk"],"exits":[{"direction":"west","to":10407},{"direction":"east","to":10409}]},
    {"vnum":10409,"name":"補紋備料間","description":"備料間層架上排著未完成的補紋石板，多數邊角已被逆灌脈潮腐蝕得斑駁脆裂。","sector_type":"SECT_INSIDE","cluster":"seal-aux-lane","coord":[5,-1,-24],"labels":["supply"],"exits":[{"direction":"west","to":10408}]},
    {"vnum":10410,"name":"底潮前橋","description":"前橋跨在兩股脈潮交會處，每次潮流撞擊橋基都會傳來深沉共鳴，震得胸口發緊。","sector_type":"SECT_INSIDE","cluster":"deep-throat","coord":[4,-2,-24],"labels":["bridge"],"exits":[{"direction":"north","to":10405},{"direction":"south","to":10411}]},
    {"vnum":10411,"name":"封口井緣","description":"井緣立著半毀封柱，柱芯仍有細弱光脈流轉，勉力維持通往更深層的單一路徑。","sector_type":"SECT_INSIDE","cluster":"deep-throat","coord":[4,-3,-24],"labels":["threshold"],"exits":[{"direction":"north","to":10410},{"direction":"down","to":10412}],"enquires":["封柱","深口"]},
    {"vnum":10412,"name":"渦核封檻臺","description":"封檻臺懸在可見最深處，腳下渦潮沿巨大脈縫盤旋而下，像在引向更深不可測的裂核渦核。","sector_type":"SECT_INSIDE","cluster":"deep-throat","coord":[4,-3,-25],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10411}],"enquires":["渦核","脈縫"]}
  ]
}
```
