# Wild Nanman Jungle Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_nanman_jungle`。此區承接 `city_guiyang` 西向外徑，把玩家從桂陽這座邊地補給城，帶進一段更潮濕、更原始、也更難單靠官道路感辨位的南蠻密林前帶，讓南線主世界在母城之後重新切回高辨識度的 wild family。

## Theme Positioning

- theme: `探險`
- subtheme: `南蠻密林 / 部族邊徑`
- experience_type: `Wild`
- player_loop_focus: `密林辨位 / 藤路探索 / 圖騰觀察 / 深帶轉場`
- contrast_with_previous_two:
  - 相對於 `city_lingling` 的山城奇聞與 `city_guiyang` 的邊地轉運，`wild_nanman_jungle` 應讓玩家感受到秩序正在快速退後，取而代之的是濕熱樹影、藤路、獸徑與部族痕跡組成的邊林壓迫感
- 世界缺口角色：
  - 把 `city_guiyang` 已預留的西向 `wild_nanman_jungle` world-link 正式轉成可持續擴建的 spec-first 野外帶
  - 為後續 `dng_nanman_temple` 或更深南蠻支線建立第一層密林入口
- reserved_room_block: `15301-15330`
- planned_vnum_range: `15301-15330`
- level_range: `94-100`
- external_links:
  - `east`: `city_guiyang` / 桂陽西岔
  - `down`: `dng_nanman_temple` / 林下古祠預留
  - `west`: `wild_nanman_deeps` / 更深林帶預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南蠻密林前帶`
  - `部族路標與圖騰痕跡`
  - `母城之後的高壓辨位野外`
- 它補的玩家 loop：
  - `從桂陽整補後切進更野、更濕熱的外帶`
  - `靠藤路、圖騰、石痕與濕地聲音辨認方向`
  - `為後續南蠻神殿或更深林區建立前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是城市主街、市口與榜示節奏
  - 不再是山城型官道與坡城氣味
  - 改用濕熱密林、部族邊徑、圖騰與高低差把節奏轉回真正的南境 wild

## Player Loop Contract

- `主線推進`
  - 玩家由桂陽西岔切入，經過藤門外徑、圖騰林口、濕根窄路與林下高台，再決定要不要繼續往更深密林或往下探入古祠方向
- `地標辨識`
  - 透過藤結、石痕、獵骨、潮泥與圖騰柱判斷哪裡像回城口、哪裡像部族邊界、哪裡像更深危險區
- `支線探索`
  - 獵骨歇點
  - 泥窪低帶
  - 林下祭柱
- `非平面節奏`
  - `up/down` 用於樹根高台、林下凹地與古祠入口高低差，讓南蠻密林不是平面迷路圖，而是帶垂直辨位感的濕林區

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0068-wild-nanman-jungle.md`
- 建立 `area/wild_nanman_jungle/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `east-entry`
  - `vine-path`
  - `totem-grove`
  - `marsh-pocket`
  - `canopy-ridge`
- 將 `南蠻 / 桂陽 / 密林 / 出口 / 古祠` 視為正式 `#Enquire` 候選
- 將 `圖騰 / 藤結 / 石痕 / 獸骨 / 根台` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供林根高台或凹地落差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_nanman_jungle/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0067-city-guiyang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_nanman_jungle/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0067-city-guiyang.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_nanhai/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `city_guiyang` 已在 runtime 與 spec 內明確預留西向 `wild_nanman_jungle` 邊界，適合把南境母城之後的第一段 wild 正式落地
  - `題材分布表` 把南方蠻荒區的 `南蠻森林` 定位成 `探險 / 詭異` 的原始森林，能有效拉開和 `city_guiyang` 的城鎮節奏
  - `players.json / skills.json` 沒有提供必須優先跳到 `city_nanhai` 的服務鏈證據，因此先做 `Wild` 能維持 queue variety gate
  - `ref/sanguo-area-specfirst` 已提供可改寫 scaffold，可直接轉成目前桂陽西向密林前帶所需版本
- `compliance_check`
  - compliant；在連續兩個 `City` 里程碑後切回 `Wild`，延續 `city_guiyang` 預留 world-link，也恢復 family 多樣性

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_nanman_jungle/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_nanman_jungle/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_guiyang/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning `15212 <-> 15301`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_guiyang/map.md`
  - rewrote `roo/15201-15212` to include the `15212 west -> 15301 external` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_nanman_jungle/map.md`
  - wrote `roo/15301-15312`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reported `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - first run exposed a loader blocker from generated `SECT_SWAMP`; corrected to `SECT_WATER_SWIM`
  - final startup smoke test passed; success signal found in `log/1034.log`
- `debug/badobject`
  - empty after final smoke test
- `debug/error`
  - only contains the expected timeout-forced shutdown path after the successful run

## Runtime Notes

- `area/directory.lst` 已加入 `wild_nanman_jungle`，保留房號段 `15301-15330`
- `area/wild_nanman_jungle/index` 已建立，`Serial 157`
- 第一輪 runtime scaffold 已加入：
  - `mob/16531-16534`
  - `obj/16551-16554`
  - `res/wild.res`
  - `shp/supplies.shp`
- `city_guiyang/15212 <-> wild_nanman_jungle/15301` 已成為正式 runtime boundary
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已同步登錄 `wild_nanman_jungle`

## Next Step Prompt

`先 commit 目前 wild_nanman_jungle 的 implementation milestone；commit 後直接盤點並建立下一個待建 area 的 spec milestone。`
