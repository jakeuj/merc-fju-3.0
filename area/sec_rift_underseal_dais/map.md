# 鎮封底座 (`sec_rift_underseal_dais`)

## Area Intent

`sec_rift_underseal_dais` 承接 `sec_rift_prison_core` 封印井心下方，讓玩家正式踏入長年承受裂界反衝的鎮封底座。此區是進入裂界本核前的最後緩衝層：仍可辨識人工鎮封痕跡，但結構已接近極限。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `鎮封底座 / 反衝承壓層`
- LevelRange: `58-72`
- Parent area: `sec_rift_prison_core`
- ReservedRoomBlock: `10101-10120`

## Planned World Links

- `up` from `10101`: `sec_rift_prison_core` room `10012`
- `down` from `10112`: future `sec_rift_true_core`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_underseal_dais",
    "title": "鎮封底座",
    "design_notes": "封印核心下層，作為前往裂界本核前的承壓過渡層。",
    "parent_area": "sec_rift_prison_core",
    "level_range": "58-72",
    "planned_vnum_range": "10101-10120",
    "reserved_room_block": "10101-10120",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "鎮封底座 / 反衝承壓層"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10101,
        "target_area": "sec_rift_prison_core",
        "target_room_vnum": 10012,
        "label": "封印井心"
      },
      {
        "direction": "down",
        "source_vnum": 10112,
        "target_area": "sec_rift_true_core",
        "label": "本核縱井"
      }
    ],
    "clusters": [
      { "id": "entry-dais", "label": "井心落階" },
      { "id": "main-ring", "label": "鎮封主環" },
      { "id": "load-annex", "label": "承壓旁廊" },
      { "id": "core-threshold", "label": "本核前緣" }
    ]
  },
  "rooms": [
    {"vnum":10101,"name":"井心落階","description":"長階貼著井壁向下貼地，石面上覆著近乎金屬化的暗紅薄膜，像千百次反衝把整段落階硬生生燒成同一種質地。","sector_type":"SECT_INSIDE","cluster":"entry-dais","coord":[0,0,-18],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10012,"external":true},{"direction":"east","to":10102}],"enquires":["退路","井心"]},
    {"vnum":10102,"name":"鎮脈沉台","description":"沉台中央嵌著一圈低鳴石環，每次共振都會讓地面細微起伏，像整個底座其實是一具仍在呼吸的巨大鎮封器官。","sector_type":"SECT_INSIDE","cluster":"entry-dais","coord":[1,0,-18],"labels":["ring"],"exits":[{"direction":"west","to":10101},{"direction":"east","to":10103}]},
    {"vnum":10103,"name":"承壓前廊","description":"前廊兩側立著歪斜鎮柱，柱面刻痕被反衝磨到近乎發亮，僅剩少量符線還能辨識原先的封界序列。","sector_type":"SECT_INSIDE","cluster":"main-ring","coord":[2,0,-18],"labels":["mainline"],"exits":[{"direction":"west","to":10102},{"direction":"east","to":10104},{"direction":"south","to":10106}]},
    {"vnum":10104,"name":"底座主環","description":"主環沿著巨大空腔邊緣鋪展，腳下每一步都伴隨低頻震盪，像下方正有某種重量無法被完全鎮住。","sector_type":"SECT_INSIDE","cluster":"main-ring","coord":[3,0,-18],"labels":["ring","pressure"],"exits":[{"direction":"west","to":10103},{"direction":"east","to":10105}],"keywords":[{"keyword":"主環","description":"主環石槽內殘留灰白粉屑，是歷代補封材料在高壓下被反覆碾碎後留下的痕跡。"}]},
    {"vnum":10105,"name":"裂壓觀臺","description":"觀臺外緣佈滿斷裂護欄，向下望去只有翻湧黑紅霧流。這裡原本像是監測點，如今只剩讀不全的刻度與警示。","sector_type":"SECT_INSIDE","cluster":"main-ring","coord":[4,0,-18],"labels":["lore","danger"],"exits":[{"direction":"west","to":10104},{"direction":"south","to":10110}],"enquires":["反衝","下層"]},
    {"vnum":10106,"name":"卸壓側庭","description":"側庭牆面開了數個導流槽，槽口仍有細光竄動，顯示此處長年承擔把過量反衝暫時導離主環的工作。","sector_type":"SECT_INSIDE","cluster":"load-annex","coord":[2,-1,-18],"labels":["annex"],"exits":[{"direction":"north","to":10103},{"direction":"east","to":10107}],"enquires":["卸壓","封印"]},
    {"vnum":10107,"name":"導流石廊","description":"石廊地面刻著密集導紋，紋路交錯後全都朝更深處匯去，像是在把不該留在這層的躁動推向另一個容器。","sector_type":"SECT_INSIDE","cluster":"load-annex","coord":[3,-1,-18],"labels":["corridor"],"exits":[{"direction":"west","to":10106},{"direction":"east","to":10108}]},
    {"vnum":10108,"name":"鎖紋維護室","description":"維護室裡排列著殘破石架與碎裂器具，牆上還留著不同年代補紋記號，顯示守印者曾在這裡接力修補。","sector_type":"SECT_INSIDE","cluster":"load-annex","coord":[4,-1,-18],"labels":["supply","lore"],"exits":[{"direction":"west","to":10107},{"direction":"east","to":10109}],"keywords":[{"keyword":"補紋","description":"不同筆觸的補紋重疊在同一面牆上，像多代守印者都在同一處留下最後手記。"}]},
    {"vnum":10109,"name":"裂鳴祭點","description":"祭點中央的圓盤被燒出一圈圈深痕，周圍散落著無法辨識原形的器材殘片，空氣裡只剩刺耳鳴振。","sector_type":"SECT_INSIDE","cluster":"load-annex","coord":[5,-1,-18],"labels":["risk"],"exits":[{"direction":"west","to":10108}]},
    {"vnum":10110,"name":"鎮封臨界橋","description":"狹橋跨過一條垂直裂隙，橋下有明滅不定的紅黑脈流。橋面每隔數步都嵌著崩裂鎮釘，像只要少一枚就可能整段斷落。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[4,-2,-18],"labels":["bridge","threshold"],"exits":[{"direction":"north","to":10105},{"direction":"south","to":10111}]},
    {"vnum":10111,"name":"本核前井","description":"前井呈喇叭狀向下收束，井壁滿是被高熱反覆沖刷過的玻化層，深處不時傳來像心搏又像低吼的長脈振。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[4,-3,-18],"labels":["well"],"exits":[{"direction":"north","to":10110},{"direction":"down","to":10112}],"enquires":["本核","風險"]},
    {"vnum":10112,"name":"鎮封縱井","description":"縱井是底座最深的立足點，腳下只剩一圈勉強穩住的石台，中央黑紅光柱沿井軸直墜，像真正的裂界本核就在幾步之遙。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[4,-3,-19],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10111}],"enquires":["下層","本核"]}
  ]
}
```
