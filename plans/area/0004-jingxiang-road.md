# Jingxiang Road Initial Area Plan

## Summary

建立第三個待建新 AREA：`jingxiang_road`。此區域定位為荊州走廊的幹道型轉接帶，串接 `襄陽`、`新野`、`江夏` 的世界層路徑，先完成 spec-first 草案，不直接進入 runtime 載入整合。

## Theme Positioning

- theme: `江湖風`
- subtheme: `軍旅風`
- 世界缺口角色：補足荊州系城市鏈之間的道路敘事、盤查壓力與商旅流向

## Scope (Milestone 1: Spec)

- 建立 `area/jingxiang_road/map.md` 第一版
- 以 `mapmd-json` 定義房間拓樸（含至少一條非平面連線）
- 補齊 `#Enquire` / `#Keyword` / `#Job` 節點意圖
- 先不建立 `index/mob/obj/res/shp`，避免在缺母城 runtime 區塊時過早掛載

## World Links (Spec Intent)

- `north`: 通往 `襄陽`
- `south`: 通往 `江夏`
- `west`: 通往 `新野` 支線
- `enter/down`：可疑驛站地窖（未來事件或地下路徑）

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/road_jingxiang/map.md`
- `ref_inputs_deferred`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `三國-MUD-題材分布表.md`
  - `references/theme-world-allocation.md`
  - `area/world_map.md`
- `compliance_check`
  - compliant；本輪僅做 spec-first 草案，沒有把生成器 prototype 或模擬系統當直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`

## Next Step Prompt

`根據 plans/area/0004-jingxiang-road.md、area/world_map.md 與 ref/Readme.md，補出 jingxiang_road 的 implementation 級資產（index/mob/obj/res/shp）並做 smoke test。`
