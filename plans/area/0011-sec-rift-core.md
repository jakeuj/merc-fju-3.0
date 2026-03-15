# Sec Rift Core Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_core`。此區域承接 `sec_rift_below` 最深處的祕境沉門下方，作為洛陽地下鏈從異象裂谷正式轉入裂谷心核與祕境底層核心的下一段，讓玩家從裂谷探索進一步下探到帶有心核脈動、失衡晶層與底層封界感的高風險核心區。

## Theme Positioning

- theme: `仙俠`
- subtheme: `心核 / 裂谷底層`
- 世界缺口角色：補 `sec_rift_below` 已預留的裂谷心核 stub，讓洛陽地下鏈在異象裂谷之後形成真正的高風險核心節點
- reserved_room_block: `9601-9620`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0011-sec-rift-core.md` 與 `area/sec_rift_core/map.md` 第一版
- 用 `mapmd-json` 定義沉門後前帶、心核主廊、晶脈支線與封界下層
- 明確標示與 `sec_rift_below/9512` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/9601-9612.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_core` 掛入 `area/directory.lst`
- 讓 `sec_rift_below/9512` 與 `sec_rift_core/9601` 形成正式雙向邊界
- 更深層 `down` world link 仍停留在 spec，不直接接到不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_below` room `9512`
- `down`: 通往未來更深層心核底井 / 裂界深層

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `area/sec_rift_below/map.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `area/world_map.md`
- `compliance_check`
  - compliant；本輪使用世界圖、題材分布表與既有 `sec_rift_below` spec 脈絡延伸地下鏈 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `sec_rift_below/9512` 的祕境沉門語意
- `planned_vnum_range` 反映首段保留 block `9601-9620`，即使第一版只先使用其中一部分

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core/map.md --validate-only`
  - passed

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core/map.md`
  - passed and wrote `roo/9601-9612.roo`
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1025.log`
  - no new `sec_rift_core`-specific parse / reset / object warning observed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_core`
- `area/sec_rift_core/roo/*.roo` 由 `map.md` scaffold 生成
- `area/sec_rift_below/roo/9512.roo` 已正式補上 down 出口到 `9601`
- `sec_rift_core` 第一輪 implementation 未出現新的 area-specific `debug/badobject` / `Load_room` / reset parse 失敗
- implementation milestone 已提交：`48393ff feat: implement rift core runtime area`

## Next Step Prompt

`建立更深裂界區的單區 plan 與 map.md spec，延續 sec_rift_core/9612 所預留的下層 world link。`
