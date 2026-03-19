# Sec Rift Spirit Core Abysmal Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_abysmal`。此區承接 `sec_rift_spirit_core_chthonic` 最深的裂魄幽玄座，讓地下鏈再往下沉入裂魄玄幽與玄幽井腹，作為後續同級更硬「冥淵」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄玄幽 / 玄幽井腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_chthonic` 既有 `down` 延伸意圖，讓幽玄井腹正式過渡到更深的玄幽層
- reserved_room_block: `13401-13420`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更深沉的幽寂壓迫、玄幽前橋與井腹守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0049-sec-rift-spirit-core-abysmal.md` 與 `area/sec_rift_spirit_core_abysmal/map.md` 第一版
- 以 `mapmd-json` 定義玄幽落座、玄幽內庭、幽冥偏廊與玄幽前座
- 明確標示與 `sec_rift_spirit_core_chthonic/13312` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/13401-13412` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_abysmal` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_chthonic/13312` 與 `sec_rift_spirit_core_abysmal/13401` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_abysmal/index`
- `area/sec_rift_spirit_core_abysmal/mob/14401.mob`
- `area/sec_rift_spirit_core_abysmal/mob/14402.mob`
- `area/sec_rift_spirit_core_abysmal/mob/14403.mob`
- `area/sec_rift_spirit_core_abysmal/obj/14451.obj`
- `area/sec_rift_spirit_core_abysmal/obj/14452.obj`
- `area/sec_rift_spirit_core_abysmal/obj/14453.obj`
- `area/sec_rift_spirit_core_abysmal/obj/14454.obj`
- `area/sec_rift_spirit_core_abysmal/res/core.res`
- `area/sec_rift_spirit_core_abysmal/shp/guide.shp`
- `area/sec_rift_spirit_core_abysmal/roo/13401-13412`
- `area/sec_rift_spirit_core_chthonic/roo/13312.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_chthonic` room `13312`
- `down`: 通往未來更深層裂魄冥淵區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_chthonic/map.md`
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
  - `area/sec_rift_spirit_core_chthonic/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_chthonic` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `13501-13520` after the current spec had already reserved `13401-13420`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_abysmal/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_abysmal/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_abysmal/map.md`
  - passed and wrote `roo/13401-13412`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py log/1057.log`
  - `log/1057.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - no non-empty `debug/*` files were observed after the smoke test
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1057.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, with no new area-specific loader/debug issue observed
## Next Step Prompt

`sec_rift_spirit_core_abysmal` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。`
