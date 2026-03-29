# Wild Chenliu West Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_chenliu_west`。此區承接 `city_chenliu` 的西城門外牌樓，把原本還停在抽象「洛陳驛路」語意上的西向邊界，先收斂成一段真正可載入、可辨位、也更符合城郊節奏的西郊母帶。它不該直接假裝自己已經是通往洛陽的整段大路，而要讓玩家清楚感到：陳留的城牆與盤查還在背後，但茶亭、田埂、柳溝與流民營灰地已經開始把人交給中原外帶。

## Theme Positioning

- theme: `江湖`
- subtheme: `西郊 / 茶亭`
- experience_type: `Wild`
- player_loop_focus: `回城 / 問路 / 茶亭補給 / 郊道辨位 / 城外灰帶探索`
- contrast_with_previous_two:
  - 相對於 `city_wan` 鏈上的 `road_wan` 與 `wild_wan_outer`，`wild_chenliu_west` 應更強調中原城郊的官道殘秩序與旅人灰帶，而不是再做一條筆直主線 road。
  - 相對於上一輪 `district_chenliu_station` 的驛站分區，這一區要把節奏從城市內部的旅行服務切回城外風塵、側路與可疑人流。
- 世界缺口角色：
  - 把 `city_chenliu/13801 west` 的成熟城門外 stub，正式轉成 `wild_chenliu_west/20801 east`
  - 為後續是否往更西側延伸 `road_chenliu_loyang` 或其他中原過渡帶，先建立一段不與 `loyang/556 <-> loyang_outskirts/7501` 衝突的西郊母帶
- reserved_room_block: `20801-20820`
- planned_vnum_range: `20801-20820`
- level_range: `14-24`
- external_links:
  - `east`: `city_chenliu` / 西城門外牌樓 (`13801`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_chenliu_west/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/maps.json`
- `area/city_chenliu/map.md`
- `area/loyang_outskirts/map.md`
- `area/loyang/roo/556.roo`
- `plans/area/0053-city-chenliu.md`
- `plans/area/0122-district-chenliu-station.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_chenliu_west/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `docs/3yWebsite/docs/data/maps.json`
  - `area/city_chenliu/map.md`
  - `area/loyang_outskirts/map.md`
  - `area/loyang/roo/556.roo`
  - `plans/area/0053-city-chenliu.md`
  - `plans/area/0122-district-chenliu-station.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/road_chenliu/map.md`
  - `ref/sanguo-area-specfirst/area/road_chenliu_loyang/map.md`
  - `docs/3yWebsite/map/chenliu.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `area/world_map.md` 已明列 `陳留西郊`，而不是只把陳留西側表述成一條已完成的直線驛路
  - `city_chenliu` 的 `13801` 已有成熟 west-edge 城門房，適合先接一段可載入的西郊外帶，再往更西側細分 road
  - `loyang/556` 已正式接到 `loyang_outskirts/7501`，代表洛陽東陽門的東郊拓樸已穩定存在；若此時硬做 `road_chenliu_loyang`，反而會撞到既有東郊線
  - `players.json / skills.json` 對陳留的強訊號集中在城內 teacher / service loop，沒有要求西側邊界必須先做長距離主線官道，支持先補一段灰帶城郊 wild
  - `wild_chenliu_west` scaffold 直接提供茶亭、路碑、樹叢與流寇感，能自然延續 `city_chenliu` 西門盤查之外的第一段過渡帶
- `compliance_check`
  - compliant；在 `district_chenliu_station` 之後選擇 `Wild`，成功避開再堆同質 `District`，也比目前邊界尚未對齊的 `road_chenliu*` 更 actionable

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_chenliu_west/map.md`
  - 通過，`8 rooms`、`0 error(s)`、`0 warning(s)`
- `python -X utf8 tools/mapmd_validate.py area/city_chenliu/map.md`
  - 通過，更新後的 `city_chenliu/13801 west -> wild_chenliu_west/20801` world link 與 mapmd-json 一致
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_chenliu_west/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_chenliu_west/map.md`
  - 通過，寫出 `20801-20808`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md`
  - 通過，重生包含新西向邊界的 `13801.roo`
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
- `python -X utf8 tools/area_acceptance_gate.py wild_chenliu_west`
  - 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `wild_chenliu_west` 的 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `20801-20808`
- 已正式落成 `city_chenliu/13801 west <-> wild_chenliu_west/20801 east` runtime boundary
- `city_chenliu` 的 west-edge spec 已從抽象 `road_chenliu_loyang` 收斂成可載入的 `wild_chenliu_west`，避免與 `loyang/556 <-> loyang_outskirts/7501` 的既有東郊拓樸衝突
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登記新區

## Next Step Prompt

`提交 wild_chenliu_west implementation milestone commit，完成 tracker gate 收尾後再回到 queue 規則盤點下一個待建 area。`
