# Wild Longqu Hills Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_longqu_hills`。此區域承接 `loyang_outskirts` 東側已落地的丘陵邊界，作為洛陽近郊往野外探索帶延伸的第二段，主題從城郊秩序轉進丘陵遺跡與隱伏風險。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `仙俠風`
- 世界缺口角色：補 `loyang_outskirts` 東向邊界之後的真正野外區，讓玩家從主城外郊進一步過渡到地形複雜、帶有遺跡暗示的探索線

## Scope (Milestone 1: Spec)

- 建立 `area/wild_longqu_hills/map.md` 第一版
- 用 `mapmd-json` 定義丘陵主線、獵戶支線與裂縫石階非平面連線
- 明確標示與 `loyang_outskirts/7510` 的 west 邊界意圖
- 先不建立 `index/mob/obj/res/shp`，避免在 spec 尚未定穩前提早掛載

## World Links (Spec Intent)

- `west`: 通往 `loyang_outskirts` room `7510`（丘陵巡路）
- `down`: 通往未來地下遺跡 / 機關秘境節點

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/wild_longqu_hills/map.md`
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
  - `ref/sanguo-progression-map.md`
- `compliance_check`
  - compliant；本輪僅建立 spec-first 草案，使用世界圖與 spec scaffold 做 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `west` 外部連線對得上既有 `loyang_outskirts` 的東向邊界語意

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_longqu_hills/map.md --validate-only`
  - passed

## Next Step Prompt

`先 commit 目前 wild_longqu_hills 的 spec 里程碑；commit 後再補 implementation 級資產，並把它正式接到 loyang_outskirts/7510。`
