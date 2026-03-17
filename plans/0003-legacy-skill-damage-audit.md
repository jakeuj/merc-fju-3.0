# Legacy Skill Damage Audit Plan

## Summary

這份計畫處理的是另一條已被確認的上游問題：

- 大量 legacy 技能的 `#Damage -> Value` 幾乎被清成 `20`
- 這會同時影響玩家體感、NPC 技能模板、以及 `Load_mobiles -> get_adeptation()` 的 failenable 判定

因此後續不能只靠替 mob 換成 NPC-only 新技能止血，還需要逐批重建舊技能鏈本身的 damage ladder。

## Why This Exists

目前 repo 已確認：

- `skill/*.ski` 中有 `#Damage Value` 的技能共 `145` 筆
- 其中 `133` 筆所有 `Value` 都是 `20`
- 舊站 `players.json` 與 `skills.json` 明確描述了玩家向技能升階鏈
- 舊站 `newhand/newbies/index.html` 也補上了新手期的技能分類與致能建議

這代表現況很可能出現：

- 新手技與高階技實際威力接近
- 宗師級 NPC 掛高階 legacy skill，卻仍可能被 loader 判定為「太差」
- 新 area / teacher / boss 設計若直接沿用舊技能名，會持續繼承失真的底層模板

另外 `docs/3yWebsite/newhand/newbies/index.html` 已明確把技能使用面分成：

- 攻擊類
- 步法類
- 逃跑類
- 法術類
- 雜類

並建議新手至少致能一個攻擊類、一個步法、與一個逃跑類技能。這表示後續做玩家向 skill ladder 重建時，不能只看單一 offensive 鏈，也要保留新手戰鬥組合的最小成立條件。

## Source Of Truth

技能模板與驗證以 runtime 為準：

- `skill/*.ski`
- `skill/skill.lst`
- `src/load.c`
- `src/handler.c`
- `src/fight.c`
- `src/act_info.c`
- `src/bit.c`
- `src/class.c`
- `document/mob.txt`

技能文件與玩家可讀說明基線：

- `docs/current-game/skill-file-format.md`
- `docs/current-game/skill-loader-reference.md`
- `docs/current-game/skill-constants.md`
- `docs/current-game/skill-pry-crosswalk.md`

技能鏈與玩家體感基線以舊站資料為準：

- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/newhand/newbies/index.html`

另外，repo 現在已補上 current-game 技能文件頁；之後遇到「玩家文案和 `.ski` 是否一致」這類問題時，先用文件頁快速對照，再回頭以 runtime source 決定最終答案，避免把舊 help 範例或玩家整理文直接當成現況。

## Core Hypothesis

目前最值得優先驗證的假設是：

- 釋出版曾把大量 legacy skill 的 `#Damage Value` 先重置為 `20`
- 這不是單一技能偶發，而是系統性清值
- failenable 的大量「太差」警告，至少有一部分正是由這個清值造成

## Important Limitation

不能把 `#Damage -> Value` 直接當成技能完整強度。

目前 runtime 已確認還有下列面向會共同影響體感：

- `#Damage -> Chance`
  - 決定各招式的出現機率與平均輸出分布
- `#Damage -> Parry`
  - 決定格擋對抗面
- `#Damage -> Innate`
  - 某些招式夾帶 innate 額外效果，不是單看 base damage
- `Skill -> Wait`
  - 決定施放節奏與攻擊頻率
- `Skill -> Cost / CostType`
  - 決定續戰效率
- `Skill -> Weapon / Check`
  - 決定武器門檻與實際攻擊型態
- `fight.c` 內的實戰折算
  - `hitroll`
  - `damroll`
  - `get_ac`
  - `dodge`
  - `sanctuary`
  - `protection`

因此：

- failenable 適合拿來判定「模板是否弱到離譜」
- 但不適合被當成唯一平衡指標
- 後續修值必須保留技能差異性，不能只把所有同階技能拉成同一碗水

另外，`document/mob.txt` 也提醒這裡至少還有一層 mob-side wiring：

- `Enable <adept> '<skill>'`
  - 固定熟練度
- `AutoEnable '<skill>'`
  - 由 loader 依 mob 條件反推熟練度
- `AttackRatio / DodgeRatio`
  - 直接影響 `get_adeptation()` 的目標強度
- `#Learn`
  - `Adept / Cost / Inventory / Name` 屬教學側 skill-facing data

因此就算某條 skill ladder 已重建，也不能直接假設所有掛這條 skill 的 mob 都會自動合理；還要看 mob 端是固定 `Enable`，還是經 `AutoEnable` 進 loader 公式。

## Combat Strength Model

後續每條技能鏈至少同時看五個面向：

1. `damage_profile`
   - `Value` 平均、峰值、最低值
2. `delivery_profile`
   - `Chance`
   - `Parry`
   - `Situs`
3. `tempo`
   - `Wait`
   - `Cost`
   - `CostType`
4. `weapon_identity`
   - `Weapon`
   - `Check`
   - 空手 / 劍 / 刀 / 槍 / 步法等類型差異
5. `runtime_amplifiers`
   - `hitroll`
   - `damroll`
   - `dodge`
   - `armor/ac`

## Design Rule

同鏈技能不追求單純的 `Value` 線性上升，而是追求：

- 綜合強度階梯成立
- 同時保留技能差異性

例：

- 輕靈劍法可接受較低單段 `Value`，但 `Wait` 較短
- 重兵技能可接受較高 `Value`，但節奏較慢、成本較重
- 步法不一定靠 `Value` 領先，而可能主要靠 dodge template 與節奏勝出

## Mandatory Pre-Check

每批 skill ladder 開工前，先列出該鏈所有 skill 的：

- `Value`
- `Chance`
- `Parry`
- `Wait`
- `Cost`
- `CostType`
- `Weapon`
- `Check`

並先判斷：

- 目前差異是不是已被清值清到幾乎消失
- 還是原本就有刻意設計成「低 damage / 高頻率」或「高爆發 / 高消耗」

只有確認該鏈真的被壓平，才直接上修 `Value`。

若這條鏈目前明顯被 mob 大量使用，或前一輪已發現 failenable / 身份錯位樣本，再額外列：

- 代表 mob 的 `Enable / AutoEnable`
- 代表 mob 的 `AttackRatio / DodgeRatio`
- 該 skill 是否常出現在 `#Learn`

目的不是把每批都變成全域 mob sweep，而是避免把「mob 端掛法」誤當成「skill 檔單點問題」。

## Execution Rules

1. 不要一次全域重寫所有 skill。
2. 先以「玩家可學、舊站有清楚升階鏈、目前 runtime 又幾乎全是 `20`」的技能鏈優先。
3. 每次只修 1 到 2 條鏈，並保留明確的 before/after 紀錄。
4. 每批開工前，先做 `Mandatory Pre-Check`。
5. 修 skill value 後，要回頭抽查：
   - 對應玩家向技能體感是否仍合理
   - 對應 mob 是否不再被 failenable 判成「太差」
   - 是否造成低階玩家技能過度膨脹
