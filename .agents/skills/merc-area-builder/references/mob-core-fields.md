# Mob Core Fields

用於查 `mob/*.mob` 的主欄位語意、legacy 寫法與 repo-specific guardrails。旗標 / 常數另讀 `mob-flags-and-constants.md`；`#Learn/#Job/Process` 另讀 `mob-teaching-and-programs.md`。

## Table Of Contents

- Identity And Display
- Combat And Balance
- Role And Lifecycle
- Skills And Automation
- Repo Guardrails

## Identity And Display

### (1) `Vnum`

- 怪物虛擬號碼，不能省略。
- legacy 文件要求是數字，且不小於 `0`。
- 依 legacy 習慣，和該區 room / obj 號碼保持可對照會比較好維護。
- 怪物彼此之間不能重號，但可和房間或物品號碼重複。

### (2) `Name`

- 怪物的英文名字，也是最短名字。
- legacy 文件明講：程式判斷時會比對這個名字，所有動作都和它有關。
- 這個欄位不能忽略，字串用 `~` 結束。
- legacy 文件強烈建議它最好是英文，否則會造成玩家不便。

### (3) `ShortDesc`

- 怪物中文名字。
- 玩家對怪物做動作時，通常看到的是這個顯示名。
- legacy 文件說系統會自動把英文名字加上去，因此這裡通常只寫中文顯示名即可。

### (4) `Description`

- 玩家 `look` 怪物時看到的描述。
- 可用來補敘事、辨識外觀、丟提示或埋謎題。
- 多行字串，以單獨一行 `~` 結尾。

### (6) `Deadmsg`

- 怪物死亡時給世界玩家看的哀嚎或收尾訊息。
- legacy 文件建議在第一個字元放 `.`，避免前導空白被讀檔吃掉。
- 若只是一般雜兵，可保持簡短；若是 named NPC 或 boss，可把世界觀味道放進來。

## Combat And Balance

### (8) `Alignment`

- 怪物陣營值，legacy 範圍是 `-1000..1000`。
- `> 300` 視為善良，`< -300` 視為邪惡，中間是中立。
- 會影響和抗善良 / 抗邪惡裝備或世界觀設定的相容性。

### (9) `Level`

- 怪物等級，直接影響強度與經驗取得。
- legacy 文件把 `100` 視為當時的最大等級，重點是不要讓升級曲線某一段突然失衡。
- current loader 的 hard gate 是 `1..120`；超出會直接被判成不合理。

### (10) `Hitroll`

- 額外命中率修正，legacy 文件以 `0` 為基準。
- 命中率會進一步影響殺傷力。

### (11) `Protect`

- 防護度。
- 若使用 `AUTOSET_VALUE`，這欄可由系統依等級自動給值。
- 想讓系統自動決定時，可填 `-1`。

### (13) `Damroll`

- 傷害力修正。
- 若使用 `AUTOSET_VALUE`，這欄同樣可讓系統自動給值；legacy 文件建議填 `-1` 交給系統。

### (14) `Str Int Wis Dex Con`

- 怪物五圍。
- 使用 `AUTOSET_VALUE` 時，可由系統依等級自動分配。
- legacy 文件提醒：自己手填時不要和等級預期差太遠。

### (15) `Hp Mana Move`

- 基礎生命、法力、體力。
- 使用 `AUTOSET_VALUE` 時，也可依等級自動給值。
- legacy 文件特別提醒體力太低會讓怪物很容易被吸乾，導致實戰偏弱。

### (17) `Gold`

- 殺死怪物會掉的金錢。
- legacy 文件建議保守處理，避免通膨。
- 使用 `AUTOSET_VALUE` 或填 `-1` 時，可交給系統決定。

### (18) `Multipile`

- 怪物經驗值加成，legacy 文件說它是百分比倍率。
- 拼字就是 `Multipile`，不要自作主張改成 `Multiple` 或 `Multiplier`。
- legacy 文件提醒：怪物經驗原本就強烈依賴等級，這欄只是在此之上做百分比微調。

### (19) `Sex`

