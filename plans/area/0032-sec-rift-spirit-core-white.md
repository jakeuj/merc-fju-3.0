# Sec Rift Spirit Core White Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_white`。此區承接 `sec_rift_spirit_core_blank` 最深的裂魄空白座，讓地下鏈再往下沉入裂魄白界與白界深井，作為更深「素界」層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄白界 / 白界深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_blank` 既有 `down` 延伸意圖，讓空白深井正式過渡到更深的白界層
- reserved_room_block: `11701-11720`
- level_range: `95-98`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0032-sec-rift-spirit-core-white.md` 與 `area/sec_rift_spirit_core_white/map.md` 第一版
- 以 `mapmd-json` 定義白界落座、白界內庭、失名偏廊與素界前座
- 明確標示與 `sec_rift_spirit_core_blank/11612` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11701-11712` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_white` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_blank/11612` 與 `sec_rift_spirit_core_white/11701` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_white/index`
- `area/sec_rift_spirit_core_white/mob/12701.mob`
- `area/sec_rift_spirit_core_white/mob/12702.mob`
- `area/sec_rift_spirit_core_white/mob/12703.mob`
- `area/sec_rift_spirit_core_white/obj/12751.obj`
- `area/sec_rift_spirit_core_white/obj/12752.obj`
- `area/sec_rift_spirit_core_white/obj/12753.obj`
- `area/sec_rift_spirit_core_white/obj/12754.obj`
- `area/sec_rift_spirit_core_white/res/core.res`
- `area/sec_rift_spirit_core_white/shp/guide.shp`
- `area/sec_rift_spirit_core_white/roo/11701.roo` to `area/sec_rift_spirit_core_white/roo/11712.roo`
- `area/sec_rift_spirit_core_blank/roo/11612.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_blank` room `11612`
- `down`: 通往未來更深層裂魄素界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_blank/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`（本輪僅確認無更高優先的城鎮服務鏈候選，未直接參與地下鏈題材決策）
  - `docs/3yWebsite/docs/data/skills.json`（本輪僅確認無更高優先的技能服務鏈候選，未直接參與地下鏈題材決策）
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_spirit_core_blank/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿 `sec_rift_spirit_core_blank` 的既有向下 world link 建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的 area rebuild 範圍

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11701-11720`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_white/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_white/map.md --validate-only`
  - passed
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin merc'`
  - `make: 'merc' is up to date.`
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && rm -f debug/* && timeout 60 ./src/startup.bash'`
  - `三國歪傳之降龍伏虎開始正常運作.` appeared in `log/1010.log`
  - the launcher was then terminated by `timeout`, which produced the expected shutdown footer
  - `debug/badobject` remained empty; `debug/error` only recorded the timeout shutdown

## Next Step Prompt

`sec_rift_spirit_core_white` 已完成第一輪 runtime implementation 並達到 `implementation_ready_for_commit`；下一步先提交這個 implementation milestone，再推進下一個待建 area。
