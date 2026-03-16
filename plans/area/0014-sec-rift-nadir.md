# Sec Rift Nadir Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_nadir`。此區域承接 `sec_rift_abyss` 最深處的禁底界井下方，作為洛陽地下鏈從裂界禁底正式轉入裂界禁牢與封印底座前帶的下一段，讓玩家從禁底邊界探索進一步下探到更高壓的禁制層。

## Theme Positioning

- theme: `仙俠`
- subtheme: `禁底 / 裂界禁牢`
- 世界缺口角色：補 `sec_rift_abyss` 已預留的更深層 stub，讓洛陽地下鏈由禁底探索銜接到真正禁牢段
- reserved_room_block: `9901-9920`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0014-sec-rift-nadir.md` 與 `area/sec_rift_nadir/map.md` 第一版
- 用 `mapmd-json` 定義禁牢落點、封印迴廊、鎮鎖側線與底層界井
- 明確標示與 `sec_rift_abyss/9812` 的 `up` 邊界意圖
- 保留更深層 `down` world link 為 spec

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/9901-9912.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_nadir` 掛入 `area/directory.lst`
- 讓 `sec_rift_abyss/9812` 與 `sec_rift_nadir/9901` 形成正式雙向邊界

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_abyss` room `9812`
- `down`: 通往未來更深層封印核心區

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_abyss/map.md`
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
  - `area/sec_rift_abyss/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪沿既有地下鏈 world link 與題材分配往下延伸，並明確保留 docs dataset 缺檔現況

## Validation Results (Spec + Implementation)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_nadir/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_nadir/map.md`
  - passed and wrote `roo/9901-9912.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_nadir`
- `area/sec_rift_nadir/roo/*.roo` 由 `map.md` scaffold 生成
- `area/sec_rift_abyss/roo/9812.roo` 已正式補上 down 出口到 `9901`

## Next Step Prompt

`繼續為 sec_rift_nadir 之下的更深封印核心建立下一段單區 plan 與 map.md spec。`
