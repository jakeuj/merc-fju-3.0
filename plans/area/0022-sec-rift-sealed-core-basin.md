# Sec Rift Sealed Core Basin Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_sealed_core_basin`。此區承接 `sec_rift_underseal_basin` 最底端的禁底沉門，將地下鏈推進到真正的封核沉盆，作為更深裂核封心區前的核心承壓內盆。

## Theme Positioning

- theme: `仙俠`
- subtheme: `封核沉盆 / 內壓核心`
- 世界缺口角色：補上 `sec_rift_underseal_basin` 既有 `down` 延伸意圖，讓地下鏈從沉壓承接層正式進入封核內盆
- reserved_room_block: `10701-10720`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0022-sec-rift-sealed-core-basin.md` 與 `area/sec_rift_sealed_core_basin/map.md` 第一版
- 以 `mapmd-json` 定義沉門落盆、封核環盆、回壓渠廊與封心前庭
- 明確標示與 `sec_rift_underseal_basin/10612` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10701-10712` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_sealed_core_basin` 掛入 `area/directory.lst`
- 讓 `sec_rift_underseal_basin/10612` 與 `sec_rift_sealed_core_basin/10701` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_underseal_basin` room `10612`
- `down`: 通往未來更深層裂核封心區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_underseal_basin/map.md`
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
  - `area/sec_rift_underseal_basin/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_underseal_basin` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的規劃範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `10701-10720`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_sealed_core_basin/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_sealed_core_basin/map.md --validate-only`
  - passed
- `git commit -m "Add sec_rift_sealed_core_basin spec"`
  - committed as `dc6a7c5`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)`; only existing legacy / disconnected-area warnings remained
- `make -C src -f Makefile.lin merc`
  - passed
- `timeout 50 ./startup.bash`
  - reached success signal `三國歪傳之降龍伏虎開始正常運作.` in `log/1036.log`
  - `debug/*` remained empty after the run, including `badobject`、`bugs`、`failenable`、`failload`
- `python -X utf8 tools/log_parse_summary.py`
  - reported startup success signal for `log/1036.log` and `0` non-empty debug files
- `python -X utf8 tools/area_acceptance_gate.py sec_rift_sealed_core_basin`
  - recommended `implementation_ready_for_commit`
- `git commit -m "Add sec_rift_sealed_core_basin area"`
  - committed as `2fb0a07`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- `area/directory.lst` 已加入 `sec_rift_sealed_core_basin`
- `area/sec_rift_underseal_basin/roo/10612.roo` 已補上 `down -> 10701` 邊界出口
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步新的 runtime area 台帳
- 本輪 smoke test 未觀察到新的 area loader / object / enable 警告

## Next Step Prompt

`sec_rift_sealed_core_basin` 已完成第一輪 implementation 並提交；下一步可為更深的 `sec_rift_sealed_core_heart` 建立單區 plan 與 map.md spec。`
