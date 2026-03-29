# Wild Wolf Forest Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_wolf_forest`。此區承接 `wild_bailang` 的北狼隘口，把北境山前前帶再往內推成更收束、更難辨位、也更帶狼群與失蹤傳聞壓力的林區 wild。這裡不應只是白狼山再多一段北路，而是一處會讓玩家明顯感到軍鎮與山脊秩序都已退到身後，只剩林路痕跡、石碑警語與狼群聲息接管方向感的前線深林節點。

## Theme Positioning

- theme: `詭異民俗`
- subtheme: `林區 / 狼群`
- experience_type: `Wild`
- player_loop_focus: `林路辨位 / 痕跡追查 / 邊地採集 / 狼群壓力`
- contrast_with_previous_two:
  - 相對於 `road_north_border` 的長路盤查感與 `fort_northern_watch` 的高處軍令秩序，`wild_wolf_forest` 應把體驗重新壓回近身、遮蔽與不確定性更高的深林 wild，而不是再做一段軍旅 road 或另一座高處 fort。
- 世界缺口角色：
  - 把 `wild_bailang/18008` 的北向預留正式轉成狼林節點
  - 為後續更深的北境 folklore / secret 區帶保留林中異象與失蹤傳聞骨架
- reserved_room_block: `18701-18720`
- planned_vnum_range: `18701-18720`
- level_range: `40-52`
- external_links:
  - `south`: `wild_bailang` / 北狼隘口
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_wolf_forest/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0095-wild-bailang.md`
- `plans/area/0100-road-north-border.md`
- `plans/area/0101-fort-northern-watch.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_wolf_forest/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0095-wild-bailang.md`
  - `plans/area/0100-road-north-border.md`
  - `plans/area/0101-fort-northern-watch.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/sec_spirit_peak/map.md`
  - `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_bailang` 現有 spec/runtime 已保留 `18008 north -> wild_wolf_forest` metadata，表示這裡是白狼山之後最自然的北向承接 wild
  - `world-graph` 明確把 `wild_wolf_forest` 定成 `Wild` family，支持在 `Fort` 之後切回更收束、更遮蔽的林地探索節奏
  - `題材分布表` 與 ref scaffold 都把此區拉向 `詭異民俗 / 狼群`，能和 `wild_bailang` 的山前異域、`fort_northern_watch` 的狼煙哨站形成清楚題材差
  - `players.json / skills.json` 對遼東北線的高頻訊號仍集中在襄平服務節點，支持在邊城與軍鎮補給已齊的前提下，把下一區做成非服務導向的深林壓力帶
- `compliance_check`
  - compliant；在 `Fort` 之後切回 `Wild`，同時承接 `wild_bailang` 的既有北向預留與北境 family variety，不是任意跳到無關城市或秘境

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_wolf_forest/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_wolf_forest/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_wolf_forest/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/wild_wolf_forest/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 60s ./startup.bash || true'`
  - passed startup smoke via `log/1074.log`; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_wolf_forest`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `18701-18708`、mob vnum `21131-21134`、obj vnum `21151-21154`
- 已正式落成 runtime boundary：`wild_bailang/18008 north -> wild_wolf_forest/18701` 與 `wild_wolf_forest/18701 south -> wild_bailang/18008`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_wolf_forest`
- smoke test 後 `debug/error` 僅反映 `timeout` 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `wild_wolf_forest` 相關 loader blocker

## Next Step Prompt

`先 commit wild_wolf_forest 的 implementation milestone：包含 wild_bailang/18008 <-> wild_wolf_forest/18701 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個北境節點。`
