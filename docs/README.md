# Docs Layout

- `docs/3yWebsite/` 是舊版遊戲介紹網站的鏡像與參考資料，供世界觀、命名、公告、地圖與歷史技能脈絡比對使用；預設不拿來登記目前 repo 新增或改寫後的正式 runtime 資料。
- `docs/current-game/` 用來記錄目前這個 repo 額外補上的開發者文件與機器可讀台帳，現行至少包含 skills 與 areas 兩組 registry；內容應明確標示它是對現行 `src/`、`skill/`、`area/`、`data/` 的補充說明，而不是舊站快照。
- `docs/current-game/` 下的 `skills.json`、`areas.json`、`quests.json` 這類檔案預設視為 generated read model；若本輪是在調整現行 skill / area authoring source，優先回到 `data/structured/skills/skills.json`、`area/<area>/content.json`、`area/<area>/map.md`、`area/directory.lst` 與 runtime 檔本身。
- `document/` 這類 legacy authoring reference 若要進 GitHub Pages，優先整理成 `docs/current-game/` 下的 Markdown 頁面，而不是直接混進 `docs/3yWebsite/`。
- GitHub Pages 入口預設放在 `docs/index.md`，`docs/current-game/` 是現行版本內容區；目前 custom domain 為 `https://sango.jakeuj.com/`。
- 舊版站點則連到外部的 `https://3y.jakeuj.com/`。
- `docs/area-data-systemization-assessment.md` 用來記錄 area rebuild 完成度與 area / skill 資料結構化、資料庫化評估結論。
- `plans/0005-area-skill-data-systemization.md` 用來記錄 v1 `structured JSON source -> exporter -> legacy runtime files` 的正式落地方案。
