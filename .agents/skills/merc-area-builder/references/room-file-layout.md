# Room File Layout

## 何時讀這份
- 你正在建立或修補 `area/<area>/roo/*.roo`。
- 你需要房間骨架、最小欄位、block 順序與收尾方式。

## 搭配閱讀
- `references/room-exits-and-interactions.md`
- `references/room-flags-and-sectors.md`
- `references/file-handling-rules.md`
- `docs/current-game/room-file-format.md`

## 檔案位置

```text
area/<area>/roo/*.roo
```

通常一個 `.roo` 檔代表一個房間。

## 最小骨架

```text
Vnum            <number>
Name            <string>~
Description
<multiline text>
~
SectorType      <number or symbol>

End
```

視需求加入：

- 房間旗標 `Yes` 行
- `#Exit`
- `#Keyword`
- `#Job`
- `#Enquire`

## 字串與結束規則

- `Name` 以 `~` 結尾。
- 多行 `Description` 從下一行開始，到單獨一行 `~` 結束。
- 每個 `#Exit` / `#Keyword` / `#Job` / `#Enquire` block 以各自的 `End` 收尾。
- 整個房間檔最後也要有最外層 `End`。

## 先看哪一層文件

預設順序：

1. `docs/current-game/room-file-format.md`
2. 本 skill 的 room split references
3. `document/room.txt`
4. repo 內已成功載入的同類型 `.roo`

## Repo-specific guardrail

- `.roo` 不只是四向平面地圖；現行 area work 需主動接受 `north / east / south / west / up / down / enter / out`。
- spec-first area 應把 `map.md + mapmd-json` 當設計源頭，`.roo` 是投影。
- `#Enquire` 是 today repo area work 的正式 room spec 部分，不要因為 legacy 文件篇幅較少就忽略。
