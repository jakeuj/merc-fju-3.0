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
- delivery_gate: `spec_ready_for_commit`

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
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_yijing/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Next Step Prompt

`先完成 road_yijing 的 validate-only 檢查與 spec milestone commit；commit 後直接進 implementation，補齊對 beiping_outskirts 的 runtime boundary、生成 roo 與最小 area runtime scaffold。`
