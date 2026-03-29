# Starfall Crater Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_starfall_crater`。此區承接 `wild_bailang` 的風蝕石壇，把原本只存在於白狼山高處傳聞中的天象異坑正式落成為可載入 secret。它不該只是再做一個「更高的山頂」，而要讓玩家明顯感到自己踩進一塊被墜星砸穿、光紋與焦黑地貌彼此糾纏的北境異象場。

## Theme Positioning

- theme: `仙俠`
- subtheme: `天坑 / 隕石`
- experience_type: `Secret`
- player_loop_focus: `異象核心辨位 / 高風險祕境探索 / 隕痕傳聞 / 稀有資源節點`
- contrast_with_previous_two:
  - 相對於 `wild_wolf_forest` 的封閉 folklore 深林與 `sec_spirit_peak` 的明亮祭天高處，`sec_starfall_crater` 應轉成更焦灼、更不穩、也更帶墜星異坑感的高風險 secret，而不是再延續單純祭壇或高臺節奏。
- 世界缺口角色：
  - 把 `wild_bailang/18005` 的 `up` 預留正式轉成星墜天坑節點
  - 為北境鏈補上另一個與 `sec_spirit_peak` 明顯不同的 `Secret` family 異象坑洞
- reserved_room_block: `18901-18920`
- planned_vnum_range: `18901-18920`
- level_range: `46-60`
- external_links:
  - `down`: `wild_bailang` / 風蝕石壇
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0095-wild-bailang.md`
- `plans/area/0102-wild-wolf-forest.md`
- `plans/area/0103-sec-spirit-peak.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0095-wild-bailang.md`
  - `plans/area/0102-wild-wolf-forest.md`
  - `plans/area/0103-sec-spirit-peak.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
  - `ref/sanguo-area-specfirst/area/fort_yiling/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_bailang` 的 spec/runtime 已保留 `18005 up -> sec_starfall_crater` metadata，代表這個天坑是目前北境鏈最直接也最低摩擦的下一個未落地節點
  - `world-graph` 已將 `sec_starfall_crater` 列在幽州遼東鏈內，提供 `Wild -> Secret` 的高風險分支，不必再強行回收成一般軍旅或城市節奏
  - `題材分布表` 雖未點名天坑，但北方幽州區仍保留高辨識度異域 / 傳說空間，適合把白狼山高處異象翻成墜星祕境
  - `players.json / skills.json` 對遼東北線的明確服務節點仍集中在襄平，沒有比既有 reserved link 更強的理由要求本輪先切回城市或教學 loop
- `compliance_check`
  - compliant；這次雖然仍是 `Secret`，但最近三個完成區是 `Fort -> Wild -> Secret`，尚未違反連續三個同 family 的 queue variety rule，而且題材已從祭天靈峰切換到墜星異坑

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/sec_starfall_crater/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_starfall_crater/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_starfall_crater/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/sec_starfall_crater/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true' | Set-Content log/1078.log`
  - passed smoke via `log/1078.log`; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py sec_starfall_crater`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `18901-18908`、mob vnum `21331-21334`、obj vnum `21351-21354`
- 已正式落成 runtime boundary：`wild_bailang/18005 up -> sec_starfall_crater/18901` 與 `sec_starfall_crater/18901 down -> wild_bailang/18005`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `sec_starfall_crater`
- smoke test 後 `debug/error` 僅反映 timeout 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `sec_starfall_crater` 相關 loader blocker

## Next Step Prompt

`先 commit sec_starfall_crater 的 implementation milestone：包含 wild_bailang/18005 <-> sec_starfall_crater/18901 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個 area。`
