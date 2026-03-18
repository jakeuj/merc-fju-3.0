# 封核沉盆 (`sec_rift_sealed_core_basin`)

## Area Intent

`sec_rift_sealed_core_basin` 承接禁底封脈盆最深的沉門，下沉到真正包住封核內壓的核心沉盆。此區定位為「內壓核心」：讓玩家在封核環盆、回壓渠廊與封心前庭之間感受到封印系統已逼近極限，並為更深裂核封心區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `封核沉盆 / 內壓核心`
- LevelRange: `80-96`
- Parent area: `sec_rift_underseal_basin`
- ReservedRoomBlock: `10701-10720`

## Planned World Links

- `up` from `10701`: `sec_rift_underseal_basin` room `10612`
- `down` from `10712`: future deeper sealed-core heart extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_sealed_core_basin",
    "title": "封核沉盆",
    "design_notes": "禁底封脈盆之下的封核沉盆，作為更深裂核封心區前的核心承壓內盆。",
    "parent_area": "sec_rift_underseal_basin",
    "level_range": "80-96",
    "planned_vnum_range": "10701-10720",
    "reserved_room_block": "10701-10720",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "封核沉盆 / 內壓核心"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10701,
        "target_area": "sec_rift_underseal_basin",
        "target_room_vnum": 10612,
        "label": "禁底沉門"
      },
      {
        "direction": "down",
        "source_vnum": 10712,
        "target_area": "sec_rift_sealed_core_heart",
        "label": "封心深井"
      }
    ],
    "clusters": [
      { "id": "entry-sink", "label": "沉門落盆" },
      { "id": "core-ring", "label": "封核環盆" },
      { "id": "pressure-sluice", "label": "回壓渠廊" },
      { "id": "heart-threshold", "label": "封心前庭" }
    ]
  },
  "rooms": [
    {"vnum":10701,"name":"沉門落盆臺","description":"落盆臺像被整片沉門壓進盆底，四周石面覆著濕冷暗膜，連腳步聲都像被封進地層裡慢半拍才傳回。","sector_type":"SECT_INSIDE","cluster":"entry-sink","coord":[0,0,-30],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10612,"external":true},{"direction":"east","to":10702}],"enquires":["退路","沉門"]},
    {"vnum":10702,"name":"內盆踏稜","description":"踏稜沿盆壁向內微微下斜，石脊間布滿像血脈般的暗紅細線，隨著腳步節奏一明一滅。","sector_type":"SECT_INSIDE","cluster":"entry-sink","coord":[1,0,-30],"labels":["mainline"],"exits":[{"direction":"west","to":10701},{"direction":"east","to":10703}]},
    {"vnum":10703,"name":"封核環盆前緣","description":"前緣正對著整座封核環盆，盆心有一圈圈回壓波紋向外推展，像整片內盆都在替中央某物分攤脈衝。","sector_type":"SECT_INSIDE","cluster":"core-ring","coord":[2,0,-30],"labels":["mainline"],"exits":[{"direction":"west","to":10702},{"direction":"east","to":10704},{"direction":"south","to":10707}]},
    {"vnum":10704,"name":"封紋觀盆座","description":"觀盆座旁立著數截半沉封紋碑柱，柱身刻痕不斷重複同一段鎮壓式樣，卻在末端出現明顯崩裂。","sector_type":"SECT_INSIDE","cluster":"core-ring","coord":[3,0,-30],"labels":["lore"],"exits":[{"direction":"west","to":10703},{"direction":"east","to":10705}],"enquires":["封紋","碑柱"]},
    {"vnum":10705,"name":"回壓分盆","description":"分盆以環狀溝槽切出數層內外圈，濃重脈液順著溝底繞行，偶爾在交會處湧起沉悶的震鳴。","sector_type":"SECT_INSIDE","cluster":"core-ring","coord":[4,0,-30],"labels":["pressure"],"exits":[{"direction":"west","to":10704},{"direction":"east","to":10706},{"direction":"south","to":10709}],"keywords":[{"keyword":"溝槽","description":"溝槽內側佈滿細密補封痕，看得出這裡曾被反覆加厚，卻仍壓不住回湧的內脈。"}]},
    {"vnum":10706,"name":"封核聽盆","description":"聽盆中央豎著一支封核聽柱，柱體每隔片刻就傳來低沉回響，像更深處有心跳正順著石層向上叩擊。","sector_type":"SECT_INSIDE","cluster":"core-ring","coord":[5,0,-30],"labels":["signal"],"exits":[{"direction":"west","to":10705}]},
    {"vnum":10707,"name":"回壓渠階","description":"渠階往下銜進一條狹長側渠，石階表面被濃稠脈液拋磨得近乎鏡亮，映出扭曲而不穩的赤光。","sector_type":"SECT_INSIDE","cluster":"pressure-sluice","coord":[2,-1,-30],"labels":["annex"],"exits":[{"direction":"north","to":10703},{"direction":"east","to":10708}]},
    {"vnum":10708,"name":"維封側渠","description":"側渠兩旁嵌著大批失效封片，部分碎片仍會在黑暗裡自行亮起，像最後一點維封餘勁還在苦撐。","sector_type":"SECT_INSIDE","cluster":"pressure-sluice","coord":[3,-1,-30],"labels":["service"],"exits":[{"direction":"west","to":10707},{"direction":"east","to":10709}],"enquires":["側渠","維封"]},
    {"vnum":10709,"name":"逆湧裂渠","description":"裂渠中段裂開一道深黑縫口，偶爾會有灼熱霧氣自縫底反衝上來，把整條通道照成忽明忽暗的赤影。","sector_type":"SECT_INSIDE","cluster":"pressure-sluice","coord":[4,-1,-30],"labels":["risk"],"exits":[{"direction":"north","to":10705},{"direction":"west","to":10708},{"direction":"east","to":10710}]},
    {"vnum":10710,"name":"封心前橋","description":"前橋橫跨沉盆最深的一道封壓裂帶，橋下不斷傳來石基被反覆震擊的悶響，像某道更深的門正試著向上推開。","sector_type":"SECT_INSIDE","cluster":"heart-threshold","coord":[5,-1,-30],"labels":["bridge"],"exits":[{"direction":"west","to":10709},{"direction":"south","to":10711}]},
    {"vnum":10711,"name":"封心井緣","description":"井緣周圍圍著一圈幾乎沉沒的封心柱，柱身殘光沿著裂紋緩慢滑動，勉強把井底傳來的壓流束成一條可行窄路。","sector_type":"SECT_INSIDE","cluster":"heart-threshold","coord":[5,-2,-30],"labels":["threshold"],"exits":[{"direction":"north","to":10710},{"direction":"down","to":10712}],"enquires":["封心","井緣"]},
    {"vnum":10712,"name":"封核深井","description":"深井內只剩一片向下收束的黑紅光潮，所有回音都在幾步之外被拖進更深處，像這裡只是封心主體前最後一個可站立的邊界。","sector_type":"SECT_INSIDE","cluster":"heart-threshold","coord":[5,-2,-31],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10711}],"enquires":["深井","核心"]}
  ]
}
```
