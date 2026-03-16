# Sec Rift Abyss Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_rift_abyss`。此區域承接 `sec_rift_deeps` 最深處的禁底界井下方，作為洛陽地下鏈從裂界深層正式轉入裂界禁底與封印底座的下一段，讓玩家從深層封印探索進一步下探到帶有禁律殘痕、鎮界回音與底層壓迫感的高風險區。

## Theme Positioning

- theme: `仙俠`
- subtheme: `裂界 / 禁底封印`
- 世界缺口角色：補 `sec_rift_deeps` 已預留的禁底 stub，讓洛陽地下鏈在裂界深層之後形成更明確的禁底節點
- reserved_room_block: `9801-9820`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0013-sec-rift-abyss.md` 與 `area/sec_rift_abyss/map.md` 第一版
- 用 `mapmd-json` 定義禁底落點、封印迴廊、鎮鎖側線與禁底井心
- 明確標示與 `sec_rift_deeps/9712` 的 `up` 邊界意圖
- 先保留更深層 `down` world link 為 spec，不提早指向不存在的 runtime area

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/9801-9812.roo` 第一版並補齊最小 runtime 資產
- 建立 `index/mob/obj/res/shp`
- 將 `sec_rift_abyss` 掛入 `area/directory.lst`
- 讓 `sec_rift_deeps/9712` 與 `sec_rift_abyss/9801` 形成正式雙向邊界
- 更深層 `down` world link 仍停留在 spec，不直接接到不存在的 runtime area

## World Links (Spec Intent)

- `up`: 通往 `sec_rift_deeps` room `9712`
- `down`: 通往未來更深層界牢 / 封印核心底座

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/sec_rift_deeps/map.md`
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
  - `area/sec_rift_deeps/map.md`
  - `ref/world-graph.md`
  - `ref/三國-MUD-題材分布表.md`
- `compliance_check`
  - compliant；本輪延續既有地下鏈 world link 與題材分配，並保留 docs dataset 缺檔事實，不以不存在資料臆測設計依據

## Validation Results (Spec + Implementation)

- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_abyss/map.md --validate-only`
  - passed
- `python3 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_rift_abyss/map.md`
  - passed and wrote `roo/9801-9812.roo`
- `make -C src -f Makefile.lin merc`
  - passed

## Runtime Notes

- `area/directory.lst` 已加入 `sec_rift_abyss`
- `area/sec_rift_abyss/roo/*.roo` 由 `map.md` scaffold 生成
- `area/sec_rift_deeps/roo/9712.roo` 已正式補上 down 出口到 `9801`

## Next Step Prompt

`繼續為 sec_rift_abyss 之下的更深裂界禁牢建立下一段單區 plan 與 map.md spec。`
