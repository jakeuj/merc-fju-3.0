# Sec Rift Core Vein Abyss Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_core_vein_abyss`。此區承接 `sec_rift_core_below_deeps` 最底端的渦核封檻臺，將地下鏈推進到真正的「裂核脈淵」層，作為更深封印底脈與最終渦核核心之前的高壓前帶。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂核脈淵 / 渦核深腹`
- 世界缺口角色：補上 `sec_rift_core_below_deeps` 既有 `down` 延伸意圖，讓地下鏈從底脈渦腹正式進入更高壓、更失衡的脈淵層
- reserved_room_block: `10501-10520`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0020-sec-rift-core-vein-abyss.md` 與 `area/sec_rift_core_vein_abyss/map.md` 第一版
- 以 `mapmd-json` 定義落檻承脈、深腹環脈、倒灌裂庭與沉紋斷口
- 明確標示與 `sec_rift_core_below_deeps/10412` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/10501-10512` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_core_vein_abyss` 掛入 `area/directory.lst`
- 讓 `sec_rift_core_below_deeps/10412` 與 `sec_rift_core_vein_abyss/10501` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_core_below_deeps` room `10412`
- `down`: 通往未來更深層裂核禁底區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_core_below_deeps/map.md`
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
  - `area/sec_rift_core_below_deeps/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_core_below_deeps` 的既有向下 world link 延伸，先固定下一段 spec-first 里程碑與保留房號，不擴張到 runtime implementation

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `10501-10520`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_core_vein_abyss/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_vein_abyss/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_core_vein_abyss/map.md`
  - passed and wrote `roo/10501-10512`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && timeout 50 ./startup.bash"`
  - reached success signal `三國歪傳之降龍伏虎開始正常運作.` in `log/1004.log`
  - `debug/badobject`、`debug/bugs`、`debug/failenable`、`debug/failload` remained empty after the run
  - `debug/error` only recorded the expected timeout-driven shutdown trace after the forced stop
- `git commit -m "Add sec_rift_core_vein_abyss area"`
  - committed as `f4fe735`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- `area/directory.lst` 已加入 `sec_rift_core_vein_abyss`
- `area/sec_rift_core_below_deeps/roo/10412.roo` 已補上 `down -> 10501` 邊界出口
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步新的 runtime area 台帳
- smoke test 首輪曾出現 `11552-11554` 的 `物品太貴` warning，後續已將成本下修並重跑，warning 消失

## Next Step Prompt

`sec_rift_core_vein_abyss` 已完成第一輪 implementation 並提交；下一步可為更深的 `sec_rift_underseal_basin` 建立單區 plan 與 `map.md` spec。`