6. 若該鏈同時牽涉已知 `AutoEnable` 樣本，再補查代表 mob 的 `AttackRatio / DodgeRatio` 是否仍和新模板相容。

## Phase 1 Scope

第一批先鎖定三條鏈：

1. 劍法主鏈
   - `hua sword`
   - `fonxan sword`
   - `dragon sleeve sword`
2. 拳法主鏈
   - `long fist`
   - `lung shan`
   - `tackle`
3. 步法主鏈
   - `cloud steps`
   - `gdragon steps`
   - `sky steps`

## Why These Chains First

### 劍法主鏈

舊站 `players.json` 明確記載：

- `華山劍法 -> 封山劍法 -> 龍袖劍法`
- `封山` 與 `龍袖` 都被視為明顯高於入門的實戰技能
- `newhand/newbies/index.html` 也把技能學習與致能當成新手核心流程，支撐 `hua sword` 這類入門攻擊技不該和高階劍法等傷

但 runtime 目前至少已確認：

- `hua sword` 幾乎全 `20`
- `fonxan sword` 全 `20`

這條鏈最能直接回答：

- 高階劍法模板是否真的被壓扁
- 新手劍法與中高階劍法是否缺乏應有的 damage 梯度

### 拳法主鏈

舊站資料指出：

- `long fist` 是新手常見入門技能
- 後續還會往更高階空手鏈發展
- `newhand/newbies/index.html` 也把攻擊類列為新手必備致能類型，支撐入門拳法不該被視為可一路撐到高階的等價模板

這條鏈適合當作：

- 新手技能基準線
- 用來和高階拳法比較，避免只修劍法卻讓新手拳仍異常接近高階技

### 步法主鏈

舊站資料多次重複：

- `cloud steps -> gdragon steps`
- `sky steps` 是更高階、且玩家體感明顯更好的步法

這條鏈與 failenable 最直接相關，因為 dodge 技也會經過 `get_adeptation()`

## Deliverables

每一批次至少交付：

1. 被修技能鏈清單
2. 每個 skill 的 before / after `Value` 摘要
3. 對應舊站 reference 依據
4. failenable / smoke test 驗證結果
5. 需要同步調整的 mob 樣本清單

## Suggested Batch Order

### Batch A

- `hua sword`
- `fonxan sword`
- `dragon sleeve sword`

目標：

- 建立第一條完整 offensive legacy ladder
- 驗證高階劍法修值後，是否能降低對應 NPC 的「太差」警告

### Batch B

- `cloud steps`
- `gdragon steps`
- `sky steps`

目標：

- 建立第一批 dodge legacy ladder
- 先確認 `cloud -> gdragon` 與 `sleev -> sky` 的交叉分支關係，再決定修值方式
- 驗證步法梯度是否能更合理對應 guard / teacher / bravo/general 路線

### Batch C

- `long fist`
- `lung shan`
- `tackle`

目標：

- 把新手拳法與中高階拳法分開
- 避免未來 area / mob 設計仍把 `long fist 100` 誤當成可撐高階樣本的模板

## Validation

每批至少做：

- `make -C src -f Makefile.lin merc`
- 若 skill data 有改，做 smoke test
- 檢查：
  - `log/*`
  - `debug/failenable`
  - `debug/failload`
  - `Load_skill`
  - `Load_mobiles`

若該批同時牽動已知 mob 樣本，額外比對：

- 修值前後是否仍出現 `怪物編號 X 技能 Y 太差`

## Code References

- [src/handler.c](/H:/repos/merc-fju-3.0/src/handler.c)
  - `get_adeptation()`
- [src/load.c](/H:/repos/merc-fju-3.0/src/load.c)
  - `Load_mobiles` failenable 判定
- [src/fight.c](/H:/repos/merc-fju-3.0/src/fight.c)
  - `striking()`
  - `damage()`
- [src/skill.c](/H:/repos/merc-fju-3.0/src/skill.c)
  - 成本、wait、武器檢查、技能施放流程

## Resume State

目前狀態：

- `status = batch_e_fallout_checked`
- `current_focus = next legacy attack ladder`
- `current_batch = Batch F implemented`

## Immediate Next Steps

1. 下一個高價值候選可回到同頁將軍線 `sun blade -> ice blade -> gold blade`
2. 維持多因子 pre-check：`Value / Chance / Parry / Wait / Cost / CostType / Weapon / Check`
3. `604` 的 `tiger blade + mirage steps` 已確認屬 high-tier special keep case；若未來進入 `mirage steps` rebuild，再一起重看 `598-601 / 604`
4. Batch D 已確認 bow ladder 為 hybrid case；後續 offensive ladder 盤點前，先檢查該鏈是否為 `#Damage` 驅動還是 `spell.c` code-driven
5. 若後續再遇到 city / teacher 樣本掛著已重建 ladder，不先急著換技能名，先判斷是不是歷史 `Enable 100` 該回調

## Batch A Result

### Scope

- `hua sword`
- `fonxan sword`
- `dragon sleeve sword`

### Reference Basis

- `docs/3yWebsite/docs/data/skills.json`
  - `hua sword -> fonxan sword`
- `docs/3yWebsite/docs/data/players.json`
  - `新手上路`
    - `hua sword` 是新手 early learn baseline
  - `刺客精練-劍法`
    - `hua sword` 建議 `LV1`
    - `fonxan sword` 建議 `LV30`
    - `dragon sleeve sword` 建議 `LV50`
  - `刺客精練-前言與說明`
    - `華山劍法 -> 封山劍法 -> 龍袖劍法`
    - 明確指出 `封山` 是不能廢掉的中階主力

### Runtime Changes

`hua sword`

- before: `20,20,20,20,20,20,20`
- after: `60,75,90,105,120,135,150`
- average: `105.0`

`fonxan sword`

- before: `20,20,20,20,20,20,20,20`
- after: `110,130,150,170,190,210,230,250`
- average: `180.0`

`dragon sleeve sword`

- before: `20,20,20,20,20,20,20,20`
- after: `180,210,240,270,300,330,360,420`
- average: `288.75`

### Interpretation

- `hua sword` 被重新定位為「新手可學但不再和高階劍法同模板」的入門劍路
- `fonxan sword` 被拉成清楚高於 `hua sword` 的中階主力
- `dragon sleeve sword` 被拉成足以站穩高階玩家劍法位置的 Batch A 頂點

這一批先處理「同鏈的 damage ladder 是否存在」，還沒有對其他劍法支線做橫向平衡。

### Validation

- `make -C src -f Makefile.lin merc`
- smoke test:
  - 先以臨時 `merc.test.ini` 避開本機 port / IPC 衝突
  - 成功訊號：`三國歪傳之降龍伏虎開始正常運作`
- 本輪未見新的：
  - `Load_skill`
  - `Load_mobiles`
  - `debug/failenable`
  - `debug/failload`

### Notes

