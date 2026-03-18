# Room Exits And Interactions

## 何時讀這份
- 你在修出口、世界連結、房內互動、`#Keyword` / `#Job` / `#Enquire`。
- 你要確認房間提示是否真的對應到可執行功能。

## 搭配閱讀
- `references/room-file-layout.md`
- `references/room-flags-and-sectors.md`
- `src/act_move.c`
- `src/job.c`

## `#Exit`

常見欄位：

- `Direction`
- `ExitVnum`
- `ExitDesc`
- `ExitKeyword`
- `Message`
- `ExitKey`
- exit flags

### 實務規則
- `Direction` 必須是 loader 能接受的合法方向。
- `ExitVnum` 必須存在，且跨 area 邊界時兩側都要同步。
- `ExitKeyword` / `Message` 不是裝飾欄位，很多互動文感會靠這裡成立。

## `#Keyword`

讓玩家可 `look <keyword>` 看到額外描述。

它只提供額外檢視內容，不會自動產生命令或行為。

## `#Job`

把房間內某個 keyword 對到 `src/job.c` 已註冊的 function。

若房間文案暗示某個動作可用，但玩家實際不能做，常見原因是：

- 沒有對應 `do_*`
- 沒有 `#Job`
- `job.c` 裡沒有對應 function

## `#Enquire`

today repo area work 的正式互動 block。

它常用在：

- 問路
- 區域 lore
- teacher / service 提示
- 交通、任務、功能導引

spec-first area 做服務節點或新手導流時，`#Enquire` 應和 `players.json` / `skills.json` 的玩法耦合一起考慮。

## Direction guardrail

現行 area work 至少要接受：

- `north`
- `east`
- `south`
- `west`
- `up`
- `down`
- `enter`
- `out`

不要把出口系統縮成傳統四向。

## Repo-specific guardrail

- `src/load.c` 會擋錯誤方向，常見訊息是 `Load_exit﹕錯誤的方向 %d。`
- world link 任務一定要同步新區與舊區邊界房。
- `#Keyword` 只是描述；`#Job` / 內建 `do_*` 才是互動入口。
