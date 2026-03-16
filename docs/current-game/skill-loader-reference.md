---
layout: default
title: Skill Loader Reference
---

# `.ski` 進階 Loader Reference

這頁補充第一頁 [`.ski` 技能檔格式說明](./skill-file-format.html) 沒有展開的進階欄位：

- `#Affect`
- `#Restrict`
- `#Damage Effect`
- `Slot / Check / Routine / Function`

重點不是列出所有歷史設計，而是對齊「目前 repo 的 loader 實際怎麼讀」。

## `#Affect`

`.ski` 裡的 `#Affect` 會先走 `src/load.c` 的 `load_affect()`，再被 `load_skill()` 接手。

支援欄位：

| 欄位 | 用途 |
| --- | --- |
| `Type` | affect 對應 skill/slot |
| `Location` | 影響位置 |
| `Modifier` / `Value` | 影響數值 |
| `End` | 結束 |

### 重要差異

skill 檔裡的 `#Affect` 和一般物件/其他資料來源的 affect block 不完全一樣，因為 `load_skill()` 讀完後還會再強制設定：

- `duration = -1`
- `location = 0`
- `modifier = 0`
- `level = MAX_LEVEL`

也就是說，在目前 skill loader 路徑裡：

- `Type` 最關鍵
- `Location` / `Modifier` 即使有寫，也會被 skill loader 正規化

所以像 `blindness.ski` 這種寫法：

```text
#Affect
Type            SLOT_BLINDNESS
Location        AFF_NONE
End
```

比較適合解讀成「這個技能帶著一個 affect 身分」，而不是把它當成一般數值 buff/debuff 描述區。

### 常見值

`Type` 常見填法：

- `SLOT_BLINDNESS`
- `SLOT_CHARM_PERSON`
- `SLOT_SLEEP`

`Location` 若只是佔位，常看到：

- `AFF_NONE`
- `AFFECT_NONE`

如果之後要做更完整的 effect/buff schema，最好另外檢查實際施法函數，而不要只憑 `#Affect`。

## `#Restrict`

`#Restrict` 由 `load_restrict()` 解析，結構上支援，但目前 `skill/*.ski` 幾乎沒有實際例子，所以它比較像「loader 已支援的進階欄位」。

支援欄位：

| 欄位 | 用途 |
| --- | --- |
| `Type` | 限制型別 |
| `Value` | 主數值 |
| `ViceValue` | 副數值 |
| `Occassion` | 限制時機 |
| `Skill` | 用技能名稱轉成 slot |
| `End` | 結束 |

### `Type` 可用值

來自 `data/symbol.def` / `src/merc.h`：

| 值 | 意思 |
| --- | --- |
| `RES_STR` | 力量限制 |
| `RES_INT` | 智力限制 |
| `RES_WIS` | 學識限制 |
| `RES_DEX` | 敏捷限制 |
| `RES_CON` | 體格限制 |
| `RES_HP` | HP 限制 |
| `RES_MANA` | MP 限制 |
| `RES_MOVE` | MV 限制 |
| `RES_CLASS` | 職業限制 |
| `RES_TRUST` | trust 限制 |
| `RES_SKILL` | 技能前置限制 |
| `RES_NOSKILL` | 相剋技能限制 |
| `RES_SEX` | 性別限制 |
| `RES_LEVEL` | 等級限制 |
| `RES_ALIGN` | 陣營限制 |

### 讀法

若你未來真的在 `.ski` 用它，推薦用這種心智模型：

- `Type + Value` = 最基本限制
- `ViceValue` = 第二參數
- `Skill` = 當 `Type` 是 `RES_SKILL` 時，用可讀技能名轉成 slot

範例概念：

```text
#Restrict
Type            RES_LEVEL
Value           50
End
```

代表技能需要某種等級限制。

另一種概念例子：

```text
#Restrict
Type            RES_SKILL
Skill           hua sword
Value           80
End
```

代表某技能熟練度要先達某個門檻。

## `#Damage Effect`

`#Damage` 內可加 `Effect` 行，會掛到 `DAMAGE_DATA.effect`。

格式概念：

