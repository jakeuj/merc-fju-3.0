# Room Exits And Interactions

## 何時讀這份
- 你在修出口、世界連結、房內互動、`#Keyword` / `#Job` / `#Enquire`。
- 你要確認房間提示是否真的對應到可執行功能。

## 搭配閱讀
- `references/room-file-layout.md`
- `references/room-flags-and-sectors.md`
- `document/room.txt`
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
- 若入口本質上仍是「一個出口 / 門 / 暗門」，優先先想 `#Exit` 能不能表達，不要下意識直接升級成 `#Job`。
- `document/room.txt` 對 `#Exit` 的 legacy contract 很有用：
  - `ExitKeyword` 是門的名字，像 `unlock gate`
  - `ExitDesc` 是玩家 `look <方向>` 時看到的描述
  - `IsDoor / Closed / Locked / Pick` 是出口狀態，不只是裝飾 metadata

### 可疑入口先用出口語意

- `area/loyang/roo/522.roo` 是好範例：房間描述先露出 `east_wall`，`#Keyword east_wall` 告訴玩家那面牆看起來像門；真正的通路仍由既有 `EAST` exit 承接。
  - 這種模式適合：
    - 可疑牆面
    - 暗門
    - 石板下的入口
    - 看起來不像一般路的通道
- 若 room 的互動其實只是「找到入口」或「理解這裡其實有路」，優先考慮：
  - 在房間描述露出可疑物件
  - 用 `#Keyword` 補一句「這裡像門 / 入口 / 通道」
  - 再用 `#Exit` / `ExitKeyword` / `IsDoor` / `Closed` 承接實際進出
- 只有當出口語意不夠，必須做特殊動作、瞬移、條件判斷或特效時，再升級到 `#Job`。
- 這也代表 keyword 要和玩家當下真的看得到的東西對齊；像 `522.roo` 的玩家看到的是牆，所以 keyword 是 `east_wall`，不是先把牆後面的秘密空間名直接塞到前一個房間。

### 兩段式入口鏈

- 若探索是分成「前置 clue 房」與「真正入口房」，每一房的 keyword 都要只對應該房間眼前可見的物件。
- `7507 -> 7511` 是 canonical 例子：
  - `7507` 只露出 `草痕`、`枯草`，不先把 `石板`、`井梯`、`井沿` 塞進來。
  - `7507` 的 `SOUTH` 若要有探索感，就不要保持明顯開放；可用 `ExitKeyword 枯草` + `IsDoor` + `Closed`，讓 `open 枯草` 真正承接進下一房。
  - `7511` 才露出 `石板`、`井梯` 與暗井本體，並用 `ExitKeyword 石板` + `IsDoor` + `Closed` 承接 `DOWN`。
- 判斷規則很簡單：如果 `south/down` 仍是玩家一進房就能直接走的明顯出口，而 `#Keyword` 只是在重述這條路，通常表示 keyword 沒有真正參與探索。
- 這種情況通常有兩個修正方向：
  - keyword 是冗餘描述，就刪掉它。
  - keyword 應該是探索節點，就把出口改成 door schema，讓 keyword 成為玩家前進前的必要觀察或操作。

## `#Keyword`

讓玩家可 `look <keyword>` 看到額外描述。

它只提供額外檢視內容，不會自動產生命令或行為。

### 描述先提示 keyword

- 不要把關鍵互動藏在玩家看不見的 noun 上。
- 若希望玩家 `look <keyword>`，房間描述裡應先出現那個詞，或至少出現會自然讓人試那個詞的明確名詞。
- 教學型房間可以直接寫明指令。
  例如 `area/new/roo/452.roo` 先寫出 `告示牌 (sign)`，再直接提示 `look sign`。
- 導覽 / 教學型房間若要玩家明確注意某個操作點，可以直接 highlight。
  例如 `area/loyang/roo/501.roo` 用 ANSI 顏色把 `new` / `fight` 變成一眼可見的操作提示。
- 探索 / 機關型房間至少要把物件名字露出來。
  例如 `area/newfight/roo/1211.roo` 先在房間描述寫出裂縫 `hole`，玩家 `look hole` 後才會看到 `bore` 的下一步提示。
