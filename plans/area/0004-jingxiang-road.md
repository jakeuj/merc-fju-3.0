# Jingxiang Road Initial Area Plan

## Summary

建立第三個待建新 AREA：`jingxiang_road`。此區域定位為荊州走廊的幹道型轉接帶，串接 `襄陽`、`新野`、`江夏` 的世界層路徑；目前已從 spec-first 草案推進到第一版 runtime implementation。

## Theme Positioning

- theme: `江湖風`
- subtheme: `軍旅風`
- 世界缺口角色：補足荊州系城市鏈之間的道路敘事、盤查壓力與商旅流向

## Scope (Milestone 1: Spec)

- 建立 `area/jingxiang_road/map.md` 第一版
- 以 `mapmd-json` 定義房間拓樸（含至少一條非平面連線）
- 補齊 `#Enquire` / `#Keyword` / `#Job` 節點意圖
- 先不建立 `index/mob/obj/res/shp`，避免在缺母城 runtime 區塊時過早掛載

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/*.roo` 第一版並補必要 runtime 調整
- 建立最小可載入的 `index/mob/obj/res/shp`
- 掛入 `area/directory.lst`，讓 area 可參與實際載入與 smoke test
- 由於 `襄陽`、`新野`、`江夏` 目前尚無對應 runtime area，本輪不強行建立假的 boundary room 連結；外部世界連線先保留在 spec

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

## Validation Results (Implementation Stage)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/jingxiang_road/map.md --validate-only`
  - passed
- `make -C src clean && make -C src merc`
  - passed
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
  - passed
- `cd src && timeout 45 bash ./startup.bash`
  - passed with startup success signal in `log/1013.log`
  - no new `jingxiang_road`-specific `Load_room` / reset / object parse failure remained after fixing `9854.obj`

## Runtime Notes

- `area/directory.lst` 已加入 `jingxiang_road`
- `area/jingxiang_road/roo/*.roo` 由 `map.md` scaffold 生成，並保留一個 `enter/out` 非平面連線
- `9301 / 9305 / 9308` 的對外世界邊界目前仍為 spec intent，不直接指向不存在的母城 runtime 房號
- `9307` 原先草案中的 `job_pull_bar` 已撤回；現有 `job_pull_bar` 是硬編碼綁定新手區房號，不適合重用到本區

## Next Step Prompt

`先 commit 目前 jingxiang_road 的 implementation 里程碑；commit 後若要繼續荊州系 world links，再等襄陽 / 新野 / 江夏 對應 runtime area 落地後補 boundary room 雙向連結。`
