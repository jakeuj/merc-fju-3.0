---
layout: default
title: Mobile File Format
---

# `.mob` 怪物檔格式說明

這頁把 `document/mob.txt` 整理成 GitHub Pages 可直接閱讀的版本，方便做 area / NPC data work 時快速定位欄位。

## Source Of Truth

- legacy 文件來源：`document/mob.txt`
- 現行 loader 與常數以這些檔案為準：
  - `src/load.c`
  - `src/merc.h`
  - `data/symbol.def`
  - repo 內已成功載入的 `area/*/mob/*.mob`

## 檔案位置

```text
area/<area>/mob/*.mob
```

每個 `.mob` 檔通常代表一個怪物定義。

## 基本格式

```text
Vnum           <number>
Name           <string>~
ShortDesc      <string>~
Description
<multiline text>
~
Deadmsg
<multiline text>
~
<mob flags>    Yes
Effect         '<string>'
Alignment      <number>
Level          <number>
Hitroll        <number>
Protect        <number>
Damroll        <number>
Str            <number>
Int            <number>
Wis            <number>
Dex            <number>
Con            <number>
Hp             <number>
Mana           <number>
Move           <number>
Class          <number or symbol>
Gold           <number>
Multipile      <number>
Sex            <number or symbol>
Reborn         <number>
Rebornroom     <number>
Tractable      <number>
Migrate        <number>
AttackRatio    <number>
DodgeRatio     <number>
Speak          <number or symbol>
Enable         <number> '<skill>'
AutoEnable     '<skill>'
Special        <string>
Auction
<string>~

#Learn
...
End

#Job
...
End

Program
Process
...
End

End
```

## 最常用主欄位

| 欄位 | 用途 |
| --- | --- |
| `Vnum` | 怪物虛擬號碼 |
| `Name` | 必填；最短 command-facing 英文關鍵名 |
| `ShortDesc` | 中文短描述 |
| `Description` | `look` 時看到的怪物描述 |
| `Deadmsg` | 死亡訊息 |
| `Alignment` | 陣營值 |
| `Level` | 怪物等級；legacy 文件建議 `<=100`，current loader 接受 `1..120` |
| `Class` | 職業常數 |
| `Sex` | 性別常數 |
| `Hp` / `Mana` / `Move` | 基礎資源 |
| `Hitroll` / `Damroll` / `Protect` | 命中、傷害、防護 |
| `Enable` / `AutoEnable` | 戰鬥技能與自動技能 |
| `Special` | 對應 `spec_*` 特殊函式 |

## `Name` 與 `Level` 的現行寫法

### `Name`

- `document/mob.txt` 明講 `Name` 不能省略；目前 `src/load.c` 的 `load_mobiles()` 也會在缺欄位時報 `Load_mobiles﹕怪物 %d 沒有名字。`
- 這個欄位不是單純的展示文字，而是程式與玩家指令拿來比對的最短關鍵名字
- 實務上請維持英文或至少 ASCII-friendly token，例如 `guard`、`rift watcher` 這類可被玩家穩定輸入的名字
- 中文顯示名請放在 `ShortDesc` / `Description`；不要把 `Name` 寫成純中文，否則雖然未必立刻 load fail，但會讓玩家操作與除錯都變差

### `Level`

- legacy `document/mob.txt` 把 `100` 視為傳統平衡上限，重點是避免升級曲線某一段突然斷層
- 目前 repo 的 `src/load.c` 會把 `<= 0` 或 `> 120` 的怪物等級判成不合理，因此 runtime hard gate 是 `1..120`
- 這代表目前要分成兩層理解：
  - 一般設計 / 平衡基線：優先維持在 `1..100`
  - loader 可接受的例外上限：`101..120`
- 本 repo 現有後段高階裂魄鏈已經刻意使用 `101..120` 區間，所以不要把 `>100` 一律視為錯誤；但也不要因為 loader 接受 `120`，就把每個新 area 都往上推到三位數
- 最安全的寫法是：若某區需要 `101..120`，在單區 plan、tracker 或 area `index` 明講它是 late-game / endgame 例外，並配合 smoke test 證明沒有踩到 loader 上限

## 怪物旗標

`document/mob.txt` 列出一批可用旗標，例如：

- `Sentinel`
- `Scavenger`
- `Aggressive`
- `StayArea`
- `Wimpy`
- `Train`
- `Rebirth`
- `Ask`
- `NoReborn`
- `NoKill`
- `Enroll`
- `AlignGood`
- `AlignEvil`
- `NoSummon`

這些旗標可以組合，但仍要和目前 repo 的實際範例比對。

## 技能相關欄位

### `Enable`

格式像：

```text
Enable        100 'long fist'
```

表示怪物會以某個機率或權重啟用對應技能。

### `AutoEnable`

用來設定自動啟動的技能名稱。

### `#Learn`

讓 NPC 具備教學能力，常見欄位：

- `Adept`
- `Cost`
- `Inventory`
- `Name`

這和師父 NPC、訓練流程高度相關。

## 互動與腳本

### `#Job`

讓怪物支援以 `Keyword` 觸發 `job.c` 內的功能。

### `Program / Process`

這是怪物程式區塊，文件範例出現：

- `fight_prog`
- `speech_prog`

常見欄位有：

- `Type`
- `Chance`
- `Argument`
- `Gold`
- `Text`

## 目前最值得注意的實務點

- `Name` 是必填、command-facing 的最短關鍵字；對玩家與 loader 來說都不是可有可無的展示欄位。
- 不要只照 `document/mob.txt` 猜 `Class`、`Effect` 或技能名稱，先比對 repo 內已成功載入的怪物範例。
- `Level > 120` 會直接變成 loader blocker；`101..120` 雖可載入，但應視為經過規劃的高階例外帶，而不是預設值。
- 若 `.mob` 內用了 `Enable` / `AutoEnable` 指到技能，驗證要求要比一般資料檔更高。
- 若新增可教學 NPC，要同步檢查技能是否真的存在、能否 `Teach`、是否有對應文件。

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/mob.txt`
- `src/load.c`
- `src/merc.h`
- `data/symbol.def`
- repo 內既有 `area/*/mob/*.mob`
