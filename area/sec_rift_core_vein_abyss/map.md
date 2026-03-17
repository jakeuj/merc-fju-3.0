# 裂核脈淵 (`sec_rift_core_vein_abyss`)

## Area Intent

`sec_rift_core_vein_abyss` 承接裂核深層最底端的渦核封檻臺，將探索重心帶入真正的脈淵層。此區定位為「高壓前帶」：讓玩家在倒灌裂潮、失衡脈環與沉陷鎮紋之間繼續下探，並為更深的禁底封脈區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `裂核脈淵 / 渦核深腹`
- LevelRange: `72-88`
- Parent area: `sec_rift_core_below_deeps`
- ReservedRoomBlock: `10501-10520`

## Planned World Links

- `up` from `10501`: `sec_rift_core_below_deeps` room `10412`
- `down` from `10512`: future deeper underseal basin extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_core_vein_abyss",
    "title": "裂核脈淵",
    "design_notes": "裂核深層之下的渦核脈淵，作為更深禁底封脈區前的高壓前帶。",
    "parent_area": "sec_rift_core_below_deeps",
    "level_range": "72-88",
    "planned_vnum_range": "10501-10520",
    "reserved_room_block": "10501-10520",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "裂核脈淵 / 渦核深腹"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10501,
        "target_area": "sec_rift_core_below_deeps",
        "target_room_vnum": 10412,
        "label": "渦核封檻臺"
      },
      {
        "direction": "down",
        "source_vnum": 10512,
        "target_area": "sec_rift_underseal_basin",
        "label": "禁底封脈"
      }
    ],
    "clusters": [
      { "id": "arrival-throat", "label": "落檻承脈" },
      { "id": "vein-ring", "label": "深腹環脈" },
      { "id": "backflow-court", "label": "倒灌裂庭" },
      { "id": "sundered-seal", "label": "沉紋斷口" }
    ]
  },
  "rooms": [
    {"vnum":10501,"name":"落檻承脈臺","description":"承脈臺懸在翻湧脈淵邊緣，頭頂僅剩一道遙遠紅痕，提醒來處已升成幾乎不可回望的高臺。","sector_type":"SECT_INSIDE","cluster":"arrival-throat","coord":[0,0,-26],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10412,"external":true},{"direction":"east","to":10502}],"enquires":["退路","脈淵"]},
    {"vnum":10502,"name":"環脈踏梁","description":"踏梁沿著深腹外圈延展，石面滿是被脈潮反覆沖刷後留下的光滑凹槽，踩上去像踏在溫熱獸骨上。","sector_type":"SECT_INSIDE","cluster":"arrival-throat","coord":[1,0,-26],"labels":["mainline"],"exits":[{"direction":"west","to":10501},{"direction":"east","to":10503}]},
    {"vnum":10503,"name":"淵環前帶","description":"前帶半包圍著一處巨大脈坑，坑底有無數紅黑細線來回交錯，彷彿整個空間都在緩慢搏動。","sector_type":"SECT_INSIDE","cluster":"vein-ring","coord":[2,0,-26],"labels":["mainline"],"exits":[{"direction":"west","to":10502},{"direction":"east","to":10504},{"direction":"south","to":10507}]},
    {"vnum":10504,"name":"倒灌觀井","description":"觀井旁的鎮桿已被脈潮磨成傾斜姿態，下方潮流卻仍不時反捲而上，像在試探整條承脈路徑的裂口。","sector_type":"SECT_INSIDE","cluster":"vein-ring","coord":[3,0,-26],"labels":["lore"],"exits":[{"direction":"west","to":10503},{"direction":"east","to":10505}],"enquires":["倒灌","鎮桿"]},
    {"vnum":10505,"name":"渦腹節環","description":"數層節環套在主脈外圈，環面裂紋此起彼伏，偶爾會有赤光沿裂痕疾走，把整圈照成森冷血色。","sector_type":"SECT_INSIDE","cluster":"vein-ring","coord":[4,0,-26],"labels":["pressure"],"exits":[{"direction":"west","to":10504},{"direction":"east","to":10506},{"direction":"south","to":10509}],"keywords":[{"keyword":"節環","description":"節環內側刻著多代修補者留下的警示，最近一層刻痕已經被脈液熔成模糊碎線。"}]},
    {"vnum":10506,"name":"脈裂聽臺","description":"聽臺邊緣裝著殘缺的聽脈銅盤，盤面會隨下層共鳴微微顫鳴，像在替更深處的巨大心跳數拍。","sector_type":"SECT_INSIDE","cluster":"vein-ring","coord":[5,0,-26],"labels":["signal"],"exits":[{"direction":"west","to":10505}]},
    {"vnum":10507,"name":"裂庭斷階","description":"斷階一路沒入半淹的側庭，地上殘留大片焦黑拖痕，像有沉重器具曾被匆忙拖往更深處。","sector_type":"SECT_INSIDE","cluster":"backflow-court","coord":[2,-1,-26],"labels":["annex"],"exits":[{"direction":"north","to":10503},{"direction":"east","to":10508}]},
    {"vnum":10508,"name":"逆潮沉庭","description":"沉庭中央的脈槽持續逆流，把碎石與鎮紋殘片一層層捲回高處，再任其無力墜落。","sector_type":"SECT_INSIDE","cluster":"backflow-court","coord":[3,-1,-26],"labels":["risk"],"exits":[{"direction":"west","to":10507},{"direction":"east","to":10509}],"enquires":["逆潮","殘片"]},
    {"vnum":10509,"name":"沉紋旁廊","description":"旁廊牆面鑲著沉陷的封紋板，板縫仍有細碎光絲流竄，顯示這裡的鎮壓系統只是勉強維持。","sector_type":"SECT_INSIDE","cluster":"sundered-seal","coord":[4,-1,-26],"labels":["service"],"exits":[{"direction":"north","to":10505},{"direction":"west","to":10508},{"direction":"east","to":10510}]},
    {"vnum":10510,"name":"裂痕封橋","description":"封橋跨在一道巨大裂痕上方，下方黑潮翻動時會把橋面照出忽明忽暗的赤色紋路。","sector_type":"SECT_INSIDE","cluster":"sundered-seal","coord":[5,-1,-26],"labels":["bridge"],"exits":[{"direction":"west","to":10509},{"direction":"south","to":10511}]},
    {"vnum":10511,"name":"沉界井緣","description":"井緣外只剩半圈護欄，護欄末端垂著斷裂鎮鏈，鏈上殘存的封印片正隨氣流輕輕碰撞。","sector_type":"SECT_INSIDE","cluster":"sundered-seal","coord":[5,-2,-26],"labels":["threshold"],"exits":[{"direction":"north","to":10510},{"direction":"down","to":10512}],"enquires":["鎮鏈","井口"]},
    {"vnum":10512,"name":"脈淵沉檻","description":"沉檻下方已看不見實體地面，只見整片黑紅脈潮沿裂縫向更深處旋落，像要把所有聲息都吞進禁底封脈。","sector_type":"SECT_INSIDE","cluster":"sundered-seal","coord":[5,-2,-27],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10511}],"enquires":["深口","封脈"]}
  ]
}
```
