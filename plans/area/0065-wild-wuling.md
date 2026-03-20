# Wild Wuling Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_wuling`。此區承接 `city_changsha` 西向山路，把玩家從荊南主城的秩序與補給節奏，轉入一段更偏山行、岔路、靈木與獵徑氣味的武陵山野外帶，讓長沙主線正式伸向更深的山區探索。

## Theme Positioning

- theme: `仙俠`
- subtheme: `山路野外 / 靈木深山`
- experience_type: `Wild`
- player_loop_focus: `山路探索 / 岔線辨位 / 靈木採集 / 山行轉場`
- contrast_with_previous_two:
  - 相對於 `sec_chibi_battlefield` 的戰痕祕區與 `city_changsha` 的主城秩序，`wild_wuling` 應讓玩家感受到一種從城門退入山氣、從官道轉進獵徑的節奏切換，風險不再來自人群或戰火，而來自地形、岔路與深林吸力
- 世界缺口角色：
  - 把 `city_changsha` 已預留的西向 `wild_wuling` world-link 正式轉成可持續擴建的 spec-first 野外帶
  - 為後續 `wild_hidden_valley`、`wild_spirit_forest` 或更深武陵秘境建立山區前帶
- reserved_room_block: `15001-15030`
- planned_vnum_range: `15001-15030`
- level_range: `78-88`
- external_links:
  - `east`: `city_changsha` / 武陵西牌
  - `west`: `wild_hidden_valley` / 隱谷獵徑預留
  - `north`: `city_jiangling` / 北山關路預留
  - `east`: `wild_spirit_forest` / 東岔靈林預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `武陵山路`
  - `靈木與獵徑`
  - `主城外第一段深山野外`
- 它補的玩家 loop：
  - `從主城補給切進山行探索`
  - `靠岔路、石碑與樹痕辨認地形`
  - `為更深秘境與山谷支線建立前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是主城的官道、市集與榜示節奏
  - 不再是帶歷史回聲的焦土戰場
  - 改用山霧、古樹、獵路與高差把節奏轉成深山野外探索

## Player Loop Contract

- `主線推進`
  - 玩家由長沙西牌切入，先經過山腳岔口與石碑路段，再進到靈木坡、獵徑深帶與山腹高地
- `地標辨識`
  - 透過路牌、石碑、古樹裂痕與山風聲判斷哪裡像回城口、哪裡像更深山路
- `支線探索`
  - 獵戶歇腳棚
  - 靈木坡面
  - 霧帶窄徑
- `非平面節奏`
  - `up/down` 用於山坡、崖階與谷地落差，讓武陵山不是平面草道而是真正有高低感的山行區

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0065-wild-wuling.md`
- 建立 `area/wild_wuling/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `east-entry`
  - `stone-way`
  - `spirit-grove`
  - `ridge-path`
  - `mist-hollow`
- 將 `武陵 / 長沙 / 山路 / 出口 / 谷地` 視為正式 `#Enquire` 候選
- 將 `石碑 / 足跡 / 靈木 / 裂岩 / 古藤` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供山坡或谷地落差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_wuling/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0064-city-changsha.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_wuling/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0064-city-changsha.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_lingling/map.md`
  - `ref/sanguo-area-specfirst/area/wild_hidden_valley/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 顯示 `江陵 - 武陵 - 長沙` 這條內陸山線與 `長沙` 西向延伸高度吻合
  - `題材分布表` 把 `武陵` 定位成 `仙俠 / 探險` 的神秘山林，適合在主城後切入野外 family
  - `players.json / skills.json` 沒有要求此刻先回到另一座城市，先補一段高辨識度山區 wild 可維持 queue 多樣性
  - `ref/sanguo-area-specfirst` 已提供可改寫 scaffold，可直接轉成目前長沙西向山路所需版本
- `compliance_check`
  - compliant；在 `City` 之後切回 `Wild`，延續長沙預留 world-link，也維持 family 與題材變化

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_wuling/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_wuling/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_changsha/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the `14912 <-> 15001` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_changsha/map.md`
  - rewrote `roo/14901-14912` to include the west boundary into `15001`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_wuling/map.md`
  - wrote `roo/15001-15012`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1031.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `wild_wuling`
- `area/wild_wuling/index` 採首版武陵山前帶 scaffold，房號段 `15001-15030`、序號 `154`
- `mob/16231-16234` 與 `obj/16251-16254` 提供山口引路客、武陵獵戶、靈木守望者、霧谷拾跡客與野外補給骨架
- `res/wild.res` 與 `shp/supplies.shp` 已建立，keeper 為 `16231`
- `area/city_changsha/map.md` 與 `area/wild_wuling/map.md` 已同步把 `14912 <-> 15001` 落成正式 runtime boundary
- `area/city_changsha/roo/14912.roo` 與 `area/wild_wuling/roo/15001.roo` 現在雙向一致
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已加入 `wild_wuling` loadable registry

## Next Step Prompt

`先 commit 目前 wild_wuling 的 implementation milestone；commit 後把它標記為 done，再盤點下一個待建 area。`
