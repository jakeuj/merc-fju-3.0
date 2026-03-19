# Sec Rift Spirit Core Plain Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_plain`。此區承接 `sec_rift_spirit_core_white` 最深的裂魄白界座，讓地下鏈再往下沉入裂魄素界與素界深井，作為更深「澹界」層區前的過渡主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄素界 / 素界深井`
- 世界缺口角色：補上 `sec_rift_spirit_core_white` 既有 `down` 延伸意圖，讓白界深井正式過渡到更深的素界層
- reserved_room_block: `11801-11820`
- level_range: `96-99`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0033-sec-rift-spirit-core-plain.md` 與 `area/sec_rift_spirit_core_plain/map.md` 第一版
- 以 `mapmd-json` 定義素界落座、素界內庭、澹痕偏廊與澹界前座
- 明確標示與 `sec_rift_spirit_core_white/11712` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/11801-11812` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_plain` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_white/11712` 與 `sec_rift_spirit_core_plain/11801` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_plain/index`
- `area/sec_rift_spirit_core_plain/mob/12801.mob`
- `area/sec_rift_spirit_core_plain/mob/12802.mob`
- `area/sec_rift_spirit_core_plain/mob/12803.mob`
- `area/sec_rift_spirit_core_plain/obj/12851.obj`
- `area/sec_rift_spirit_core_plain/obj/12852.obj`
- `area/sec_rift_spirit_core_plain/obj/12853.obj`
- `area/sec_rift_spirit_core_plain/obj/12854.obj`
- `area/sec_rift_spirit_core_plain/res/core.res`
- `area/sec_rift_spirit_core_plain/shp/guide.shp`
- `area/sec_rift_spirit_core_plain/roo/11801.roo` to `area/sec_rift_spirit_core_plain/roo/11812.roo`
- `area/sec_rift_spirit_core_white/roo/11712.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_white` room `11712`
- `down`: 通往未來更深層裂魄澹界區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_white/map.md`
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
  - `area/sec_rift_spirit_core_white/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_white` 的既有向下 world link 建立下一段 spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - suggested `11801-11820`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_plain/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_plain/map.md --validate-only`
  - passed
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)` and unrelated legacy warnings outside this area
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin merc'`
  - `make: 'merc' is up to date.`
- `wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && rm -f debug/* && timeout 60 ./src/startup.bash'`
  - `三國歪傳之降龍伏虎開始正常運作.` appeared in `log/1011.log`
  - the launcher was then terminated by `timeout`, which produced the expected shutdown footer
  - `debug/badobject` remained empty; `debug/error` only recorded the timeout shutdown

## Next Step Prompt

`sec_rift_spirit_core_plain` 已完成第一輪 runtime implementation 並達到 `implementation_ready_for_commit`；下一步先提交這個 implementation milestone，再推進下一個待建 area。
