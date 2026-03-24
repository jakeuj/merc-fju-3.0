# Wild Liaodong Plain Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_liaodong_plain`。此區承接 `city_xiangping` 的北原牌樓，把北境主線從遼東邊城的補給、訓練與驛站節奏，再次推回開闊北地，讓 `襄平 -> 遼東平原` 成為一段真正可辨位、可問路、也能為更北遼東節點留出空間的 wide-open wild。

## Theme Positioning

- theme: `軍旅`
- subtheme: `草原 / 騎兵前帶`
- experience_type: `Wild`
- player_loop_focus: `平原辨位 / 風勢觀察 / 馬跡辨認 / 北地轉場`
- contrast_with_previous_two:
  - 相對於 `wild_barbarian_camp` 的敵蹤與舊營壓力，以及 `city_xiangping` 的邊城整補與服務節奏，`wild_liaodong_plain` 應把玩家重新放回開闊視野、遠距判斷與草原風勢主導的北地 wild，而不是先做另一段以路亭為主的 connector。
- 世界缺口角色：
  - 把 `city_xiangping/18308` 的北向預留正式轉成遼東平原入口節點
  - 為後續更深遼東平野、騎兵帶或北境支線建立第一段 open-field wild 骨架
- reserved_room_block: `18401-18420`
- planned_vnum_range: `18401-18420`
- level_range: `32-44`
- external_links:
  - `south`: `city_xiangping` / 襄平北原牌樓
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_liaodong_plain/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0098-city-xiangping.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_liaodong_plain/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0098-city-xiangping.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/road_north_border/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 把 `wild_liaodong_plain` 放在 `city_xiangping` 北側，level 帶也自然承接 `34-46` 的邊城節奏，是襄平之後最順的 open-field 主線節點
  - `題材分布表` 對應 `平原外草原` 與 `遼東入口` 的北地空間感，支持先把城市之後的開闊 wild 補出來，再談更專注的 road connector
  - `players.json / skills.json` 對襄平提供的是服務與整補訊號，而不是把玩家立刻推向另一段驛路；這反而支持城市之後先切回 `Wild`，恢復 family variety
  - `city_xiangping` runtime 已把 `18308 north` 留在 world-link metadata，現在補這個 spec 能讓下一輪 implementation 直接承接北原牌樓
- `compliance_check`
  - compliant；在 `City` 之後切回 `Wild`，同時回應遼東主線拓撲與 queue variety，不讓 `road_north_border` 先把節奏收窄成純 connector

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_liaodong_plain/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_liaodong_plain/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_liaodong_plain/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\wild_liaodong_plain\roo`)
- `python -X utf8 tools/mapmd_validate.py area/city_xiangping/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangping/map.md`
  - passed；同步把 `city_xiangping/18308` 補成 `north -> 18401` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && timeout 45 ./merc merc.test.ini"`
  - passed；因使用中的遊戲實例已占用預設 `3838`，改以臨時測試 port `23838/21234/28888` 做 direct-load smoke，並在 console 看見 `三國歪傳之降龍伏虎開始正常運作`
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `wild_liaodong_plain` 與 `city_xiangping` 相關新 warning

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20831-20834`、`obj/20851-20854`、`res/wild.res`、`shp/supplies.shp`、`roo/18401-18408`
- 已正式落成南側 runtime boundary：`city_xiangping/18308 <-> wild_liaodong_plain/18401`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_liaodong_plain`

## Next Step Prompt

`wild_liaodong_plain` 的 implementation milestone 已完成；下一步依 queue 規則盤點下一個遼東待建 area，優先檢查 `road_north_border` 是否成為新的 spec milestone。`
