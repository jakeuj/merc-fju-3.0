# City Xiangping Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_xiangping`。此區承接 `wild_barbarian_camp` 的東向城路，把北境主線從邊地 hostile wild 重新收束進一座真正帶補給、訓練、技藝與驛站服務密度的遼東邊城 hub，讓 `白狼山 -> 胡營舊地 -> 襄平` 這條線第一次完整落成「野外壓力 -> 城市回補 -> 再往北分流」的節奏。

## Theme Positioning

- theme: `軍旅`
- subtheme: `遼東邊城 / 驛站與服務樞紐`
- experience_type: `City`
- player_loop_focus: `邊城整補 / 問路分流 / 訓練教導 / 北路轉場`
- contrast_with_previous_two:
  - 相對於 `dng_ancient_cave` 的地下封閉壓力與 `wild_barbarian_camp` 的舊營敵蹤感，`city_xiangping` 應把節奏重新收回有人煙、有規矩、也有實際服務收益的邊城秩序，而不是再延續另一段純軍野或秘境壓力。
- 世界缺口角色：
  - 把 `wild_barbarian_camp/18208` 的東向預留正式轉成遼東邊城 hub
  - 為後續 `wild_liaodong_plain` 與 `road_north_border` 建立新的北境城市分流母點
- reserved_room_block: `18301-18330`
- planned_vnum_range: `18301-18330`
- level_range: `34-46`
- external_links:
  - `west`: `wild_barbarian_camp` / 胡營舊地方向
  - `north`: `wild_liaodong_plain` / 遼東平原預留
  - `north`: `road_north_border` / 北境邊道預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_xiangping/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0097-wild-barbarian-camp.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_xiangping/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0097-wild-barbarian-camp.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/wild_liaodong_plain/map.md`
  - `ref/sanguo-area-specfirst/area/road_north_border/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `city_xiangping` 放在 `wild_barbarian_camp` 之後，並向 `wild_liaodong_plain` 與 `road_north_border` 繼續分流，是北境主線自然的城市回補節點
  - `world_map` 直接把 `濮陽 - 南皮 - 北平 - 襄平` 放進北線主幹，並點出 `襄平驛站`，支持此區作為交通與服務樞紐
  - `players.json / skills.json` 對 `襄平` 提出明確服務訊號：`倫直` 的 `refresh`、`玉霖大師` 的訓練，以及藥材行老闆的 `venom`，支持此區優先補成可承接玩家 loop 的城市 hub
  - `wild_barbarian_camp` runtime 已把 `18208 east` 明確保留給襄平，現在補城市 spec 可以讓下一輪 implementation 直接延續，不再重做 queue 判斷
- `compliance_check`
  - compliant；在 `Wild` 之後切回 `City`，同時回應舊站服務鏈、交通節點與 queue variety，且不會把邊城 hub 再往後拖成純 metadata

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_xiangping/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangping/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)

## Runtime Notes

- pending

## Next Step Prompt

`先 commit 目前 city_xiangping 的 spec milestone；commit 後直接做 implementation milestone：生成 roo、補最小 index / mob / obj / res / shp、正式接上 wild_barbarian_camp/18208 <-> city_xiangping/18301 runtime boundary，並把北向雙分流保留為後續遼東節點的 spec 預留。`
