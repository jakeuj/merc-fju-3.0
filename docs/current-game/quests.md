---
layout: default
title: Current Game Quests
---

# Current Game Quests

這頁整理目前 `merc-fju-3.0` 的 quest / question runtime registry，讓 GitHub Pages 上能直接查到這套系統的載入來源、格式與現況基線。

對應的機器可讀台帳在 `docs/current-game/quests.json`。

## 邊界

- `docs/current-game/quests.md`：現行 repo 的 quest / question 補充說明。
- `docs/current-game/quests.json`：目前 runtime 的 quest / question 機器可讀台帳。
- `area/rebuild_plan.md`、`plans/area/*.md`：仍然是 area rebuild 專用追蹤，不取代 quest registry。
- 預設 area rebuild 不要求補 `data/quest`；只有單區 runtime flow 明確依賴 quest mark 時，才把 quest data 視為該區附帶交付物。

## Runtime Source Of Truth

目前這套系統的實際載入來源是：

- `data/quest`
- `data/question`
- `src/db.c`
- `src/load.c`
- `src/quest.c`
- `src/question.c`
- `src/merc.sample.ini`
- `src/merc.ini`

area 內容本身不直接提供 quest registry，但 area 的 mobprog 仍可能透過 `mpsetquest`、`mpremquest`、`isquest` 間接依賴 quest mark。

## 目前基線

- `QUEST FILE` 目前指向 `data/quest`
- `QUESTION FILE` 目前指向 `data/question`
- quest entries：`0`
- question entries：`30`
- 目前啟動訊息基線：
  - `系統載入 0 個解謎資料。`
  - `系統載入 30 個問題資料。`

這代表 quest registry 目前仍是空的，但 question bank 已經有一組可正常載入的題庫。

## 載入順序

在 `src/db.c` 的 boot 流程中，這套資料是用下列順序載入：

1. `load_bus`
2. `load_ship`
3. `load_quest`
4. `load_question`
5. `load_immlist`

因此它屬於 current-game runtime content，不屬於 area directory 的直接載入範圍。

## Quest 格式

`data/quest` 的單筆格式以 `#Quest` 開頭、`End` 結尾，loader 目前會讀以下欄位：

- `Keyword`
- `Information`
- `Show`
- `Title`
- `Help`

目前語意：

- `Keyword` 對應 `QUEST_INFO.mark`，必須全域唯一。
- `Information` 對應 `QUEST_INFO.info`，會出現在 `qstat` 一類工具輸出。
- `Show` 控制這筆 quest 是否應出現在可見清單。
- 若 `Show` 開啟，loader 期待同時提供 `Help`。

## Question 格式

`data/question` 的單筆格式以 `#Question` 開頭、`End` 結尾，loader 目前會讀：

- `Title`
- `Question`

其中每一行 `Question` 會同時帶選項文字與 `YES` / `NO` 答案旗標。loader 目前至少要求：

- 題目要有 `Title`
- 至少兩個以上選項
- 至少一個正確答案

目前 repo 內基線題庫是 `30` 題，每題 `4` 個選項，且每題 `1` 個正確答案。

## 指令面

目前可直接關聯到這套資料的指令 / 介面包含：

- 玩家面：`question`
- 管理或 builder 面：`qstat`、`qset`
- mobprog / script 面：`mpsetquest`、`mpremquest`、`isquest`

也就是說，這套系統雖然不是 area registry，但若某個 area 的 NPC 或事件設計需要 quest flag，就會跟它產生實際 runtime 耦合。

## 目前判讀

- `0` 個 quest entries 不是 area loader 壞掉，而是 `data/quest` 目前尚未填入正式 `#Quest` 條目。
- `30` 個 question entries 代表防呆 / 問答題庫仍有正常內容。
- 目前 area rebuild 的正式主軸仍是 world graph、single-area spec、`.roo` 投影、boundary links 與 runtime 驗證，不是全面回補 legacy quest system。
- 若未來要把某段解謎正式掛進 area 設計，建議只在該單區真的依賴 quest mark 時才升級處理：
  - 在單區 plan 記錄 quest mark 依賴
  - 在 `data/quest` 補正式條目
  - 再同步更新 `docs/current-game/quests.json`

## 相關檔案

- [Quest / Question 機器可讀台帳](./quests.json)
- [Current Game 首頁](./index.html)
- [Area 補充說明](./areas.html)
- [技能補充說明](./skills.html)
