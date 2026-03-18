# Sec Rift Spirit Core Blank Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_blank`。此區承接 `sec_rift_spirit_core_zero` 最深的裂魄零界座，讓地下鏈進一步沉入裂魄空白與空白深井，作為更深失序白界層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄空白 / 空白深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_zero` 既有 `down` 延伸意圖，讓零界深井正式過渡到更深的空白層
- reserved_room_block: `11601-11620`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0031-sec-rift-spirit-core-blank.md` 與 `area/sec_rift_spirit_core_blank/map.md` 第一版
- 以 `mapmd-json` 定義空白落座、空白內庭、失序偏廊與白界前座
- 明確標示與 `sec_rift_spirit_core_zero/11512` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11601-11612` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_blank` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_zero/11512` 與 `sec_rift_spirit_core_blank/11601` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_zero` room `11512`
- `down`: 通往未來更深層裂魄白界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_zero/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`（本輪僅確認無更高優先的城鎮服務鏈候選，未直接參與地下鏈題材決策）
  - `docs/3yWebsite/docs/data/skills.json`（本輪僅確認無更高優先的技能服務鏈候選，未直接參與地下鏈題材決策）
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_spirit_core_zero/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_spirit_core_zero` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的 area rebuild 範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11601-11620`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_blank/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_blank/map.md --validate-only`
  - passed

## Next Step Prompt

`sec_rift_spirit_core_blank` 已完成 spec；下一步續做第一輪 runtime implementation，補齊最小 area data、`area/directory.lst` 與 `11512 <-> 11601` 邊界。
