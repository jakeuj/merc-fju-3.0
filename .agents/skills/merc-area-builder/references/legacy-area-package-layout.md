# Legacy Area Package Layout

## 何時讀這份
- 題目引用 `document/README`，但你真正需要的是 area package 結構、`area/` 子目錄角色、或「為什麼要回看舊 area 範例」。
- 你正在解讀 `index / mob / obj / res / roo / shp` 在 legacy 釋出包裡各自負責什麼。

## 搭配閱讀
- `references/file-handling-rules.md`
- `references/current-repo-state.md`
- `docs/current-game/legacy-readme.md`

## 這份只保留什麼
- `document/README` 中和 area authoring 直接有關的部分
- legacy release tree 對 today repo 的大方向映射
- area 子目錄的角色與回看既有 area 的理由

## 這份刻意不處理什麼
- `make clean; make`
- `startup &`
- `merc.ini`
- `log/` / `debug/` 啟動排錯

這些內容現在應交給 `merc-local-ops`；若題目是在追資料樹和 code/data load flow 的對應，交給 `merc-source-explainer`。

## Legacy 釋出包視角

`document/README` 把舊版工作樹分成幾個主要部分：

- `src/`
- `area/`
- `data/`
- `document/`
- `skill/`
- `help/`
- `social/`
- `player/`
- `mail/`
- `log/`
- `debug/`

對 area builder 最重要的是：它明確把 area 視為一個資料包，而不是單一大檔。

## 一個 area 至少包含什麼

legacy 文件點出的 area 子結構，今天仍然是 repo 的核心概念：

- `index`
- `mob/`
- `obj/`
- `res/`
- `roo/`
- `shp/`

對今天的 `merc-fju-3.0` 來說，可以把它理解成：

- `index`：area metadata，對應區域名稱、編輯者、序號、等級帶、出生城等
- `mob/`：怪物定義
- `obj/`：物品定義
- `res/`：reset / spawn / equip / door state 指令
- `roo/`：房間與出口投影
- `shp/`：商店資料

spec-first area 另外會多一層：

- `map.md`：人類可讀 spec
- `mapmd-json`：canonical machine-readable graph

## 為什麼 area 任務要回看既有區域

`document/README` 的年代很早，但有一個觀念到現在仍然成立：不要只靠格式手冊猜資料長什麼樣子，還要回看已成功載入的 area 範例。

在現在的 repo，這個原則更重要，因為：

- legacy 文件和 current loader 行為有落差
- 一些欄位名、常數名、結束規則只看手冊會誤判
- `#Keyword` / `#Job` / `#Enquire` 等 `.roo` block 需要和 repo 現況一起理解

## Today repo crosswalk

把 `document/README` 的釋出包視角對映到今天 repo 時，可先抓這個粗略關係：

- legacy `area/` -> today `area/`，但多了 `map.md`、plan/tracker、current-game docs 支援
- legacy `document/` -> today `document/` 仍是 source material；快速閱讀入口則在 `docs/current-game/`
- legacy build/startup 說明 -> today `README.md`、`src/startup.bash`、`merc-local-ops`

## Repo-specific guardrail

- `document/README` 是 release-era 背景文件，不是目前 area workflow 的最終流程文件。
- area 結構與檔種角色可以沿用它的概念，但實際 authoring 順序、驗證與 spec-first workflow 應以 `docs/area-development-handbook.md`、`plans/`、`area/rebuild_plan.md` 和本 skill 其他 references 為準。
