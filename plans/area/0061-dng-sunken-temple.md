# Sunken Temple Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_sunken_temple`。此區承接 `wild_yunmeng` 深沼前帶之下的第一段濕地下探 dungeon，讓玩家從迷霧、泥灘與半沉地標的野外壓力，正式轉入被積水石階、殘廊封紋與沉沒祭室主導的水浸古廟探索節奏。

## Theme Positioning

- theme: `仙俠`
- subtheme: `沉沒古廟 / 濕地下探`
- experience_type: `Dungeon`
- player_loop_focus: `下探遺跡 / 封印辨識 / 潮水地形 / 深處風險升壓`
- contrast_with_previous_two:
  - 相對於 `city_jiangxia` 的江港秩序與 `wild_yunmeng` 的霧沼錯路，`dng_sunken_temple` 應讓玩家感受到地表的濕與霧都被壓成更封閉、更古老也更有機關感的地下壓力
- 世界缺口角色：
  - 把荊州線從雲夢濕地正式推進到第一個下探型 dungeon
  - 為更深 `sec_spirit_marsh` 一類 secret / sealed zone 預熱
- reserved_room_block: `14601-14630`
- planned_vnum_range: `14601-14630`
- level_range: `58-68`
- external_links:
  - `up`: `wild_yunmeng` / 深沼前帶
  - `down`: `sec_spirit_marsh` / 更深封印沼域
  - `out`: `city_jiangxia` / 回城遁路預留
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `濕地下探 dungeon`
  - `沉沒古廟`
  - `封印與機關前帶`
- 它補的玩家 loop：
  - `從野外辨路轉成地下辨位`
  - `觀察水痕、石門與封紋找前進線`
  - `為更深 secret zone 建立吸力`
- 它和前兩個已完成 area 的題材差異：
  - 不再是開放的濕地霧景
  - 不再是港城補給與官署節奏
  - 改用狹長石廊、積水前庭與半沉祭室製造壓迫

## Player Loop Contract

- `主線推進`
  - 玩家由深沼裂口下探，先經過積水前庭與倒塌石階，再逐步深入古廟主廊與封印側室
- `地形辨識`
  - 透過水痕高低、符紋殘片與石門狀態判斷哪裡像退路、哪裡像更深層
- `支線探索`
  - 祭器偏室
  - 漏水碑廊
  - 半沉封檻
- `非平面節奏`
  - `up/down` 用於落井、下沉祭室與封檻落差，形成真正在地底下探的感覺

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0061-dng-sunken-temple.md`
- 建立 `area/dng_sunken_temple/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `entry-sump`
  - `flooded-corridor`
  - `inscription-hall`
  - `ritual-wing`
  - `sealed-well`
- 將 `入口 / 深處 / 石門 / 封印 / 退路` 視為正式 `#Enquire` 候選
- 將 `水痕 / 符文 / 石門 / 鎖鏈 / 祭臺` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供落井或沉陷祭室使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_sunken_temple/map.md`
- `plans/area/0060-wild-yunmeng.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_sunken_temple/map.md`
  - `plans/area/0060-wild-yunmeng.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/shanyan.html`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/sanguo-area-specfirst/area/city_changsha/map.md`
  - `ref/sanguo-area-specfirst/area/city_chaisang/map.md`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `progression-map` 明確要求雲夢段之後切入一個 `Dungeon`
  - `dng_sunken_temple` 參考 spec 的沉沒古廟題材能自然承接濕地與深沼
  - 題材分布從 `詭異` 濕地再往 `仙俠` 封印遺跡切換，層次明確
- `compliance_check`
  - compliant；在 `wild_yunmeng` 後切到 `Dungeon`，不是把濕地地表無限延長

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_sunken_temple/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_sunken_temple/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/wild_yunmeng/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the `down` planned link target to `dng_sunken_temple`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_yunmeng/map.md`
  - rewrote `roo/14501-14512` to include the down boundary into `14601`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_sunken_temple/map.md`
  - wrote `roo/14601-14612`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1027.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `dng_sunken_temple`
- `area/dng_sunken_temple/index` 採首版濕地下探 dungeon scaffold，房號段 `14601-14630`、序號 `150`
- `mob/15831-15834` 與 `obj/15851-15854` 提供拾遺客、漏廊殘影、守井者、祭室鎖衛與地下補給骨架
- `res/temple.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15831`
- `area/wild_yunmeng/map.md` 與 `area/dng_sunken_temple/map.md` 已同步把 `14512 <-> 14601` 落成正式 runtime boundary
- `area/wild_yunmeng/roo/14512.roo` 與 `area/dng_sunken_temple/roo/14601.roo` 現在雙向一致
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已加入 `dng_sunken_temple` loadable registry

## Next Step Prompt

`先 commit 目前 dng_sunken_temple 的 implementation milestone；commit 後把它標記為 done，再盤點下一個待建 area。`
