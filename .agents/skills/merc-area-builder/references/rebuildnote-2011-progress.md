# 3Y Rebuildnote 2011 Progress Reference

這份補充參考整理 `https://3yrebuildnote.blogspot.com/2013/04/blog-post.html`（2013-04-23 發文、回顧 2011-03-14 到 2011-04-25 的重建進度）的可操作訊號。

## 用途

- 補 `world_map`、`ref/`、`players.json`、`skills.json` 之外的「歷史重建時期」脈絡
- 幫助判斷 area queue、等級帶、城市規模與 generator 投資是否合理
- 幫助判斷技能數值重建應不應該設成分批、可回滾、需實測的流程

## 它不是什麼

- 不是 current repo 的 source of truth
- 不是 current runtime registry
- 不是 loader / parser schema 文件
- 不是可以直接覆蓋 `area/world_map.md`、`ref/Readme.md` 或單區 plan 的最終權威

## 可直接採用的歷史訊號

- `2011-03-14`
  - 陳留城 `roo` 曾完成到 `213` 個房間
  - 大型城市手寫 `roo` 很容易踩到 parser / terminator 錯誤，當時需要大量逐段 debug
- `2011-03-15`
  - 洛陽城郊完成 `37` 房，定位約 `Lv15~Lv25`
  - 技能數值已開始分批重建，尤其是步法與部分攻擊技能
- `2011-03-29`
  - 已完成房間產生器與區域產生器
  - `長安` 這種 `300+` 房的大城若沒有 generator，純手改成本極高
- `2011-04-07`
  - 已完成第二版區域產生器與怪物產生器
  - 弘農、陳留先只放基本設施 NPC，再逐步補完整城內內容
  - 黃土高原定位約 `Lv15~Lv20`，並帶小型任務
  - 黃巾賊窟討伐預計約 `Lv25~Lv35`
- `2011-04-10`
  - 山賊窟完成，定位 `Lv26~Lv35`
- `2011-04-18`
  - 長安城完成，定位 `Lv35~Lv50`
  - 針對不能連擊的技能補做傷害數值重設
- `2011-04-25`
  - 南蠻區域大致完成，定位 `Lv50~Lv60`

## 使用規則

- 若 `players.json` / `skills.json` 只能說明 teacher 與服務 loop，卻無法說明 rebuild-era 的 area queue 或 level band，可用這份補歷史脈絡
- 若單區是大型城市或預期會超過 `100` 房，優先考慮 generator / scaffold，而不是直接手刻大量 `.roo`
- 若 blog 提到的是「先放基本設施 NPC，再逐步補完整內容」，可用來支持 service backbone first 的 staging 策略
- 若 blog 提到的是技能數值與連擊/步法交互影響，預設把技能重建視為需實測、可迭代的工作，不要寫成一次性定版假設

## 回寫要求

- 若這輪真的用到這份補充參考，單區 plan 或 tracker 的 `ref_inputs_used` 要寫明：
  - 精確 URL
  - 使用的是哪一段歷史訊號
  - 它影響的是 area order、level band、城市規模，還是技能重建節奏
- 若最後決定不採用 blog 的歷史做法，也可以在 `ref_inputs_deferred` 或 `compliance_check` 記錄「有查過，但刻意未採用」
