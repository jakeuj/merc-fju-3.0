# 裂魄冥獄 (`sec_rift_spirit_core_infernal`)

## Area Intent

`sec_rift_spirit_core_infernal` 承接裂魄冥淵最深的裂魄冥淵座，再往下沉入裂魄冥獄與冥獄井腹。此區定位為「冥獄井腹」：讓玩家從冥獄落座、冥獄內庭與獄冥偏廊之間，感受到魄壓已從冥淵再被壓成近乎只剩獄核輪廓的冷硬界面，並為後續同級更硬的裂魄業獄層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄冥獄 / 冥獄井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_tartarean`
- ReservedRoomBlock: `13601-13620`

## Planned World Links

- `up` from `13601`: `sec_rift_spirit_core_tartarean` room `13512`
- `down` from `13612`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_infernal",
    "title": "裂魄冥獄",
    "design_notes": "裂魄冥淵之下的冥獄井腹，作為後續同級 plateau 業獄層區前的主段。",
    "parent_area": "sec_rift_spirit_core_tartarean",
    "level_range": "100-100",
    "planned_vnum_range": "13601-13620",
    "reserved_room_block": "13601-13620",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄冥獄 / 冥獄井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13601,
        "target_area": "sec_rift_spirit_core_tartarean",
        "target_room_vnum": 13512,
        "label": "裂魄冥淵座"
      },
      {
        "direction": "down",
        "source_vnum": 13612,
        "target_area": "sec_rift_spirit_core_gehennal",
        "label": "裂魄業獄"
      }
    ],
    "clusters": [
      { "id": "infernal-shelf", "label": "冥獄落座" },
      { "id": "infernal-court", "label": "冥獄內庭" },
      { "id": "gehennal-annex", "label": "獄冥偏廊" },
      { "id": "gehennal-threshold", "label": "業獄前座" }
    ]
  },
  "rooms": [
    {"vnum":13601,"name":"冥獄落座","description":"落座像嵌在冥獄外緣的一截黑沉魄石，腳下環界已硬到幾乎不再回應任何細微震盪，只剩一圈冷得近乎發脆的獄紋貼在石座邊沿，像把最後還能退回冥淵的路硬生生封成一道狹線。","sector_type":"SECT_INSIDE","cluster":"infernal-shelf","coord":[0,0,-87],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13512,"external":true},{"direction":"east","to":13602}],"enquires":["冥獄","退路"]},
    {"vnum":13602,"name":"獄紋沉階","description":"沉階表面覆著一層層向內扣合的獄紋，每踏下一階，都像踩進一塊還沒完全冷透的重獄鐵板，連鞋底殘留的聲音都會被壓成聽不見的黑點。","sector_type":"SECT_INSIDE","cluster":"infernal-shelf","coord":[1,0,-87],"labels":["mainline"],"exits":[{"direction":"west","to":13601},{"direction":"east","to":13603}]},
    {"vnum":13603,"name":"冥獄內庭前緣","description":"前緣俯瞰整座向內下壓的冥獄內庭，庭心像一口沒有火焰卻仍持續燒蝕魄殼的重井，視線一旦停久，連原本勉強還保得住的念頭輪廓都會被磨成更沉的暗印。","sector_type":"SECT_INSIDE","cluster":"infernal-court","coord":[2,0,-87],"labels":["mainline"],"exits":[{"direction":"west","to":13602},{"direction":"east","to":13604},{"direction":"south","to":13607}]},
    {"vnum":13604,"name":"聽獄鎮魄臺","description":"鎮魄臺旁的聽獄碑只剩幾道被高壓獄紋硬刻出來的細槽，碑與界在此幾乎只靠最後一層鎮束秩序分開，彷彿再往下壓一步，就會整片傾成沒有回頭餘地的業獄。","sector_type":"SECT_INSIDE","cluster":"infernal-court","coord":[3,0,-87],"labels":["lore"],"exits":[{"direction":"west","to":13603},{"direction":"east","to":13605}],"enquires":["聽獄","鎮魄"]},
    {"vnum":13605,"name":"冥獄沉黯槽","description":"沉黯槽裡看不見流勢，只剩一道被獄壓反覆擠窄的黑線沿槽底朝更深處緩慢收束，像整段井腹正在把最後仍帶名字的殘痕一筆筆壓成純粹的重暗。","sector_type":"SECT_INSIDE","cluster":"infernal-court","coord":[4,0,-87],"labels":["pressure"],"exits":[{"direction":"west","to":13604},{"direction":"east","to":13606},{"direction":"south","to":13609}],"keywords":[{"keyword":"沉黯","description":"槽壁封紋已被獄壓壓成難再分辨的暗層，只留下把界面持續逼向更深業獄的冷硬靜力。"}]},
    {"vnum":13606,"name":"聽獄沉座","description":"沉座中央懸著一枚像被整口冥獄硬生生壓薄的黑晶，晶體不發光，只持續把周圍還能分層的輪廓磨成一片更平整、更沉重的暗面。","sector_type":"SECT_INSIDE","cluster":"infernal-court","coord":[5,0,-87],"labels":["signal"],"exits":[{"direction":"west","to":13605}]},
    {"vnum":13607,"name":"獄冥側階","description":"側階斜切進偏廊時，腳下每一級都像被更深層獄壓提前鎖死，回頭再看，剛才踩過的紋路已收成幾道發黑的細線，像不願再把任何退回的餘地留給來人。","sector_type":"SECT_INSIDE","cluster":"gehennal-annex","coord":[2,-1,-87],"labels":["annex"],"exits":[{"direction":"north","to":13603},{"direction":"east","to":13608}]},
    {"vnum":13608,"name":"獄冥偏廊","description":"偏廊兩側嵌著一列列被壓得近乎貼平的導響殼片，殼面不再回應完整聲響，只會把人的念頭敲成更短、更重的幾段暗鳴，最後全數沉回井腹。","sector_type":"SECT_INSIDE","cluster":"gehennal-annex","coord":[3,-1,-87],"labels":["service"],"exits":[{"direction":"west","to":13607},{"direction":"east","to":13609}],"enquires":["獄冥","偏廊"]},
    {"vnum":13609,"name":"冥獄逆腹廊","description":"逆腹廊中央橫著一道只有側目時才看得出層差的獄裂，裂底既沒有火光也沒有回聲，卻像能把最後還保得住形名的碎片慢慢拖往更深的業獄井腹。","sector_type":"SECT_INSIDE","cluster":"gehennal-annex","coord":[4,-1,-87],"labels":["risk"],"exits":[{"direction":"north","to":13605},{"direction":"west","to":13608},{"direction":"east","to":13610}]},
    {"vnum":13610,"name":"業獄前橋","description":"前橋橫跨在一段已被獄壓磨成冷黑鐵面的井腹上方，橋面每次受力都只留下一道極短的黯痕，下一瞬便像被更深處的業獄整片吞掉，不准任何重量停留太久。","sector_type":"SECT_INSIDE","cluster":"gehennal-threshold","coord":[5,-1,-87],"labels":["bridge"],"exits":[{"direction":"west","to":13609},{"direction":"south","to":13611}]},
    {"vnum":13611,"name":"冥獄井腹緣","description":"井腹緣圍著幾座朝內傾壓的封魄柱座，柱面殘紋已被磨成一圈圈近乎同心的黑痕，像這裡就是所有界層最後還能被壓出輪廓的地帶。","sector_type":"SECT_INSIDE","cluster":"gehennal-threshold","coord":[5,-2,-87],"labels":["threshold"],"exits":[{"direction":"north","to":13610},{"direction":"down","to":13612}],"enquires":["井腹","柱座"]},
    {"vnum":13612,"name":"裂魄冥獄座","description":"冥獄座像整段冥獄井腹最後一塊仍勉強聚得住輪廓的黑沉魄座，腳下環界只剩一圈隨時會再被壓薄一層的細窄獄紋，所有殘痕都在這裡被拖往更深的裂魄業獄。","sector_type":"SECT_INSIDE","cluster":"gehennal-threshold","coord":[5,-2,-88],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13611}],"enquires":["冥獄座","深處"]}
  ]
}
```
