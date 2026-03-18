# Object Affects Restricts And Jobs

## 何時讀這份
- 你正在處理 `.obj` 的附加 block，而不是主欄位。
- 你要加屬性、額外描述、裝備限制、互動 job 或訊息。

## 搭配閱讀
- `references/obj-file-layout.md`
- `references/obj-core-fields.md`
- `references/system-sync-checks.md`

## `#Affect`

用來定義物品帶來的能力或屬性修正。

常見欄位會包含：

- `Location`
- `Modifier`

實務上要和 repo 常數、已成功載入的裝備範例一起看。

## `#Extra`

用來定義可以 `look <keyword>` 看到的補充描述。

常見欄位：

- `Keyword`
- `Description`

這是「額外可檢視描述」，不是新的玩家命令。

## `#Job`

讓物品能把特定關鍵字導向 `job.c` 裡已註冊的 function。

要先確認兩件事：

- data 檔真的有 `#Job`
- `src/job.c` 真的有對應 function

只寫文字提示不等於功能存在。

## `#Restrict`

用來做職業、技能、條件等限制。

若限制涉及技能、職業或 nation/system 行為，別只停在 `.obj`；應再檢查：

- `src/merc.h`
- `src/class.c`
- `data/structured/skills/skills.json`
- repo 既有 working examples

## `#Message`

用來補充與物品互動或使用時的訊息。

## Repo-specific guardrail

- 任何 block 都要以自己的 `End` 關閉，避免吃掉後續欄位。
- 若物件互動其實依賴全域 skill、job 或系統規則，不要把問題誤判成單純 `.obj` 語法問題。
- `#Job` 和 `#Extra` 很容易被混淆：前者是可觸發 function 的互動，後者只是附加描述。
