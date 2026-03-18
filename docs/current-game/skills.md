---
layout: default
title: Current Game Skills
---

# Current Game Skills

這份文件記錄目前 `merc-fju-3.0` 的整合技能台帳規則，用來把：

- 舊站技能設計證據
- 現行 runtime 技能存在狀態
- 目前 audit / rebuild 進度

放在同一個可追蹤的地方，而不再只記「repo 額外補上的技能」。

對應的機器可讀整合台帳在 `docs/current-game/skills.json`，但它現在是 generated read model，不再是 editable source。

目前 GitHub Pages 可讀頁入口：

- `docs/current-game/skills-index.md`
- `docs/current-game/skill-file-format.md`
- `docs/current-game/skill-loader-reference.md`
- `docs/current-game/skill-constants.md`
- `docs/current-game/skill-pry-crosswalk.md`
- `docs/current-game/skills/step.md`
- `docs/current-game/skills/sword.md`
- `docs/current-game/skills/bow.md`
- 以及其餘依舊站葉節點生成的分類子頁

這些頁面由 `scripts/generate_current_game_skills_pages.py` 生成，後續若 `skills.json` 更新，應重新執行該 script。
只有 `skill-file-format.md` 這類 schema / loader 說明頁是手寫維護，不走生成流程。

目前推薦的同步順序是：

1. 修改 `data/structured/skills/skills.json`
2. `python -X utf8 scripts/export_structured_skills.py --check`
3. 需要落地時：`python -X utf8 scripts/export_structured_skills.py --write`
4. `python -X utf8 scripts/build_current_game_skill_registry.py`
5. `python -X utf8 scripts/generate_current_game_skills_pages.py`

前 3 步負責把 canonical structured source 對齊到 runtime artifact；後 2 步才把更新後的 runtime / audit 狀態投影成 `docs/current-game/skills.json`、`skills-index.md` 與 `docs/current-game/skills/*.md`。

## 邊界

- `docs/3yWebsite/`：reference-only，主要提供舊版世界觀、命名語彙、公告與技能體系脈絡。
- `docs/current-game/skills.md`：現行 repo 的整合技能台帳說明。
- `data/structured/skills/skills.json`：skill runtime artifact 的 canonical structured source。
- `docs/current-game/skills.json`：整合型技能總表；保留 legacy chain、structured source、runtime audit、NPC-only 設計與 audit 狀態。

## 舊站參考基線

目前這份文件在技能脈絡上，已明確參考兩份舊站 JSON 與一份新手導引頁：

- `docs/3yWebsite/docs/data/skills.json`
  - 用來抓舊版技能的中文名、分類、可否互相教導、資源消耗與升階鏈
- `docs/3yWebsite/docs/data/players.json`
  - 用來補強玩家攻略裡實際出現的技能路線、入門技能組與職系定位
- `docs/3yWebsite/newhand/newbies/index.html`
  - 用來補強新手期實際會接觸到的技能分類、學習方式、以及「至少致能一個攻擊類、一個步法、一個逃跑類」的戰鬥建議

這三份資料目前是 `reference baseline`，不是現行 runtime registry。
也就是說：

- 新遊戲裡技能是否真的存在，仍以 `skill/*.ski`、`skill/skill.lst`、`src/merc.h`、`data/symbol.def` 為準
- 舊站 JSON 只用來回答「這個技能在舊世界裡原本屬什麼脈絡」與「新技能替換是否有合理對照」

## Runtime Source Of Truth

目前的 authoring / runtime 分工如下：

- authoring source：`data/structured/skills/skills.json`
- runtime artifact：`skill/*.ski`、`skill/skill.lst`
- loader contract：`src/merc.h`、`data/symbol.def`
- generated read model：`docs/current-game/skills.json`

真正決定目前遊戲技能是否存在、可否載入、NPC 會不會使用的 boot input 仍然是：

- `skill/*.ski`
- `skill/skill.lst`
- `src/merc.h`
- `data/symbol.def`
- 對應 `mob/*.mob` 的 `Enable` / `AutoEnable`
- 必要時的 `obj/*.obj` 與 `res/*.res`

這份文件只做開發紀錄；`docs/current-game/skills.json` 也只做 read model，不取代上述 runtime boot input。

## Mob 端技能掛法

參照 `document/mob.txt`，目前 mob 端和技能直接相關的欄位至少有：

- `Enable <數值> '<技能名>'`
  - 代表固定熟練度的技能掛法
  - 比較適合已知身份鏈、需要穩定 runtime 行為的 NPC
- `AutoEnable '<技能名>'`
  - 代表交給 loader 依怪物條件自動反推熟練度
  - 不應和固定 `Enable` 視為同一種資料
- `AttackRatio`
  - 會影響 offensive skill 經 `get_adeptation()` 反推時的目標強度
