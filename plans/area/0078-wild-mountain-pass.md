# Wild Mountain Pass Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_mountain_pass`。此區承接 `wild_jianye_west` 南向坡口，把建業西郊的水鄉與官道節奏正式轉進會稽方向的山道、棧路與風口岔徑，作為江東主城鏈往 `city_kuaiji` 推進前的第一段山區 wild。

## Theme Positioning

- theme: `江湖`
- subtheme: `山道 / 棧路`
- experience_type: `Wild`
- player_loop_focus: `離城遠行 / 山道辨位 / 岔路探索 / 進城前轉場`
- contrast_with_previous_two:
  - 相對於 `city_jianye` 的都城秩序與 `wild_jianye_west` 的水鄉城郊，`wild_mountain_pass` 應讓玩家明顯感到地勢抬升、視野收束，並把路感從平緩官道切進帶風口、石磴和祠痕的山路節奏
- 世界缺口角色：
  - 把 `wild_jianye_west` 的南向預留正式展開成可擴建的山道 wild
  - 為後續 `city_kuaiji` 與 `dng_temple_ruins` 建立北口前帶
- reserved_room_block: `16301-16330`
- planned_vnum_range: `16301-16330`
- level_range: `100-100`
- external_links:
  - `north`: `wild_jianye_west` / 建業南坡
  - `south`: `city_kuaiji` / 會稽北口
  - `down`: `dng_temple_ruins` / 山腹古祠
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_mountain_pass/map.md`
- `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/quaji.html`
- `plans/area/0077-wild-jianye-west.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_mountain_pass/map.md`
  - `ref/sanguo-area-specfirst/area/city_kuaiji/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/quaji.html`
  - `plans/area/0077-wild-jianye-west.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/sanguo-area-specfirst/area/dng_temple_ruins/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 明確把 `建業 - 會稽` 放在同一條江東主線上，適合先用山道 wild 把主城外帶收束進更高壓的地形節奏
  - `題材分布表` 把 `會稽` 定位成 `江湖 / 仙俠` 的山城節點，支持先以前置山路建立氣氛與路線辨位
  - `wild_mountain_pass` scaffold 本身就提供岔路、地標與疑似支線的語彙，能自然承接 `wild_jianye_west` 的南向坡口
  - `maps.json` 與 `quaji.html` 證明會稽在舊站地圖上是正式主城節點，因此先補它前方的山口過渡帶合理
- `compliance_check`
  - compliant；在 `Outskirts` 之後切進 `Wild`，維持建業鏈的 family 變化，也避免過早回到下一個 city-like 片區

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_mountain_pass/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_mountain_pass/map.md --validate-only`
  - passed (`Validation succeeded for 9 room(s).`)

## Next Step Prompt

`先 commit 目前 wild_mountain_pass 的 spec milestone；commit 後直接做 implementation milestone，補 boundary、roo、index/mob/obj/res/shp，並跑 WSL build 與 startup smoke test。`
