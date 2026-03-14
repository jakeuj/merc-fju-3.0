# Dng Loyang Sewer Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_loyang_sewer`。此區域承接 `loyang_outskirts` 的暗井與井下檢修道，作為洛陽系重建流程中第一個正式地下支線，將城郊的暗井入口擴張成可探索的地下水脈 / 水門前帶。

## Theme Positioning

- theme: `仙俠風`
- subtheme: `詭異民俗風`
- 世界缺口角色：補齊 `loyang_outskirts` 已落地的 `7511/7512` 地下入口，讓洛陽系不只往外野延伸，也能往地下秘密路線延伸

## Scope (Milestone 1: Spec)

- 建立 `area/dng_loyang_sewer/map.md` 第一版
- 用 `mapmd-json` 定義地下水道主線、側渠支線與 deeper sewer 垂直連線
- 明確標示與 `loyang_outskirts/7512` 的 `up` 邊界意圖
- 先不建立 `index/mob/obj/res/shp`，避免在地下 deeper 線還未穩定前過早掛載

## World Links (Spec Intent)

- `up`: 通往 `loyang_outskirts` room `7512`
- `down`: 通往未來 deeper sewer / 地底機關區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/dng_loyang_sewer/map.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `ref/三國-MUD-題材分布表.md`
  - `area/world_map.md`
  - `ref/world-graph.md`
- `compliance_check`
  - compliant；本輪僅建立 spec-first 草案，使用 world-map 與 spec scaffold 做 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `loyang_outskirts/7512` 的地下入口語意

## Next Step Prompt

`先 commit 目前 dng_loyang_sewer 的 spec 里程碑；commit 後再補 implementation 級資產，並把它正式接到 loyang_outskirts/7512。`
