# District Chenliu Station Initial Area Plan

## Summary

建立下一個待建新 AREA：`district_chenliu_station`。此區承接 `city_chenliu` 的南驛前院，把原本只停在「往許昌 / 下一站」語意上的驛站轉接帶，正式展成有車馬棚、旅票櫃、行李長棚、旅舍前廊與小販棚口的人流分區。這裡不該只是 `city_chenliu` 的附屬巷道，而要讓玩家明顯感到自己正從中原樞紐城的主街秩序，走進一段真正會把旅人、差役、消息與下一段長路接手的驛站 district。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `驛站 / 補給`
- experience_type: `District`
- player_loop_focus: `問路 / 車馬轉接 / 驛站補給 / 旅宿停留 / 南向傳聞導流`
- contrast_with_previous_two:
  - 相對於 `road_wan` 的線性官道與 `wild_wan_outer` 的城郊灰帶，`district_chenliu_station` 應把節奏重新收進有功能分工的人流分區，形成 `Road -> Wild -> District` 的 family 切換。
- 世界缺口角色：
  - 把 `city_chenliu/13816` 的南驛前院正式轉成 `district_chenliu_station/20701` 的 runtime boundary
  - 為陳留後續更南向的許昌線、驛馬補給與旅宿傳聞 loop 建立第一段可載入的驛站分區
- reserved_room_block: `20701-20720`
- planned_vnum_range: `20701-20720`
- level_range: `15-25`
- external_links:
  - `north`: `city_chenliu` / 陳留驛站前院 (`13816`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/district_chenliu_station/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_chenliu/map.md`
- `area/city_chenliu/roo/13816.roo`
- `plans/area/0053-city-chenliu.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/district_chenliu_station/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_chenliu/map.md`
  - `area/city_chenliu/roo/13816.roo`
  - `plans/area/0053-city-chenliu.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/road_chenliu/map.md`
  - `ref/sanguo-area-specfirst/area/road_chenliu_loyang/map.md`
  - `docs/3yWebsite/map/chenliu.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `city_chenliu` 現有 spec 已把 `13816` 定位成南驛前院並明確預留 `south -> district_chenliu_station`，代表掛接點已成熟，不需再額外整理方向契約
  - `world-graph` 直接把 `district_chenliu_station` 列為 `district / 歷史城市 / 15-25` 節點，剛好補上 `city_chenliu` 已經鋪好的旅行與轉站 loop
  - `players.json` 對陳留的強訊號集中在 `浪人 / bravo hashin an`、`震南山 / zhen nan shan` 與初中段練功導流，支持本輪不要再補一條抽象官道，而是優先把城市內的 travel / service density 做完整
  - `road_chenliu` 與 `road_chenliu_loyang` 雖然題材合理，但目前缺少一個和 `city_chenliu/13816` 同等成熟的 `loyang` 邊界落點；相較之下先補驛站 district 的風險明顯更低
- `compliance_check`
  - compliant；本輪從空 queue 重建後選 `district_chenliu_station`，既避開 `wild_wan_outer` 後再堆一段 `Wild`，也避免在尚未對齊洛陽邊界前硬開新的 `Road`

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/district_chenliu_station/map.md`
  - 通過，`8 rooms`、`0 error(s)`、`0 warning(s)`
- `python -X utf8 tools/mapmd_validate.py area/city_chenliu/map.md`
  - 通過，更新後的 `city_chenliu/13816 south -> district_chenliu_station/20701` world link 與 mapmd-json 一致
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_chenliu_station/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/district_chenliu_station/map.md`
  - 通過，寫出 `20701-20708`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md`
  - 通過，重生包含新南向邊界的 `13816.roo`
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
- `python -X utf8 tools/area_acceptance_gate.py district_chenliu_station`
  - 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `district_chenliu_station` 的 `index / roo / mob / obj / res / shp` 最小可載入集合，首版房間落在 `20701-20708`
- 已正式落成 `city_chenliu/13816 south <-> district_chenliu_station/20701 north` runtime boundary
- 中途修正 `21974.obj` 的 weapon loader 型別，將不存在的 `WEAPON_STAFF` 改成 loader 可接受的 `WEAPON_CLUB`
- `city_chenliu/index`、`area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登記新區

## Next Step Prompt

`提交 district_chenliu_station implementation milestone commit，完成 tracker gate 收尾後再回到 queue 規則盤點下一個待建 area。`
