# Fort Naval Base Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_naval_base`。此區承接 `wild_pirate_islands` 東向暗棧，把玩家從無秩序的碎島海寇帶，重新推進到一段由哨柵、水軍棧門、軍需棚與望樓水寨構成的高壓軍事關卡，讓南境海路主線在外海 wild 之後，回到更有組織也更有壓迫感的 `Fort` 節奏。

## Theme Positioning

- theme: `軍旅`
- subtheme: `東吳水軍`
- experience_type: `Fort`
- player_loop_focus: `軍營辨位 / 關卡通行 / 棧門轉場 / 哨樓壓迫`
- contrast_with_previous_two:
  - 相對於 `dng_boat_graveyard` 的封閉沉舟與 `wild_pirate_islands` 的碎島野外，`fort_naval_base` 應讓玩家感受到秩序重新回來，但那不是港城式的煙火秩序，而是哨兵、軍令、柵門與水軍防線構成的高壓秩序
- 世界缺口角色：
  - 把 `wild_pirate_islands` 東向暗棧預留的海上勢力節點正式轉成可持續擴建的 spec-first `Fort`
  - 為後續 `city_jianye` 或更大的江東水軍鏈建立海上軍事前哨與交通 choke point
- reserved_room_block: `15901-15930`
- planned_vnum_range: `15901-15930`
- level_range: `100-100`
- external_links:
  - `west`: `wild_pirate_islands` / 東向暗棧
  - `north`: `city_jianye` / 建業水門預留
  - `south`: `sea_naval_patrol` / 外海巡防預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `外海水軍大營`
  - `東吳軍令與海防壓迫`
  - `海上 wild 之後的軍事關卡`
- 它補的玩家 loop：
  - `從碎島暗棧切進軍營關口`
  - `靠軍旗、柵門、補給棚與望樓辨認軍方地盤`
  - `為建業水門與更深巡防海域建立正式中繼`
- 它和前兩個已完成 area 的題材差異：
  - 不再是沉舟遺跡與深艙壓迫
  - 不再是碎島與海寇的半無序野外
  - 改用軍門、哨位與內營節奏把海路重新收束成 `Fort`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0074-fort-naval-base.md`
- 建立 `area/fort_naval_base/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `outer-pier`
  - `gate-line`
  - `supply-yard`
  - `watch-rise`
  - `inner-dock`
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_naval_base/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0073-wild-pirate-islands.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_naval_base/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0073-wild-pirate-islands.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_pirate_islands` 已把海路節奏重新打開成碎島 wild，適合在下一區收束成軍事 choke point，形成 `Wild -> Fort` 的節奏轉折
  - `fort_naval_base` scaffold 能直接支撐海門、軍旗、柵門與望樓語彙，讓海上主線不只剩海寇與遺跡，也開始出現正式政權力量
  - `world-graph` 把水軍大營放在江東水域鏈的軍事節點，適合作為之後銜接 `city_jianye` 的前哨
  - `players.json / skills.json` 沒有提供此時必須先切回秘境或另一個自由探索 wild 的強證據，因此先收成 `Fort` 更符合 queue variety
- `compliance_check`
  - compliant；在 `Wild` 之後切入 `Fort`，讓海路鏈維持 family 多樣性，也避免連續疊 `Wild` / `Secret`

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_naval_base/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_naval_base/map.md --validate-only`
  - passed for `10` room(s)
- `python -X utf8 tools/mapmd_validate.py area/wild_pirate_islands/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15812 <-> 15901`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_pirate_islands/map.md`
  - rewrote `roo/15801-15812` to include the `15812 east -> 15901 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_naval_base/map.md`
  - wrote `roo/15901-15912`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1040.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `fort_naval_base`，保留房號段 `15901-15930`
- `area/fort_naval_base/index` 已建立，`Serial 163`
- 第一輪 runtime scaffold 已加入：
  - `mob/17431-17434`
  - `obj/17451-17454`
  - `res/naval.res`
  - `shp/supplies.shp`
- `wild_pirate_islands/15812 <-> fort_naval_base/15901` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `fort_naval_base`

## Next Step Prompt

`先 commit 目前 fort_naval_base 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
