---
layout: default
title: Skill File Format
---

# `.ski` 技能檔格式說明

這頁說明目前 repo 內 `skill/*.ski` 的欄位用途、常見設定值，以及它們對應到哪個 runtime loader。

最適合把這份文件放在 `docs/current-game/`：

- 這是現行 runtime schema，不是舊站鏡像內容。
- GitHub Pages 會直接發佈 `docs/`，之後可以從網站直接查。
- 後續若要補更多欄位、例子或 parser 注意事項，也能和 `skills.md`、`skills.json` 放在同一條 current-game 文件線上。

## Source Of Truth

`.ski` 說明的主要依據是：

- `src/load.c`
  - `load_skill()`
  - `load_damage()`
- `src/body.c`
  - `random_situs()`
- `src/merc.h`
  - `SKILL_DATA`
  - `DAMAGE_DATA`
  - `LIMIT_DATA`
- `data/symbol.def`
  - `TAR_*`
  - `COST_*`
  - `WEAPON_*`
  - `RATING_*`
  - `ATTACK_*`
- `data/situs.txt`
  - 實際部位權重與名稱

## 檔案位置與載入方式

- 索引檔：`skill/skill.lst`
- 實際技能檔：`skill/<首字母>/<name>.ski`
- loader 會先讀 `skill/skill.lst`，再依英文名稱首字母去對應子資料夾。

例：

- `gold_blade`
- 實際檔案在 `skill/g/gold_blade.ski`

## 以 `gold_blade.ski` 為例

`skill/g/gold_blade.ski` 是一個典型的近戰攻擊技能，主體可分成兩層：

1. 技能主欄位
2. 多個 `#Damage` 區塊

技能主欄位決定這個技能「是什麼、誰能用、怎麼啟用、耗什麼資源」。
`#Damage` 區塊則決定「一招一式的敘述、機率、傷害、命中部位與附帶效果」。

## 主欄位

| 欄位 | 用途 | 例子 |
| --- | --- | --- |
| `Name` | 英文技能 key，會被指令、NPC、其他資料引用。 | `gold blade~` |
| `Cname` | 中文名稱。 | `紫金六陽刀法~` |
| `Slot` | 對應 `SLOT_*` 常數，必須全域唯一。 | `SLOT_GOLD_BLADE` |
| `Check` | 指向 skill check function。 | `check_blade_attack~` |
| `Position` | 可施放/施展時要求的人物狀態。 | `POS_FIGHTING` |
| `Type` | 技能目標型態。 | `TAR_CHAR_OFFENSIVE` |
| `Costtype` | 消耗哪種資源。 | `COST_MOVE` |
| `Cost` | 每次使用的消耗量。 | `15` |
| `Wait` | wait state。 | `10` |
| `Exp` | 技能經驗基值。 | `15` |
| `Associate` | 升階或關聯技能；`-1` 代表沒有。 | `-1` |
| `Degree` | 技能程度或難度參數。 | `5` |
| `Affect` / `AffectID` | 對應 affect 類型。沒有就填 `AFFECT_NONE`。 | `AFFECT_NONE` |
| `CanAsk` | NPC 可否被 `ask` 相關流程查詢。 | `NO` |
| `Valid` | 是否視為正式可用技能。很多 NPC-only / placeholder 會是 `NO`。 | `NO` |
| `Cast` | 是否能以 cast/主動施展流程進入。 | `YES` |
| `Concentration` | 是否要求專注。 | `NO` |
| `Teach` | NPC 是否能教。 | `NO` |
| `SaySpell` | 是否需要說出咒語。 | `NO` |
| `Enable` | 是否可被 enable 成戰鬥技能。 | `YES` |
| `Weapon` | 對應武器類型。 | `WEAPON_BLADE` |
| `Rating` | 技能分類。 | `RATING_SKILL` |
| `Innate` | 是否 innate。 | `NO` |
| `Ply` | ply 相關限制；沒有通常是 `-1`。 | `-1` |
| `Qutoient` | 熟練度/等級門檻計算倍率。拼字就是 repo 現況的 `Qutoient`。 | `1` |
| `Adeptation` | 預設熟練度或 innate 熟練度。 | `0` |
| `Limit` | 每個職業的可學等級與熟練度上限。可出現多行。 | `CLASS_GENERAL 1 90` |
| `Help` | 額外 help 文字。空字串常寫成 `~`。 | `~` |

