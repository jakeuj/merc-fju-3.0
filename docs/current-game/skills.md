---
layout: default
title: Current Game Skills
---

# Current Game Skills

這份文件只記錄目前 `merc-fju-3.0` repo 額外補上的技能資訊，用來避免和 `docs/3yWebsite/` 的舊站參考資料混在一起。

對應的機器可讀補充台帳在 `docs/current-game/skills.json`。

## 邊界

- `docs/3yWebsite/`：reference-only，主要提供舊版世界觀、命名語彙、公告與技能體系脈絡。
- `docs/current-game/skills.md`：現行 repo 額外新增或重定義的技能補充說明。

## 舊站參考基線

目前這份文件在技能脈絡上，已明確參考兩份舊站 JSON：

- `docs/3yWebsite/docs/data/skills.json`
  - 用來抓舊版技能的中文名、分類、可否互相教導、資源消耗與升階鏈
- `docs/3yWebsite/docs/data/players.json`
  - 用來補強玩家攻略裡實際出現的技能路線、入門技能組與職系定位

這兩份資料目前是 `reference baseline`，不是現行 runtime registry。
也就是說：

- 新遊戲裡技能是否真的存在，仍以 `skill/*.ski`、`skill/skill.lst`、`src/merc.h`、`data/symbol.def` 為準
- 舊站 JSON 只用來回答「這個技能在舊世界裡原本屬什麼脈絡」與「新技能替換是否有合理對照」

## Runtime Source Of Truth

真正決定目前遊戲技能是否存在、可否載入、NPC 會不會使用的來源仍然是：

- `skill/*.ski`
- `skill/skill.lst`
- `src/merc.h`
- `data/symbol.def`
- 對應 `mob/*.mob` 的 `Enable` / `AutoEnable`
- 必要時的 `obj/*.obj` 與 `res/*.res`

這份文件只做開發紀錄，不取代上述 runtime 資料。

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
- `players.json -> 刺客精練-前言與說明 / 弱弱的刺客之道 Part 2`
  - 把 `two sword / 雙十` 放在刺客高階劍法脈絡，而不是城防或禁軍制式技能脈絡

這些訊號目前主要拿來支撐兩件事：

- 說明為什麼 `military blade` / `military steps` / `imperial sword` / `imperial steps` 這批 NPC-only 技能是合理替換，不只是任意重命名
- 區分哪些舊技能屬於「可保留作 legacy 對照」，哪些則已經和現行 NPC 身份鏈錯位

## 維護規則

- 若只是引用舊版名稱、熟練度詞彙、背景設定或技能鏈靈感，更新 `docs/3yWebsite/` 以外的現行 repo 檔案即可，不要回寫舊站鏡像。
- 若目前 repo 新增了真正會被 loader 載入的新技能，除了 runtime 檔案外，補記在這份文件與 `docs/current-game/skills.json`。
- 若未來要擴充機器可讀的現行技能台帳，應繼續放在 `docs/current-game/` 或其他 repo 自有資料路徑，而不是直接擴寫 `docs/3yWebsite/docs/data/skills.json`。
