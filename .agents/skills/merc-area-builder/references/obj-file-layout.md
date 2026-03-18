# Object File Layout

## 何時讀這份
- 你正在建立或修補 `area/<area>/obj/*.obj`。
- 你需要最小可載入骨架、區塊順序、`End` / `~` 的收尾方式。

## 搭配閱讀
- `references/obj-core-fields.md`
- `references/obj-types-and-values.md`
- `references/obj-affects-restricts-and-jobs.md`
- `docs/current-game/object-file-format.md`

## 檔案位置

```text
area/<area>/obj/*.obj
```

每個 `.obj` 檔通常只定義一個物品。

## 最小骨架

```text
#OBJECT
Vnum            <number>
Name            <string>~
ShortDesc       <string>~
Description
<multiline text>
~
Unit            <string>~
ItemType        <number or symbol>
WearLoc         <number or symbol>
Level           <number>
Value           <values...>
Weight          <number>
Cost            <number>
Exp             <number>
Armor           <number>
Disappear       <number or symbol>

End
```

視需求再加入：

- `LongDesc`
- extra / wear / item flags 的 `Yes` 行
- `#Affect`
- `#Extra`
- `#Job`
- `#Restrict`
- `#Message`

## 字串與結束規則

- 單行字串通常以 `~` 結尾。
- 多行 `Description` 從下一行開始，到單獨一行 `~` 結束。
- block 類段落如 `#Affect`、`#Extra`、`#Job`、`#Restrict`、`#Message` 以各自的 `End` 結束。
- 整個物品檔最後也要有最外層 `End`。

## 先看哪一層文件

預設順序：

1. `docs/current-game/object-file-format.md`
2. 本 skill 的 object split references
3. `document/obj.txt`
4. repo 內已成功載入的同類型 `.obj`

不要每次都直接整份 `document/obj.txt` 從頭讀到底。

## 常見結構誤判

- area `obj/*.obj` 不是角色存檔或 runtime object serialization。
- 不要把 save/runtime 風格欄位名直接搬進 area source。
- 若不知道某個 `Value*` 怎麼解，先依 `ItemType` 找 working example，再回看 legacy 文件。

## Repo-specific guardrail

- 目前 loader 行為以 `src/load.c` 為準；若文件與 loader 不一致，以 loader 和已成功載入的 repo 範例為準。
- `Load_object﹕物品 %d 沒有名字。` 通常是 `Name` 缺失或結束符錯位。
- `Load_object﹕物品等級 %d 錯誤。` 代表 `Level` 超出目前 loader 可接受範圍；設計上仍以一般帶 `1..100` 為主，`101..120` 只留給明確規劃過的 endgame 特例。
