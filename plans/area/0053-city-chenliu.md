# City Chenliu Initial Area Plan

## Summary

建立下一個待建新 AREA：`city_chenliu`。此區是主世界 rebuild 由晚期 `sec_rift_spirit_core_*` plateau 轉回三國地表主線的第一個正式節點，定位為中原樞紐城市與軍旅 / 江湖中繼城。

## Theme Positioning

- theme: `歷史城市`
- subtheme: `中原樞紐城 / 軍旅與江湖中繼`
- experience_type: `City`
- player_loop_focus: `補給 / 學技 / 旅行 / 軍旅徵募 / 打探情報`
- contrast_with_previous_two:
  - 相對於 `sec_rift_spirit_core_infernal` 與 `sec_rift_spirit_core_gehennal` 的垂直、封閉、滿級 endgame 深井，`city_chenliu` 應是橫向展開、日照可感、NPC 與服務密度高、路線分流明確的主線城市 hub
- 世界缺口角色：
  - 把主世界 progression 從 `洛陽` 自然推進到 `陳留 -> 濮陽 / 官渡 -> 虎牢 -> 襄陽 / 江夏`
  - 提供 midgame 玩家補給、武學學習、旅行轉接與地方軍旅導流
- reserved_room_block: `13801-13830`
- planned_vnum_range: `13801-13830`
- level_range: `15-26`
- external_links:
  - `west`: `city_loyang` / `road_chenliu_loyang`
  - `north`: `wild_puyang_forest` / 濮陽主線
  - `east`: 徐州向主幹
  - `south`: `district_chenliu_station` / 許昌支線
- delivery_gate: `implementation_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `歷史城市`
  - `中原交通樞紐`
  - `軍旅與江湖共存的服務城`
- 它補的玩家 loop：
  - `補給`
  - `學技`
  - `旅行`
  - `招募 / 軍旅導流`
  - `地方情報 / 問路`
- 它和前兩個已完成 area 的題材差異：
  - 不再以「更深、更暗、更滿級」製造變化
  - 改用城市街廓、師父 NPC、商店服務、城門盤查、驛站分流與軍旅組織來提供玩法差異

## Player Loop Contract

- `補給與後勤`
  - `食堂`
  - `錢莊`
  - `武器店`
  - `防具店`
  - `打鐵舖`
  - `馬廄`
  - `鏢局`
- `武學與江湖服務`
  - `華山劍法`：陳留城 `十文字劍 / swordman`
  - `風雲袖步`：陳留城 `浪人 / bravo hashin an`
  - `翦雲步`、`金蟬脫殼(flee)`：陳留城 `震南山 / zhen nan shan`
- `軍旅與地方勢力 loop`
  - `太守衙門`
  - `虎豹騎招募處`
  - `義勇軍`
  - `測驗場`
  - `鼓樓 / 鐘樓`
- `旅行 loop`
  - 向西回 `洛陽`
  - 向北接 `濮陽 / 官渡`
  - 向東往 `徐州`
  - 向南接 `陳留驛站 / 許昌線`

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0053-city-chenliu.md`
- 下一輪建立 `area/city_chenliu/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `west-gate`
  - `main-street`
  - `service-quarter`
  - `militia-quarter`
  - `south-station`
- 將 `城門 / 太守衙門 / 食堂 / 拳館 / 驛站` 視為正式 `#Enquire` 候選
- 將 `告示 / 招牌 / 城門 / 軍旗` 視為正式 `#Keyword` 候選
- 至少保留一組 `enter/out` 室內或驛站轉場
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Birthplace Policy

- `city_chenliu` 是 midgame 服務樞紐，不是預設出生地
- 未來 `index` 若建立，`Capital` 預設維持 `0`

## Suggested Room Clusters

- `west-gate`
  - 城門盤查、回洛陽主道、公告與問路入口
- `main-street`
  - 城內主幹道、人流、市聲、招牌密度
- `service-quarter`
  - 食堂、錢莊、武器 / 防具 / 打鐵 / 馬廄 / 鏢局
- `militia-quarter`
  - 太守衙門、虎豹騎、義勇軍、拳館、測驗場
- `south-station`
  - 驛站、行李、車馬與往許昌 / 徐州的轉接

## Suggested Theme Hooks

- `west-gate`
  - 玩家一進城就感受到中原主線交通節點與盤查壓力
- `main-street`
  - 用招牌、攤販、吆喝與旅人對話感建立城市熱度
- `service-quarter`
  - 把補給、裝備、馬匹、金流與鏢局整合成可閱讀的城市後勤面貌
- `militia-quarter`
  - 用軍旗、試武、衙門與徵募感建立地方武備與曹魏壓力
- `south-station`
  - 讓玩家明確感受到這裡不是終點，而是往許昌、徐州與更南方世界的轉接點

## Reference Entry Points

- `area/world_map.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `docs/3yWebsite/map/chenliu.html`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `ref/mud-area-templates/city_loyang.md`
- `ref/sanguo-area-specfirst/area/city_chenliu/map.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `docs/3yWebsite/map/chenliu.html`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `https://3yrebuildnote.blogspot.com/2013/04/blog-post.html`
  - `https://disp.cc/b/mud_3y/2mUG`
  - `ref/mud-area-templates/city_loyang.md`
  - `ref/sanguo-area-specfirst/area/city_chenliu/map.md`
- `ref_inputs_deferred`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
  - `sec_rift_*`
  - `sec_rift_spirit_core_*`
  - 完整 `213` 房歷史等比還原
- `theme_basis`
  - progression map 的 Lv15 主線城市槽位
  - 題材分布表的中原歷史城市節點
  - 陳留舊站地圖提供的服務節點與城內分區
  - `players.json / skills.json` 提供的師父、技能來源與服務 loop
  - 歷史重建筆記指出陳留曾先完成大型 `roo` 與基本設施 NPC，支持本 milestone 先做城市服務骨架、再分階段擴房
  - 玩家 leveling baseline 將陳留列為 `Lv15-21` 練功城，支持目前 `15-26` 的 service-hub + midgame band 設定
- `compliance_check`
  - compliant；本輪刻意把 queue 從 spirit-core 尾鏈轉回三國主世界城市 / 補給 / 交通 gameplay，而不是延續垂直深井

## First-Round Validation

- 後續 `area/city_chenliu/map.md` 必須包含有效 `mapmd-json`
- 城市服務 loop 必須以明確 node、`#Enquire` 或 `#Keyword` 反映
- 方向只使用 `north / east / south / west / up / down / enter / out`
- `city_chenliu` 不得退化成純戰鬥 dungeon prose；必須保留城市生活、軍旅與交通可讀性

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/city_chenliu/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md --validate-only`
  - passed for `17` room(s)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/city_chenliu/map.md`
  - wrote `roo/13801-13817`
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
  - passed; Linux build path reports `merc` up to date
- `wsl bash -lc "cd /mnt/h/repos/merc-fju-3.0 && timeout 45 bash -lc 'cd src && ./startup.bash'"`
  - startup log `log/1017.log` reached `三國歪傳之降龍伏虎開始正常運作`
  - `debug/badobject` remained empty
  - `debug/error` only records the forced shutdown path caused by timeout, not a loader failure

## Next Step Prompt

`先 commit 目前 city_chenliu 的 implementation milestone；commit 後將 city_chenliu 標記為 done，再把 wild_puyang_forest 推進成下一個 actionable area。`
