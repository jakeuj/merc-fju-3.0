# Sec Water Ruins Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_water_ruins`。此區承接 `wild_pirate_islands` 外礁深灘下方的水府裂井，把玩家從外海群島的風浪與海寇痕跡正式帶進一段更稀有、更沉靜也更帶仙俠異象感的水底遺跡，作為江東海路線在群島 wild 之後的 secret 探索節點。

## Theme Positioning

- theme: `仙俠`
- subtheme: `水府遺跡 / 裂井殘宮`
- experience_type: `Secret`
- player_loop_focus: `深水下探 / 異象辨位 / 水府試探 / 高風險祕境`
- contrast_with_previous_two:
  - 相對於 `dng_temple_ruins` 的封閉古寺與 `wild_river_delta` 的開放外水，`sec_water_ruins` 應把節奏再收進更稀有、更靜壓的水底殘宮，讓江東鏈從外放水域切向高風險 secret。
- 世界缺口角色：
  - 把 `wild_pirate_islands/15810` 的 `down` 預留正式轉成可持續擴建的水底 secret
  - 為江東海路後段的水府、異象與更深水底支線建立第一個高風險祕境節點
- reserved_room_block: `16701-16730`
- planned_vnum_range: `16701-16730`
- level_range: `100-100`
- external_links:
  - `up`: `wild_pirate_islands` / 水府裂井
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0073-wild-pirate-islands.md`
- `plans/area/0081-wild-river-delta.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0073-wild-pirate-islands.md`
  - `plans/area/0081-wild-river-delta.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/wild_river_delta/map.md`
  - `ref/sanguo-area-specfirst/area/fort_naval_base/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `sec_water_ruins` 放在江東海路的 secret 節點，適合在 `Wild` 之後切進更高風險的水底祕境
  - `題材分布表` 為江東區保留 `仙俠` 補題空間，支持把外海與江汊探索延伸成更神祕的水府遺跡
  - `sec_water_ruins` scaffold 已提供 `異象核心 / 條件入口 / 獎勵區` 骨架，能直接轉成目前需要的裂井殘宮版本
  - `players.json / skills.json` 沒有要求這一段必須優先回到城市服務 loop，反而支持用高辨識度 secret 拉開和前段 wild 的體驗差
- `compliance_check`
  - compliant；在 `Wild` 之後切到 `Secret`，避免江東鏈連續堆疊水域 wild，也符合 queue variety

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/sec_water_ruins/map.md`
  - passed (`Validated 7 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_water_ruins/map.md --validate-only`
  - passed (`Validation succeeded for 7 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_water_ruins/map.md`
  - passed (`Wrote 7 room scaffold file(s) to area/sec_water_ruins/roo`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1053.log`
- `debug/badobject`
  - passed (empty after smoke test)

## Next Step Prompt

`先 commit 目前 sec_water_ruins 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立新的 spec milestone。`
