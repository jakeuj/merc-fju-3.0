# Road Nanpi Beiping Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_nanpi_beiping`。此區承接 `city_nanpi` 北道牌樓，把河北主線從地方主城正式送上往北平的長路官道，讓 `南皮 -> 河北北道 -> 北平` 不再只是抽象 world link，而是一段可辨位、可問路、也能承接北地旅訊流動的 road 型過渡區。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `往北平官道`
- experience_type: `Road`
- player_loop_focus: `北地轉場 / 問路歇腳 / 驛訊流動 / 北行延伸`
- contrast_with_previous_two:
  - 相對於 `fort_river_crossing` 的軍事壓迫與 `wild_hebei_plain` 的開闊平原，`road_nanpi_beiping` 應把節奏收回成更有旅途與官道秩序感的長路 connector，而不是繼續維持關卡或野外壓力。
- 世界缺口角色：
  - 把 `city_nanpi/17409` 的北向預留正式轉成河北北道節點
  - 為後續 `city_beiping` 建立清楚的北行官道骨架
- reserved_room_block: `17701-17720`
- planned_vnum_range: `17701-17720`
- level_range: `24-36`
- external_links:
  - `south`: `city_nanpi` / 北道牌樓
  - `north`: `city_beiping` / 北平方向預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_nanpi_beiping/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0089-city-nanpi.md`
- `plans/area/0091-fort-river-crossing.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_nanpi_beiping/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0089-city-nanpi.md`
  - `plans/area/0091-fort-river-crossing.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/city_beiping/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `road_nanpi_beiping` 放成 `city_nanpi` 北側的 `road` 節點，並以 `city_beiping` 作為北向目標
  - `題材分布表` 與 `road_nanpi_beiping` 參考 spec 都支持把這段做成北地驛路與官道節點，而不是另一塊平原或營寨
  - `city_nanpi` 已保留 `17409 north -> road_nanpi_beiping`，支持現在把河北北路正式展開
  - `players.json / skills.json` 沒有對河北北段提出更強的秘境或服務點要求，支持先補交通骨架
- `compliance_check`
  - compliant；在 `Fort` 之後切到 `Road`，符合 queue variety，也不是直接沿最新完成 area 的預留硬往下接

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_nanpi_beiping/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_nanpi_beiping/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Next Step Prompt

`先 commit 目前 road_nanpi_beiping 的 spec milestone；commit 後直接進 implementation，補齊對 city_nanpi 的 runtime boundary、生成 roo 與最小 area runtime scaffold。`
