# 裂魄白界 (`sec_rift_spirit_core_white`)

## Area Intent

`sec_rift_spirit_core_white` 承接裂魄空白最深的裂魄空白座，再往下沉入裂魄白界與白界深井。此區定位為「白界深井」：讓玩家從白界落座、白界內庭與失名偏廊之間，感受到魄壓已從空白進一步洗成素白，並為更深裂魄素界區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄白界 / 白界深井`
- LevelRange: `95-98`
- Parent area: `sec_rift_spirit_core_blank`
- ReservedRoomBlock: `11701-11720`

## Planned World Links

- `up` from `11701`: `sec_rift_spirit_core_blank` room `11612`
- `down` from `11712`: future deeper spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_white",
    "title": "裂魄白界",
    "design_notes": "裂魄空白之下的白界深井，作為更深素界層區前的過渡主段。",
    "parent_area": "sec_rift_spirit_core_blank",
    "level_range": "95-98",
    "planned_vnum_range": "11701-11720",
    "reserved_room_block": "11701-11720",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄白界 / 白界深井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 11701,
        "target_area": "sec_rift_spirit_core_blank",
        "target_room_vnum": 11612,
        "label": "裂魄空白座"
      },
      {
        "direction": "down",
        "source_vnum": 11712,
        "target_area": "sec_rift_spirit_core_plain",
        "label": "裂魄素界"
      }
    ],
    "clusters": [
      { "id": "white-shelf", "label": "白界落座" },
      { "id": "white-court", "label": "白界內庭" },
      { "id": "nameless-annex", "label": "失名偏廊" },
      { "id": "plain-threshold", "label": "素界前座" }
    ]
  },
  "rooms": [
    {"vnum":11701,"name":"白界落座","description":"落座像嵌在白界邊緣的一截素白石影，腳下殘留的環界已被洗到幾乎不再像界面，只剩一種比空白更薄、更冷的存在感，像連最後那點灰意都在此被拂盡。","sector_type":"SECT_INSIDE","cluster":"white-shelf","coord":[0,0,-50],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":11612,"external":true},{"direction":"east","to":11702}],"enquires":["白界","退路"]},
    {"vnum":11702,"name":"素白下階","description":"下階表面平整得沒有半點紋理可循，連白色也像被拉得過度稀薄，只剩一層勉強承住腳步的冷白薄殼，讓人不確定自己是否真站在階上。","sector_type":"SECT_INSIDE","cluster":"white-shelf","coord":[1,0,-50],"labels":["mainline"],"exits":[{"direction":"west","to":11701},{"direction":"east","to":11703}]},
    {"vnum":11703,"name":"白界內庭前緣","description":"前緣俯瞰整座向內沉落的白界內庭，庭底像一潭被洗去名字的素白空井，沒有光影可供對照，只剩視線一靠近就會被慢慢磨平的靜冷。","sector_type":"SECT_INSIDE","cluster":"white-court","coord":[2,0,-50],"labels":["mainline"],"exits":[{"direction":"west","to":11702},{"direction":"east","to":11704},{"direction":"south","to":11707}]},
    {"vnum":11704,"name":"觀素鎮魄臺","description":"鎮魄臺旁立著一座幾乎與周圍融成一體的觀素碑，碑面只剩少數往中心內收的白痕，像所有曾能辨識層次的記號都在這裡被洗成同一種素白。","sector_type":"SECT_INSIDE","cluster":"white-court","coord":[3,0,-50],"labels":["lore"],"exits":[{"direction":"west","to":11703},{"direction":"east","to":11705}],"enquires":["觀素","鎮魄"]},
    {"vnum":11705,"name":"白界斷層槽","description":"斷層槽裡沒有水聲、沒有風聲，只有一道極淡的白線筆直朝更深處下沉，像整段深井正在把所有殘留層理直接洗成更無名的素白底色。","sector_type":"SECT_INSIDE","cluster":"white-court","coord":[4,0,-50],"labels":["pressure"],"exits":[{"direction":"west","to":11704},{"direction":"east","to":11706},{"direction":"south","to":11709}],"keywords":[{"keyword":"斷層","description":"槽壁封紋比空白層更少，留下的只是一種把一切紋理直接漂洗掉的白冷意志。"}]},
    {"vnum":11706,"name":"聽素沉座","description":"沉座中央懸著一枚邊界幾乎完全融掉的素白長晶，晶體沒有發光，卻把周圍所有可供辨識的層次一點點磨成同色薄白，只留下空得發冷的鎮壓感。","sector_type":"SECT_INSIDE","cluster":"white-court","coord":[5,0,-50],"labels":["signal"],"exits":[{"direction":"west","to":11705}]},
    {"vnum":11707,"name":"失名側階","description":"側階斜切進偏廊時，連腳下踏過的感覺都像被擦去，只剩一道道素白殘痕在你身後迅速淡掉，讓人懷疑自己的名字是否也正被白界一併洗薄。","sector_type":"SECT_INSIDE","cluster":"nameless-annex","coord":[2,-1,-50],"labels":["annex"],"exits":[{"direction":"north","to":11703},{"direction":"east","to":11708}]},
    {"vnum":11708,"name":"失名偏廊","description":"偏廊兩側嵌著成排幾乎看不出接縫的導響殼片，殼面既無凹痕也無反光，只剩一種讓人一旦久留就會連自我稱述都慢慢失焦的素白錯覺。","sector_type":"SECT_INSIDE","cluster":"nameless-annex","coord":[3,-1,-50],"labels":["service"],"exits":[{"direction":"west","to":11707},{"direction":"east","to":11709}],"enquires":["失名","偏廊"]},
    {"vnum":11709,"name":"白界逆廊","description":"逆廊中央只剩一道細到近乎無法分辨的白縫，縫底沒有陰影，卻像能把所有尺度與名字一併拖進更深的素界井腹，讓人越看越抓不住仍屬於自己的部分。","sector_type":"SECT_INSIDE","cluster":"nameless-annex","coord":[4,-1,-50],"labels":["risk"],"exits":[{"direction":"north","to":11705},{"direction":"west","to":11708},{"direction":"east","to":11710}]},
    {"vnum":11710,"name":"素界前橋","description":"前橋橫跨在一段像被漂洗到無從命名的白腹上方，橋面每次受力後都只留下極短暫的冷白回音，下一瞬便像連那次踏步也不曾存在。","sector_type":"SECT_INSIDE","cluster":"plain-threshold","coord":[5,-1,-50],"labels":["bridge"],"exits":[{"direction":"west","to":11709},{"direction":"south","to":11711}]},
    {"vnum":11711,"name":"白界井緣","description":"井緣圍著幾座向內傾斜的封魄柱座，柱面殘紋已被洗到只剩幾道不穩的白線，像這裡就是所有界面最後還能勉強維持層次的地方。","sector_type":"SECT_INSIDE","cluster":"plain-threshold","coord":[5,-2,-50],"labels":["threshold"],"exits":[{"direction":"north","to":11710},{"direction":"down","to":11712}],"enquires":["井緣","柱座"]},
    {"vnum":11712,"name":"裂魄白界座","description":"白界座像整段白界深井最後一塊仍勉強保有輪廓的素白石影，腳下只剩一圈幾乎與周圍融成同色的環界，所有殘痕都在這裡被拖往更深的裂魄素界。","sector_type":"SECT_INSIDE","cluster":"plain-threshold","coord":[5,-2,-51],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":11711}],"enquires":["白界座","深處"]}
  ]
}
```
