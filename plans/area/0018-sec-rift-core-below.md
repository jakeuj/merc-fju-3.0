# Sec Rift Core Below Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_core_below`。此區承接 `sec_rift_true_core` 核心臺深井下方，作為「裂核下層通道」首版，讓地下鏈從本核外環正式進入更危險的深井內核。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂核下層 / 深井脈道`
- 世界缺口角色：補上 `sec_rift_true_core` 既有 `down` stub，使本核之下有可載入、可維運、可繼續延伸的深井過渡層
- reserved_room_block: `10301-10320`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0018-sec-rift-core-below.md` 與 `area/sec_rift_core_below/map.md` 第一版
- 以 `mapmd-json` 定義落井接臺、深井裂道、導脈側廊與下層封橋
- 明確標示與 `sec_rift_true_core/10212` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10301-10312` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_core_below` 掛入 `area/directory.lst`
- 讓 `sec_rift_true_core/10212` 與 `sec_rift_core_below/10301` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_true_core` room `10212`
- `down`: 通往未來更深層裂核區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_true_core/map.md`
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
  - `area/sec_rift_true_core/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_true_core` 的既有向下 world link 延伸，僅補齊 spec-first 與 runtime 可載入里程碑

## Validation Results

- `python3 tools/mapmd_validate.py area/sec_rift_core_below/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_below/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_below/map.md`
  - passed and wrote `roo/10301-10312.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_core_below`
- `area/sec_rift_true_core/roo/10212.roo` 已補上 down 出口到 `10301`

## Next Step Prompt

`繼續為 sec_rift_core_below 之下的更深裂核區建立下一段單區 plan 與 map.md spec。`
