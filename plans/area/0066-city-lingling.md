# City Lingling Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_lingling`。此區承接 `city_changsha` 南向主線，把玩家從武陵山的山氣與獵徑節奏，重新收束回一座帶山城氣質、地方奇聞與南境轉運功能的城市 hub，讓荊南主線在更深南方重新恢復城鎮秩序。

## Theme Positioning

- theme: `江湖`
- subtheme: `山城主邑 / 奇聞與轉運`
- experience_type: `City`
- player_loop_focus: `回城補給 / 南線整線 / 奇聞打聽 / 山城服務`
- contrast_with_previous_two:
  - 相對於 `city_changsha` 的官道主城感與 `wild_wuling` 的深山探索，`city_lingling` 應讓玩家感受到一種更地方、更有山城人情與異聞氣味的南境城市節奏
- 世界缺口角色：
  - 把 `city_changsha` 已預留的南向 `city_lingling` 主線正式轉成可持續擴建的 spec-first 城市 hub
  - 為後續 `city_guiyang` 與更南方支線建立新的山城母城
- reserved_room_block: `15101-15130`
- planned_vnum_range: `15101-15130`
- level_range: `84-94`
- external_links:
  - `north`: `city_changsha` / 北向官道
  - `south`: `city_guiyang` / 更南主城預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南境山城`
  - `江湖奇聞`
  - `主線再補給與轉場`
- 它補的玩家 loop：
  - `從山區野外回城整補`
  - `靠榜示、街巷與地方傳聞重建南線方向感`
  - `為桂陽 / 南海一線建立下一個城市節點`
- 它和前兩個已完成 area 的題材差異：
  - 不再是深山野外與高差辨位
  - 不再是荊南北口的官道大城
  - 改用更地方性的山城秩序與奇聞氛圍製造新鮮感

## Player Loop Contract

- `主線推進`
  - 玩家由北向官道切入，經過北門、主街、市集與南門，往更深南境接續
- `城市辨識`
  - 透過榜示、路牌、城巷與差役位置判斷哪裡能補給、哪裡能問路、哪裡像更南出城口
- `支線探索`
  - 市角藥鋪
  - 城巷偏院
  - 山城望樓
- `非平面節奏`
  - `up/down` 用於城樓與坡城高差，維持山城辨位感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0066-city-lingling.md`
- 建立 `area/city_lingling/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-gate`
  - `main-street`
  - `market-quarter`
  - `yamen-quarter`
  - `south-road`
- 將 `零陵 / 長沙 / 城門 / 官府 / 南邊` 視為正式 `#Enquire` 候選
- 將 `告示 / 路牌 / 招牌 / 城門 / 望樓` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供城樓或坡城高差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_lingling/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0064-city-changsha.md`
- `plans/area/0065-wild-wuling.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_lingling/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0064-city-changsha.md`
  - `plans/area/0065-wild-wuling.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_guiyang/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 明確把 `長沙 -> 零陵` 放在同一條南向主線上
  - `題材分布表` 把零陵定位成 `江湖 / 詭異` 的山林城，適合在武陵野外後切回帶地方異聞的城市 family
  - `players.json / skills.json` 沒有要求先跳往其他區線，先把荊南主線城市補穩最合理
  - `ref/sanguo-area-specfirst` 已提供城市 scaffold，可直接改寫成符合目前南線節奏的版本
- `compliance_check`
  - compliant；在 `Wild` 之後切回 `City`，延續長沙主線，也維持 family 與題材變化

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_lingling/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_lingling/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_changsha/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the `14910 <-> 15101` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_changsha/map.md`
  - rewrote `roo/14901-14912` to include the south boundary into `15101`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_lingling/map.md`
  - wrote `roo/15101-15112`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1032.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `city_lingling`
- `area/city_lingling/index` 採首版南境山城 scaffold，房號段 `15101-15130`、序號 `155`
- `mob/16331-16334` 與 `obj/16351-16354` 提供山城掌櫃、城門巡役、官署書吏、坡城哨官與城市補給骨架
- `res/city.res` 與 `shp/supplies.shp` 已建立，keeper 為 `16331`
- `area/city_changsha/map.md` 與 `area/city_lingling/map.md` 已同步把 `14910 <-> 15101` 落成正式 runtime boundary
- `area/city_changsha/roo/14910.roo` 與 `area/city_lingling/roo/15101.roo` 現在雙向一致
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已加入 `city_lingling` loadable registry

## Next Step Prompt

`先 commit 目前 city_lingling 的 implementation milestone；commit 後把它標記為 done，再盤點下一個待建 area。`
