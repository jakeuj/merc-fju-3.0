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

這代表現況很可能出現：

- 新手技與高階技實際威力接近
- 宗師級 NPC 掛高階 legacy skill，卻仍可能被 loader 判定為「太差」
- 新 area / teacher / boss 設計若直接沿用舊技能名，會持續繼承失真的底層模板

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

## Core Hypothesis

目前最值得優先驗證的假設是：

- 釋出版曾把大量 legacy skill 的 `#Damage Value` 先重置為 `20`
- 這不是單一技能偶發，而是系統性清值
- failenable 的大量「太差」警告，至少有一部分正是由這個清值造成

## Execution Rules

1. 不要一次全域重寫所有 skill。
2. 先以「玩家可學、舊站有清楚升階鏈、目前 runtime 又幾乎全是 `20`」的技能鏈優先。
3. 每次只修 1 到 2 條鏈，並保留明確的 before/after 紀錄。
4. 修 skill value 後，要回頭抽查：
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

- 建立第一條 dodge legacy ladder
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

## Resume State

目前狀態：

- `status = ready_for_batch_a`
- `current_focus = offensive sword ladder`
- `current_batch = Batch A`

## Immediate Next Steps

1. 盤 `hua sword` / `fonxan sword` / `dragon sleeve sword` 現行 `#Damage Value`
2. 依 `players.json` / `skills.json` 定出入門、中階、高階的目標梯度
3. 小批次修 skill 檔
4. build + smoke test
5. 抽對應 mob / failenable 結果回寫到 `docs/current-game/skill-combat-audit.json`

## Next Prompt

可直接續跑的 prompt：

> 請直接續做 `plans/0003-legacy-skill-damage-audit.md` 的 Batch A，先處理 `hua sword`、`fonxan sword`、`dragon sleeve sword` 的 damage ladder 重建。先讀 `docs/3yWebsite/docs/data/players.json`、`docs/3yWebsite/docs/data/skills.json`、對應 `skill/*.ski`，然後直接修改 skill value、做 build / smoke test、更新 plan 與必要的 audit。
