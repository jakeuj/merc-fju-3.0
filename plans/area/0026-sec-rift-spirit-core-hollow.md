# Sec Rift Spirit Core Hollow Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_hollow`。此區承接 `sec_rift_core_spirit_abyss` 最深的魄核沉座，讓地下鏈進一步沉入魄核空井與空腹暗層，作為更深裂魄空心區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `魄核空井 / 空腹暗層`
- 世界缺口角色：補上 `sec_rift_core_spirit_abyss` 既有 `down` 延伸意圖，讓深井暗層正式過渡到魄核空腹區
- reserved_room_block: `11101-11120`
- level_range: `86-90`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0026-sec-rift-spirit-core-hollow.md` 與 `area/sec_rift_spirit_core_hollow/map.md` 第一版
- 以 `mapmd-json` 定義空井落臺、空腹環脈、失響偏廊與裂魄前座
- 明確標示與 `sec_rift_core_spirit_abyss/11012` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11101-11112` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_hollow` 掛入 `area/directory.lst`
- 讓 `sec_rift_core_spirit_abyss/11012` 與 `sec_rift_spirit_core_hollow/11101` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_core_spirit_abyss` room `11012`
- `down`: 通往未來更深層裂魄空心區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_core_spirit_abyss/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`（repo 目前不存在，僅保留追蹤需求）
  - `docs/3yWebsite/docs/data/skills.json`（repo 目前不存在，僅保留追蹤需求）
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_core_spirit_abyss/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_core_spirit_abyss` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的規劃範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11101-11120`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_hollow/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_hollow/map.md --validate-only`
  - passed
- `git commit -m "Add sec_rift_spirit_core_hollow spec"`
  - committed as `766d1b7`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)`; only existing legacy / disconnected-area warnings remained
- `make -C src -f Makefile.lin merc`
  - passed
- `timeout 50 ./startup.bash`
  - reached success signal `三國歪傳之降龍伏虎開始正常運作.` in `log/1040.log`
  - `debug/*` remained empty after the run, including `badobject`、`bugs`、`failenable`、`failload`
- `python -X utf8 tools/log_parse_summary.py`
  - reported startup success signal for `log/1040.log` and `0` non-empty debug files
- `python -X utf8 tools/area_acceptance_gate.py sec_rift_spirit_core_hollow`
  - recommended `implementation_ready_for_commit`
- `git commit -m "Add sec_rift_spirit_core_hollow area"`
  - committed as `813fb02`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- `area/directory.lst` 已加入 `sec_rift_spirit_core_hollow`
- `area/sec_rift_core_spirit_abyss/roo/11012.roo` 已補上 `down -> 11101` 邊界出口
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步新的 runtime area 台帳
- 本輪 smoke test 未觀察到新的 area loader / object / enable 警告

## Next Step Prompt

`sec_rift_spirit_core_hollow` implementation milestone 已提交；下一步續做 `sec_rift_spirit_core_void` 的第一輪 runtime implementation。
