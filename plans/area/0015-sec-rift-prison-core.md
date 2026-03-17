# Sec Rift Prison Core Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_prison_core`。此區域承接 `sec_rift_nadir` 最深處的禁牢界井下方，作為洛陽地下鏈從裂界禁牢正式轉入封印核心與鎮封底座前帶的下一段，讓玩家從高壓禁制探索進一步下探到真正承受封印主體反衝的深層心獄區。

## Theme Positioning

- theme: `仙俠`
- subtheme: `禁牢 / 封印核心`
- 世界缺口角色：補 `sec_rift_nadir` 已預留的封印核心 stub，讓洛陽地下鏈在禁牢之後形成真正的核心鎮封節點
- reserved_room_block: `10001-10020`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0015-sec-rift-prison-core.md` 與 `area/sec_rift_prison_core/map.md` 第一版
- 用 `mapmd-json` 定義心獄落點、鎮封主廊、護印支線與核心井心
- 明確標示與 `sec_rift_nadir/9912` 的 `up` 邊界意圖
- 保留更深層 `down` world link 為 spec

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10001-10012.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_prison_core` 掛入 `area/directory.lst`
- 讓 `sec_rift_nadir/9912` 與 `sec_rift_prison_core/10001` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_nadir` room `9912`
- `down`: 通往未來更深層鎮封底座 / 裂界本核

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_nadir/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`（repo 目前不存在，僅保留追蹤需求）
  - `docs/3yWebsite/docs/data/skills.json`（repo 目前不存在，僅保留追蹤需求）
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_nadir/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿既有地下鏈 world link 與題材分配往下延伸到封印核心，並明確保留 docs dataset 缺檔現況

## Validation Targets (Spec Stage)

- `map.md` 內含有效 `mapmd-json` 區塊
- scaffold validator `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- `up` 外部連線對得上既有 `sec_rift_nadir/9912` 的禁牢界井語意
- `planned_vnum_range` 反映首段保留 block `10001-10020`，即使第一版只先使用其中一部分

## Validation Results

- `python3 tools/mapmd_validate.py area/sec_rift_prison_core/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_prison_core/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_prison_core/map.md`
  - passed and wrote `roo/10001-10012.roo`
- `make -C src clean && make -C src merc`
  - passed
- `cd src && ./startup.bash` with 50s timeout wrapper
  - timed out as expected for smoke test harness, but `log/1027.log` contains startup success signal `三國歪傳之降龍伏虎開始正常運作`
  - `tools/log_parse_summary.py` reports startup success and no non-empty debug files

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_prison_core`
- `area/sec_rift_prison_core/roo/*.roo` 由 `map.md` scaffold 生成
- `area/sec_rift_nadir/roo/9912.roo` 已正式補上 down 出口到 `10001`
- 本輪 smoke test 未觀察到新的 `sec_rift_prison_core`-specific `debug/badobject` / `Load_room` / reset parse 失敗

## Next Step Prompt

`繼續為 sec_rift_prison_core 之下的更深鎮封底座建立下一段單區 plan 與 map.md spec。`