- `DodgeRatio`
  - 會影響 dodge skill 經 `get_adeptation()` 反推時的目標強度
- `#Learn`
  - `Adept / Cost / Inventory / Name`
  - 這是 mob 的教學能力，不是 combat template，但仍屬 skill-facing runtime data

這代表 skill audit 不能只看 `skill/*.ski`：

- 同一個 skill template 若掛在 `Enable 45` 與 `AutoEnable` 的 NPC 上，風險不同
- `AutoEnable` 的 failenable 告警，必須連同 mob 的 `Level / AttackRatio / DodgeRatio` 一起解讀
- `#Learn` 若和 `Teach / CanAsk / Valid` 或 NPC 身份衝突，也應視為技能系統的一部分

目前 registry 雖然還沒有把每個 skill 的 mob usage 全量展開，但後續若某條鏈需要重判，至少要補看：

- `area/*/mob/*.mob` 的 `Enable`
- `area/*/mob/*.mob` 的 `AutoEnable`
- `area/*/mob/*.mob` 的 `AttackRatio / DodgeRatio`
- `area/*/mob/*.mob` 的 `#Learn`

## Current Registry Schema

`docs/current-game/skills.json` 現在不再只記 supplemental additions，而是改成整合型 registry。每筆 skill 目前可包含：

- `legacy_navigation`
  - 舊站技能導覽層的群組與葉節點
  - 例如 `武器技能 / 劍`、`法術技能 / 雷系`、`其他技能 / 步法`
- `legacy_catalog`
  - `docs/3yWebsite/docs/data/skills.json` 的原始抽取欄位
  - 用來保留舊站頁面上已被扁平抽出的技能資料
- `legacy_reference`
  - 舊站 HTML / JSON 的來源頁
  - 舊站技能鏈中的前後關係
  - 舊站顯示的 prerequisite
- `legacy_requirements`
  - 舊站 HTML 解析出的 `職業限制`
  - `限 制` 中的屬性門檻、技能熟練度門檻、職業限制
  - `教 導` 來源
- `runtime`
  - 是否存在於目前 repo
  - `skill_file`
  - `skill_lst_key`
  - `slot_symbol`
  - `type`
  - 需要時補 `cost / wait / associate / canask / teach / valid / enable`
- `combat_dimensions`
  - `damage_values`
  - `chance_values`
  - `parry_values`
  - `innate_values`
  - `wait / cost / cost_type / weapon / check`
  - `damage_source`
  - `damage_gap_classification`
  - `code_path`
  - `code_damage_summary`
  - 以及後續調整批次要補的備註
- `status`
  - 是否玩家向
  - 是否 NPC-only
  - 目前 audit 狀態，例如 `runtime_active`、`batch_b_prechecked`、`legacy_unreviewed`

這個 schema 的目標是讓後續工作能直接回答：

- 這個技能在舊站屬於哪條鏈
- 它在舊站有哪些職業限制、屬性限制、前置技能限制、教學來源
- 目前 runtime 還在不在
- 它是玩家技能還是 NPC-only
- 它現在是否已納入某個 rebuild 批次
- 它目前的 combat template 長什麼樣，之後要改哪些維度

## Missing Damage Sections 分類

目前 current-game registry 不再把所有空的 `damage_values` 都直接視為 skill data 壞掉，而是會先區分：

- `data-driven`
  - 傷害模型寫在 `.ski -> #Damage`
- `code-driven`
  - `.ski` 沒有 `#Damage`
  - 但真正傷害寫在 `src/spell.c` 或 `src/ex_spell.c` 的 `cast_*()` / `spell_*()` 裡
- `unresolved`
  - 目前還看不出直接傷害路徑，需要另做 review

這條分類主要是為了解決像 bow 主鏈這種情況：

- `shoot sun`
  - 是 `data-driven`
- `water cloud blast`
  - 是 `code-driven`
  - 真正輸出在 `cast_water_cloud_blast()`
- `fun wu blast`
  - 是 `code-driven`
  - 真正輸出在 `cast_fun_wu_blast()`

因此 `Damage values: []` 不再自動等於「技能沒作用」；要先看 `damage_source` 與 `code_path`。

## Legacy Skill Damage 重建注意事項

近期技能鏈重建已確認：大量 legacy `skill/*.ski` 的 `#Damage Value` 曾被壓成 `20`，這會直接扭曲 failenable 對高等 mob 的判讀，也會讓玩家向技能鏈失去原本應有的階梯。

但這不代表之後所有修正都應該只看 `Value`。實作上至少還要同時檢查：

- `#Damage Chance`
- `#Damage Parry`
- `#Damage Innate`
- `Wait`
- `Cost`
- `CostType`
- `Weapon`
- `Check`

另外還要連同 combat runtime 一起判讀：

