# City Jiangxia Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_jiangxia`。此區承接 `wild_jiangxia_river` 東向渡口前帶之後的第一座真正江港主城，讓玩家從蘆葦、濕灘與殘樁水寨的野外壓力，重新回到有碼頭秩序、港務差役、水軍營棚與市集補給交錯運作的荊州東岸重鎮。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `江港水軍 / 荊州東岸重鎮`
- experience_type: `City`
- player_loop_focus: `港口補給 / 問路轉場 / 水軍城門辨識 / 東進柴桑的水陸節點整理`
- contrast_with_previous_two:
  - 相對於 `city_xiangyang` 的內陸主城與 `wild_jiangxia_river` 的江岸野外，`city_jiangxia` 應讓玩家感受到主線已正式進入以船、碼頭、倉棚與水軍巡防為核心的江港城市秩序
- 世界缺口角色：
  - 把荊州主線從襄陽水路前帶正式接進江夏主城
  - 為後續 `city_chaisang` 與更東向江港鏈建立補給與交通 hub
- reserved_room_block: `14401-14430`
- planned_vnum_range: `14401-14430`
- level_range: `45-55`
- external_links:
  - `west`: `wild_jiangxia_river` / 東向渡口外路
  - `east`: `city_chaisang` / 江東水路主城
  - `south`: `wild_yunmeng_marsh` / 雲夢大澤前帶
  - `north`: `jingxiang_road` / 荊州陸路回程
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `江港城市`
  - `水軍港務`
  - `東岸補給與渡運樞紐`
- 它補的玩家 loop：
  - `由水路野外回到城市補給`
  - `辨識港務、軍務與商旅節點`
  - `為東向柴桑與南向雲夢做問路轉場`
  - `把江岸旅程收束成有秩序的主城 hub`
- 它和前兩個已完成 area 的題材差異：
  - 不再是蘆葦濕灘與殘樁野外
  - 不再是襄陽那種偏城門與主街的內陸城市感
  - 改用碼頭、倉棚、官渡、水軍和港市噪音建立辨識度

## Player Loop Contract

- `主線推進`
  - 玩家從東向渡口進城，先經過外港與驗貨棚，再匯入主街與官署軸線
- `城市補給`
  - 透過市集、藥鋪、船具攤與驛亭把水路旅程重新整理成補給節奏
- `港務辨識`
  - 透過榜牌、路牌、碼頭差役與水軍崗棚讓玩家理解江夏是控制船路的城市，而不只是靠江的普通城鎮
- `立體節奏`
  - `up/down` 用於城門樓、堤岸、棧橋與瞭臺高差，讓港務與軍務都帶有垂直辨識

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0059-city-jiangxia.md`
- 建立 `area/city_jiangxia/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `west-ferry-gate`
  - `harbor-front`
  - `main-street`
  - `market-yard`
  - `naval-yamen`
- 將 `碼頭 / 主街 / 市集 / 官府 / 水軍 / 柴桑` 視為正式 `#Enquire` 候選
- 將 `路牌 / 榜文 / 纜樁 / 帆索 / 船鐘` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供堤岸高差或瞭臺使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Scope (Milestone 2: Runtime Scaffold)

- 依 `area/city_jiangxia/map.md` 生成第一批 `roo`
- 建立最小 loadable runtime 結構：
  - `index`
  - `mob/`
  - `obj/`
  - `res/`
  - `shp/`
- 將 area 登錄到 `area/directory.lst`
- 正式把 `wild_jiangxia_river/14312` 與 `city_jiangxia/14401` 做成雙向 runtime boundary
- 同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`

## Birthplace Policy

- `city_jiangxia` 是中後段江港主城，不是預設新手出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `west-ferry-gate`
  - 東向渡口、驗貨棚、進城牌坊
- `harbor-front`
  - 外港碼頭、纜樁、水路候船區
- `main-street`
  - 江夏主街、官道銜接、公告牆
- `market-yard`
  - 補給市集、藥鋪、船具與雜貨攤
- `naval-yamen`
  - 水軍營棚、港務官署、堤上望臺

## Suggested Theme Hooks

- `west-ferry-gate`
  - 讓玩家明確感覺自己從野外水路重新回到有秩序的城市邊界
- `harbor-front`
  - 用船纜、木樁、潮痕與工人喊聲建立第一眼江港辨識
- `main-street`
  - 把城市的問路、轉場和榜文節奏重新拉回來
- `market-yard`
  - 讓水路補給和旅人消耗真正有落腳點
- `naval-yamen`
  - 讓江夏的軍事角色透過地景和高差自然浮出來

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/city_jiangxia/map.md`
- `plans/area/0058-wild-jiangxia-river.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/city_jiangxia/map.md`
  - `plans/area/0058-wild-jiangxia-river.md`
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
  - `world_map` 把江夏放在襄陽與柴桑之間，是天然的江港樞紐
  - 參考 spec 清楚把江夏定義成水軍重鎮，因此本區首版應優先落成港口、官署與水軍辨識，而不是做成另一條野外或純商城
  - `wild_jiangxia_river` 已建立從襄陽往江夏的水路節奏，現在適合用主城把補給、問路與交通功能收回來
- `compliance_check`
  - compliant；延續主世界三國地表主線，且題材從江岸野外切回江港城市，維持玩法與視覺節奏變化

## First-Round Validation

- `area/city_jiangxia/map.md` 必須包含有效 `mapmd-json`
- 江港補給 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `city_jiangxia` 不得退化成單一路徑 connector；必須保留港口、主街、市集、官署與水軍高差

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_jiangxia/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_jiangxia/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 city_jiangxia 的 spec milestone；commit 後直接開始 implementation milestone。`
