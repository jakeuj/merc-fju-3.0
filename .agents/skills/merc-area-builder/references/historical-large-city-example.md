# 歷史範例：Stormwind / Orgrimmar

這份參考整理 commit `8df189ef9153e463e435d817893967e033f3a976` 中的 `stormwind` / `orgrimmar` 區域做法。

把它當成「歷史大型城鎮範例」即可，不要把它當成目前 `merc-fju-3.0` 的主模板。現在專案的現行世界線仍應優先參考：
- `area/loyang`
- `area/beiping`
- `area/new`
- `area/newfight`
- `area/pk_area`
- `area/free_fight`

## 先看這份範例的用途
- 適合拿來觀察「大型城鎮級區域」如何拆 `mob/obj/roo/res/shp`
- 適合拿來看 `res` 如何依守衛、商店、功能 NPC 分段
- 適合拿來看大量 `Process` / guard / faction 類 NPC 的寫法
- 不適合直接當 3.0 正式世界觀、地名、勢力或 VNUM 規劃的主依據

## 使用限制
- 這份範例來自舊設計脈絡，世界觀是 Warcraft 城市，不是目前 repo 的三國主世界
- `stormwind` / `orgrimmar`、Alliance / Horde、相關 NPC 與物件命名都屬歷史內容；若要借骨架，搬入前必須全部改名
- 原範例採用大段連號 VNUM 與城市級配置，僅能參考其拆分方式，不能直接假設現行 3.0 也要照同一區段
- 若現行 repo 已有對應功能（出生地、交通、懸賞、戰鬥入口），仍以現行 `src/`、`data/`、`help/` 耦合為準

## 可以學的結構

### 目錄拆分
- 每區都拆成 `index`, `mob/`, `obj/`, `roo/`, `res/`, `shp/`
- 這點仍然有參考價值，因為符合 `document/*.txt` 與目前 3.0 area 目錄習慣

### 大型城市的 reset 分段
- `res/*.res` 以功能群組分段，例如守衛、商店、王宮、交通 NPC
- 這種分段方式在今天仍值得保留，因為 debug `M/E/G/O/D/R` 關聯時比較快
- 若遇到原始 Merc reset 細節不確定，回看 `doc/area-file-format.txt` 與 `doc/security-features.txt`

### NPC 行為集中在少數核心角色
- 守衛、首領、功能 NPC 會帶 `Process`
- 這適合當作「把複雜邏輯集中在少數核心 mob」的範例，而不是要求每個 mob 都寫 script
- 若要理解 trigger 背景，可補看 `doc/mobprogram-guide.txt`

### 商店與物件供應鏈
- `shp/*.shp` 只定義店型與 keeper
- 真正的 keeper 刷新與裝備/商品綁定仍在 `res`
- 這點很重要：不要把商店存在與商品來源混成單一檔案概念

## 不要照抄的地方

### 世界觀與用詞
- 不要直接留下 Stormwind、Orgrimmar、Alliance、Horde 等名稱
- 不要直接沿用其陣營對立腳本描述
- 若是三國語境，應改成現行城名、國別、職官、怪物與交通語意

### VNUM 規劃
- 不要因為範例用了 `100xx` / `101xx` 就直接照搬
- 現行任務仍要先搜尋 `area/`、`src/`、`data/` 確認未撞號
- 若是從舊範例搬到 3.0，先做 mapping 表，再修改 `roo/res/mob/obj/shp`

### 系統耦合
- 這份範例只說明 area 內部資料，不代表現行出生點、`recall`、巴士、船、懸賞、help 文案都會自動跟上
- 真正落地時，仍要回到：
- `src/merc.ini`
- `src/variable.c`
- `src/job.c`
- `data/bounty.txt`
- `data/bus.txt`
- `data/ship.txt`
- `help/`

## 如何正確使用這份歷史範例
1. 先用現行 3.0 區域決定目錄格式、命名習慣與系統耦合。
2. 只在需要大型城市骨架、reset 分段方式、商店配置方式時，回頭參考這份歷史範例。
3. 若要搬內容，先把舊 VNUM、舊地名、舊 NPC 名稱整理成 mapping。
4. 完成後再依 `document/*.txt`、`doc/area-file-format.txt`、`doc/skills-and-spells-guide.txt` 重新驗證欄位意義。
5. 最後用現行 3.0 啟動流程與 `log/`、`debug/` 實際驗證，不要只因為範例能讀就視為完成。

## 可借用的觀察點
- `index` 如何寫城市級描述
- `roo/` 如何切主街、功能區、王宮或特殊區
- `res/` 如何分段組織大量 NPC / 物件刷新
- `shp/` 如何配置多間不同用途的商店
- `Process` 如何集中在少量關鍵 NPC

## 交叉參考
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`
- `doc/area-file-format.txt`
- `doc/mobprogram-guide.txt`
- `doc/security-features.txt`
- `doc/skills-and-spells-guide.txt`
- `references/area-build-checklist.md`
