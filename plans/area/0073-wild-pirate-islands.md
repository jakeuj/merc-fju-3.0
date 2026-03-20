# Wild Pirate Islands Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_pirate_islands`。此區承接 `dng_boat_graveyard` 更南側的破舷裂口，把玩家從封閉沉舟內部重新帶回更開闊但更無秩序的外海群島，讓南境海路主線在 wreck dungeon 之後，轉進一段由碎島、海寇舊寨與礁灣繞行構成的高風險海上 wild。

## Theme Positioning

- theme: `江湖`
- subtheme: `群島 / 海寇`
- experience_type: `Wild`
- player_loop_focus: `群島辨位 / 礁灣轉場 / 海寇痕跡 / 外海探路`
- contrast_with_previous_two:
  - 相對於 `wild_south_sea_route` 的近海棧道與 `dng_boat_graveyard` 的封閉沉艙，`wild_pirate_islands` 應讓玩家感受到視野再次打開，但秩序不再來自港城或殘舟，而是來自海寇棧橋、礁灣暗路與碎島之間勉強延續的生存規則
- 世界缺口角色：
  - 把 `dng_boat_graveyard` 南界預留的 `sea_outer_isles` 正式轉成可持續擴建的 spec-first 群島 wild
  - 為後續 `sec_water_ruins` 或更深外海祕境建立第一層外海落腳點
- reserved_room_block: `15801-15830`
- planned_vnum_range: `15801-15830`
- level_range: `100-100`
- external_links:
  - `north`: `dng_boat_graveyard` / 外海破舷
  - `down`: `sec_water_ruins` / 水府裂井預留
  - `east`: `fort_naval_base` / 海寇前哨預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `外海群島`
  - `海寇據點與碎島礁灣`
  - `wreck dungeon 之後重新打開的高風險 wild`
- 它補的玩家 loop：
  - `從沉舟深處切回外海辨位`
  - `靠礁標、破旗、棧橋與碎島高度判斷去路`
  - `為更深水府或海寇前哨建立前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是港城邊的近海水道
  - 不再是封閉沉舟與深艙壓迫
  - 改用碎島、海風與海寇殘留秩序把節奏轉回高風險 wild

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0073-wild-pirate-islands.md`
- 建立 `area/wild_pirate_islands/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `wreck-exit`
  - `reef-lane`
  - `pirate-cove`
  - `signal-ridge`
  - `outer-shoal`
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_pirate_islands/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0072-dng-boat-graveyard.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_pirate_islands/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0072-dng-boat-graveyard.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/fort_naval_base/map.md`
  - `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `dng_boat_graveyard` 已把海路節奏壓進 wreck dungeon，適合在下一區重新打開視野，形成 `Wild -> Dungeon -> Wild` 的回彈
  - `ref` scaffold 已提供 `wild_pirate_islands` 類型，能直接支撐碎島、海寇、暗灣與外海棧橋語彙
  - `world-graph` 支持群島之後再往更深水域或 ruins 推進，因此此區適合作為高風險但仍可辨位的外海落腳點
  - `players.json / skills.json` 沒有提供必須優先回到城市 hub 的服務鏈證據，因此先做群島 wild 更符合目前海路主線節奏
- `compliance_check`
  - compliant；在 `Dungeon` 之後切回 `Wild`，讓海路鏈維持 family 多樣性，也避免連續下探造成題材過度壓縮

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_pirate_islands/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_pirate_islands/map.md --validate-only`
  - passed for `11` room(s)
- `python -X utf8 tools/mapmd_validate.py area/dng_boat_graveyard/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15712 <-> 15801`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_boat_graveyard/map.md`
  - rewrote `roo/15701-15712` to include the `15712 south -> 15801 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_pirate_islands/map.md`
  - wrote `roo/15801-15812`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1039.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `wild_pirate_islands`，保留房號段 `15801-15830`
- `area/wild_pirate_islands/index` 已建立，`Serial 162`
- 第一輪 runtime scaffold 已加入：
  - `mob/17231-17234`
  - `obj/17251-17254`
  - `res/islands.res`
  - `shp/supplies.shp`
- `dng_boat_graveyard/15712 <-> wild_pirate_islands/15801` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `wild_pirate_islands`

## Next Step Prompt

`先 commit 目前 wild_pirate_islands 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
