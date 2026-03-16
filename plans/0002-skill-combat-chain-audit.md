# 技能戰鬥鏈資料盤點與重建計畫

## Summary

這份計畫把「NPC 技能實效偏弱是否來自釋出版清值」正式落成為可執行的全域審計流程。
本輪範圍只鎖定技能戰鬥鏈，不擴大到掉寶經濟、一般物件數值或全 area 生態平衡。

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
    - 舊站 `skills.json` 已確認 `cloud steps -> gdragon steps` 是既有步法升階鏈，因此 `gdragon steps` 可保留作 legacy 對照，但 `two sword 1` 仍明顯脫離目前守軍軍旅技能定位

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

## Ref Metadata

- `ref_inputs_used`
  - `ref/Readme.md`
- `ref_inputs_deferred`
  - `world-graph.json`
  - `三國-MUD-世界設計總藍圖-Architecture-Map.md`
  - `三國-MUD-題材分布表.md`
- `theme_basis`
  - 這輪以 loyang / beiping 現有守軍、皇城、夜行 NPC 的舊版體感與現行 runtime 身份戰技補完為主，不以新世界藍圖重寫強度體系
- `compliance_check`
  - 本輪只建立全域計畫與機器可讀審計台帳，未修改 runtime data；未動用 area tracker，也未改動 area load order
