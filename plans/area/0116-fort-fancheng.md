# Fort Fancheng Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_fancheng`。此區承接 `city_xiangyang` 北向大道，把原本只停在「北路 / 樊城」想像層的北岸城防，正式落成一座有關前坡、柵門、甕城軍道、校場棚與旗樓望臺的主線 fort。它不該像城市分區那樣讓人停留太久，而要讓玩家一踏進去就明顯感到自己已從襄陽的補給與秩序，切進更偏軍令、盤查與守備壓力的軍事 choke point。

## Theme Positioning

- theme: `軍旅`
- subtheme: `北岸城防 / 軍令關門`
- experience_type: `Fort`
- player_loop_focus: `盤查 / 軍令傳遞 / 軍需補給 / 北路轉接 / 荊州軍事前帶`
- contrast_with_previous_two:
  - 相對於 `wild_chengdu_outer` 的城外過渡與 `district_chengdu_scholar` 的文士靜區，`fort_fancheng` 應把節奏強烈拉回邊防、關門與守備壓力。
- 世界缺口角色：
  - 把 `city_xiangyang/14208` 的北向大道正式落成為北岸城防入口
  - 讓荊州主線在 `city_xiangyang` 之後，不必立刻再走一個城區，而是先經過一座軍旅 fort
- reserved_room_block: `20101-20120`
- planned_vnum_range: `20101-20120`
- level_range: `38-52`
- external_links:
  - `south`: `city_xiangyang` / 北向大道
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_fancheng/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/map/sinya.html`
- `area/city_xiangyang/map.md`
- `plans/area/0115-district-chengdu-scholar.md`
- `area/fort_yiling/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_fancheng/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `docs/3yWebsite/map/sinya.html`
  - `area/city_xiangyang/map.md`
  - `area/city_xiangyang/index`
  - `area/fort_yiling/map.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_xinye/map.md`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - `ref/sanguo-area-specfirst/area/wild_xinye_fields/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_xiangyang/14208` 已有成熟的北向大道 stub，可低風險接成 `Fort`
  - `players.json` 對襄陽的訊號偏向高段訓練與中繼 hub，支持先補它北側的軍事前帶
  - `city_xinye` 雖然仍是合理候選，但 ref scaffold 與現行 runtime stub 在方位上互相衝突，本輪不宜硬推
- `compliance_check`
  - compliant；在 queue 為空時重新盤點後，`fort_fancheng` 同時滿足非 `District` family variety 與 runtime 邊界成熟度

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_fancheng/map.md` 與 `area/city_xiangyang/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `fort_fancheng` 與 `city_xiangyang` 均通過；正式 `.roo` 生成後已確認 `city_xiangyang/14208 north <-> fort_fancheng/20101 south` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py fort_fancheng` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 第一版預計落地 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版房間預計使用 `20101-20108`
- `city_xiangyang/14208 north <-> fort_fancheng/20101 south` 會在本輪正式落成 runtime boundary
- `city_xinye` 延後處理，直到 `city_xiangyang` / `jingxiang_road` / ref scaffold 的方位契約先被整理一致

## Next Step Prompt

`提交 fort_fancheng implementation milestone commit：內容包含 city_xiangyang/14208 <-> fort_fancheng/20101 runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
