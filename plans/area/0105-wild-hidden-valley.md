# Hidden Valley Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_hidden_valley`。此區承接 `wild_wuling` 的隱谷西徑，把武陵山西側原本只存在於深山岔徑與獵戶傳聞裡的谷地正式落成為可載入 wild。它不該只是再加一段「更深的山路」，而要讓玩家明顯感到自己從高山主徑滑進一塊地勢更收、痕跡更古、也更像通往失落地底入口前帶的隱谷。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `隱谷 / 秘徑`
- experience_type: `Wild`
- player_loop_focus: `谷地辨位 / 支線探索 / 失蹤傳聞 / 古陵入口前帶`
- contrast_with_previous_two:
  - 相對於 `sec_spirit_peak` 的高處祭天祕境與 `sec_starfall_crater` 的墜星異坑，`wild_hidden_valley` 應把節奏拉回更可行走、可辨位、也更像「深山主世界支線」的探險 wild，而不是繼續堆高處異象與 secret 壓力。
- 世界缺口角色：
  - 把 `wild_wuling/15010` 的 `west` 預留正式轉成隱谷支線節點
  - 為後續 `dng_ancient_tomb_shu` 提供穩定的上層地表入口前帶
- reserved_room_block: `19001-19020`
- planned_vnum_range: `19001-19020`
- level_range: `44-58`
- external_links:
  - `east`: `wild_wuling` / 隱谷西徑
  - `down`: `dng_ancient_tomb_shu` / 沉陵坳口（先保留 spec link）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_hidden_valley/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0067-wild-wuling.md`
- `plans/area/0103-sec-spirit-peak.md`
- `plans/area/0104-sec-starfall-crater.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_hidden_valley/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0067-wild-wuling.md`
  - `plans/area/0103-sec-spirit-peak.md`
  - `plans/area/0104-sec-starfall-crater.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/chendo.html`
  - `ref/sanguo-area-specfirst/area/wild_spirit_forest/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_wuling` 現有 spec/runtime 已保留 `15010 west -> wild_hidden_valley` metadata，表示它是蜀漢西山鏈最直接也最低摩擦的下一個未落地節點
  - `world-graph` 將 `wild_hidden_valley` 放在 `wild_wuling` 之後，並預留往 `dng_ancient_tomb_shu` 的下探可能，適合拿來當高段蜀地探索鏈的新入口
  - `題材分布表` 對蜀漢區保留 `仙俠 / 探險` 的山區配置空間，支持把武陵山之後的下一段節奏做成更偏隱谷與古痕的 `Wild`，而不是再接一個 `Secret`
  - `players.json / skills.json` 對這段蜀地高段區沒有提出比既有 world link 更強的城市服務優先訊號，支持先利用現成山區母點展開新 wild 支線
- `compliance_check`
  - compliant；在連續兩個北境 `Secret` 之後切回 `Wild`，而且直接承接已存在的 `wild_wuling` 預留 world link，符合 queue variety 與既有拓樸約束

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_hidden_valley/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_hidden_valley/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_hidden_valley/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/wild_hidden_valley/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true'`
  - passed direct smoke; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_hidden_valley`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `19001-19008`、mob vnum `21431-21434`、obj vnum `21451-21454`
- 已正式落成 runtime boundary：`wild_wuling/15010 west -> wild_hidden_valley/19001` 與 `wild_hidden_valley/19001 east -> wild_wuling/15010`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_hidden_valley`
- smoke test 後 `debug/error` 僅反映 timeout 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `wild_hidden_valley` 相關 loader blocker

## Next Step Prompt

`先 commit wild_hidden_valley 的 implementation milestone：包含 wild_wuling/15010 <-> wild_hidden_valley/19001 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個 area。`
