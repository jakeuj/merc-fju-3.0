# 裂魄真空 (`sec_rift_spirit_core_vacuum`)

## Area Intent

`sec_rift_spirit_core_vacuum` 承接裂魄空心最深的裂魄虛座，再往下沉入裂魄真空與真空深腹。此區定位為「真空深腹」：讓玩家從真空落臺、真空環脈與滅響偏廊之間，感受到魄壓已被抽離到連震痕都近乎停滯，並為更深裂魄歸零區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄真空 / 真空深腹`
- LevelRange: `94-110`
- Parent area: `sec_rift_spirit_core_void`
- ReservedRoomBlock: `11301-11320`

## Planned World Links

- `up` from `11301`: `sec_rift_spirit_core_void` room `11212`
- `down` from `11312`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_vacuum",
    "title": "裂魄真空",
    "design_notes": "裂魄空心之下的真空深腹，作為更深歸零層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_void",
    "level_range": "94-110",
    "planned_vnum_range": "11301-11320",
    "reserved_room_block": "11301-11320",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄真空 / 真空深腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11301,
        "target_area": "sec_rift_spirit_core_void",
        "target_room_vnum": 11212,
        "label": "裂魄虛座"
      },
      {
        "direction": "down",
        "source_vnum": 11312,
        "target_area": "sec_rift_spirit_core_null",
        "label": "裂魄歸零"
      }
    ],
    "clusters": [
      { "id": "entry-shelf", "label": "真空落臺" },
      { "id": "vacuum-ring", "label": "真空環脈" },
      { "id": "null-annex", "label": "滅響偏廊" },
      { "id": "null-threshold", "label": "歸零前座" }
    ]
  },
  "rooms": [
    {"vnum":11301,"name":"真空落臺","description":"落臺像嵌在黑空內壁的一截石臺，邊緣殘留的暗紋不再震動，只以極慢的速度往下滑落，像整個深腹正被更深處的歸零層悄悄拖走。","sector_type":"SECT_INSIDE","cluster":"entry-shelf","coord":[0,0,-42],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11212,"external":true},{"direction":"east","to":11302}],"enquires":["退路","真空"]},
    {"vnum":11302,"name":"真空下階","description":"下階表面失去了先前井層那種明顯的抽蝕聲，只剩石面裡側偶爾漫出的鈍白冷痕，讓每一步都像踏進無聲深水。","sector_type":"SECT_INSIDE","cluster":"entry-shelf","coord":[1,0,-42],"labels":["mainline"],"exits":[{"direction":"west","to":11301},{"direction":"east","to":11303}]},
    {"vnum":11303,"name":"真空環脈前緣","description":"前緣俯瞰整圈向內塌落的真空環脈，環壁上的暗環一層疊著一層向中心收縮，像深腹最深處正以絕對寂靜吸納所有殘流。","sector_type":"SECT_INSIDE","cluster":"vacuum-ring","coord":[2,0,-42],"labels":["mainline"],"exits":[{"direction":"west","to":11302},{"direction":"east","to":11304},{"direction":"south","to":11307}]},
    {"vnum":11304,"name":"觀滅鎮魄座","description":"鎮魄座旁的觀滅碑已幾乎失去碑形，只留下幾道內縮白痕，像連封印本身也在這裡開始被真空慢慢磨成空白。","sector_type":"SECT_INSIDE","cluster":"vacuum-ring","coord":[3,0,-42],"labels":["lore"],"exits":[{"direction":"west","to":11303},{"direction":"east","to":11305}],"enquires":["觀滅","鎮魄"]},
    {"vnum":11305,"name":"真空引流槽","description":"引流槽裡沒有水聲、沒有風聲，只有一道極細的白亮裂痕一路向下延伸，像所有餘波都被導向更深處那個看不見的歸零核心。","sector_type":"SECT_INSIDE","cluster":"vacuum-ring","coord":[4,0,-42],"labels":["pressure"],"exits":[{"direction":"west","to":11304},{"direction":"east","to":11306},{"direction":"south","to":11309}],"keywords":[{"keyword":"引流","description":"槽壁封紋比上層更簡短而冷硬，顯示這裡已不再試圖調節壓力，只剩單向下送的殘酷功能。"}]},
    {"vnum":11306,"name":"聽滅沉座","description":"沉座中央懸著一枚灰白長晶，晶體沒有震鳴，也沒有回音，卻讓整片真空環脈像被某種無形重壓穩穩按住。","sector_type":"SECT_INSIDE","cluster":"vacuum-ring","coord":[5,0,-42],"labels":["signal"],"exits":[{"direction":"west","to":11305}]},
    {"vnum":11307,"name":"滅響側階","description":"側階斜切進偏廊時連腳步都像被吞掉，只剩靴底與石面擦過的一絲微澀觸感提醒你自己仍在移動。","sector_type":"SECT_INSIDE","cluster":"null-annex","coord":[2,-1,-42],"labels":["annex"],"exits":[{"direction":"north","to":11303},{"direction":"east","to":11308}]},
    {"vnum":11308,"name":"滅響偏廊","description":"偏廊兩側嵌著一排排斷裂導響片，片面只餘極淡白影，像舊日所有聲響都在此被削成無法回收的碎屑。","sector_type":"SECT_INSIDE","cluster":"null-annex","coord":[3,-1,-42],"labels":["service"],"exits":[{"direction":"west","to":11307},{"direction":"east","to":11309}],"enquires":["滅響","偏廊"]},
    {"vnum":11309,"name":"真空逆廊","description":"逆廊中央裂著一道纖長白縫，縫底沒有任何翻湧，只維持一種近乎靜止的下墜感，像整段深腹正朝著歸零邊界緩慢墜落。","sector_type":"SECT_INSIDE","cluster":"null-annex","coord":[4,-1,-42],"labels":["risk"],"exits":[{"direction":"north","to":11305},{"direction":"west","to":11308},{"direction":"east","to":11310}]},
    {"vnum":11310,"name":"歸零前橋","description":"前橋橫跨在一段連黑暗都顯得過度稀薄的空腔上方，橋面每次受力後都只剩一圈極淡白痕，像所有振動都被即刻抹平。","sector_type":"SECT_INSIDE","cluster":"null-threshold","coord":[5,-1,-42],"labels":["bridge"],"exits":[{"direction":"west","to":11309},{"direction":"south","to":11311}]},
    {"vnum":11311,"name":"真空井緣","description":"井緣圍著數座向內傾斜的封魄柱臺，柱臺上的白痕正一條條慢慢淡去，彷彿這裡是最後仍能辨認形體的邊界。","sector_type":"SECT_INSIDE","cluster":"null-threshold","coord":[5,-2,-42],"labels":["threshold"],"exits":[{"direction":"north","to":11310},{"direction":"down","to":11312}],"enquires":["井緣","柱臺"]},
    {"vnum":11312,"name":"裂魄真空座","description":"真空座像整段真空深腹最後一塊仍勉強存在的石影，腳下只剩一圈幾乎靜止的白暗空環，所有殘痕都在這裡被拖往更深的裂魄歸零。","sector_type":"SECT_INSIDE","cluster":"null-threshold","coord":[5,-2,-43],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11311}],"enquires":["真空座","深處"]}
  ]
}
```
