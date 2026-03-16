# 技能戰鬥鏈資料盤點與重建計畫

## Summary

這份計畫把「NPC 技能實效偏弱是否來自釋出版清值」正式落成為可執行的全域審計流程。
本輪範圍只鎖定技能戰鬥鏈，不擴大到掉寶經濟、一般物件數值或全 area 生態平衡。

另已拆出一份專門處理 legacy skill `#Damage Value` 重建的子計畫：

- `plans/0003-legacy-skill-damage-audit.md`

之後若問題主因偏向 skill 模板本身，而不是 mob 掛鏈錯位，應優先續做 `0003`。

第一階段先完成兩件事：

1. 建立統一的審計模型與異常判定規則。
2. 產出機器可讀審計台帳，先覆蓋試點批次與已知高風險樣本。

這份計畫不取代既有的 `plans/failenable-npc-skill-audit.md`；後者仍作為 loyang / beiping 守軍高風險族群的聚焦審計輸入。

## Runtime Source Of Truth

- `skill/*.ski`
- `skill/skill.lst`
- `src/merc.h`
- `data/symbol.def`
- `area/*/mob/*.mob`
- `area/*/obj/*.obj`
- `area/*/res/*.res`
- `src/merc.sample.ini`
- `src/merc.ini`

## Audit Domains

審計台帳固定拆成五個 domain：

- `skill_definition`
  - `Valid / Enable / Teach / CanAsk / Adeptation / Damage / Limit`
- `mob_enable`
  - `Enable / AutoEnable`
- `mob_teach`
  - `#Learn`
- `skill_item`
  - `RES_SKILL` 或其他技能引用物件
- `global_coeff`
  - `Attack Value / Skill Value / Mob Practice`

每筆審計記錄固定欄位：

- `domain`
- `runtime_key`
- `source_file`
- `current_value`
- `reference_value`
- `reference_source`
- `status`
- `notes`
- `pilot_batch`

`status` 只使用：

- `ok`
- `suspect`
- `restore_candidate`
- `intentional_divergence`
- `blocked`

## Reference Priority

重建與判定一律依以下優先序：

1. 舊版可運作體感資料
   - `docs/3yWebsite/docs/data/skills.json`
   - `docs/3yWebsite/docs/data/players.json`
   - `docs/3yWebsite/docs/skills.md`
   - 必要時再回查 2.0 舊 repo
2. 目前 repo 的 runtime 現況
   - `skill/*.ski`
   - `area/*/mob/*.mob`
   - `area/*/obj/*.obj`
   - `area/*/res/*.res`
3. `ref/` 中的新設計資料
   - 只補設計意圖、命名體系與世界觀
   - 不直接覆蓋舊版強度基準
4. 舊資料若和 3.0 loader 結構衝突
   - 以可載入、可驗證的 3.0 結構優先

### 舊站 `skills.json` 已確認可直接提供的鏈路訊號

第一輪已從 `docs/3yWebsite/docs/data/skills.json` 抽到下列可直接使用的 legacy reference：

- `cloud steps`
  - `互相教導 = 可以`
  - `技能功能 = 閃躲類`
  - `領悟技能 = 青玄身法(gdragon steps)`
- `hua`
  - `中文名稱 = 華山劍法`
  - `互相教導 = 可以`
  - `領悟技能 = 封山劍法(fonxan sword)`
- `pry`
  - `中文名稱 = 打聽技能`
  - `技能分類 = 吟唱系`
  - `互相教導 = 不可以`

這些欄位目前足夠支撐：

- 既有 guard / escort 類 NPC 的舊技能升階脈絡比對
- `cloud steps -> gdragon steps` 這條步法鏈的 legacy 對照
- `hua sword` 與宮廷 / 守軍新技能鏈之間的替換合理性說明
- `pry` 在現行 repo 中作為 NPC 教學或工具技能時，和舊站玩家向技能定位的差異標註

### 舊站 `players.json` 已確認可直接提供的玩家養成定位

第二輪補讀 `docs/3yWebsite/docs/data/players.json` 後，已確認它適合拿來補強 `skills.json` 不會直接講出的「玩家職系定位」：

- `刺客精練-步法`
  - `cloud steps` 是舊站玩家向步法之一
  - 內容直接接到 `青玄身法(gdragon steps)`，可和 `skills.json` 的升階欄位互證
- `將軍精練-步法`
  - 再次確認 `cloud steps -> gdragon steps` 並非單篇偶然提及，而是武官向共通知識
