# Spirit Peak Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_spirit_peak`。此區承接 `dng_ancient_cave` 的靈峰裂井，把白狼山地下遺跡再往上翻成一段更稀有、更明亮、也更帶祭天與異象壓力的高處 secret。這裡不應只是古洞上方再多一個井口出口，而是一處會讓玩家明顯感到自己從濕冷封印洞窟跨進了另一種帶光紋、祭壇與天象回聲的北境祕境。

## Theme Positioning

- theme: `仙俠`
- subtheme: `靈峰 / 祭天`
- experience_type: `Secret`
- player_loop_focus: `異象辨位 / 高處探索 / 祭壇傳聞 / 稀有祕境節點`
- contrast_with_previous_two:
  - 相對於 `fort_northern_watch` 的軍旅高處戒備與 `wild_wolf_forest` 的封閉深林壓力，`sec_spirit_peak` 應把體驗轉成更垂直、更稀有、也更帶祭天與異象感的祕境，而不是再延續一般邊地 road / wild 節奏。
- 世界缺口角色：
  - 把 `dng_ancient_cave/18108` 的 `up` 預留正式轉成白狼靈峰節點
  - 為北境鏈建立第一個明確的高處 `Secret` family 祕境母點
- reserved_room_block: `18801-18820`
- planned_vnum_range: `18801-18820`
- level_range: `44-56`
- external_links:
  - `down`: `dng_ancient_cave` / 靈峰裂井
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/sec_spirit_peak/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0096-dng-ancient-cave.md`
- `plans/area/0101-fort-northern-watch.md`
- `plans/area/0102-wild-wolf-forest.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/sec_spirit_peak/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0096-dng-ancient-cave.md`
  - `plans/area/0101-fort-northern-watch.md`
  - `plans/area/0102-wild-wolf-forest.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `dng_ancient_cave` 現有 spec/runtime 已保留 `18108 up -> sec_spirit_peak` metadata，表示它是北境鏈最成熟也最直接的下一個 `Secret` family 母點
  - `world-graph` 將 `sec_spirit_peak` 放在 `dng_ancient_cave` 之後，提供 `Dungeon -> Secret` 的自然 family 切換
  - `題材分布表` 與 ref scaffold 都把此區拉向 `仙俠 / 靈峰 / 祭天`，能和 `wild_wolf_forest` 的 folklore 林壓力形成清楚題材轉折
  - `players.json / skills.json` 對遼東北線仍未提出比既有 reserved link 更強的城市服務優先訊號，支持這時候補上高處祕境而不是再新增一般城鎮節點
- `compliance_check`
  - compliant；在 `Wild` 之後切到 `Secret`，同時承接 `dng_ancient_cave` 的既有 `up` 預留與 queue variety，不是沿最新 surface route 任意外插

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/sec_spirit_peak/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_spirit_peak/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_spirit_peak/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/sec_spirit_peak/roo`)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc'`
  - passed (warning-free WSL Linux build)
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 60s ./startup.bash || true'`
  - passed startup smoke via `log/1075.log`; observed `三國歪傳之降龍伏虎開始正常運作`
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py sec_spirit_peak`
  - returned `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，room vnum `18801-18808`、mob vnum `21231-21234`、obj vnum `21251-21254`
- 已正式落成 runtime boundary：`dng_ancient_cave/18108 up -> sec_spirit_peak/18801` 與 `sec_spirit_peak/18801 down -> dng_ancient_cave/18108`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `sec_spirit_peak`
- smoke test 後 `debug/error` 僅反映 `timeout` 主動中止；`debug/failexit` 僅有既有 baseline `17201/17208` fixups，未見 `sec_spirit_peak` 相關 loader blocker

## Next Step Prompt

`先 commit sec_spirit_peak 的 implementation milestone：包含 dng_ancient_cave/18108 <-> sec_spirit_peak/18801 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新；commit 後再依 queue 規則決定下一個北境節點。`
