# Fort Yongan Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_yongan`。此區承接 `fort_yiling` 西向關坪，把蜀荊咽喉再往西推成更厚、更偏內陸堡寨節奏的永安險關。它雖然會形成一次少見的 `Fort -> Fort` 連續，但在目前 runtime 現況下，它是唯一已具成熟掛接 stub、又能把蜀漢主線從邊界關隘再往上游城帶穩定推進的下一步。

## Theme Positioning

- theme: `軍旅`
- subtheme: `險關 / 堡壘`
- experience_type: `Fort`
- player_loop_focus: `盤關 / 軍令 / 軍械補給 / 堡門轉接 / 上游前導`
- contrast_with_previous_two:
  - 相對於 `city_jiangling` 的主城秩序與 `fort_yiling` 的咽喉壓力，`fort_yongan` 應把節奏從邊界關門再推成更內縮、更厚重的蜀漢堡寨軍務空間。
- 世界缺口角色：
  - 把 `fort_yiling/19408` 的西向關坪正式轉成 `fort_yongan` 的東向堡前入口
  - 為後續 `city_jiangzhou` 建立蜀漢上游城帶的軍事前口與西向掛接點
- reserved_room_block: `19501-19520`
- planned_vnum_range: `19501-19520`
- level_range: `40-54`
- external_links:
  - `east`: `fort_yiling` / 西向關坪
  - `west`: `city_jiangzhou` / 上游城路（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_yongan/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/fort_yiling/map.md`
- `plans/area/0109-fort-yiling.md`
- `ref/sanguo-area-specfirst/area/city_jiangzhou/map.md`
- `ref/sanguo-area-specfirst/area/city_chengdu/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_yongan/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/fort_yiling/map.md`
  - `plans/area/0109-fort-yiling.md`
  - `ref/sanguo-area-specfirst/area/city_jiangzhou/map.md`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
- `ref_inputs_deferred`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `fort_yiling` 已把 `19408` 明確塑造成西向關坪，代表 `fort_yongan` 已有成熟的 runtime 掛接入口，而不是純抽象 world link
  - `world-graph` 將 `fort_yongan` 放在 `city_jiangzhou` 與 `fort_yiling` 之間，是蜀漢上游城帶前的最後一段軍事收束層
  - `題材分布表` 把永安定位成更偏內陸堡壘式的軍旅節點，能和 `fort_yiling` 的邊界咽喉形成同 family 內的次題材差異
  - `players.json / skills.json` 沒有提供另一個同等成熟的蜀漢非 `Fort` runtime 掛接點；`city_jiangzhou` 與 `city_chengdu` 雖有 scaffold，但目前都缺少可直接銜接現行 runtime 的邊界 stub
- `compliance_check`
  - conditional-but-acceptable；雖然此選擇形成 `Fort -> Fort` 連續，理論上不如 non-`Fort` variety 理想，但在 `world_map + progression + 題材分布表 + players/skills + current runtime stub` 共同檢查後，`fort_yongan` 是目前唯一既符合主線位置、又能直接落地 runtime boundary 的候選，因此作為 queue variety gate 的例外前進

## Validation Results

- `2026-03-29` `python -X utf8 tools/mapmd_validate.py area/fort_yongan/map.md`
  - `Validated 8 room(s)`，`0 error(s), 0 warning(s)`
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yongan/map.md --validate-only`
  - validation succeeded for `8` rooms
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yongan/map.md`
  - 實際生成 `area/fort_yongan/roo/19501-19508.roo`
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
- `2026-03-29` `python -X utf8 tools/area_acceptance_gate.py fort_yongan`
  - 回報 `Recommended gate: implementation_ready_for_commit`
  - 腳本附註 `no log/debug evidence supplied`，此處已補記本輪實際 smoke / debug evidence

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `19501-19508`
- 已正式落成 runtime boundary：`fort_yiling/19408 west -> fort_yongan/19501` 與 `fort_yongan/19501 east -> fort_yiling/19408`
- `city_jiangzhou` 方向維持在 `map.md` / `plan` / `tracker` 的 spec 預留，不提前建立假外連
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 fort_yongan implementation milestone commit：內容包含 fort_yiling/19408 <-> fort_yongan/19501 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
