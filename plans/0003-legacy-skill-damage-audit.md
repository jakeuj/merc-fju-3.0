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

- `status = batch_as_implemented`
- `current_focus = next legacy attack ladder`
- `current_batch = Batch AS implemented`

## Immediate Next Steps

1. 下一個高價值候選可續盤剩餘單點技能，優先可看 `cry ghost / dream dance / drunk` 之後的其餘孤立 high-tier attack skill
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

## Batch P Pre-Check

### Scope

- `know pen`
- `write pen`
- `eten dragon`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/fan.html`
  - 明確給出 `know pen -> write pen -> eten dragon`
  - `write pen` 以 `know pen` 為 prerequisite
  - `eten dragon` 以 `write pen` 為 prerequisite
- `docs/current-game/skills/fan.md`
  - current-game 已把這條鏈整理成 `legacy-page:fan` 內目前唯一有完整 runtime 對應的筆扇主線
  - 三者目前 damage values 皆為全 `20`
- runtime `skill/*.ski`
  - `know_pen.ski`
    - `Associate SLOT_WRITE_PEN`
    - `CanAsk YES / Teach YES / Valid YES / Enable YES`
  - `write_pen.ski`
    - `Associate SLOT_ETEN`
    - `CanAsk YES / Valid YES / Enable YES`
  - `eten.ski`
    - `Associate -1`
    - `CanAsk NO / Valid YES / Enable YES`

### Mandatory Pre-Check Snapshot

`know pen`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `19 / COST_MOVE / 12`
- weapon / check: `WEAPON_PEN / check_pen_attack`
- canask / teach / valid: `YES / YES / YES`
- damage entries: `4`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`write pen`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `19 / COST_MOVE / 12`
- weapon / check: `WEAPON_PEN / check_pen_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `13`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`eten dragon`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `19 / COST_MOVE / 10`
- weapon / check: `WEAPON_PEN / check_pen_attack`
- canask / teach / valid: `NO / NO / YES`
- damage entries: `6`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Representative Runtime Consumers

- 目前未看到 `know pen`、`write pen`、`eten dragon` 的現成 `Enable` / `AutoEnable` / `#Learn` 樣本
- `area/limbo/obj/238.obj`
  - `know pen book`
- `area/limbo/obj/393.obj`
  - `write pen book`

### Interpretation

- 這條筆扇鏈是舊站與 current-game/runtime 都能直接對照的玩家向主鏈。
- `know pen` 與 `write pen` 同為 `Cost 19 / Wait 12`，最明顯被壓平的仍是 `Value`；`write pen` 靠更多段數與 prerequisite 承接中高階。
- `eten dragon` 雖然目前 `CanAsk NO`，但 runtime 仍為 `Valid YES / Enable YES`，因此本批先處理 combat template，不混入開放政策。
- 因為這批目前沒看到 mob-side wiring，驗證重點會放在 build / smoke 是否乾淨，以及避免把文人系筆扇鏈硬拉成失去節奏差異的純重兵模板。

## Batch P Result

### Scope

- `know pen`
- `write pen`
- `eten dragon`

### Runtime Changes

`know pen`

- before: `20 x 4`
- after: `75, 90, 105, 125`
- average: `98.75`

`write pen`

- before: `20 x 13`
- after: `95, 105, 115, 125, 135, 145, 155, 165, 180, 195, 210, 230, 255`
- average: `162.69`

`eten dragon`

- before: `20 x 6`
- after: `170, 200, 230, 265, 305, 350`
- average: `253.33`

### Design Notes

- 本批只調 `Value`，保留筆扇鏈既有的文人系節奏、武器 identity 與 prerequisite 結構。
- `know pen` 回到可成立的 root，不再只是全 `20` 的教學殼。
- `write pen` 以大量段數與穩定 `Chance 20` 站穩中階主體；`eten dragon` 再以更高單段值與較短 `Wait 10` 站穩 endpoint。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-p.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch O Pre-Check

### Scope

- `universe`
- `six fire`
- `fire dragon`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/energy.html`
  - 明確給出 `universe -> six fire -> fire dragon`
  - `six fire` 以 `universe` 為 prerequisite
  - `fire dragon` 以 `six fire` 為 prerequisite
- `docs/current-game/skills/force.md`
  - current-game 已把這條鏈整理成 `legacy-page:energy`
  - runtime 目前顯示三者 damage values 皆為全 `20`
- runtime `skill/*.ski`
  - `universe.ski`
    - `Associate SLOT_SIXFIRE`
    - `CanAsk YES / Valid YES / Enable YES`
  - `sixfire.ski`
    - `Associate SLOT_FIRE_DRAGON`
    - `CanAsk YES / Valid YES / Enable YES`
  - `fire_dragon.ski`
    - `Associate -1`
    - `CanAsk YES / Valid YES / Enable YES`

### Mandatory Pre-Check Snapshot

`universe`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`six fire`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `25 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `6`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`fire dragon`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 7`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `9`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Representative Runtime Consumers

- `area/loyang/mob/583.mob`
  - `Enable 100 'universe'`
- `area/loyang/mob/558.mob`
  - `Enable 75 'fire dragon'`
- 目前未看到 `six fire` 的現成 mob enable / `#Learn` 樣本

### Interpretation

- 這條氣功鏈是很典型的玩家向空手 progression，舊站與 current-game/runtime 都能直接互證。
- 三招在 `Chance / Parry / Check` 上幾乎完全同型，節奏則從 `Wait 5` 漸進到 `Wait 7`，最明顯被壓平的維度就是 `Value`。
- `universe` 仍要成立為可用的 root，不應因為是前置功法就被壓成假模板；`six fire` 與 `fire dragon` 則要在更高 cost 與 prerequisite 下站穩中高階與終點差距。
- 由於 loyang 現成 mob 已掛用 `universe` 與 `fire dragon`，本批會在驗證時特別留意 debug，但仍先只修 skill template，不在這輪直接改 mob runtime data。

## Batch O Result

### Scope

- `universe`
- `six fire`
- `fire dragon`

### Runtime Changes

`universe`

- before: `20 x 7`
- after: `70, 85, 100, 115, 130, 150, 170`
- average: `117.14`

`six fire`

- before: `20 x 6`
- after: `140, 160, 180, 205, 230, 260`
- average: `195.83`

`fire dragon`

- before: `20 x 9`
- after: `220, 250, 280, 310, 340, 375, 415, 460, 520`
- average: `352.22`

### Design Notes

- 本批只調 `Value`，保留空手氣功鏈原本的 `Wait / Cost / Check` 身分。
- `universe` 不再是全 `20` 的前置殼，而是能成立的高階 root。
- `six fire` 以更重的輸出階段承接 `universe`，`fire dragon` 則拉開明顯的終點爆發，對齊舊站的高階氣功定位。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-o.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch N Pre-Check

### Scope

- `be needle`
- `seven dagger`
- `dragon dagger`
- `rain throwing`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/dagger.html`
  - 明確給出 `be needle -> seven dagger`
  - 明確給出 `dragon dagger -> rain throwing`
  - `seven dagger` 與 `rain throwing` 都是各自 root 的 prerequisite 後續段
- `docs/current-game/skills/short.md`
  - current-game 已把這兩條鏈整理成 `legacy-page:dagger`
  - 四招目前 damage values 皆為全 `20`
- runtime `skill/*.ski`
  - `be_needle.ski`
    - `Associate SLOT_SEVEN_DAGGER`
    - `CanAsk YES / Valid YES / Enable YES`
  - `seven_dagger.ski`
    - `Associate -1`
    - `CanAsk YES / Valid YES / Enable YES`
  - `dragon_dagger.ski`
    - `Associate -1`
    - `Valid NO / CanAsk NO / Enable YES`
  - `rain_throwing.ski`
    - `Associate -1`
    - `Valid NO / CanAsk NO / Enable YES`

### Mandatory Pre-Check Snapshot

`be needle`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 2`
- weapon / check: `WEAPON_DAGGER / check_dagger_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `12`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`seven dagger`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 3`
- weapon / check: `WEAPON_DAGGER / check_dagger_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `13`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`dragon dagger`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_DAGGER / check_dagger_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `5`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`rain throwing`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `WEAPON_DAGGER / check_dagger_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `6`
- chance set: `10, 20, 20, 10, 10, 10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這一批不是單一鏈，而是短兵頁上兩條清楚的玩家向 legacy chain。
- `be needle -> seven dagger` 兩者都仍屬現行可 ask 的玩家技能，且 `Wait 2 / 3`、`Cost 20` 很接近，最明顯被壓平的就是 `Value`。
- `dragon dagger -> rain throwing` 則屬目前 runtime 保留為 `Enable YES`、但 `Valid/CanAsk NO` 的封存鏈；本批仍只修 combat template，不混入開放政策。
- `rain throwing` 雖然 `Wait 1`、`Cost 10`，仍是 prerequisite 後的 endpoint；因此應保留高速投擲 identity，但不能再和 `dragon dagger` 同樣維持全 `20`。
- area `*.mob` 與 `#Learn` 目前未看到這四招的現成 runtime enable 樣本，因此本批仍先修 skill template，不先動 mob fallout。

## Batch N Result

### Scope

- `be needle`
- `seven dagger`
- `dragon dagger`
- `rain throwing`

### Runtime Changes

`be needle`

- before: `20 x 12`
- after: `55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120`
- average: `83.75`

`seven dagger`

- before: `20 x 13`
- after: `90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210, 230`
- average: `152.69`

`dragon dagger`

- before: `20 x 5`
- after: `105, 125, 145, 165, 190`
- average: `146.0`

`rain throwing`

- before: `20 x 6`
- after: `135, 155, 175, 195, 220, 250`
- average: `188.33`

### Design Notes

- 本批仍只調 `Value`，保留短兵頁原有的高頻、輕兵與投擲感。
- `be needle -> seven dagger` 重新建立快節奏短兵從高頻 root 到高階針訣的階梯，而不是只剩段數不同的全 `20` 模板。
- `dragon dagger -> rain throwing` 則維持封存鏈的高速匕法 / 暗器 identity，只用更高 `Value` 拉開 endpoint 差距。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-n.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch M Pre-Check

### Scope

- `monkey stick`
- `day stick`

### Reference Basis

- `/Users/jakeuj/auggie/3yWebsite/skill/stick.html`
  - 明確給出 `monkey stick -> day stick`
  - `day stick` 以 `monkey stick` 為 prerequisite
- `docs/current-game/skills/staff.md`
  - current-game 已把這條鏈整理成 `legacy-page:stick`
  - runtime 目前顯示兩者 damage values 皆為全 `20`
- runtime `skill/*.ski`
  - `monkey_stick.ski`
    - `Associate SLOT_DAYSTICK`
    - `CanAsk YES / Valid YES / Enable YES`
  - `daystick.ski`
    - `Associate -1`
    - `CanAsk YES / Valid YES / Enable YES`

### Mandatory Pre-Check Snapshot

`monkey stick`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 17`
- weapon / check: `WEAPON_CLUB / check_club_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `5`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`day stick`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 14`
- weapon / check: `WEAPON_CLUB / check_club_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `5`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條棍系短鏈是典型的玩家向 legacy ladder，舊站鏈路與 current-game/runtime 都能互相對上。
- 兩招同為高體力消耗棍法，但 `day stick` 既有 prerequisite、可學職業更少、且 `Chance` 更高，不能和 `monkey stick` 一樣維持全 `20`。
- `monkey stick` 雖是 root，help 文案仍明講「殺傷力不小」；因此本批不會把它壓成純新手刮痧模板，而是重建成可成立的入門重棍。
- area `*.mob` 與 `#Learn` 目前未看到 `monkey stick` / `day stick` 的現成 runtime enable 樣本，因此本批仍先修 skill template，不先動 mob fallout。

## Batch M Result

### Scope

- `monkey stick`
- `day stick`

### Runtime Changes

`monkey stick`

- before: `20 x 5`
- after: `80, 95, 110, 130, 150`
- average: `113.0`

`day stick`

- before: `20 x 5`
- after: `125, 145, 165, 185, 210`
- average: `166.0`

### Design Notes

- 本批只調 `Value`，保留棍系既有的高成本與重兵器節奏。
- `monkey stick` 站穩高成本 root，不再是和高階棍法幾乎無差別的清值模板。
- `day stick` 以更高的單段值承接 prerequisite 後的進階段，讓這條短鏈重新有明顯的玩家向升階感。

### Validation

- `make -C src -f Makefile.lin merc`
- `make -C src merc`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-m.log`
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

## Batch Q Pre-Check

### Scope

- `fu sword`
- `sky dragon sword`
- `duansun sword`

### Reference Basis

- `docs/3yWebsite/skill/sword.html`
  - 明確給出 `fu sword -> sky dragon sword -> duansun sword`
  - `fu sword` 可互教，且是整條鏈的 root
  - `sky dragon sword` 以 `fu sword` 為 prerequisite，且舊站標成「領悟機率極低」的高階延伸
  - `duansun sword` 以 `sky dragon sword` 為 prerequisite，且是 50 級後的終點劍法
- `docs/current-game/skills/sword.md`
  - current-game 已把這條鏈整理在 `legacy-page:sword`
  - runtime 顯示三者 damage values 仍幾乎全 `20`
- runtime `skill/*.ski`
  - `fuswords.ski`
    - `Associate SLOT_SKYDRAGON_SWORD`
    - `CanAsk YES / Teach YES / Valid YES`
  - `skydragon_sword.ski`
    - `Associate -1`
    - `CanAsk YES / Teach NO / Valid YES`
  - `duansun_sword.ski`
    - `Associate -1`
    - `CanAsk NO / Teach NO / Valid NO`

### Mandatory Pre-Check Snapshot

`fu sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 13`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `YES / YES / YES`
- damage entries: `11`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`sky dragon sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 14`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `8`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`duansun sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 10`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈的舊站 progression 很清楚，而且 runtime `Associate` 也和舊站順序一致。
- 三者目前共同 distortion 很明顯：`Value` 幾乎整串被清成 `20`，但 `Cost / Wait / Chance` 並沒有被抹平。
- `fu sword` 不是新手快劍 root，而是較慢、較重、但仍可 teach 的中階起點；因此回補後平均值應高於 `hua sword` 這類入門根技能。
- `sky dragon sword` 成本更高、限制更重，且舊站直接把它放成「極低機率領悟」的進階段，應站穩高於 `fu sword` 的重型中高階段。
- `duansun sword` 雖然 `Cost / Wait` 反而略低，但它同時具備：
  - 更高 prerequisite
  - 更晚的等級門檻
  - 較低的 `Chance 10`
- 因此本批最合理的修法仍是只重建 `Value`，把 `duansun sword` 做成較高單段、較低出手機率的終點模板，而不在這輪改 `Valid / CanAsk / Teach` 的 runtime policy。
- area `*.mob` 目前未看到這三招的現成 `Enable / AutoEnable` 樣本，因此本批先不做 mob fallout。

## Batch Q Result

### Scope

- `fu sword`
- `sky dragon sword`
- `duansun sword`

### Runtime Changes

`fu sword`

- before: `20 x 11`
- after: `95, 115, 135, 155, 175, 200, 225, 250, 275, 305, 340`
- average: `206.36`

`sky dragon sword`

- before: `20 x 8`
- after: `150, 180, 210, 240, 275, 315, 360, 410`
- average: `267.5`

`duansun sword`

- before: `20 x 7`
- after: `200, 225, 250, 280, 315, 355, 400`
- average: `289.29`

### Design Notes

- 本批仍只調 `Value`，刻意保留這條劍鏈既有的慢節奏、體力消耗與武器 identity。
- `fu sword` 回到可成立的中階 root，不再是 11 段全 `20` 的殘缺模板。
- `sky dragon sword` 用更高成本、更高單段值承接真正的高階銜接段，呼應舊站「極低領悟機率」與重限制定位。
- `duansun sword` 雖保留 `Chance 10`，但以更高單段值站穩終點模板，避免它因清值而和前段幾乎沒有本質差距。
- 本批不處理 `Valid / CanAsk / Teach` 的遺留政策，將 combat ladder 重建與技能開放政策分開處理。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-q.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch R Pre-Check

### Scope

- `shan sword`
- `shadow kill sword`
- `six sword`

### Reference Basis

- `docs/3yWebsite/skill/sword.html`
  - 明確給出 `shan sword -> shadow kill sword -> six sword`
  - `shan sword` 是可教 root，且舊站直接列出多個老師樣本
  - `shadow kill sword` 以 `shan sword` 為 prerequisite，舊站標示為高階、不可互教的延伸段
  - `six sword` 以 `shadow kill sword` 為 prerequisite，且是整條鏈的終點技能
- `docs/current-game/skills/sword.md`
  - current-game 已把這條鏈整理在 `legacy-page:sword`
  - runtime 顯示三者 `Value` 幾乎仍全 `20`
- runtime `skill/*.ski`
  - `shansword.ski`
    - `Associate -1`
    - `CanAsk NO / Teach NO / Valid NO`
  - `shadow_kill.ski`
    - `Associate -1`
    - `CanAsk NO / Teach NO / Valid NO`
  - `six_sword.ski`
    - `Associate -1`
    - `CanAsk NO / Teach NO / Valid NO`

### Mandatory Pre-Check Snapshot

`shan sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`shadow kill sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `17`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`six sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈和 `bad sword -> wumin sword -> noname` 類似，舊站 progression 很清楚，但 runtime 現況保留成封存式 legacy 技能。
- 三者共同 distortion 很明顯：`Value` 被整串清成 `20`，但 `Wait 1` 與 `Chance 10` 的快劍特性仍被保留。
- `shan sword` 應維持成快劍 root，雖然平均值要回升，但不能直接和終點技能拉到同一級。
- `shadow kill sword` 同樣 `Cost 10 / Wait 1`，但有更高 prerequisite、更多段數，應被拉成清楚高於 `shan sword` 的中高階連段模板。
- `six sword` 是整條鏈的終點，雖然 damage entries 較少，但有更重 `Cost 20` 與更嚴格的屬性／熟練限制，應以更高單段值站穩終點身分。
- area `*.mob` 目前未看到這三招的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch R Result

### Scope

- `shan sword`
- `shadow kill sword`
- `six sword`

### Runtime Changes

`shan sword`

- before: `20 x 8`
- after: `55, 70, 85, 100, 115, 130, 145, 165`
- average: `108.13`

`shadow kill sword`

- before: `20 x 17`
- after: `90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 290, 310, 335, 360`
- average: `214.12`

`six sword`

- before: `20 x 7`
- after: `170, 195, 220, 245, 275, 310, 350`
- average: `252.14`

### Design Notes

- 本批仍只調 `Value`，保留這條鏈原本的 `Wait 1` 快劍性格與 `Chance 10` 的低出手機率分布。
- `shan sword` 回到可成立的 root，不再是看起來像高級技能、實際卻和入門殘值一樣的假模板。
- `shadow kill sword` 以更多段數與更高平均值承接中高階段，但仍避免直接壓過終點技能的單段定位。
- `six sword` 用更高單段值與更重成本站穩終點模板，讓這條快劍鏈重新有清楚的三段式梯度。
- 本批不處理 `Valid / CanAsk / Teach` 的 runtime policy，維持和前幾批相同的「先重建 combat template，再分開討論開放政策」策略。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-r.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch S Pre-Check

### Scope

- `two sword`
- `gsword`
- `tendo slash`

### Reference Basis

- `docs/3yWebsite/skill/sword.html`
  - 明確給出 `two sword -> gsword -> tendo slash`
  - `two sword` 是可教 root，且舊站列出多個 general/fighter 教師樣本
  - `gsword` 以 `two sword` 為 prerequisite，屬更高階的中段
  - `tendo slash` 以 `gsword` 為 prerequisite，且為終點技能
- `docs/current-game/skills/sword.md`
  - current-game 已把這條鏈整理在 `legacy-page:sword`
  - runtime 顯示三者多數 `Value` 仍停在 `20`
- runtime `skill/*.ski`
  - `twosword.ski`
    - `Associate SLOT_GSWORD`
    - 大多數 `Value 20`，但保留一筆 `Value 200`、`Chance 30`、`Innate 404 150`
  - `gsword.ski`
    - `Associate SLOT_TENDO_SLASH`
    - `Value` 全 `20`
  - `tendo_slash.ski`
    - `Associate -1`
    - `Value` 全 `20`

### Mandatory Pre-Check Snapshot

`two sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 12`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `12`
- chance set: `20` except one `30`
- value set before rebuild: `20` except one `200`
- parry set: `0`
- special case:
  - one entry keeps `Innate 404 150`

`gsword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `25 / COST_MOVE / 13`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `11`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`tendo slash`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 14`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / YES`
- damage entries: `9`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈不是單純的「整串全被清成 20」；`two sword` 明顯保留了一筆高值與 innate 特例。
- 因此本批不能把 `two sword` 誤當成普通扁平鏈全面重寫，而應視為 hybrid case：
  - 保留那筆 `Value 200 / Chance 30 / Innate 404 150` 的特色招
  - 補回其餘被清空的周邊招式
- `two sword` 仍應是可教 root，故整體平均值需要回升，但不能直接壓過 `gsword`。
- `gsword` 與 `tendo slash` 則屬更典型的被清值中高階段，可較直接以 `Value` 階梯重建。
- area `*.mob` 目前未看到這三招的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批仍先不做 mob fallout。

## Batch S Result

### Scope

- `two sword`
- `gsword`
- `tendo slash`

### Runtime Changes

`two sword`

- before: `20, 200, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20`
- after: `70, 200, 85, 100, 115, 130, 145, 160, 175, 190, 205, 225`
- average: `150.0`
- keep case:
  - 保留第二段的 `Value 200`
  - 保留第二段的 `Chance 30`
  - 保留第二段的 `Innate 404 150`

`gsword`

- before: `20 x 11`
- after: `110, 130, 150, 170, 190, 215, 240, 265, 295, 330, 370`
- average: `224.09`

`tendo slash`

- before: `20 x 9`
- after: `180, 205, 230, 255, 285, 320, 360, 405, 455`
- average: `299.44`

### Design Notes

- 本批採 hybrid rebuild，不把 `two sword` 那筆歷史特例抹平成普通招式。
- `two sword` 的特殊高值／innate 仍保留成鏈中的亮點，其餘招式則補回可支撐 root 身分的梯度。
- `gsword` 用更高成本、更高平均值承接中高階段。
- `tendo slash` 以更高單段值與整體平均值站穩終點模板，讓這條鏈重新恢復 clear progression。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-s.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch T Pre-Check

### Scope

- `evil fist`
- `evil king`

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - 明確給出 `evil fist -> evil king`
  - `evil fist` 是可學 root
  - `evil king` 以 `evil fist` 為 prerequisite，且是該支鏈的終點
- `docs/current-game/skills/fist.md`
  - current-game 已把這條鏈整理在 `legacy-page:fist`
  - runtime 顯示兩者 `Value` 仍全 `20`
- runtime `skill/*.ski`
  - `evilfist.ski`
    - `Associate SLOT_EVIL_KING`
    - `CanAsk YES / Teach NO / Valid YES`
  - `evil_king.ski`
    - `Associate -1`
    - `CanAsk YES / Teach NO / Valid YES`

### Mandatory Pre-Check Snapshot

`evil fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`evil king`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 8`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條拳法支鏈屬標準清值案例：兩端都被壓成全 `20`，沒有明顯 hybrid / innate keep case。
- `evil fist` 仍應站穩 root，但它本來就不算輕量快拳，因此回補後應高於 `long fist` 那類新手模板。
- `evil king` 和 `evil fist` 同為 `Chance 10`，但 `Wait` 更短、prerequisite 更高，應在不改節奏參數的前提下，用更高 `Value` 站穩終點拳路。
- area `*.mob` 目前未看到這兩招的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch T Result

### Scope

- `evil fist`
- `evil king`

### Runtime Changes

`evil fist`

- before: `20 x 7`
- after: `70, 85, 100, 115, 130, 155, 190`
- average: `120.71`

`evil king`

- before: `20 x 8`
- after: `125, 145, 165, 185, 205, 230, 260, 300`
- average: `201.88`

### Design Notes

- 本批只調 `Value`，保留這條拳法支鏈既有的 `Chance 10` 與出招節奏。
- `evil fist` 回到可成立的中階 root，不再和被清值後的殘缺模板混成一團。
- `evil king` 以更短 `Wait` 和更高單段值承接終點定位，恢復 clear progression。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-t.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch U Pre-Check

### Scope

- `ghost strike`
- `ghost marial`

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - 明確給出 `ghost strike -> ghost marial`
  - `ghost strike` 是可教 root
  - `ghost marial` 以 `ghost strike` 為 prerequisite，為該支鏈終點
- `docs/current-game/skills/fist.md`
  - current-game 已把這條鏈整理在 `legacy-page:fist`
  - runtime 顯示兩者 `Value` 仍全 `20`
- runtime `skill/*.ski`
  - `ghoststrike.ski`
    - `Associate SLOT_GHOST_MARIAL`
    - `CanAsk YES / Teach YES / Valid YES`
  - `ghost_marial.ski`
    - `Associate -1`
    - `CanAsk YES / Teach NO / Valid YES`

### Mandatory Pre-Check Snapshot

`ghost strike`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / YES / YES`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`ghost marial`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 7`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `6`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條支鏈同樣是標準清值案例，沒有看到單筆高值或 innate keep case。
- `ghost strike` 與 `ghost marial` 和 `evil fist` 系最大的不同，是它們本來就維持 `Chance 20`，因此體感上應更偏穩定輸出而不是低頻爆發。
- `ghost strike` 作為 root，回補後仍要保留中階掌法身分。
- `ghost marial` 有更短 `Wait` 與更高 prerequisite，應用更高 `Value` 清楚承接終點定位。
- area `*.mob` 目前未看到這兩招的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch U Result

### Scope

- `ghost strike`
- `ghost marial`

### Runtime Changes

`ghost strike`

- before: `20 x 7`
- after: `75, 95, 115, 135, 155, 180, 210`
- average: `137.86`

`ghost marial`

- before: `20 x 6`
- after: `135, 160, 185, 210, 240, 275`
- average: `200.83`

### Design Notes

- 本批只調 `Value`，保留這條拳法支鏈原本 `Chance 20` 的穩定輸出風格。
- `ghost strike` 回到可成立的 root，不再是全 `20` 的殘缺模板。
- `ghost marial` 以更短 `Wait` 和更高單段值承接終點身分，和 `ghost strike` 拉開清楚距離。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-u.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch V Pre-Check

### Scope

- `ryo`
- `hashin`

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - 明確給出 `ryo -> hashin`
  - `ryo` 是可學 root
  - `hashin` 以 `ryo` 為 prerequisite，為高階終點拳路
- `docs/current-game/skills/fist.md`
  - current-game 已把這條鏈整理在 `legacy-page:fist`
  - runtime 顯示兩者多數 `Value` 仍停在 `20`
- runtime `skill/*.ski`
  - `ryo.ski`
    - `Associate SLOT_HASHIN`
    - 第一段保留 `Value 150`
    - 其餘段落仍為 `20`
  - `hashin.ski`
    - `Associate -1`
    - `Value` 全 `20`
- area runtime samples
  - `area/loyang/mob/593.mob`
    - `Enable 100 'ryo'`
  - `area/loyang/mob/594.mob`
    - `Enable 100 'ryo'`
  - `area/loyang/mob/595.mob`
    - `Enable 100 'ryo'`
  - `area/loyang/mob/596.mob`
    - `Enable 100 'ryo'`
  - `area/loyang/mob/597.mob`
    - `Enable 100 'ryo'`

### Mandatory Pre-Check Snapshot

`ryo`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `150, 20, 20, 20, 20, 20, 20`
- parry set: `0`
- special case:
  - 第一段已保留 `Value 150`

`hashin`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `10`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈和 `two sword` 類似，是 hybrid root case：
  - `ryo` 並不是完全清值
  - 它保留了一招明顯較強的 root 特例
- 因此本批不應把 `ryo` 全數重寫成等距 ladder，而是：
  - 保留第一段 `Value 150`
  - 補回其餘被清空的段落
- `hashin` 則是標準高階終點清值案例，可直接用更高 `Value` 階梯重建。
- 目前已有多個洛陽 mob 固定 `Enable 100 'ryo'`，因此這批至少要把代表樣本記錄在案；不過因為它們是 explicit `Enable`，本輪先不做 failenable fallout 處理。

## Batch V Result

### Scope

- `ryo`
- `hashin`

### Runtime Changes

`ryo`

- before: `150, 20, 20, 20, 20, 20, 20`
- after: `150, 135, 155, 175, 195, 220, 250`
- average: `182.86`
- keep case:
  - 保留第一段的 `Value 150`

`hashin`

- before: `20 x 10`
- after: `170, 195, 220, 245, 275, 310, 350, 395, 445, 500`
- average: `310.5`

### Design Notes

- 本批採 hybrid rebuild，不把 `ryo` 唯一保留下來的高值特例抹掉。
- `ryo` 其餘段落補回後，整體才真正像高階 root，而不是只靠單一特例硬撐。
- `hashin` 以更高成本但相同 `Wait 5` 的節奏，承接真正的終點拳路定位。
- 本批先記錄 `ryo` 的 explicit mob 使用樣本，不在這輪直接動 `area/*.mob`。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-v.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch W Pre-Check

### Scope

- `king fist`
- `sky dragon`
- `sky dragon force`

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - 明確給出 `king fist -> sky dragon -> sky dragon force`
  - `king fist` 是 root
  - `sky dragon` 以 `king fist` 為中段延伸
  - `sky dragon force` 以 `sky dragon` 為終點延伸
- `docs/current-game/skills/fist.md`
  - current-game 已把這條鏈整理在 `legacy-page:fist`
  - runtime 顯示三者 `Value` 幾乎全 `20`
- runtime `skill/*.ski`
  - `king_fist.ski`
    - `CanAsk NO / Valid NO`
    - `Value` 全 `20`
  - `skydragon.ski`
    - `CanAsk NO / Valid NO`
    - `Value` 全 `20`
  - `skydragon_force.ski`
    - `CanAsk NO / Valid NO`
    - `Value` 全 `20`

### Mandatory Pre-Check Snapshot

`king fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `19 / COST_MOVE / 12`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`sky dragon`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `13`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

`sky dragon force`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `3`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這條鏈屬標準直線清值案例，沒有 hybrid keep case。
- 雖然 `sky dragon` / `sky dragon force` 的 `Wait` 反而更短，但它們同時是封存式高階技能，且 damage entries 與舊站鏈位都明顯更高階，因此適合單純以 `Value` 重建梯度。
- `king fist` 應站穩較慢、較厚重的 root。
- `sky dragon` 應被拉成真正的高階快拳主力。
- `sky dragon force` 雖然只有 3 段，但可用更高單段值站成這條鏈的終點祕招。
- area `*.mob` 目前未看到這三招的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch W Result

### Scope

- `king fist`
- `sky dragon`
- `sky dragon force`

### Runtime Changes

`king fist`

- before: `20 x 7`
- after: `95, 115, 135, 155, 175, 200, 230`
- average: `157.86`

`sky dragon`

- before: `20 x 13`
- after: `135, 155, 175, 195, 215, 235, 260, 285, 315, 350, 390, 435, 485`
- average: `279.62`

`sky dragon force`

- before: `20 x 3`
- after: `220, 270, 330`
- average: `273.33`

### Design Notes

- 本批只調 `Value`，維持這條鏈原本 `Chance 10` 與快拳／祕招節奏。
- `king fist` 回到可成立的厚重 root。
- `sky dragon` 以更多段數與更高平均值承接高階快拳主力。
- `sky dragon force` 雖然段數少，但以高單段值站穩終點祕招定位。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-w.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch X Pre-Check

### Scope

- `rulai`

### Reference Basis

- `docs/3yWebsite/skill/fist.html`
  - `rulai` 以單獨技能列在拳法頁，無 prerequisite、無 next
  - 舊站明確標成玩家可學的高階空手技能
- `docs/current-game/skills/fist.md`
  - current-game 已把 `rulai` 列為 `legacy-page:fist` 的單點技能
  - runtime 顯示其 `Value` 仍全 `20`
- runtime `skill/r/rulai.ski`
  - `CanAsk NO / Teach NO / Valid YES`
  - `Value` 全 `20`
- area runtime samples
  - `area/loyang/mob/591.mob`
    - `Enable 100 'rulai'`
  - `area/loyang/mob/602.mob`
    - `Enable 100 'rulai'`

### Mandatory Pre-Check Snapshot

`rulai`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / YES`
- damage entries: `9`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- `rulai` 雖不是多段 prerequisite ladder，但仍是明確的 player-facing legacy 高階掌法。
- 現況全 `20` 很難成立其高階定位，因此適合獨立做單點 rebuild。
- 目前已有兩個洛陽樣本固定 `Enable 100 'rulai'`，代表這不是純文件孤兒技能；不過它們屬 explicit `Enable`，本輪先不動 mob data。

## Batch X Result

### Scope

- `rulai`

### Runtime Changes

`rulai`

- before: `20 x 9`
- after: `120, 145, 170, 195, 220, 250, 285, 325, 370`
- average: `231.11`

### Design Notes

- 本批只調 `Value`，保留 `rulai` 原本 `Chance 20 / Wait 10` 的穩定高階掌法節奏。
- 這樣可以先把單點高階模板從清值狀態救回來，再視需要另開一輪處理 teacher / validity policy 或 mob wiring。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-x.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch Y Pre-Check

### Scope

- `dragon phoenix`

### Reference Basis

- `docs/3yWebsite/skill/general.html`
  - `dragon phoenix` 以單獨技能列在格鬥系頁
  - 舊站明確給出職業限制、屬性限制與 prerequisite
- `docs/current-game/skills/job-fighter.md`
  - current-game 已把 `dragon phoenix` 列為 `legacy-page:general`
  - runtime 顯示其 `Value` 仍全 `20`
- runtime `skill/d/dragon_phoe.ski`
  - `CanAsk YES / Teach NO / Valid YES`
  - `Value` 全 `20`

### Mandatory Pre-Check Snapshot

`dragon phoenix`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `40 / COST_MOVE / 10`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `9`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是單點高階刀法，不屬於多段 prerequisite ladder，但仍是明確的 player-facing legacy 高階技能。
- `Cost 40` 已明顯高於一般刀法，因此只要 `Value` 維持全 `20`，模板就會嚴重失真。
- area `*.mob` 目前未看到 `dragon phoenix` 的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch Y Result

### Scope

- `dragon phoenix`

### Runtime Changes

`dragon phoenix`

- before: `20 x 9`
- after: `180, 210, 240, 270, 305, 345, 390, 440, 500`
- average: `320.0`

### Design Notes

- 本批只調 `Value`，保留 `dragon phoenix` 原本高成本、大刀、高階刀法的節奏與武器 identity。
- 這樣可以先把單點高階模板從清值狀態拉回來，再視需要另開一輪處理更細的教學／職業政策。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-y.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
  - `debug/error`
    - 無新增內容

## Batch Z Pre-Check

### Scope

- `dragon heroism blade`

### Reference Basis

- runtime `skill/d/dragon_heroism.ski`
  - `CanAsk NO / Teach NO / Valid NO`
  - `Value` 全 `20`
  - 第七段保留 `Innate 44 160`
- `docs/current-game/skills/blade.md`
  - current-game 已收錄 `dragon heroism blade`
  - runtime 顯示其 `Value` 仍全 `20`
- source note
  - 目前未在舊站 `skill/*.html` 找到獨立條目，但 runtime `.ski` 與 current-game 已足以確認它是現行可 enable 的高階刀法模板

### Mandatory Pre-Check Snapshot

`dragon heroism blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 14`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- damage entries: `8`
- chance set:
  - first entry `20`
  - remaining entries `10`
- value set before rebuild: `20`
- parry set: `0`
- special case:
  - seventh entry keeps `Innate 44 160`

### Interpretation

- 這是單點高階刀法，且不是完全同質模板：
  - 第一段 `Chance 20`
  - 第七段帶 `Innate 44 160`
- 因此本批不應動 `Chance` 或 innate 特例，只重建 `Value` 階梯。
- area `*.mob` 目前未看到 `dragon heroism blade` 的現成 `Enable / AutoEnable / #Learn` 樣本，因此本批先不做 mob fallout。

## Batch Z Result

### Scope

- `dragon heroism blade`

### Runtime Changes

`dragon heroism blade`

- before: `20 x 8`
- after: `130, 155, 180, 210, 245, 285, 335, 395`
- average: `241.88`
- keep case:
  - 保留第七段 `Innate 44 160`

### Design Notes

- 本批只調 `Value`，保留原本的 `Chance` 分布與 innate 特例。
- 這樣可以在不抹平技能個性的前提下，把高階刀法模板從清值狀態拉回成立。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 4838 / 2234 / 9888`
  - 改用 `IPC KEY 4585`
- 檢查：
  - `log/smoke-batch-z.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/badobject`
    - 無新增內容
- `debug/error`
    - 無新增內容

## Batch AA Pre-Check

### Scope

- `hate sword`

### Reference Basis

- `docs/3yWebsite/skill/bravo.html`
  - 舊站仍列出 `hate sword`
  - 確認它屬於 bravo 路線玩家向高階劍技
- runtime `skill/h/hate_sword.ski`
  - `Value` 全 `20`
  - `Chance` 固定 `10`
  - `Weapon WEAPON_SWORD / Check check_sword_attack`

### Mandatory Pre-Check Snapshot

`hate sword`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `40 / COST_MOVE / 9`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `12`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向高成本、高階 bravo 劍技，不屬於新手鏈或多段 prerequisite ladder。
- `Cost 40` 與 `12` 段傷害描述都顯示它不該維持全 `20` 的清值模板。
- 本批先只回填 `Value` 階梯，保留原本的成本、節奏與劍系 identity。

## Batch AA Result

### Scope

- `hate sword`

### Runtime Changes

`hate sword`

- before: `20 x 12`
- after: `155, 175, 195, 220, 245, 275, 310, 350, 395, 445, 500, 560`
- average: `318.75`

### Design Notes

- 本批只調 `Value`，保留 `Chance / Wait / Cost / Weapon / Check` 原樣。
- 這樣可以先把 high-tier bravo 劍技從清值模板拉回成立，再視需要另外處理教學或職業政策。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-aa.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AQ Pre-Check

### Scope

- `cry ghost`

### Reference Basis

- runtime `skill/c/cry_ghost.ski`
  - 單段 `Value 20`
  - `Cost 20 / Wait 1 / Weapon WEAPON_SPEAR / Check check_spear_attack`
  - `Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `cry ghost`
  - `family = legacy-page:cry ghost`
  - combat 維度顯示單段 `Value 20`

### Mandatory Pre-Check Snapshot

`cry ghost`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_SPEAR / check_spear_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `1`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是單段但明確玩家向的槍系必殺招，不是一般低階雜技。
- 既然只有一段，`Value 20` 幾乎沒有成立空間，因此適合直接做單點補值。
- 本批只調單段 `Value`，保留其高速 spear finisher identity。

## Batch AQ Result

### Scope

- `cry ghost`

### Runtime Changes

`cry ghost`

- before: `20`
- after: `260`

### Design Notes

- 本批把 `cry ghost` 拉回可成立的高速必殺招，而不擴成多段或改節奏。
- 這樣能先修掉清值模板問題，同時保留它作為單段槍系大招的辨識度。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-as.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AR Pre-Check

### Scope

- `dream dance`

### Reference Basis

- runtime `skill/d/dreamdance.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 12 / Check check_unrigid_attack`
  - `Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `dream dance`
  - `family = legacy-page:dream dance`
- `area/limbo/obj/255.obj`
  - book slot 對應 `SLOT_DREAMDANCE`

### Mandatory Pre-Check Snapshot

`dream dance`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 12`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `7`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是偏重節奏的舞系攻擊技，`Wait 12` 表示單段威力應高於快節奏小招。
- 多段描述完整但全 `20`，顯示其模板被壓平。
- 本批只回填 `Value` 階梯，保留舞系技的出手節奏。

## Batch AR Result

### Scope

- `dream dance`

### Runtime Changes

`dream dance`

- before: `20 x 7`
- after: `130, 155, 185, 220, 260, 305, 360`
- average: `230.71`

### Design Notes

- 本批讓 `dream dance` 保持重節奏、姿態型的單點技能定位。
- 這樣能和 `Wait 1` 的快節奏技維持差異，同時讓後段有明顯高階感。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-as.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AS Pre-Check

### Scope

- `drunk`

### Reference Basis

- runtime `skill/d/drunk.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 1 / Check check_unrigid_attack`
  - `Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `drunk`
  - `family = legacy-page:drunk`
- `area/limbo/obj/256.obj`
  - 仍存在 `drunk book`
- `area/loyang/mob/564.mob`
  - 現存 `drunk man` 樣本，說明這套模板仍在世界中被保留

### Mandatory Pre-Check Snapshot

`drunk`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是快節奏醉拳模板，雖然帶有 flavor，但 current-game 與 area 樣本都證明它仍是活的 runtime skill。
- 因為 `Wait 1`，均值不應拉到慢節奏重技那麼高，但全 `20` 仍然失真。
- 本批只回填 `Value` 階梯，保留其高速、花式的醉拳 identity。

## Batch AS Result

### Scope

- `drunk`

### Runtime Changes

`drunk`

- before: `20 x 8`
- after: `95, 110, 125, 145, 170, 200, 235, 275`
- average: `169.38`

### Design Notes

- 本批讓 `drunk` 維持快節奏、偏中低單段但持續成長的風格。
- 這樣既不會壓成清值模板，也不會和重節奏高階拳技混成同一種體感。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-as.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AO Pre-Check

### Scope

- `citizen`

### Reference Basis

- runtime `skill/c/citizen.ski`
  - `Value` 全 `20`
  - `Cost 5 / Wait 5`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `citizen`
  - `family = legacy-page:citizen`
  - combat 維度標記 `prepared_for_adjustment = true`
- area samples
  - `area/loyang/mob/505.mob`
  - `area/loyang/mob/508.mob`
  - `area/loyang/mob/557.mob`
  - 這些都以 `citizen` 身分出現，符合低階/NPC-adjacent 用途

### Mandatory Pre-Check Snapshot

`citizen`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `5 / COST_MOVE / 5`
- weapon / check: `- / -`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `3`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這不是高階玩家主戰技能，而是低階/NPC-adjacent 的街頭亂打模板。
- 但 current-game 已標成可調整，且全 `20` 讓三段描述完全失去層次。
- 本批只把它拉回最低限度可成立的低階梯度，不把它抬成正式高階 combat line。

## Batch AO Result

### Scope

- `citizen`

### Runtime Changes

`citizen`

- before: `20, 20, 20`
- after: `40, 55, 75`
- average: `56.67`

### Design Notes

- 本批刻意把 `citizen` 壓在低檔，只讓街頭亂打不再和清值模板完全相同。
- 這樣能避免 NPC flavor skill 失真，同時不干擾玩家向高階技能層次。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ap.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AP Pre-Check

### Scope

- `shoutsky`

### Reference Basis

- runtime `skill/s/shoutsky.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 1 / Weapon WEAPON_BLADE / Check check_blade_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `shout sky`
  - runtime combat 維度顯示 `4` 段 `Value 20`
- `area/limbo/obj/230.obj`
  - book slot 對應 `SLOT_SHOUTSKY`

### Mandatory Pre-Check Snapshot

`shoutsky`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `4`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是快節奏 blade 單點技能，雖然段數不多，但作為血刀三式衍生特技不應維持全 `20`。
- `Wait 1` 意味著不能套用重節奏刀法的數值尺度，但仍該有明顯高階成長。
- 本批先只回填 `Value` 階梯，保留高速 blade identity。

## Batch AP Result

### Scope

- `shoutsky`

### Runtime Changes

`shoutsky`

- before: `20 x 4`
- after: `120, 155, 200, 255`
- average: `182.5`

### Design Notes

- 本批讓 `shoutsky` 保持快節奏 blade 特技定位，但不再是清值模板。
- 這樣和慢節奏高階刀法仍有差異，同時後段也有可感知的成長。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ap.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AM Pre-Check

### Scope

- `sevencolor`

### Reference Basis

- runtime `skill/s/sevencolor.ski`
  - `Value` 全 `20`
  - `Cost 10 / Wait 1 / Check check_unrigid_attack`
  - `Enable NO`
- `docs/current-game/skills.json`
  - current-game 已收錄 `seven color`
  - `family = legacy-page:seven color`
  - 明確記錄 prerequisite 為 `碧血十二針(be needle)`
- `area/limbo/obj/206.obj`
  - 仍存在 `seven color book`
- runtime comparison
  - `be needle` 已具正常遞增梯度，證明 `sevencolor` 目前全 `20` 並非同系預期終態

### Mandatory Pre-Check Snapshot

`sevencolor`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `10 / COST_MOVE / 1`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `NO`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 雖然 `Enable NO`，但它仍是明確玩家向 legacy 技能，且有祕笈樣本與 current-game prerequisite 記錄。
- 作為 `be needle` 之後的高階特殊招式，維持全 `20` 明顯失真。
- 本批先只回填 `Value` 階梯，保留其 `Wait 1` 的高速特殊技定位。

## Batch AM Result

### Scope

- `sevencolor`

### Runtime Changes

`sevencolor`

- before: `20 x 9`
- after: `105, 125, 150, 180, 215, 255, 300, 355, 420`
- average: `233.89`

### Design Notes

- 本批讓 `sevencolor` 站在 `be needle` 之後、但仍維持高速特殊技的定位。
- 這樣既能保留連續技節奏，也不會把它抬成慢節奏重砲模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-an.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AN Pre-Check

### Scope

- `tree touch`

### Reference Basis

- runtime `skill/t/tree_touch.ski`
  - 單段 `Value 20`
  - `Cost 20 / Wait 1 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `tree touch`
  - `family = legacy-page:tree touch`

### Mandatory Pre-Check Snapshot

`tree touch`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `1`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是單段玩家向特殊技，雖然資訊量比多段技能少，但 current-game 已明確把它保留下來。
- 單段 `Value 20` 幾乎沒有作為玩家攻擊技成立的空間，因此適合當輕量單點補值。
- 本批先只調單段 `Value`，不改其快節奏與出手型態。

## Batch AN Result

### Scope

- `tree touch`

### Runtime Changes

`tree touch`

- before: `20`
- after: `180`

### Design Notes

- 本批把 `tree touch` 拉回可成立的單點特殊技，但不把它擴寫成多段或改節奏。
- 這樣可以先止住清值模板問題，之後若要再細分功能再另開批次。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-an.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AJ Pre-Check

### Scope

- `yu needle`

### Reference Basis

- `docs/3yWebsite/docs/data/skills.json`
  - 收錄 `yu needle`
- runtime `skill/y/yu_needle.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 1 / Weapon WEAPON_PEN / Check check_pen_attack`
  - `Valid YES / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `yu needle`
  - `family = legacy-page:yu needle`
  - combat 維度顯示 `15` 段 `Value 20`
- `area/limbo/obj/288.obj`
  - 仍存在 `yu needle book`

### Mandatory Pre-Check Snapshot

`yu needle`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_PEN / check_pen_attack`
- canask / teach / valid: `NO / NO / YES`
- enable: `YES`
- damage entries: `15`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向高段數針系攻擊技，且 `Wait 1` 明顯屬於快節奏連擊模板。
- 因為頻率高、段數多，所以平均值不應用重節奏大招的尺度，但全 `20` 仍明顯失真。
- 本批先只回填 `Value` 階梯，保留其快節奏與針系 identity。

## Batch AJ Result

### Scope

- `yu needle`

### Runtime Changes

`yu needle`

- before: `20 x 15`
- after: `95, 110, 125, 140, 160, 180, 205, 230, 255, 285, 315, 350, 390, 440, 500`
- average: `252.0`

### Design Notes

- 本批讓 `yu needle` 保持高速連擊模板，但後段仍有清楚的高階成長。
- 這樣不會把針系快技拉成慢節奏重砲，同時也不再是清值模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-al.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AK Pre-Check

### Scope

- `blood ten`

### Reference Basis

- runtime `skill/b/blood_ten.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 1 / Weapon WEAPON_BLADE / Check check_blade_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `blood ten`
  - `family = legacy-page:blood ten`
  - combat 維度顯示 `10` 段 `Value 20`
- `area/limbo/obj/390.obj`
  - 仍存在 `blood ten book`

### Mandatory Pre-Check Snapshot

`blood ten`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `10`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向快節奏刀技，雖然 weapon identity 明確，但目前仍被壓成全 `20`。
- 由於 `Wait 1`，它的均值應壓低於同級慢節奏 blade 重技，但後段仍該有明顯提升。
- 本批先只回填 `Value` 階梯，保留高速刀技節奏。

## Batch AK Result

### Scope

- `blood ten`

### Runtime Changes

`blood ten`

- before: `20 x 10`
- after: `120, 140, 165, 190, 220, 255, 295, 340, 395, 460`
- average: `258.0`

### Design Notes

- 本批把 `blood ten` 定位成高速但仍帶中後段爆發的 blade 單點技能。
- 這樣能與慢節奏重刀技能保持差異，同時避免它和其他 `Wait 1` 技能完全同模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-al.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AL Pre-Check

### Scope

- `dark word`

### Reference Basis

- runtime `skill/d/dark_word.ski`
  - `Value` 全 `20`
  - `Cost 19 / Wait 12 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `dark word`
  - `family = legacy-page:dark word`
  - combat 維度顯示 `8` 段 `Value 20`
- `area/limbo/obj/246.obj`
  - 仍存在 `dark word book`

### Mandatory Pre-Check Snapshot

`dark word`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `19 / COST_MOVE / 12`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向重節奏拳掌特技，與 `Wait 1` 的 `yu needle / blood ten` 節奏完全不同。
- 因為出手慢、段數較少，所以單段威力應明顯高於快節奏連擊技。
- 本批先只回填 `Value` 階梯，保留其重節奏與無兵器拳掌 identity。

## Batch AL Result

### Scope

- `dark word`

### Runtime Changes

`dark word`

- before: `20 x 8`
- after: `140, 165, 195, 230, 270, 320, 380, 450`
- average: `268.75`

### Design Notes

- 本批讓 `dark word` 的單段威力高於快節奏針/刀技，但總體仍保留漸進的高階成長。
- 這樣比較符合 `Wait 12` 的重節奏模板，不會和 `Wait 1` 類型混在一起。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-al.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AH Pre-Check

### Scope

- `dragon leg`

### Reference Basis

- runtime `skill/d/dragonleg.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 12 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `dragon leg`
  - `family = legacy-page:dragon leg`
  - combat 維度顯示 `10` 段 `Value 20`
- `area/limbo/obj/245.obj`
  - 仍存在 `dragon leg book`

### Mandatory Pre-Check Snapshot

`dragon leg`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 12`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `10`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向高階腿法，和 `wind leg` 類似屬於偏重節奏、非快攻型的腿路。
- 在 `10` 段完整描述下仍維持全 `20`，明顯屬於清值模板。
- 本批先只回填 `Value` 階梯，保留原本節奏與腿法 identity。

## Batch AH Result

### Scope

- `dragon leg`

### Runtime Changes

`dragon leg`

- before: `20 x 10`
- after: `145, 165, 190, 220, 255, 295, 340, 395, 460, 535`
- average: `300.0`

### Design Notes

- 本批把 `dragon leg` 定位成高於一般腿法、後段爆發更重的高階長節奏腿技。
- 這樣可以和已補過的 `wind leg` 保持同系但不同峰值的層次差異。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ai.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AI Pre-Check

### Scope

- `thunder hammer`

### Reference Basis

- runtime `skill/t/thunder_hammer.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 1 / Weapon WEAPON_HAMMER`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `thunder hammer`
  - `family = legacy-page:thunder hammer`
  - combat 維度顯示 `8` 段 `Value 20`

### Mandatory Pre-Check Snapshot

`thunder hammer`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 1`
- weapon / check: `WEAPON_HAMMER / -`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `8`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向特殊槌法，`Wait 1` 顯示它節奏極快，因此不能用重節奏刀腿技的梯度直接套上去。
- 雖然平均應低於慢節奏高階單點，但 `8` 段全 `20` 仍然明顯失真。
- 本批先只回填 `Value` 階梯，保留其極快節奏與槌類 identity。

## Batch AI Result

### Scope

- `thunder hammer`

### Runtime Changes

`thunder hammer`

- before: `20 x 8`
- after: `130, 155, 185, 220, 260, 310, 370, 440`
- average: `258.75`

### Design Notes

- 本批刻意讓 `thunder hammer` 的平均值低於同級慢節奏重技，但後段仍保留明顯成長。
- 這樣比較符合 `Wait 1` 的高速輸出型定位，不會把它拉成過重的大錘模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ai.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AG Pre-Check

### Scope

- `wind leg`

### Reference Basis

- runtime `skill/w/windleg.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 12 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `wind leg`
  - `family = legacy-page:wind leg`
  - combat 維度顯示 `9` 段 `Value 20`
- `area/limbo/obj/219.obj`
  - 仍存在 `wind leg book`

### Mandatory Pre-Check Snapshot

`wind leg`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 12`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `9`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 雖然目前沒有抓到獨立舊站技能頁，但 runtime、current-game 與祕笈樣本已足以確認它是玩家向 legacy 腿法。
- `Wait 12` 顯示它不是快節奏拳腳，而是偏重節奏、重份量的腿法單點技能。
- 本批先只回填 `Value` 階梯，保留原本 `Chance / Wait / Cost / Check`。

## Batch AG Result

### Scope

- `wind leg`

### Runtime Changes

`wind leg`

- before: `20 x 9`
- after: `135, 155, 180, 210, 245, 285, 330, 385, 450`
- average: `263.89`

### Design Notes

- 本批把 `wind leg` 定位成偏重節奏、後段加速拉高的高階腿法。
- 這樣可以保留它和較快的拳掌系單點技能的區別，同時脫離清值模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ag.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AF Pre-Check

### Scope

- `sky blade`
- `dream soul`
- `dream tear`

### Reference Basis

- `docs/3yWebsite/skill/blade.html`
  - 舊站明確收錄 `dream soul`
  - 顯示其為高階女性向特殊刀法，且帶職業/屬性/前置限制
- `docs/current-game/skills.json`
  - current-game 已收錄 `sky blade / dream soul / dream tear`
  - 三者皆為獨立 `legacy-page:*` family
  - runtime combat 維度仍顯示 `Value` 全 `20`
- runtime
  - `skill/s/sky_blade.ski`
  - `skill/d/dream_soul.ski`
  - `skill/d/dream_tear.ski`
- area samples
  - `area/loyang/mob/598.mob` -> `Enable 100 'sky blade'`
  - `area/loyang/mob/599.mob` -> `Enable 100 'dream soul'`
  - `area/loyang/mob/601.mob` -> `Enable 100 'dream tear'`

### Mandatory Pre-Check Snapshot

`sky blade`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `40 / COST_MOVE / 10`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `12`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

`dream soul`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `30 / COST_MOVE / 16`
- weapon / check: `WEAPON_BLADE / check_blade_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `8`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`
- special role note:
  - 舊站明確標為高階女性 special blade

`dream tear`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `25 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `YES / NO / YES`
- damage entries: `9`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這三個技能都不是一般新手鏈，而是高階特殊單點技能。
- `598 / 599 / 601` 已確認是高階 special sample，因此本批只重建 skill 模板，不回頭調 mob 端 explicit `Enable 100`。
- 三者的 `Wait / Cost / Weapon / Check` 差異明顯，因此只回填 `Value`，保留各自 identity：
  - `sky blade`：高成本、長段數、大刀
  - `dream soul`：更重節奏、女性 special blade
  - `dream tear`：節奏較快、無兵器拳掌式終技

## Batch AF Result

### Scope

- `sky blade`
- `dream soul`
- `dream tear`

### Runtime Changes

`sky blade`

- before: `20 x 12`
- after: `170, 195, 220, 250, 285, 325, 370, 420, 475, 535, 600, 670`
- average: `376.25`

`dream soul`

- before: `20 x 8`
- after: `190, 220, 255, 295, 340, 390, 450, 520`
- average: `332.5`

`dream tear`

- before: `20 x 9`
- after: `145, 170, 195, 225, 260, 300, 345, 395, 455`
- average: `276.67`

### Design Notes

- `sky blade` 被定位成高階大刀單點技能，整體高於一般中高階 blade，但仍低於極端傳說級模板。
- `dream soul` 保留其重節奏、高限制、情緒型特殊刀法的定位，讓單段威力高於一般 skill。
- `dream tear` 則維持較快節奏與較輕成本，因此平均 `Value` 低於前兩者，但已不再是清值模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-af.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AB Pre-Check

### Scope

- `cloud fist`

### Reference Basis

- runtime `skill/c/cloud_fist.ski`
  - `Value` 全 `20`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
  - `Check check_unrigid_attack`
- `docs/current-game/skills.json`
  - current-game 已收錄 `cloud fist`
  - `family = legacy-page:cloud fist`
  - runtime combat 維度顯示 `11` 段 `Value 20`
- `area/limbo/obj/263.obj`
  - 仍存在 `cloud fist book`
  - 證明它不是純 NPC-only 或廢棄殘檔

### Mandatory Pre-Check Snapshot

`cloud fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 10`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `11`
- chance set: `10`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 雖然目前沒抓到獨立舊站技能頁，但 runtime、current-game 與祕笈樣本足以確認這是玩家向 legacy 高階掌法。
- 它有 `11` 段獨立傷害描述，且整條仍被壓成 `20`，明顯屬於清值模板。
- 本批先只回填 `Value` 階梯，保留原本的 `Chance / Wait / Cost / Check`。

## Batch AB Result

### Scope

- `cloud fist`

### Runtime Changes

`cloud fist`

- before: `20 x 11`
- after: `130, 150, 170, 195, 220, 250, 285, 325, 370, 420, 480`
- average: `272.27`

### Design Notes

- 本批把 `cloud fist` 定位成高於中階拳掌、但仍低於最頂階爆發單點的 high-tier palm template。
- 這樣可以先恢復它作為玩家向祕笈技能的成立梯度，不去抹平其他拳法系既有個性。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ae.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AD Pre-Check

### Scope

- `taichi fist`

### Reference Basis

- runtime `skill/t/taichi_fist.ski`
  - `Value` 全 `20`
  - `Cost 20 / Wait 5 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `taichi fist`
  - `family = legacy-page:taichi fist`
  - combat 維度顯示 `8` 段 `Value 20`

### Mandatory Pre-Check Snapshot

`taichi fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `20 / COST_MOVE / 5`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `8`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向單點拳法，且 `Wait 5` 屬偏快節奏的高階拳掌模板。
- 在完整 `8` 段傷害描述下仍維持全 `20`，顯示它被壓平成清值模板。
- 本批先只回填 `Value` 階梯，保留原本的節奏與太極拳風格。

## Batch AD Result

### Scope

- `taichi fist`

### Runtime Changes

`taichi fist`

- before: `20 x 8`
- after: `125, 145, 170, 195, 225, 260, 305, 360`
- average: `223.13`

### Design Notes

- 本批把 `taichi fist` 定位成節奏較快、輸出中高階、偏技巧型的單點拳法。
- 這樣能保留它和重爆發掌法的差異，不把所有高階空手技拉成同一個模板。

### Validation

- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src merc"`
- `wsl.exe bash -lc "cd /mnt/h/repos/merc-fju-3.0 && make -C src -f Makefile.lin merc"`
- smoke test:
  - 使用臨時 `merc.test.ini`
  - 改用 `MUD PORT 5838 / 6234 / 6888`
  - 改用 `IPC KEY 5585`
- 檢查：
  - `log/smoke-batch-ae.log`
    - 出現 `三國歪傳之降龍伏虎開始正常運作`
  - `debug/failenable`
    - 無新增內容
  - `debug/failload`
    - 無新增內容
  - `debug/error`
    - 只有 smoke timeout 收尾時的關機 noise

## Batch AE Pre-Check

### Scope

- `dragon shout`

### Reference Basis

- runtime `skill/d/dragon_shout.ski`
  - `Value` 全 `20`
  - `Cost 15 / Wait 11 / Weapon WEAPON_SWORD / Check check_sword_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `dragon shout`
  - `family = legacy-page:dragon shout`
  - combat 維度顯示 `7` 段 `Value 20`

### Mandatory Pre-Check Snapshot

`dragon shout`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `15 / COST_MOVE / 11`
- weapon / check: `WEAPON_SWORD / check_sword_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `7`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 這是玩家向高階單點劍法，`Wait 11` 顯示其節奏比一般中階劍技更重、更慢。
- 以目前完整招式描述與 current-game family 來看，全 `20` 明顯不是合理的終態。
- 本批先只回填 `Value` 階梯，保留原本劍系身份與重節奏。

## Batch AE Result

### Scope

- `dragon shout`

### Runtime Changes

`dragon shout`

- before: `20 x 7`
- after: `145, 170, 200, 235, 275, 320, 380`
- average: `246.43`

### Design Notes

- 本批把 `dragon shout` 定位成偏重節奏、每段更有份量的高階劍法。
- 這樣可以和較快或段數較多的劍系單點技能維持辨識度。

### Validation

- 待本批 build / smoke test 完成後補入

## Batch AC Pre-Check

### Scope

- `dragon fist`

### Reference Basis

- runtime `skill/d/dragonfist.ski`
  - `Value` 全 `20`
  - `Cost 50 / Wait 10 / Check check_unrigid_attack`
  - `CanAsk NO / Teach NO / Valid NO / Enable YES`
- `docs/current-game/skills.json`
  - current-game 已收錄 `dragon fist`
  - `family = legacy-page:dragon fist`
  - combat 維度顯示 `18` 段 `Value 20`
- `area/limbo/obj/252.obj`
  - 仍存在 `dragon fist book`
- `area/limbo/mob/6.mob`
  - 仍有 `Enable 100 'dragon fist'` 與對應施放樣本

### Mandatory Pre-Check Snapshot

`dragon fist`

- type: `TAR_CHAR_OFFENSIVE`
- cost / costtype / wait: `50 / COST_MOVE / 10`
- weapon / check: `- / check_unrigid_attack`
- canask / teach / valid: `NO / NO / NO`
- enable: `YES`
- damage entries: `18`
- chance set: `20`
- value set before rebuild: `20`
- parry set: `0`

### Interpretation

- 雖然目前沒抓到獨立舊站頁面，但 runtime、current-game、祕笈與 limbo 樣本都足以確認這是玩家向高階掌法，而不是單純 NPC 殘檔。
- `Cost 50` 加上 `18` 段完整招式，卻維持全 `20`，幾乎可以直接視為高階模板被清值。
- 本批先只回填 `Value` 階梯，保留原本的 `Chance / Wait / Cost / Check`。

## Batch AC Result

### Scope

- `dragon fist`

### Runtime Changes

`dragon fist`

- before: `20 x 18`
- after: `150, 170, 190, 210, 235, 260, 290, 325, 360, 400, 445, 495, 550, 610, 675, 745, 820, 900`
- average: `435.56`

### Design Notes

- 本批把 `dragon fist` 定位成傳說級、超高成本、長段數掌法模板，整體高於目前已補的多數拳掌單點技能。
- 這樣可以恢復 `降龍十八掌` 作為高階祕笈技能的存在感，同時不去改動它原本的出手節奏與命中分布。

### Validation

- 待本批 build / smoke test 完成後補入
