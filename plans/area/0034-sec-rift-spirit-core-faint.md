# Sec Rift Spirit Core Faint Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_faint`。此區承接 `sec_rift_spirit_core_plain` 最深的裂魄素界座，讓地下鏈再往下沉入裂魄澹界與澹界深井，作為後續同級更硬「微界」層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄澹界 / 澹界深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_plain` 既有 `down` 延伸意圖，讓素界深井正式過渡到更深的澹界層
- reserved_room_block: `11901-11920`
- level_range: `97-100`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0034-sec-rift-spirit-core-faint.md` 與 `area/sec_rift_spirit_core_faint/map.md` 第一版
- 以 `mapmd-json` 定義澹界落座、澹界內庭、微痕偏廊與微界前座
- 明確標示與 `sec_rift_spirit_core_plain/11812` 的 `up` 邊界
- 保留更深層 `down` world link 為後續同級更硬的 endgame 微界區規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11901-11912` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_faint` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_plain/11812` 與 `sec_rift_spirit_core_faint/11901` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_faint/index`
- `area/sec_rift_spirit_core_faint/mob/12901.mob`
- `area/sec_rift_spirit_core_faint/mob/12902.mob`
- `area/sec_rift_spirit_core_faint/mob/12903.mob`
- `area/sec_rift_spirit_core_faint/obj/12951.obj`
- `area/sec_rift_spirit_core_faint/obj/12952.obj`
- `area/sec_rift_spirit_core_faint/obj/12953.obj`
- `area/sec_rift_spirit_core_faint/obj/12954.obj`
- `area/sec_rift_spirit_core_faint/res/core.res`
- `area/sec_rift_spirit_core_faint/shp/guide.shp`
- `area/sec_rift_spirit_core_faint/roo/11901.roo` to `area/sec_rift_spirit_core_faint/roo/11912.roo`
- `area/sec_rift_spirit_core_plain/roo/11812.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_plain` room `11812`
- `down`: 通往未來同級 plateau 的裂魄微界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_plain/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `ref_inputs_deferred`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-scaffold/`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `area/sec_rift_spirit_core_plain/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_plain` 的既有向下 world link 建立下一段 spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11901-11920`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_faint/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_faint/map.md --validate-only`
  - passed
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin merc'`
  - `make: 'merc' is up to date.`
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && rm -f debug/* && timeout 60 ./src/startup.bash'`
  - 2026-03-19 balance correction normalized the recent spirit-core late-chain mob levels back to `<=100` to align with `document/mob.txt`
  - `三國歪傳之降龍伏虎開始正常運作.` appeared in `log/1014.log`
  - the launcher was then terminated by `timeout`, which produced the expected shutdown footer
  - `debug/badobject` remained empty; `debug/failload` / `debug/failenable` / `debug/bugs` did not report new area issues; `debug/error` only recorded the timeout shutdown

## Next Step Prompt

`sec_rift_spirit_core_faint` 已完成第一輪 runtime implementation 並達到 `implementation_ready_for_commit`；下一步先提交這個 implementation milestone，再推進下一個待建 area。