- `新手上路`
  - 把 `cloud steps`、`hua sword`、`long fist` 放在新手早期 learn 清單，說明它們屬舊版常見入門技能線
- `刺客精練-前言與說明` / `弱弱的刺客之道 Part 2`
  - `雙十` 被放在刺客高階劍法討論脈絡，而不是守軍制式技能脈絡

這份玩家資料目前最有價值的用途有兩個：

- 把 `skills.json` 的技能欄位訊號轉成「這個技能在舊站是給誰走的」語境
- 用來區分 `legacy but role-consistent` 和 `legacy but role-misaligned` 兩種 outlier

## First-Pass Findings

### 1. Global coeff 並非全部都是戰鬥倍率

第一輪原始碼追查結果：

- `Attack Value`
  - 只控制戰鬥訊息中是否顯示實際傷害數字，見 `src/fight.c`
- `Skill Value`
  - 只控制技能熟練度是否顯示在技能/致能相關輸出中，見 `src/act_move.c`、`src/enable.c`、`src/bit.c`
- `Mob Practice`
  - 指向 `make.c` 產生的練功用 mob vnum，不是 NPC 技能傷害或熟練度倍率

因此這三個欄位仍保留在審計台帳內，但目前不視為第一優先修值點。

### 2. NPC-only 技能的 `Valid NO` 目前屬刻意分歧

目前試點新增技能如：

- `military blade`
- `military steps`
- `imperial sword`
- `imperial steps`
- `night blade`
- `shadowtrace steps`
- `cavalry lance`

都呈現 `Valid NO` 且 `Enable YES`。

這代表它們預設不面向玩家技能查詢/學習清單，但仍允許 mob 透過 `Enable` 使用。
因此這類條目應標成 `intentional_divergence`，不是直接當作 loader 錯誤。

### 3. 試點批次已存在可維持的正常梯階，也存在待回補 outlier

目前 loyang / beiping 已可觀察到：

- 正常梯階樣本
  - `501`, `503`, `545`, `565`, `569`
  - `9001`, `9002`, `9008`, `9009`, `9011`
- 明顯 outlier
  - `559`
    - 仍使用 `gdragon steps 26` + `two sword 1`
    - 相對於同 guard family 的軍旅技能梯階，應列入 `restore_candidate`
    - 舊站 `skills.json` 已確認 `cloud steps -> gdragon steps` 是既有步法升階鏈；`players.json` 也確認這條鏈屬新手 / 武官常見步法脈絡，因此 `gdragon steps` 可保留作 legacy 對照
    - `players.json` 另把 `雙十` 放在刺客高階劍法脈絡，進一步說明 `two sword 1` 不只是數值偏低，而是角色身份鏈本身錯位

### 5. `559.mob` 已完成第一個 runtime 修正試點

目前 `area/loyang/mob/559.mob` 已由：

- `gdragon steps 26`
- `two sword 1`

調整為：

- `military steps 55`
- `military blade 55`

這次修正的意義是：

- 讓 `559` 正式回到 `city_guard_mid` 的軍旅身份鏈
- 把最明確的 `restore_candidate` 轉成已落地樣本
- 用最小 runtime 變更驗證目前的審計方法確實能導出可載入、可啟動的修正

### 6. `loyang / beiping` guard-family sweep 第一輪結果

`559.mob` 修正後，已重新掃過 loyang / beiping 兩區與本試點最相關的 guard-family 樣本：

- 已在既定梯階內，無需再動的核心樣本
  - `501`, `503`, `545`, `560`, `565`, `569`, `576`, `577`, `578`
  - `9001`, `9002`, `9008`, `9009`, `9011`
- 這輪沒有再發現第二個「像 `559` 一樣仍掛 legacy 錯位技能鏈」的明確 outlier

但 sweep 也補出兩個新的邊界樣本：

- `9010` `城門衛軍`
  - guard-family 身份明確，但目前完全沒有 `Enable`
  - 比較像「尚未配置 entry-level 軍旅技能」而不是 legacy 錯鏈殘留
- `9018` `禁衛軍小隊長`
  - 皇城 guard-family 身份明確，但目前也沒有 `Enable`
  - 比較像「缺少小隊長級軍旅 / 皇城技能配置」而不是沿用錯技能

因此下一輪不再把重點放在「清理錯位 legacy skill」，而是：

- 補一個 `guard entry / junior leader` 子批次
- 先定義低階城防與低階禁衛的目標帶，再落 runtime 值

