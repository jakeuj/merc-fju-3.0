# Sec Rift True Core Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_true_core`。此區承接 `sec_rift_underseal_dais` 最深縱井下方，讓玩家正式進入裂界本核。第一版定位為「本核外環與核心井場」：從失穩封圈、碎印導脈一路推進到本核核心臺，作為後續更深層裂界支線的入口。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂界本核 / 失穩封圈`
- 世界缺口角色：補上 `sec_rift_underseal_dais` 的 `down` stub，使地下鏈在鎮封底座之後有可載入、可維護、可繼續延伸的本核主區
- reserved_room_block: `10201-10220`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0017-sec-rift-true-core.md` 與 `area/sec_rift_true_core/map.md` 第一版
- 以 `mapmd-json` 定義本核落井、本核外環、導脈偏廊與核心井場
- 明確標示與 `sec_rift_underseal_dais/10112` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10201-10212` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_true_core` 掛入 `area/directory.lst`
- 讓 `sec_rift_underseal_dais/10112` 與 `sec_rift_true_core/10201` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_underseal_dais` room `10112`
- `down`: 通往未來更深層裂界核心

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_underseal_dais/map.md`
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
  - `area/sec_rift_underseal_dais/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿既有鎮封底座 world link 向下延伸裂界本核，未引入超出 `ref/Readme.md` 範圍的實作依據

## Validation Results

- `python3 tools/mapmd_validate.py area/sec_rift_true_core/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_true_core/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_true_core/map.md`
  - passed and wrote `roo/10201-10212.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_true_core`
- `area/sec_rift_underseal_dais/roo/10112.roo` 已補上 down 出口到 `10201`
- 本區 `down` 深層出口仍保留到後續裂界核心延伸區

## Next Step Prompt

`繼續為 sec_rift_true_core 之下的更深裂界核心建立下一段單區 plan 與 map.md spec。`
