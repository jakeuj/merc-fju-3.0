# Area Theme Design Patterns

這份索引用來替 `merc-area-builder` 導向較小的題材參考檔，避免每次都把六大題材模板整份讀入。

## 何時讀哪一份

- 若要做世界級題材分布、主城 / 郊外 / 秘境的主題配置，讀 `theme-world-allocation.md`
- 若要做 `歷史城市風` 或 `軍旅風`，讀 `theme-patterns-civic-military.md`
- 若要做 `江湖風` 或 `仙俠風`，讀 `theme-patterns-jianghu-mystic.md`
- 若要做 `詭異民俗風` 或 `探險遺跡風`，讀 `theme-patterns-folklore-ruins.md`

## 共通原則

- 題材模板是 flavor 與設計輔助，不是新的 source of truth
- 優先採用題材母型，不要直接照抄受保護作品的唯一識別名稱
- `三國志`、`三國演義` 的歷史人物、地名、官職、戰役與典故可直接借用，但仍要對齊 repo 與 docs 現有世界線
- 近代武俠 / 仙俠作品以「母型改寫」為主，不直接搬用唯一角色名、門派名、完整招式名或劇情橋段

## 快速套用清單

開始寫新 area 前，至少先決定：

1. 主題與輔題材
2. 玩家第一眼感受
3. 代表場景
4. 主要 NPC 類型
5. 任務鉤子
6. 代表性物件 / 裝備
7. `#Enquire` 詞彙
8. `#Keyword` 提示物件
9. 世界層缺口價值

## 與 `map.md` 的對接

在 `map.md` prose 中至少補：

- `Theme`
- `Subtheme`
- `Mood`
- `Signature scenes`
- `NPC factions or roles`
- `Quest hooks`
- `Interaction cues`
- `Rumor seeds`
- `Local props`
- `Secret node or hidden hook`

若 area 要交給 scaffold script：

- 主題說明留在 prose
- 拓樸、cluster、節點 metadata 留在 `mapmd-json`
- 不要把題材段落寫成會誤導 generator 的假 schema
