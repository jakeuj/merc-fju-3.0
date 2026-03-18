# Object Core Fields

## 何時讀這份
- 你已經知道 `.obj` 骨架，但要決定主欄位怎麼寫。
- 你在處理 `Vnum / Name / ShortDesc / Description / Level` 這些最常出錯的核心欄位。

## 搭配閱讀
- `references/obj-file-layout.md`
- `references/obj-types-and-values.md`
- `docs/current-game/object-file-format.md`

## 核心欄位

### `Vnum`
- 物品虛擬編號。
- area 內不可重複，且要和 reset、shop、mob 掉落或裝備關聯對得上。

### `Name`
- 最短、可被系統與玩家指令比對的關鍵名。
- 預設保留英文或至少 ASCII-friendly token。
- 中文顯示放在 `ShortDesc` / `Description`。

### `ShortDesc`
- 持有、裝備、商店等場景常看到的短描述。
- 慣例上可在中文描述裡帶上英文 keyword，方便玩家辨識。

### `LongDesc`
- legacy 文件有此欄位，但 today repo 任務裡常不是必需。
- 若 area 範例已普遍不用，就不要為了對齊手冊硬塞。

### `Description`
- 房間地面上看到的完整敘述。
- 多行文本從下一行開始，到 `~` 結束。

### `Unit`
- 物品單位，例如「把」「件」「本」。
- legacy 文件允許預設值思考，但現代 authoring 建議明寫。

### `Weight`
- 重量。
- 若你在複製範例，避免把裝備重量整批照抄到不合理的輕重帶。

### `Cost`
- 價值。
- 商店價格、經濟感受、掉落價值都會受影響。

### `Level`
- 物品等級。
- 平衡面預設仍以 `1..100` 為一般設計帶。
- current loader 的硬 gate 以 repo 現況為準；若要用 `101..120`，必須是刻意規劃過的 late-game / endgame 帶，且最好能在單區 plan 或 area metadata 說明理由。

### `Disappear`
- 丟棄後是否消失。
- 常數以 repo working examples 為準。

### `Armor`
- 主要給防具與部分防禦型物件使用。

### `Exp`
- 主要和武器、防具的成長或升級經驗有關。

## 兩個最常踩到的 parser 風險

### `Name`
- 缺失、錯誤 `~`、或把多個欄位串在一起時，loader 常直接報沒有名字。
- 確認 `Name` 這行本身完整，並且最短 token 仍可給玩家輸入。

### `Level`
- 不要只看 legacy 文件，也不要只看當前例外樣本。
- 寫超出 loader 可接受範圍時，啟動期會直接被 loader 擋下。

## Legacy 文件的小陷阱

`document/obj.txt` 的編號裡 `Value` 和 `Disappear` 都被標成 `(14)`；這是 legacy 文件排版問題，不是 today loader 真的把兩個欄位合成一個。

## Repo-specific guardrail

- 對主欄位有疑慮時，先比對 repo 內已成功載入的同類型 `.obj`，不要只靠單一手冊定義。
- 若 `Name` / `Level` 與設計意圖有 tradeoff，寧可把理由寫進 plan，也不要留下 loader 會擋的模糊值。
