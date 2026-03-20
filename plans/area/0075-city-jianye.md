# City Jianye Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_jianye`。此區承接 `fort_naval_base` 北向建業水門，把玩家從海防軍營的高壓秩序，正式帶入江東都城的主街、市集、官署與港城節奏，讓南境海路鏈在 `Fort` 之後收束成真正的 `City` hub。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `江東都城`
- experience_type: `City`
- player_loop_focus: `主城補給 / 水門轉場 / 城市服務 / 江東中樞`
- contrast_with_previous_two:
  - 相對於 `wild_pirate_islands` 的碎島海寇帶與 `fort_naval_base` 的軍令壓力，`city_jianye` 應讓玩家感受到秩序終於從防線轉成城政與民生，節奏也從戒備轉成補給、問路與都城流動
- 世界缺口角色：
  - 把 `fort_naval_base` 北向建業水門正式轉成可持續擴建的 spec-first `City`
  - 為後續 `district_jianye_port`、`city_kuaiji` 與 `wild_river_delta` 建立江東主城 hub
- reserved_room_block: `16001-16030`
- planned_vnum_range: `16001-16030`
- level_range: `100-100`
- external_links:
  - `south`: `fort_naval_base` / 建業水門
  - `east`: `district_jianye_port` / 港區預留
  - `west`: `wild_jianye_west` / 西郊預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_jianye/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0074-fort-naval-base.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0074-fort-naval-base.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `fort_naval_base` 已把海路收束成軍事關卡，適合在下一區切回城市 hub，形成 `Wild -> Fort -> City` 的節奏閉環
  - `city_jianye` scaffold 提供都城、水門、市集與官署語彙，能直接承接海防前哨回城後的補給與治理感
  - `world-graph` 把建業放在江東主鏈的核心位置，因此此區適合作為港區、會稽與江東水域的總樞紐
  - `players.json / skills.json` 沒有提供必須先往更深海域或秘境跳轉的強證據，因此先回主城更符合節奏
- `compliance_check`
  - compliant；在 `Fort` 之後切入 `City`，讓海路鏈回到完整主城節奏，也維持 family 多樣性

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_jianye/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jianye/map.md --validate-only`
  - passed for `10` room(s)
- `python -X utf8 tools/mapmd_validate.py area/fort_naval_base/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15910 <-> 16001`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_naval_base/map.md`
  - rewrote `roo/15901-15912` to include the `15910 north -> 16001 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jianye/map.md`
  - wrote `roo/16001-16010`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1042.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `city_jianye`，保留房號段 `16001-16030`
- `area/city_jianye/index` 已建立，`Serial 164`
- 第一輪 runtime scaffold 已加入：
  - `mob/17631-17634`
  - `obj/17651-17654`
  - `res/city.res`
  - `shp/supplies.shp`
- `fort_naval_base/15910 <-> city_jianye/16001` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `city_jianye`

## Next Step Prompt

`先 commit 目前 city_jianye 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
