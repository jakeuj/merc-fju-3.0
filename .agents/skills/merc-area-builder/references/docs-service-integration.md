# Docs Service Integration

這份參考檔集中說明何時要串接 `sango-docs-service` 與 `docs/3yWebsite`。

`docs/3yWebsite/` 在目前 repo 內預設視為 reference-only 的舊站鏡像；若任務有新增目前 repo 真正會載入的新技能、NPC 戰技或其他現行資料，應把正式補充紀錄寫到 repo 自有路徑，例如 `docs/current-game/skills.md` / `docs/current-game/skills.json`，不要直接把舊站快照改成現行技能台帳。

## 何時一起用 `sango-docs-service`

遇到下列情境時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起用：

- 要替區域補世界觀、歷史事件、國家勢力或角色背景
- 要確認技能描述、掉落來源、NPC 對應或玩家指南
- 要比對地圖交通、巴士站、下載資料或公告時間線
- 要確認新手教學節奏、常用指令導引、規則告示或玩家常見卡點
- 要確認技能命名、熟練度詞彙、資源消耗、秘笈 / study 流程或職業技能來源
- 要確認國家指令流程、官職/權限、首都房間功能、入國/叛國導流或國家公告板
- 要確認故事時間線、系統公告、Immortal/官方 NPC 映射、版權提示或公開版用語

## 優先資料來源

- 主題總覽：`docs/3yWebsite/docs/index.md`
- 世界與公告：`docs/3yWebsite/docs/system.md`
- 新手/規則/玩家心得：`docs/3yWebsite/docs/newbie.md`
- 技能：`docs/3yWebsite/docs/skills.md` 與 `docs/3yWebsite/docs/data/skills.json`
- 國家系統：`docs/3yWebsite/docs/realm.md` 與 `docs/3yWebsite/docs/data/realm_commands.json`
- 地圖交通：`docs/3yWebsite/docs/maps.md` 與 `docs/3yWebsite/docs/data/maps.json`
- 下載與手冊：`docs/3yWebsite/docs/download.md` 與 `docs/3yWebsite/docs/data/downloads.json`

## 回報要求

- 回答或規劃時，清楚標示資料來自哪個 docs 檔或 JSON
- 說明它會影響區域建置流程的哪一步
- `maps.md` / `maps.json` 可直接用來核對主城與區域節點命名、巴士/船運站點、價格、推薦等級提示與地圖導流
- `newbie.md` 可直接用來核對新手區的教學順序、服務 NPC、常用指令提示、規則告示與升級導流
- `skills.md` / `skills.json` 可直接用來核對舊版技能中文/英文名稱、來源類型、熟練度詞彙、資源消耗與 study 相關物件；若本輪新增的是目前 repo 的新技能，另查 `docs/current-game/skills.md`、`docs/current-game/skills.json` 與 runtime 檔案
- `realm.md` / `realm_commands.json` 可直接用來核對 Capital 房間、國家公告板、銀行門檻、官職權限、入國/離境/叛國流程與國家專屬服務
- `system.md` / `news.json` / `immortals.json` 可直接用來核對故事時間線、公告順序、Immortal 稱謂、官方 NPC 風格、`help fju` / `credit` 提示與公開版相關文案
