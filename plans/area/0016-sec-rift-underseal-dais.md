# Sec Rift Underseal Dais Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_underseal_dais`。此區承接 `sec_rift_prison_core` 封印井心下方，將玩家從「封印核心前帶」推進到真正承壓的鎮封底座，作為進入裂界本核前的最後可立足節點。

## Theme Positioning

- theme: `仙俠`
- subtheme: `鎮封底座 / 反衝承壓層`
- 世界缺口角色：補上 `sec_rift_prison_core` 既有 `down` stub，使地下鏈在封印核心之後形成可探索且可維運的底座過渡層
- reserved_room_block: `10101-10120`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0016-sec-rift-underseal-dais.md` 與 `area/sec_rift_underseal_dais/map.md` 第一版
- 以 `mapmd-json` 定義井心落階、鎮封底座主環、承壓旁廊與本核前緣
- 明確標示與 `sec_rift_prison_core/10012` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10101-10112` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_underseal_dais` 掛入 `area/directory.lst`
- 讓 `sec_rift_prison_core/10012` 與 `sec_rift_underseal_dais/10101` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_prison_core` room `10012`
- `down`: 通往未來 `sec_rift_true_core`（裂界本核）

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_prison_core/map.md`
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
  - `area/sec_rift_prison_core/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿封印核心既有 world link 往下銜接鎮封底座，僅補 runtime 可載入與邊界一致性

## Validation Results

- `python3 tools/mapmd_validate.py area/sec_rift_underseal_dais/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_underseal_dais/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_underseal_dais/map.md`
  - passed and wrote `roo/10101-10112.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_underseal_dais`
- `area/sec_rift_prison_core/roo/10012.roo` 已補上 down 出口到 `10101`
- 本區 `down` 深層出口仍保留到未來 `sec_rift_true_core`

## Next Step Prompt

`繼續為 sec_rift_underseal_dais 之下的裂界本核建立下一段單區 plan 與 map.md spec。`
