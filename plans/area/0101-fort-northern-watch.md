# Fort Northern Watch Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_northern_watch`。此區承接 `fort_yijing` 的北望樓，把北境軍鎮再往上一層推成更純粹的高處哨站與狼煙 fort，讓 `易京 -> 北方哨樓` 不再只是抽象 `up/down` world link，而是一段帶著戒備、軍令與高處巡望壓力的前線 watch fort。

## Theme Positioning

- theme: `軍旅`
- subtheme: `哨站 / 狼煙`
- experience_type: `Fort`
- player_loop_focus: `高處巡望 / 軍令交接 / 邊境戒備 / 狼煙預警`
- contrast_with_previous_two:
  - 相對於 `road_north_border` 的長路收束感與 `city_xiangping` 的邊城整補節奏，`fort_northern_watch` 應把體驗重新壓成更垂直、更高處、也更前線化的 watch fort，而不是再做一段平面 road 或城市服務區。
- 世界缺口角色：
  - 把 `fort_yijing/17907` 的 `up` 預留正式轉成北方哨樓節點
  - 為後續更北前線或狼煙事件帶保留高處 watch fort 骨架
- reserved_room_block: `18601-18620`
- planned_vnum_range: `18601-18620`
- level_range: `36-48`
- external_links:
  - `down`: `fort_yijing` / 北望樓
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/fort_northern_watch/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0094-fort-yijing.md`
- `plans/area/0100-road-north-border.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/fort_northern_watch/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0094-fort-yijing.md`
  - `plans/area/0100-road-north-border.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/sec_starfall_crater/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 只給出 `fort_yijing up -> fort_northern_watch / down -> fort_yijing` 這組明確連線，表示它是北境鏈上最自然的下一個 `Fort` family 節點
  - `fort_yijing` 現有 spec/runtime 已保留 `17907 up -> fort_northern_watch` metadata，現在補這個 spec 能直接承接既有分流母點
  - `ref` scaffold 將其定成 `哨站 / 狼煙` 的高處 watch fort，能和 `road_north_border` 的平面旅途感形成清楚題材切換
  - `players.json / skills.json` 對襄平高頻訊號仍集中在服務與訓練，不要求繼續擴城市內環；此時切回前線 `Fort` 比再補一段一般 road 更能維持 family variety
- `compliance_check`
  - compliant；在 `Road` 之後切到 `Fort`，同時回應 `world-graph` 的既有 `up/down` 預留與北境題材節奏，不是任意跳到無關區塊

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_northern_watch/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_northern_watch/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Runtime Notes

- pending

## Next Step Prompt

`先完成 fort_northern_watch 的 spec milestone：跑 map validate 與 generator --validate-only，通過後自動 commit；接著直接做 implementation milestone，正式把 fort_yijing/17907 接進北方哨樓。`
