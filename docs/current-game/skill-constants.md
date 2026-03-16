---
layout: default
title: Skill Constants
---

# `.ski` 常數查表

這頁是給 `.ski` 維護時快速查的常數表，和前兩頁分工如下：

- [`.ski` 技能檔格式說明](./skill-file-format.html)：先看欄位怎麼寫
- [`.ski` 進階 Loader Reference](./skill-loader-reference.html)：再看 loader 實際怎麼解
- 這一頁：最後查 `APPLY_*`、`RES_*`、`EFFECT_*`、`ATTACK_*` 這些設定值

## `APPLY_*`

這組常數來自 `data/symbol.def`，原本是 affect 影響項目表。

| 值 | 用途 |
| --- | --- |
| `APPLY_NONE` | 不指定屬性 |
| `APPLY_STR` | 力量 |
| `APPLY_DEX` | 敏捷 |
| `APPLY_INT` | 智力 |
| `APPLY_WIS` | 學識 |
| `APPLY_CON` | 體格 |
| `APPLY_SEX` | 性別 |
| `APPLY_CLASS` | 職業 |
| `APPLY_LEVEL` | 等級 |
| `APPLY_AGE` | 年齡 |
| `APPLY_HEIGHT` | 身高 |
| `APPLY_WEIGHT` | 體重 |
| `APPLY_MANA` | 法力 |
| `APPLY_HIT` | 生命 |
| `APPLY_MOVE` | 體力 |
| `APPLY_GOLD` | 金錢 |
| `APPLY_EXP` | 經驗 |
| `APPLY_AC` | 防禦值 |
| `APPLY_HITROLL` | 命中 |
| `APPLY_DAMROLL` | 傷害 |
| `APPLY_SAVING_PARA` | 麻痺豁免 |
| `APPLY_SAVING_ROD` | 杖類豁免 |
| `APPLY_SAVING_PETRI` | 石化豁免 |
| `APPLY_SAVING_BREATH` | 吐息豁免 |
| `APPLY_SAVING_SPELL` | 法術豁免 |

## `RES_*`

這組是 `#Restrict` 常用型別。

| 值 | 用途 |
| --- | --- |
| `RES_STR` | 力量限制 |
| `RES_INT` | 智力限制 |
| `RES_WIS` | 學識限制 |
| `RES_DEX` | 敏捷限制 |
| `RES_CON` | 體格限制 |
| `RES_HP` | 生命限制 |
| `RES_MANA` | 法力限制 |
| `RES_MOVE` | 體力限制 |
| `RES_CLASS` | 職業限制 |
| `RES_TRUST` | trust 限制 |
| `RES_SKILL` | 前置技能限制 |
| `RES_SEX` | 性別限制 |
| `RES_LEVEL` | 等級限制 |
| `RES_NOSKILL` | 相剋技能限制 |
| `RES_ALIGN` | 陣營限制 |

### `RES_CLASS` 位元值

若 `Type` 是 `RES_CLASS`，`Value` 會用下列位元組合：

| 值 | 職業 |
| --- | --- |
| `RES_DEMOS` | demos |
| `RES_SCHOLAR` | scholar |
| `RES_FIGHTER` | fighter |
| `RES_SHAMAN` | shaman |
| `RES_THIEF` | thief |
| `RES_DOCTOR` | doctor |
| `RES_BARD` | bard |
| `RES_GENERAL` | general |
| `RES_BRAVO` | bravo |
| `RES_MAGE` | mage |
| `RES_SMITH` | smith |

## `EFFECT_*`

這組是 `#Damage` 裡 `Effect` 行的第一欄。

