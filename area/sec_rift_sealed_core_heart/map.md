# 封心核心 (`sec_rift_sealed_core_heart`)

## Area Intent

`sec_rift_sealed_core_heart` 承接封核沉盆最深的封核深井，下沉到真正束住裂核心跳的封心主體。此區定位為「心脈主井」：讓玩家在封心環脈、心壓偏廊與裂核前座之間感受到整個封印系統已逼近最後臨界，並為更深裂核心魄區預留正式連線。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `封心核心 / 心脈主井`
- LevelRange: `84-100`
- Parent area: `sec_rift_sealed_core_basin`
- ReservedRoomBlock: `10801-10820`

## Planned World Links

- `up` from `10801`: `sec_rift_sealed_core_basin` room `10712`
- `down` from `10812`: future deeper sealed-heart extension

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "sec_rift_sealed_core_heart",
    "title": "封心核心",
    "design_notes": "封核沉盆之下的封心主體，作為更深裂核心魄區前的主心脈節點。",
    "parent_area": "sec_rift_sealed_core_basin",
    "level_range": "84-100",
    "planned_vnum_range": "10801-10820",
    "reserved_room_block": "10801-10820",
    "room_vnum_policy": "xx01_variable_block",
    "theme": {
      "primary": "仙俠",
      "secondary": "封心核心 / 心脈主井"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 10801,
        "target_area": "sec_rift_sealed_core_basin",
        "target_room_vnum": 10712,
        "label": "封核深井"
      },
      {
        "direction": "down",
        "source_vnum": 10812,
        "target_area": "sec_rift_core_spirit_nadir",
        "label": "心魄深座"
      }
    ],
    "clusters": [
      { "id": "entry-well", "label": "深井落心" },
      { "id": "heart-ring", "label": "封心環脈" },
      { "id": "pressure-annex", "label": "心壓偏廊" },
      { "id": "core-threshold", "label": "裂核前座" }
    ]
  },
  "rooms": [
    {"vnum":10801,"name":"深井落心臺","description":"落心臺貼著深井最底的弧壁延展，腳下石面正隨著某種遙遠心跳微微顫動，彷彿整座封印主體就在壁後呼吸。","sector_type":"SECT_INSIDE","cluster":"entry-well","coord":[0,0,-32],"labels":["entry","world-link-up"],"exits":[{"direction":"up","to":10712,"external":true},{"direction":"east","to":10802}],"enquires":["退路","深井"]},
    {"vnum":10802,"name":"心壁踏脈","description":"踏脈沿著內壁向前延伸，牆面暗紅細脈不斷起伏，像有無形血流正從更深處往外一圈圈送壓。","sector_type":"SECT_INSIDE","cluster":"entry-well","coord":[1,0,-32],"labels":["mainline"],"exits":[{"direction":"west","to":10801},{"direction":"east","to":10803}]},
    {"vnum":10803,"name":"封心環脈前緣","description":"前緣俯視整圈封心環脈，環壁上流動的赤光忽聚忽散，像整座核心正在用最後秩序維持脈衝平衡。","sector_type":"SECT_INSIDE","cluster":"heart-ring","coord":[2,0,-32],"labels":["mainline"],"exits":[{"direction":"west","to":10802},{"direction":"east","to":10804},{"direction":"south","to":10807}]},
    {"vnum":10804,"name":"鎮脈觀心座","description":"觀心座旁立著數面向內傾斜的鎮脈鏡碑，碑面映不出人影，只映得出一陣陣來自心核深處的赤黑波紋。","sector_type":"SECT_INSIDE","cluster":"heart-ring","coord":[3,0,-32],"labels":["lore"],"exits":[{"direction":"west","to":10803},{"direction":"east","to":10805}],"enquires":["鎮脈","鏡碑"]},
    {"vnum":10805,"name":"心壓分脈池","description":"分脈池將整道心壓分流成幾股緩慢旋轉的暗潮，表面看似平穩，底下卻不時傳來短促而尖銳的爆裂聲。","sector_type":"SECT_INSIDE","cluster":"heart-ring","coord":[4,0,-32],"labels":["pressure"],"exits":[{"direction":"west","to":10804},{"direction":"east","to":10806},{"direction":"south","to":10809}],"keywords":[{"keyword":"分脈","description":"分脈池內壁佈滿層層補封刻痕，深淺不一，像歷代鎮封者都只來得及補住最急的一次脈衝。"}]},
    {"vnum":10806,"name":"封心聽脈座","description":"聽脈座中央豎著一支細長心柱，柱體每隔片刻就發出低沉重震，像更深處有真正的核心正以極慢節奏搏動。","sector_type":"SECT_INSIDE","cluster":"heart-ring","coord":[5,0,-32],"labels":["signal"],"exits":[{"direction":"west","to":10805}]},
    {"vnum":10807,"name":"心壓側階","description":"側階通向偏廊時逐漸下沉，石階邊緣沾滿濃黑封泥，踩上去會留下像被心脈吞吐過的濕冷光印。","sector_type":"SECT_INSIDE","cluster":"pressure-annex","coord":[2,-1,-32],"labels":["annex"],"exits":[{"direction":"north","to":10803},{"direction":"east","to":10808}]},
    {"vnum":10808,"name":"維心偏廊","description":"偏廊兩側嵌滿失效維心片，碎片仍在陰影中緩慢起亮，像最後一層人工秩序正試圖把心壓留在可控範圍。","sector_type":"SECT_INSIDE","cluster":"pressure-annex","coord":[3,-1,-32],"labels":["service"],"exits":[{"direction":"west","to":10807},{"direction":"east","to":10809}],"enquires":["維心","偏廊"]},
    {"vnum":10809,"name":"裂脈逆廊","description":"逆廊中央裂開一道細長脈縫，縫裡不時往外噴出灼亮氣流，把整條走道照得像一截正在發燒的血管。","sector_type":"SECT_INSIDE","cluster":"pressure-annex","coord":[4,-1,-32],"labels":["risk"],"exits":[{"direction":"north","to":10805},{"direction":"west","to":10808},{"direction":"east","to":10810}]},
    {"vnum":10810,"name":"裂核前橋","description":"前橋橫跨心脈最深的一道裂壓溝，橋下傳來規律而沉重的轟鳴，像更深的某個核心正反覆撞擊封底。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[5,-1,-32],"labels":["bridge"],"exits":[{"direction":"west","to":10809},{"direction":"south","to":10811}]},
    {"vnum":10811,"name":"心座井緣","description":"井緣外圍著一圈向內傾倒的心座封柱，柱面殘光一路往井下滑落，像在替更深處指示最後的下降路徑。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[5,-2,-32],"labels":["threshold"],"exits":[{"direction":"north","to":10810},{"direction":"down","to":10812}],"enquires":["心座","井緣"]},
    {"vnum":10812,"name":"封心深座","description":"深座像整條主井最後一塊立足的邊界，腳下只剩向內捲縮的黑紅光環，所有聲息都在這裡被拖往更深的心魄暗層。","sector_type":"SECT_INSIDE","cluster":"core-threshold","coord":[5,-2,-33],"labels":["world-link-down","boss-threshold"],"exits":[{"direction":"up","to":10811}],"enquires":["深座","核心"]}
  ]
}
```
