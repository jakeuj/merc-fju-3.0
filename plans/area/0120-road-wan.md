# Road Wan Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_wan`。此區承接 `loyang/593` 的津陽門與 `city_wan/20407` 的北門官道口，把洛陽南向通宛那條一直停在城門說明文字裡的主線，正式落成為一段可辨位、可歇腳、也能承接旅訊與盤查節奏的官道。它不該搶走 `city_wan` 本身的城市 hub 身分，而要讓玩家明顯感到自己正從洛陽城門的帝都秩序，被一路送往更貼近荊州內陸轉接帶的長路節奏。

## Theme Positioning

- theme: `江湖`
- subtheme: `官道 / 南行`
- experience_type: `Road`
- player_loop_focus: `旅途中轉 / 問路歇腳 / 驛訊流動 / 南行轉場`
- contrast_with_previous_two:
  - 相對於 `wild_xinye_fields` 的田野近郊與 `city_wan` 的歷史城市轉接，`road_wan` 應刻意把節奏收成長路、路亭、盤查與換馬的線性旅程，讓 `City -> Road` 的 family 切換明確成立。
- 世界缺口角色：
  - 把 `loyang` 與 `city_wan` 之間只存在於舊城門描述裡的南向主線，正式補成可載入的官道節點
  - 先替 `loyang -> road_wan -> city_wan -> city_xinye` 這條內陸主線補上真正能承接旅行與轉場節奏的 road 母帶
- reserved_room_block: `20501-20520`
- planned_vnum_range: `20501-20520`
- level_range: `8-18`
- external_links:
  - `north`: `loyang` / 津陽門 (`593`)
  - `south`: `city_wan` / 北門官道口 (`20407`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_wan/map.md`
- `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/index.html`
- `area/city_wan/map.md`
- `area/loyang/roo/593.roo`
- `area/directory.lst`
- `plans/area/0119-city-wan.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_wan/map.md`
  - `ref/sanguo-area-specfirst/area/wild_wan_outer/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `docs/3yWebsite/docs/data/maps.json`
  - `docs/3yWebsite/map/index.html`
  - `area/city_wan/map.md`
  - `area/loyang/roo/593.roo`
  - `area/directory.lst`
  - `plans/area/0119-city-wan.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/sinya.html`
  - `docs/3yWebsite/map/shanyan.html`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `area/world_map.md` 與 `docs/3yWebsite/map/index.html` 都把主骨架寫成 `洛陽 -> 宛 -> 新野 -> 襄陽`，支持先補 `road_wan` 這條南北主線，而不是先展開 `wild_wan_outer` 這種側向外帶
  - `world-graph` 已把 `road_wan` 定位成 `city_loyang <-> city_wan` 間的 `road / 8-18` 節點，而 `wild_wan_outer` 只是 `city_wan` 西側的 outskirts，主次順序清楚
  - `loyang/593` 與 `city_wan/20407` 都已有成熟的「往宛 / 官道」語意 stub，落地 `593 south <-> 20501 north` 與 `20508 south <-> 20407 north` 的風險明顯低於先去展開新側帶
  - `area/directory.lst` 已顯示 `jingxiang_road` 是既有 loadable runtime area，不屬於本輪「下一個待建 area」的真正候選
  - `players.json / skills.json` 在荊州段提供的強訊號仍偏向 `襄陽 / 新野` 的服務與練功 loop，沒有足以推翻主線官道先行的 `宛城外道` 優先證據
- `compliance_check`
  - compliant；本輪在 `city_wan` 之後選 `Road`，既維持 family variety，也先補世界主骨架缺口，沒有把已存在的 `jingxiang_road` 誤判成待建新區

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_wan/map.md` 與 `area/city_wan/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `road_wan` 與 `city_wan` 均通過；正式 `.roo` 生成後已確認 `loyang/593 south <-> road_wan/20501 north` 與 `road_wan/20508 south <-> city_wan/20407 north` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- 本輪 direct smoke 未額外產生新的 numbered `log/*`；成功訊號以 stdout 與 `debug/*` 檢查為準
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py road_wan` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版 runtime 房間落在 `20501-20508`
- 已正式落成兩個 runtime boundary：
  - `loyang/593 south <-> road_wan/20501 north`
  - `road_wan/20508 south <-> city_wan/20407 north`

## Next Step Prompt

`提交 road_wan implementation milestone commit：內容包含 loyang/593 south <-> road_wan/20501 north、road_wan/20508 south <-> city_wan/20407 north runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
