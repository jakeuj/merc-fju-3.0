# Sec Rift Spirit Core Final Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_final`。此區承接 `sec_rift_spirit_core_last` 最深的裂魄末界座，讓地下鏈再往下沉入裂魄終界與終界井腹，作為後續同級更硬「絕界」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄終界 / 終界井腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_last` 既有 `down` 延伸意圖，讓末界深井正式過渡到更深的終界層
- reserved_room_block: `12401-12420`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更終極的歸盡壓迫、終核前橋與井心守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0039-sec-rift-spirit-core-final.md` 與 `area/sec_rift_spirit_core_final/map.md` 第一版
- 以 `mapmd-json` 定義終界落座、終界內庭、極終偏廊與終核前座
- 明確標示與 `sec_rift_spirit_core_last/12312` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/12401-12412` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_final` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_last/12312` 與 `sec_rift_spirit_core_final/12401` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_final/index`
- `area/sec_rift_spirit_core_final/mob/13401.mob`
- `area/sec_rift_spirit_core_final/mob/13402.mob`
- `area/sec_rift_spirit_core_final/mob/13403.mob`
- `area/sec_rift_spirit_core_final/obj/13451.obj`
- `area/sec_rift_spirit_core_final/obj/13452.obj`
- `area/sec_rift_spirit_core_final/obj/13453.obj`
- `area/sec_rift_spirit_core_final/obj/13454.obj`
- `area/sec_rift_spirit_core_final/res/core.res`
- `area/sec_rift_spirit_core_final/shp/guide.shp`
- `area/sec_rift_spirit_core_final/roo/12401.roo` to `area/sec_rift_spirit_core_final/roo/12412.roo`
- `area/sec_rift_spirit_core_last/roo/12312.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_last` room `12312`
- `down`: 通往未來更深層裂魄絕界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_last/map.md`
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
  - `area/sec_rift_spirit_core_last/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_last` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `12401-12420`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_final/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_final/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_final/map.md`
  - passed and wrote `roo/12401-12412`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py`
  - `log/1047.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - `debug/error` only recorded the expected timeout shutdown footer; no new area-specific loader/debug issue was observed
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1047.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, which produced the expected shutdown footer in the log

## Next Step Prompt

`sec_rift_spirit_core_final` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。
