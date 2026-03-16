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

技能鏈與玩家體感基線以舊站資料為準：

- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/newhand/newbies/index.html`

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

## Execution Rules

1. 不要一次全域重寫所有 skill。
2. 先以「玩家可學、舊站有清楚升階鏈、目前 runtime 又幾乎全是 `20`」的技能鏈優先。
3. 每次只修 1 到 2 條鏈，並保留明確的 before/after 紀錄。
4. 每批開工前，先做 `Mandatory Pre-Check`。
5. 修 skill value 後，要回頭抽查：
   - 對應玩家向技能體感是否仍合理
   - 對應 mob 是否不再被 failenable 判成「太差」
   - 是否造成低階玩家技能過度膨脹

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

- `status = batch_b_implemented`
- `current_focus = dodge ladder`
- `current_batch = Batch B`

## Immediate Next Steps

1. 直接轉入 Batch C，先完成 `long fist / lung shan / tackle` 的多因子 pre-check
2. 盤出 `long fist` 目前掛在城市 / 教學 / 服務 NPC 上的樣本，區分入門自保與身份錯位
3. 後續若再有 city / teacher 樣本仍掛 `gdragon steps`，以 `cloud steps` 是否更符合其自保定位為優先判準

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
- 下一個關鍵 decision point 已轉為 Batch C 的 `long fist / lung shan / tackle`
