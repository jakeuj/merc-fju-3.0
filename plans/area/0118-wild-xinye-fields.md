# Wild Xinye Fields Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_xinye_fields`。此區承接 `city_xinye` 西田路牌外那條原本只停在郊野想像層的田路，把新野從邊鎮人情與義士消息，正式鬆開成田埂、灌渠、村口茶棚與西野風碑交錯的近郊 wild。它不該只是 `city_xinye` 的附屬背景，而要讓玩家明顯感到自己正從鎮中熟路人的指點，走進更看天色、地勢與地方痕跡辨位的外野帶。

## Theme Positioning

- theme: `江湖`
- subtheme: `田野 / 村落`
- experience_type: `Wild`
- player_loop_focus: `離鎮 / 問路 / 村口歇腳 / 郊野辨位 / 外帶過渡`
- contrast_with_previous_two:
  - 相對於 `fort_fancheng` 的軍令壓力與 `city_xinye` 的邊鎮人情，`wild_xinye_fields` 應把節奏重新放開成田路、灌渠與村口小交易構成的近郊探索帶。
- 世界缺口角色：
  - 把 `city_xinye/20205` 原本只停在 spec 層的西向田路，正式落成為 `wild_xinye_fields/20301` 的可載入 runtime boundary
  - 先替新野外圍建立一圈貼著田地與村落生活的郊野母帶，讓後續更深野外或支線能從成熟的外帶節點繼續延伸
- reserved_room_block: `20301-20320`
- planned_vnum_range: `20301-20320`
- level_range: `18-28`
- external_links:
  - `east`: `city_xinye` / 西田路牌
- delivery_gate: `implementation_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_xinye_fields/map.md`
- `ref/sanguo-area-specfirst/area/city_wan/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `area/city_xinye/map.md`
- `area/jingxiang_road/map.md`
- `plans/area/0117-city-xinye.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_xinye_fields/map.md`
  - `ref/sanguo-area-specfirst/area/city_wan/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `area/city_xinye/map.md`
  - `area/jingxiang_road/map.md`
  - `plans/area/0117-city-xinye.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/sinya.html`
  - `ref/sanguo-area-specfirst/area/road_wan/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 已把 `wild_xinye_fields` 列為 `江湖 / 18-28` 的 `Wild` 節點，正好能作為 `city_xinye` 之後的第一圈外帶
  - `題材分布表` 把荊州段的 `新野` 放在更有人情的邊鎮位置，因此把下一步落在貼田地、村路與在地腳步感的近郊 wild，比立刻再堆一個城市更能維持題材起伏
  - `city_xinye` 現行 runtime 已有成熟的 `20205 西田路牌` stub，代表這條外連能低風險落地；相較之下，`city_wan` 與 `jingxiang_road` 仍各自帶著尚未完全對齊的方向契約
  - `players.json / skills.json` 沒有提供「新野之後必須立刻再做服務城市」的強訊號，目前能看到的荊州服務感仍偏向襄陽，反而支持先補外圍 travel / exploration belt
- `compliance_check`
  - compliant；在 `fort_fancheng -> city_xinye` 之後接 `wild_xinye_fields`，可恢復 `Fort -> City -> Wild` 的 family variety，同時優先解掉已成熟的西向 runtime stub，而不是先把 `jingxiang_road` 的契約混亂帶進下一輪

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_xinye_fields/map.md` 與 `area/city_xinye/map.md` 均通過，結果為 `0 error / 0 warning`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py ... --validate-only` 對 `wild_xinye_fields` 與 `city_xinye` 均通過；正式 `.roo` 生成後已確認 `city_xinye/20205 west <-> wild_xinye_fields/20301 east` 雙向邊界一致
- `python -m json.tool docs/current-game/areas.json > $null` 通過
- WSL Linux `make -f Makefile.lin clean && make -f Makefile.lin merc` 通過
- direct `timeout 45s ./merc merc.ini || true` smoke 明確出現 `三國歪傳之降龍伏虎開始正常運作`
- 本輪 direct smoke 未額外產生新的 numbered `log/*`；成功訊號以 stdout 與 `debug/*` 檢查為準
- `debug/error` 只有 timeout 關機訊息，`debug/failexit` 只有既有 baseline `17201/17208` fixup，`debug/badobject` 為空
- `$env:PYTHONUTF8='1'; python tools/area_acceptance_gate.py wild_xinye_fields` 回報 `implementation_ready_for_commit`

## Runtime Notes

- 已建立 `index / roo / mob / obj / res / shp` 最小可載入集合
- 首版 runtime 房間落在 `20301-20308`
- 已正式落成 runtime boundary：`city_xinye/20205 west -> wild_xinye_fields/20301` 與 `wild_xinye_fields/20301 east -> city_xinye/20205`
- `city_wan` 與 `jingxiang_road` 仍保留在 queue / spec 判斷層，不在這一輪硬接

## Next Step Prompt

`提交 wild_xinye_fields implementation milestone commit：內容包含 city_xinye/20205 west <-> wild_xinye_fields/20301 east runtime boundary、index / roo / mob / obj / res / shp、directory.lst 與 current-game area registry 更新。`
