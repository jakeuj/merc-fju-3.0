# Sec Rift Spirit Core Vacuum Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_vacuum`。此區承接 `sec_rift_spirit_core_void` 最深的裂魄虛座，讓地下鏈進一步沉入裂魄真空與真空深腹，作為更深歸零層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄真空 / 真空深腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_void` 既有 `down` 延伸意圖，讓虛腹暗層正式過渡到更深的真空層
- reserved_room_block: `11301-11320`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0028-sec-rift-spirit-core-vacuum.md` 與 `area/sec_rift_spirit_core_vacuum/map.md` 第一版
- 以 `mapmd-json` 定義真空落臺、真空環脈、滅響偏廊與歸零前座
- 明確標示與 `sec_rift_spirit_core_void/11212` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11301-11312` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_vacuum` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_void/11212` 與 `sec_rift_spirit_core_vacuum/11301` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_void` room `11212`
- `down`: 通往未來更深層裂魄歸零區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_void/map.md`
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
  - `area/sec_rift_spirit_core_void/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_spirit_core_void` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的 area rebuild 範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11301-11320`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_vacuum/map.md`
  - pending
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_vacuum/map.md --validate-only`
  - pending

## Next Step Prompt

`sec_rift_spirit_core_vacuum` 已完成 spec；下一步續做第一輪 runtime implementation，補齊最小 area data、`area/directory.lst` 與 `11212 <-> 11301` 邊界。
