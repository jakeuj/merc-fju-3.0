# City Changsha Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_changsha`。此區承接 `city_chaisang` 南向主線，把玩家從江岸古戰場與柴桑轉場節奏，再次收束回一座更偏荊南內陸的主城 hub，讓南線探索重新回到官道、市集、驛站與地方勢力消息匯流的城市節奏。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `荊南主城 / 南境轉運 hub`
- experience_type: `City`
- player_loop_focus: `回城補給 / 南線轉場 / 問路整線 / 荊南主城服務`
- contrast_with_previous_two:
  - 相對於 `city_chaisang` 的江岸轉場與 `sec_chibi_battlefield` 的戰痕祕區，`city_changsha` 應讓玩家感受到更穩定、更內陸、也更像荊南主城的秩序感，讓節奏從江風與焦土重新回到街市、驛路與官署
- 世界缺口角色：
  - 把 `city_chaisang` 已預留的南向 `city_changsha` 主線正式轉成可持續擴建的 spec-first 城市 hub
  - 為後續 `city_lingling`、`wild_wuling` 與更深荊南線建立穩定母城
- reserved_room_block: `14901-14930`
- planned_vnum_range: `14901-14930`
- level_range: `72-82`
- external_links:
  - `north`: `city_chaisang` / 荊南北路
  - `south`: `city_lingling` / 更南主城預留
  - `west`: `wild_wuling` / 山路與獵徑預留
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `荊南主城`
  - `驛站與市集節奏`
  - `地方官署與南線消息中樞`
- 它補的玩家 loop：
  - `從戰場與支線回到主城整補`
  - `靠路牌、榜示與差役重新建立南線方向感`
  - `為零陵 / 武陵 / 南境支線建立穩定出發點`
- 它和前兩個已完成 area 的題材差異：
  - 不再是帶焦土回聲的戰場祕區
  - 不再是江岸與碼頭感更重的東口城市
  - 改用內陸主城、驛路流動與南境消息網製造新的城市節奏

## Player Loop Contract

- `主線推進`
  - 玩家由北向官道切入，經過北門、主街、市集與官署，再往南接出更深荊南主線
- `城市辨識`
  - 透過驛牌、榜示、市聲與巡役分布判斷哪裡能補給、哪裡能問路、哪裡像更南的出城口
- `支線探索`
  - 驛站偏院
  - 藥材街角
  - 南門馬棚
- `非平面節奏`
  - `up/down` 用於城樓、望臺與後巷階差，維持主城不只是平面街格

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0064-city-changsha.md`
- 建立 `area/city_changsha/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-gate`
  - `main-street`
  - `market-quarter`
  - `yamen-quarter`
  - `south-road`
- 將 `長沙 / 柴桑 / 驛站 / 官府 / 南邊` 視為正式 `#Enquire` 候選
- 將 `告示 / 路牌 / 城門 / 驛旗 / 馬棚` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供城樓或望臺使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_changsha/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0062-city-chaisang.md`
- `plans/area/0063-sec-chibi-battlefield.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_changsha/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0062-city-chaisang.md`
  - `plans/area/0063-sec-chibi-battlefield.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `ref/sanguo-area-specfirst/area/city_lingling/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 明確把 `柴桑 -> 長沙` 放在同一條南向主線上，且 `city_chaisang` 已長期預留這個 world-link
  - `題材分布表` 把長沙定位成荊南核心城市，能在戰場支線後把節奏重新拉回主城補給與轉運 hub
  - `players.json / skills.json` 沒有強烈要求此刻改跳另一條未接續的東吳或蜀線，因此先把荊南主城補穩最合理
  - `ref/sanguo-area-specfirst` 已提供城市 scaffold，可直接改寫成符合目前 room block 與南線節奏的版本
- `compliance_check`
  - compliant；在 `Secret` 之後切回 `City`，延續 `city_chaisang` 已預留主線，也維持 queue 的題材與 family 變化

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_changsha/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_changsha/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 city_changsha 的 spec milestone；commit 後直接做 implementation milestone。`