- `src/handler.c`
  - `get_adeptation()` / failenable 比較接近「模板太弱或太強的靜態告警」
- `src/fight.c`
  - 會把命中、護甲、閃避、防護類效果帶進實戰結果
- `src/skill.c`
  - 會把等待時間、資源與武器限制帶進技能體感

因此目前的維護原則是：

- 先承認 `Value=20` 大量殘留本身是問題
- 但不要把所有高階技能都修成同質高傷模板
- 保留武器差異、節奏差異、職系差異與技能風格差異
- 做玩家向技能鏈重建時，優先用 `docs/3yWebsite/docs/data/players.json` 與 `docs/3yWebsite/docs/data/skills.json` 還原「進階順序與定位」，再回頭調整 runtime skill template
- 若某個 skill 主要是經 `AutoEnable` 供 mob 使用，還要把 `AttackRatio / DodgeRatio / Level` 一起列進判讀，避免把 mob 端反推熟練度問題誤判成 skill 檔本身唯一失真

## 2026-03 NPC 身份戰技補完

| 技能 | 檔案 | 主要用途 | 主要對象 | 補充 |
| --- | --- | --- | --- | --- |
| `military blade` | `skill/m/military_blade.ski` | 軍旅刀法 | 城市守衛、城門守衛、禁軍護衛 | 用來取代不合身份的低階江湖散招。 |
| `military steps` | `skill/m/military_steps.ski` | 軍旅步法 | 城市守軍、騎卒、低中階軍職 NPC | 對齊列伍、巡城、軍門轉位感。 |
| `imperial sword` | `skill/i/imperial_sword.ski` | 御衛劍法 | 殿前護衛、御前護衛、皇宮禁衛軍高階樣本 | 形成明確高於城市守軍的階梯。 |
| `imperial steps` | `skill/i/imperial_steps.ski` | 御衛步法 | 殿前 / 御前護衛 | 和皇城禮制、厚甲、巡守定位相配。 |
| `night blade` | `skill/n/night_blade.ski` | 夜行刀法 | 盜賊、浪人、大盜類 NPC | 保留高機動與狠辣風格。 |
| `shadowtrace steps` | `skill/s/shadowtrace_steps.ski` | 夜行步法 | 盜賊、浪人、大盜類 NPC | 和 `night blade` 配套，避免只掛基礎步法。 |
| `cavalry lance` | `skill/c/cavalry_lance.ski` | 軍旅槍術 | 騎兵與持槍軍職 NPC | 補足軍旅兵器技能缺口。 |

## 目前已落地的 legacy reference 訊號

這一批現行技能文件目前已正確接上的舊站訊號包括：

- `skills.json -> cloud steps`
  - 舊站標成閃躲類，且可領悟 `gdragon steps`
- `players.json -> 刺客精練-步法 / 將軍精練-步法`
  - 兩篇都把 `cloud steps -> gdragon steps` 當成玩家向步法路線
- `skills.json -> hua sword`
  - 舊站標成可互相教導、可往 `fonxan sword` 升階的入門劍法
- `players.json -> 新手上路`
  - 把 `cloud steps`、`hua sword`、`long fist`、`flee` 放在早期 learn 清單
- `newhand/newbies/index.html -> skills / enableskill`
  - 把技能分成攻擊、步法、逃跑、法術、雜類五大類
  - 明確建議新手至少致能一個攻擊類、一個步法、以及一個逃跑類技能
- `players.json -> 刺客精練-前言與說明 / 弱弱的刺客之道 Part 2`
  - 把 `two sword / 雙十` 放在刺客高階劍法脈絡，而不是城防或禁軍制式技能脈絡

這些訊號目前主要拿來支撐兩件事：

- 說明為什麼 `military blade` / `military steps` / `imperial sword` / `imperial steps` 這批 NPC-only 技能是合理替換，不只是任意重命名
- 區分哪些舊技能屬於「可保留作 legacy 對照」，哪些則已經和現行 NPC 身份鏈錯位

## 2026-03 Legacy Ladder Audit 批次基線

目前已正式展開玩家向 legacy 技能梯階重建，第一批先處理刺客/新手共用的劍法鏈：

| 技能 | 檔案 | 目前定位 | 本輪處置 |
| --- | --- | --- | --- |
| `hua sword` | `skill/h/hua_sword.ski` | 新手 / 入門劍法 | 拉回低階基線傷害模板，保留作升階起點。 |
| `fonxan sword` | `skill/f/fonxansword.ski` | 中階刺客劍法 | 調整為明確高於 `hua sword` 的中階模板。 |
| `dragon sleeve sword` | `skill/d/dragonsleeve.ski` | 高階刺客劍法 | 調整為高於 `fonxan sword` 的高階模板。 |

