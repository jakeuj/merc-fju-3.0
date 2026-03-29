# Ancient Tomb Shu Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_ancient_tomb_shu`。此區承接 `wild_hidden_valley` 的沉陵坳口，把蜀地深谷裡原本只剩地勢暗示與獵戶傳聞的古陵入口正式落成為可載入 dungeon。它不該只是再做一段「谷底往下」，而要讓玩家明顯感到自己從可辨位的山谷地表切進一處更封閉、更人工、也更帶石門與封紋壓力的古墓前帶。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `古墓 / 石門`
- experience_type: `Dungeon`
- player_loop_focus: `墓道辨位 / 石門封紋 / 深入調查 / 封印前帶壓力`
- contrast_with_previous_two:
  - 相對於 `sec_starfall_crater` 的高處異象 secret 與 `wild_hidden_valley` 的開放式深谷探索，`dng_ancient_tomb_shu` 應把節奏收束成封閉墓道與石門機關，不再靠大地形與遠景施壓。
- 世界缺口角色：
  - 把 `wild_hidden_valley/19008` 的 `down` 預留正式轉成蜀漢古墓節點
  - 為蜀漢西山鏈建立第一個明確的高段 `Dungeon` family 下探節點
- reserved_room_block: `19101-19120`
- planned_vnum_range: `19101-19120`
- level_range: `48-62`
- external_links:
  - `up`: `wild_hidden_valley` / 沉陵坳口
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_ancient_tomb_shu/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0105-wild-hidden-valley.md`
- `plans/area/0067-wild-wuling.md`
- `plans/area/0104-sec-starfall-crater.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_ancient_tomb_shu/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0105-wild-hidden-valley.md`
  - `plans/area/0067-wild-wuling.md`
  - `plans/area/0104-sec-starfall-crater.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/chendo.html`
  - `ref/sanguo-area-specfirst/area/wild_spirit_forest/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_hidden_valley` 現有 spec 已保留 `19008 down -> dng_ancient_tomb_shu` metadata，表示這個古墓是蜀地深谷鏈最直接也最成熟的下一個下探節點
  - `world-graph` 將 `dng_ancient_tomb_shu` 放在 `wild_hidden_valley` 之後，提供 `Wild -> Dungeon` 的自然 family 切換，不必再回到平面山林
  - `題材分布表` 對蜀漢區保留 `探險遺跡` 與 `仙俠` 疊合的深山空間，支持把谷底陰口正式翻成古墓石門 dungeon
  - `players.json / skills.json` 對蜀地高段區沒有提出比既有谷底預留 link 更強的城市服務優先訊號，支持先展開墓道調查鏈
- `compliance_check`
  - compliant；在 `Wild` 之後切到 `Dungeon`，而且直接承接已存在的 `wild_hidden_valley` 下探口，符合 queue variety 與既有拓樸約束

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_ancient_tomb_shu/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_ancient_tomb_shu/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_ancient_tomb_shu/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/dng_ancient_tomb_shu/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true'`
  - passed direct smoke; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py dng_ancient_tomb_shu`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `19101-19108`、mob vnum `21531-21534`、obj vnum `21551-21554`
- 已正式落成 runtime boundary：`wild_hidden_valley/19008 down -> dng_ancient_tomb_shu/19101` 與 `dng_ancient_tomb_shu/19101 up -> wild_hidden_valley/19008`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `dng_ancient_tomb_shu`
- smoke test 後 `debug/error` 僅反映 timeout 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `dng_ancient_tomb_shu` 相關 loader blocker

## Next Step Prompt

`先 commit dng_ancient_tomb_shu 的 implementation milestone：包含 wild_hidden_valley/19008 <-> dng_ancient_tomb_shu/19101 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個 area。`
