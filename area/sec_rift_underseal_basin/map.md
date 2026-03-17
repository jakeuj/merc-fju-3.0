# 禁底封脈盆 (`sec_rift_underseal_basin`)

## Area Intent

`sec_rift_underseal_basin` 承接裂核脈淵最底端的沉檻，下沉到真正承受封脈回壓的禁底盆地。此區定位為「沉壓承接層」：讓玩家在封脈環池、沉陷壓紋與底盆沉門之間維持推進節奏，並為更深裂核禁底核心區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `禁底封脈 / 沉壓盆地`
- LevelRange: `76-92`
- Parent area: `sec_rift_core_vein_abyss`
- ReservedRoomBlock: `10601-10620`

## Planned World Links

- `up` from `10601`: `sec_rift_core_vein_abyss` room `10512`
- `down` from `10612`: future deeper sealed-core basin extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_underseal_basin",
    "title": "禁底封脈盆",
    "design_notes": "裂核脈淵之下的禁底封脈盆地，作為更深裂核禁底核心區前的沉壓承接層。",
    "parent_area": "sec_rift_core_vein_abyss",
    "level_range": "76-92",
    "planned_vnum_range": "10601-10620",
    "reserved_room_block": "10601-10620",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "禁底封脈 / 沉壓盆地"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10601,
        "target_area": "sec_rift_core_vein_abyss",
        "target_room_vnum": 10512,
        "label": "脈淵沉檻"
      },
      {
        "direction": "down",
        "source_vnum": 10612,
        "target_area": "sec_rift_sealed_core_basin",
        "label": "禁底核心"
      }
    ],
    "clusters": [
      { "id": "arrival-bowl", "label": "沉檻落盆" },
      { "id": "seal-ring-pool", "label": "封脈環池" },
      { "id": "pressure-side-lane", "label": "壓紋支廊" },
      { "id": "sunken-gate", "label": "底盆沉門" }
    ]
  },
  "rooms": [
    {"vnum":10601,"name":"沉檻落盆臺","description":"落盆臺卡在巨大盆地上緣，頭頂的脈淵已像一抹遠紅，四周則只剩沉厚得幾乎聽不見回音的封脈壓流。","sector_type":"SECT_INSIDE","cluster":"arrival-bowl","coord":[0,0,-28],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10512,"external":true},{"direction":"east","to":10602}],"enquires":["退路","盆地"]},
    {"vnum":10602,"name":"封盆踏脊","description":"踏脊沿盆地內壁蜿蜒，石面被長年壓流磨得發亮，每一步都能感到腳下有悶重脈震傳來。","sector_type":"SECT_INSIDE","cluster":"arrival-bowl","coord":[1,0,-28],"labels":["mainline"],"exits":[{"direction":"west","to":10601},{"direction":"east","to":10603}]},
    {"vnum":10603,"name":"環池前緣","description":"前緣俯瞰整座封脈環池，池中黑紅脈液呈環狀緩慢旋流，像在把更深處的壓力分批導開。","sector_type":"SECT_INSIDE","cluster":"seal-ring-pool","coord":[2,0,-28],"labels":["mainline"],"exits":[{"direction":"west","to":10602},{"direction":"east","to":10604},{"direction":"south","to":10607}]},
    {"vnum":10604,"name":"封池觀座","description":"觀座旁殘留多座沉沒石碑，碑面記著歷代封池修補時的壓流紀錄，多數最後都停在同一段模糊缺口。","sector_type":"SECT_INSIDE","cluster":"seal-ring-pool","coord":[3,0,-28],"labels":["lore"],"exits":[{"direction":"west","to":10603},{"direction":"east","to":10605}],"enquires":["石碑","缺口"]},
    {"vnum":10605,"name":"沉壓節池","description":"節池以數圈低矮石檻切分不同流域，黑紅脈液在檻邊翻捲時會發出如低鳴般的震顫。","sector_type":"SECT_INSIDE","cluster":"seal-ring-pool","coord":[4,0,-28],"labels":["pressure"],"exits":[{"direction":"west","to":10604},{"direction":"east","to":10606},{"direction":"south","to":10609}],"keywords":[{"keyword":"石檻","description":"石檻表面滿是長年沖刷出的細紋，內側還能看到後補封泥被再次扯裂的痕跡。"}]},
    {"vnum":10606,"name":"回壓聽池","description":"聽池中央立著半折聽脈柱，柱內偶爾傳出悶雷般的回震，像整座盆地正在替更深處承受壓差。","sector_type":"SECT_INSIDE","cluster":"seal-ring-pool","coord":[5,0,-28],"labels":["signal"],"exits":[{"direction":"west","to":10605}]},
    {"vnum":10607,"name":"壓紋側階","description":"側階通往支廊的石級多半已沉陷，牆面壓紋被脈液浸得發黑，只剩零散亮線仍勉強串接。","sector_type":"SECT_INSIDE","cluster":"pressure-side-lane","coord":[2,-1,-28],"labels":["annex"],"exits":[{"direction":"north","to":10603},{"direction":"east","to":10608}]},
    {"vnum":10608,"name":"沉紋維壓廊","description":"維壓廊兩側嵌滿失效壓紋片，片面時而浮現微弱赤光，又很快被沉重陰影吞沒。","sector_type":"SECT_INSIDE","cluster":"pressure-side-lane","coord":[3,-1,-28],"labels":["service"],"exits":[{"direction":"west","to":10607},{"direction":"east","to":10609}],"enquires":["壓紋","維壓"]},
    {"vnum":10609,"name":"回湧裂廊","description":"裂廊地面裂開長長一道黑縫，縫中不時噴出短促熱浪，把四周石壁照得像在呼吸。","sector_type":"SECT_INSIDE","cluster":"pressure-side-lane","coord":[4,-1,-28],"labels":["risk"],"exits":[{"direction":"north","to":10605},{"direction":"west","to":10608},{"direction":"east","to":10610}]},
    {"vnum":10610,"name":"底盆封橋","description":"封橋橫跨盆地最深的沉壓裂帶，橋下脈液撞擊石基時發出的悶響，像遠處有門扉正被反覆敲擊。","sector_type":"SECT_INSIDE","cluster":"sunken-gate","coord":[5,-1,-28],"labels":["bridge"],"exits":[{"direction":"west","to":10609},{"direction":"south","to":10611}]},
    {"vnum":10611,"name":"沉門井緣","description":"井緣外圍著一圈半沉封柱，柱頂細光沿著殘缺刻紋流動，勉強把更深處的壓流束成一條窄路。","sector_type":"SECT_INSIDE","cluster":"sunken-gate","coord":[5,-2,-28],"labels":["threshold"],"exits":[{"direction":"north","to":10610},{"direction":"down","to":10612}],"enquires":["封柱","井緣"]},
    {"vnum":10612,"name":"禁底沉門","description":"沉門下方只剩一片向內收斂的黑紅深井，所有回音與光線都被更深處的封脈核心吸走，彷彿此地只是最後一道前庭。","sector_type":"SECT_INSIDE","cluster":"sunken-gate","coord":[5,-2,-29],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10611}],"enquires":["沉門","核心"]}
  ]
}
```
