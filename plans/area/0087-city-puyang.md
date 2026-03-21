# City Puyang Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_puyang`。此區承接目前 repo 已落地的 `wild_puyang_forest` 與 `dng_guandu_battlefield` 之間缺口，把濮陽正式補成河北前沿的軍旅主城，讓「林野前帶 -> 前沿補給城 -> 官渡戰場」這條已存在於世界圖與 ref scaffold 的節奏，第一次在 runtime 規劃層完整接起來。

## Theme Positioning

- theme: `軍旅`
- subtheme: `河北前沿 / 糧道與軍政中繼`
- experience_type: `City`
- player_loop_focus: `前線回補 / 糧道問路 / 軍務傳聞 / 戰地轉場`
- contrast_with_previous_two:
  - 相對於 `city_shouchun` 的淮南母城與 `wild_shouchun_fields` 的近郊田野，`city_puyang` 應刻意切回河北前沿的軍政壓力，讓 queue 在 `Wild` 之後回到一座帶戰事氣味的 frontier city，而不是繼續沿江東鏈重複另一個城郊 loop。
- 世界缺口角色：
  - 把先前已完成的 `wild_puyang_forest` 與 `dng_guandu_battlefield` 中間缺掉的濮陽主城補起來
  - 為後續 `city_nanpi` 與河北北路建立新的前沿城市樞紐
- reserved_room_block: `17201-17220`
- planned_vnum_range: `17201-17220`
- level_range: `20-32`
- external_links:
  - `west`: `wild_puyang_forest` / 濮陽林外路
  - `east`: `dng_guandu_battlefield` / 官渡糧道殘線
  - `south`: `road_puyang` / 南驛官道預留
  - `north`: `city_nanpi` / 河北北路預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_puyang/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/map/puyang.html`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0054-wild-puyang-forest.md`
- `plans/area/0055-dng-guandu-battlefield.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_puyang/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/map/puyang.html`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0054-wild-puyang-forest.md`
  - `plans/area/0055-dng-guandu-battlefield.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_nanpi/map.md`
  - `ref/sanguo-area-specfirst/area/wild_floodplain/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把濮陽放成兗州河北區的 `city` 節點，並與 `city_nanpi`、戰場 / 野外節點共同構成河北前沿主線
  - `wild_puyang_forest` 與 `dng_guandu_battlefield` 兩個已完成 area 都已把 `city_puyang` 當成相鄰目標，支持現在回補這座缺失中的前沿主城
  - `題材分布表` 把濮陽定位為軍旅城鎮，適合先落成糧道、市集、軍務與城門壓力都明確的邊地城市
  - `puyang.html` 舊站地圖證明濮陽確實具備獨立城市規模，而不是只能當抽象路點
  - `players.json / skills.json` 沒有提供必須優先續走江東或秘境鏈的強信號，支持回頭補齊已落地河北鏈的城市缺口
- `compliance_check`
  - compliant；queue 在 `Wild` 之後切回 `City`，同時補的是現有已建河北鏈的缺口，不是憑空開新支線

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_puyang/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_puyang/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_puyang/map.md`
  - passed (`Wrote 9 room scaffold file(s) to H:\repos\merc-fju-3.0\area\city_puyang\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_puyang_forest/map.md`
  - passed；同步把 `wild_puyang_forest/13906` 補成 `enter -> 17201` runtime boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_guandu_battlefield/map.md`
  - passed；同步把 `dng_guandu_battlefield/14007` 補成 `out -> 17208` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed；成功訊號寫入 `log/1058.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/19631-19634`、`obj/19651-19654`、`res/city.res`、`shp/supplies.shp`、`roo/17201-17209`
- 已正式落成兩個 runtime boundary：
  - `wild_puyang_forest/13906 <-> city_puyang/17201`
  - `dng_guandu_battlefield/14007 <-> city_puyang/17208`
- `south -> road_puyang` 與 `north -> city_nanpi` 仍維持 spec 預留，不在本輪 implementation scope
- `docs/current-game/areas.md`、`docs/current-game/areas.json` 與 `area/directory.lst` 已同步納入 `city_puyang`

## Next Step Prompt

`先 commit 目前 city_puyang 的 implementation milestone；commit 後依 queue 規則重建下一個 actionable area，建立新 spec 並在通過 validate-only 後直接前進。`
