# Dng Boat Graveyard Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_boat_graveyard`。此區承接 `wild_south_sea_route` 南航分水附近的渦潮沉舟帶，把玩家從近海外航道的開闊海面，拉進一段由殘桅、裂艙、錨鏈與沉鐘構成的封閉海上 wreck dungeon，讓南境海路主線在真正進入外海群島之前，先經過一層更幽閉也更具遺跡感的沉船墓場。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `沉舟 / 水鬼`
- experience_type: `Dungeon`
- player_loop_focus: `殘舟下探 / 錨鏈辨位 / 艙道轉場 / 深艙壓迫`
- contrast_with_previous_two:
  - 相對於 `city_nanhai` 的港城秩序與 `wild_south_sea_route` 的開闊海路，`dng_boat_graveyard` 應讓玩家感受到視野突然被斷桅與艙壁壓縮，風險也從潮汐辨位轉成殘骸迷走、沉鐘回音與深艙未知物的心理壓力
- 世界缺口角色：
  - 把 `wild_south_sea_route` 南航分水附近的外海殘舟帶正式轉成可持續擴建的 spec-first dungeon
  - 為後續 `sec_water_ruins` 或更深外海群島建立第一層沉船遺跡前帶
- reserved_room_block: `15701-15730`
- planned_vnum_range: `15701-15730`
- level_range: `99-100`
- external_links:
  - `up`: `wild_south_sea_route` / 南航分水
  - `down`: `sec_water_ruins` / 深海水府預留
  - `south`: `sea_outer_isles` / 外海群島預留
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南境外海沉船墓場`
  - `殘桅與錨鏈交錯的沉舟遺跡`
  - `海路 wild 之後的封閉 wreck dungeon`
- 它補的玩家 loop：
  - `從海路辨位切進沉舟下探`
  - `靠殘桅、斷索、錨鏈、沉鐘與裂艙辨認進退`
  - `為更深水府與外海群島建立第一層危險前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是港城補給與問路節奏
  - 不再是近海棧道與礁岸水路的開闊辨位
  - 改用破桅、艙壁、沉鐘與深艙壓迫把節奏轉成海上遺跡 dungeon

## Player Loop Contract

- `主線推進`
  - 玩家由南航分水附近的渦潮裂口下切，先經過破桅前廊、漏艙窄道與中艙殘庭，再逐步接近錨鏈井口與墓場深艙
- `地標辨識`
  - 透過殘桅、錨鏈、沉鐘、斷槳與艙壁水痕判斷哪裡像退路、哪裡像深處、哪裡像仍可繼續下探
- `支線探索`
  - 潮骨偏艙
  - 船鐘暗壁
  - 浮屍掛橋
- `非平面節奏`
  - `up/down` 用於艙層落差與井口深井，讓沉舟墓場維持垂直壓迫感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0072-dng-boat-graveyard.md`
- 建立 `area/dng_boat_graveyard/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `maelstrom-entry`
  - `broken-hull`
  - `bone-hold`
  - `anchor-shaft`
  - `deep-bell`
- 將 `沉舟 / 退路 / 深處 / 井口 / 外海` 視為正式 `#Enquire` 候選
- 將 `殘桅 / 錨鏈 / 沉鐘 / 斷槳 / 艙壁` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供艙層或井口高低差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_boat_graveyard/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0071-wild-south-sea-route.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_boat_graveyard/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0071-wild-south-sea-route.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/wild_pirate_islands/map.md`
  - `ref/sanguo-area-specfirst/area/fort_naval_base/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `wild_south_sea_route` 已把南境節奏從港城推進到外海前帶，適合在 `Wild` 之後切進一個更封閉的海上遺跡 dungeon
  - `ref` scaffold 已提供 `dng_boat_graveyard` 類型，能直接支撐沉舟、殘艙與水鬼壓迫感的題材連續性
  - `world-graph` 與題材分布表都支持在水域鏈上安排 wreck / ruins 類節點，讓海上主線不只是一段更遠的平面水道
  - `players.json / skills.json` 沒有提供南海後必須立即回到另一座城市服務鏈的明確證據，因此在 `Wild` 後切入 `Dungeon` 更符合 queue variety
- `compliance_check`
  - compliant；在 `Wild` 之後切入 `Dungeon`，延續海路高風險節奏，也避免 queue 在港口 / 海路題材上連續堆疊過多同 family wild

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_boat_graveyard/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_boat_graveyard/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 dng_boat_graveyard 的 spec milestone；commit 後直接做 implementation milestone，補 boundary、roo、index/mob/obj/res/shp，並跑 WSL build 與 startup smoke test。`
