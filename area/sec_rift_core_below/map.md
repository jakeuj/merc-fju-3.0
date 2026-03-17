# 裂核下層 (`sec_rift_core_below`)

## Area Intent

`sec_rift_core_below` 承接裂界本核核心臺下方的深井，將探索重心由外環封圈推進到井內裂脈主道。此區定位為「深井過渡層」：讓玩家在強壓脈動與碎化封橋之間尋找立足點，並為更深層裂核區預留明確世界連接。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂核下層 / 深井脈道`
- LevelRange: `66-82`
- Parent area: `sec_rift_true_core`
- ReservedRoomBlock: `10301-10320`

## Planned World Links

- `up` from `10301`: `sec_rift_true_core` room `10212`
- `down` from `10312`: future deeper rift-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core_below",
    "title": "裂核下層",
    "design_notes": "裂界本核下方的深井脈道，作為更深裂核區前的首段過渡層。",
    "parent_area": "sec_rift_true_core",
    "level_range": "66-82",
    "planned_vnum_range": "10301-10320",
    "reserved_room_block": "10301-10320",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂核下層 / 深井脈道"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10301,
        "target_area": "sec_rift_true_core",
        "target_room_vnum": 10212,
        "label": "本核縱井"
      },
      {
        "direction": "down",
        "source_vnum": 10312,
        "target_area": "sec_rift_core_below_deeps",
        "label": "裂核底脈"
      }
    ],
    "clusters": [
      { "id": "well-foot", "label": "落井接臺" },
      { "id": "rift-mainline", "label": "深井裂道" },
      { "id": "vein-annex", "label": "導脈側廊" },
      { "id": "seal-bridge", "label": "下層封橋" }
    ]
  },
  "rooms": [
    {"vnum":10301,"name":"落井承臺","description":"承臺懸在黑紅井壁之間，背後仍看得到上層核心臺殘光，前方卻只剩向下延展的裂道與低沉脈鳴。","sector_type":"SECT_INSIDE","cluster":"well-foot","coord":[0,0,-22],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10212,"external":true},{"direction":"east","to":10302}],"enquires":["退路","井壁"]},
    {"vnum":10302,"name":"裂井橫踏","description":"橫踏以粗石樑跨越井側縫隙，石面佈滿被高熱反覆燒蝕後留下的玻化紋。","sector_type":"SECT_INSIDE","cluster":"well-foot","coord":[1,0,-22],"labels":["mainline"],"exits":[{"direction":"west","to":10301},{"direction":"east","to":10303}]},
    {"vnum":10303,"name":"深井裂道","description":"裂道沿井壁向內延伸，地面每隔一段便可見舊封紋崩斷的斜裂痕，像有人曾在此急就補封。","sector_type":"SECT_INSIDE","cluster":"rift-mainline","coord":[2,0,-22],"labels":["mainline"],"exits":[{"direction":"west","to":10302},{"direction":"east","to":10304},{"direction":"south","to":10306}]},
    {"vnum":10304,"name":"脈壓觀井臺","description":"井臺外側是翻湧不定的脈霧，霧中偶爾浮現巨大暗紋，像有某種封印結構仍在底層運作。","sector_type":"SECT_INSIDE","cluster":"rift-mainline","coord":[3,0,-22],"labels":["lore"],"exits":[{"direction":"west","to":10303},{"direction":"east","to":10305}],"enquires":["脈壓","暗紋"]},
    {"vnum":10305,"name":"裂脈節點帶","description":"節點帶排列著多組導脈石樁，石樁頂端反覆冒出細碎電芒，顯示此處壓差長期處於危險邊緣。","sector_type":"SECT_INSIDE","cluster":"rift-mainline","coord":[4,0,-22],"labels":["pressure"],"exits":[{"direction":"west","to":10304},{"direction":"south","to":10310}],"keywords":[{"keyword":"石樁","description":"每組石樁都刻著不同年代修補標記，可看出這條裂道曾多次被迫延命。"}]},
    {"vnum":10306,"name":"導脈側轉廊","description":"側轉廊刻滿細密導脈線，微光沿線奔流，把主裂道溢出的壓流分送至下方封橋區。","sector_type":"SECT_INSIDE","cluster":"vein-annex","coord":[2,-1,-22],"labels":["annex"],"exits":[{"direction":"north","to":10303},{"direction":"east","to":10307}],"enquires":["導脈","補封"]},
    {"vnum":10307,"name":"監測窄廳","description":"窄廳牆面留有密集測壓刻線，最新幾道記錄已超過原始量尺，旁邊還插著斷裂筆桿。","sector_type":"SECT_INSIDE","cluster":"vein-annex","coord":[3,-1,-22],"labels":["service"],"exits":[{"direction":"west","to":10306},{"direction":"east","to":10308}]},
    {"vnum":10308,"name":"餘壓洩放室","description":"洩放室中央槽池翻著紅黑泡沫，邊緣散落半融的鎮印片，空氣裡充滿刺鼻焦鐵味。","sector_type":"SECT_INSIDE","cluster":"vein-annex","coord":[4,-1,-22],"labels":["risk"],"exits":[{"direction":"west","to":10307},{"direction":"east","to":10309}]},
    {"vnum":10309,"name":"補紋工間","description":"工間堆滿不同規格補紋石版，多數只完成一半就因壓流逆灌而報廢。","sector_type":"SECT_INSIDE","cluster":"vein-annex","coord":[5,-1,-22],"labels":["supply"],"exits":[{"direction":"west","to":10308}]},
    {"vnum":10310,"name":"下層前橋","description":"前橋橫跨一道更深裂縫，橋面每次震動都伴隨低鳴回響，像深處核心正以固定節奏呼吸。","sector_type":"SECT_INSIDE","cluster":"seal-bridge","coord":[4,-2,-22],"labels":["bridge"],"exits":[{"direction":"north","to":10305},{"direction":"south","to":10311}]},
    {"vnum":10311,"name":"封橋井緣","description":"井緣立著半毀封柱，柱基仍持續輸出微弱光脈，勉強維持前往底脈的唯一落點。","sector_type":"SECT_INSIDE","cluster":"seal-bridge","coord":[4,-3,-22],"labels":["threshold"],"exits":[{"direction":"north","to":10310},{"direction":"down","to":10312}],"enquires":["封柱","底脈"]},
    {"vnum":10312,"name":"裂核底脈臺","description":"底脈臺懸在深井最低可見處，腳下黑紅脈潮翻湧不息，彷彿還有更巨大的裂核層在更下方緩慢甦醒。","sector_type":"SECT_INSIDE","cluster":"seal-bridge","coord":[4,-3,-23],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10311}],"enquires":["深層","脈潮"]}
  ]
}
```
