# Area Index And Title

## 何時讀這份
- 你正在建立或修補 `area/<area>/index`。
- 你要決定 `Serial`、`Capital`、等級帶、area flags 或區域描述。

## 搭配閱讀
- `docs/current-game/title-file-format.md`
- `area/directory.lst`
- repo 內既有 `area/*/index`

## 檔案位置

```text
area/<area>/index
```

legacy 文件把它稱為「標題檔」，但 today repo area work 應把它視為 area metadata。

## 基本骨架

```text
Echo          <symbol or number>
Editor        <string>~
Name          <string>~
Flags         <symbol or number>
Upper         <symbol or number>
Lower         <symbol or number>
Fog           <number>
Serial        <number>
Capital       <number>
Description
<multiline text>
~

End
```

## 主要欄位

### `Serial`
- area 序號。
- 是 area 身分的一部分，不只是備註欄位。

### `Capital`
- 若非 `0`，會影響出生地 / recall 類行為的判定。
- 不是所有區都該填。

### `Name`
- 區域名稱。

### `Editor`
- 區域編輯者。

### `Description`
- area help 或補充敘述。

### `Upper` / `Lower`
- 建議等級帶。
- 若某區故意做高於一般帶的 endgame 內容，這裡也應與設計帶相呼應。

### `Flags`
- 區域級屬性，例如新手區或特殊環境條件。

## 和 `area/directory.lst` 的關係

- `index` 描述 area 自己是誰。
- `area/directory.lst` 決定載入順序與實際是否被世界讀到。

兩者都要同步。

## Repo-specific guardrail

- `src/load.c` 會對缺少 `Serial`、重複 `Serial` 等情況報錯。
- `Capital` 牽涉出生城語意，不要為了填欄位而填。
- 新增可載入 area 時，除了 `index`，還要一起檢查 `area/directory.lst` 與 `docs/current-game/areas.*` 是否需要同步。
