# District Loyang East Market Initial Area Plan

## Summary

建立下一個待建新 AREA：`district_loyang_east_market`。此區承接 `loyang` 的商街前帶，把帝都內部原本分散在 `553` 商街、`563` 武防具店與 `613` 票據所周邊的 service loop，正式整理成一段有入口街口、商行主街、票據與馬販側棚、茶湯攤與差役榜口的市場 district。這裡應讓玩家感到自己仍在洛陽秩序內，但腳步已經從主城御道切進真正替新手與中低段玩家提供補給、交易、問路與轉場的城市腹地。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `市集 / 商業`
- experience_type: `District`
- player_loop_focus: `補給 / 採買 / 問路 / 馬市導流 / 市井傳聞`
- contrast_with_previous_two:
  - 相對於上一輪 `road_chenliu` 的長路節奏，`district_loyang_east_market` 要把體驗收回帝都腹地的人流、招牌、攤聲與服務節點。
  - 相對於既有 `loyang_outskirts` 的出城過渡帶，本區不再是離城，而是把洛陽城內最直接可用的商業 service loop 正式拆成可載入 district。
- 世界缺口角色：
  - 把 `loyang/553` 的市場前帶正式轉成 `district_loyang_east_market/21001`
  - 為洛陽後續 `east_market / west_market / scholar` 城內分區鏈建立第一個實作中的 `District`
- reserved_room_block: `21001-21020`
- planned_vnum_range: `21001-21020`
- level_range: `1-10`
- external_links:
  - `out`: `loyang` / 商街前帶 (`553`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/world-graph.md`
- `ref/sanguo-area-specfirst/area/district_loyang_east_market/map.md`
- `ref/sanguo-area-specfirst/area/district_loyang_west_market/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/loyang/roo/553.roo`
- `area/loyang/roo/563.roo`
- `area/loyang/roo/597.roo`
- `area/loyang/roo/598.roo`
- `area/loyang/roo/612.roo`
- `area/loyang/roo/613.roo`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/world-graph.md`
  - `ref/sanguo-area-specfirst/area/district_loyang_east_market/map.md`
  - `ref/sanguo-area-specfirst/area/district_loyang_west_market/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/loyang/roo/553.roo`
  - `area/loyang/roo/563.roo`
  - `area/loyang/roo/597.roo`
  - `area/loyang/roo/598.roo`
  - `area/loyang/roo/612.roo`
  - `area/loyang/roo/613.roo`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/loyang.html`
  - `ref/sanguo-area-specfirst/area/district_loyang_scholar/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `district_loyang_east_market` 列成 `city_loyang` 旁的低等 `District`，而且與 `city_loyang` 的方向契約清楚
  - `players.json` 直接反覆提到洛陽武器店、馬房與大校場，支持先補洛陽城內最直接承接新手與轉職 service loop 的商業 district
  - `loyang/553` 的描述已經明講南側商家興榮，周邊又串到 `613` 票據所與 `563` 武防具街，代表東市服務聚落比西市更成熟、更 actionable
  - 在 `road_chenliu` 之後切回 `District`，能維持 queue variety，避免連續堆疊另一條中原 road
- `compliance_check`
  - compliant；優先落地 service loop 明確、入口 stub 成熟的 `district_loyang_east_market`，比目前仍較鬆散的 `district_loyang_west_market` 更適合作為下一個 actionable area

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/district_loyang_east_market/map.md`
  - 通過，`8 rooms`、`0 error(s)`、`0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_loyang_east_market/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_loyang_east_market/map.md`
  - 通過，寫出 `21001-21008`
- `python -m json.tool docs/current-game/areas.json`
  - 通過
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && make -f Makefile.lin clean && make -f Makefile.lin merc"`
  - 通過
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && timeout 45s ./merc merc.ini || true"`
  - 通過；stdout 明確出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/error` 僅有 timeout 關機訊息
  - `debug/failexit` 僅有既有 baseline `17201/17208` `Fix_exits`
  - `debug/badobject` 為空
  - 本輪未新增 numbered `log/*`，因此成功訊號以 stdout 與 `debug/*` 檢查為準
- `PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python -X utf8 tools/area_acceptance_gate.py district_loyang_east_market`
  - 回報 `implementation_ready_for_commit`

## Runtime Notes

- 第一版預計建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版房間將落在 `21001-21008`
- 先正式落成 `loyang/553 enter <-> district_loyang_east_market/21001 out`
- 東市會先聚焦商街、票據、馬販與茶湯攤，不提前把整個洛陽商業帶一次做滿
- 已同步 `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Next Step Prompt

`提交 district_loyang_east_market implementation milestone，然後把 tracker 從 in_progress 推進成 done。`
