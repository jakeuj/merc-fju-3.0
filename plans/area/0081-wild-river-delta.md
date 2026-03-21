# Wild River Delta Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_river_delta`。此區承接 `city_kuaiji` 東市轉角，把玩家從會稽山城與地脈異聞重新帶回開闊的江東水域，作為會稽鏈在地下 dungeon 之後重新展開的外放 wild 節點，並為後續更東側的港汊、外埠與水底支線預留穩定接點。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `江東水域 / 洲灘渡汊`
- experience_type: `Wild`
- player_loop_focus: `離城外放 / 水路辨位 / 洲灘探索 / 江東轉場`
- contrast_with_previous_two:
  - 相對於 `city_kuaiji` 的山城回補與 `dng_temple_ruins` 的封閉下探，`wild_river_delta` 應把節奏重新打開成有潮路、洲灘與分汊視野的江東外水 wild，讓玩家從封閉傳聞回到可選路、可辨位的開放轉場。
- 世界缺口角色：
  - 把 `city_kuaiji` 的東市預留正式轉成可載入的江東外水 wild
  - 為後續 `harbor_outpost`、`islet_shrine` 與更深江東水路支線建立第一段外放骨架
- reserved_room_block: `16601-16630`
- planned_vnum_range: `16601-16630`
- level_range: `100-100`
- external_links:
  - `west`: `city_kuaiji` / 會稽東市
  - `east`: `harbor_outpost` / 江汊外埠預留
  - `south`: `islet_shrine` / 洲心古祠預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_river_delta/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/quaji.html`
- `docs/3yWebsite/docs/data/players.json`
- `plans/area/0079-city-kuaiji.md`
- `plans/area/0080-dng-temple-ruins.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_river_delta/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/quaji.html`
  - `docs/3yWebsite/docs/data/players.json`
  - `plans/area/0079-city-kuaiji.md`
  - `plans/area/0080-dng-temple-ruins.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `wild_river_delta` 放在 `city_kuaiji` 與更深江東水路之間，適合在會稽的 city / dungeon 節奏後重新打開成外水 wild
  - `題材分布表` 將江東區的 `江東水道` 定位為 `探險` 主題，支持用河汊、洲灘與航道辨位來拉開和山城、古寺的體驗差
  - `wild_river_delta` scaffold 已提供河汊 / 航道骨架，可直接轉成目前需要的洲灘渡汊版本
  - `quaji.html` 與 `maps.json` 證明會稽本身是完整城市節點，從東市再往外展開成江汊野外具有舊站地圖語意上的合理性
  - `players.json` 雖未直接提供會稽後段服務 loop，但反而支持在會稽之後先做高辨識度的交通 / 探索 wild，而非立刻再疊一個城市片區
- `compliance_check`
  - compliant；在 `City -> Dungeon` 之後切回 `Wild`，既符合 queue variety，也讓江東鏈從封閉古寺重新回到開放水域節奏

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_river_delta/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_river_delta/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_river_delta/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/wild_river_delta/roo`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1052.log`
- `debug/badobject`
  - passed (empty after smoke test)

## Next Step Prompt

`先 commit 目前 wild_river_delta 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立新的 spec milestone。`
