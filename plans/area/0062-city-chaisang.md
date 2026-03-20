# City Chaisang Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_chaisang`。此區承接 `city_jiangxia` 東向幹道與江岸水路之後的第一座江東入口城市，讓玩家從濕地與古廟的壓迫重新回到可補給、可問路、可轉往長沙與赤壁方向的江岸城市節奏。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `江岸城鎮 / 江東門戶`
- experience_type: `City`
- player_loop_focus: `回城補給 / 江岸轉場 / 問路整線 / 東進江東主線`
- contrast_with_previous_two:
  - 相對於 `wild_yunmeng` 的迷霧濕地與 `dng_sunken_temple` 的下探遺跡，`city_chaisang` 應讓玩家明確感受到又回到了有人管理碼頭、路牌與城務的江岸城市秩序
- 世界缺口角色：
  - 把荊州東進主線正式接進柴桑城市 hub
  - 為後續 `city_changsha`、`sec_chibi_battlefield` 與更東向江東線建立穩定轉場點
- reserved_room_block: `14701-14730`
- planned_vnum_range: `14701-14730`
- level_range: `62-72`
- external_links:
  - `west`: `city_jiangxia` / 東向幹道
  - `west`: `wild_reed_bank` / 江岸蘆洲外帶
  - `south`: `city_changsha` / 荊南主城
  - `south`: `sec_chibi_battlefield` / 戰場祕區
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_chaisang/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_chaisang/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `ref/sanguo-area-specfirst/area/city_changsha/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 與現有 `city_jiangxia` world-link 都直接支持江夏往柴桑的主線延伸
  - 柴桑作為江岸城鎮，剛好能把濕地 / 古廟段後的節奏拉回補給與交通 hub
  - `players.json / skills.json` 沒有要求此時轉向另一條未銜接主線，因此先把江岸東進鏈收穩最合理
- `compliance_check`
  - compliant；`Dungeon -> City` 的節奏合理，且選的是 repo 現有預留最成熟的下一座城市

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_chaisang/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chaisang/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 city_chaisang 的 spec milestone；commit 後直接開始 implementation milestone。`
