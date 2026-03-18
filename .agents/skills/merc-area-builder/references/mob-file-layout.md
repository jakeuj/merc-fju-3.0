# Mob File Layout

在 area 工作需要新增、閱讀或搬修 `mob/*.mob` 檔時，先用這份檔快速建立整體結構感；欄位細節再分流到其他 mob references。

## Source Order

- legacy 格式說明：`document/mob.txt`
- current loader reality：`src/load.c`
- repo 內已成功載入的 `area/*/mob/*.mob`

若三者有差異，先以 loader 與已成功載入範例為準，再回寫 skill / docs。

## File Location And Naming

- 檔案位置：`area/<area>/mob/*.mob`
- legacy 文件建議檔名直接跟怪物號碼走，方便尋找與除錯
- 一個檔案通常只定義一個怪物

## Canonical Skeleton

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
<mob flag>     Yes
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
Class          <number or constant>
Gold           <number>
Multipile      <number>
Sex            <number or constant>
Reborn         <number>
Rebornroom     <number>
Tractable      <number>
Migrate        <number>
AttackRatio    <number>
DodgeRatio     <number>
Speak          <number or constant>
Enable         <number> '<skill>'
AutoEnable     '<skill>'
Special        <string>
Auction
<multiline text>
~

#Learn
Adept          <number>
Cost           <number>
Inventory      <number>
Name           <string>
End

#Job
Keyword        <string>~
Function       <string>~
Position       <number or constant>
End

Program
Process
Type           <string>
Chance         <number>
Argument       <string>~
Gold           <number>
Text
<program text>
~
End

End
```

## Structural Notes

- `*` 開頭行是註解，legacy 文件視為不讀入。
- 大多數字串欄位用 `~` 結尾；`Description`、`Deadmsg`、`Auction`、`Text` 都是多行字串。
- `Deadmsg` 依 legacy 文件建議可在第一個字元放 `.`，避免讀檔時前導空白被吃掉。
- `Program` 是程式容器，實際一筆一筆的程式區塊是 `Process ... End`。
- `#Learn`、`#Job`、`Program` 都是選用區塊；需要時才放。
- 整個檔案最後要有一個總結束 `End`。

## Minimum Practical Read Path

- 要查 `Name`、`Level`、`Enable`、`AutoEnable`、`Special`、`Reborn` 這些主欄位，讀 `mob-core-fields.md`
- 要查 `#Learn`、`#Job`、`Process`、`spec_*` 類互動行為，讀 `mob-teaching-and-programs.md`
- 要查 Act / Effect / Sex / Class / Position 常數，讀 `mob-flags-and-constants.md`

## Repo-Specific Reminders

- `Name` 缺失會直接對應到 `Load_mobiles﹕怪物 %d 沒有名字。`
- `Level <= 0` 或 `Level > 120` 會直接對應到 `Load_mobiles﹕怪物 %d 等級 %d 不合理。`
- `document/mob.txt` 把 `100` 視為平衡上的傳統上限；即使 loader 可接受到 `120`，world-map-area-rebuild 的新 area 仍應把 `100` 當交付上限