- 這一批主要修的是 skill template，因此目前不一定會立刻改變現行 explicit `Enable` mob 的 loader 警告
- 但它已經建立後續 area / teacher / boss 設計可依賴的第一條玩家向 offensive 劍法梯度
- 這一批尚未完整把 `Chance / Wait / Cost / Weapon` 納入同鏈對照，因此 Batch B 開始前必須先做 `Mandatory Pre-Check`

## Next Prompt

可直接續跑的 prompt：

> 請直接續做 `plans/0003-legacy-skill-damage-audit.md` 的 Batch A，先處理 `hua sword`、`fonxan sword`、`dragon sleeve sword` 的 damage ladder 重建。先讀 `docs/3yWebsite/docs/data/players.json`、`docs/3yWebsite/docs/data/skills.json`、對應 `skill/*.ski`，然後直接修改 skill value、做 build / smoke test、更新 plan 與必要的 audit。

目前可直接改用：

> 請直接續做 `plans/0003-legacy-skill-damage-audit.md` 的 Batch B，先處理 `cloud steps`、`gdragon steps`、`sky steps` 的 dodge ladder 重建。先讀 `docs/3yWebsite/docs/data/players.json`、`docs/3yWebsite/docs/data/skills.json`、對應 `skill/*.ski`，然後直接修改 skill value、做 build / smoke test、更新 plan 與必要的 audit。

## Batch B Pre-Check

### Reference Basis

- `docs/3yWebsite/docs/data/players.json`
  - `新手上路`
    - `cloud steps` 是新手 early learn baseline
  - `刺客精練-步法`
    - `cloud steps` 列為可直接學習的步法
    - `gdragon steps` 與 `cloud steps` 同段出現，對應 `cloud` 的高階方向
    - `sky steps` 明確寫成由 `sleev steps` 領悟，不是 `cloud` 的直升下一段
    - `sky steps` 被描述為「武官系數一數二的步法，花費體力很少、必備」
  - `將軍精練-步法`
    - 和刺客文同樣把 `sky steps` 放在 `sleev steps` 鏈上
- `docs/3yWebsite/newhand/newbies/index.html`
  - 新手導引明確把步法列為必備致能類型之一
  - 並且把攻擊 / 步法 / 逃跑列為新手最少應同時致能的三類技能
  - 因此 `cloud steps` 不只是 old-site chain 的 root，也屬於實際新手戰鬥組合的一環
- `docs/3yWebsite/docs/data/skills.json`
  - 只有 `cloud steps` 有單獨技能頁
  - `cloud steps` 明確標註可領悟 `gdragon steps`
- runtime `skill/*.ski`
  - `cloud_steps.ski`
    - `Associate SLOT_GDRAGON_STEPS`
  - `gdragon_steps.ski`
    - `Associate SLOT_MIRAGE_STEPS`
  - `sleev_steps.ski`
    - `Associate SLOT_SKY_STEPS`
  - `sky_steps.ski`
    - `Associate -1`

### Mandatory Pre-Check Snapshot

`cloud steps`

- type: `TAR_DODGE`
- cost: `5`
- costtype: `COST_MOVE`
- wait: `1`
- canask / teach: `YES / YES`
- damage entries: `7`
- chance set: `10`
- value set: `20`
- parry set: `0`
- damage innate set: `0 0`

`gdragon steps`

- type: `TAR_DODGE`
- cost: `15`
- costtype: `COST_MOVE`
- wait: `10`
- canask / teach: `YES / NO`
- damage entries: `7`
- chance set: `20`
- value set: `20`
- parry set: `0`
- damage innate set: `0 0`

`sleev steps`

- type: `TAR_DODGE`
- cost: `10`
- costtype: `COST_MOVE`
- wait: `10`
- canask / teach: `YES / NO`
- damage entries: `4`
- chance set: `20`
- value set: `20`
- parry set: `0`
- damage innate set: `0 0`

`sky steps`

- type: `TAR_DODGE`
- cost: `10`
- costtype: `COST_MOVE`
- wait: `10`
- canask / teach: `YES / NO`
- damage entries: `6`
- chance set: `20`
- value set: `20`
- parry set: `0`
- damage innate set: `0 0`

### Interpretation

- `cloud steps -> gdragon steps` 是舊站與 runtime 都能確認的同鏈關係。
- `sky steps` 不是 `cloud/gdragon` 直線升階；它更像 `sleev steps -> sky steps` 這條分支上的高階步法。
- `sleev steps` 也必須一起看，因為 `sky` 的 prerequisite、runtime `Associate`、以及舊站玩家文都指向 `sleev -> sky`，不是孤立高階技。
- 四者的 `Value` 都被壓成 `20`，表示 dodge template 確實存在系統性清值。
- 但這批也沒有被完全壓成同質：
  - `cloud steps` 只有 `Cost 5`、`Wait 1`，明顯保留了入門高頻、低成本特性。
  - `gdragon steps` 雖然也是 `Value 20`，但 `Cost 15`、`Wait 10`，代表它不可能單靠「更快」來成立高階定位。
  - `sleev steps` 與 `sky steps` 同為 `Cost 10 / Wait 10`，但 `sleev` 只有 `4` 段 damage entry、可學範圍更寬，較像平行分支的根技能。
  - `sky steps` 同樣 `Wait 10`，但 `Cost 10` 低於 `gdragon steps`，和舊站「花費體力很少」的描述相符。
- 因此 Batch B 不應直接把三者當同一條單線梯度一起上調；較合理的做法是：
  - 先把 `cloud -> gdragon` 當主鏈修 dodge template
  - 把 `sleev -> sky` 當平行分支一起檢查，避免只修 `sky` 卻讓 prerequisite 仍停在被清值的殘缺模板
  - 再把 `sky steps` 當平行高階步法，保留其「較省體力」特色來做橫向比較

### Implementation-Ready Direction

下一步修值前，建議採這個順序：

1. 先針對 `cloud steps` / `gdragon steps` 設計入門與中高階 dodge template 差距
2. 補進 `sleev steps` 的 branch baseline，至少讓 `sky` 的 prerequisite 不再維持全 `20` 殘缺模板
3. `sky steps` 不追求單純高於 `gdragon` 的所有數值，而是維持：
   - 高階定位
   - 相對省體力
   - 與 `sleev steps` 分支相符的武官 / bravo 路線特色
4. 修值後抽查目前大量掛著 `gdragon steps` 的城市 / 教學 / 服務 NPC，確認 failenable 與實戰模板是否較合理

## Batch B Result

### Scope

- `cloud steps`
- `gdragon steps`
- `sleev steps`
- `sky steps`

### Runtime Changes

- `skill/c/cloud_steps.ski`
  - `Value`: `35, 45, 55, 65, 75, 85, 95`
  - 保留 `Chance 10`, `Cost 5`, `Wait 1`
- `skill/g/gdragon_steps.ski`
  - `Value`: `80, 95, 110, 125, 140, 155, 170`
  - 保留 `Chance 20`, `Cost 15`, `Wait 10`
