# Sec Rift Spirit Core Stygian Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_stygian`。此區承接 `sec_rift_spirit_core_nether` 最深的裂魄冥界座，讓地下鏈再往下沉入裂魄玄冥與玄冥井腹，作為後續同級更硬「幽玄」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄玄冥 / 玄冥井腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_nether` 既有 `down` 延伸意圖，讓冥界井腹正式過渡到更深的玄冥層
- reserved_room_block: `13201-13220`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更深沉的陰冥壓迫、玄冥前橋與井腹守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0047-sec-rift-spirit-core-stygian.md` 與 `area/sec_rift_spirit_core_stygian/map.md` 第一版
- 以 `mapmd-json` 定義玄冥落座、玄冥內庭、玄幽偏廊與玄冥前座
- 明確標示與 `sec_rift_spirit_core_nether/13112` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/13201-13212` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_stygian` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_nether/13112` 與 `sec_rift_spirit_core_stygian/13201` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_stygian/index`
- `area/sec_rift_spirit_core_stygian/mob/14201.mob`
- `area/sec_rift_spirit_core_stygian/mob/14202.mob`
- `area/sec_rift_spirit_core_stygian/mob/14203.mob`
- `area/sec_rift_spirit_core_stygian/obj/14251.obj`
- `area/sec_rift_spirit_core_stygian/obj/14252.obj`
- `area/sec_rift_spirit_core_stygian/obj/14253.obj`
- `area/sec_rift_spirit_core_stygian/obj/14254.obj`
- `area/sec_rift_spirit_core_stygian/res/core.res`
- `area/sec_rift_spirit_core_stygian/shp/guide.shp`
- `area/sec_rift_spirit_core_stygian/roo/13201-13212`
- `area/sec_rift_spirit_core_nether/roo/13112.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_nether` room `13112`
- `down`: 通往未來更深層裂魄幽玄區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_nether/map.md`
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
  - `area/sec_rift_spirit_core_nether/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_nether` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `13301-13320` after the current spec had already reserved `13201-13220`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_stygian/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_stygian/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_stygian/map.md`
  - passed and wrote `roo/13201-13212`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py log/1055.log`
  - `log/1055.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - no non-empty `debug/*` files were observed after the smoke test
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1055.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, with no new area-specific loader/debug issue observed

## Next Step Prompt

`sec_rift_spirit_core_stygian` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。`