這一批的目的不是宣告全體 legacy skill 都已平衡完成，而是先把「同一條玩家向技能鏈不應全部等傷」這個最低限度的 runtime 梯階補回來，並作為後續步法、拳法、刀法批次的對照基線。

## 2026-03 Batch B 前置盤點結論

第二批預備處理的步法樣本是 `cloud steps`、`gdragon steps`、`sky steps`，但前置盤點後已確認它們不是單一直線：

- `cloud steps -> gdragon steps`
  - 舊站 `skills.json` 與 runtime `Associate` 都支持這條主鏈
- `sleev steps -> sky steps`
  - 舊站 `players.json` 與 runtime `Associate` 都支持這條分支

所以 Batch B 的正確做法不是把 `cloud / gdragon / sky` 當同一條 ladder 一起上調，而是：

- 把 `cloud -> gdragon` 當主鏈處理
- 把 `sky steps` 當平行高階步法處理，保留它「花費體力很少」的特色

前置盤點也確認：

- 三者目前 `#Damage Value` 都仍是 `20`
- 但 `Cost / Wait` 沒有被壓平
- `cloud steps` 仍保有低耗、極短 wait 的入門高頻特性
- `gdragon steps` 與 `sky steps` 都是 `Wait 10`，但 `sky steps` 的 `Cost 10` 低於 `gdragon steps` 的 `Cost 15`

這代表 Batch B 下一步修值時，應優先重建 dodge template，而不是抹掉原本殘留的節奏與耗能差異。

## 2026-03 Step Family Registry Seed

目前 `docs/current-game/skills.json` 已完成三層 seed：

- 舊站 `docs/3yWebsite/docs/data/skills.json` 的全部 `31` 筆條目
- `docs/3yWebsite/skill/*.html` 額外才看得到的 descendants
- 舊站 HTML 才有的 `職業限制 / 限制 / 教導` 結構化欄位

所以現在至少能直接看出這些舊設計：

- `cloud steps -> gdragon steps -> mirage steps`
- `sleev steps -> sky steps`
- `nine steps -> color steps`
- `cloud ghost -> wind color steps`
- `shade steps -> wind steps`
- `night steps` / `free steps` / `hundred steps` / `eight steps` 為獨立或特殊高階線

這一批的意義是把舊站 HTML 才看得到的鏈路拓樸，正式轉進 current-game registry，避免之後只靠舊的扁平 JSON 推錯技能鏈。

目前 coverage 仍是第一版，但已不再只有步法：

- 已納入：
  - 舊站 `skills.json` 全條目
  - 舊站 `skill/*.html` 各頁的額外升階節點
  - 舊站 HTML 中的職業限制、屬性限制、前置技能熟練度限制、教學來源
  - 2026-03 NPC-only 新技能
- 尚未納入：
  - 其他舊站 HTML 頁裡、但沒有被 `skills.json` 扁平抽出的升階 descendants
  - 每個 skill 對應的 mob 使用樣本
  - 每次 rebuild 後的 before/after combat audit 快照

所以後續若要做全技能總表，正確方向是繼續擴這份 schema，而不是回頭把 `docs/3yWebsite/docs/data/skills.json` 當成現行 registry。

## 舊站分類骨架保留

新台帳現在也保留了舊站技能導覽骨架，不只保留單筆 skill 資料。也就是說，這些既有分類已經能在 `docs/current-game/skills.json` 裡直接表達：

- `武器技能`
  - `劍` `刀` `弓` `槍` `棍`
  - `斧` `鞭` `筆扇` `短兵` `拳法`
  - `氣功`
- `法術技能`
  - `火系` `風系` `光系` `聖系` `雷系`
  - `水系` `土系` `暗系` `邪系` `毒系`
- `職業技能`
  - `格鬥系` `暗殺系` `法師系` `鑄造系` `吟唱系`
  - `醫療系` `盜賊系`
- `其他技能`
  - `步法` `技能` `技能熟練度`

其中有一個 normalization：

- 舊站抽取 JSON 裡有 `雷電系`
- 新台帳的導覽骨架統一記成 `雷系`
- 但原始 `legacy_catalog` 欄位仍保留舊字樣，不會覆蓋掉原始資料

## 維護規則

- 若只是引用舊版名稱、熟練度詞彙、背景設定或技能鏈靈感，更新 `docs/3yWebsite/` 以外的現行 repo 檔案即可，不要回寫舊站鏡像。
- 若目前 repo 新增了真正會被 loader 載入的新技能，除了 runtime 檔案外，補記在這份文件與 `docs/current-game/skills.json`。
- 若未來要擴充機器可讀的現行技能台帳，應繼續放在 `docs/current-game/` 或其他 repo 自有資料路徑，而不是直接擴寫 `docs/3yWebsite/docs/data/skills.json`。