- `skill/s/sleev_steps.ski`
  - `Value`: `60, 80, 100, 120`
  - 保留 `Chance 20`, `Cost 10`, `Wait 10`
- `skill/s/sky_steps.ski`
  - `Value`: `95, 115, 135, 155, 175, 195`
  - 保留 `Chance 20`, `Cost 10`, `Wait 10`

### Design Notes

- `cloud -> gdragon` 形成明確主鏈梯度
- `sleev -> sky` 補回平行分支梯度，不再讓 `sky` 掛在全 `20` 的 prerequisite 上
- 本批只調 `Value`，刻意不動 `Chance / Wait / Cost / CostType`
- `sky steps` 仍維持相對省體力的高階步法定位，不把它硬拉成全面碾壓 `gdragon`

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- `log/smoke-batch-b.log`
  - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - 尾端 `系統不正常終止` 為 `timeout 50s` 截停後的正常關機
- `debug/*`
  - 無新的 `failenable`
  - 無新的 `failload`
  - `badobject` 為空

### Follow-up

- 已完成城市 / 教學 / 服務 NPC 的 Batch B follow-up 抽查
- `512` 地政官吏與 `572` 郎中已從 `gdragon steps` 回調到 `cloud steps`
- `537`、`538`、`539`、`9003` 目前先保留，因為其主要定位仍是教學 / 店務 / 法術服務
- `570` 詩人已根據 `detect evil` 舊站教學紀錄與 `shade steps` 的 scholar/bard-compatible 定位，從 civic suspect 轉成合理保留
- 已完成城市 / 教學 / 服務 `long fist` sweep：`512` 歸入入門自保；`537`、`570`、`9003` 歸入合理保留；目前沒有新的 long-fist civic mismatch
- 下一個關鍵 decision point 已轉為 Batch C 的 `long fist / lung shan / tackle`

## Batch C Pre-Check

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - 明確給出 `long fist -> lung shan -> tackle`
  - `long fist` 為可互教 root
  - `lung shan` 需要 `long fist >= 心神領會`
  - `tackle` 需要 `lung shan >= 神乎其技`
- `docs/3yWebsite/newhand/newbies/index.html`
  - `long fist` 屬新手最小攻擊技能組的一部分
- `docs/3yWebsite/newhand/players/newplayer/9903151.html`
  - 再次把 `long fist` 放在新手早期 learn baseline
- `docs/3yWebsite/newhand/players/bravo/0104244.html`
  - 把 `long fist -> lung shan -> tackle` 放在刺客拳法路線
- `docs/3yWebsite/newhand/players/general/0104234.html`
  - 把同一條鏈放在將軍拳法路線

### Mandatory Pre-Check Snapshot

`long fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `18`
- value set before rebuild: `20`

`lung shan`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `7`
- value set before rebuild: `20`

`tackle`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `8`
- value set before rebuild: `20`

### Interpretation

- 這條拳法鏈在 `Chance / Parry / Wait / Cost / CostType / Weapon / Check` 上幾乎完全同型
- 目前最明顯被壓平的維度只有 `Value`
- 因此 Batch C 第一輪先只重建 `Value`，保留「空手、耗體、同節奏」的交付型態

## Batch C Result

### Scope

- `long fist`
- `lung shan`
- `tackle`

### Runtime Changes

`long fist`

- before: `20 x 18`
- after: `45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 135`
- average: `87.78`

`lung shan`

- before: `20 x 7`
- after: `100, 115, 130, 145, 160, 180, 205`
- average: `147.86`

`tackle`

- before: `20 x 8`
- after: `140, 160, 180, 200, 220, 240, 260, 290`
- average: `211.25`

### Design Notes

- `long fist` 被重新定位為 starter baseline，不再與中高階拳法共用同模板
- `lung shan` 成為明確高於 `long fist` 的中階拳法主力
- `tackle` 成為這條 legacy 拳法鏈的高階端點
- 本批刻意不動 `Chance / Parry / Wait / Cost / CostType / Weapon / Check`，避免在尚未證明有必要前改變這條鏈的基本手感

### Validation

- `make -C src -f Makefile.lin merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-c.log`
  - `debug/failenable`
  - `debug/failload`
  - `debug/badobject`
  - `debug/error`

### Follow-up

- Batch C 完成後，`long fist` 不再適合被當成「一路撐到高階」的 generic模板
- 但先前已分類的城市 / 教學 / 服務樣本，仍應優先按角色定位而不是單看技能名重判
- 下一步應以 smoke / failenable 結果決定是否需要回頭調整 `512`、`537`、`570`、`9003` 這些 long-fist baseline 樣本

## Batch C Fallout Recheck

### Scope

- `512` 地政官吏
- `537` 訓練師
- `570` 詩人
- `9003` 藥鋪伙計

### Decision

- `512`
  - 保留 `long fist + cloud steps`
  - 但在 Batch C 還原拳法梯度後，`long fist 100` 已不再符合城市文職的入門自保基線
  - 調整為 `long fist 70 + cloud steps 70`
- `537`
  - 維持 `long fist 100 + gdragon steps 100`
  - `NoKill` 訓練師樣本，不屬可被玩家擊倒的城市自保樣本
- `570`
  - 保留 `long fist + shade steps`
  - `detect evil` 舊站教學來源與 `shade steps` 的 scholar / bard 相容性仍支持其 flavor
  - 但在 Batch C 後，`long fist 100` 對詩人樣本偏高，因此回調為 `long fist 70 + shade steps 100`
- `9003`
  - 維持 `long fist 100 + gdragon steps 100`
  - `NoKill` 服務樣本，先不因拳法梯度回升而重寫其固定 enable

### Interpretation

- 這一輪 fallout 的核心不是把 `long fist` 從城市 / 教學 / 服務樣本全面移除，而是把 killable civic sample 從「過高熟練度的 starter baseline」拉回合理區間
- `512`、`570` 都屬 `adept rollback`，不是身份鏈重寫
- `537`、`9003` 目前仍可視為 `NoKill` 服務樣本的合理保留，後續只有在同批再出現 failenable / runtime 問題時才需要重審

## Batch D Pre-Check

### Scope

- `shoot sun`
- `water cloud blast`
- `fun wu blast`

### Reference Basis

- `docs/3yWebsite/skill/bow.html`
  - 明確給出 `shoot sun -> water cloud blast -> fun wu blast`
  - 並保留完整職業 / 屬性 / 前置熟練度限制
- `docs/3yWebsite/newhand/players/general/0104234.html`
  - 將軍文明確把這條鏈當成弓法主線
  - `shoot sun`
    - `LV10、敏捷10`
    - 建議等級 `LV50`
    - 特性：可連擊
  - `water cloud blast`
    - `LV10、敏捷15、力量15、shoot sun 出類拔萃`
    - 建議等級 `LV70`
    - 特性：自動連擊
  - `fun wu blast`
    - `LV50、敏捷35、力量25、體格25、water cloud blast 出神入化`
    - 建議等級 `LV90`
    - 特性：自動連擊 3 到 5 下、花費體力少、威力強大

### Mandatory Pre-Check Snapshot

`shoot sun`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `WEAPON_BOW / check_bow_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `7`
- value set before rebuild: `20`