## `#Damage` 區塊

每個 `#Damage` 都是一個可被抽到的招式片段。

| 欄位 | 用途 | 例子 |
| --- | --- | --- |
| `Description` | ACT 訊息模板。 | `$W$n側身橫鋤...$Z。~` |
| `Chance` | 這招被選中的權重。最後會累加到 skill 的總機率。 | `10` |
| `Value` | 傷害數值基線。 | `20` |
| `Parry` | 是否偏向可被格擋或格擋調整值。 | `0` |
| `Situs` | 命中部位 mask。 | `ATTACK_RANDOM` |
| `Innate` | 對應物件/倍數；沒有通常是 `0 0`。 | `0 0` |
| `Effect` | 額外效果，可做失明、毒、扣 mana 等。 | 此例沒有 |
| `Routine` | 額外 damage routine。 | 此例沒有 |
| `ViceValue` | 次要數值；不是每個技能都用。 | 此例沒有 |

## 常見枚舉值

### `Type`

來自 `data/symbol.def` 的 `TAR_*`：

| 值 | 意思 |
| --- | --- |
| `TAR_IGNORE` | 技能自己決定目標 |
| `TAR_CHAR_OFFENSIVE` | 攻擊型，通常對敵方角色 |
| `TAR_CHAR_DEFENSIVE` | 防禦或輔助型 |
| `TAR_CHAR_SELF` | 只能對自己 |
| `TAR_OBJ_INV` | 作用於背包內物件 |
| `TAR_DODGE` | 閃躲型技能 |
| `TAR_FLEE` | 逃跑型技能 |
| `TAR_MEDITATION` | 冥想型技能 |
| `TAR_MOUNT` | 騎乘型技能 |
| `TAR_NO_CAST` | 不走一般 cast 流程 |

### `Costtype`

| 值 | 意思 |
| --- | --- |
| `COST_HIT` | 消耗 HP |
| `COST_MANA` | 消耗 MP |
| `COST_MOVE` | 消耗 MV |
| `COST_GOLD` | 消耗金錢 |

### `Position`

| 值 | 意思 |
| --- | --- |
| `POS_DEAD` | 幾乎只用於特殊邏輯 |
| `POS_SLEEPING` | 睡眠也可用 |
| `POS_RESTING` | 休息狀態可用 |
| `POS_FIGHTING` | 戰鬥中可用 |
| `POS_STANDING` | 站立即可用 |

### `Weapon`

| 值 | 意思 |
| --- | --- |
| `WEAPON_HAND` | 空手 |
| `WEAPON_DAGGER` | 短兵 |
| `WEAPON_SWORD` | 劍 |
| `WEAPON_BLADE` | 刀 |
| `WEAPON_AXE` | 斧 |
| `WEAPON_WHIP` | 鞭 |
| `WEAPON_SPEAR` | 槍矛 |
| `WEAPON_PEN` | 筆扇 |
| `WEAPON_HAMMER` | 鎚 |
| `WEAPON_CLUB` | 棍棒 |
| `WEAPON_BOW` | 弓 |
| `WEAPON_FORCE` | 氣功 |

### `Rating`

| 值 | 意思 |
| --- | --- |
| `RATING_SKILL` | 一般技能 |
| `RATING_WIND` | 風系 |
| `RATING_EARTH` | 土系 |
| `RATING_LIGHTNING` | 雷系 |
| `RATING_POISON` | 毒系 |
| `RATING_FIRE` | 火系 |
| `RATING_WATER` | 水系 |
| `RATING_DARKNESS` | 暗系 |
| `RATING_LIGHT` | 光系 |
| `RATING_SAINT` | 聖系 |
| `RATING_EVIL` | 邪系 |
| `RATING_CURE` | 治療向 |
| `RATING_SING` | 吟唱向 |
| `RATING_FIGHT` | 格鬥向 |
| `RATING_MURDER` | 暗殺向 |
| `RATING_CREATE` | 製作向 |
| `RATING_THIEF` | 盜賊向 |