### 7. `9010` / `9018` 已完成 entry-level guard 子批次

這輪已把北平兩個缺 `Enable` 的 guard-family 邊界樣本補齊：

- `9010` `城門衛軍`
  - 補為 `military blade 40` + `military steps 40`
  - 定位為低階城門軍職，略低於 `501/559` 的 `city_guard_mid`
- `9018` `禁衛軍小隊長`
  - 補為 `imperial sword 50` + `military steps 50`
  - 定位為皇城入門到正式禁衛之間的過渡帶，低於 `9009` 這類高階皇城守衛

這樣的好處是：

- 把兩個「沒有技能」的 guard 樣本先拉回可戰鬥、可分層的狀態
- 保留 `9001 -> 9009` 的皇城主鏈，不讓小隊長直接跳進高階 `imperial steps`
- 讓北平 guard-family 從城門低階、禁衛入門到御前高階有連續梯度

### 4. `RES_SKILL 'noname'` 目前不能再直接標成 placeholder 壞資料

第二輪交叉比對後，`area/limbo/obj/84.obj` 的 `RES_SKILL 'noname'` 已確認：

- runtime 有真實技能檔：`skill/n/noname.ski`
- `skill/skill.lst`、`src/merc.h`、`data/symbol.def` 也都有正式登錄 `SLOT_NONAME`
- loader 對 `RES_SKILL` 的檢查只要求技能名稱可成功 resolve 成 slot

因此 `noname` 目前不是「不存在的技能名」，而是：

- 一條已存在的 legacy 技能門檻
- 是否仍符合 limbo 物件設計意圖，屬於後續 `skill_item` 子批次再判讀的問題

也就是說，`84.obj` 不再是目前最明確的 loader-risk 修正點；它應從「立即修值目標」降級為「已 resolve 名稱存在性、待補設計意圖驗證」。

### 8. `skill_item` 子批次首筆 `84.obj` 已完成設計意圖判讀

這輪已把 `area/limbo/obj/84.obj` 的 `RES_SKILL 'noname'` 從「名稱存在性確認」再往前推到「設計意圖確認」：

- runtime 端有真實技能檔 `skill/n/noname.ski`
- repo 內有對應秘笈 `area/limbo/obj/215.obj`
  - `ShortDesc = 無名劍法秘笈`
  - `Value1 = SLOT_NONAME`
- 舊站 `docs/3yWebsite/skill/sword.html` 也有 `無名劍法(noname)` 的技能頁

因此目前可以把 `84.obj` 判定為：

- 一把明確綁定 `無名劍法` 熟練度門檻的 legacy 劍系裝備
- 不是 placeholder、不是錯 skill name，也不是目前最需要修掉的 skill_item 異常

這輪沒有修改 `84.obj` runtime data，因為現有證據比較支持「它本來就是這樣設計」。

### 9. loyang / beiping 城市與宮廷 legacy sweep 第二輪

這輪把試點範圍從 guard-family 再往外擴一小圈，直接重掃 loyang / beiping 目前仍掛 legacy combat skill 的城市 / 宮廷 / 地痞 / 教學戰鬥樣本，並分成三類：

- 可合理保留
  - `537` 訓練師
  - `538` / `539` / `572` 等支援型 NPC
  - `9003` 藥鋪伙計
  - 以及 `548-554`、`583`、`591`、`593-604` 這些已偏特殊 / named / 高階樣本
- 明顯錯位或過弱，已直接修正
  - `571` 流氓
  - `9014` 錦衣侍者
- 證據不足，先記 suspect
  - `512` 地政官吏
  - `570` 詩人

這裡最重要的新結論有兩個：

- `area/loyang/mob/571.mob` 的 `gdragon step` 已可確認是 typo / 殘留錯值，不是 alias
  - repo 內真實存在且唯一登錄的技能只有 `gdragon steps`
  - 全 repo 搜尋沒有第二條可載入的 `gdragon step` 技能定義
- 並非所有 legacy skill 都應直接抹掉
  - `NoKill` 的教學 / 店務 NPC，或已經長期自成一條 named / boss 線的樣本，現階段更適合先保留並記錄理由

### 10. 本輪 runtime 修正：`571` / `9014`

`571` `流氓` 由：

- `long fist 100`
- `gdragon step 100`

調整為：

- `evil fist 60`
- `gdragon steps 55`

理由：

