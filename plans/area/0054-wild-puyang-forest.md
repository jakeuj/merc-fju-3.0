# Wild Puyang Forest Initial Area Plan

## Summary

建立下一個待建新 AREA：`wild_puyang_forest`。此區承接 `city_chenliu` 北向戰前導流，定位為濮陽與官渡之間的中原林野前帶，讓玩家從城市補給與軍旅中繼，過渡到視線受阻、伏兵風險升高、古戰場氣味漸濃的探索型野外。

## Theme Positioning

- theme: `探險`
- subtheme: `中原林野 / 官渡前哨外圍`
- experience_type: `Wild`
- player_loop_focus: `練功 / 探路 / 傳聞蒐集 / 伏兵風險辨識`
- contrast_with_previous_two:
  - 相對於 `sec_rift_spirit_core_gehennal` 的抽象 endgame 深井與 `city_chenliu` 的高服務密度城市 hub，`wild_puyang_forest` 應提供中段主線的橫向林野壓力、視線遮蔽與戰前探路節奏
- 世界缺口角色：
  - 把 `city_chenliu` 北向 world link 落成真正可探索的野外承接帶
  - 為後續 `dng_guandu_battlefield` 的軍旅 / 古戰場主題預熱
- reserved_room_block: `13901-13930`
- planned_vnum_range: `13901-13930`
- level_range: `20-30`
- external_links:
  - `south`: `city_chenliu` / 北街牌樓後的北路出城帶
  - `north`: `dng_guandu_battlefield` / 官渡古戰場前帶
  - `east`: 濮陽方向的林外官道
  - `west`: 廢棧道與林間斥候支線
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `中原林野`
  - `戰前前哨外圍`
  - `官道失序邊帶`
- 它補的玩家 loop：
  - `中段練功`
  - `探路`
  - `辨識伏兵與風險地形`
  - `從城市補給轉入野外遭遇`
- 它和前兩個已完成 area 的題材差異：
  - 不走城市服務密度
  - 不走抽象地下深層
  - 改用林蔭遮蔽、舊哨、濕地、獵徑與戰前耳語建立壓力

## Player Loop Contract

- `主線推進`
  - 從 `city_chenliu` 北出後進入林蔭道、濕地與前哨殘路
  - 往北感受到官渡戰場氣氛逐步增強
- `探索與風險辨識`
  - 路牌漸少
  - 林下視線變差
  - 舊軍哨與倒木形成天然埋伏點
- `傳聞節點`
  - 樵夫歇棚
  - 斥候舊哨
  - 枯池邊石
- `地形節奏`
  - 平面林道
  - 濕地側線
  - 高土塍與下陷獵徑

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0054-wild-puyang-forest.md`
- 建立 `area/wild_puyang_forest/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `south-threshold`
  - `forest-road`
  - `wet-hollow`
  - `old-scout-line`
  - `north-warfront`
- 將 `樵棚 / 舊哨 / 枯池 / 去路 / 官渡` 視為正式 `#Enquire` 候選
- 將 `路牌 / 倒木 / 斷旗 / 枯池 / 哨樓` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 非平面林塍 / 壕溝位移
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Birthplace Policy

- `wild_puyang_forest` 是中段野外承接區，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `south-threshold`
  - 北出林口、林蔭官道、最後清楚路牌
- `forest-road`
  - 林間主徑、倒木彎道、樵夫歇棚
- `wet-hollow`
  - 枯池濕窪、蘆草泥路、下陷獵徑
- `old-scout-line`
  - 舊哨木梯、斥候土塍、殘旗監看點
- `north-warfront`
  - 北向荒路、戰前風聲、官渡前帶

## Suggested Theme Hooks

- `south-threshold`
  - 讓玩家感覺自己剛離開城市控制範圍，秩序還在，但已不穩
- `forest-road`
  - 用林蔭、倒木與分岔感建立視線受阻的探路壓力
- `wet-hollow`
  - 用泥濘、蘆草與水痕營造不適與伏兵感
- `old-scout-line`
  - 用舊哨、殘旗與抄近路痕跡暗示軍旅前帶
- `north-warfront`
  - 把官渡的戰前空氣先吹進來，但不提早直接變成戰場

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/road_puyang/map.md`
- `ref/sanguo-area-specfirst/area/city_puyang/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/road_puyang/map.md`
  - `ref/sanguo-area-specfirst/area/city_puyang/map.md`
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
  - `city_chenliu` 之後的野外承接帶
  - `濮陽` 與 `官渡` 之間需要戰前探索型練功區
  - progression map 的 `陳留 -> 濮陽 -> 官渡` 主線節奏
- `compliance_check`
  - compliant；本輪以 `City -> Wild` 做題材切換，維持 queue variety，不回頭延續 spirit-core 深井鏈

## First-Round Validation

- `area/wild_puyang_forest/map.md` 必須包含有效 `mapmd-json`
- 林野探索 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `wild_puyang_forest` 不得退化成單一路直通 connector；必須保留側線、視線壓力與戰前前哨氣氛

## Next Step Prompt

`先 commit 目前 wild_puyang_forest 的 spec milestone；commit 後開始 Milestone 2，依 area/wild_puyang_forest/map.md 生成 roo 草案並建立最小 runtime index/mob/obj/res/shp。`
