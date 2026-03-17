# Sec Rift Core Below Deeps Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_core_below_deeps`。此區承接 `sec_rift_core_below` 最底端裂核底脈臺，將地下鏈推進到更深層「底脈渦腹」地帶，作為後續極深層裂核區前的第二段承接層。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂核深層 / 底脈渦腹`
- 世界缺口角色：補上 `sec_rift_core_below` 既有 `down` 延伸意圖，讓深井探索從過渡層進入高壓渦腹環境
- reserved_room_block: `10401-10420`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0019-sec-rift-core-below-deeps.md` 與 `area/sec_rift_core_below_deeps/map.md` 第一版
- 以 `mapmd-json` 定義入脈落臺、渦腹主脈、鎮紋旁廊與底潮封口
- 明確標示與 `sec_rift_core_below/10312` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10401-10412` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_core_below_deeps` 掛入 `area/directory.lst`
- 讓 `sec_rift_core_below/10312` 與 `sec_rift_core_below_deeps/10401` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_core_below` room `10312`
- `down`: 通往未來更深層裂核渦核區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_core_below/map.md`
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
  - `area/sec_rift_core_below/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_core_below` 的既有向下意圖落地為可載入新區，維持 spec-first 與單區里程碑流程

## Validation Results

- `python3 tools/mapmd_validate.py area/sec_rift_core_below_deeps/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_below_deeps/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_below_deeps/map.md`
  - passed and wrote `roo/10401-10412.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_core_below_deeps`
- `area/sec_rift_core_below/roo/10312.roo` 已補上 down 出口到 `10401`

## Next Step Prompt

`繼續為 sec_rift_core_below_deeps 之下的更深裂核渦核區建立下一段單區 plan 與 map.md spec。`
