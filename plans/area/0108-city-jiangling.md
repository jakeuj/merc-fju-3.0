# City Jiangling Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_jiangling`。此區承接 `wild_wuling` 北側那段原本只靠舊道與車轍暗示的山關出口，把武陵深山重新收束回一座真正有官署、客棧、盤查與西關去路的荊蜀轉接主城。它不該只是再做一個普通城鎮，而要讓玩家明顯感到自己從蜀地山林脫離後，重新回到秩序、補給與地方消息流動都更密集的主世界節奏。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `荊蜀轉接`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 地方情報 / 山城轉接 / 西關前導`
- contrast_with_previous_two:
  - 相對於 `dng_ancient_tomb_shu` 的封閉石門壓力與 `wild_spirit_forest` 的深山失向感，`city_jiangling` 應把節奏重新收回到有路牌、榜文、客棧與官署的城市秩序。
- 世界缺口角色：
  - 把 `wild_wuling/15011` 的北山關路正式轉成 `city_jiangling` 的南向城門入口
  - 為後續 `fort_yiling` 建立蜀荊交界的城市母城與西關掛接點
- reserved_room_block: `19301-19320`
- planned_vnum_range: `19301-19320`
- level_range: `38-52`
- external_links:
  - `south`: `wild_wuling` / 北山關路
  - `west`: `fort_yiling` / 西關去路（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_jiangling/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/wild_wuling/map.md`
- `plans/area/0107-wild-spirit-forest.md`
- `plans/area/0106-dng-ancient-tomb-shu.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_jiangling/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/wild_wuling/map.md`
  - `plans/area/0107-wild-spirit-forest.md`
  - `plans/area/0106-dng-ancient-tomb-shu.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
  - `ref/sanguo-area-specfirst/area/fort_yiling/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_wuling` 現有 spec 已保留 `15011 north -> city_jiangling` metadata，表示江陵是武陵北出主路上最成熟的城市回收節點
  - `world-graph` 將 `city_jiangling` 放在 `fort_yiling` 與 `wild_wuling` 之間，提供 `Wild -> City` 的 family 切換，也替後續 `fort_yiling` 建立母城支點
  - `題材分布表` 對蜀漢區保留成都 / 江州 / 永安 / 江陵 / 武陵的主線骨架，支持先用 `江陵` 來把山林節奏收束回歷史城市
  - `players.json / skills.json` 雖未對蜀地高段區指出更強的特定服務 NPC，但城市 hub 仍比再做一段山林或先開一座未掛接關隘更能提供 loop variety
- `compliance_check`
  - compliant；雖然上一輪 tracker 舉例是 `city_chengdu` 與 `fort_yiling`，但 `city_jiangling` 同樣屬於非 `Wild` family，且更 actionable，因為它已有 `wild_wuling/15011` 的現成 runtime 邊界 stub 可正式落地

## Validation Results

- `2026-03-29` `python -X utf8 tools/mapmd_validate.py area/city_jiangling/map.md`
  - `Validated 8 room(s)`，`0 error(s), 0 warning(s)`
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangling/map.md --validate-only`
  - validation succeeded for `8` rooms
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangling/map.md`
  - 實際生成 `area/city_jiangling/roo/19301-19308.roo`
- `2026-03-29` `python -m json.tool docs/current-game/areas.json`
  - JSON registry 格式正常
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc"`
  - WSL Linux `Makefile.lin` build 成功，未出現新的 warning / link error
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true"`
  - stdout 明確出現 `三國歪傳之降龍伏虎開始正常運作`
  - 本輪 direct smoke 未額外產生新的 `log/*`；成功訊號以 stdout 與 debug 檢查為準
  - `debug/error` 只有 timeout 關機造成的 `系統臨界錯誤`
  - `debug/failexit` 只有既有 baseline `17201/17208` `Fix_exits`
  - `debug/badobject` 為空
- `2026-03-29` `python -X utf8 tools/area_acceptance_gate.py city_jiangling`
  - 回報 `Recommended gate: implementation_ready_for_commit`
  - 腳本附註 `no log/debug evidence supplied`，此處已補記本輪實際 smoke / debug evidence

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `19301-19308`
- 已正式落成 runtime boundary：`wild_wuling/15011 north -> city_jiangling/19301` 與 `city_jiangling/19301 south -> wild_wuling/15011`
- `fort_yiling` 方向維持在 `map.md` / plan / tracker 的 spec 預留，不提前建立假外連
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 city_jiangling implementation milestone commit：內容包含 wild_wuling/15011 <-> city_jiangling/19301 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
