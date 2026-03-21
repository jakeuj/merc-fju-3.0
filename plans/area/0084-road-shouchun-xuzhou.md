# Road Shouchun Xuzhou Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_shouchun_xuzhou`。此區承接 `city_xuzhou` 南門驛口，把玩家從東線州府正式送上通往壽春的淮東官道，讓 `徐州 -> 壽春` 之間不再只是抽象 world link，而是一段可辨位、可問路、也能承接驛路與旅貨流動的 road 型 area。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `淮東官道 / 驛路轉場`
- experience_type: `Road`
- player_loop_focus: `驛路轉場 / 問路歇腳 / 官道傳聞 / 州城南出`
- contrast_with_previous_two:
  - 相對於 `sec_water_ruins` 的靜壓祕境與 `city_xuzhou` 的州府回補，`road_shouchun_xuzhou` 應把節奏推回開放地表與驛路移動感，讓玩家從城內秩序過渡到真正往壽春南下的陸路旅程。
- 世界缺口角色：
  - 把 `city_xuzhou/16808` 的南向預留正式轉成可載入的官道節點
  - 為後續 `city_shouchun` 與 `wild_shouchun_fields` 建立清楚的北段路網骨架
- reserved_room_block: `16901-16920`
- planned_vnum_range: `16901-16920`
- level_range: `20-32`
- external_links:
  - `north`: `city_xuzhou` / 南門驛口
  - `south`: `city_shouchun` / 壽春方向預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_shouchun_xuzhou/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0083-city-xuzhou.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_shouchun_xuzhou/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0083-city-xuzhou.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_shouchun/map.md`
  - `ref/sanguo-area-specfirst/area/wild_shouchun_fields/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `area/world_map.md` 把 `徐州 -> 壽春 -> 建業` 放在同一條東線南下骨架上，支持先補官道，再收束到壽春母城
  - `world-graph` 已明確提供 `road_shouchun_xuzhou` 作為 `road` 類節點，說明這段不應直接跳過，而應有獨立的交通與問路體驗
  - `題材分布表` 讓江東北段維持 `歷史城市` 與交通節奏，適合把官道做成驛路、路亭與分岔口的中繼區，而不是再疊一座城市
  - `players.json / skills.json` 沒有要求在徐州後立刻切回港口或秘境，反而支持先把陸路轉場節點補齊
- `compliance_check`
  - compliant；在 `City` 之後切到 `Road`，符合 queue variety，也能自然承接下一步的 `city_shouchun`

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_shouchun_xuzhou/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_shouchun_xuzhou/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Next Step Prompt

`先 commit 目前 road_shouchun_xuzhou 的 spec milestone；commit 後直接做 implementation milestone，補 runtime scaffold、接上 city_xuzhou 邊界並跑 build / smoke test。`
