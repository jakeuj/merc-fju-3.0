# City Jiangzhou Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_jiangzhou`。此區承接 `fort_yongan` 西嶺堡口，把原本還停在堡牆、上游山路與遠行想像裡的蜀中前帶，正式收束回一座有城門、市街、州府與貨旅節奏的上游港城。它不該只是永安後的放鬆段，而要讓玩家明顯感到軍旅壓力在這裡被重新翻譯成補給、問路、告示與西向官道分流的城市秩序。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `上游港城 / 蜀中轉運`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 城市情報 / 東關轉入 / 西向成都前導`
- contrast_with_previous_two:
  - 相對於 `fort_yiling` 的咽喉關道與 `fort_yongan` 的內層堡寨壓力，`city_jiangzhou` 應把軍旅節奏重新收回到有市聲、榜示、州府與行旅停靠點的城市秩序。
- 世界缺口角色：
  - 把 `fort_yongan/19508` 的上游堡口正式轉成 `city_jiangzhou` 的東向城門入口
  - 為後續 `city_chengdu` 建立蜀地主線西向母城與官道掛接點
- reserved_room_block: `19601-19620`
- planned_vnum_range: `19601-19620`
- level_range: `36-50`
- external_links:
  - `east`: `fort_yongan` / 東嶺堡路
  - `west`: `city_chengdu` / 西向官道（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_jiangzhou/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/fort_yongan/map.md`
- `plans/area/0110-fort-yongan.md`
- `ref/sanguo-area-specfirst/area/city_chengdu/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_jiangzhou/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/fort_yongan/map.md`
  - `plans/area/0110-fort-yongan.md`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/chendo.html`
  - `ref/sanguo-area-specfirst/area/district_chengdu_market/map.md`
  - `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `fort_yongan` 現有 spec 已保留 `19508 west -> city_jiangzhou` metadata，且本輪之前已把 `19508` 穩定成上游城路前口，代表江州已有成熟的 runtime 掛接入口
  - `world-graph` 將 `city_jiangzhou` 放在 `city_chengdu` 與 `fort_yongan` 之間，提供 `Fort -> City` 的 family 切換，也替後續蜀都母城建立更自然的東向支點
  - `題材分布表` 將江州定位成蜀漢區的 `歷史 / 軍旅` 上游城市，適合把永安的堡寨壓力轉成交通、補給與地方秩序
  - `players.json / skills.json` 雖未直接給出江州專屬 teacher，但整體玩法訊號仍偏向中段主線需要穩定的城市服務 loop，而不是再連續堆一個軍事關口
- `compliance_check`
  - compliant；這輪不是機械沿 `fort_yongan` 預留 link 續寫，而是在 `world_map + progression + 題材分布表 + players/skills + current runtime stub` 共同檢查後，確認 `city_jiangzhou` 同時滿足 family variety、主線位置與掛接成熟度

## Validation Results

- `2026-03-29` `python -X utf8 tools/mapmd_validate.py area/city_jiangzhou/map.md`
  - `Validated 8 room(s)`，`0 error(s), 0 warning(s)`
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangzhou/map.md --validate-only`
  - validation succeeded for `8` rooms
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangzhou/map.md`
  - 實際生成 `area/city_jiangzhou/roo/19601-19608.roo`
- `2026-03-29` `python -X utf8 tools/mapmd_validate.py area/fort_yongan/map.md`
  - 因西向 boundary 補上 `19601` 而重新驗證，`Validated 8 room(s)`，`0 error(s), 0 warning(s)`
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yongan/map.md --validate-only`
  - validation succeeded for `8` rooms
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yongan/map.md`
  - 重新生成 `area/fort_yongan/roo/19501-19508.roo`，讓 `19508 west -> 19601` 正式落地
- `2026-03-29` `python -m json.tool docs/current-game/areas.json`
  - JSON registry 格式正常
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc"`
  - WSL Linux `Makefile.lin` build 成功，未出現新的 warning / link error
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true"`
  - stdout 明確出現 `三國歪傳之降龍伏虎開始正常運作`
  - 本輪 direct smoke 仍未額外產生新的 `log/*`；成功訊號以 stdout 與 debug 檢查為準
  - `debug/error` 只有 timeout 關機造成的 `系統臨界錯誤`
  - `debug/failexit` 只有既有 baseline `17201/17208` `Fix_exits`
  - `debug/badobject` 在修正 `21724.obj` weapon value / wearloc 後已為空
- `2026-03-29` `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py city_jiangzhou`
  - 回報 `Recommended gate: implementation_ready_for_commit`
  - 腳本附註 `no log/debug evidence supplied`，此處已補記本輪實際 smoke / debug evidence

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `19601-19608`
- 已正式落成 runtime boundary：`fort_yongan/19508 west -> city_jiangzhou/19601` 與 `city_jiangzhou/19601 east -> fort_yongan/19508`
- `city_chengdu` 方向維持在 `map.md` / `plan` / `tracker` 的 spec 預留，不提前建立假外連
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 city_jiangzhou implementation milestone：內容包含 fort_yongan/19508 <-> city_jiangzhou/19601 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
