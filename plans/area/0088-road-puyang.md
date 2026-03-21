# Road Puyang Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_puyang`。此區承接剛補完的 `city_puyang` 南驛牌口，把濮陽和更早段的洛陽主城之間正式補成一段可辨位、可歇腳、也能承接旅訊流動的北行官道，讓 `洛陽 -> 濮陽` 不再只剩抽象 world link，而是有清楚前後節奏的 road 型過渡區。

## Theme Positioning

- theme: `軍旅`
- subtheme: `官道 / 北行`
- experience_type: `Road`
- player_loop_focus: `旅途中轉 / 問路歇腳 / 驛訊流動 / 北行轉場`
- contrast_with_previous_two:
  - 相對於 `wild_shouchun_fields` 的近郊田野與 `city_puyang` 的河北前沿主城，`road_puyang` 應刻意把節奏收回長路、路亭與驛訊，讓 queue 在 `City` 之後切到明確的交通 connector，而不是立刻再疊一座河北城市。
- 世界缺口角色：
  - 把 `city_puyang/17207` 的南向預留正式轉成可實作的官道節點
  - 為後續 `city_loyang` 與 `city_puyang` 之間建立可延續的中原北行路網骨架
- reserved_room_block: `17301-17320`
- planned_vnum_range: `17301-17320`
- level_range: `8-18`
- external_links:
  - `south`: `city_loyang` / 洛陽北門
  - `north`: `city_puyang` / 濮陽南驛
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_puyang/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0087-city-puyang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_puyang/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0087-city-puyang.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/loyang.html`
  - `ref/sanguo-area-specfirst/area/city_nanpi/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `road_puyang` 當成 `city_loyang <-> city_puyang` 之間的獨立 `road` 節點，支持先補交通帶，而不是直接回頭擴寫另一座城市
  - `city_puyang` 的當前 spec 已明確保留 `17207 south -> road_puyang`，支持此區作為既有邊界的自然承接
  - `題材分布表` 讓這段中原北行保持 `軍旅 / 官道` 氣質，適合把玩法重心放在路亭、押貨與旅訊，而非城內服務點
  - `players.json / skills.json` 沒有要求濮陽完成後必須立刻切去另一個城市 hub，支持用 connector area 把世界骨架補齊
- `compliance_check`
  - compliant；在 `City` 之後切到 `Road`，符合 queue variety，也直接承接剛完成的 `city_puyang` 南向預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_puyang/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_puyang/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Next Step Prompt

`先 commit 目前 road_puyang 的 spec milestone；commit 後直接進 implementation，補齊對 city_puyang 與 city_loyang 的 runtime boundary、生成 roo 與最小 area runtime scaffold。`
