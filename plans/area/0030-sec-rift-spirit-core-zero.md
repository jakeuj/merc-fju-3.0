# Sec Rift Spirit Core Zero Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_zero`。此區承接 `sec_rift_spirit_core_null` 最深的裂魄歸零座，讓地下鏈進一步沉入裂魄零界與零界深井，作為更深空白層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄零界 / 零界深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_null` 既有 `down` 延伸意圖，讓歸零深庭正式過渡到更深的零界層
- reserved_room_block: `11501-11520`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0030-sec-rift-spirit-core-zero.md` 與 `area/sec_rift_spirit_core_zero/map.md` 第一版
- 以 `mapmd-json` 定義零界落座、零界內庭、無痕偏廊與空白前座
- 明確標示與 `sec_rift_spirit_core_null/11412` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11501-11512` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_zero` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_null/11412` 與 `sec_rift_spirit_core_zero/11501` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_zero/index`
- `area/sec_rift_spirit_core_zero/mob/12501.mob`
- `area/sec_rift_spirit_core_zero/mob/12502.mob`
- `area/sec_rift_spirit_core_zero/mob/12503.mob`
- `area/sec_rift_spirit_core_zero/obj/12551.obj`
- `area/sec_rift_spirit_core_zero/obj/12552.obj`
- `area/sec_rift_spirit_core_zero/obj/12553.obj`
- `area/sec_rift_spirit_core_zero/obj/12554.obj`
- `area/sec_rift_spirit_core_zero/res/core.res`
- `area/sec_rift_spirit_core_zero/shp/guide.shp`
- `area/sec_rift_spirit_core_zero/roo/11501.roo` to `area/sec_rift_spirit_core_zero/roo/11512.roo`
- `area/sec_rift_spirit_core_null/roo/11412.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_null` room `11412`
- `down`: 通往未來更深層裂魄空白區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_null/map.md`
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
  - `area/sec_rift_spirit_core_null/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_spirit_core_null` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的 area rebuild 範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11501-11520`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_zero/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_zero/map.md --validate-only`
  - passed
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin merc'`
  - `make: 'merc' is up to date.`
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && rm -f debug/* && timeout 60 ./src/startup.bash'`
  - `三國歪傳之降龍伏虎開始正常運作.` appeared in `log/1008.log`
  - the launcher was then terminated by `timeout`, which produced the expected shutdown footer
  - `debug/badobject` remained empty; `debug/error` only recorded the timeout shutdown

## Next Step Prompt

`sec_rift_spirit_core_zero` 已完成 runtime implementation；下一步應先 commit 這個 milestone，再回到 fixed prompt 選下一個 actionable area。
