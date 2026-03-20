# City Xiangyang Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_xiangyang`。此區承接 `fort_hulao` 的軍事門戶節奏，但把玩家重新帶回一座活著的荊州主城，讓城門盤查、市集煙火、衙署秩序與水陸交通一起成為中段主線的城市 hub。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `荊州門戶 / 軍旅樞紐`
- experience_type: `City`
- player_loop_focus: `補給 / 問路 / 地方情報 / 水陸交通 / 軍旅與民生並存`
- contrast_with_previous_two:
  - 相對於 `dng_guandu_battlefield` 的戰地殘局與 `fort_hulao` 的重兵關隘，`city_xiangyang` 應讓玩家感受到秩序、商旅、人流與地方勢力流動重新變得可見
- 世界缺口角色：
  - 把中段主線從中原軍旅關卡推進到荊州門戶主城
  - 為後續 `wild_jiangxia_river` 提供水路、碼頭與南向外野的母城節點
- reserved_room_block: `14201-14230`
- planned_vnum_range: `14201-14230`
- level_range: `35-45`
- external_links:
  - `north`: `fort_fancheng` / 樊城方向
  - `south`: `jingxiang_road` / 荊襄大道
  - `east`: `wild_jiangxia_river` / 江夏水道
  - `west`: 荊州內陸與軍道
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `襄陽主城`
  - `荊州軍民交會樞紐`
  - `水陸交通與地方秩序並存`
- 它補的玩家 loop：
  - `補給`
  - `問路`
  - `打探地方消息`
  - `由主城轉向江夏水路與荊州支線`
- 它和前兩個已完成 area 的題材差異：
  - 不再是純軍事 choke point
  - 改用主街、市集、碼頭與官署建立城市節奏

## Player Loop Contract

- `補給與城市服務`
  - 市集
  - 客棧
  - 錢莊
  - 武器 / 防具 / 藥材
- `地方情報與官署 loop`
  - 官府
  - 差役
  - 榜文
  - 跑腿送信
- `交通 loop`
  - 北上樊城 / 新野
  - 南接荊襄大道
  - 東出江岸與碼頭，為 `wild_jiangxia_river` 預熱

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0057-city-xiangyang.md`
- 建立 `area/city_xiangyang/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `south-gate`
  - `main-avenue`
  - `market-quarter`
  - `yamen-quarter`
  - `east-wharf`
- 將 `城門 / 市集 / 碼頭 / 官府 / 去路` 視為正式 `#Enquire` 候選
- 將 `告示 / 招牌 / 路牌 / 城門 / 旗幟` 視為正式 `#Keyword` 候選
- 至少保留一組 `enter/out` 室內或碼頭轉場
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/city_xiangyang/map.md` 生成 `roo/14201-14212`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 將 area 登錄到 `area/directory.lst`
- 正式把 `jingxiang_road/9301` 與 `city_xiangyang/14201` 做成雙向 runtime boundary
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `city_xiangyang` 是 midgame 主線城市，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `south-gate`
  - 南城門、盤查棚、入城大道
- `main-avenue`
  - 主街、十字口、旅人流
- `market-quarter`
  - 客棧、市集、商舖與補給
- `yamen-quarter`
  - 官府、榜文、差役與軍旅資訊
- `east-wharf`
  - 碼頭、江風、水路路牌與南東向交通

## Suggested Theme Hooks

- `south-gate`
  - 讓玩家明確感受到這是荊州門戶，而不是普通城鎮
- `main-avenue`
  - 用人潮與招牌建立城市熱度
- `market-quarter`
  - 把補給與商旅後勤整理成一眼可懂的主城 loop
- `yamen-quarter`
  - 用衙署、差役與榜文補足地方治理感
- `east-wharf`
  - 提前把水路與江夏方向的空氣吹進城市，不讓下一區突然變成孤立新題材

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_xiangyang/map.md`
- `docs/3yWebsite/map/shanyan.html`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_xiangyang/map.md`
  - `docs/3yWebsite/map/shanyan.html`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - 主線推進到荊州門戶後，需要一座比關隘更有民生與交通厚度的主城
  - `shanyan.html` 提供襄陽舊站的主街、市集、碼頭與官府分區感
  - spec-first 參考稿提供城門 / 主街 / 服務區的基本骨架，但本區改寫為更貼近當前 queue 的 city-hub 版本
- `compliance_check`
  - compliant；在 `Fort` 之後切回 `City`，維持 queue variety，並為下一個水路 `Wild` area 做題材導流

## First-Round Validation

- `area/city_xiangyang/map.md` 必須包含有效 `mapmd-json`
- 城市服務與交通 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `city_xiangyang` 不得退化成只有世界連線的空城；必須保留市集、官府與碼頭辨識度

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_xiangyang/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangyang/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/jingxiang_road/map.md`
  - passed with `0 error(s), 1 warning(s)`; remaining warning is the pre-existing `reserved_room_block` metadata gap, not a runtime blocker
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/jingxiang_road/map.md`
  - rewrote `roo/9301-9310` to include the north boundary into `14201`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangyang/map.md`
  - wrote `roo/14201-14212`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1022.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `city_xiangyang`
- `area/city_xiangyang/index` 採首版城市 scaffold，房號段 `14201-14230`、序號 `146`
- `mob/15431-15434` 與 `obj/15451-15454` 提供客棧掌櫃、巡檢兵、差役頭目、碼頭護行與城市補給骨架
- `res/city.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15431`
- `area/jingxiang_road/map.md` 與 `area/city_xiangyang/map.md` 已同步把 `9301 <-> 14201` 落成正式 runtime boundary
- `area/jingxiang_road/roo/9301.roo` 與 `area/city_xiangyang/roo/14201.roo` 現在雙向一致

## Next Step Prompt

`先 commit 目前 city_xiangyang 的 implementation milestone；commit 後把此區標記為 done，再開始 wild_jiangxia_river 的 spec milestone。`
