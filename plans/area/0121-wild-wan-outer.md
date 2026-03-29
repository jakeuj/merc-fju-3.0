# Wild Wan Outer Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_wan_outer`。此區承接 `city_wan` 西城牌樓，把剛剛在宛城內重新收束起來的驛傳與榜牌秩序，鬆開成茶棚、郊道、田埂與路旁樹叢交錯的城外過渡帶。它不該只是 `city_wan` 的背景外框，而要讓玩家明顯感到自己正從可整補、可問路的歷史城市，走進一段已經開始摻進流民、耳語與灰色腳步的宛城外帶。

## Theme Positioning

- theme: `江湖`
- subtheme: `郊道 / 茶棚`
- experience_type: `Wild`
- player_loop_focus: `回城 / 問路 / 茶棚補給 / 郊道辨位 / 城外灰帶探索`
- contrast_with_previous_two:
  - 相對於 `city_wan` 的城市秩序與 `road_wan` 的線性主線官道，`wild_wan_outer` 應刻意把節奏切回較鬆、較斜、也更有灰色人流氣味的城郊過渡 wild。
- 世界缺口角色：
  - 把 `city_wan/20408` 的 `out` 正式轉成 `wild_wan_outer/20601` 的 `enter`
  - 為宛城西側更深的郊道、林帶與後續側向支線建立第一段可載入的外城母帶
- reserved_room_block: `20601-20620`
- planned_vnum_range: `20601-20620`
- level_range: `14-24`
- external_links:
  - `enter`: `city_wan` / 西城牌樓 (`20408`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/index.html`
- `area/city_wan/map.md`
- `area/road_wan/map.md`
- `plans/area/0119-city-wan.md`
- `plans/area/0120-road-wan.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/index.html`
  - `area/city_wan/map.md`
  - `area/road_wan/map.md`
  - `plans/area/0119-city-wan.md`
  - `plans/area/0120-road-wan.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/road_chenliu_loyang/map.md`
  - `ref/sanguo-area-specfirst/area/city_chenliu/map.md`
  - `docs/3yWebsite/map/chenliu.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_wan` 現有 spec 已把 `20408` 定位成西城牌樓並預留 `out -> wild_wan_outer`，代表這條城外掛接點已成熟，不必再額外整理方向契約
  - `world-graph` 直接把 `wild_wan_outer` 列為 `city_wan` 旁的 `outskirts / 江湖 / 14-24` 節點，正好能在 `road_wan` 之後把 family 從 `Road` 切回 `Wild`
  - `area/world_map.md` 與 `docs/3yWebsite/map/index.html` 都更重視 `洛陽 -> 宛 -> 新野 -> 襄陽` 這條主骨架；既然 `road_wan` 已經先補完主線，現在回頭把宛西側外帶落地，節奏比直接再開另一條 `Road` 更平衡
  - `players.json / skills.json` 沒有提供必須立刻跳回 `road_chenliu` 的強訊號，反而支持先補一個能承接補給、問路與灰色遭遇的近郊 wild，避免連續堆同質官道
- `compliance_check`
  - compliant；本輪從空 queue 重建後選 `wild_wan_outer`，成功避開 `road_wan -> road_chenliu` 的同 family 疊加，也沿用了 `city_wan` 已成熟的 west-edge stub

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_wan_outer/map.md` 與 `area/city_wan/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `wild_wan_outer` 與 `city_wan` 均通過；正式 `.roo` 生成後已確認 `city_wan/20408 out <-> wild_wan_outer/20601 enter` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- 本輪 direct smoke 未額外產生新的 numbered `log/*`；成功訊號以 stdout 與 `debug/*` 檢查為準
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_wan_outer` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版 runtime 房間落在 `20601-20608`
- 已正式落成 runtime boundary：`city_wan/20408 out -> wild_wan_outer/20601` 與 `wild_wan_outer/20601 enter -> city_wan/20408`
- 首版聚焦西城外道口、郊道、茶棚、田埂與路旁樹叢，暫不提前延伸更深的宛西支線 world link
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 wild_wan_outer implementation milestone commit：內容包含 city_wan/20408 out <-> wild_wan_outer/20601 enter runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
