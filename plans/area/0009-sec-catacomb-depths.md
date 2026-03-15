# Sec Catacomb Depths Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_catacomb_depths`。此區域承接 `dng_royal_tomb` 最深處的下層石階下方，作為洛陽地下鏈從帝王古墓再往下探入靈異地穴與秘境異象的下一段，讓探索感從古墓機關逐步轉成帶有仙俠異象與高風險高回報的 secret zone。

## Theme Positioning

- theme: `仙俠`
- subtheme: `地穴 / 靈異`
- 世界缺口角色：補 `dng_royal_tomb` 已預留的更深墓室群 stub，讓洛陽地下鏈能從墓葬探索自然過渡到帶有異象核心與秘境試煉感的 deeper secret

## Scope (Milestone 1: Spec)

- 建立 `area/sec_catacomb_depths/map.md` 第一版
- 用 `mapmd-json` 定義地穴入口、異象核心、裂隙支線與秘壇深處
- 明確標示與 `dng_royal_tomb/9490` 的 `up` 邊界意圖
- 先不建立 runtime 資產，避免在秘境條件與 deeper progression 尚未定穩前提早掛載

## Scope (Milestone 2: Implementation)

- 建立 `area/sec_catacomb_depths/index` 第一版
- 產生並掛入 `roo/9491-9499.roo`
- 補最小 `mob / obj / res / shp`
- 將 `sec_catacomb_depths` 掛入 `area/directory.lst`
- 讓 `dng_royal_tomb/9490` 與 `sec_catacomb_depths/9491` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `dng_royal_tomb` room `9490`
- `down`: 通往未來更深層異象裂谷 / 秘境底層

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `ref/sanguo-area-specfirst/area/sec_catacomb_depths/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
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
  - compliant；本輪僅建立 spec-first 草案，使用 world-graph、題材分布表與 spec scaffold 做 topology / 題材決策，未把 generator prototype 或模擬系統當成直接 runtime 依據

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `dng_royal_tomb/9490` 的下層石階語意

## Validation Results (Spec Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_catacomb_depths/map.md --validate-only`
  - passed

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_catacomb_depths/map.md --validate-only`
  - passed
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1020.log`
  - no new `sec_catacomb_depths`-specific `Load_room` / reset / object parse failure observed after regenerating missing `.roo`

## Runtime Notes

- `area/directory.lst` 已加入 `sec_catacomb_depths`
- `area/sec_catacomb_depths/roo/*.roo` 由 `map.md` scaffold 生成
- `area/dng_royal_tomb/roo/9490.roo` 已正式補上 down 出口到 `9491`
- 初次 smoke test 曾因漏生 `.roo` 導致 `Load_shop` 找不到 `9495`；補生成房間檔後已解除
- 第二次啟動卡在殘留 shared memory；清除 IPC 後重新 smoke test 成功，因此 blocker 不屬於 area data 本身
- implementation milestone 已提交：`7d21770 feat: implement catacomb depths runtime area`

## Next Step Prompt

`建立 sec_rift_below 的單區 plan 與 map.md spec，延續 sec_catacomb_depths/9499 的 down world link。`
