# Wild Barbarian Camp Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_barbarian_camp`。此區承接 `wild_bailang` 的東向荒徑，把北境主線從白狼山的邊山傳說與裂風山脊，推進到更帶敵蹤、舊柵、火堆與部族營痕的人為 hostile wild，並替後續 `city_xiangping` 的遼東邊城 hub 建立真正可載入的前置過渡區。

## Theme Positioning

- theme: `軍旅`
- subtheme: `部族營地 / 邊地敵蹤`
- experience_type: `Wild`
- player_loop_focus: `邊地辨位 / 營痕觀察 / 舊柵轉場 / 襄平前帶`
- contrast_with_previous_two:
  - 相對於 `wild_bailang` 的傳說邊山與 `dng_ancient_cave` 的濕冷地下遺跡，`wild_barbarian_camp` 應把節奏重新拉回地表，但不是回到純自然山野，而是進入一塊明顯帶著人為占據痕跡、敵意記憶與邊地壓力的 hostile wild。
- 世界缺口角色：
  - 把 `wild_bailang/18007` 的東向預留正式轉成北境主線可持續擴建的 wild 節點
  - 為後續 `city_xiangping` 建立可載入的前置轉場，而不是讓邊城 hub 懸空在未落地的 world link 後面
- reserved_room_block: `18201-18220`
- planned_vnum_range: `18201-18220`
- level_range: `34-46`
- external_links:
  - `west`: `wild_bailang` / 白狼山東荒徑
  - `east`: `city_xiangping` / 襄平城路預留
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_barbarian_camp/map.md`
- `ref/sanguo-area-specfirst/area/city_xiangping/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0095-wild-bailang.md`
- `plans/area/0096-dng-ancient-cave.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_barbarian_camp/map.md`
  - `ref/sanguo-area-specfirst/area/city_xiangping/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0095-wild-bailang.md`
  - `plans/area/0096-dng-ancient-cave.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/wild_wolf_forest/map.md`
  - `ref/sanguo-area-specfirst/area/sec_spirit_peak/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `wild_bailang -> wild_barbarian_camp -> city_xiangping` 放成同一段北境主線，`wild_barbarian_camp` 是白狼山往襄平的直接中介節點
  - `題材分布表` 把白狼山與襄平之間切成 `探險遺跡 -> 軍旅邊城` 的北境帶，適合用一塊帶部族駐留痕跡的 hostile wild 來承接這個氣氛轉換
  - `players.json / skills.json` 對 `襄平` 提出 `refresh`、屬性訓練與 `venom` 等服務訊號，反而支持先把通往 `city_xiangping` 的前置野外補起來，而不是讓邊城 hub 在 implementation 時變成孤點
  - `wild_bailang` 的既有 spec/runtime 已明確保留 `18007 east -> wild_barbarian_camp`，使本區成為目前最可直接延續且不會卡住下一輪 implementation 的北境候選
- `compliance_check`
  - compliant；雖然這輪會形成 `Dungeon -> Wild` 的 family 切換，但它同時滿足 runtime 可接性、通往 `city_xiangping` 的主線過渡需求，以及 queue variety 不把高階 `secret` 先行孤立化的原則

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_barbarian_camp/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_barbarian_camp/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_barbarian_camp/map.md`
  - passed (`Wrote 8 room scaffold file(s) to H:\repos\merc-fju-3.0\area\wild_barbarian_camp\roo`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_bailang/map.md`
  - passed；同步把 `wild_bailang/18007` 補成 `east -> 18201` runtime boundary
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0/src && timeout 45 ./merc merc.test.ini"`
  - passed；因使用中的遊戲實例已占用預設 `3838`，改以臨時測試 port `23838/21234/28888` 做 direct-load smoke，並在 console 看見 `三國歪傳之降龍伏虎開始正常運作`
- `debug/badobject`
  - empty
- `debug/error`
  - only timeout-triggered shutdown path after smoke window closed；無新增 area loader blocker
- `debug/failexit`
  - only legacy baseline `17201/17208` fixups；無 `wild_barbarian_camp` 與 `wild_bailang` 相關新 warning

## Runtime Notes

- 已建立最小 loadable runtime scaffold：`index`、`mob/20631-20634`、`obj/20651-20654`、`res/wild.res`、`shp/supplies.shp`、`roo/18201-18208`
- 已正式落成西側 runtime boundary：`wild_bailang/18007 <-> wild_barbarian_camp/18201`
- `east -> city_xiangping` 仍維持 world-link metadata，待後續邊城 milestone 再正式接上
- `area/directory.lst`、`docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步納入 `wild_barbarian_camp`

## Next Step Prompt

`wild_barbarian_camp` 的 implementation milestone 已完成；下一步依 queue 規則盤點並建立 `city_xiangping` 的 spec milestone，讓北境主線正式往遼東邊城 hub 推進。`