- `evil fist` 本身就帶有地痞 / 惡霸語境，比 generic starter 拳路 `long fist` 更符合身份
- `gdragon step` 的 singular 拼法不是現行 runtime skill key，修回 `gdragon steps` 才是正確 loader 路徑

`9014` `錦衣侍者` 由：

- `gdragon steps 100`

調整為：

- `imperial sword 48`
- `military steps 45`

理由：

- 這個樣本實際上穿全套裝備、持 `紫微軟劍`，並駐在京城軍糧節點，不是單純無戰鬥力的背景僕役
- 先補成低階宮廷 / 京城侍從可用的劍步組，並刻意壓在 `9018` 這種正式小隊長之下

### 11. Batch B follow-up：`512` / `572` 回調到 `cloud steps`

在 `plans/0003-legacy-skill-damage-audit.md` 完成 Batch B 後，`cloud steps` 與 `gdragon steps` 的身份界線變得更清楚：

- `cloud steps`
  - 舊站與新手導流都支持它是入門步法 / 基線自保
- `gdragon steps`
  - 現在已重新站穩為 `cloud steps` 的升階步法

因此這輪回看城市服務 NPC 時，`512` 與 `572` 的判讀不再需要停在 suspect：

- `512` `地政官吏`
  - 位在洛陽宮城入口南側的文職服務節點
  - 保留 `long fist 100`
  - 將 `gdragon steps 100` 改為 `cloud steps 70`
- `572` `郎中`
  - 城內可被攻擊的醫療服務 NPC
  - 本來就主要靠 `fight_prog` 施放 `burning hands`
  - 將 `gdragon steps 100` 改為 `cloud steps 70`

這兩筆修正的共同原則是：

- 不把可被玩家打到的城市服務 NPC 留在已重建的進階步法鏈上
- 但也不把它們改成完全沒有自保
- 讓 `cloud steps` 回到「入門自保 / 城市平民級身法」的 runtime 位置

相對地，這輪仍先保留：

- `570` 詩人
- `537` 訓練師
- `538` 醫生
- `539` 小道士
- `9003` 藥鋪伙計

原因是它們不是 `NoKill` 就是明顯以教學 / 法術 / 店務為主，目前沒有足夠收益支持再動。

### 12. `570` 詩人：由 suspect 轉為合理保留

這輪補完 `570` 的 old-site 與 runtime 證據後，判讀已足夠從 suspect 移到合理保留：

- 舊站 `skill/holy.html` 直接記載
  - `洛陽城的詩人(poet man)` 有教導 `detect evil`
- `570.mob` 目前的教學內容正是
  - `detect evil`
- `shade steps` 本身在 runtime 與舊站都不是純盜賊專用
  - 可學職系包含 `伶人 / 郎中 / 文官 / 道士 / 將軍 / 天師 / 鑄劍師`
  - 舊站步法頁把它列為 `換星步 -> 風影藏` 的獨立支線

因此 `570` 更像是：

- 一個帶有文人氣質、能教導聖系偵測技的洛陽特色 NPC
- 掛 `shade steps` 屬於風格化自保，而不是像 `gdragon steps` 那樣明顯踩進已重建的入門主鏈 / 升階主鏈衝突

現階段不建議為了「城市 NPC 看起來要弱一些」而硬把它改回 `cloud steps` 或其他 generic dodge，避免抹掉這個樣本少數還保有的職系味道。

### 13. `long fist` 城市 / 教學 / 服務樣本盤點

這輪把目前仍掛著 `long fist` 的樣本再掃一遍，並只保留「城市 / 教學 / 服務 NPC」：

- 納入盤點
  - `512` 地政官吏
  - `537` 訓練師
  - `570` 詩人
  - `9003` 藥鋪伙計
- 排除
  - `548-554`
  - 這批雖然也掛 `long fist`，但實際上是 `sky shaman` 特殊道士群，分布在 `650-656` 的獨立節點，不屬於城市 / 教學 / 服務 baseline

本輪分群結果：

- 入門自保
  - `512` 地政官吏
    - 現在已是 `long fist + cloud steps`
    - 屬於可被玩家打到的文職服務節點，較像 baseline self-defense，而不是身份錯位
- 可合理保留
  - `537` 訓練師
    - 新手屬性訓練主節點，`NoKill`
  - `570` 詩人
    - `detect evil` 教學 NPC，保留文人氣質線
  - `9003` 藥鋪伙計
    - `NoKill` 店務樣本，現階段仍以低暴露服務 NPC 看待