- 英文 keyword 混在中文敘述裡時，通常已自帶辨識度；像 `hole` 這種 token，不一定要再額外上色。
- 中文 keyword 若混在中文房間敘述裡，玩家較不容易立刻辨識成可互動詞；若它屬於新手主線、必要路徑、問路骨架或核心教學，預設用小括弧、顏色或直接寫出 `look <keyword>` 來額外 highlight。
- spec-first area 若靠 `#Keyword` 才能讓玩家看懂路線、入口或可疑物件，先把那個 noun 寫進房間描述，再讓 `#Keyword` 補細節；不要只在 extra description 裡第一次出現它。
- 完全隱性的 keyword 預設只留給 puzzle、secret、支線捷徑或彩蛋；不要把新手必經路線做成必須先猜中文 keyword 才能前進。
- 若 keyword 要承接必要探索，描述裡除了 noun 之外，也要盡量暗示可執行的下一步；例如 `open 石板`、`open 枯草` 這種 repo 內建 door 操作，可以直接寫進 keyword 描述。

### ANSI 顏色寫法

- repo 目前 area data 慣例直接寫 raw ANSI escape sequence；`area/loyang/roo/501.roo` 的 `[1;32mnew[0m`、`[1;33mfight[0m` 就是 canonical 例子。
- 常用組合可直接照抄：
  - `[1;32m` = 亮綠
  - `[1;33m` = 亮黃
  - `[1;36m` = 亮青
  - `[0m` = 還原
- 若要查 repo 既有「色名 <-> token <-> ANSI」對照，先看 `command/t/title.ins`，再以 `src/ansi.c` 的 `ansi_token` / `ansi_info` 為實作準據。
- `title.ins` 裡那套 token 可當顏色選擇的 canonical 名稱：
  - `$HIG$` = `[1;32m`
  - `$HIY$` = `[1;33m`
  - `$HIC$` = `[1;36m`
  - `$NOR$` = `[0m`
- 在 `.roo` / `.obj` / `.mob` 這類 flat runtime file 中，可直接寫：
  `輸入 [1;32mnew[0m 可以到達新手訓練區`
- 在 `map.md` 的 `mapmd-json` JSON string 內，不能直接塞原始 ESC；要寫成：
  `"description": "輸入 \\u001b[1;32mnew\\u001b[0m 可以到達新手訓練區"`
- 不要只開色不收色；每段 highlight 後預設補 `[0m`，避免把後面整行或整段都染色。
- area data 目前幾乎都直接用 raw ANSI，而不是 `$HIG$` / `$HIY$` / `$NOR$` token；`title.ins` / `command/*.ins` 比較像 token 用法的 canonical 參考。除非你在改已明確使用 token 的程式輸出、title/chat/custom string 邏輯，否則 area authoring 預設跟 `501.roo` 一樣寫 raw ANSI。
- 玩家可用 `config +ansi` / `config -ansi` 控制彩色輸出，因此顏色是輔助，不要讓顏色成為唯一線索；必要關鍵字仍應靠括號、詞形或句意可辨識。

## `#Job`

把房間內某個 keyword 對到 `src/job.c` 已註冊的 function。

若房間文案暗示某個動作可用，但玩家實際不能做，常見原因是：

- 沒有對應 `do_*`
- 沒有 `#Job`
- `job.c` 裡沒有對應 function

### 描述也要提示動作

- `#Job` 不是自動發現機制；玩家仍要先想到要做什麼。
- 若 room job 依賴特殊動詞，房間描述或 `#Keyword` 描述裡要把動作也講出來。
- `document/room.txt` 也明寫 `#Job` 的 `Function` 必須是 `job.c` 已定義的函數；如果只是門/出口語意，先不要為了互動感硬開新 job。
- `area/newfight/roo/1211.roo` 的寫法是好模板：
  先讓玩家看到 `hole`，再在 `look hole` 的描述裡明講要 `鑽(bore)` 過去。
- 若同一件事其實可以用 `#Exit` / door schema 表達，優先用 `522.roo` 那種 clue + exit 的輕量模式，不要把每個秘密入口都做成 room job。
- 若互動是新手主線或必要路徑，允許在房間描述中直接點指令；若 keyword 是中文，必要時也可用顏色或括號先把詞打亮。若是探索型支線，至少要讓文字自然暗示動作與目標物的組合。

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
- 但「互動入口」不只 `#Job`；很多探索房其實是 `#Keyword` 提示 + `#Exit` / 門語意在承接。
- 但對玩家體感來說，真正的入口通常是房間描述先把 keyword 或動詞講出來。
