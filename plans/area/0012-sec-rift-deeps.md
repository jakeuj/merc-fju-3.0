# Sec Rift Deeps Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_deeps`。此區域承接 `sec_rift_core` 最深處的底層封界下方，作為洛陽地下鏈從裂谷心核正式轉入更深裂界與深層封印帶的下一段，讓玩家從心核脈動與鎮界痕跡進一步下探到帶有封印殘律、裂界回音與禁制壓力感的高風險深層區。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂界 / 深層封印`
- 世界缺口角色：補 `sec_rift_core` 已預留的裂界深層 stub，讓洛陽地下鏈在心核之後仍保有更下層的探索延伸與封印主題轉折
- reserved_room_block: `9701-9720`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0012-sec-rift-deeps.md` 與 `area/sec_rift_deeps/map.md` 第一版
- 用 `mapmd-json` 定義下井前帶、封印回廊、禁制支線與深層界井
- 明確標示與 `sec_rift_core/9612` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/9701-9712.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_deeps` 掛入 `area/directory.lst`
- 讓 `sec_rift_core/9612` 與 `sec_rift_deeps/9701` 形成正式雙向邊界
- 更深層 `down` world link 仍停留在 spec，不直接接到不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_core` room `9612`
- `down`: 通往未來更深層界井 / 裂界禁底

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `area/sec_rift_core/map.md`
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
  - compliant；本輪使用世界圖、題材分布表與既有 `sec_rift_core` spec 脈絡延伸地下鏈 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `sec_rift_core/9612` 的底層封界語意
- `planned_vnum_range` 反映首段保留 block `9701-9720`，即使第一版只先使用其中一部分

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_deeps/map.md --validate-only`
  - passed

## Next Step Prompt

`以 sec_rift_deeps/map.md 生成第一批 roo 與最小 runtime 資產，並把 sec_rift_core/9612 的 down 邊界正式接到 sec_rift_deeps/9701。`
