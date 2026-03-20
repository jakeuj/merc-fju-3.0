# City Nanhai Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_nanhai`。此區承接 `city_guiyang` 南向主線，把玩家從桂陽這座邊地轉運城，再收束進一座真正帶海港、遠航與南境終點氣味的港市 hub，讓南海成為南方主線的城市落點，而不是只停在邊林與祕殿支線。

## Theme Positioning

- theme: `探險`
- subtheme: `海港 / 遠航`
- experience_type: `City`
- player_loop_focus: `港城補給 / 海路問訊 / 南線收束 / 遠航轉場`
- contrast_with_previous_two:
  - 相對於 `wild_nanman_jungle` 的濕熱密林與 `dng_serpent_temple` 的封閉血祭壓力，`city_nanhai` 應讓玩家感受到空氣重新打開、視野變寬、秩序與煙火氣回來，但主題已從山城轉成港城與遠行
- 世界缺口角色：
  - 把 `city_guiyang` 已預留的南向 `city_nanhai` 主線正式轉成可持續擴建的 spec-first 港市 hub
  - 為後續海港支線、外海航路與更南遠征建立穩定母城
- reserved_room_block: `15501-15530`
- planned_vnum_range: `15501-15530`
- level_range: `96-100`
- external_links:
  - `north`: `city_guiyang` / 桂陽南路
  - `south`: `sea_south_route` / 外海南航預留
  - `east`: `district_nanhai_port` / 港埠棧橋預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南境海港城市`
  - `遠航與商旅收束點`
  - `主線最南端的城市節奏`
- 它補的玩家 loop：
  - `從桂陽下行後重新回到城市補給與問路`
  - `靠告示、碼頭消息與商旅口風確認海路與更南方向`
  - `為後續港埠 / 外海 / 南洋題材建立母城`
- 它和前兩個已完成 area 的題材差異：
  - 不再是密林辨位與藤路壓力
  - 不再是神殿下探與血祭封印
  - 改用海風、棧橋、市集與遠航氣味把節奏重新打開

## Player Loop Contract

- `主線推進`
  - 玩家由北向官道入城，穿過城門、港街、市集與臨海路，再往更南航路或港埠分區延伸
- `城市辨識`
  - 透過碼頭告示、港務差役、南貨商與遠航招牌判斷哪裡能補給、哪裡能問海路、哪裡像出海南口
- `支線探索`
  - 南貨行
  - 港務前院
  - 臨海望臺
- `非平面節奏`
  - `up/down` 用於望臺、坡港與棧橋高差，維持港城不是純平面街格

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0070-city-nanhai.md`
- 建立 `area/city_nanhai/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-gate`
  - `harbor-street`
  - `market-quarter`
  - `port-office`
  - `south-seafront`
- 將 `南海 / 桂陽 / 碼頭 / 海路 / 官府` 視為正式 `#Enquire` 候選
- 將 `告示 / 招牌 / 路牌 / 城門 / 棧橋` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供望臺或坡港高差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0067-city-guiyang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0067-city-guiyang.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/wild_nanman_jungle/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 明確把 `零陵 -> 桂陽 -> 南海` 放在同一條南向主線上，適合在桂陽之後把節奏推到真正的海港城市
  - `題材分布表` 把 `南海` 定位成 `探險 / 江湖` 的海上貿易節點，能有效拉開和桂陽山城、南蠻密林的體驗差
  - `players.json / skills.json` 沒有要求南境主線停在支線 dungeon，因此先把港市 hub 補穩更合理
  - `ref/sanguo-area-specfirst` 已提供可改寫 scaffold，可直接轉成目前南境最南端港城所需版本
- `compliance_check`
  - compliant；在 `Dungeon` 之後切回 `City`，延續 `city_guiyang` 預留南向主線，也恢復主線母城節奏

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_nanhai/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_nanhai/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_guiyang/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15210 <-> 15501`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_guiyang/map.md`
  - rewrote `roo/15201-15212` to include the `15210 south -> 15501 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_nanhai/map.md`
  - wrote `roo/15501-15512`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1036.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `city_nanhai`，保留房號段 `15501-15530`
- `area/city_nanhai/index` 已建立，`Serial 159`
- 第一輪 runtime scaffold 已加入：
  - `mob/16731-16734`
  - `obj/16751-16754`
  - `res/city.res`
  - `shp/supplies.shp`
- `city_guiyang/15210 <-> city_nanhai/15501` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `city_nanhai`

## Next Step Prompt

`先 commit 目前 city_nanhai 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
