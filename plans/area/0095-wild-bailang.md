# Wild Bailang Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_bailang`。此區承接 `fort_yijing` 的東側寨牆，把北境鏈從軍鎮關隘正式切進白狼山前帶的山前 wild 節奏，讓 `易京 -> 白狼山` 不再只是抽象 graph，而是一段可辨位、可問路、也能預留北林、古洞、胡營與更高秘境分流的探險節點。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `山前異域`
- experience_type: `Wild`
- player_loop_focus: `山前轉場 / 風裂地標 / 異族前帶 / 深山分流`
- contrast_with_previous_two:
  - 相對於 `road_yijing` 的軍旅驛道與 `fort_yijing` 的軍鎮秩序，`wild_bailang` 應把節奏打開成更冷、更荒、也更帶傳說感的山前探索，而不是再維持寨牆與軍令主體。
- 世界缺口角色：
  - 把 `fort_yijing/17908` 的東向預留正式轉成白狼山前帶 wild 節點
  - 為後續 `wild_wolf_forest`、`dng_ancient_cave`、`wild_barbarian_camp` 與 `sec_starfall_crater` 建立可辨位的分流母點
- reserved_room_block: `18001-18020`
- planned_vnum_range: `18001-18020`
- level_range: `30-42`
- external_links:
  - `west`: `fort_yijing` / 東側寨牆
  - `north`: `wild_wolf_forest` / 狼林方向預留
  - `down`: `dng_ancient_cave` / 古洞遺跡預留
  - `east`: `wild_barbarian_camp` / 胡營舊地方向預留
  - `up`: `sec_starfall_crater` / 星墜天坑預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_bailang/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0094-fort-yijing.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_bailang/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0094-fort-yijing.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/wild_wolf_forest/map.md`
  - `ref/sanguo-area-specfirst/area/dng_ancient_cave/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 把 `S 白狼山` 標成遼東 / 襄平方向的邊境節點，支持此區成為易京之後把視野從關隘打開到邊山探索的下一步
  - `world-graph` 明確把 `fort_yijing` 之後的 family 切換點之一定成 `wild_bailang`，level 帶也自然承接 `26-38 -> 30-42`
  - `題材分布表` 把 `白狼山` 定位成 `探險遺跡 / 詭異` 的山區與異族傳說帶，能和 `fort_yijing` 的軍旅秩序形成清楚體驗差
  - `players.json / skills.json` 沒有提出比既有北境鏈更強的城市或分區服務優先訊號，支持先補這個由 `fort_yijing` 明確預留的東向 wild 節點
- `compliance_check`
  - compliant；在 `Fort` 之後切到 `Wild`，符合 queue variety，也直接承接 `fort_yijing/17908` 的既有東向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_bailang/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_bailang/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_bailang/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\wild_bailang\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_bailang/map.md`
  - passed；後續 `dng_ancient_cave` implementation milestone 已同步把 `wild_bailang/18006` 補成 `down -> 18101` runtime boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yijing/map.md`
  - passed；同步把 `fort_yijing/17908` 補成 `east -> 18001` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- WSL startup smoke
  - passed；有效結果寫入 `log/1067.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `wild_bailang` 與 `fort_yijing` 相關新 warning

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20431-20434`、`obj/20451-20454`、`res/wild.res`、`shp/supplies.shp`、`roo/18001-18008`
- 已正式落成西側 runtime boundary：`fort_yijing/17908 <-> wild_bailang/18001`
- 已正式落成下側 runtime boundary：`wild_bailang/18006 <-> dng_ancient_cave/18101`
- `north -> wild_wolf_forest`、`east -> wild_barbarian_camp` 與 `up -> sec_starfall_crater` 仍維持 world-link metadata，待後續北境節點 milestone 再正式接上
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_bailang`

## Next Step Prompt

`wild_bailang` 的 implementation milestone 已完成；下一步依 queue 規則盤點下一個北境待建 area，優先檢查 `Wild -> Dungeon` 的 family 切換下 `dng_ancient_cave` 是否成為新的 next actionable area。`