| 值 | 用途 |
| --- | --- |
| `EFFECT_NONE` | 無額外效果 |
| `EFFECT_VICTIM_MANA` | 影響目標 mana |
| `EFFECT_SELF_MANA` | 影響自己 mana |
| `EFFECT_VICTIM_MOVE` | 影響目標 move |
| `EFFECT_SELF_MOVE` | 影響自己 move |
| `EFFECT_VICTIM_BLINDNESS` | 使目標眼盲 |
| `EFFECT_VICTIM_CURSE` | 使目標詛咒 |
| `EFFECT_VICTIM_POISON` | 使目標中毒 |
| `EFFECT_VICTIM_SLEEP` | 使目標睡眠 |
| `EFFECT_VICTIM_PARA` | 使目標麻痺 |
| `EFFECT_VICTIM_FAERIE_FIRE` | 使目標帶妖火 |
| `EFFECT_VICTIM_HIT` | 影響目標 HP |
| `EFFECT_SELF_HIT` | 影響自己 HP |
| `EFFECT_HIT_DIE` | 特殊重擊或致死類效果 |

## `ATTACK_*`

這組對應攻擊命中部位。`.ski` 最常看到的是 `Situs` 欄位引用它。

| 值 | 部位 |
| --- | --- |
| `ATTACK_RANDOM` | 依 `data/situs.txt` 權重隨機抽部位 |
| `ATTACK_LIGHT` | 照明位 |
| `ATTACK_FINGER_L` | 左手指 |
| `ATTACK_FINGER_R` | 右手指 |
| `ATTACK_NECK_1` | 頸部槽 1 |
| `ATTACK_NECK_2` | 頸部槽 2 |
| `ATTACK_BODY` | 身體 |
| `ATTACK_HEAD` | 頭部 |
| `ATTACK_LEGS` | 腿部 |
| `ATTACK_FEET` | 腳部 |
| `ATTACK_HANDS` | 手部 |
| `ATTACK_ARMS` | 手臂 |
| `ATTACK_SHIELD` | 盾牌位 |
| `ATTACK_ABOUT` | 披掛位 |
| `ATTACK_WAIST` | 腰部 |
| `ATTACK_WRIST_L` | 左手腕 |
| `ATTACK_WRIST_R` | 右手腕 |
| `ATTACK_WIELD` | 右手持武器 |
| `ATTACK_HOLD` | 左手持物 |
| `ATTACK_EARRING_1` | 左耳 |
| `ATTACK_EARRING_2` | 右耳 |
| `ATTACK_BACK` | 背部 |

### `ATTACK_RANDOM` 為什麼重要

`ATTACK_RANDOM` 在 `src/merc.h` 是 `0`，但它不是空值，而是「交給 `random_situs()` 依 `data/situs.txt` 的 `Chance` 權重抽部位」。

所以像：

```text
Situs           ATTACK_RANDOM
```

意思不是「沒指定命中部位」，而是「要跑正式的隨機命中流程」。

## `SLOT_*`

`SLOT_*` 是 skill registry 的主索引，定義在 `src/merc.h` 與 `data/symbol.def`。目前數量很多，不適合直接手寫整張表維護，所以這頁只記使用規則：

- `.ski` 的 `Slot` 必須填已存在的 `SLOT_*`
- `Name`、檔名、`skill/skill.lst` key、`SLOT_*` 最好一起對齊
- 新增 slot 時，要同時更新 `src/merc.h` 與 `data/symbol.def`
- 若只改 `.ski` 不補 slot 定義，loader 會失敗

常見例子：

| `.ski` | `Slot` |
| --- | --- |
| `gold_blade.ski` | `SLOT_GOLD_BLADE` |
| `blindness.ski` | `SLOT_BLINDNESS` |
| `charm_person.ski` | `SLOT_CHARM_PERSON` |
| `refresh.ski` | `SLOT_REFRESH` |
| `hide.ski` | `SLOT_HIDE` |

如果之後你真的要做完整 `SLOT_*` 名錄，比較好的做法是另外做一頁由 `src/merc.h` / `data/symbol.def` 自動生成，不要手抄。

## Source Of Truth

- `data/symbol.def`
- `src/merc.h`
- `src/body.c`
- `data/situs.txt`
