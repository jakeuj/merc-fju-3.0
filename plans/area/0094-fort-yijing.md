# Fort Yijing Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_yijing`。此區承接 `road_yijing` 的易京前路口，把北平北境鏈從軍旅驛道正式收束成有關門、內營、軍需棚與望樓層次的關隘節點，讓 `北平郊區 -> 易京官道 -> 易京` 不再只停在抽象 graph，而是成為一段可辨位、可問路、也可承接後續白狼山與北方哨樓分流的 fort 型 choke point。

## Theme Positioning

- theme: `軍旅`
- subtheme: `北境軍鎮`
- experience_type: `Fort`
- player_loop_focus: `關隘轉場 / 軍令辨位 / 北境分流 / 補給與巡路壓力`
- contrast_with_previous_two:
  - 相對於 `road_nanpi_beiping` 的長路旅訊與 `road_yijing` 的邊境驛道節奏，`fort_yijing` 應把體驗重新收緊成軍鎮關門、內營秩序與望樓高差，而不是再延續一段只會更北、更直的長路。
- 世界缺口角色：
  - 把 `road_yijing/17808` 的北向預留正式轉成易京關隘節點
  - 為後續 `fort_northern_watch` 與 `wild_bailang` 建立可辨位的雙向分流母點
- reserved_room_block: `17901-17920`
- planned_vnum_range: `17901-17920`
- level_range: `26-38`
- external_links:
  - `south`: `road_yijing` / 易京前路口
  - `up`: `fort_northern_watch` / 北方哨樓預留
  - `east`: `wild_bailang` / 白狼山方向預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_yijing/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0003-beiping-outskirts.md`
- `plans/area/0093-road-yijing.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_yijing/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0003-beiping-outskirts.md`
  - `plans/area/0093-road-yijing.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/fort_northern_watch/map.md`
  - `ref/sanguo-area-specfirst/area/wild_bailang/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 把 `R 易京` 明確標成北平外圍的北方節點，適合作為北境鏈從 road 收束到 fort 的第一個軍事 choke point
  - `world-graph` 直接給出 `road_yijing -> fort_yijing -> fort_northern_watch / wild_bailang` 的 family 與 level 帶，支持這區成為北境鏈的分流母點
  - `題材分布表` 把 `易京` 定位成 `軍旅 / 探險` 的關隘型袁紹勢力據點，支持這區強調戒備、軍令與前線壓力，而不是再做一段普通官道
  - `players.json / skills.json` 沒有提出比既有北境鏈更強的城市服務型優先訊號，支持先補這個已被 `road_yijing` 明確預留的北向 fort 節點
- `compliance_check`
  - compliant；在 `Road` 之後切到 `Fort`，符合 queue variety，也直接承接 `road_yijing` 已完成的北向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_yijing/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 tools/mapmd_validate.py area/road_yijing/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yijing/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yijing/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\fort_yijing\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_yijing/map.md`
  - passed；同步把 `road_yijing/17808` 補成 `north -> 17901` runtime boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yijing/map.md`
  - passed；後續 `wild_bailang` implementation milestone 已同步把 `fort_yijing/17908` 補成 `east -> 18001` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- WSL startup smoke
  - passed；有效結果寫入 `log/1066.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `fort_yijing` 與 `road_yijing` 相關新 warning

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20331-20334`、`obj/20351-20354`、`res/fort.res`、`shp/supplies.shp`、`roo/17901-17908`
- 已正式落成南側 runtime boundary：`road_yijing/17808 <-> fort_yijing/17901`
- 已正式落成東側 runtime boundary：`fort_yijing/17908 <-> wild_bailang/18001`
- `up -> fort_northern_watch` 仍維持 world-link metadata，待後續北境節點 milestone 再正式接上
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `fort_yijing`

## Next Step Prompt

`fort_yijing` 的 implementation milestone 已完成；下一步依 queue 規則盤點下一個北境待建 area，優先檢查 `Fort -> Wild` 的 family 切換下 `wild_bailang` 是否成為新的 next actionable area。`
