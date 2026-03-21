# Dng Temple Ruins Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_temple_ruins`。此區承接 `city_kuaiji` 預留的古祠地脈入口，把會稽山城裡流動的門派傳聞、地方勢力與山中異聞正式收束成一座可下探的古寺 dungeon，作為江東線在山城之下的第一個封閉探索節點。

## Theme Positioning

- theme: `仙俠`
- subtheme: `古寺 / 異聞`
- experience_type: `Dungeon`
- player_loop_focus: `地脈下探 / 異聞調查 / 古寺封印 / 山城支線`
- contrast_with_previous_two:
  - 相對於 `wild_mountain_pass` 的山道遠行與 `city_kuaiji` 的山城回補，`dng_temple_ruins` 應把節奏收進更封閉、更潮濕也更帶封印感的地下空間，讓玩家從城市傳聞正式轉進實際探查
- 世界缺口角色：
  - 把 `city_kuaiji` 的 `down` 預留正式轉成可擴建的山中古寺 dungeon
  - 為會稽鏈後續的地脈、異聞與更深支線建立第一層封閉探索節點
- reserved_room_block: `16501-16530`
- planned_vnum_range: `16501-16530`
- level_range: `100-100`
- external_links:
  - `up`: `city_kuaiji` / 古祠地脈
  - `down`: `sec_kuaiji_seal_chamber` / 深封石室預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_temple_ruins/map.md`
- `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/quaji.html`
- `plans/area/0079-city-kuaiji.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_temple_ruins/map.md`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/quaji.html`
  - `plans/area/0079-city-kuaiji.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/sanguo-area-specfirst/area/sec_water_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `dng_temple_ruins` 放在 `city_kuaiji` 之下的江東 dungeon 節點，適合直接承接會稽山城的異聞與地脈感
  - `題材分布表` 對會稽所在區帶給了 `仙俠` 補題空間，支持在主城之後切進帶封印與殘祠感的地底探索
  - `dng_temple_ruins` scaffold 直接提供古寺、封印與深處節點語彙，能自然轉成目前會稽鏈需要的地下 dungeon
  - `quaji.html` 證明會稽本身是一座有完整城市輪廓的山城，因此把地下異聞留在其下方作為支線延伸是合理的
- `compliance_check`
  - compliant；在 `City` 之後切進 `Dungeon`，避免會稽鏈連續堆疊 city-like 片區，也符合 `City -> Wild -> Dungeon` 的節奏切換

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_temple_ruins/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_temple_ruins/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)

## Next Step Prompt

`先 commit 目前 dng_temple_ruins 的 spec milestone；commit 後直接做 implementation milestone，補 boundary、roo、index/mob/obj/res/shp，並跑 WSL build 與 startup smoke test。`
