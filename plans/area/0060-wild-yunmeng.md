# Wild Yunmeng Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_yunmeng`。此區承接 `city_jiangxia` 南向水巷之外的第一段雲夢濕地前帶，讓玩家從江港城市的船貨秩序與水軍哨棚，一步滑進被蘆霧、浮木、泥灘與失路感主導的大澤探索節奏。

## Theme Positioning

- theme: `詭異民俗`
- subtheme: `雲夢大澤 / 迷霧濕地`
- experience_type: `Wild`
- player_loop_focus: `迷霧辨路 / 濕地探勘 / 地標記憶 / 失蹤異聞追跡`
- contrast_with_previous_two:
  - 相對於 `wild_jiangxia_river` 的江岸水路與 `city_jiangxia` 的江港秩序，`wild_yunmeng` 應讓玩家感受到水域不再被碼頭與城牆管理，而是被霧、泥、鳥鳴與錯路重新支配
- 世界缺口角色：
  - 把荊州主線從江夏港城自然推進到雲夢大澤的濕地探索帶
  - 為後續更深層的 `dng_yunmeng_swamp` 或沉沒神廟類 dungeon 提前建立地景與異聞基調
- reserved_room_block: `14501-14530`
- planned_vnum_range: `14501-14530`
- level_range: `50-60`
- external_links:
  - `north`: `city_jiangxia` / 南向水巷
  - `down`: `dng_yunmeng_swamp` / 沉沒神廟或更深濕地密穴
  - `south`: `city_changsha` / 荊南方向遠端主線
  - `east`: `city_chaisang` / 江東水陸轉接
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `大型濕地野外`
  - `迷霧與錯路`
  - `詭異民俗前帶`
- 它補的玩家 loop：
  - `從港城補給轉入高辨識度探索風險`
  - `依地標記憶回溯路線`
  - `追查失蹤者與異響來源`
  - `為後續 dungeon 建立入口吸力`
- 它和前兩個已完成 area 的題材差異：
  - 不再是碼頭、榜文與官署秩序
  - 不再是沿江直線推進的水道
  - 改用泥灘、霧牆、倒木與半沉石碑製造壓力

## Player Loop Contract

- `主線推進`
  - 玩家由江夏南向水巷踏入濕地邊緣，先用較清晰的蘆灘與樁道承接，再逐步深入更會迷向的霧沼核心
- `濕地辨路`
  - 依浮木、枯樹、石碑和鳥鳴方向辨識自己是繼續深入、折返還是走上錯路
- `支線探索`
  - 半沉祭壇
  - 漁棚殘架
  - 霧中高埠
- `非平面節奏`
  - `up/down` 用於高埠、下陷泥坑與沉陷祭壇，形成濕地探索的立體落差

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0060-wild-yunmeng.md`
- 建立 `area/wild_yunmeng/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-water-edge`
  - `mist-marsh`
  - `reed-islet`
  - `sunken-marker`
  - `deep-bog-front`
- 將 `去路 / 石碑 / 霧路 / 江夏 / 大澤` 視為正式 `#Enquire` 候選
- 將 `蘆葦 / 浮木 / 泥痕 / 石碑 / 祭壇` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供高埠或沉陷祭壇使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/wild_yunmeng/map.md` 生成第一批 `roo`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 將 area 登錄到 `area/directory.lst`
- 正式把 `city_jiangxia/14407` 與 `wild_yunmeng/14501` 做成雙向 runtime boundary
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `wild_yunmeng` 是中後段濕地野外，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `north-water-edge`
  - 水巷出口、濕地邊樁、第一段泥道
- `mist-marsh`
  - 迷霧泥灘、蘆牆岔路、積水窪口
- `reed-islet`
  - 半乾草洲、倒木短徑、獵人舊棚
- `sunken-marker`
  - 半沉石碑、祭壇斷臺、泥下磚痕
- `deep-bog-front`
  - 霧心高埠、深沼入口、下探前帶

## Suggested Theme Hooks

- `north-water-edge`
  - 讓玩家清楚感受到自己剛從城市秩序滑入濕地不確定性
- `mist-marsh`
  - 用霧、泥、聲音與遮蔽建立核心壓力
- `reed-islet`
  - 提供短暫辨位點與探索喘息
- `sunken-marker`
  - 讓詭異民俗與更深 dungeon 的暗示自然浮現
- `deep-bog-front`
  - 把後續下探吸力立起來，但先不直接把 dungeon 做滿

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/wild_yunmeng/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/wild_yunmeng/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/shanyan.html`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `ref/sanguo-area-specfirst/area/district_jianye_port/map.md`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `progression-map` 支持江夏之後切入 `雲夢大澤`
  - `題材分布表` 把雲夢定位為 `詭異 + 仙俠` 的大型濕地祕境前帶
  - `players.json / skills.json` 沒有提供足夠理由讓 queue 在此時再做一座城市或港區，因此濕地 wild 更符合玩法差異與主線節奏
- `compliance_check`
  - compliant；在 `city_jiangxia` 後切回高辨識度 `Wild`，並以資料盤點而非單純沿最新 world link 決定 queue

## First-Round Validation

- `area/wild_yunmeng/map.md` 必須包含有效 `mapmd-json`
- 迷霧濕地 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `wild_yunmeng` 不得退化成單一路徑 connector；必須保留濕地岔路、地標記憶與下探吸力

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_yunmeng/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_yunmeng/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_jiangxia/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the south planned link target to `wild_yunmeng`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangxia/map.md`
  - rewrote `roo/14401-14412` to include the south boundary into `14501`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_yunmeng/map.md`
  - wrote `roo/14501-14512`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1026.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `wild_yunmeng`
- `area/wild_yunmeng/index` 採首版濕地 wild scaffold，房號段 `14501-14530`、序號 `149`
- `mob/15731-15734` 與 `obj/15751-15754` 提供引路客、獵戶、守望者、拾荒客與濕地補給骨架
- `res/marsh.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15731`
- `area/city_jiangxia/map.md` 與 `area/wild_yunmeng/map.md` 已同步把 `14407 <-> 14501` 落成正式 runtime boundary
- `area/city_jiangxia/roo/14407.roo` 與 `area/wild_yunmeng/roo/14501.roo` 現在雙向一致
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已加入 `wild_yunmeng` loadable registry

## Next Step Prompt

`先 commit 目前 wild_yunmeng 的 implementation milestone；commit 後把它標記為 done，再盤點下一個待建 area。`
