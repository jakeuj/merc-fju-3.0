# Wild Spirit Forest Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_spirit_forest`。此區承接 `wild_wuling` 山腹下方原本只在 spec 留有「東岔靈林」的側線，把武陵主山道旁那條更靜、更密、也更帶靈木與妖藤氣息的岔路正式落成為可載入 wild。它不該只是再做一段普通山林，而要讓玩家明顯感到自己從可辨位的山腹高徑切進一處更會誤導方向、更會吞掉聲音、也更像把人慢慢引離主路秩序的靈林支帶。

## Theme Positioning

- theme: `仙俠`
- subtheme: `靈木 / 妖藤`
- experience_type: `Wild`
- player_loop_focus: `岔路辨位 / 靈木採集 / 支線追查 / 深林風險感`
- contrast_with_previous_two:
  - 相對於 `wild_hidden_valley` 的谷地古痕與 `dng_ancient_tomb_shu` 的封閉石門壓力，`wild_spirit_forest` 應把節奏重新打開回地表 wild，但保留蜀地深山的仙俠與失向感，不再靠墓道或石門製造壓迫。
- 世界缺口角色：
  - 把 `wild_wuling/15012` 的東向靈林岔路正式轉成可載入的靈木森林節點
  - 為蜀漢西山鏈補上一個與 `Dungeon` family 形成對比的高段 `Wild` 側枝
- reserved_room_block: `19201-19220`
- planned_vnum_range: `19201-19220`
- level_range: `42-56`
- external_links:
  - `west`: `wild_wuling` / 東岔靈林
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_spirit_forest/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/wild_wuling/map.md`
- `plans/area/0106-dng-ancient-tomb-shu.md`
- `plans/area/0105-wild-hidden-valley.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_spirit_forest/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/wild_wuling/map.md`
  - `plans/area/0106-dng-ancient-tomb-shu.md`
  - `plans/area/0105-wild-hidden-valley.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
  - `ref/sanguo-area-specfirst/area/fort_yiling/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_wuling` 現有 spec 已保留 `15012 east -> wild_spirit_forest` metadata，表示靈木森林是武陵山支線裡最成熟的直接延伸節點
  - `world-graph` 把 `wild_spirit_forest` 放在 `wild_wuling` 之後，提供 `Dungeon -> Wild` 的 family 切換，不讓蜀地節奏連續往更深地底堆疊
  - `題材分布表` 對蜀漢區明確保留 `武陵` 與 `武陵秘境` 的 `仙俠` / `探險` 疊合空間，支持把這條支線翻成靈木與妖藤主導的深山 wild
  - `players.json / skills.json` 沒有對蜀地高段區提出比現成武陵支線更強的城市服務優先訊號，支持先補齊山林探索 loop
- `compliance_check`
  - compliant；在 `dng_ancient_tomb_shu` 之後切回 `Wild`，而且直接承接已存在的 `wild_wuling` 側枝 world-link，符合 queue variety 與既有拓樸約束

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_spirit_forest/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_spirit_forest/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_spirit_forest/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/wild_spirit_forest/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true'`
  - passed direct smoke; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_spirit_forest`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `19201-19208`、mob vnum `21561-21564`、obj vnum `21581-21584`
- 已正式落成 runtime boundary：`wild_wuling/15012 east -> wild_spirit_forest/19201` 與 `wild_spirit_forest/19201 west -> wild_wuling/15012`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_spirit_forest`
- smoke test 後 `debug/error` 僅反映 timeout 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `wild_spirit_forest` 相關 loader blocker

## Next Step Prompt

`先 commit wild_spirit_forest 的 implementation milestone：包含 wild_wuling/15012 <-> wild_spirit_forest/19201 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個 area。`
