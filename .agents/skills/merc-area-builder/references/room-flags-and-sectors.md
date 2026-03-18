# Room Flags And Sectors

## 何時讀這份
- 你正在決定 `SectorType`、房間旗標、環境感與移動語意。
- 你不確定某個房間應該被視為城市、室內、山地、水域或特殊功能點。

## 搭配閱讀
- `references/room-file-layout.md`
- `references/room-exits-and-interactions.md`
- `docs/current-game/room-file-format.md`

## `SectorType`

legacy 文件列出的常見地形包含：

- `SECT_INSIDE`
- `SECT_CITY`
- `SECT_FIELD`
- `SECT_FOREST`
- `SECT_HILLS`
- `SECT_MOUNTAIN`
- `WATER_SWIM`
- `WATER_NOSWIM`
- `SECT_AIR`
- `SECT_DESERT`

地形不只影響文感，也常和移動成本、交通體驗、區域敘事節奏一起運作。

## 房間旗標

legacy 文件裡常見的旗標例如：

- `Dark`
- `NoMob`
- `Indoors`
- `Private`
- `Safe`
- `ForeverLight`
- `NoRecall`
- `DepositMoney`
- `StoreRoom`
- `NoFight`
- `NoQuit`
- `Club`
- `Memorize`
- `Stock`
- `NoWhere`
- `Sail`
- `Fane`
- `Killer`
- `Standard`

不要為了套常數而套常數；先問自己這個房間在玩法上想禁止、允許、強化什麼。

## 設計判斷

- 城市、交易、服務節點通常和 `Safe`、`DepositMoney`、`StoreRoom` 等玩法性旗標連動。
- 地下洞穴、秘境、軍事要地、野外水路的 `SectorType` 不應只靠描述文字決定，也要對齊玩法。
- 若區域主題是明確的一條語彙線，地形與旗標也應跟著維持一致，而不是房間文案一套、旗標另一套。

## Repo-specific guardrail

- 方向系統與地形判讀要和 `src/act_move.c` 一起理解，不要只照 legacy 常數表。
- spec-first 新區在選 `SectorType` 時，應讓 prose、`mapmd-json`、`.roo` 三層保持一致。
