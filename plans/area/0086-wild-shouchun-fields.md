# Wild Shouchun Fields Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_shouchun_fields`。此區承接 `city_shouchun` 的田野外口，把玩家從壽春主城的軍政秩序自然放回城外田埂、村舍與灌渠交錯的近郊帶，讓 `徐州 -> 壽春 -> 建業` 這條東線主骨架不只靠城市和官道串接，也有一段真正能呼吸、能辨位的壽春外野。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `田野 / 村舍`
- experience_type: `Wild`
- player_loop_focus: `離城外放 / 近郊問路 / 田野轉場 / 南路前帶`
- contrast_with_previous_two:
  - 相對於 `road_shouchun_xuzhou` 的驛路轉場與 `city_shouchun` 的城內收束，`wild_shouchun_fields` 應把節奏重新打開成有田埂、灌渠與村舍呼吸感的近郊 wild，讓玩家從壽春城心的秩序退到更貼近土地的外圍地帶，再準備往建業線繼續南下。
- 世界缺口角色：
  - 把 `city_shouchun/17008` 的田野預留正式轉成可載入的近郊 wild
  - 為後續更南的建業方向保留一段比官道更柔性的主線緩衝區
- reserved_room_block: `17101-17120`
- planned_vnum_range: `17101-17120`
- level_range: `22-34`
- external_links:
  - `enter`: `city_shouchun` / 田野外口
  - `south`: `city_jianye` / 建業方向預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_shouchun_fields/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0085-city-shouchun.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_shouchun_fields/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0085-city-shouchun.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `ref/sanguo-area-specfirst/area/wild_jianye_west/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `wild_shouchun_fields` 放在 `city_shouchun` 與 `city_jianye` 之間，說明壽春之後不該直接再跳一座主城，而應先經過一段近郊 wild 過渡
  - `area/world_map.md` 的世界骨架明確存在 `徐州 - 壽春 - 建業` 這條東線，支持把壽春外圍補成真正可行走的田野，而不是只留抽象 world link
  - `題材分布表` 把壽春定位成江東北段的歷史城市據點，適合先往外展開成田埂、村舍與農時氣味都明確的近郊帶，而不是立刻切回另一座城市或秘境
  - `players.json / skills.json` 沒有提供必須把壽春外圍做成高服務密度節點的強信號，反而支持先把離城、問路與轉場節奏補完整
- `compliance_check`
  - compliant；在 `Road -> City` 之後切到 `Wild`，符合 queue variety，也能自然承接後續更南的建業主線

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_shouchun_fields/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_shouchun_fields/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 tools/mapmd_validate.py area/city_shouchun/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`) after aligning `17008 <-> 17101`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_shouchun_fields/map.md`
  - passed (`Wrote 8 room scaffold file(s) to area/wild_shouchun_fields/roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_shouchun/map.md`
  - passed (`Wrote 9 room scaffold file(s) to area/city_shouchun/roo`) after aligning `17008 <-> 17101`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed (`make: 'merc' is up to date.`)
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - passed via startup success log `log/1057.log`
- `debug/badobject`
  - passed (empty after smoke test)
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `wild_shouchun_fields`，保留房號段 `17101-17120`
- `area/wild_shouchun_fields/index` 已建立，`Serial 175`
- 第一輪 runtime scaffold 已加入：
  - `mob/19531-19534`
  - `obj/19551-19554`
  - `res/fields.res`
  - `shp/supplies.shp`
- `city_shouchun/17008 <-> wild_shouchun_fields/17101` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `wild_shouchun_fields`

## Next Step Prompt

`先 commit 目前 wild_shouchun_fields 的 implementation milestone；commit 後回到 queue 規則盤點下一個待建 area，建立新的 spec milestone。`
