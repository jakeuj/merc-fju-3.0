# Dng Serpent Temple Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_serpent_temple`。此區承接 `wild_nanman_jungle` 林下古祠入口，把玩家從濕熱、開放但仍可折返的南蠻密林前帶，拉進一段更封閉、更帶血祭與蛇神崇拜壓迫感的地下神殿 dungeon，讓南境支線從野外壓力切入真正的深處危險區。

## Theme Positioning

- theme: `詭異民俗`
- subtheme: `蛇殿 / 血祭`
- experience_type: `Dungeon`
- player_loop_focus: `神殿下探 / 封紋辨位 / 血祭遺痕 / 深處轉場`
- contrast_with_previous_two:
  - 相對於 `city_guiyang` 的邊地城鎮與 `wild_nanman_jungle` 的濕熱密林，`dng_serpent_temple` 應讓玩家感受到空間突然收窄、秩序不再來自路徑而來自禁忌與封印，風險也從迷路轉成深處未知物與儀式痕跡的心理壓力
- 世界缺口角色：
  - 把 `wild_nanman_jungle` 已預留的 `down` 向林下古祠正式轉成可持續擴建的 spec-first dungeon
  - 為後續 `sec_jungle_ruins` 或更深南蠻秘殿建立第一層封閉型下探區
- reserved_room_block: `15401-15430`
- planned_vnum_range: `15401-15430`
- level_range: `98-100`
- external_links:
  - `up`: `wild_nanman_jungle` / 林下祠痕
  - `down`: `sec_jungle_ruins` / 深封地宮預留
  - `enter`: `dng_serpent_sanctum` / 內祭殿預留
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `南蠻蛇神殿`
  - `血祭與封紋遺痕`
  - `密林之下的封閉 dungeon`
- 它補的玩家 loop：
  - `從密林辨位切進神殿下探`
  - `靠蛇紋石門、祭血水痕與符紋柱辨認進退`
  - `為更深 jungle ruins 或內祭殿建立前帶`
- 它和前兩個已完成 area 的題材差異：
  - 不再是母城補給與問路節奏
  - 不再是開放式密林與高差辨位節奏
  - 改用石門、祭槽、封印與暗道把節奏轉成壓縮型 dungeon

## Player Loop Contract

- `主線推進`
  - 玩家由林下祠痕往下切入，先經過潮濕前廳、蛇紋甬道與祭槽偏殿，再逐步接近封紋內殿與更深地宮入口
- `地標辨識`
  - 透過蛇紋、石門、滴水聲、殘骨與祭火痕判斷哪裡像退路、哪裡像機關帶、哪裡像深處入口
- `支線探索`
  - 偏殿祭槽
  - 殘骨儲室
  - 封印石門
- `非平面節奏`
  - `up/down` 用於地階、塌落井口與更深封室落差，讓蛇神殿維持垂直壓迫感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0069-dng-serpent-temple.md`
- 建立 `area/dng_serpent_temple/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `entry-hall`
  - `serpent-corridor`
  - `ritual-chamber`
  - `sealed-core`
  - `deep-shaft`
- 將 `蛇殿 / 密林 / 退路 / 深處 / 封印` 視為正式 `#Enquire` 候選
- 將 `石門 / 蛇紋 / 血槽 / 符文 / 鎖鍊` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供落階或井口高低差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_serpent_temple/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0068-wild-nanman-jungle.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_serpent_temple/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0068-wild-nanman-jungle.md`
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
  - `wild_nanman_jungle` 已在 spec 與 runtime 內明確預留 `down` 向林下古祠，適合把南蠻支線的第一個 dungeon 正式落地
  - `ref` scaffold 已提供 `蛇神殿` 類型，與南蠻密林的圖騰、祭柱與古祠痕跡有直接題材連續性
  - `players.json / skills.json` 沒有提供必須先回到 `city_nanhai` 的服務鏈證據，因此在 `Wild` 後切入 `Dungeon` 更符合 queue variety 與支線張力
  - `題材分布表` 的南方蠻荒區與特殊探索區都支持把這段南境外帶延伸成更詭異、更封閉的祭祀遺跡
- `compliance_check`
  - compliant；在 `Wild` 之後切入 `Dungeon`，延續 `wild_nanman_jungle` 的 `down` 向預留 world-link，也維持 family 多樣性

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_serpent_temple/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_serpent_temple/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 dng_serpent_temple 的 spec milestone；commit 後直接做 implementation milestone。`
