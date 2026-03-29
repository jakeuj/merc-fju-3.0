# District Chengdu Scholar Initial Area Plan

## Summary

建立下一個待建新 AREA：`district_chengdu_scholar`。此區承接 `city_chengdu` 的學舍外街，把蜀漢都城原本只停在氣味與方向感上的書卷氛圍，正式展開成講席、書坊、碑廊、靜院與榜帖角交錯的文士分區。這裡不該只是另一段「比較安靜的街」，而要讓玩家清楚感到成都除了市井與官務，也有一整套靠讀書、問學與消息整理撐起來的城市厚度。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `文士 / 書院`
- experience_type: `District`
- player_loop_focus: `問學導流 / 城內問路 / 榜帖傳聞 / 靜院停留 / 書院氛圍`
- contrast_with_previous_two:
  - 相對於 `wild_chengdu_outer` 的離城鬆動感與 `district_chengdu_market` 的人潮喧鬧，`district_chengdu_scholar` 應把節奏轉回更安靜、更有知性秩序的都城腹地，讓成都的城市厚度不是只靠商街與主街撐起來。
- 世界缺口角色：
  - 把 `city_chengdu/19706` 的學舍預留正式轉成 `district_chengdu_scholar/20001` 的 runtime boundary
  - 為成都後續更深的書院、地方問學、告示任務與都城知識型支線建立第一段文士 `District`
- reserved_room_block: `20001-20020`
- planned_vnum_range: `20001-20020`
- level_range: `36-48`
- external_links:
  - `south`: `city_chengdu` / 學舍外街
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_chengdu/map.md`
- `plans/area/0112-city-chengdu.md`
- `plans/area/0114-district-chengdu-market.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_chengdu/map.md`
  - `plans/area/0112-city-chengdu.md`
  - `plans/area/0114-district-chengdu-market.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_xinye/map.md`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_chengdu/19706` 已有成熟的學舍外街 stub，只需補一個 `north` boundary 就能把文士分區正式掛接進成都母城
  - 比起 `city_xinye` 等非 `District` 候選，`district_chengdu_scholar` 不需要同時重排多個既有 area 的內部方向，實作風險更低、world link 成熟度更高
  - `world-graph` 明確把 `district_chengdu_scholar` 放在成都旁的 `district / 36-48` 節點，正好承接 `district_chengdu_market` 後的另一種都城腹地體驗
  - `題材分布表` 把成都定位成蜀漢首都；在市場分區之後補一段書院 / 文士分區，能讓城市節奏往不同語彙擴張，而不是只重複商街或官街
- `compliance_check`
  - conditionally compliant；雖然連續兩個 `District` 不是 queue variety 的理想節奏，但這輪比較後未找到同等成熟、又不用大改既有 runtime 邊界的非 `District` 候選，因此先完成成都第二個核心分區

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/district_chengdu_scholar/map.md` 與 `area/city_chengdu/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `district_chengdu_scholar` 與 `city_chengdu` 均通過；正式 `.roo` 生成後已確認 `city_chengdu/19706 north <-> district_chengdu_scholar/20001 south` 雙向邊界一致
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py district_chengdu_scholar` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版 runtime 房間落在 `20001-20008`
- 已正式落成 runtime boundary：`city_chengdu/19706 north -> district_chengdu_scholar/20001` 與 `district_chengdu_scholar/20001 south -> city_chengdu/19706`
- 首版聚焦書院口、書坊長街、講席院、碑廊、靜讀巷與榜帖角，暫不提前延伸更深的蜀中學政或特殊 quest system
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 district_chengdu_scholar implementation milestone，然後把 tracker 從 in_progress 推進成 done。`
