# Mob Teaching And Programs

用於查 `mob/*.mob` 裡的 `#Learn`、`#Job`、`Program / Process`，以及和 `Special` 類行為的分工。

## Table Of Contents

- `#Learn`
- `#Job`
- `Program / Process`
- `Special` vs `Process`
- Repo Guardrails

## `#Learn`

`#Learn` 用來讓 NPC 具備教學能力。legacy 文件明講：只要出現 `#Learn`，其內各欄位就都應存在，最後以 `End` 結束。

### Canonical Shape

```text
#Learn
Adept          <number>
Cost           <number>
Inventory      <number>
Name           <skill name>
End
```

### Fields

- `Adept`
  - 老師對該技能的熟練度。
  - legacy 文件建議範圍 `1..100`。
- `Cost`
  - 教學費用。
  - legacy 文件提醒：失敗也會收費，而且不建議設太低。
- `Inventory`
  - 技能隱藏度。
  - 數值越高，玩家越不容易從查詢中看出這個老師會教該技能。
- `Name`
  - 教學技能名稱。
  - legacy 文件提醒不要把未開放技能塞進來。

## `#Job`

`#Job` 是把怪物上的特殊觸發綁到 `job.c` 內既有 function 的方式。

### Canonical Shape

```text
#Job
Keyword        <string>~
Function       <string>~
Position       <number or constant>
End
```

### Fields

- `Keyword`
  - 觸發特殊動作時比對的關鍵字。
- `Function`
  - 真正執行的函數名稱，必須在 `job.c` 內有定義。
- `Position`
  - 觸發所需最低狀態。
  - legacy 文件列出 `POS_DEAD / POS_SLEEPING / POS_RESTING / POS_FIGHTING / POS_STANDING`。

### Authoring Intent

- 若 NPC 的互動比較像「輸入特定關鍵字後跑固定功能」，優先想 `#Job`。
- 這和 room 的 `#Job` 是同一類概念，只是掛在 mob 身上。

## `Program / Process`

legacy 文件把新格式怪物程式包在 `Program` 容器下，實際一段一段的是 `Process`。

### Canonical Shape

```text
Program
Process
Type           <prog type>
Chance         <number>
Argument       <string>~
Gold           <number>
Text
<commands>
~
End
```

### Trigger Data

- `Type`
  - 程式觸發型態。
- `Chance`
  - 大多數 trigger 用機率。
- `Argument`
  - `speech_prog`、`give_prog`、`act_prog` 類型會用到參數。
- `Gold`
  - `bribe_prog` 類型會用金額。
- `Text`
  - 真正執行的程式本文，多行字串，以 `~` 結尾。

### Legacy Trigger Types

- `act_prog`
- `speech_prog`
- `rand_prog`
- `fight_prog`
- `death_prog`
- `hitprcnt_prog`
- `greet_prog`
- `give_prog`
- `bribe_prog`
- `entry_prog` / `all_greet_prog` / `in_file_prog` / `error_prog`
  - legacy 文件明講其中幾種不要用；實作前仍優先比對 repo 內成功樣本

### Helper Commands Mentioned In `mob.txt`

- `mpasound`
- `mpjunk`
- `mppurge`
- `mpechoat`
- `mpechoaround`
- `mpkill`
- `mpmload`
- `mpoload`
- `mpgoto`
- `mpat`
- `mptransfer`
- `mpforce`

### Example Predicates Mentioned In `mob.txt`

- `rand`
- `ispc`
- `isnpc`
- `isgood`
- `isfight`
- `isimmort`
- `ischarmed`
- `isfollow`
- `isaffected`
- `hitprcnt`
- `inroom`
- `sex`
- `position`
- `level`
- `class`
- `name`
- `goldsmt`
- `objtype`
- `objval0..objval3`
- `number`

## `Special` vs `Process`

- `Special`
  - 指向程式碼裡的 `spec_*` 函數
  - 適合固定、可重用、偏系統級的 NPC 行為
- `Process`
  - 是資料驅動的怪物程式
  - 適合對話、條件判斷、事件觸發、謎題流程

可先這樣判斷：

- 行為已經是 repo 內穩定共用能力，用 `Special`
- 行為是單區敘事或事件邏輯，用 `Process`
- 行為看起來像「玩家對怪輸入某關鍵字就呼叫已註冊函數」，用 `#Job`

## Repo Guardrails

- `#Learn`
  - 技能名稱必須和 repo 內實際存在、可教學的技能對得上。
  - 若同輪還改到 skill runtime data，驗證要求要提高，不要把它當純 area 文案。
- `#Job`
  - `Function` 一定要先對 `src/job.c`，不要只看 legacy 文件想像函數名。
- `Process`
  - 先對 `doc/mobprogram-guide.txt` 與 repo 內成功樣本，不要只照 `mob.txt` 的舊範例擴寫。
  - 若程式流程依賴 quest mark、teacher 狀態或特殊 world service，記得回寫單區 plan / tracker。
- `Special`
  - 要先確認函數真的存在於 `special.c` 或 loader 實際註冊的清單中。
