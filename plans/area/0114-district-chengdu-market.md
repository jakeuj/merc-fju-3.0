# District Chengdu Market Initial Area Plan

## Summary

建立下一個待建新 AREA：`district_chengdu_market`。此區承接 `city_chengdu` 的市樓牌坊，把蜀漢都城原本只停在「看得見熱鬧」的市場感，正式展開成有主街、糧行、布招、茶食街棚與差役告示口的市井分區。這裡要讓玩家感到自己仍在成都秩序之內，卻已經從母城幹道走進真正吞吐貨物、傳聞與地方人情的市場腹地。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `市井 / 商街`
- experience_type: `District`
- player_loop_focus: `城內補給 / 問路導流 / 商街停留 / 告示傳聞 / 市井轉場`
- contrast_with_previous_two:
  - 相對於 `city_chengdu` 的都城主骨架與 `wild_chengdu_outer` 的離城鬆動感，`district_chengdu_market` 應把節奏重新收回人潮、店鋪、交易與口耳消息交錯的城市腹地，形成 `City -> Wild -> District` 的 family variety 回切。
- 世界缺口角色：
  - 把 `city_chengdu/19704` 的市場預留正式轉成 `district_chengdu_market/19901` 的 runtime boundary
  - 為成都後續更細的城市服務鏈、地方委託與傳聞分流建立第一段城內 `District`
- reserved_room_block: `19901-19920`
- planned_vnum_range: `19901-19920`
- level_range: `34-46`
- external_links:
  - `west`: `city_chengdu` / 市樓牌坊
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/district_chengdu_market/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_chengdu/map.md`
- `plans/area/0112-city-chengdu.md`
- `plans/area/0113-wild-chengdu-outer.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/district_chengdu_market/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_chengdu/map.md`
  - `plans/area/0112-city-chengdu.md`
  - `plans/area/0113-wild-chengdu-outer.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/district_chengdu_scholar/map.md`
  - `docs/3yWebsite/map/chendo.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_chengdu` 現有 spec 已把 `19704` 定位成市樓牌坊，且預留東向 `district_chengdu_market` world link，代表母城內的市場分區已有成熟掛接點
  - `world-graph` 直接把 `district_chengdu_market` 列為成都旁的 `district / 歷史城市 / 34-46` 節點，比 `district_chengdu_scholar` 更貼近目前已落地的市場邊界與主街節奏
  - `題材分布表` 把成都定為蜀漢首都；在 `wild_chengdu_outer` 之後回切一個商街 `District`，能把 family variety 從 `Wild` 拉回城市腹地，而不會再堆另一段郊野
  - `players.json / skills.json` 沒有提供必須 scholar-first 的強訊號，因此本輪優先補齊都城裡最直接可用的市場 / 問路 / 傳聞 loop
- `compliance_check`
  - compliant；在 `wild_chengdu_outer` 之後改做 `District`，既避免同質郊野連續堆疊，也沿用 `city_chengdu/19704` 的成熟 boundary stub，不需要跳離成都主線

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/district_chengdu_market/map.md` 與 `area/city_chengdu/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `district_chengdu_market` 與 `city_chengdu` 均通過；正式 `.roo` 生成後已確認 `city_chengdu/19704 east <-> district_chengdu_market/19901 west` 雙向邊界一致
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py district_chengdu_market` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合，首版 runtime 房間落在 `19901-19908`
- 已正式落成 runtime boundary：`city_chengdu/19704 east -> district_chengdu_market/19901` 與 `district_chengdu_market/19901 west -> city_chengdu/19704`
- 首版聚焦牌坊入口、市井主街、糧行棚廊、茶食街棚、布招與差役告示口，暫不提前延伸學舍或更深成都內城分區
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 district_chengdu_market implementation milestone，然後把 tracker 從 in_progress 推進成 done。`