- 怪物性別，通常用 `SEX_NEUTRAL`、`SEX_MALE`、`SEX_FEMALE`。
- 雖然 legacy 文件說影響不大，仍建議和敘事一致。

### `Speak`

- `Speak` 出現在 legacy 語法段，但 `document/mob.txt` 後半沒有替它寫獨立說明章節。
- 遇到這個欄位時，不要只靠 `mob.txt` 猜語意；先對 repo 內成功載入範例與 loader 實際接受的值。
- 若本輪只是 area data work，最安全做法是沿用同類 NPC 的既有寫法，不要隨手發明新常數。

## Role And Lifecycle

### (16) `Class`

- 怪物職業。
- 對轉職 NPC、技能使用與師父類角色特別重要。
- legacy 文件列出固定職業常數；實作時仍要先對 repo 內成功載入範例。

### (20) `Reborn`

- 若怪物有 `RebornFight` 旗標，這裡指定死後要再讀出的怪物號碼。
- 指到的怪物必須存在。

### (21) `Rebornroom`

- 指定再生怪物出現的房間。
- 不填時通常在原地出現；有填時，該房間必須存在。

### (22) `Tractable`

- 馴服度，關係到能不能當坐騎。
- `<= 0` 視為不能騎；數值越高越容易騎上去。

### (25) `Migrate`

- 怪物遷移率，用百分比表示。
- legacy 文件說不能超過 `100`，預設為 `0`。
- 適合雲遊 NPC 或不固定刷點的遭遇。

### (26) `AttackRatio`

- 攻擊威力倍率，`100` 為基準。
- 主要加強怪物用技能時的攻擊輸出。

### (27) `DodgeRatio`

- 防禦威力倍率，`100` 為基準。
- 主要影響步法或防禦面的效果。

## Skills And Automation

### (23) `Enable`

- 指定怪物預設使用的技能，以及該技能熟練度。
- legacy 文件強調：不給技能的怪物只會空手打，容易比等級看起來弱很多。
- 填進去的技能必須是可致能的技能；法術類不一定能直接拿來 `Enable`。

### (24) `Special`

- 怪物特殊函式，實作在 `special.c`。
- 用來補足 mob program 難做或不適合寫成程式腳本的行為。
- legacy 文件舉 `spec_new_doctor` 為例，代表會幫同房玩家回復的醫生 NPC。

### (28) `AutoEnable`

- 當你不知道熟練度該填多少時，讓系統自動推算。
- legacy 文件把它定位成「先選對技能，再讓系統估熟練度」。
- 若技能不適合怪物，系統也可能警告你換技能。

### (29) `Auction`

- 針對會自動拍賣的怪物，設定拍賣前想說的話。
- 是多行字串欄位，使用方式和 `Description` / `Deadmsg` 類似。

## Repo Guardrails

- legacy 編號本身有缺口：文件從 `(11) Protect` 直接跳到 `(13) Damroll`，這是原文現象，不是這份 reference 漏欄。
- `Name`
  - 在 repo 內把它當成 command-facing keyword，而不是展示文字。
  - 預設維持英文或至少 ASCII-friendly token；中文顯示放 `ShortDesc` / `Description`。
  - 缺欄位時會直接對應到 `Load_mobiles﹕怪物 %d 沒有名字。`
- `Level`
  - 現在要分兩層理解：
    - legacy 平衡基線：`<= 100`
    - current loader hard gate：`1..120`
  - 對 world-map-area-rebuild 與新建 area 來說，實際 authoring cap 仍應維持 `<= 100`。
  - `>120` 會直接踩 loader blocker。
- `AUTOSET_VALUE`
  - 這是讓系統依等級自動回填部分數值的旗標。
  - legacy 文件把 `Protect`、`Damroll`、五圍、`Hp/Mana/Move`、`Gold` 等欄位填 `-1` 視為「單欄交給系統處理」的方式。
- `AutoEnable`
  - current repo 若自動推導出極端熟練度，會寫 `debug/failenable`。
  - 想穩定消除 loader warning 時，通常直接改成固定 `Enable` 比改攻閃係數更可控。
