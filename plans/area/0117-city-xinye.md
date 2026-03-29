# City Xinye Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_xinye`。此區承接 `city_xiangyang` 官署前街外那條原本只停在 world-link 想像層的新野內陸去路，把荊州北段從單純軍務與關隘壓力，重新展開成一座更偏邊鎮、義士與地方煙火氣的小型城市 hub。它不該和襄陽重複成另一座大城，而要讓玩家明顯感到自己是從州府門戶，轉進一座更有人情、更靠消息與地方人物撐住節奏的內陸邊鎮。

## Theme Positioning

- theme: `江湖`
- subtheme: `邊鎮 / 義士`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 地方消息 / 邊鎮停腳 / 宛道前導`
- contrast_with_previous_two:
  - 相對於 `district_chengdu_scholar` 的都城靜院秩序與 `fort_fancheng` 的北岸軍令壓力，`city_xinye` 應把節奏轉成更小尺度、更多人情與地方傳聞感的內陸邊鎮。
- 世界缺口角色：
  - 把 `city_xiangyang` 那條通往新野的內陸去路，正式落成為可載入的城市節點
  - 先替荊州北段建立 `襄陽 -> 新野 -> 宛` 這條內陸支鏈的第一個可停留母城
- reserved_room_block: `20201-20220`
- planned_vnum_range: `20201-20220`
- level_range: `18-30`
- external_links:
  - `enter`: `city_xiangyang` / 官署前街外路
  - `north`: `city_wan` / 宛道（spec 保留，暫不落 runtime 外連）
  - `west`: `wild_xinye_fields` / 郊野田路（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_xinye/map.md`
- `ref/sanguo-area-specfirst/area/wild_xinye_fields/map.md`
- `ref/sanguo-area-specfirst/area/city_wan/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/map/sinya.html`
- `area/city_xiangyang/map.md`
- `area/jingxiang_road/map.md`
- `plans/area/0116-fort-fancheng.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_xinye/map.md`
  - `ref/sanguo-area-specfirst/area/wild_xinye_fields/map.md`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `docs/3yWebsite/map/sinya.html`
  - `area/city_xiangyang/map.md`
  - `area/jingxiang_road/map.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/road_wan/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 與 `world-graph` 都把 `宛 -> 新野 -> 襄陽` 視為荊州北段主幹，支持先把 `city_xinye` 補成內陸邊鎮 hub
  - `題材分布表` 把新野定位成 `江湖 / 歷史` 的邊鎮，剛好能在 `fort_fancheng` 的軍事壓力後拉回更有人情的地方城市節奏
  - `city_xiangyang` 現行 spec 已明確保留新野去路，但原本寫成 `14209 west` 會和既有內部 `west` 出口衝突；本輪改用 `out/enter` 才能讓 runtime 正式落地
  - `jingxiang_road/9305 -> city_xinye` 與 ref scaffold 的方向契約仍互相打架，本輪不硬接，先讓 `city_xinye` 以一側成熟邊界正式上線
- `compliance_check`
  - conditionally compliant；本輪仍以 `city_xinye` 為下一個 actionable area，但採「現行 runtime 可落地邊界優先」策略，只先正式接回 `city_xiangyang`，把 `jingxiang_road` 與 `city_wan` 的後續方位整理留給下一輪 queue 判斷

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_xinye/map.md` 與 `area/city_xiangyang/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `city_xinye` 與 `city_xiangyang` 均通過；正式 `.roo` 生成後已確認 `city_xiangyang/14209 out <-> city_xinye/20201 enter` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- 本輪 direct smoke 未額外產生新的 numbered `log/*`；成功訊號以 stdout 與 `debug/*` 檢查為準
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py city_xinye` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 第一版預計落地 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版房間預計使用 `20201-20208`
- 本輪正式邊界會採 `city_xiangyang/14209 out <-> city_xinye/20201 enter`
- `city_wan` 與 `wild_xinye_fields` 先保留在 `map.md` / tracker 的 spec 層，不提前建立假外連
- `jingxiang_road/9305` 的現行方位契約暫時不動，等後續 queue 重建時再單獨整理

## Next Step Prompt

`提交 city_xinye implementation milestone commit：內容包含 city_xiangyang/14209 out <-> city_xinye/20201 enter runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
