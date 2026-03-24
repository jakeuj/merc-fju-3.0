# Road Yijing Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_yijing`。此區承接 `beiping_outskirts` 的邊關整隊場，把北平北境外帶正式送上往易京去的軍旅驛道，讓 `北平郊區 -> 易京官道 -> 易京` 不再只剩抽象 world link，而是一段可辨位、可問路、也能把邊境傳聞往更北處推進的 road 型過渡區。

## Theme Positioning

- theme: `軍旅`
- subtheme: `北方驛道`
- experience_type: `Road`
- player_loop_focus: `北境轉場 / 驛道問路 / 巡隊換班 / 邊關傳聞`
- contrast_with_previous_two:
  - 相對於 `fort_river_crossing` 的關卡壓迫與 `road_nanpi_beiping` 的北地長路旅訊，`road_yijing` 應把節奏再往邊境軍旅推近一層，強調驛道、巡隊與易京前帶，而不是再做一塊單純城際官道。
- 世界缺口角色：
  - 把 `beiping_outskirts/9105` 的北向預留正式轉成易京官道節點
  - 為後續 `fort_yijing` 建立清楚的北境軍旅路網骨架
- reserved_room_block: `17801-17820`
- planned_vnum_range: `17801-17820`
- level_range: `22-32`
- external_links:
  - `south`: `beiping_outskirts` / 邊關整隊場
  - `north`: `fort_yijing` / 易京方向預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_yijing/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0003-beiping-outskirts.md`
- `plans/area/0092-road-nanpi-beiping.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_yijing/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0003-beiping-outskirts.md`
  - `plans/area/0092-road-nanpi-beiping.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/fort_yijing/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 與 `world-graph` 都明確把北平往易京方向定成北境主線，`road_yijing` 是 `beiping_outskirts` 之後的自然承接節點
  - `beiping_outskirts` 的既有 spec/runtime 已保留 `9105 north -> yijing_road` 預留，支持這區直接接著落地
  - `題材分布表` 把 `北平郊區 -> 易京` 這段定成 `江湖 / 軍旅 / 關隘` 漸進帶，適合先用一段軍旅驛道把主線拉向易京
  - `players.json / skills.json` 沒有對北平內城分區提出比既有北境預留更強的優先訊號，支持先補這條已明示的北向驛道路骨架
- `compliance_check`
  - compliant；雖然這輪會形成 `Road -> Road` 連續 family，但 `road_yijing` 是既有 `beiping_outskirts` 明確預留的 next actionable boundary，且 world-map / dataset 沒有更強的內城服務區優先訊號，屬於可說明的 queue variety 例外

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_yijing/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 tools/mapmd_validate.py area/beiping_outskirts/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_yijing/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/beiping_outskirts/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_yijing/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\road_yijing\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/beiping_outskirts/map.md`
  - passed；同步把 `beiping_outskirts/9105` 補成 `north -> 17801` runtime boundary，並補齊 `reserved_room_block`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- WSL startup smoke
  - passed；有效結果寫入 `log/1065.log`（`三國歪傳之降龍伏虎開始正常運作`）
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `road_yijing` 與 `road_nanpi_beiping` 相關新 warning

## Next Step Prompt

`road_yijing` 的 implementation milestone 已完成；下一步依 queue 規則盤點下一個待建 area，優先檢查北境鏈在 family variety 與既有 world-link 預留下的下一個 actionable 節點。`

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20231-20234`、`obj/20251-20254`、`res/road.res`、`shp/supplies.shp`、`roo/17801-17808`
- 已正式落成南側 runtime boundary：`beiping_outskirts/9105 <-> road_yijing/17801`
- 北側 `fort_yijing` 仍維持 world-link metadata，待下一個 fort milestone 再正式接上
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `road_yijing`