## `Situs` 是什麼

`Situs` 是 `#Damage` 內的「命中部位 mask」。

例：

```text
Situs           ATTACK_RANDOM
```

這行不是裝備欄位，也不是 `data/situs.txt` 裡那個 `Situs = 頭部/手部/...` 文字欄。
它實際上是：

- 在 `.ski` 裡指定一個 `ATTACK_*` mask
- 交給 `src/body.c` 的 `random_situs()` 選出本次命中的實際部位
- 再由 `data/situs.txt` 中各部位的 `Chance` 權重決定偏向哪裡

### 常見 `Situs` 值

| 值 | 意思 |
| --- | --- |
| `ATTACK_RANDOM` | 隨機部位；最常見 |
| `ATTACK_HEAD` | 頭部 |
| `ATTACK_BODY` | 身體 |
| `ATTACK_HANDS` | 手部 |
| `ATTACK_LEGS` | 腿部 |
| `ATTACK_FEET` | 腳部 |
| `ATTACK_WIELD` | 持武器手 |
| `ATTACK_SHIELD` | 盾牌位 |

### `ATTACK_RANDOM` 的實際效果

`ATTACK_RANDOM` 在 `src/merc.h` 中是 `0`，但 `src/body.c` 會把 `ATTACK_RANDOM` 或 `0` 特判成「對全部可用部位做 weighted random」。

也就是說：

- 它不是「沒有命中部位」
- 而是「交給 body system 依 `data/situs.txt` 權重挑一個部位」

所以 `gold_blade.ski` 裡一整串：

```text
Situs           ATTACK_RANDOM
```

代表這些刀招都不是固定砍頭或砍手，而是用一般近戰的隨機命中部位邏輯。

## `Limit` 怎麼看

`Limit` 一行格式是：

```text
Limit           <CLASS_*> <最低等級> <熟練度上限>
```

例：

```text
Limit           CLASS_FIGHTER    1  40
Limit           CLASS_GENERAL    1  90
Limit           CLASS_BRAVO      1  90
```

意思是：

- `fighter` 1 級可學，但上限 40
- `general` 1 級可學，上限 90
- `bravo` 1 級可學，上限 90

這裡的第三欄不是百分比字串，而是 loader 直接讀入的 adept 上限數值。

## 常見維護規則

- `Name`、`Slot`、檔名、`skill/skill.lst` key 必須一致且全域唯一。
- 如果新增技能，至少一起檢查：
  - `skill/skill.lst`
  - `src/merc.h` 的 `SLOT_*`
  - `data/symbol.def`
  - `skill/<letter>/<name>.ski`
- `Valid NO`、`CanAsk NO`、`Teach NO` 常用於 NPC-only 技能，但不代表可以省略其他 runtime 欄位。
- `Qutoient` 是 repo 既有拼字，不要擅自改成 `Quotient`。
- `ATTACK_RANDOM` 雖然值為 `0`，但有特殊語意，不能當成「未設定」直接刪掉。

## 建議後續擴充

如果你要把這頁做成長期維護入口，下一步最值得補的是：

1. 加一張「`.ski` 欄位 -> `SKILL_DATA` 成員 -> loader case」對照表。
2. 補 `#Affect`、`#Restrict`、`Effect` 的完整範例。
3. 再做一頁「常見欄位值字典」，把 `TAR_*`、`WEAPON_*`、`RATING_*`、`ATTACK_*` 分頁整理。

這三塊我已先拆出第二頁：

- [進階 Loader Reference](./skill-loader-reference.html)

> 例子來源：`skill/g/gold_blade.ski`、`src/load.c`、`src/body.c`、`src/merc.h`、`data/symbol.def`、`data/situs.txt`
