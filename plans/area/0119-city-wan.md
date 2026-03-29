# City Wan Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_wan`。此區承接 `city_xinye` 北門路口外那條原本只停在宛道想像層的內陸去路，把荊州北段從邊鎮人情與田野過渡，正式收束成一座更有秩序、驛傳與郡城煙火氣的歷史城市 hub。它不該和 `city_xinye` 重複成另一個小鎮，而要讓玩家明顯感到自己正從熟路人的邊鎮節奏，走進一座更能整補、問政、轉接南北交通的城內節點。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `南北轉接城`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 驛傳轉接 / 城內打聽 / 宛道前導`
- contrast_with_previous_two:
  - 相對於 `city_xinye` 的邊鎮人情與 `wild_xinye_fields` 的田野外帶，`city_wan` 應把節奏重新收束成更有城門秩序、榜牌與驛舍導流感的內陸城市。
- 世界缺口角色：
  - 把 `city_xinye` 那條指向宛道的北門去路，正式落成為可載入的城市節點
  - 先替 `洛陽 -> road_wan -> city_wan -> city_xinye -> 襄陽` 這條內陸南北鏈補上第一個真正可停留的歷史城市 hub
- reserved_room_block: `20401-20420`
- planned_vnum_range: `20401-20420`
- level_range: `14-24`
- external_links:
  - `south`: `city_xinye` / 北門路口
  - `north`: `road_wan` / 往宛官道（spec 保留，暫不落 runtime 外連）
  - `out`: `wild_wan_outer` / 宛城外道（spec 保留，暫不落 runtime 外連）
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_wan/map.md`
- `ref/sanguo-area-specfirst/area/road_wan/map.md`
- `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_xinye/map.md`
- `area/jingxiang_road/map.md`
- `plans/area/0117-city-xinye.md`
- `plans/area/0118-wild-xinye-fields.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - `ref/sanguo-area-specfirst/area/road_wan/map.md`
  - `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_xinye/map.md`
  - `area/jingxiang_road/map.md`
  - `plans/area/0117-city-xinye.md`
  - `plans/area/0118-wild-xinye-fields.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/sinya.html`
  - `docs/3yWebsite/map/shanyan.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `city_wan` 列為 `歷史城市 / 14-24` 的 city 節點，並讓它夾在 `road_wan` 與 `city_xinye` 之間，支持本輪先把南向成熟邊界落成
  - `題材分布表` 把荊州段的 `宛` 定位成更有歷史城市秩序感的節點，剛好能在 `wild_xinye_fields` 後把節奏從田野重新收回城門、榜牌與驛傳導流
  - `city_xinye/20207` 已有成熟的 `北門路口` runtime stub，與 `city_wan` scaffold 的 `south -> city_xinye` 契約一致，落地風險明顯低於仍需要整理既有方向的 `jingxiang_road`
  - `road_wan` 與 `wild_wan_outer` 目前都只有 spec scaffold，方向契約本身是乾淨的，因此本輪採「先落成 `south`，其餘外連保留在 spec 層」的策略最穩定
  - `players.json / skills.json` 沒有提供必須優先回頭整理 `jingxiang_road` 的強訊號，反而支持先補一個真正可停留、可整補的內陸城市節點
- `compliance_check`
  - compliant；在 `wild_xinye_fields` 之後接 `city_wan`，可恢復 `City -> Wild -> City` 的 family variety，並優先落地已成熟的北向邊界 stub，而不是先把 `jingxiang_road` 的契約整理混成下一個新區 milestone

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_wan/map.md` 與 `area/city_xinye/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `city_wan` 與 `city_xinye` 均通過；正式 `.roo` 生成後已確認 `city_xinye/20207 north <-> city_wan/20401 south` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- 本輪 direct smoke 未額外產生新的 numbered `log/*`；成功訊號以 stdout 與 `debug/*` 檢查為準
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py city_wan` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版 runtime 房間落在 `20401-20408`
- 已正式落成 runtime boundary：`city_xinye/20207 north -> city_wan/20401` 與 `city_wan/20401 south -> city_xinye/20207`
- `road_wan` 與 `wild_wan_outer` 先保留在 `map.md` / tracker 的 spec 層，不提前建立假外連

## Next Step Prompt

`提交 city_wan implementation milestone commit：內容包含 city_xinye/20207 north <-> city_wan/20401 south runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
