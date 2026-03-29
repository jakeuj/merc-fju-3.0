# Fort Yiling Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_yiling`。此區承接 `city_jiangling` 西關路口，把原本只停在路標與關道想像層的蜀荊咽喉，正式落成一座有關門、甕城、軍需棚與望樓壓力的主線 fort。它不該只是另一段城市延伸，而要讓玩家明顯感到自己已從江陵的補給秩序，切進更偏盤查、軍令與遠征節奏的關隘空間。

## Theme Positioning

- theme: `軍旅`
- subtheme: `咽喉 / 關道`
- experience_type: `Fort`
- player_loop_focus: `盤查 / 軍令 / 軍需補給 / 關隘轉接 / 西進前導`
- contrast_with_previous_two:
  - 相對於 `wild_spirit_forest` 的深山靈異與 `city_jiangling` 的城市秩序，`fort_yiling` 應把節奏再收束成更有壓力、更有邊界感的軍事 choke point。
- 世界缺口角色：
  - 把 `city_jiangling/19308` 的西關路口正式轉成 `fort_yiling` 的東向關前入口
  - 為後續 `fort_yongan` 建立蜀荊關道上的中繼關隘與西向掛接點
- reserved_room_block: `19401-19420`
- planned_vnum_range: `19401-19420`
- level_range: `42-56`
- external_links:
  - `east`: `city_jiangling` / 西關路口
  - `west`: `fort_yongan` / 西進關道（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_yiling/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_jiangling/map.md`
- `plans/area/0108-city-jiangling.md`
- `area/fort_northern_watch/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_yiling/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_jiangling/map.md`
  - `plans/area/0108-city-jiangling.md`
  - `area/fort_northern_watch/map.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_chengdu/map.md`
  - `ref/sanguo-area-specfirst/area/fort_yongan/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_jiangling` 已把 `19308` 明確塑造成西關路口，代表 `fort_yiling` 已有成熟的 runtime 掛接入口，而不是抽象 world link
  - `world-graph` 將 `fort_yiling` 放在 `city_jiangling` 與 `fort_yongan` 之間，正好提供 `City -> Fort` 的 family 切換
  - `題材分布表` 把夷陵放在蜀漢主線軍旅關道上，適合在江陵補給節奏後收成更強烈的軍事 choke point
  - `players.json / skills.json` 沒有提供另一個更強、更成熟的蜀地非 `City` 服務節點；在目前 runtime 現況下，`fort_yiling` 比重新跳去無掛接的新城市更 actionable
- `compliance_check`
  - compliant；本輪不是因為 `city_jiangling` 剛做完就機械沿預留 link 往下走，而是在 `world_map + progression + 題材分布表 + players/skills + current runtime stub` 共同檢查後，確認 `fort_yiling` 同時滿足 family variety 與掛接成熟度

## Validation Results

- `2026-03-29` `python -X utf8 tools/mapmd_validate.py area/fort_yiling/map.md`
  - `Validated 8 room(s)`，`0 error(s), 0 warning(s)`
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yiling/map.md --validate-only`
  - validation succeeded for `8` rooms
- `2026-03-29` `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_yiling/map.md`
  - 實際生成 `area/fort_yiling/roo/19401-19408.roo`
- `2026-03-29` `python -m json.tool docs/current-game/areas.json`
  - JSON registry 格式正常
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc"`
  - WSL Linux `Makefile.lin` build 成功，未出現新的 warning / link error
- `2026-03-29` `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && mkdir -p log player mail debug vote && find debug -maxdepth 1 -type f -exec truncate -s 0 {} + && cd src && timeout 45s ./merc merc.ini || true"`
  - stdout 明確出現 `三國歪傳之降龍伏虎開始正常運作`
  - 本輪 direct smoke 未額外產生新的 `log/*`；成功訊號以 stdout 與 debug 檢查為準
  - `debug/error` 只有 timeout 關機造成的 `系統臨界錯誤`
  - `debug/failexit` 只有既有 baseline `17201/17208` `Fix_exits`
  - `debug/badobject` 為空
- `2026-03-29` `python -X utf8 tools/area_acceptance_gate.py fort_yiling`
  - 回報 `Recommended gate: implementation_ready_for_commit`
  - 腳本附註 `no log/debug evidence supplied`，此處已補記本輪實際 smoke / debug evidence

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `19401-19408`
- 已正式落成 runtime boundary：`city_jiangling/19308 west -> fort_yiling/19401` 與 `fort_yiling/19401 east -> city_jiangling/19308`
- `fort_yongan` 方向維持在 `map.md` / plan / tracker 的 spec 預留，不提前建立假外連
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 fort_yiling implementation milestone commit：內容包含 city_jiangling/19308 <-> fort_yiling/19401 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
