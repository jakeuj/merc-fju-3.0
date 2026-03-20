# Fort Hulao Initial Area Plan

## Summary

建立下一個待建新 AREA：`fort_hulao`。此區承接 `dng_guandu_battlefield` 的軍旅節奏，但不再強調鏖兵殘跡，而是把玩家推進到一座仍有秩序、軍令與守備壓力的三國關隘 choke point。

## Theme Positioning

- theme: `軍旅`
- subtheme: `東都門戶 / 虎牢雄關`
- experience_type: `Fort`
- player_loop_focus: `關隘通行 / 問路與盤查 / 軍營補給 / 高低差守備線`
- contrast_with_previous_two:
  - 相對於 `wild_puyang_forest` 的林野探路與 `dng_guandu_battlefield` 的古戰場殘局，`fort_hulao` 應讓玩家感受到軍令仍在運作、守兵仍在執勤、地形被刻意設計成難以硬闖的戰略門戶
- 世界缺口角色：
  - 把中原主線從官渡戰地延伸到「控制交通與東都門戶」的關卡節點
  - 為後續回接 `city_loyang` / `city_xiangyang` 一類更大型主城或幹線節點提供高辨識度的軍事轉場
- reserved_room_block: `14101-14120`
- planned_vnum_range: `14101-14120`
- level_range: `28-36`
- external_links:
  - `west`: `city_hongnong` / 弘農方向關前道
  - `east`: `city_loyang` / 洛陽門戶
  - `south`: `dng_guandu_battlefield` / 官渡戰場餘線
  - `north`: 更北的軍道與巡哨帶
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `虎牢關`
  - `重兵把守的戰略門戶`
  - `關隘高低差與盤查壓力`
- 它補的玩家 loop：
  - `辨認關隘主路與側營`
  - `透過問路與軍令線索理解通行結構`
  - `在關門 / 甕城 / 望樓間感受 choke point 壓力`
- 它和前兩個已完成 area 的題材差異：
  - 不再是自然野外
  - 不再是戰後殘場
  - 改用「仍在運作的軍事設施」提供節奏與辨識度

## Player Loop Contract

- `主線推進`
  - 由西向東沿關前道接近虎牢關
  - 經外寨、關門與甕城才真正踏入內關
- `軍旅辨識`
  - 從軍旗、軍令、望樓與拒馬看出這裡不是單純路口，而是被刻意管制的門戶
- `支線探索`
  - 關兵營盤
  - 軍需棚
  - 望樓高道
- `非平面節奏`
  - `up/down` 用於關樓、坡道與甕城高差，形成軍事視野與壓迫感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0056-fort-hulao.md`
- 建立 `area/fort_hulao/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `west-approach`
  - `outer-gate`
  - `inner-bailey`
  - `barracks-line`
  - `watchtower-ridge`
- 將 `虎牢關 / 關門 / 軍令 / 守兵 / 去路` 視為正式 `#Enquire` 候選
- 將 `軍旗 / 柵門 / 拒馬 / 關樓 / 望樓` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 關樓 / 望樓 / 甕城高差位移
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/fort_hulao/map.md` 生成 `roo/14101-14112`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 將 area 登錄到 `area/directory.lst`
- 正式把 `dng_guandu_battlefield/14012` 與 `fort_hulao/14105` 做成雙向 runtime boundary
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `fort_hulao` 是中段軍事關卡，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `west-approach`
  - 關前道、坡口、外拒馬
- `outer-gate`
  - 外寨、關門、盤查點
- `inner-bailey`
  - 甕城、軍令榜、內關通道
- `barracks-line`
  - 軍營、軍需棚、換哨角
- `watchtower-ridge`
  - 石階、望樓、高牆巡道

## Suggested Theme Hooks

- `west-approach`
  - 讓玩家從還能行旅的道路，逐步進入明顯受軍方控制的地段
- `outer-gate`
  - 用盤查、厚門與守備痕跡建立「不能直接闖過」的體感
- `inner-bailey`
  - 用甕城與榜文讓玩家意識到關隘是一個制度化空間，不只是大門
- `barracks-line`
  - 把軍旅後勤與輪值生活感補進來，避免整區只剩空洞戰鬥感
- `watchtower-ridge`
  - 透過高處視野強化關隘控制交通的戰略辨識度

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/mud-area-templates/fort_hulao.md`
- `ref/sanguo-area-specfirst/area/fort_hulao/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/mud-area-templates/fort_hulao.md`
  - `ref/sanguo-area-specfirst/area/fort_hulao/map.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `ref/三國-MUD-題材分布表.md`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 將虎牢關視為洛陽一帶的重要門戶節點
  - `sanguo-progression-map` 支持在官渡戰地之後放入高辨識度軍事 choke point
  - `fort_hulao` 模板提供關門、軍營、望樓與軍令感的基本結構
  - spec-first 參考稿提供 world-link 與關隘功能分區的初步骨架，但本區改寫為更適合現行 queue 的主線關卡版本
- `compliance_check`
  - compliant；延續 `City -> Wild -> Dungeon -> Fort` 的 queue variety，不回頭掉進同質化野外或深井鏈

## First-Round Validation

- `area/fort_hulao/map.md` 必須包含有效 `mapmd-json`
- 關隘 choke point loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `fort_hulao` 不得退化成平面直線 connector；必須保留關門、甕城、營盤與望樓高差

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/fort_hulao/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_hulao/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/dng_guandu_battlefield/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the `14012 <-> 14105` boundary and fixing the `14011/14012` reverse-link drift
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_guandu_battlefield/map.md`
  - rewrote `roo/14001-14012` to include the north boundary into `14105`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/fort_hulao/map.md`
  - wrote `roo/14101-14112`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1021.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `fort_hulao`
- `area/fort_hulao/index` 採首版關隘 scaffold，房號段 `14101-14120`、序號 `145`
- `mob/15331-15334` 與 `obj/15351-15354` 提供軍需官、守關兵、關樓哨卒與虎牢長槍骨架
- `res/garrison.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15331`
- `area/dng_guandu_battlefield/map.md` 與 `area/fort_hulao/map.md` 已同步把 `14012 <-> 14105` 落成正式 runtime boundary
- `area/dng_guandu_battlefield/roo/14012.roo` 與 `area/fort_hulao/roo/14105.roo` 現在雙向一致

## Next Step Prompt

`先 commit 目前 fort_hulao 的 implementation milestone；commit 後把此區標記為 done，再開始 city_xiangyang 的 spec milestone。`
