# City Chengdu Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_chengdu`。此區承接 `city_jiangzhou` 西城官道口，把原本還停在上游貨旅、蜀中官道與都城想像裡的主線節奏，正式收束回蜀漢都城。這裡不該只是再做一個普通城市，而要讓玩家明顯感到自己從上游轉運城帶真正進入了更穩、更厚、更像母城核心的蜀地秩序。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `蜀漢都城`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 官署情報 / 都城母城 / 往市場與學舍前導`
- contrast_with_previous_two:
  - 相對於 `fort_yongan` 的堡寨壓力與 `city_jiangzhou` 的上游轉運節奏，`city_chengdu` 應更強調都城的穩定秩序、規模感與母城回收效果。
- 世界缺口角色：
  - 把 `city_jiangzhou/19608` 的西向官道正式轉成 `city_chengdu` 的東城門入口
  - 為後續 `district_chengdu_market`、`district_chengdu_scholar` 與 `wild_chengdu_outer` 建立都城母區
- reserved_room_block: `19701-19720`
- planned_vnum_range: `19701-19720`
- level_range: `34-48`
- external_links:
  - `east`: `city_jiangzhou` / 東來官道
  - `east`: `district_chengdu_market` / 市井分區（spec 保留）
  - `north`: `district_chengdu_scholar` / 學舍分區（spec 保留）
  - `out`: `wild_chengdu_outer` / 成都近郊（spec 保留）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
- `ref/sanguo-area-specfirst/area/wild_chengdu_outer/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_jiangzhou/map.md`
- `plans/area/0111-city-jiangzhou.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
  - `ref/sanguo-area-specfirst/area/wild_chengdu_outer/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_jiangzhou/map.md`
  - `plans/area/0111-city-jiangzhou.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/district_chengdu_market/map.md`
  - `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_jiangzhou` 現有 spec 已保留 `19608 west -> city_chengdu` metadata，代表成都已有成熟的 runtime 主線掛接入口
  - `world-graph` 與 `area/world_map.md` 都把主線寫成 `成都 -> 江州 -> 永安 -> 江陵`，若先跳去 `wild_chengdu_outer` 反而會繞過都城母區與直接主線掛點
  - `wild_chengdu_outer` 雖可提供 family variety，但目前只有 `enter -> city_chengdu` 的 scaffold，缺少與現行 runtime 直接對接的成熟邊界 stub
  - `題材分布表` 將成都定位成蜀漢首都，支持在上游港城之後收束回更厚重的都城節奏，而不是立刻轉回外郊
- `compliance_check`
  - conditional-but-acceptable；雖然此選擇形成 `City -> City` 連續，理論上不如 non-`City` variety 理想，但在 `world_map + progression + 題材分布表 + players/skills + current runtime stub` 共同檢查後，`city_chengdu` 是目前唯一既符合主線位置、又能直接落地 runtime boundary 的候選，因此作為 queue variety gate 的例外前進

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_chengdu/map.md` 與 `area/city_jiangzhou/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `city_chengdu` 與 `city_jiangzhou` 均通過；正式 `.roo` 生成後已確認 `city_jiangzhou/19608 west <-> city_chengdu/19701 east` 雙向邊界一致
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py city_chengdu` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版 runtime 房間落在 `19701-19708`
- 已正式落成 runtime boundary：`city_jiangzhou/19608 west -> city_chengdu/19701` 與 `city_chengdu/19701 east -> city_jiangzhou/19608`
- `district_chengdu_market`、`district_chengdu_scholar`、`wild_chengdu_outer` 目前仍維持在 `map.md` / `plan` / `tracker` 的 spec 預留，不提前建立假外連
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`
- smoke 初次載入曾抓到 `區域 成都 的首都 1 不存在`；已將 `area/city_chengdu/index` 的 `Capital` 修正為 loader 一致使用的 `0`

## Next Step Prompt

`提交 city_chengdu implementation milestone，然後把 tracker 從 in_progress 推進成 done。`
