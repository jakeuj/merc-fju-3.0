# Dng Guandu Battlefield Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_guandu_battlefield`。此區承接 `wild_puyang_forest` 北向戰前前帶，定位為官渡鏖兵的古戰場 dungeon，讓玩家從林野探路正式轉入壕溝、殘旗、焚毀糧車與死地高塹交錯的軍旅主題區。

## Theme Positioning

- theme: `軍旅`
- subtheme: `古戰場 / 官渡鏖兵`
- experience_type: `Dungeon`
- player_loop_focus: `戰場探索 / 路線判斷 / 伏擊辨識 / 戰地掉寶`
- contrast_with_previous_two:
  - 相對於 `city_chenliu` 的服務城市與 `wild_puyang_forest` 的林野前帶，`dng_guandu_battlefield` 應把玩家直接推進到壕塹、火攻遺痕與戰後殘陣構成的高壓軍旅場景
- 世界缺口角色：
  - 把 `wild_puyang_forest` 北向戰前風聲落成真正的官渡古戰場主題區
  - 為後續更高辨識度的 `fort_hulao` 軍事 choke point 維持軍旅節奏，但不重複做純關隘
- reserved_room_block: `14001-14030`
- planned_vnum_range: `14001-14030`
- level_range: `24-34`
- external_links:
  - `south`: `wild_puyang_forest` / 北向荒路後的戰場入口
  - `north`: 官渡主陣更深處 / 焚糧核心帶
  - `east`: 曹軍糧道殘線
  - `west`: 袁軍舊壘斷帶
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `官渡古戰場`
  - `壕塹與殘陣探索`
  - `火攻後戰地壓迫`
- 它補的玩家 loop：
  - `戰場路線選擇`
  - `辨識高低地與伏擊點`
  - `戰地風險與掉寶`
  - `由林野前帶轉入正式軍旅 dungeon`
- 它和前兩個已完成 area 的題材差異：
  - 不走城市服務
  - 不走純自然野外
  - 改用戰地廢墟、斷旗、焦木與壕溝高差製造壓力

## Player Loop Contract

- `主線推進`
  - 由 `wild_puyang_forest` 北向荒路進入戰場前塹
  - 沿壕溝、土壘與殘車線深入官渡鏖兵地帶
- `戰地辨識`
  - 透過高塹、壕溝、焦土與斷旗判斷危險路線
- `支線探索`
  - 糧車殘帶
  - 鼓旗坡
  - 焚木堆與斷戟坑
- `非平面節奏`
  - `up/down` 用於土塹、瞭望高地與崩陷壕溝

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0055-dng-guandu-battlefield.md`
- 建立 `area/dng_guandu_battlefield/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `south-approach`
  - `trench-line`
  - `burned-wagons`
  - `banner-ridge`
  - `north-deadground`
- 將 `官渡 / 壕溝 / 糧車 / 鼓旗 / 去路` 視為正式 `#Enquire` 候選
- 將 `殘旗 / 斷戟 / 糧車 / 焦木 / 土塹` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 土壘 / 壕溝高差移動
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/dng_guandu_battlefield/map.md` 生成 `roo/14001-14017`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 正式把 `wild_puyang_forest/13912` 與 `dng_guandu_battlefield/14001` 做成雙向 runtime boundary
- 將 area 登錄到 `area/directory.lst`
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `dng_guandu_battlefield` 是中段戰地 dungeon，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `south-approach`
  - 戰場前塹、破木拒馬、入場風聲
- `trench-line`
  - 壕溝、土塹、斷戟泥地
- `burned-wagons`
  - 焚糧車列、焦木坑、煙灰側帶
- `banner-ridge`
  - 鼓旗坡、殘旗高地、瞭望塹口
- `north-deadground`
  - 死地前帶、散兵荒路、主陣深處預留口

## Suggested Theme Hooks

- `south-approach`
  - 讓玩家立刻感覺自己已不在戰前外圍，而是踏進真正的鏖兵現場
- `trench-line`
  - 用壕溝與高低差建立戰地 dungeon 的路線判斷
- `burned-wagons`
  - 用焚糧與焦木意象強化官渡辨識度
- `banner-ridge`
  - 用殘旗、鼓位與高坡營造局勢張力
- `north-deadground`
  - 把主陣壓力留在前方，而不是一版就把整個戰場做滿

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/mud-area-templates/dng_royal_tomb.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/mud-area-templates/dng_royal_tomb.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - progression 主線的官渡戰場位置
  - 題材由林野承接到正式軍旅古戰場
  - `dng_royal_tomb` 模板提供 dungeon 化 cluster / choke point 參考，但本區改寫成戰地語彙
- `compliance_check`
  - compliant；提供戰場型 dungeon，而不是再做一個地下深井或關隘複製品

## First-Round Validation

- `area/dng_guandu_battlefield/map.md` 必須包含有效 `mapmd-json`
- 戰場探索 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `dng_guandu_battlefield` 不得退化成單一路直通 connector；必須保留壕溝高差、支線與古戰場辨識度

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_guandu_battlefield/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_guandu_battlefield/map.md --validate-only`
  - passed for `17` room(s)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_puyang_forest/map.md`
  - rewrote `roo/13901-13912` to include the north boundary into `14001`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_guandu_battlefield/map.md`
  - wrote `roo/14001-14017`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1020.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `dng_guandu_battlefield`
- `area/dng_guandu_battlefield/index` 採首版 dungeon scaffold，房號段 `14001-14030`、序號 `144`
- `mob/15231-15234` 與 `obj/15251-15254` 提供戰地補給、散兵與古戰場掉落骨架
- `res/battlefield.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15231`
- `area/wild_puyang_forest/map.md` 與 `area/dng_guandu_battlefield/map.md` 已同步把 `13912 <-> 14001` 落成正式 runtime boundary
- `area/wild_puyang_forest/roo/13912.roo` 與 `area/dng_guandu_battlefield/roo/14001.roo` 現在雙向一致

## Next Step Prompt

`先 commit 目前 dng_guandu_battlefield 的 implementation milestone；commit 後把此區標記為 done，再開始 fort_hulao 的 spec milestone。`
