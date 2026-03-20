# Wild Jiangxia River Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_jiangxia_river`。此區承接 `city_xiangyang` 東碼頭之外的第一段水路野外，讓玩家從荊州主城的秩序、補給與官署節奏，轉入蘆葦河岸、水寨殘樁、渡口木棧與江霧壓迫並存的江夏水道前帶。

## Theme Positioning

- theme: `探險`
- subtheme: `江夏水道 / 水軍河岸`
- experience_type: `Wild`
- player_loop_focus: `江岸探路 / 水路轉場 / 渡口問路 / 河霧伏擊辨識`
- contrast_with_previous_two:
  - 相對於 `fort_hulao` 的軍事關隘與 `city_xiangyang` 的城市 hub，`wild_jiangxia_river` 應讓玩家感受到主線已從陸上秩序滑進水路不確定性，視線、聲音與去路都被江霧和蘆葦重新切碎
- 世界缺口角色：
  - 把荊州主線從襄陽主城自然推進到江夏方向的水路外野
  - 為後續 `city_jiangxia` / 柴桑 / 雲夢大澤一類水域與江港節點預熱
- reserved_room_block: `14301-14330`
- planned_vnum_range: `14301-14330`
- level_range: `40-50`
- external_links:
  - `west`: `city_xiangyang` / 東碼頭外路
  - `east`: `city_jiangxia` / 江夏水軍重鎮
  - `south`: `wild_yunmeng_marsh` / 雲夢濕澤前帶
  - `north`: 江岸巡防與上游渡口
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `江岸野外`
  - `水寨與渡口前帶`
  - `河霧與蘆葦的水路壓迫`
- 它補的玩家 loop：
  - `沿江探路`
  - `辨識渡口與水寨殘跡`
  - `從主城補給切換到水路風險`
  - `為後續江夏 / 柴桑 / 雲夢鏈做節奏轉場`
- 它和前兩個已完成 area 的題材差異：
  - 不再是城市街廓
  - 不再是關門與大道
  - 改用江風、木棧、蘆葦與河霧製造閱讀與路線壓力

## Player Loop Contract

- `主線推進`
  - 由襄陽東碼頭外路沿江岸向東展開
  - 穿過蘆汀、殘樁水寨與渡口木棧，逐步接近江夏方向
- `水路辨識`
  - 透過潮痕、繫船樁、破網與蘆棚判斷哪裡像安全停靠點、哪裡像埋伏帶
- `支線探索`
  - 河汊木橋
  - 水寨殘樁
  - 漁棚歇腳點
- `非平面節奏`
  - `up/down` 用於堤岸高差、棧橋與濕地陷落帶，形成水域野外的立體感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0058-wild-jiangxia-river.md`
- 建立 `area/wild_jiangxia_river/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `west-wharf-edge`
  - `riverbank-trail`
  - `reed-marsh`
  - `waterfort-remains`
  - `east-ferry-front`
- 將 `碼頭 / 江路 / 水寨 / 去路 / 江夏` 視為正式 `#Enquire` 候選
- 將 `蘆葦 / 棧橋 / 繫船樁 / 漁網 / 水旗` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 堤岸 / 棧橋 / 濕地高差位移
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/wild_jiangxia_river/map.md` 生成 `roo/14301-14312`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 將 area 登錄到 `area/directory.lst`
- 正式把 `city_xiangyang/14212` 與 `wild_jiangxia_river/14301` 做成雙向 runtime boundary
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `wild_jiangxia_river` 是中後段水路野外，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `west-wharf-edge`
  - 城外東碼頭、離城木棧、第一段江岸路
- `riverbank-trail`
  - 沿江土道、繫船樁、河汊木橋
- `reed-marsh`
  - 蘆葦濕灘、泥岸、下陷汊口
- `waterfort-remains`
  - 水寨殘樁、斷旗、舊哨棚
- `east-ferry-front`
  - 東向渡口、江夏前帶、上船路牌

## Suggested Theme Hooks

- `west-wharf-edge`
  - 讓玩家清楚感受到自己剛從城市退到江岸邊緣
- `riverbank-trail`
  - 用潮痕、繫船樁與船板聲讓水路感盡快成立
- `reed-marsh`
  - 用蘆葦、泥灘與視線遮蔽製造天然埋伏壓力
- `waterfort-remains`
  - 把三國水軍與江岸防務的題材痕跡留在地景裡，而不必直接做完整軍港
- `east-ferry-front`
  - 把江夏方向的主線吸力先建立起來，但不提早把主城做滿

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_jiangxia/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_jiangxia/map.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/shanyan.html`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 與 progression map 都支持襄陽之後往江夏 / 柴桑的水路延伸
  - `city_jiangxia` 參考稿提示江夏鏈必須帶出水軍與江港節奏，因此先以河岸野外作過渡最穩
  - 題材分布表支持以水域與交通風險為主題，避免襄陽後面又直接接另一座相似城市
- `compliance_check`
  - compliant；在 `City` 之後切回 `Wild`，維持 queue variety，且不重複陸地林野或山道主題

## First-Round Validation

- `area/wild_jiangxia_river/map.md` 必須包含有效 `mapmd-json`
- 水路探索 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `wild_jiangxia_river` 不得退化成單一路直通 connector；必須保留蘆葦、濕灘、水寨殘跡與渡口辨識度

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/wild_jiangxia_river/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_jiangxia_river/map.md --validate-only`
  - passed for `12` room(s)
- `python -X utf8 tools/mapmd_validate.py area/city_xiangyang/map.md`
  - passed with `0 error(s), 0 warning(s)` after aligning the `14212 <-> 14301` boundary
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_xiangyang/map.md`
  - rewrote `roo/14201-14212` to include the east boundary into `14301`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/wild_jiangxia_river/map.md`
  - wrote `roo/14301-14312`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1024.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Runtime Notes

- `area/directory.lst` 已加入 `wild_jiangxia_river`
- `area/wild_jiangxia_river/index` 採首版水路野外 scaffold，房號段 `14301-14330`、序號 `147`
- `mob/15531-15534` 與 `obj/15551-15554` 提供船伕、巡汊手、水匪、護纜手與江岸補給骨架
- `res/river.res` 與 `shp/supplies.shp` 已建立，keeper 為 `15531`
- `area/city_xiangyang/map.md` 與 `area/wild_jiangxia_river/map.md` 已同步把 `14212 <-> 14301` 落成正式 runtime boundary
- `area/city_xiangyang/roo/14212.roo` 與 `area/wild_jiangxia_river/roo/14301.roo` 現在雙向一致

## Next Step Prompt

`先 commit 目前 wild_jiangxia_river 的 implementation milestone；commit 後把此區標記為 done，再開始 city_jiangxia 的 spec milestone。`