```text
Effect          <EFFECT_*> <value1> <value2> <value3> ...
```

目前 parser 支援的 effect type：

| 值 | 意思 |
| --- | --- |
| `EFFECT_VICTIM_MANA` | 扣目標 mana |
| `EFFECT_SELF_MANA` | 扣自己 mana |
| `EFFECT_VICTIM_MOVE` | 扣目標 move |
| `EFFECT_SELF_MOVE` | 扣自己 move |
| `EFFECT_VICTIM_BLINDNESS` | 使目標眼盲 |
| `EFFECT_VICTIM_CURSE` | 使目標詛咒 |
| `EFFECT_VICTIM_POISON` | 使目標中毒 |
| `EFFECT_VICTIM_SLEEP` | 使目標睡眠 |
| `EFFECT_VICTIM_PARA` | 使目標麻痺 |
| `EFFECT_VICTIM_FAERIE_FIRE` | 使目標帶 faerie fire |
| `EFFECT_VICTIM_HIT` | 影響目標 HP |
| `EFFECT_SELF_HIT` | 影響自己 HP |
| `EFFECT_HIT_DIE` | 特殊致死/重擊類效果 |

### 注意點

- parser 會把 effect 的數值塞進 `value[]`
- 第三個數值目前會被當成機率檢查，必須落在 `0-100`
- 這表示 `Effect` 不是純文字備註，而是會被 loader 視為有結構的資料

目前 skill 檔內幾乎沒有現成例子，所以如果你要開始用它，最好先用單一技能做 smoke test，不要一次鋪一整批。

## `Slot`

`Slot` 是整個 skill registry 的核心索引。

規則：

- 必須對應 `src/merc.h` 裡已存在的 `SLOT_*`
- `data/symbol.def` 也要有相同符號
- `skill/skill.lst` 的 key、檔名、`Name` 最好一起對齊
- 不能重複

例：

```text
Slot            SLOT_GOLD_BLADE
```

如果 `Slot` 不存在或重複，loader 會報錯。

## `Check`

`Check` 不是 enum，而是函數名稱字串，會透過 `src/function.c` 的 `check_function_name()` 轉成 function pointer。

目前 lookup 內建的值包括：

- `check_sword_attack`
- `check_unrigid_attack`
- `check_pc_attack`
- `check_spear_attack`
- `check_blade_attack`
- `check_whip_attack`
- `check_dagger_attack`
- `check_axe_attack`
- `check_pen_attack`
- `check_bow_attack`
- `check_hammer_attack`
- `check_club_attack`

例：

```text
Check           check_blade_attack~
```

代表這個技能走刀系攻擊檢查流程。

## `Routine`

`Routine` 是寫在 `#Damage` 裡的額外 routine function。

它會透過 `src/function.c` 的 `check_routine_name()` 解析。

目前 lookup 幾乎只有：

- `routine_none`

所以這欄位目前屬於「已支援但幾乎未展開」的 extension point。

## `Function`

`Function` 是技能主執行函數，會透過 `skill_function_name()` 解析。

它不像 `Slot` 那樣是封閉 enum，比較像一個 runtime 白名單。常見型態：

- `cast_blindness`
- `cast_charm_person`
- `cast_refresh`
- `cast_make_sword`
- `skill_hide`
- `skill_sneak`
- `cast_backstab`

如果你要知道某個名字能不能用，最直接的檢查方法就是看：

- `src/function.c`
- 以及 repo 內其他 `.ski` 的既有寫法

## 實務建議

如果你的目標是長期維護 `.ski` 文件，我會建議把查表分三層：

1. [`.ski` 技能檔格式說明](./skill-file-format.html)
   - 給日常快速查欄位
2. 這一頁
   - 給 loader 細節、少用欄位與 enum/function 對照
3. [`.ski` 常數查表](./skill-constants.html)
   - 專門收 `SLOT_*`、`APPLY_*`、`EFFECT_*`、`RES_*`、`ATTACK_*`

> 來源：`src/load.c`、`src/function.c`、`src/merc.h`、`data/symbol.def`、`skill/b/blindness.ski`、`skill/c/charm_person.ski`
