# Dng Royal Tomb Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_royal_tomb`。此區域承接 `dng_sewer_depths` 最深處的下沉井口下方，作為洛陽地下鏈從黑水深渠正式轉入古墓 / 機關型秘境的下一段，讓玩家從潮濕封印帶進一步下探到帶有帝王墓痕跡與機關鎮壓感的深層遺跡。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `古墓 / 機關`
- 世界缺口角色：補 `dng_sewer_depths` 已預留的古墓深井 stub，讓洛陽地下鏈能從水道系統自然過渡到遺跡、封墓與機關探索段

## Scope (Milestone 1: Spec)

- 建立 `area/dng_royal_tomb/map.md` 第一版
- 用 `mapmd-json` 定義墓道前帶、石門主廊、陪葬側室與封墓深井
- 明確標示與 `dng_sewer_depths/9470` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/*.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `dng_royal_tomb` 掛入 `area/directory.lst`
- 讓 `dng_sewer_depths/9470` 與 `dng_royal_tomb/9481` 形成正式雙向邊界
- `sec_catacomb_depths` world link 仍保留在 spec，不直接接到不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `dng_sewer_depths` room `9470`
- `down`: 通往未來更深層墓室群 / 地底埋葬層

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/dng_royal_tomb/map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/world-graph.md`
- `ref_inputs_deferred`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/world-graph.md`
  - `area/world_map.md`
- `compliance_check`
  - compliant；本輪僅建立 spec-first 草案，使用 world-graph、題材分布表與 spec scaffold 做 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `dng_sewer_depths/9470` 的下沉井口語意

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_royal_tomb/map.md --validate-only`
  - passed

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_royal_tomb/map.md --validate-only`
  - passed
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1017.log`
  - no new `dng_royal_tomb`-specific `Load_room` / reset / object parse failure observed

## Runtime Notes

- `area/directory.lst` 已加入 `dng_royal_tomb`
- `area/dng_royal_tomb/roo/*.roo` 由 `map.md` scaffold 生成
- `area/dng_sewer_depths/roo/9470.roo` 已正式補上 down 出口到 `9481`
- `9490` 以下的更深墓室群仍停留在 spec，不先做假的 runtime boundary

## Next Step Prompt

`先 commit 目前 dng_royal_tomb 的 implementation 里程碑；commit 後若要續推洛陽地下鏈，優先補 sec_catacomb_depths spec。`
