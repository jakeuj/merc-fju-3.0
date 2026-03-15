# Sec Rift Below Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_below`。此區域承接 `sec_catacomb_depths` 最深處的下層裂谷階下方，作為洛陽地下鏈從忘川地穴正式轉入更深異象裂谷與秘境底層前帶的下一段，讓玩家從靈異地穴探索進一步下探到帶有裂風、冷光深井與失衡地脈感的高風險秘境區。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂谷 / 異象秘境`
- 世界缺口角色：補 `sec_catacomb_depths` 已預留的更深異象裂谷 stub，讓洛陽地下鏈在 secret zone 之後還能延伸到更深、更危險的下層探索帶
- reserved_room_block: `9501-9520`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0010-sec-rift-below.md` 與 `area/sec_rift_below/map.md` 第一版
- 用 `mapmd-json` 定義裂谷著階、風脊主線、祭痕支線與深井沉門
- 明確標示與 `sec_catacomb_depths/9499` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/9501-9512.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_below` 掛入 `area/directory.lst`
- 讓 `sec_catacomb_depths/9499` 與 `sec_rift_below/9501` 形成正式雙向邊界
- 更深層 `down` world link 仍停留在 spec，不直接接到不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `sec_catacomb_depths` room `9499`
- `down`: 通往未來更深層祕境沉門 / 裂谷心核

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/sec_catacomb_depths/map.md`
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
  - compliant；本輪使用世界圖、題材分布表與既有 `sec_catacomb_depths` spec 脈絡延伸地下鏈 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `sec_catacomb_depths/9499` 的裂谷石階語意
- `planned_vnum_range` 反映首段保留 block `9501-9520`，即使第一版只先使用其中一部分

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_below/map.md --validate-only`
  - passed

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_below/map.md`
  - passed and wrote `roo/9501-9512.roo`
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1024.log`
  - no new `sec_rift_below`-specific parse / reset / object warning remained after fixing mob class and item values

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_below`
- `area/sec_rift_below/roo/*.roo` 由 `map.md` scaffold 生成
- `area/sec_catacomb_depths/roo/9499.roo` 已正式補上 down 出口到 `9501`
- 初次 smoke test 曾因 `10503.mob` 使用不支援的 `CLASS_WARRIOR` 失敗；改為 `CLASS_FIGHTER` 後已解除
- 第二次 smoke test 出現 `10552` / `10553` 的 item value 警告；補成合法 food / drink 值後已清除 `debug/badobject`

## Next Step Prompt

`先 commit 目前 sec_rift_below 的 implementation 里程碑；commit 後若要續推洛陽地下鏈，優先補更深裂谷心核區的 spec。`
