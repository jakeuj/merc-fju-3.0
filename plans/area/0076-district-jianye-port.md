# District Jianye Port Initial Area Plan

## Summary

建立下一個待建新 AREA：`district_jianye_port`。此區承接 `city_jianye` 東向港向街口，把玩家從江東都城主街正式帶進碼頭、貨棚、泊位與船行聚集的商港分區，讓建業的城市節奏從內城治理延伸到對外航運與交易服務。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `碼頭 / 商港`
- experience_type: `District`
- player_loop_focus: `港區補給 / 船貨轉運 / 問路導流 / 對外航線`
- contrast_with_previous_two:
  - 相對於 `fort_naval_base` 的軍事海防與 `city_jianye` 的都城中樞，`district_jianye_port` 應讓玩家感受到更明確的商港功能分區，節奏從行政與主街流動轉成裝卸、交易與航運導流
- 世界缺口角色：
  - 把 `city_jianye` 東向港區預留正式轉成可持續擴建的 spec-first `District`
  - 為後續更深港埠、航線、船務或東向海路分支建立商港 hub
- reserved_room_block: `16101-16130`
- planned_vnum_range: `16101-16130`
- level_range: `100-100`
- external_links:
  - `west`: `city_jianye` / 港向街口
  - `south`: `sea_trade_route` / 商船航路預留
  - `east`: `district_shipyards` / 造船區預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
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
  - `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0075-city-jianye.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - `ref/sanguo-area-specfirst/area/wild_jianye_west/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_jianye` 已把海路主線收束到都城 hub，適合先往東補齊港區服務鏈，而不是立刻再切回另一個大範圍野外或城市
  - `district_jianye_port` scaffold 提供碼頭、商港與交易導流語彙，能直接承接建業的都城氣質並補出更細的港埠功能
  - `world-graph` 把建業港區放在建業主城旁的功能分區，適合作為後續船務、商線與對外 travel 的落點
  - `players.json / skills.json` 沒有提供必須優先跳去會稽或西郊的強證據，因此先做港區 district 更符合服務鏈完整性
- `compliance_check`
  - compliant；在 `City` 之後切入 `District`，先細化主城服務節點，再決定往 `Wild` 或另一座 `City` 展開

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/district_jianye_port/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_jianye_port/map.md --validate-only`
  - passed for `8` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_jianye/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `16010 <-> 16101`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jianye/map.md`
  - rewrote `roo/16001-16010` to include the `16010 east -> 16101 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_jianye_port/map.md`
  - wrote `roo/16101-16110`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1043.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `district_jianye_port`，保留房號段 `16101-16130`
- `area/district_jianye_port/index` 已建立，`Serial 165`
- 第一輪 runtime scaffold 已加入：
  - `mob/17831-17834`
  - `obj/17851-17854`
  - `res/port.res`
  - `shp/supplies.shp`
- `city_jianye/16010 <-> district_jianye_port/16101` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `district_jianye_port`

## Next Step Prompt

`先 commit 目前 district_jianye_port 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
