# City Nanpi Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_nanpi`。此區承接 `city_puyang` 北路預留，把河北前沿主線從濮陽正式推進到袁紹勢力範圍內的歷史城鎮，讓 `濮陽 -> 南皮 -> 河北平原 / 北道` 這條北線不再只剩抽象 graph，而是有清楚主街、城心與北向分流的 city 型 hub。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `河北城鎮 / 袁紹勢力前帶`
- experience_type: `City`
- player_loop_focus: `河北主線轉場 / 城內補給 / 問路分流 / 勢力氣氛`
- contrast_with_previous_two:
  - 相對於 `road_puyang` 的長路 connector 與 `city_puyang` 的前沿軍旅緊繃，`city_nanpi` 應把節奏轉成更有地方秩序、勢力色彩與北方城鎮煙火氣的河北主城，而不是再複製另一段純軍路。
- 世界缺口角色：
  - 把 `city_puyang/17209` 的北向預留正式轉成河北主線城市節點
  - 為後續 `wild_hebei_plain` 與 `road_nanpi_beiping` 建立新的北方城市分流 hub
- reserved_room_block: `17401-17420`
- planned_vnum_range: `17401-17420`
- level_range: `24-36`
- external_links:
  - `south`: `city_puyang` / 河北南路
  - `east`: `wild_hebei_plain` / 平原外道預留
  - `north`: `road_nanpi_beiping` / 河北北道預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_nanpi/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0087-city-puyang.md`
- `plans/area/0088-road-puyang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_nanpi/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0087-city-puyang.md`
  - `plans/area/0088-road-puyang.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/puyang.html`
  - `ref/sanguo-area-specfirst/area/wild_hebei_plain/map.md`
  - `ref/sanguo-area-specfirst/area/road_nanpi_beiping/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `city_nanpi` 放成 `city_puyang` 北側的城市 hub，並向 `wild_hebei_plain` 與 `road_nanpi_beiping` 分流
  - `題材分布表` 把南皮標成 `歷史 / 軍旅` 的河北城鎮，適合把玩法拉回帶地方勢力感的北方主城
  - `city_puyang` 已保留 `17209 north -> city_nanpi`，支持現在補齊河北主線的下一座城市節點
  - `players.json / skills.json` 沒有要求在 `road_puyang` 後立刻切入秘境或支洞，支持先把北線城市骨架補起來
- `compliance_check`
  - compliant；在 `Road` 之後切回 `City`，符合 queue variety，也直接承接 `city_puyang` 的既有北向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_nanpi/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_nanpi/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_nanpi/map.md`
  - passed (`Wrote 9 room scaffold file(s) to H:\repos\merc-fju-3.0\area\city_nanpi\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_puyang/map.md`
  - passed；同步把 `city_puyang/17209` 補成 `north -> 17401` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed；成功訊號寫入 `log/1061.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/19831-19834`、`obj/19851-19854`、`res/city.res`、`shp/supplies.shp`、`roo/17401-17409`
- 已正式落成 runtime boundary：`city_puyang/17209 <-> city_nanpi/17401`
- `east -> wild_hebei_plain` 與 `north -> road_nanpi_beiping` 仍維持 spec 預留，不在本輪 implementation scope
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `city_nanpi`

## Next Step Prompt

`先 commit 目前 city_nanpi 的 implementation milestone；commit 後依 queue 規則盤點下一個待建 area，建立新 spec 並在通過 validate-only 後直接前進。`
