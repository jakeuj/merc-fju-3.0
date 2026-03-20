# Sec Rift Spirit Core Infernal Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_spirit_core_infernal`。此區承接 `sec_rift_spirit_core_tartarean` 最深的裂魄冥淵座，讓地下鏈再往下沉入裂魄冥獄與冥獄井腹，作為後續同級更硬「業獄」層區前的 plateau 主段。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂魄冥獄 / 冥獄井腹`
- 世界缺口角色：補上 `sec_rift_spirit_core_tartarean` 既有 `down` 延伸意圖，讓冥淵井腹正式過渡到更深的冥獄層
- reserved_room_block: `13601-13620`
- level_range: `100-100`
- plateau 差異：維持 `100` 封頂 endgame band，但以更沉重的獄壓封鎖、業獄前橋與井腹守壓提高危險度，而不是再往 `100+` 疊高

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0051-sec-rift-spirit-core-infernal.md` 與 `area/sec_rift_spirit_core_infernal/map.md` 第一版
- 以 `mapmd-json` 定義冥獄落座、冥獄內庭、獄冥偏廊與業獄前座
- 明確標示與 `sec_rift_spirit_core_tartarean/13512` 的 `up` 邊界
- 保留更深層 `down` world link 為後續區域規劃

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/13601-13612` 第一版並補齊最小 runtime 資產
- 建立 `index / mob / obj / res / shp`
- 將 `sec_rift_spirit_core_infernal` 掛入 `area/directory.lst`
- 讓 `sec_rift_spirit_core_tartarean/13512` 與 `sec_rift_spirit_core_infernal/13601` 形成正式雙向邊界

## Implementation Results

- `area/sec_rift_spirit_core_infernal/index`
- `area/sec_rift_spirit_core_infernal/mob/14601.mob`
- `area/sec_rift_spirit_core_infernal/mob/14602.mob`
- `area/sec_rift_spirit_core_infernal/mob/14603.mob`
- `area/sec_rift_spirit_core_infernal/obj/14651.obj`
- `area/sec_rift_spirit_core_infernal/obj/14652.obj`
- `area/sec_rift_spirit_core_infernal/obj/14653.obj`
- `area/sec_rift_spirit_core_infernal/obj/14654.obj`
- `area/sec_rift_spirit_core_infernal/res/core.res`
- `area/sec_rift_spirit_core_infernal/shp/guide.shp`
- `area/sec_rift_spirit_core_infernal/roo/13601-13612`
- `area/sec_rift_spirit_core_tartarean/roo/13512.roo`
- `area/directory.lst`
- `docs/current-game/areas.md`
- `docs/current-game/areas.json`

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_spirit_core_tartarean` room `13512`
- `down`: 通往未來更深層裂魄業獄區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_spirit_core_tartarean/map.md`
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
  - `area/sec_rift_spirit_core_tartarean/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `compliance_check`
  - compliant；本輪先依 `players.json` / `skills.json` 確認沒有更高優先的服務型候選，再沿 `sec_rift_spirit_core_tartarean` 的既有向下 world link 建立下一段 plateau spec-first 里程碑

## Validation Results

- `python -X utf8 tools/area_vnum_allocator.py --estimated-rooms 12 --headroom 8`
  - after `0051` / `map.md` had already reserved `13601-13620`, the allocator suggested the next free block `13701-13720`
- `python -X utf8 tools/mapmd_validate.py area/sec_rift_spirit_core_infernal/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_infernal/map.md --validate-only`
  - passed
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_spirit_core_infernal/map.md`
  - regenerated `roo/13601-13612`
- `python -X utf8 scripts/world_consistency_checker.py`
  - passed with `0 error(s)`; only pre-existing legacy warnings remained
- `make -C src clean && make -C src merc`
  - passed
- `python -X utf8 tools/log_parse_summary.py log/1059.log`
  - `log/1059.log` contained `三國歪傳之降龍伏虎開始正常運作.`
  - no non-empty `debug/*` files were observed after the smoke test
- smoke test via Python timeout wrapper around `./src/startup.bash`
  - created new run log `log/1059.log`
  - launcher was terminated after `60` seconds by the wrapper timeout, with no new area-specific loader/debug issue observed

## Next Step Prompt

`sec_rift_spirit_core_infernal` 已完成第一輪 runtime implementation 與 smoke test 驗證，並達到 `validated_ready_to_advance`；下一步可回到 queue 盤點下一個待建 area。
