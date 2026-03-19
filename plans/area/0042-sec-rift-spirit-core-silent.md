# Sec Rift Spirit Core Silent Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_silent`。此區承接 `sec_rift_spirit_core_extinct` 最深的裂魄滅界座，讓地下鏈再往下沉入裂魄寂界與寂界井腹，作為後續同級更硬「寥界」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄寂界 / 寂界井腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_extinct` 既有 `down` 延伸意圖，讓滅界井腹正式過渡到更深的寂界層
- reserved_room_block: `12701-12720`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更徹底的靜寂壓迫、寥核前橋與井腹守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0042-sec-rift-spirit-core-silent.md` 與 `area/sec_rift_spirit_core_silent/map.md` 第一版
- 以 `mapmd-json` 定義寂界落座、寂界內庭、寥寂偏廊與寥核前座
- 明確標示與 `sec_rift_spirit_core_extinct/12612` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/12701-12712` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_silent` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_extinct/12612` 與 `sec_rift_spirit_core_silent/12701` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_silent/index`
- `area/sec_rift_spirit_core_silent/mob/13701.mob`
- `area/sec_rift_spirit_core_silent/mob/13702.mob`
- `area/sec_rift_spirit_core_silent/mob/13703.mob`
- `area/sec_rift_spirit_core_silent/obj/13751.obj`
- `area/sec_rift_spirit_core_silent/obj/13752.obj`
- `area/sec_rift_spirit_core_silent/obj/13753.obj`
- `area/sec_rift_spirit_core_silent/obj/13754.obj`
- `area/sec_rift_spirit_core_silent/res/core.res`
- `area/sec_rift_spirit_core_silent/shp/guide.shp`
- `area/sec_rift_spirit_core_silent/roo/12701-12712`
- `area/sec_rift_spirit_core_extinct/roo/12612.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_extinct` room `12612`
- `down`: 通往未來更深層裂魄寥界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_extinct/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `ref_inputs_deferred`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_spirit_core_extinct/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_extinct` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `12701-12720`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_silent/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_silent/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_silent/map.md`
  - passed and wrote `roo/12701-12712`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py`
  - `log/1050.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - `debug/error` only recorded the expected timeout shutdown footer; no new area-specific loader/debug issue was observed
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1050.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, which produced the expected shutdown footer in the log

## Next Step Prompt

`sec_rift_spirit_core_silent` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。
