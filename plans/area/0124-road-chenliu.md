# Road Chenliu Initial Area Plan

## Summary

建立下一個待建新 AREA：`road_chenliu`。此區承接 `wild_chenliu_west` 的 `更西荒道`，把原本仍停在「未來也許會一路接回洛陽」的抽象 west-edge，先落成一段真正可載入、可補給、可盤查、也明確屬於 `Road` family 的驛路骨架。這一版不硬把 Luoyang 端塞進已經穩定掛著 `loyang_outskirts` 的東陽門出口，而是先把 `陳留西郊 -> 西行驛路` 這段玩家實際會走到的交通層做紮實，讓後續 Luoyang 端能在不撞既有拓樸的前提下再掛接。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `西行驛道 / 中原長路`
- experience_type: `Road`
- player_loop_focus: `問路 / 歇腳 / 補給 / 盤查 / 驛路辨位`
- contrast_with_previous_two:
  - 相對於上一輪 `wild_chenliu_west` 的茶亭灰帶與流民側路，`road_chenliu` 應回到有車轍、木堠、驛棚與差役秩序的正式長路節奏。
  - 相對於更早的 `district_chenliu_station`，本區不再是城內旅行服務分區，而是把服務語意往真正離城後的野外驛路展開。
- 世界缺口角色：
  - 把 `wild_chenliu_west/20808` 的 `future-road` west-edge，正式落成 `road_chenliu/20901 east`
  - 先建立 `陳留西郊 -> 西行驛路` 的 loadable road 骨架，保留 Luoyang 端世界契約給後續不衝突的 gate / outskirts 設計
- reserved_room_block: `20901-20920`
- planned_vnum_range: `20901-20920`
- level_range: `15-25`
- external_links:
  - `east`: `wild_chenliu_west` / 更西荒道 (`20808`)
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/world-graph.md`
- `ref/sanguo-area-specfirst/area/road_chenliu/map.md`
- `ref/sanguo-area-specfirst/area/road_chenliu_loyang/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/wild_chenliu_west/map.md`
- `area/wild_chenliu_west/roo/20808.roo`
- `area/loyang_outskirts/map.md`
- `area/loyang/roo/556.roo`
- `plans/area/0123-wild-chenliu-west.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/world-graph.md`
  - `ref/sanguo-area-specfirst/area/road_chenliu/map.md`
  - `ref/sanguo-area-specfirst/area/road_chenliu_loyang/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/wild_chenliu_west/map.md`
  - `area/wild_chenliu_west/roo/20808.roo`
  - `area/loyang_outskirts/map.md`
  - `area/loyang/roo/556.roo`
  - `plans/area/0123-wild-chenliu-west.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/chenliu.html`
  - `docs/3yWebsite/map/loyang.html`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `ref/world-graph.md` 仍把 `road_chenliu` 視為 `city_loyang <-> city_chenliu` 之間較 canonical 的 road 節點，優先度高於只剩單側 scaffold 的 `road_chenliu_loyang`
  - `wild_chenliu_west` 已先把陳留西門外從抽象直通長路收斂成可載入的近郊灰帶，因此下一步切回 `Road` family 很自然，也能滿足 queue variety
  - `loyang/556` 已正式接到 `loyang_outskirts/7501`，代表洛陽東陽門 east edge 已被穩定佔用；本輪若硬把 `road_chenliu` 或 `road_chenliu_loyang` 直接掛在同一出口，會和既有東郊 topology 衝突
  - `players.json / skills.json` 沒有顯示 Luoyang 東門必須優先再開另一條同向交通層，反而支持先把陳留西向的 service / travel loop 做成真正可走的 road
- `compliance_check`
  - compliant；在 `wild_chenliu_west` 之後切回 `Road`，避免再堆同質郊野，也沒有為了滿足 world-graph 直線敘事而破壞 `loyang_outskirts` 既有 east-edge 契約

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/road_chenliu/map.md`
  - 通過，`8 rooms`、`0 error(s)`、`0 warning(s)`
- `python -X utf8 tools/mapmd_validate.py area/wild_chenliu_west/map.md`
  - 通過，更新後的 `wild_chenliu_west/20808 west -> road_chenliu/20901` world link 與 mapmd-json 一致
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_chenliu/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_chenliu_west/map.md --validate-only`
  - 通過
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/road_chenliu/map.md`
  - 通過，寫出 `20901-20908`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_chenliu_west/map.md`
  - 通過，重生包含新 westbound boundary 的 `20808.roo`
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
- `PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python -X utf8 tools/area_acceptance_gate.py road_chenliu`
  - 回報 `implementation_ready_for_commit`

## Runtime Notes

- 第一版預計建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版房間將落在 `20901-20908`
- 先正式落成 `wild_chenliu_west/20808 west <-> road_chenliu/20901 east`
- `road_chenliu` 的更西端會保留為 `future-loyang-contract`，暫不硬掛到 `loyang` 任一城門
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登記新區

## Next Step Prompt

`提交 road_chenliu implementation milestone commit，完成 tracker gate 收尾後再回到 queue 規則盤點下一個待建 area。`
