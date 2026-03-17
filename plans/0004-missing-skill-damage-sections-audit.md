# Missing Skill Damage Sections Audit Plan

## Summary

這份計畫處理的是和 `0003` 不同的一條技能審計線：

- `0003` 解的是：skill 有 `#Damage`，但 `Value` 被系統性清成 `20`
- `0004` 解的是：player-facing offensive skill 在 `.ski` 裡根本沒有 `#Damage`

這裡不能直接把所有空的 `damage_values` 都當成 runtime 缺損，因為目前 repo 已確認存在兩種不同來源：

- `data-driven`
  - 傷害模型直接寫在 `.ski -> #Damage`
- `code-driven`
  - `.ski` 只掛 `Function`
  - 真正的傷害模型寫在 `src/spell.c` 或 `src/ex_spell.c` 的 `cast_*()` / `spell_*()` 內

因此這份計畫的核心不是「看到空陣列就補 `.ski #Damage`」，而是先分類，再決定是否要修 runtime data。

## Why This Exists

目前 `docs/current-game/skills.json` 與可讀頁會把沒有 `.ski #Damage` 的 offensive skill 呈現成：

- `Damage values: []`
- `Chance values: []`
- `Parry values: []`
- `Innate values: []`

這種呈現會讓 player-facing skill 看起來像：

- 進階後沒有實際作用
- 或 skill data 壞掉

但 source pre-check 已證明，至少 bow 主鏈中的：

- `shoot sun`
- `water cloud blast`
- `fun wu blast`

不是同一種問題。

## Current Baseline Snapshot

目前以 current-game registry 為基線重新掃描：

- player-facing
- `runtime.type = TAR_CHAR_OFFENSIVE`
- `combat_dimensions.damage_values = []`

共 `42` 筆。

依 source pre-check 初步可分成：

- `34` 筆 `code-driven offensive exception`
  - 在 `src/spell.c` / `src/ex_spell.c` 有對應 function
  - 而且 function 內可確認有 `spell_damage()`、`damage()` 或 `raw_kill()` 路徑
- `8` 筆 `needs review`
  - 有對應 function
  - 但目前看不到直接傷害呼叫，較像 debuff / 特效 / 特殊處理

目前首批 `needs review` 清單：

- `cannibal`
- `crash weapon`
- `defloration`
- `energy drain`
- `know alignment`
- `magic power`
- `slow`
- `weaken`

這 `8` 筆在分類完成前，不應直接補假 `#Damage`。

## Source Of Truth

runtime 與 damage path 以 source 為準：

- `skill/*.ski`
- `skill/skill.lst`
- `src/spell.c`
- `src/ex_spell.c`
- `src/function.c`
- `src/load.c`

技能鏈與玩家向定位仍以 reference baseline 為準：

- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/newhand/newbies/index.html`

current-game 文件層：

- `docs/current-game/skills.json`
- `docs/current-game/skills.md`
- `docs/current-game/skills/*.md`

## Classification Rules

每個 player-facing offensive 且 `damage_values = []` 的技能，固定記錄：

- `english_name / chinese_name`
- `skill_file`
- `legacy previous / next`
- `.ski` 的 `Function`
- `.ski` 是否真的沒有 `#Damage`
- 是否有對應 `cast_*()` / `spell_*()` source block
- source block 是否有直接傷害呼叫
- 若有，記錄 code path、damage 摘要、repeat loop、weapon multiplier

最終分類只允許三種：

### 1. `data-driven gap`

條件：

- 技能應靠 `.ski #Damage` 建模
- 目前 `.ski` 沒有 `#Damage`
- 也找不到可信的 code-driven damage path

處置：

- 補完整 `#Damage`
- 不只補 `Value`
- 連同 `Chance / Parry / Innate / Situs / Description` 一起補

### 2. `code-driven offensive exception`

條件：

- 技能沒有 `.ski #Damage`
- 但在 `src/spell.c` / `src/ex_spell.c` 有對應 damage path

處置：

- 不補假 `#Damage`
- 在 current-game registry / 可讀頁明確標示 `Damage model = code-driven`
- 記錄 code path 與 damage summary

### 3. `needs review`

條件：

- 技能沒有 `.ski #Damage`
- source block 存在
- 但目前看不到直接傷害呼叫，或行為更像 debuff / 特效 / 複合效果

處置：

- 先保留
- 不猜數值
- 後續按單技能語義重判是否應改 type、補 docs，或補 runtime data

## Batch A Bow Baseline

第一批固定以弓法主鏈建立基準：

### `shoot sun`

- 類型：`data-driven root`
- `.ski` 有完整 `#Damage`
- 目前保留為 bow 主鏈根技能基線

### `water cloud blast`

- 類型：`code-driven offensive exception`
- runtime file 無 `#Damage`
- 真正傷害在 `src/spell.c -> cast_water_cloud_blast()`
- code-side base damage ladder：
  - `300, 350, 400, 450, 500, 600, 700, 800, 900, 1000`
- repeat loop：
  - `for (tt = 0; tt <= level / 33; tt++)`
- weapon multiplier：
  - bow `value[1..2]`

### `fun wu blast`

- 類型：`code-driven offensive exception`
- runtime file 無 `#Damage`
- 真正傷害在 `src/spell.c -> cast_fun_wu_blast()`
- code-side base damage ladder：
  - `450, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1400`
- repeat loop：
  - `for (tt = 0; tt <= level / 20; tt++)`
- weapon multiplier：
  - bow `value[1..2]`

Batch A 的目標不是修改 bow runtime data，而是把：

- `shoot sun = data-driven`
- `water cloud blast / fun wu blast = code-driven`

這個差異正式建模到 current-game docs 與 registry。

## Registry / Docs Changes

`docs/current-game/skills.json` 的 `combat_dimensions` 需要新增：

- `damage_source`
  - `data-driven`
  - `code-driven`
  - `unresolved`
- `damage_gap_classification`
  - `code-driven offensive exception`
  - `needs review`
- `code_path`
- `code_damage_summary`

可讀頁生成規則：

- `data-driven`
  - 照常顯示 arrays
- `code-driven`
  - 顯示 `Damage model: code-driven`
  - 顯示 `Code path`
  - 顯示 `Code damage summary`
  - 不再只留下空陣列造成誤解
- `unresolved`
  - 顯示 `Damage model: unresolved`
  - 顯示 `needs review`

## Runtime Edit Rules

只有在分類為 `data-driven gap` 時，才允許修改 `.ski`：

- 保留既有 `Function / Cost / Wait / CostType / Weapon / Check`
- 補完整 `#Damage` 區塊
- `Chance / Parry / Innate` 以鏈上相鄰技能與同武器同職系模型為基準

若技能已確認為 `code-driven offensive exception`：

- 不改 `.ski`
- 不補 fake `#Damage`

## Validation

每一輪至少做：

- 重新產出 player-facing offensive 且 `damage_values = []` 的分類清單
- 抽查 `shoot sun / water cloud blast / fun wu blast`
- 重建：
  - `python -X utf8 scripts/build_current_game_skill_registry.py`
  - `python -X utf8 scripts/generate_current_game_skills_pages.py`
- 編譯：
  - `make -C src merc`
  - `make -C src -f Makefile.lin merc`
- smoke test：
  - 臨時 `merc.test.ini`
  - 檢查 `debug/failenable`
  - 檢查 `debug/failload`

## Acceptance Criteria

- `water cloud blast / fun wu blast` 在 current-game docs 中被明確標為 `code-driven`
- bow 可讀頁不再讓它們看起來像「進階後技能沒作用」
- 所有 player-facing offensive 且 `damage_values = []` 的樣本，都能在 registry 裡看到分類與證據
- 若日後出現真正的 `data-driven gap`，可以沿這份計畫直接補 `.ski #Damage`，而不會誤傷 code-driven spell
