# Reset Runtime Guardrails

## 何時讀這份
- 你要把 legacy `document/reset.txt` 和 current loader 行為對齊。
- 你碰到 reset parser 問題，或在懷疑 `S`、EOF、door state、shop inventory 等 repo-specific 差異。

## 搭配閱讀
- `references/reset-file-layout.md`
- `docs/current-game/reset-file-format.md`
- `src/load.c`

## 最大差異：結束規則

legacy 文件把 `S` 當 reset 結束行，但 current repo 應以 loader 行為為準。

目前 repo 的 `src/load.c` `load_resets()` 是讀到 EOF，不是靠 literal `S` 收尾。

因此在今天的 repo：

- 檔案直接以 EOF 結束
- 不要為了對齊 legacy 手冊再放 literal `S`

## 為什麼這很重要

如果把 `S` 當一般文字行放進 `.res`，它可能不是 harmless terminator，而是 parser 風險來源。

## Loader-aware 檢查順序

1. 先看 `.res` 的參照 vnum 是否存在
2. 再看 `mob / obj / roo / shp` 是否真的已被 area 載入
3. 再看 reset 行順序是否合理
4. 最後才懷疑純語法

## 和其他檔種的耦合

- `mob/*.mob`：`M`、`G`、`E`、`A`
- `obj/*.obj`：`O`、`P`、`G`、`E`
- `roo/*.roo`：`M`、`O`、`D`、`R`
- `shp/*.shp`：商店會賣什麼常常仰賴 `.res` 給店長的物品

## Repo-specific guardrail

- reset 檔不要混回 upstream `.are` 心智模型裡的 section terminator 想像。
- 若 area 啟動後商店、掉落、裝備、門狀態看起來怪，先查 `.res` 和它參照的其他檔，不要直接懷疑 command code。