`water cloud blast`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 15`
- weapon / check: `WEAPON_BOW / check_bow_attack`
- runtime file has no `#Damage`
- actual damage path: `src/spell.c -> cast_water_cloud_blast()`
- code-side base damage ladder before weapon multiplier: `300, 350, 400, 450, 500, 600, 700, 800, 900, 1000`
- repeat loop: `for (tt = 0; tt <= level / 33; tt++)`

`fun wu blast`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 15`
- weapon / check: `WEAPON_BOW / check_bow_attack`
- runtime file has no `#Damage`
- actual damage path: `src/spell.c -> cast_fun_wu_blast()`
- code-side base damage ladder before weapon multiplier: `450, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1400`
- repeat loop: `for (tt = 0; tt <= level / 20; tt++)`

### Interpretation

- 這條弓法鏈不是和 Batch A / B / C 一樣的純 `#Damage Value` 清值問題
- 只有 `shoot sun` 仍依賴 `.ski` 內的 `#Damage`
- `water cloud blast` 與 `fun wu blast` 雖然 skill 檔沒有 `#Damage`，但不是殘缺；它們主要靠 `spell.c` 的專屬函式與 bow weapon multiplier 出傷
- 因此 Batch D 不應把後兩者硬補成假 `#Damage` 模板
- 這一批更合理的修法是：
  - 把 `shoot sun` 補回合理 root-template
  - 把 `water cloud blast / fun wu blast` 明確記為 `code-driven offensive exception`

## Batch D Result

### Runtime Changes

`shoot sun`

- before: `20, 20, 20, 20, 20, 20, 20`
- after: `80, 95, 110, 125, 140, 160, 180`
- average: `127.14`

### Design Notes

- `shoot sun` 重新站穩弓法 root 的 offensive template，不再是全 `20` 的系統性清值殘留
- `water cloud blast` 與 `fun wu blast` 本輪不改 skill data
- 這不是漏修，而是根據 source pre-check 的刻意保留：
  - 兩者真正的 ladder 已存在於 `spell.c`
  - 再往 `.ski` 補假 `#Damage` 反而會混淆 loader / runtime 邏輯
- 因此 Batch D 的輸出是：
  - 一筆 root-template 修復
  - 一筆對 `code-driven bow ladder` 的明確建模

### Validation

- `make -C src -f Makefile.lin merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-d.log`
  - `debug/failenable`
  - `debug/failload`
  - `debug/badobject`
  - `debug/error`

## Batch E Pre-Check

### Scope

- `her blade`
- `dragon blade`
- `tiger blade`

### Reference Basis

- `docs/3yWebsite/skill/blade.html`
  - 明確給出 `her blade -> dragon blade -> tiger blade`
  - 並保留完整職業 / 屬性 / 前置熟練度限制
- `docs/3yWebsite/newhand/players/general/0104232.html`
  - 將軍文明確把這條鏈列為主線刀法
  - `her blade`
    - `LV10`
    - 建議等級 `LV10`
    - 特性：可連擊、初期所用刀法
  - `dragon blade`
    - `LV10、力量15、her blade 心神領會`
    - 建議等級 `LV100`
  - `tiger blade`
    - `LV50、敏捷20、力量25、dragon blade 登峰造極`
    - 建議等級 `LV100`
    - 特性：威力強大，攻傷 `1600~5500`

### Mandatory Pre-Check Snapshot

`her blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 8`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `10`
- parry set: `0`
- damage entries: `8`
- value set before rebuild: `20`

`dragon blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 14`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `9`
- value set before rebuild: `20`

`tiger blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 18`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `10`
- value set before rebuild: `20`

### Interpretation

- 這條鏈的 `weapon_identity`、`tempo` 與 `resource profile` 已經保留出明顯差異
- `her blade`
  - 入門、較快、較省
- `dragon blade`
  - 更慢，但仍維持中階成本
- `tiger blade`
  - 最慢、最耗體、而且舊站文案直接明指「威力強大」
- 因此本批和 Batch C 類似，核心問題仍是 `Value` 被系統性壓平
- 修法應維持：
  - `her blade` 站穩 starter / early-general blade root
  - `dragon blade` 成為清楚中階主力
  - `tiger blade` 承接高威力、大刀、重成本定位

## Batch E Result

### Runtime Changes

`her blade`

- before: `20 x 8`
- after: `75, 90, 105, 120, 135, 150, 165, 185`
- average: `128.13`

`dragon blade`

- before: `20 x 9`
- after: `140, 160, 180, 200, 220, 240, 260, 285, 315`
- average: `222.22`

`tiger blade`

- before: `20 x 10`
- after: `240, 270, 300, 330, 360, 400, 440, 480, 520, 580`
- average: `392.0`

### Design Notes

- 本批只調 `Value`，刻意保留原本的大刀手感差異：
  - `her blade` 仍是比較快、比較省的 early blade
  - `dragon blade` 用更長 `Wait` 換更高單段輸出
  - `tiger blade` 以 `Cost 30 / Wait 18` 承接真正的高階重兵爆發
- 這樣的梯度也較符合舊站對 `tiger blade`「威力強大」的文字定位

### Validation

- `make -C src -f Makefile.lin merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-e.log`
  - `debug/failenable`
  - `debug/failload`

## Batch E Fallout Recheck

### Scope

- `area/loyang/mob/604.mob`

### Result

- `604` `six demon king`
  - 保留 `tiger blade 100`
  - 保留 `mirage steps 100`
  - 不做 runtime 變更

### Why Keep

- 這不是 civic / teacher / service 樣本，而是 loyang 地下水區的 named high-tier special
- `tiger blade` 在 Batch E 後已恢復成符合舊站描述的高威力重刀模板
- `mirage steps` 在同區還有 `598-601` 這批 high-tier 樣本共同使用，較像 cluster 設計，而非單點錯配
- 因此這筆 fallout recheck 的結論是「收斂 audit 判定」，不是「回調 adept」

### Validation

- docs-only fallout decision
- `docs/current-game/skill-combat-audit.json` JSON parse should remain clean

## Batch F Pre-Check

### Scope

- `dream blade`
- `sea flow blade`
- `fast blade`

### Reference Basis

- `docs/3yWebsite/skill/blade.html`
  - 明確給出 `dream blade -> sea flow blade -> fast blade`
  - 保留完整職業 / 屬性 / 前置熟練度限制
- `docs/3yWebsite/newhand/players/general/0104232.html`
  - 將軍文把這條鏈列成另一條主力刀法線
  - `dream blade`
    - 建議等級 `LV30`
  - `sea flow blade`
    - 建議等級 `LV50`
  - `fast blade`
    - 建議等級 `LV80`
    - 特性：可連擊、威力強大

### Mandatory Pre-Check Snapshot