- 身份錯位
  - 目前沒有新的明確樣本

這個結果對 Batch C 有兩個直接意義：

- `long fist` 目前在城市 / 教學 / 服務樣本裡，更多是「入門自保」與「generic fallback」訊號，而不是自動代表錯配
- 所以下一輪做 `long fist / lung shan / tackle` 時，重點應該放在技能梯階本身是否失真，而不是先假設所有掛 `long fist` 的城市 NPC 都要換掉

補記：

- `plans/0003-legacy-skill-damage-audit.md` 的 Batch C 現已完成第一輪實作
- `long fist / lung shan / tackle` 已按多因子 pre-check 結果，只重建 `Value` 梯階，保留原本的 `Chance / Parry / Wait / Cost / CostType / Weapon / Check`
- 因此這份計畫接下來不再是「是否要做 Batch C」，而是「Batch C 之後哪些城市 / 教學 / 服務樣本需要第二輪身份分流」

## Next Execution Queue

下一輪若開始真正動 runtime data，建議順序固定為：

1. `Batch E` fallout recheck 後續
   - `604` 已確認屬高階地下水區 special keep case，不需 civic-style 回調
   - 若後續重建 `mirage steps`，再一併回看 `598-601 / 604` 這條地下水區 elite cluster 的整體手感
2. 下一條 legacy offensive ladder
   - 優先考慮同為將軍線的 `dream blade -> sea flow blade -> fast blade`
   - 延續 `Value / Chance / Parry / Wait / Cost / CostType / Weapon / Check` 多因子 pre-check 流程
3. `skill_item` 子批次
   - `84.obj` 已確認屬 legacy 設計正例
   - 若後續還有其他 `RES_SKILL` 物件，再擴成全量 object gate 盤點；目前 limbo 內未看到第二個同型樣本

### 14. Batch C fallout recheck：`512 / 537 / 570 / 9003`

這輪把 Batch C 後最直接受影響的四個 `long fist` 城市 / 教學 / 服務樣本重新盤了一次，重點改成：

- 不再只問「技能名要不要換掉」
- 而是分開問：
  - 角色身份鏈是否仍合理
  - `long fist 100` 在 restored ladder 下是否過高

結論如下：

- `512` `地政官吏`
  - 仍屬 `entry_self_defense`
  - 保留 `long fist + cloud steps`
  - 但把 `long fist` 由 `100` 回調到 `70`
  - 原因是它是可被攻擊的宮城外文職服務節點；在 Batch C 後，`long fist 100` 已不再像 generic fallback，而更像完整戰鬥樣本
- `570` `詩人`
  - 保留 `long fist + shade steps`
  - 舊站 `holy.html` 對 `detect evil` teacher 的證據仍成立，`shade steps` 也仍屬文人相容支線
  - 但同樣把 `long fist` 由 `100` 回調到 `70`
  - 這讓它維持文人氣質自保，不會因拳法模板重建後變成過強 civic combatant
- `537` `訓練師`
  - 維持現狀
  - `NoKill` 新手服務節點，現階段沒有足夠收益去再調
- `9003` `藥鋪伙計`
  - 維持現狀
  - `NoKill` 店務樣本，低暴露、低優先

所以這輪 fallout recheck 的實際動作不是再換技能鏈，而是：

- `512`
  - `long fist 100 -> 70`
- `570`
  - `long fist 100 -> 70`

這也進一步確認：Batch C 之後真正需要補的，往往不是整條 civic chain 推倒重來，而是把「原本歷史上隨手填的 `Enable 100`」回調到和角色身份相符的等級。

### 15. Batch E fallout recheck：`604` `six demon king`

這輪補做了刀法梯階重建後最直接的 fallout 檢查，聚焦目前唯一直接掛著 `tiger blade` 的 runtime 樣本：

- `604` `六天魔王`
  - `Enable 100 'tiger blade'`
  - `Enable 100 'mirage steps'`
  - `Level 100`
  - `AttackRatio / DodgeRatio = 200 / 200`
  - `sanctuary`、`detect invis`、`detect hidden`

結論是：維持現狀，列為 `reasonable_to_keep`，不做 runtime adept 回調。

理由：

