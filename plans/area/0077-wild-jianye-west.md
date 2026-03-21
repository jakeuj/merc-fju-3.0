# Wild Jianye West Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_jianye_west`。此區承接 `city_jianye` 西向城郊出口，把玩家從建業主城與港區的密集服務節奏，重新帶回一段由官道、水鄉、茶亭與郊野支路構成的江東城郊外帶，讓建業鏈在 `City / District` 之後切回 `Outskirts` 節奏。

## Theme Positioning

- theme: `江湖`
- subtheme: `郊野 / 水鄉`
- experience_type: `Outskirts`
- player_loop_focus: `回城轉場 / 郊道辨位 / 水鄉節奏 / 城外支線`
- contrast_with_previous_two:
  - 相對於 `city_jianye` 的都城中樞與 `district_jianye_port` 的商港分區，`wild_jianye_west` 應讓玩家感受到視野重新打開，但不再是外海壓力，而是主城外那種帶水氣、帶人煙、又開始可能偏離官道的江東郊野節奏
- 世界缺口角色：
  - 把 `city_jianye` 西向城郊預留正式轉成可持續擴建的 spec-first `Outskirts`
  - 為後續 `city_kuaiji`、山道或更深江東鄉野建立第一段主城外帶
- reserved_room_block: `16201-16230`
- planned_vnum_range: `16201-16230`
- level_range: `100-100`
- external_links:
  - `east`: `city_jianye` / 建業西門
  - `south`: `wild_mountain_pass` / 山道預留
  - `west`: `river_villages` / 水鄉村路預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_jianye_west/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0075-city-jianye.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_jianye_west/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0075-city-jianye.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - `ref/sanguo-area-specfirst/area/wild_mountain_pass/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_jianye` 已把海路節奏收束到江東主城，適合先往西補上一段城郊外帶，讓主城的陸路出口也正式成形
  - `wild_jianye_west` scaffold 提供官道、水鄉與茶亭語彙，能直接承接建業主城的都會節奏並轉成較鬆的郊外探索感
  - `world-graph` 把建業西郊放在建業旁的主城外帶位置，適合作為未來再往會稽或山道延伸的前置區
  - `players.json / skills.json` 沒有提供此時必須先跳去另一座城市的強證據，因此先補郊外過渡更符合 loop 完整性
- `compliance_check`
  - compliant；在 `City / District` 之後切回 `Outskirts`，讓建業鏈維持 family 多樣性，也避免主城片區連續堆疊過多 city-like 區塊

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_jianye_west/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_jianye_west/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)

## Next Step Prompt

`先 commit 目前 wild_jianye_west 的 spec milestone；commit 後直接做 implementation milestone，補 boundary、roo、index/mob/obj/res/shp，並跑 WSL build 與 startup smoke test。`
