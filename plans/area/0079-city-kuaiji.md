# City Kuaiji Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_kuaiji`。此區承接 `wild_mountain_pass` 南下山門，把玩家從抬升的山道與風口岔台正式帶進會稽這座帶山城、門派與地方勢力氣息的江東城市，作為建業鏈往更深江東支線展開前的下一個 city hub。

## Theme Positioning

- theme: `江湖`
- subtheme: `山城 / 門派`
- experience_type: `City`
- player_loop_focus: `進城回補 / 山城問路 / 門派傳聞 / 江東中繼`
- contrast_with_previous_two:
  - 相對於 `wild_jianye_west` 的水鄉城郊與 `wild_mountain_pass` 的抬升山道，`city_kuaiji` 應把節奏重新收束成有人煙、有秩序、但仍明顯帶著地方門派與山城流動感的主城節點
- 世界缺口角色：
  - 把建業鏈正式從山道轉進會稽主城
  - 為後續 `dng_temple_ruins`、更深江東支線與會稽周邊片區建立母城節點
- reserved_room_block: `16401-16430`
- planned_vnum_range: `16401-16430`
- level_range: `100-100`
- external_links:
  - `north`: `wild_mountain_pass` / 會稽北口
  - `east`: `district_kuaiji_market` / 東市預留
  - `down`: `dng_temple_ruins` / 古祠地脈預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
- `ref/sanguo-area-specfirst/area/wild_mountain_pass/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/quaji.html`
- `plans/area/0078-wild-mountain-pass.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - `ref/sanguo-area-specfirst/area/wild_mountain_pass/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/quaji.html`
  - `plans/area/0078-wild-mountain-pass.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/sanguo-area-specfirst/area/dng_temple_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 與 `world-graph` 都把會稽放在建業之後的江東主城節點，適合在山道 wild 之後立刻收束成正式城市 hub
  - `題材分布表` 把會稽定位成 `江湖 / 仙俠` 的山城與門派節點，支持在城市語氣中保留地方勢力與傳聞感
  - `city_kuaiji` scaffold 提供城門、主街、市集與官府骨架，能直接轉成目前需要的山城主街版本
  - `maps.json` 與 `quaji.html` 證明會稽在舊站地圖上具有完整城市輪廓，適合作為下一個主城落點
- `compliance_check`
  - compliant；在 `Wild` 之後切回 `City`，延續 `City -> Outskirts -> Wild -> City` 的節奏，也讓建業鏈恢復母城回補節點

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_kuaiji/map.md`
  - passed (`Validated 10 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_kuaiji/map.md --validate-only`
  - passed (`Validation succeeded for 10 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_kuaiji/map.md`
  - passed (`Wrote 10 room scaffold file(s) to area/city_kuaiji/roo`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1048.log`
- `debug/badobject`
  - passed (empty after smoke test)

## Next Step Prompt

`先 commit 目前 city_kuaiji 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立下一個 spec milestone。`
