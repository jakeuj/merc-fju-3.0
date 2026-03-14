# Dng Sewer Depths Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_sewer_depths`。此區域承接 `dng_loyang_sewer` 最深處的鐵梯下方，作為洛陽地下鏈真正進入深層水道與半封印機關帶的第二段，讓玩家從前哨型地下水區進一步下探到更危險、更不穩定的黑水深渠。

## Theme Positioning

- theme: `詭異民俗風`
- subtheme: `深層水道`
- 世界缺口角色：補 `dng_loyang_sewer` 已預留的更深水道 stub，讓洛陽地下鏈不只停在入口前帶，而能自然延伸到具封印感與失落設施痕跡的 deeper section

## Scope (Milestone 1: Spec)

- 建立 `area/dng_sewer_depths/map.md` 第一版
- 用 `mapmd-json` 定義深井落點、黑水主渠、機關側室與封印深槽
- 明確標示與 `dng_loyang_sewer/9460` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `dng_loyang_sewer` room `9460`
- `down`: 通往未來更深層封印墓井 / 地底遺構

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/dng_sewer_depths/map.md`
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
  - compliant；本輪僅建立 spec-first 草案，使用世界圖與 spec scaffold 做 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `dng_loyang_sewer/9460` 的深井鐵梯語意

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_sewer_depths/map.md --validate-only`
  - passed

## Next Step Prompt

`先 commit 目前 dng_sewer_depths 的 spec 里程碑；commit 後若要落地 runtime 資產，再把它正式接到 dng_loyang_sewer/9460。`
