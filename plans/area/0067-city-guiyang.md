# City Guiyang Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_guiyang`。此區承接 `city_lingling` 南向主線，把玩家從零陵山城的地方奇聞與轉運節奏，再收束進一座更靠南境邊緣、帶江湖與仙俠混合氣味的城鎮 hub，讓桂陽成為南海與南蠻方向前的主線中繼城。

## Theme Positioning

- theme: `江湖`
- subtheme: `南嶺城鎮 / 邊地轉運`
- experience_type: `City`
- player_loop_focus: `回城補給 / 南線整補 / 邊地問路 / 更南轉場`
- contrast_with_previous_two:
  - 相對於 `wild_wuling` 的深山探索與 `city_lingling` 的山城奇聞，`city_guiyang` 應讓玩家感受到更靠南、更帶邊地氣味的城鎮節奏，像是所有再往南海與南蠻前的人都會在這裡重新整理行裝
- 世界缺口角色：
  - 把 `city_lingling` 已預留的南向 `city_guiyang` 主線正式轉成可持續擴建的 spec-first 城鎮 hub
  - 為後續 `city_nanhai` 與 `wild_nanman_jungle` 建立南境最後一層穩定母城
- reserved_room_block: `15201-15230`
- planned_vnum_range: `15201-15230`
- level_range: `90-100`
- external_links:
  - `north`: `city_lingling` / 零陵北路
  - `south`: `city_nanhai` / 南海港路預留
  - `west`: `wild_nanman_jungle` / 南蠻外帶預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南境邊地城鎮`
  - `更深南線前的最後主城補給`
  - `江湖與邊地傳聞混合氣味`
- 它補的玩家 loop：
  - `從零陵再往南前重新整補`
  - `靠路牌、榜示與地方商旅確認南海 / 南蠻方向`
  - `為最南主線建立穩定轉場節點`
- 它和前兩個已完成 area 的題材差異：
  - 不再是山城與地方奇聞的節奏
  - 不再是深山辨位的野外節奏
  - 改用更邊地、更臨近南境末段的城鎮氛圍做變化

## Player Loop Contract

- `主線推進`
  - 玩家由北向官道切入，經過北門、主街、市集與南口，再往更南的港路與邊地延伸
- `城市辨識`
  - 透過榜示、路牌、商旅與差役位置判斷哪裡能補給、哪裡能問路、哪裡像更南出城口
- `支線探索`
  - 南貨鋪
  - 巷內偏院
  - 城樓望口
- `非平面節奏`
  - `up/down` 用於城樓與坡地高差，維持邊地城鎮不是平面街格

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0067-city-guiyang.md`
- 建立 `area/city_guiyang/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-gate`
  - `main-street`
  - `market-quarter`
  - `yamen-quarter`
  - `south-road`
- 將 `桂陽 / 零陵 / 南海 / 南蠻 / 官府` 視為正式 `#Enquire` 候選
- 將 `告示 / 路牌 / 招牌 / 城門 / 城樓` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供城樓或坡地高差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_guiyang/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0066-city-lingling.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_guiyang/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0066-city-lingling.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
  - `ref/sanguo-area-specfirst/area/wild_nanman_jungle/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world_map` 明確把 `零陵 -> 桂陽 -> 南海` 放在同一條南向主線上
  - `題材分布表` 把桂陽定位成帶 `江湖 / 仙俠` 氣味的南方城鎮，適合在零陵後作為邊地城鎮節點
  - `players.json / skills.json` 沒有要求先跳到非南線主骨架，先把南境城市鏈補穩最合理
  - `ref/sanguo-area-specfirst` 已提供城市 scaffold，可直接改寫成符合目前南線節奏的版本
- `compliance_check`
  - compliant；延續 `City` 主線推進，且為南海與南蠻前的母城補位，不是跳去無連接支線

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_guiyang/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_guiyang/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_lingling/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15110 <-> 15201`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_lingling/map.md`
  - rewrote `roo/15101-15112` to include the `15110 south -> 15201 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_guiyang/map.md`
  - wrote `roo/15201-15212`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup smoke test passed; success signal found in `log/1032.log`
- `debug/badobject`
  - empty after smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path, no new area loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `city_guiyang`，保留房號段 `15201-15230`
- `area/city_guiyang/index` 已建立，`Serial 156`
- 第一輪 runtime scaffold 已加入：
  - `mob/16431-16434`
  - `obj/16451-16454`
  - `res/city.res`
  - `shp/supplies.shp`
- `city_lingling/15110 <-> city_guiyang/15201` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `city_guiyang`

## Next Step Prompt

`先 commit 目前 city_guiyang 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
