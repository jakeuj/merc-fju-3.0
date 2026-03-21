# City Shouchun Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_shouchun`。此區承接 `road_shouchun_xuzhou` 南下官道口，把玩家從淮東驛路正式收束進壽春這座淮南據點主城，讓 `徐州 -> 淮東官道 -> 壽春` 形成完整的北段陸路節奏，並為後續 `wild_shouchun_fields` 與更南的建業方向建立新的城市 hub。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `淮南據點 / 北段轉運城`
- experience_type: `City`
- player_loop_focus: `進城回補 / 淮南問路 / 官道收束 / 北段轉運`
- contrast_with_previous_two:
  - 相對於 `city_xuzhou` 的州府秩序與 `road_shouchun_xuzhou` 的驛路轉場，`city_shouchun` 應把節奏重新收回一座更偏軍政與轉運氣息的淮南主城，讓玩家從路上疲態回到有補給、有官署也有外郊出口的母城節點。
- 世界缺口角色：
  - 把 `road_shouchun_xuzhou/16908` 的壽春預留正式轉成可載入的 spec-first `City`
  - 為後續 `wild_shouchun_fields` 與更南的建業線建立新的北段母城
- reserved_room_block: `17001-17020`
- planned_vnum_range: `17001-17020`
- level_range: `24-36`
- external_links:
  - `north`: `road_shouchun_xuzhou` / 淮東官道
  - `out`: `wild_shouchun_fields` / 城外田野預留
  - `south`: `city_jianye` / 建業方向預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_shouchun/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0084-road-shouchun-xuzhou.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_shouchun/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0084-road-shouchun-xuzhou.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/wild_shouchun_fields/map.md`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 把 `city_shouchun` 放在 `road_shouchun_xuzhou` 之後，並同時保留 `wild_shouchun_fields` 與 `city_jianye` 出口，支持壽春作為北段陸路重新收束成主城的節點
  - `area/world_map.md` 把 `徐州 - 壽春 - 建業` 放在同一條東線骨架上，說明壽春不是旁支，而是往江東主城前的重要中繼
  - `題材分布表` 把壽春定位為江東北段的歷史城市據點，適合先落成官署、市集與出城分流都清楚的母城
  - `players.json / skills.json` 沒有提供必須跳過壽春直接切別條支線的強信號，因此先補母城更符合節奏
- `compliance_check`
  - compliant；在 `Road` 之後切回 `City`，既符合 queue variety，也能自然承接 `wild_shouchun_fields`

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_shouchun/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_shouchun/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)
- `python -X utf8 tools/mapmd_validate.py area/road_shouchun_xuzhou/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`) after aligning `16908 <-> 17001`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_shouchun/map.md`
  - passed (`Wrote 9 room scaffold file(s) to area/city_shouchun/roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_shouchun_xuzhou/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/road_shouchun_xuzhou/roo`) after aligning `16908 <-> 17001`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1056.log`
- `debug/badobject`
  - passed (empty after smoke test)
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `city_shouchun`，保留房號段 `17001-17020`
- `area/city_shouchun/index` 已建立，`Serial 174`
- 第一輪 runtime scaffold 已加入：
  - `mob/19431-19434`
  - `obj/19451-19454`
  - `res/city.res`
  - `shp/supplies.shp`
- `road_shouchun_xuzhou/16908 <-> city_shouchun/17001` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `city_shouchun`

## Next Step Prompt

`先 commit 目前 city_shouchun 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立新的 spec milestone。`
