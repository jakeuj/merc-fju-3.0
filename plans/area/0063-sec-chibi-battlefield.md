# Sec Chibi Battlefield Initial Area Plan

## Summary

建立下一個待建新 AREA：`sec_chibi_battlefield`。此區承接 `city_chaisang` 南向戰場支線，把江岸城市的秩序與補給節奏切進一段帶有火痕、殘艦、煙灰與歷史回聲的古戰場祕區，讓玩家感受到自己不是單純離城往南，而是踏進一處仍被舊戰意與江風殘響佔據的戰場傷口。

## Theme Positioning

- theme: `軍旅`
- subtheme: `江岸古戰場 / 戰痕幻境`
- experience_type: `Secret`
- player_loop_focus: `戰場探索 / 邊界辨位 / 火痕遺物 / 祕區支線`
- contrast_with_previous_two:
  - 相對於 `dng_sunken_temple` 的濕地下探與 `city_chaisang` 的江岸城鎮秩序，`sec_chibi_battlefield` 應讓玩家感受到一種既開闊又不安的歷史戰場壓力，像是走在被燒黑的江岸與破船殘架之間，隨時會被舊戰意牽去更深處
- 世界缺口角色：
  - 把 `city_chaisang` 已預留的南向 `sec_chibi_battlefield` world-link 正式轉成可持續擴建的 spec-first area
  - 在江岸主線與未來更南、更東的主世界展開之間，先插入一段高辨識度的戰場祕區節奏
- reserved_room_block: `14801-14830`
- planned_vnum_range: `14801-14830`
- level_range: `68-78`
- external_links:
  - `north`: `city_chaisang` / 赤壁路標
  - `south`: `wild_old_battlefield` / 江岸焦土外帶預留
  - `east`: `river_crossing` / 殘艦與浮橋支線預留
- delivery_gate: `spec_ready_for_commit`

## Fun / Variety Check

- 這區提供的三國體驗：
  - `赤壁戰場餘燼`
  - `江岸殘艦與焦木陣地`
  - `帶幻境感的歷史戰痕祕區`
- 它補的玩家 loop：
  - `從城市補給切進高風險支線`
  - `靠地標與戰痕辨認前進方向`
  - `沿殘船、灰坡與祭火臺探索更深事件空間`
- 它和前兩個已完成 area 的題材差異：
  - 不再是官署、市集與問路為主的城市節奏
  - 不再是地下石廊與積水封印的遺跡節奏
  - 改用開闊江岸、焦土陣線與戰後回聲製造不安與探索吸力

## Player Loop Contract

- `主線推進`
  - 玩家由柴桑南牌與赤壁路標切入，先經過邊緣哨帶與焦木坡，再逐步推進到殘艦灘、火痕主陣與祭火高地
- `地標辨識`
  - 透過焦黑船板、插地斷戟、燒裂旗座與江風吹向辨認哪裡像退路、哪裡像更深戰場
- `支線探索`
  - 灰燼壕溝
  - 破旗坡面
  - 殘艦岸棚
- `非平面節奏`
  - `up/down` 用於灰坡、望火臺與壕溝落差，維持古戰場不只是平面大廣場的辨位感

## Scope (Milestone 1: Spec)

- 建立 `plans/area/0063-sec-chibi-battlefield.md`
- 建立 `area/sec_chibi_battlefield/map.md` 第一版
- 以 `mapmd-json` 定義至少五個 cluster：
  - `north-marker`
  - `ash-slope`
  - `burned-flotilla`
  - `ember-line`
  - `ritual-rise`
- 將 `赤壁 / 柴桑 / 戰場 / 焦土 / 江風` 視為正式 `#Enquire` 候選
- 將 `殘艦 / 灰燼 / 斷戟 / 火痕 / 祭臺` 視為正式 `#Keyword` 候選
- 至少保留一組 `up/down` 供灰坡或壕溝落差使用
- 本 milestone 不建立 `index / mob / obj / res / shp` runtime data

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/sec_chibi_battlefield/map.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0062-city-chaisang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/sec_chibi_battlefield/map.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0062-city-chaisang.md`
- `ref_inputs_deferred`
  - `ref/sanguo-area-specfirst/area/city_changsha/map.md`
  - `ref/sanguo-area-specfirst/area/city_jianye/map.md`
  - `docs/3yWebsite/map/shanyan.html`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
  - 各類經濟/勢力/歷史事件模擬系統
- `theme_basis`
  - `world_map` 讓 `江夏 -> 柴桑` 成為已落地主線，`city_chaisang` 又已預留 `sec_chibi_battlefield` 的南向戰場支線，現在補上古戰場祕區最順
  - `題材分布表` 的 `古戰場遺址` 與 `軍旅 / 探險` 混合題材，剛好能把江岸城市之後的節奏拉向事件感更強的歷史戰場
  - `players.json / skills.json` 沒有要求此刻必須立即切回另一座教學城市或師父密集區，因此先用高辨識度支線維持探索新鮮度更合理
  - `ref/sanguo-area-specfirst` 已提供可改寫的戰場 scaffold，可直接轉成符合目前 queue 的江岸赤壁版本
- `compliance_check`
  - compliant；在 `City` 之後切一個 `Secret` 戰場支線，題材明確、world-link 已預留、也避免連續再做第三座城市

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/sec_chibi_battlefield/map.md`
  - passed with `0 error(s), 0 warning(s)`
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/sec_chibi_battlefield/map.md --validate-only`
  - passed for `12` room(s)

## Next Step Prompt

`先 commit 目前 sec_chibi_battlefield 的 spec milestone；commit 後把它標記為 done，再直接做 implementation milestone。`
