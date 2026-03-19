# Sec Rift Spirit Core Last Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_last`。此區承接 `sec_rift_spirit_core_grain` 最深的裂魄粒界座，讓地下鏈再往下沉入裂魄末界與末界深井，作為後續同級更硬「終界」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄末界 / 末界深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_grain` 既有 `down` 延伸意圖，讓粒界深井正式過渡到更深的末界層
- reserved_room_block: `12301-12320`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更末細的終塵偏廊、終界前橋與井緣守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0038-sec-rift-spirit-core-last.md` 與 `area/sec_rift_spirit_core_last/map.md` 第一版
- 以 `mapmd-json` 定義末界落座、末界內庭、終塵偏廊與終界前座
- 明確標示與 `sec_rift_spirit_core_grain/12212` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/12301-12312` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_last` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_grain/12212` 與 `sec_rift_spirit_core_last/12301` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_last/index`
- `area/sec_rift_spirit_core_last/mob/13301.mob`
- `area/sec_rift_spirit_core_last/mob/13302.mob`
- `area/sec_rift_spirit_core_last/mob/13303.mob`
- `area/sec_rift_spirit_core_last/obj/13351.obj`
- `area/sec_rift_spirit_core_last/obj/13352.obj`
- `area/sec_rift_spirit_core_last/obj/13353.obj`
- `area/sec_rift_spirit_core_last/obj/13354.obj`
- `area/sec_rift_spirit_core_last/res/core.res`
- `area/sec_rift_spirit_core_last/shp/guide.shp`
- `area/sec_rift_spirit_core_last/roo/12301.roo` to `area/sec_rift_spirit_core_last/roo/12312.roo`
- `area/sec_rift_spirit_core_grain/roo/12212.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_grain` room `12212`
- `down`: 通往未來更深層裂魄終界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_grain/map.md`
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
  - `area/sec_rift_spirit_core_grain/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_grain` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `12301-12320`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_last/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_last/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_last/map.md`
  - passed and wrote `roo/12301-12312`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py`
  - `log/1046.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - `debug/error` only recorded the expected timeout shutdown footer; no new area-specific loader/debug issue was observed
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1046.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, which produced the expected shutdown footer in the log

## Next Step Prompt

`sec_rift_spirit_core_last` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。
