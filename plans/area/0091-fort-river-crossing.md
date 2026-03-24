# Fort River Crossing Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_river_crossing`。此區承接 `wild_hebei_plain` 南向營道，把河北主線從開闊平原正式推進到渡河要地的軍事關卡，讓 `河北平原 -> 渡河營寨` 不再只是抽象 graph，而是有關前道、關門與內營層次的 fort 型節點。

## Theme Positioning

- theme: `軍旅`
- subtheme: `河渡要地`
- experience_type: `Fort`
- player_loop_focus: `營寨轉場 / 關卡辨位 / 軍令壓迫 / 河渡前帶`
- contrast_with_previous_two:
  - 相對於 `wild_hebei_plain` 的開闊風感與 `city_nanpi` 的城市秩序，`fort_river_crossing` 應把節奏重新收緊成軍令、關卡與渡河壓力，而不是繼續維持沒有邊界感的平原路帶。
- 世界缺口角色：
  - 把 `wild_hebei_plain/17508` 的南向預留正式轉成渡河營寨節點
  - 為後續更深層的河北軍事鏈建立清楚的 fort 骨架
- reserved_room_block: `17601-17620`
- planned_vnum_range: `17601-17620`
- level_range: `26-38`
- external_links:
  - `north`: `wild_hebei_plain` / 渡河營道口
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_river_crossing/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0090-wild-hebei-plain.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_river_crossing/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0090-wild-hebei-plain.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/road_nanpi_beiping/map.md`
  - `ref/sanguo-area-specfirst/area/sec_yellow_turban_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `fort_river_crossing` 放在 `wild_hebei_plain` 之後，作為河北平原主線上的 `fort` 節點
  - `題材分布表` 讓這段北地延續 `軍旅` 但從平原轉成關卡與渡河壓迫，題材切換清楚
  - `wild_hebei_plain` 已保留 `17508 south -> fort_river_crossing`，支持現在把南向營道收束成軍事 choke point
  - `players.json / skills.json` 沒有要求平原之後立刻回到服務型城市，支持先補軍事關卡節點
- `compliance_check`
  - compliant；在 `Wild` 之後切到 `Fort`，符合 queue variety，也直接承接 `wild_hebei_plain` 的既有南向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_river_crossing/map.md`
  - passed (`Validated 7 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_river_crossing/map.md --validate-only`
  - passed (`Validation succeeded for 7 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_river_crossing/map.md`
  - passed (`Wrote 7 room scaffold file(s) to H:\repos\merc-fju-3.0\area\fort_river_crossing\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_hebei_plain/map.md`
  - passed；同步把 `wild_hebei_plain/17508` 補成 `south -> 17601` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed；成功訊號寫入 `log/1063.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20031-20034`、`obj/20051-20054`、`res/fort.res`、`shp/supplies.shp`、`roo/17601-17607`
- 已正式落成 runtime boundary：`wild_hebei_plain/17508 <-> fort_river_crossing/17601`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `fort_river_crossing`

## Next Step Prompt

`先 commit 目前 fort_river_crossing 的 implementation milestone；commit 後依 queue 規則盤點下一個待建 area，建立新 spec 並在通過 validate-only 後直接前進。`