`dream blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `25 / COST_MOVE / 15`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `9`
- value set before rebuild: `20`

`sea flow blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `25 / COST_MOVE / 12`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `8`
- value set before rebuild: `20`

`fast blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 11`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- chance set: `20`
- parry set: `0`
- damage entries: `22`
- value set before rebuild: `20`

### Pre-Check Conclusion

- 三者共通的 distortion 仍是 `Value` 被系統性壓成 `20`
- 但節奏並沒有同質：
  - `dream blade` 最慢，應保留成華麗中階 root
  - `sea flow blade` 較快，作為中高階銜接段
  - `fast blade` 最多段、最快之一，而且舊站直接寫它可連擊、威力強大
- 所以本批仍以「只重建 `Value`」為主，不動 `Chance / Parry / Wait / Cost / CostType / Weapon / Check`

## Batch F Result

### Runtime Changes

`dream blade`

- before: `20 x 9`
- after: `95, 115, 135, 155, 175, 195, 215, 240, 270`
- average: `176.67`

`sea flow blade`

- before: `20 x 8`
- after: `140, 165, 190, 215, 240, 265, 290, 325`
- average: `228.75`

`fast blade`

- before: `20 x 22`
- after: `190, 205, 220, 235, 250, 265, 280, 295, 310, 325, 340, 355, 370, 385, 400, 420, 440, 460, 480, 500, 520, 550`
- average: `355.0`

### Design Notes

- 本批只調 `Value`，保留原本的華麗快刀節奏差異：
  - `dream blade` 仍偏慢，維持高等 root 的鋪陳感
  - `sea flow blade` 以較短 `Wait` 承接中高階主力
  - `fast blade` 用最多 damage entries 和更高 `Value` 承接「可連擊、威力強大」定位
- 這樣也避免把 `fast blade` 修成和 `tiger blade` 一樣的重刀手感

### Validation

- `make -C src -f Makefile.lin merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-f.log`
  - `debug/failenable`
  - `debug/failload`
  - `debug/badobject`
  - `debug/error`

## Batch G Pre-Check

### Scope

