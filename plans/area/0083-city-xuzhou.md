# City Xuzhou Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_xuzhou`。此區承接 `city_chenliu` 東街路標，把玩家從中原樞紐城正式帶進徐州這座東線州府，讓 `陳留 -> 徐州 -> 壽春 / 建業` 這條陸路主線重新有一個可回補、可問路、也能承接州府秩序與商旅消息的城市 hub。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `東線州府 / 商旅樞紐`
- experience_type: `City`
- player_loop_focus: `進城回補 / 州府問路 / 商旅中繼 / 東線轉場`
- contrast_with_previous_two:
  - 相對於 `wild_river_delta` 的開放江汊外水與 `sec_water_ruins` 的靜壓殘宮，`city_xuzhou` 應把節奏明確拉回地表城市秩序，讓玩家從深水祕境回到有城門、州府、市集與驛路消息的東線交通 hub。
- 世界缺口角色：
  - 把 `city_chenliu/13810` 的徐州預留正式轉成可載入的 spec-first `City`
  - 為後續 `road_shouchun_xuzhou`、`city_shouchun` 與江東北段陸路主線建立母城節點
- reserved_room_block: `16801-16820`
- planned_vnum_range: `16801-16820`
- level_range: `20-32`
- external_links:
  - `west`: `city_chenliu` / 徐州大道
  - `south`: `road_shouchun_xuzhou` / 淮東官道預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_xuzhou/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0053-city-chenliu.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_xuzhou/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0053-city-chenliu.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_shouchun/map.md`
  - `ref/sanguo-area-specfirst/area/road_shouchun_xuzhou/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `area/world_map.md` 明確把 `洛陽 - 陳留 - 徐州` 與 `壽春 - 建業` 放在同一條東線陸路骨架上，支持先把徐州補成州府 hub，再往南接壽春線
  - `world-graph` 把 `city_xuzhou` 設為 `city`，並直接承接 `city_chenliu`，說明這裡是中原往江東北段推進時最缺的城市接面
  - `題材分布表` 把江東北段保留為 `歷史城市 / 軍旅` 混合帶，支持徐州先以州府秩序、市集煙火與州城交通為主，而非再次滑向秘境或純野外
  - `players.json / skills.json` 沒有提供必須延續外海 secret 或再疊更深祕境的強信號，反而支持先回到能承接補給與問路 loop 的城市節點
- `compliance_check`
  - compliant；在 `Secret` 之後切回 `City`，同時補上 `陳留 -> 徐州` 的主線缺口，符合 queue variety 與東線交通骨架

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_xuzhou/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xuzhou/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)
- `python -X utf8 tools/mapmd_validate.py area/city_chenliu/map.md`
  - passed (`Validated 17 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`) after aligning `13810 <-> 16801`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xuzhou/map.md`
  - passed (`Wrote 9 room scaffold file(s) to area/city_xuzhou/roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md`
  - passed (`Wrote 17 room scaffold file(s) to area/city_chenliu/roo`) after aligning `13810 <-> 16801`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1054.log`
- `debug/badobject`
  - passed (empty after smoke test)
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `city_xuzhou`，保留房號段 `16801-16820`
- `area/city_xuzhou/index` 已建立，`Serial 172`
- 第一輪 runtime scaffold 已加入：
  - `mob/19231-19234`
  - `obj/19251-19254`
  - `res/city.res`
  - `shp/supplies.shp`
- `city_chenliu/13810 <-> city_xuzhou/16801` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `city_xuzhou`

## Next Step Prompt

`先 commit 目前 city_xuzhou 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立新的 spec milestone。`
