# Wild Longqu Hills Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_longqu_hills`。此區域承接 `loyang_outskirts` 東側已落地的丘陵邊界，作為洛陽近郊往野外探索帶延伸的第二段，主題從城郊秩序轉進丘陵遺跡與隱伏風險；目前已從 spec-first 草案推進到第一版 runtime implementation。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `仙俠風`
- 世界缺口角色：補 `loyang_outskirts` 東向邊界之後的真正野外區，讓玩家從主城外郊進一步過渡到地形複雜、帶有遺跡暗示的探索線

## Scope (Milestone 1: Spec)

- 建立 `area/wild_longqu_hills/map.md` 第一版
- 用 `mapmd-json` 定義丘陵主線、獵戶支線與裂縫石階非平面連線
- 明確標示與 `loyang_outskirts/7510` 的 west 邊界意圖
- 先不建立 `index/mob/obj/res/shp`，避免在 spec 尚未定穩前提早掛載

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/*.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `wild_longqu_hills` 掛入 `area/directory.lst`
- 讓 `loyang_outskirts/7510` 與 `wild_longqu_hills/9401` 形成正式雙向邊界
- `9410` 以下的地下遺跡 world link 仍保留在 spec，不直接指向不存在的 runtime 房號

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

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_longqu_hills/map.md --validate-only`
  - passed
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1014.log`
  - no new `wild_longqu_hills`-specific `Load_room` / reset / object parse failure observed

## Runtime Notes

- `area/directory.lst` 已加入 `wild_longqu_hills`
- `area/wild_longqu_hills/roo/*.roo` 由 `map.md` scaffold 生成
- `area/loyang_outskirts/roo/7510.roo` 已正式補上 east 出口到 `9401`
- `9410` 的 deeper underground 連結仍停留在 spec，不先做假的 runtime boundary

## Next Step Prompt

`先 commit 目前 wild_longqu_hills 的 implementation 里程碑；commit 後若要繼續洛陽系 rebuild，優先補 loyang_outskirts 另一條地下支線：洛陽地下水區。`