- `shade steps`
- `wind steps`
- `mirage steps`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/step.html`
  - 明確給出 `shade steps -> wind steps`
  - 明確給出 `gdragon steps -> mirage steps`
  - `wind steps` 是 thief-only 的高階步法
  - `mirage steps` 是 `gdragon` 的高階延伸，不是獨立 root
- `/Users/jakeuj/auggie/3yWebsite/newhand/players/bravo/0104243.html`
  - 把 `cloud steps`、`gdragon steps`、`mirage steps` 放在同一套步法路線中
- `/Users/jakeuj/auggie/3yWebsite/newhand/players/general/0104233.html`
  - 將軍文也保留 `mirage steps`，支撐它不是單一職業外掛技能
- runtime `skill/*.ski`
  - `shade_steps.ski`
    - `Associate SLOT_WIND_STEPS`
  - `wind_steps.ski`
    - `Associate -1`
  - `gdragon_steps.ski`
    - Batch B 已重建
  - `mirage_steps.ski`
    - `Associate -1`

### Mandatory Pre-Check Snapshot

`shade steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- canask / teach: `YES / NO`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`wind steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- canask / teach: `NO / NO`
- damage entries: `8`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`mirage steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- canask / teach: `YES / NO`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- `shade -> wind` 與 `gdragon -> mirage` 都是舊站與 runtime 可交叉確認的玩家向步法鏈。
- 這三個 skill 的 `Cost / Wait / CostType` 幾乎完全同型，表示本輪最明顯的 distortion 仍是 `Value` 被系統性壓平成 `20`。
- `mirage steps` 是 Batch B 已完成 `gdragon` 主鏈的自然延伸；若不補上，`gdragon` 的高階端點仍會停在清值殘留模板。
- `shade -> wind` 則補齊另一條 thief-oriented 閃躲分支，避免目前 repo 只修到 `cloud/gdragon` 與 `sleev/sky`，卻留下同樣全 `20` 的另一條玩家向步法鏈。
- mob 端目前只看到：
  - `mirage steps` 被 loyang 高階 named 樣本 `598 / 599 / 600 / 601 / 604` 掛用
  - `shade steps` 僅 `570` 詩人固定啟用
  - `wind steps` 目前沒有現成 mob enable
- 因此本批仍先只修 skill template，不先動 mob runtime data。

## Batch G Result

### Scope

- `shade steps`
- `wind steps`
- `mirage steps`

### Runtime Changes

`shade steps`

- before: `20 x 7`
- after: `60, 75, 90, 105, 120, 135, 150`
- average: `105.0`

`wind steps`

- before: `20 x 8`
- after: `90, 110, 130, 150, 170, 190, 210, 235`
- average: `160.62`

`mirage steps`

- before: `20 x 7`
- after: `115, 135, 155, 175, 195, 215, 240`
- average: `175.71`

### Design Notes

- 本批只調 `Value`，刻意保留 `Chance / Wait / Cost / CostType` 不變，讓這輪仍屬純 dodge template 重建。
- `shade steps` 被重新定位為另一條玩家向 root-step baseline，不再是和高階分支共用全 `20` 模板。
- `wind steps` 以 thief-only 高階步法定位，明確高於 `shade steps`，但不靠額外減 cost 或縮 wait 來改手感。
- `mirage steps` 承接 Batch B 已重建的 `gdragon` 高階端，站穩高階 dodge branch，而不是讓已修復的前置技能接到清值終點。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-g.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch L Pre-Check

### Scope

- `young gun`
- `eight gun`
- `gwhip`
- `ming snake`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/lance.html`
  - 明確給出 `young gun -> eight gun`
- `/Users/jakeuj/auggie/3yWebsite/skill/whip.html`
  - 明確給出 `gwhip -> ming snake`
- `docs/current-game/skills/lance.md`
  - current-game 已把 `young gun -> eight gun` 整理成 `legacy-page:lance`
- `docs/current-game/skills/whip.md`
  - current-game 已把 `gwhip -> ming snake` 整理成 `legacy-page:whip`

### Mandatory Pre-Check Snapshot

`young gun`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 14`
- weapon / check: `WEAPON_SPEAR / check_spear_attack`
- canask / teach / valid: `NO / NO / YES`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`eight gun`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 17`
- weapon / check: `WEAPON_SPEAR / check_spear_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`gwhip`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_WHIP / check_whip_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `11`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`ming snake`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_WHIP / check_whip_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這批收的是兩條短鏈，且四招都仍屬現行可用的玩家向 runtime 技能，不是封存鏈。
- `young gun -> eight gun` 保留明顯的重槍遞進：
  - `young gun` 已經不算快，但仍是可承接的 root
  - `eight gun` 更慢、更重、也應有更明顯的高階單段輸出
- `gwhip -> ming snake` 則同為 `Cost 15 / Wait 10`，但 `ming snake` 有更嚴格的 prerequisite，應在相同節奏下靠更高 `Value` 站穩高階定位。
- area `*.mob` 目前未看到這四招的現成 `Enable` 樣本，因此本批先不做 mob fallout。

## Batch L Result

### Scope

- `young gun`
- `eight gun`
- `gwhip`
- `ming snake`

### Runtime Changes

`young gun`

- before: `20 x 7`
- after: `90, 110, 130, 150, 170, 195, 220`
- average: `152.14`

`eight gun`

- before: `20 x 9`
- after: `170, 195, 220, 245, 270, 300, 335, 375, 420`
- average: `281.11`

`gwhip`

- before: `20 x 11`
- after: `85, 100, 115, 130, 145, 160, 180, 200, 220, 245, 270`
- average: `168.18`

`ming snake`

- before: `20 x 8`
- after: `120, 140, 160, 180, 205, 230, 260, 295`
- average: `198.75`

### Design Notes

- 本批仍只調 `Value`，保留槍與鞭兩條鏈既有的武器 identity 與節奏。
- `young gun -> eight gun` 用更高成本、更慢節奏與更高單段值站穩高階槍法差距。
- `gwhip -> ming snake` 則在同節奏前提下，透過 `Value` 階梯重建高階鞭法的進化感。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-l.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch K Pre-Check

### Scope

- `ghost axe`
- `tiger axe`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/axe.html`
  - 明確給出 `ghost axe -> tiger axe`
  - `tiger axe` 以 `ghost axe` 為 prerequisite
- `docs/current-game/skills/axe.md`
  - current-game 已把這條鏈整理成 `legacy-page:axe`
  - runtime 仍顯示兩者 damage values 幾乎全 `20`
- runtime `skill/*.ski`
  - `ghost_axe.ski`
    - `Associate SLOT_TIGER_AXE`
    - `CanAsk YES / Teach YES / Valid YES`
  - `tiger_axe.ski`
    - `Associate -1`
    - `CanAsk YES / Teach NO / Valid YES`

### Mandatory Pre-Check Snapshot

`ghost axe`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 15`
- weapon / check: `WEAPON_AXE / check_axe_attack`
- canask / teach / valid: `YES / YES / YES`
- damage entries: `6`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`tiger axe`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `35 / COST_MOVE / 18`
- weapon / check: `WEAPON_AXE / check_axe_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `13`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條 axe 鏈和最近幾批最大的不同，是它目前仍屬真正可 ask / teach 的玩家向 runtime 技能，不是封存鏈。
- 兩者在 `Chance`、`Weapon`、`Check` 上同型，但 `tiger axe` 本來就更重、更慢、段數也更多，因此本批最合理的修法仍是只重建 `Value`，保留既有重兵節奏。
- `ghost axe` 站穩高成本 root，`tiger axe` 則承接高階重斧終點。
- area `*.mob` 目前未看到這兩招的現成 `Enable` 樣本，因此本批先不做 mob fallout。

## Batch K Result

### Scope

- `ghost axe`
- `tiger axe`

### Runtime Changes

`ghost axe`

- before: `20 x 6`
- after: `95, 115, 135, 155, 180, 210`
- average: `148.33`

`tiger axe`

- before: `20 x 13`
- after: `180, 205, 230, 255, 280, 305, 335, 365, 400, 440, 485, 540, 600`
- average: `355.38`

### Design Notes

- 本批只調 `Value`，刻意保留 axe 鏈既有的高成本、慢節奏與重兵器手感。
- `ghost axe` 不再是全 `20` 的假 root，而是能成立為高成本玩家向入門斧法。
- `tiger axe` 以更多段數與更高平均值承接真正的高階重斧端點，不必再靠額外調整 `Wait / Cost` 來硬做差距。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-k.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch J Pre-Check

### Scope

- `bad sword`
- `wumin sword`
- `noname`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/sword.html`
  - 明確給出 `bad sword -> wumin sword -> noname`
  - `wumin sword` 以 `bad sword` 為 prerequisite
  - `noname` 以 `wumin sword` 為 prerequisite
- `docs/current-game/skills/sword.md`
  - current-game 已把這條鏈整理在 `legacy-page:sword`
  - 三者目前 damage values 仍是全 `20`
- runtime `skill/*.ski`
  - `badsword.ski`
    - `Wait 1`
    - `Valid NO / CanAsk NO`
  - `wumin_sword.ski`
    - `Wait 12`
    - `Valid NO / CanAsk NO`
  - `noname.ski`
    - `Wait 10`
    - `Valid NO / CanAsk NO`

### Mandatory Pre-Check Snapshot

`bad sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`wumin sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 12`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`noname`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈和 Batch I 類似，是 old-site 玩家鏈清楚、但 runtime 目前保留為封存/不可 ask 的 legacy 劍法組。
- 本輪先做 combat template 重建，不在這批把 `Valid / CanAsk / Teach` 的 runtime 開放政策一起重寫。
- 三者共通的 distortion 很明顯是 `Value` 被壓平；但節奏仍有差異：
  - `bad sword` 是 `Wait 1` 的快劍 root
  - `wumin sword` 最慢，較像重型中階主力
  - `noname` 稍快於 `wumin`，但作為終點應保留更高單段強度
- area `*.mob` 目前未看到這三招的現成 `Enable` 樣本，因此本批先不做 mob fallout。

## Batch J Result

### Scope

- `bad sword`
- `wumin sword`
- `noname`

### Runtime Changes

`bad sword`

- before: `20 x 8`
- after: `60, 75, 90, 105, 120, 140, 160, 185`
- average: `116.88`

`wumin sword`

- before: `20 x 9`
- after: `115, 135, 155, 175, 195, 220, 245, 275, 310`
- average: `202.78`

`noname`

- before: `20 x 9`
- after: `155, 175, 195, 215, 235, 260, 290, 325, 360`
- average: `245.56`

### Design Notes

- 本批仍只調 `Value`，把 runtime 封存狀態和舊站玩家鏈的 combat template 重建分開處理。
- `bad sword` 保留 `Wait 1` 的快劍 root 身分，因此雖然輸出回升，仍刻意壓在後兩段之下。
- `wumin sword` 用更高單段值配合 `Wait 12`，站穩中階 heavy sword 段位。
- `noname` 以略短於 `wumin` 的節奏承接終點模板，但仍維持這條鏈最高的平均與峰值。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-j.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch H Pre-Check

### Scope

- `nine steps`
- `color steps`
- `cloud ghost`
- `wind color steps`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/step.html`
  - 明確給出 `nine steps -> color steps`
  - 明確給出 `cloud ghost -> wind color steps`
  - `wind color steps` 不是 `color steps` 的直升下一段，而是另一條文士/醫者/天師系 branch
- `/Users/jakeuj/auggie/3yWebsite/newhand/players/bard/0106121.html`
  - 明確列出 `cloud ghost` 與 `wind color steps`
- `/Users/jakeuj/auggie/3yWebsite/newhand/players/newplayer/9904101.html`
  - 直接寫出 `cloud ghost` 可領悟 `wind color steps`
- runtime `skill/*.ski`
  - `nine_step.ski`
    - `Associate SLOT_COLOR_STEPS`
  - `color_steps.ski`
    - `Associate -1`
  - `cloud_ghost.ski`
    - `Associate SLOT_WINDCOLOR_STEPS`
  - `windcolor_steps.ski`
    - `Associate -1`

### Mandatory Pre-Check Snapshot

`nine steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `5 / COST_MOVE / 1`
- canask / teach: `YES / NO`
- damage entries: `8`
- chance set: `10`
- runtime raw value lines before rebuild: `20, 20, 20, 100, 20, 20, 20, 20, 20`
- parry set: `0`

`color steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `10 / COST_MOVE / 5`
- canask / teach: `YES / NO`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`cloud ghost`

- type: `TAR_DODGE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- canask / teach: `YES / NO`
- damage entries: `6`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`wind color steps`

- type: `TAR_DODGE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- canask / teach: `NO / NO`
- damage entries: `6`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這一批不是單一鏈，而是兩條平行玩家向步法鏈：
  - `nine -> color`
  - `cloud ghost -> wind color`
- `nine steps` 的 raw file 內有一筆重複 `Value`，形成單筆 `100` 異常值；這看起來不像完整 ladder，而更像未完成的局部人工殘改。
- 因此這批不能把 `nine steps` 誤判成「其實已經有設計好的高點」，而應把它視為：
  - 大體仍被清值壓平
  - 但帶著一筆需要被整理回一致梯度的噪音點
- 兩條鏈在 `Cost / Wait / CostType` 上本來就保留差異：
  - `nine steps` 是低成本、高頻 root
  - `color steps` 是較慢、較貴的進階延伸
  - `cloud ghost` 與 `wind color steps` 同為較重節奏的文士系 branch
- mob / teacher 端目前只看到：
  - `area/loyang/mob/539.mob` 有 `#Learn 'nine steps'`
  - `area/loyang/mob/583.mob` 固定 `Enable 100 'color steps'`
  - 目前未看到 `cloud ghost` 或 `wind color steps` 的現成 mob enable
- 因此本批仍先修 skill template，不先動 mob runtime data。

## Batch H Result

### Scope

- `nine steps`
- `color steps`
- `cloud ghost`
- `wind color steps`

### Runtime Changes

`nine steps`

- before: `20, 20, 100, 20, 20, 20, 20, 20` with one duplicated raw `Value 20` line in file
- after: `45, 55, 65, 80, 95, 110, 125, 145`
- average: `90.0`

`color steps`

- before: `20 x 7`
- after: `80, 95, 110, 125, 140, 160, 180`
- average: `127.14`

`cloud ghost`

- before: `20 x 6`
- after: `70, 90, 110, 130, 150, 170`
- average: `120.0`

`wind color steps`

- before: `20 x 6`
- after: `110, 130, 150, 170, 190, 215`
- average: `160.83`

### Design Notes

- `nine steps` 這輪不只是加值，也順手把單筆 `100` 異常整理回一條可讀的 root ladder。
- `color steps` 以較高成本 / 較慢節奏承接 `nine steps` 的進階段，不需要靠額外改 `Wait` 來證明定位。
- `cloud ghost -> wind color steps` 則維持文士系 branch 的重節奏特色，只用 `Value` 重建高階差距。
- 這樣可以同時保留：
  - `nine` 系的低成本高頻
  - `cloud ghost` 系的較重詩意步法節奏
  - 兩條 branch 不被錯誤地壓成同一種 dodge template

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-h.log`
    - 未到 `三國歪傳之降龍伏虎開始正常運作`
    - 啟動期被 `Load_object﹕命令 Keywords 不正確`
    - 指向 `/area/sec_rift_core_below/obj/11353.obj`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

### Validation Status

- 後續 recheck 已通過
- 最新 smoke recheck:
  - `log/smoke-recheck.log`
  - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - 無 `Load_object` / `Keywords 不正確`
  - `debug/failenable`、`debug/failload`、`debug/badobject`、`debug/error` 無新增內容

## Batch I Pre-Check

### Scope

- `sun blade`
- `ice blade`
- `gold blade`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/blade.html`
  - 明確給出 `sun blade -> ice blade -> gold blade`
  - `sun blade` 是可互教 root
  - `ice blade` 與 `gold blade` 都是其後續高階延伸
- `docs/current-game/skills/blade.md`
  - current-game 已把這條鏈整理成 `legacy-page:blade` 的第三條主線
  - runtime 目前仍顯示 `sun / ice / gold` 的 damage values 幾乎全 `20`
- runtime `skill/*.ski`
  - `sun_blade.ski`
    - `Associate -1`
    - `Valid NO / CanAsk NO`
  - `iceblade.ski`
    - `Associate -1`
    - `Valid NO / CanAsk NO`
  - `gold_blade.ski`
    - `Associate -1`
    - `Valid NO / CanAsk NO`

### Mandatory Pre-Check Snapshot

`sun blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `6`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`ice blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`gold blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `10`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈的舊站玩家向 progression 很清楚，但 runtime 目前保留的是「可 enable、不可 ask/teach/valid」的遺留狀態。
- 本輪先處理的是 combat template，不是技能開放政策；因此只修 `Value`，不在這批直接改 `Valid / CanAsk / Teach`。
- 三者在 `Chance / Parry / Weapon / Check` 上幾乎同型，且 `sun blade` 的 `Wait 1` 明顯保留了入門快刀特色；因此梯度主軸應是：
  - `sun blade` 維持低成本高頻 root
  - `ice blade` 站穩中高階主力
  - `gold blade` 成為這條 legacy 刀法鏈的終點
- area `*.mob` 目前未看到這三招的現成 `Enable` 樣本，因此本批優先以玩家向 ladder 重建為主，不做 mob fallout。

## Batch I Result

### Scope

- `sun blade`
- `ice blade`
- `gold blade`

### Runtime Changes

`sun blade`

- before: `20 x 6`
- after: `55, 70, 85, 100, 115, 130`
- average: `92.5`

`ice blade`

- before: `20 x 9`
- after: `110, 130, 150, 170, 190, 210, 235, 260, 290`
- average: `193.89`

`gold blade`

- before: `20 x 10`
- after: `150, 170, 190, 210, 230, 255, 280, 305, 335, 370`
- average: `249.5`

### Design Notes

- 本批仍只調 `Value`，不把 runtime 目前的 `Valid NO` 遺留狀態和 combat ladder 重建混在同一輪處理。
- `sun blade` 保留 `Wait 1` 的快刀 root 身分，因此雖然平均值回升，仍刻意壓在同頁其他重刀高階模板之下。
- `ice blade` 與 `gold blade` 同為 `Cost 15 / Wait 10`，但以更高的 `Value` 階段承接明顯的中高階與終點差距。
- 這樣可以先把 old-site clear chain 的 combat template 拉回可用，再決定是否另開一輪處理 `Valid / CanAsk / Teach` 的 runtime policy。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-i.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容
