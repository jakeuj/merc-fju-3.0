# Wild South Sea Route Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_south_sea_route`。此區承接 `city_nanhai` 南向臨海路，把玩家從南海港城的秩序與補給節奏，推進到一段以潮風、棧道、礁岸與近海外航道構成的海路 wild，讓南境主線真正離開陸城、進入更開闊也更不穩定的水域前帶。

## Theme Positioning

- theme: `探險`
- subtheme: `外海南航 / 礁岸水道`
- experience_type: `Wild`
- player_loop_focus: `海路辨位 / 棧道轉場 / 潮汐觀察 / 外航前帶`
- contrast_with_previous_two:
  - 相對於 `dng_serpent_temple` 的封閉石殿與 `city_nanhai` 的港城秩序，`wild_south_sea_route` 應讓玩家感受到視野重新打開，但安全感也被海風、潮汐與礁岸水道迅速抽走
- 世界缺口角色：
  - 把 `city_nanhai` 已預留的南向 `sea_south_route` 正式轉成可持續擴建的 spec-first 海路 wild
  - 為後續外海群島、海上祕境或南洋遠征建立第一層水域前帶
- reserved_room_block: `15601-15630`
- planned_vnum_range: `15601-15630`
- level_range: `98-100`
- external_links:
  - `north`: `city_nanhai` / 南海臨海南口
  - `south`: `sea_outer_isles` / 外海群島預留
  - `east`: `district_nanhai_port` / 港外棧橋預留
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南境外海前帶`
  - `礁岸與棧道海路`
  - `主線離開陸地後的第一段海上 wild`
- 它補的玩家 loop：
  - `從港城補給切進更看天色與潮汐的海路節奏`
  - `靠潮聲、浮標、礁石與棧橋辨認方向`
  - `為更深外海與群島題材建立前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是港城主街與榜示節奏
  - 不再是封閉神殿與血祭壓力
  - 改用開闊水面、礁岸岔道與潮汐風險把節奏轉成海路 wild

## Player Loop Contract

- `主線推進`
  - 玩家由南海南口切出，經過近岸棧道、潮石灣、浮標水道與外航前帶，再決定是否繼續往更深海面或側向港外棧橋
- `地標辨識`
  - 透過浮標、礁石、繩柱、潮痕與遠帆方向判斷哪裡像回港口、哪裡像外海、哪裡像側向水道
- `支線探索`
  - 漁具歇棚
  - 退潮礁坪
  - 風望高臺
- `非平面節奏`
  - `up/down` 用於望臺、坡岸與低潮礁面落差，讓海路不只是平面水道而有真正高低感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0071-wild-south-sea-route.md`
- 建立 `area/wild_south_sea_route/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-entry`
  - `pier-path`
  - `reef-bend`
  - `tide-flat`
  - `watch-rise`
- 將 `南海 / 海路 / 外海 / 棧橋 / 出口` 視為正式 `#Enquire` 候選
- 將 `浮標 / 礁石 / 繩柱 / 潮痕 / 風帆` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供望臺或礁坪高差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
- `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0070-city-nanhai.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
  - `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0070-city-nanhai.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/wild_nanman_jungle/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_nanhai` 已在 spec 與 runtime 內明確預留南向外海南航，適合把主線從港城正式推到海路 wild
  - `progression-map` 的高等帶強調遠征探索，支持在南海之後轉入更開闊的海上前帶而不是再次折回內陸城市
  - `district_jianye_port` ref scaffold 提供了港埠與棧橋語彙，可借來支撐南海後的水路辨位與港外分流設計
  - `players.json / skills.json` 沒有提供南海後穩定城市服務鏈證據，因此先做 `Wild` 更符合 queue variety 與港城後節奏
- `compliance_check`
  - compliant；在 `City` 之後切回 `Wild`，延續 `city_nanhai` 預留南向主線，也維持 family 多樣性

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_south_sea_route/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_south_sea_route/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 wild_south_sea_route 的 spec milestone；commit 後直接做 implementation milestone。`
