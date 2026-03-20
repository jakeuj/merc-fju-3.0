# 裂魄業獄 (`sec_rift_spirit_core_gehennal`)

## Area Intent

`sec_rift_spirit_core_gehennal` 承接裂魄冥獄最深的裂魄冥獄座，再往下沉入裂魄業獄與業獄井腹。此區定位為「業獄井腹」：讓玩家從業獄落座、業獄內庭與業冥偏廊之間，感受到魄壓已從冥獄再被碾成近乎只剩罪痕輪廓的冷硬界面，並為後續同級更硬的裂魄寒獄層預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂魄業獄 / 業獄井腹`
- LevelRange: `100-100`
- Parent area: `sec_rift_spirit_core_infernal`
- ReservedRoomBlock: `13701-13720`

## Planned World Links

- `up` from `13701`: `sec_rift_spirit_core_infernal` room `13612`
- `down` from `13712`: future same-cap plateau spirit-core extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_spirit_core_gehennal",
    "title": "裂魄業獄",
    "design_notes": "裂魄冥獄之下的業獄井腹，作為後續同級 plateau 寒獄層區前的主段。",
    "parent_area": "sec_rift_spirit_core_infernal",
    "level_range": "100-100",
    "planned_vnum_range": "13701-13720",
    "reserved_room_block": "13701-13720",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂魄業獄 / 業獄井腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 13701,
        "target_area": "sec_rift_spirit_core_infernal",
        "target_room_vnum": 13612,
        "label": "裂魄冥獄座"
      },
      {
        "direction": "down",
        "source_vnum": 13712,
        "target_area": "sec_rift_spirit_core_cocytal",
        "label": "裂魄寒獄"
      }
    ],
    "clusters": [
      { "id": "gehennal-shelf", "label": "業獄落座" },
      { "id": "gehennal-court", "label": "業獄內庭" },
      { "id": "cocytal-annex", "label": "業冥偏廊" },
      { "id": "cocytal-threshold", "label": "寒獄前座" }
    ]
  },
  "rooms": [
    {"vnum":13701,"name":"業獄落座","description":"落座像嵌在業獄外緣的一截罪魄黑石，腳下環界已被壓得像一張隨時會裂卻又始終不斷的薄板，只剩幾道細窄罪痕貼在座沿，像把最後能回望冥獄的餘光也逐層封死。","sector_type":"SECT_INSIDE","cluster":"gehennal-shelf","coord":[0,0,-88],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":13612,"external":true},{"direction":"east","to":13702}],"enquires":["業獄","退路"]},
    {"vnum":13702,"name":"罪紋沉階","description":"沉階表面覆著一層層向內收束的罪紋，每踏下一階，都像踩進一塊帶著舊業回響的黑沉鐵面，連原本該散去的腳步聲也會被壓成更鈍的低鳴。","sector_type":"SECT_INSIDE","cluster":"gehennal-shelf","coord":[1,0,-88],"labels":["mainline"],"exits":[{"direction":"west","to":13701},{"direction":"east","to":13703}]},
    {"vnum":13703,"name":"業獄內庭前緣","description":"前緣俯瞰整座向內下沉的業獄內庭，庭心像一口專門磨蝕罪痕的無火重井，視線停久了，連腦中剛冒出的念頭都像會被壓成一枚枚再也分不清來處的黑印。","sector_type":"SECT_INSIDE","cluster":"gehennal-court","coord":[2,0,-88],"labels":["mainline"],"exits":[{"direction":"west","to":13702},{"direction":"east","to":13704},{"direction":"south","to":13707}]},
    {"vnum":13704,"name":"照業鎮魄臺","description":"鎮魄臺旁的照業碑只剩幾道被長年獄壓磨亮的罪槽，碑與界在此幾乎只靠最後一層鎮束法意硬撐，像再往下沉一步，就會整片崩入更深的寒獄。","sector_type":"SECT_INSIDE","cluster":"gehennal-court","coord":[3,0,-88],"labels":["lore"],"exits":[{"direction":"west","to":13703},{"direction":"east","to":13705}],"enquires":["照業","鎮魄"]},
    {"vnum":13705,"name":"業獄沉黯槽","description":"沉黯槽裡看不見任何流勢，只剩一道被業壓反覆擠窄的黑線沿槽底朝更深處收束，像整段井腹正在把所有還帶因果的殘痕一筆筆磨回冷黑底色。","sector_type":"SECT_INSIDE","cluster":"gehennal-court","coord":[4,0,-88],"labels":["pressure"],"exits":[{"direction":"west","to":13704},{"direction":"east","to":13706},{"direction":"south","to":13709}],"keywords":[{"keyword":"沉黯","description":"槽壁罪紋已被業壓磨成難再分辨的黑層，只留下把界面持續逼向更深寒獄的靜重壓力。"}]},
    {"vnum":13706,"name":"照業沉座","description":"沉座中央懸著一枚像被整口業獄反覆碾薄的黯晶，晶體不發光，只默默把周圍還能分層的輪廓磨成更平、更冷的重暗面。","sector_type":"SECT_INSIDE","cluster":"gehennal-court","coord":[5,0,-88],"labels":["signal"],"exits":[{"direction":"west","to":13705}]},
    {"vnum":13707,"name":"業冥側階","description":"側階斜切進偏廊時，腳下每一級都像被更深層業壓提前鎖死，回頭再看，剛踩過的紋路已收成一束束發黑細線，像不願再為來人留下任何折返餘地。","sector_type":"SECT_INSIDE","cluster":"cocytal-annex","coord":[2,-1,-88],"labels":["annex"],"exits":[{"direction":"north","to":13703},{"direction":"east","to":13708}]},
    {"vnum":13708,"name":"業冥偏廊","description":"偏廊兩側嵌著一列列被壓平到幾乎失去弧度的導響殼片，殼面不再回應完整聲響，只會把人的念頭敲成短促、沉重的暗鳴，最後全數壓回井腹底層。","sector_type":"SECT_INSIDE","cluster":"cocytal-annex","coord":[3,-1,-88],"labels":["service"],"exits":[{"direction":"west","to":13707},{"direction":"east","to":13709}],"enquires":["業冥","偏廊"]},
    {"vnum":13709,"name":"業獄逆腹廊","description":"逆腹廊中央橫著一道只有斜眼才看得出層差的罪裂，裂底既沒有火光也沒有回聲，卻像能把最後還保得住形名的碎片慢慢拖往更深的寒獄井腹。","sector_type":"SECT_INSIDE","cluster":"cocytal-annex","coord":[4,-1,-88],"labels":["risk"],"exits":[{"direction":"north","to":13705},{"direction":"west","to":13708},{"direction":"east","to":13710}]},
    {"vnum":13710,"name":"寒獄前橋","description":"前橋橫跨在一段已被業壓磨成冷黑鏡面的井腹上方，橋面每次受力都只留下極短的一道寒痕，下一瞬便像被更深處的寒獄整片吞沒，不准任何重量停留太久。","sector_type":"SECT_INSIDE","cluster":"cocytal-threshold","coord":[5,-1,-88],"labels":["bridge"],"exits":[{"direction":"west","to":13709},{"direction":"south","to":13711}]},
    {"vnum":13711,"name":"業獄井腹緣","description":"井腹緣圍著幾座朝內傾壓的封魄柱座，柱面殘紋已被磨成一圈圈幾乎同心的黑痕，像這裡就是所有界層最後還能被壓出輪廓的地帶。","sector_type":"SECT_INSIDE","cluster":"cocytal-threshold","coord":[5,-2,-88],"labels":["threshold"],"exits":[{"direction":"north","to":13710},{"direction":"down","to":13712}],"enquires":["井腹","柱座"]},
    {"vnum":13712,"name":"裂魄業獄座","description":"業獄座像整段業獄井腹最後一塊仍勉強聚得住輪廓的黑沉魄座，腳下環界只剩一圈隨時會再被壓薄一層的細窄罪紋，所有殘痕都在這裡被拖往更深的裂魄寒獄。","sector_type":"SECT_INSIDE","cluster":"cocytal-threshold","coord":[5,-2,-89],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":13711}],"enquires":["業獄座","深處"]}
  ]
}
```
