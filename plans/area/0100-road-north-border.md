# Road North Border Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_north_border`。此區承接 `city_xiangping` 的北境邊道路口，把遼東邊城的整補與分流節奏正式送上一段往更北疆道去的軍旅 road，讓 `襄平 -> 北境邊道` 不再只是抽象 world link，而是一段可辨位、可問路、也能收束旅訊與盤查氣味的長路 connector。

## Theme Positioning

- theme: `軍旅`
- subtheme: `往更北疆道`
- experience_type: `Road`
- player_loop_focus: `北境轉場 / 問路歇腳 / 盤查過客 / 邊道傳聞`
- contrast_with_previous_two:
  - 相對於 `city_xiangping` 的邊城整補與 `wild_liaodong_plain` 的開闊平原辨位，`road_north_border` 應把節奏重新收成更具軍務秩序與長路感的 road，而不是繼續維持另一塊 open-field wild。
- 世界缺口角色：
  - 把 `city_xiangping/18309` 的北向預留正式轉成北境邊道節點
  - 為後續更北遼東軍旅節點保留清楚的 road 骨架
- reserved_room_block: `18501-18520`
- planned_vnum_range: `18501-18520`
- level_range: `34-46`
- external_links:
  - `south`: `city_xiangping` / 北境邊道路口
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_north_border/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0098-city-xiangping.md`
- `plans/area/0099-wild-liaodong-plain.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_north_border/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0098-city-xiangping.md`
  - `plans/area/0099-wild-liaodong-plain.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `road_north_border` 放在 `city_xiangping` 北側，且型別就是 `road`，支持在 `Wild` 之後用一段軍旅邊道把節奏重新收束
  - `area/world_map.md` 的 `北平 - 襄平` 北線主幹與 `襄平驛站` 訊號，支持襄平之後存在一段帶旅訊與盤查感的北向 road，而不必立刻跳回另一座城市
  - `players.json / skills.json` 對襄平給出的高頻訊號是 `refresh`、訓練與 `venom` 等服務節點，表示襄平本身已承接整補 loop；下一步更合理的是把城市北口的 outbound road 補齊
  - `city_xiangping` 已保留 `18309 north -> road_north_border` world-link metadata，而 `wild_liaodong_plain` 剛完成 runtime，現在補 `Road` 也符合 `City -> Wild -> Road` 的 family variety
- `compliance_check`
  - compliant；在 `City` 與 `Wild` 之後切到 `Road`，同時回應遼東主線拓撲、舊站服務節點與 queue variety，不是無條件沿最新完成區硬往更深處堆疊 wild

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_north_border/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_north_border/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 tools/mapmd_validate.py area/city_xiangping/map.md`
  - passed (`Validated 9 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_north_border/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\road_north_border\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangping/map.md`
  - passed；同步把 `city_xiangping/18309` 補成 `north -> 18501` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && timeout 45 ./merc merc.test.ini"`
  - passed；因使用中的遊戲實例已占用預設 `3838`，改以臨時測試 port `23838/21234/28888` 做 direct-load smoke，並在 console 看見 `三國歪傳之降龍伏虎開始正常運作`
- `debug/badobject`
  - empty；中途修正 `20954` 的 `ITEM_LIGHT` value 格式後再跑 smoke，已清空 blocker
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `road_north_border` 與 `city_xiangping` 相關新 warning

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20931-20934`、`obj/20951-20954`、`res/road.res`、`shp/supplies.shp`、`roo/18501-18508`
- 已正式落成南側 runtime boundary：`city_xiangping/18309 <-> road_north_border/18501`
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `road_north_border`

## Next Step Prompt

`road_north_border` 的 implementation milestone 已完成；下一步依 queue 規則盤點下一個遼東待建 area，優先檢查是否切進下一個 `Fort` family 節點。`
