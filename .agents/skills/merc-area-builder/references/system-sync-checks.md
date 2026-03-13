# System Sync Checks

這份參考檔集中處理 area 改動時容易牽動的系統設定與 docs 對照點。

## 系統設定

只要牽涉出生點、recall、新手流程、戰鬥傳送或固定服務點，就要一起檢查：

- `etc/merc.ini`
- `src/merc.ini`
- `src/variable.c`
- `src/job.c`
- `data/bounty.txt`
- `data/bus.txt`
- `data/ship.txt`
- `help/` 內玩家可見提示

## 地圖交通

- 若區域涉及驛站、渡口、碼頭、首都入口或新手導流，補看 `docs/3yWebsite/docs/maps.md`
- `maps.md` 明確把地圖視為 `Serial/Capital` 之間的動線來源；若你新增或改寫交通節點，除了 area 檔本身，也要同步核對 `data/bus.txt`、`data/ship.txt`、相關 NPC / `res` 與 help 提示
- 若 docs 或 `maps.json` 提到票價、站名、推薦等級或主節點用途，區域內的房間描述、告示、交通 NPC 與 `area` 指令導引也要保持同一套說法

## 新手流程

- 若區域涉及新手教學、出生後第一輪探索或練功導流，補看 `docs/3yWebsite/docs/newbie.md`
- `newbie.md` 也反映歷史攻略中依賴的服務 NPC 與互動，例如學習、修裝、補給、救濟金、轉職、官職/國家導引
- `newbie.md` 與歷史攻略若提到像 `bore hole`、特定房間關鍵字、地圖捷徑或任務互動詞，也要把它們當成新手導流的一部分

## 技能來源

- 若區域涉及技能教師、秘笈掉落、訓練場、職業試煉、法器或技能型獎勵，補看 `docs/3yWebsite/docs/skills.md`
- `skills.md` 也提供「可教導 / 僅領悟 / 秘笈 study / 任務獎勵」這類來源線索；若你移動技能來源，除了 `mob/obj/res/shp`，也要同步檢查 help、任務提示、掉落敘述與相關主城服務 NPC

## 國家系統

- 若區域涉及國家首都、國界、官署、建國/入國導引、國家公告板或國家專屬服務，補看 `docs/3yWebsite/docs/realm.md`
- `realm.md` 也反映 `realm !join`、`!leave`、`!quit`、`!news`、`!read`、`!help`、`!attribution` 這些流程依賴的場景

## 世界觀與官方敘事

- 若區域涉及世界觀敘事、官方公告脈絡、元老/神族 NPC、授權文字或系統級 help/credit 提示，補看 `docs/3yWebsite/docs/system.md`
- `system.md` 也整理公告時間線、Immortal 名冊與版權要求；若你新增官方風格 NPC、歷史事件、傳送試煉、系統公告或公開版說明，要一起檢查 `help fju`、`credit`、相關 help 文案與遊戲內用語
