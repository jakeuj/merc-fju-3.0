# Wild Hebei Plain Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_hebei_plain`。此區承接 `city_nanpi` 東向平原口，把河北主線從城市秩序正式推開成開闊野外與官道風險帶，讓 `南皮 -> 河北平原 -> 渡河營寨` 不再只是抽象 graph，而是一段可辨位、可探索、也能承接北地風感的 wild 型區域。

## Theme Positioning

- theme: `軍旅`
- subtheme: `平原 / 官道`
- experience_type: `Wild`
- player_loop_focus: `平原探索 / 官道轉場 / 地標辨位 / 北地主線外帶`
- contrast_with_previous_two:
  - 相對於 `city_nanpi` 的地方秩序與 `road_puyang` 的長路 connector，`wild_hebei_plain` 應把節奏重新打開成有風感、有視野、也更不受城牆約束的北地野外，而不是繼續留在牌樓與坊市節奏裡。
- 世界缺口角色：
  - 把 `city_nanpi/17408` 的東向預留正式轉成河北平原 wild 節點
  - 為後續 `fort_river_crossing` 建立南向官道與野外過渡骨架
- reserved_room_block: `17501-17520`
- planned_vnum_range: `17501-17520`
- level_range: `24-36`
- external_links:
  - `west`: `city_nanpi` / 東向平原口
  - `south`: `fort_river_crossing` / 渡河營寨預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_hebei_plain/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0089-city-nanpi.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_hebei_plain/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0089-city-nanpi.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/fort_river_crossing/map.md`
  - `ref/sanguo-area-specfirst/area/road_nanpi_beiping/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `wild_hebei_plain` 放成 `city_nanpi` 之後的 `wild` 節點，並向 `fort_river_crossing` 延伸
  - `題材分布表` 讓這段北地維持 `軍旅 / 平原` 的主題，適合把城市主線鬆開成更開闊的野外轉場
  - `city_nanpi` 已保留 `17408 east -> wild_hebei_plain`，支持現在接續東向平原外帶
  - `players.json / skills.json` 沒有要求南皮之後立刻回到另一座城市 hub，支持先把野外骨架補齊
- `compliance_check`
  - compliant；在 `City` 之後切到 `Wild`，符合 queue variety，也直接承接 `city_nanpi` 的既有東向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_hebei_plain/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_hebei_plain/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_hebei_plain/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\wild_hebei_plain\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_nanpi/map.md`
  - passed；同步把 `city_nanpi/17408` 補成 `east -> 17501` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed；成功訊號寫入 `log/1062.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/19931-19934`、`obj/19951-19954`、`res/wild.res`、`shp/supplies.shp`、`roo/17501-17508`
- 已正式落成 runtime boundary：`city_nanpi/17408 <-> wild_hebei_plain/17501`
- `south -> fort_river_crossing` 仍維持 spec 預留，不在本輪 implementation scope
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_hebei_plain`

## Next Step Prompt

`先 commit 目前 wild_hebei_plain 的 implementation milestone；commit 後依 queue 規則盤點下一個待建 area，建立新 spec 並在通過 validate-only 後直接前進。`
