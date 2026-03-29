# Wild Chengdu Outer Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_chengdu_outer`。此區承接 `city_chengdu` 西郊城關，把剛剛在都城母區收束起來的秩序重新鬆開成官道、茶亭、圩田與路旁林地交錯的城外過渡帶。這裡不該只是附屬背景，而要讓玩家明顯感到自己從成都的厚重規矩走進了真正會把旅程重新拉長、也把風險重新打開的蜀地近郊。

## Theme Positioning

- theme: `江湖`
- subtheme: `郊外 / 農田`
- experience_type: `Wild`
- player_loop_focus: `回城 / 問路 / 茶亭補給 / 郊道路徑辨位 / 城外過渡`
- contrast_with_previous_two:
  - 相對於 `fort_yongan` 的堡寨壓力與 `city_chengdu` 的都城秩序，`wild_chengdu_outer` 應更強調離城後的鬆動感、官道長路感與城外灰色人群的混雜氣味。
- 世界缺口角色：
  - 把 `city_chengdu/19708` 的 `out` 正式轉成 `wild_chengdu_outer/19801` 的 `enter`
  - 為成都之後的更深郊野、農路與支線事件建立第一段城外母帶
- reserved_room_block: `19801-19820`
- planned_vnum_range: `19801-19820`
- level_range: `30-42`
- external_links:
  - `enter`: `city_chengdu` / 西郊城關
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_chengdu_outer/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_chengdu/map.md`
- `plans/area/0112-city-chengdu.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_chengdu_outer/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_chengdu/map.md`
  - `plans/area/0112-city-chengdu.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/district_chengdu_market/map.md`
  - `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_chengdu` 現有 spec 已把 `19708` 定位成西郊城關，並預留 `out -> wild_chengdu_outer` metadata，代表近郊外帶已有成熟的 runtime 掛接點
  - `world-graph` 直接把 `wild_chengdu_outer` 列為成都之後的 `outskirts / 江湖 / 30-42` 節點，是目前最直接也最不破壞蜀地主線的 non-`City` 候選
  - `題材分布表` 將成都定位成蜀漢首都、將蜀地山野拉往更外側的探索帶，因此在都城後先補一段官道與農田近郊，比先切入 `district_chengdu_*` 更能維持題材起伏
  - `players.json / skills.json` 沒有提供「成都城內 teacher / service district 必須優先」的強訊號，因此本輪先補城外過渡 loop 而非再堆城市分區
- `compliance_check`
  - compliant；在 `city_jiangzhou -> city_chengdu` 連續兩個 `City` 後，`wild_chengdu_outer` 既能恢復 family variety，又不用脫離當前蜀地主線與成熟 boundary stub

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_chengdu_outer/map.md` 與 `area/city_chengdu/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `wild_chengdu_outer` 與 `city_chengdu` 均通過；正式 `.roo` 生成後已確認 `city_chengdu/19708 out <-> wild_chengdu_outer/19801 enter` 雙向邊界一致
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_chengdu_outer` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版 runtime 房間落在 `19801-19808`
- 已正式落成 runtime boundary：`city_chengdu/19708 out -> wild_chengdu_outer/19801` 與 `wild_chengdu_outer/19801 enter -> city_chengdu/19708`
- 首版聚焦城關外坡、官道、茶亭、圩田與路旁林地，暫不提前延伸更深的蜀地腹心 world link
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 wild_chengdu_outer implementation milestone，然後把 tracker 從 in_progress 推進成 done。`