- 它不是城市 / 教學 / 服務 NPC，而是 loyang 地下水區的 named high-tier special sample
- `tiger blade` 在 Batch E 後已明確回到高威力、重成本、慢節奏的將軍高階刀法定位
- `mirage steps` 雖尚未進入獨立 rebuild batch，但和同區 `598-601` 一起形成地下水區 elite cluster，並非單隻誤掛
- 因此這個樣本更像是「高階 special 組合需要後續整批一起看」，而不是 civic fallout 那種因 ladder 恢復後變得過強的 generic `Enable 100`

這個判定也代表下一輪若繼續動 runtime，優先順序應回到新的 legacy attack ladder，而不是先對 `604` 做單點止血。

## Pilot Batch

第一個試點批次固定為：

- `loyang`
- `beiping`

聚焦 NPC archetype：

- 城市守衛 / 城門守衛
- 騎兵 / 禁軍護衛
- 殿前護衛 / 御前護衛
- 京城大盜 / 扶桑浪人

聚焦技能：

- `military blade`
- `military steps`
- `imperial sword`
- `imperial steps`
- `night blade`
- `shadowtrace steps`
- `cavalry lance`

### Pilot archetype target bands

| Archetype | 攻擊技能 | 目標熟練度 | 步法 | 目標熟練度 |
| --- | --- | --- | --- | --- |
| 城防中階 | `military blade` | `55-65` | `military steps` | `55-65` |
| 城防高階 | `military blade` | `65-75` | `military steps` | `60-70` |
| 軍旅騎兵中階 | `cavalry lance` | `60-70` | `military steps` | `50-60` |
| 皇城入門 | `imperial sword` | `45-55` | `military steps` | `45-55` |
| 皇城高階 | `imperial sword` | `75-85` | `imperial steps` | `70-80` |
| 皇城頂階 | `imperial sword` | `90-95` | `imperial steps` | `85-90` |
| 夜行入門 | `night blade` | `50-60` | `shadowtrace steps` | `55-60` |
| 夜行中階 | `night blade` | `55-65` | `shadowtrace steps` | `60-65` |

## Anomaly Rules

優先標記以下異常：

1. `skill_definition`
   - `Enable NO` 但仍被現行 mob `Enable` 引用
   - `Valid NO` 但沒有明確 NPC-only 設計依據
2. `mob_enable`
   - 同 archetype 的熟練度落差過大且無設計解釋
   - 技能名稱明顯偏離既有身份鏈
   - `AutoEnable` 算出的熟練度與角色定位不符
3. `mob_teach`
   - `#Learn` 與技能 flags 或 teacher 角色定位矛盾
4. `skill_item`
   - `RES_SKILL` 指向不存在或不明技能
5. `global_coeff`
   - 只有在證明會直接改變實戰體感時，才升級為修值批次

## Validation

審計階段：

- 檢查 `skill/*.ski`、`skill/skill.lst`、`src/merc.h`、`data/symbol.def` 的登錄一致性
- 檢查 `mob Enable / AutoEnable / #Learn` 是否能對應到有效 runtime 路徑
- 檢查 `RES_SKILL` 物件是否能對應到真實技能名稱
- 更新 `docs/current-game/skill-combat-audit.json`

若下一輪開始做 runtime 修正：

- `make -C src -f Makefile.lin merc`
- 有 runtime data 變更時，再做一次本機 smoke test
- 回看 `log/*` 與 `debug/*`
- 特別檢查 `Load_skill`、`Load_mobiles`、`LOG_FAILENABLE`

本輪已完成的 runtime 驗證：

- `bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- `timeout 45s sh -lc 'cd src && ./merc merc.ini' > log/smoke-legacy-round2.log 2>&1`
- 成功訊號：`三國歪傳之降龍伏虎開始正常運作`
- 本輪額外關注 `Load_skill`、`Load_mobiles`、`LOG_FAILENABLE`，尤其針對 `571` 的 typo 修正與 `9014` 的新 `Enable` 組

## Ref Metadata

- `ref_inputs_used`
  - `ref/Readme.md`
- `ref_inputs_deferred`
  - `world-graph.json`
  - `三國-MUD-世界設計總藍圖-Architecture-Map.md`
  - `三國-MUD-題材分布表.md`
- `theme_basis`
  - 這輪以 loyang / beiping 現有守軍、皇城、夜行、城市雜兵 / 教學 NPC 的舊版體感與現行 runtime 身份戰技補完為主，不以新世界藍圖重寫強度體系
- `compliance_check`
  - 本輪已直接落地 `area/loyang/mob/571.mob` 與 `area/beiping/mob/9014.mob` 的 runtime 修正；未動用 area tracker，也未改動 area load order
