---
layout: default
title: Skill Pry Crosswalk
---

# `pry` 技能說明對照手冊

這頁專門回答一種很實際的維護需求：

- 玩家或 help 文案貼了一段技能說明
- 想知道它對應 `.ski` 的哪些欄位
- 或反過來確認目前 repo 裡的 `.ski` 會印出什麼 `pry` 文案

前兩種文件偏 loader / schema，這一頁偏「玩家可讀文案 <-> runtime 欄位」。

## Source Of Truth

目前 `pry` 輸出規則主要來自：

- `src/act_info.c` 的 `do_pry()`
- `src/bit.c` 的 `adeptation_name()`
- `src/class.c` 的 `class_name()`
- `skill/*.ski`

如果玩家文案、help 範例、`pry` 輸出、`.ski` 四者衝突，維護時建議優先順序是：

1. `skill/*.ski`
2. `src/act_info.c` 的實際輸出規則
3. help 範例
4. 玩家手抄文案

## 一般對照規則

| `pry` 文案欄位 | 來源 |
| --- | --- |
| `英文名稱` | `.ski` 的 `Name` |
| `中文名稱` | `.ski` 的 `Cname` |
| `攻擊武器` | `.ski` 的 `Weapon` 經 `weapon_type_name()` 轉字串 |
| `互相教導` | `.ski` 的 `Teach` |
| `技能功能` | `.ski` 的 `Type` 經 `skill_type()` 轉字串 |
| `技能分類` | `.ski` 的 `Rating` 經 `skill_rating()` 轉字串 |
| `浪費數值` | `.ski` 的 `Costtype` 經 `do_pry()` 轉字串 |
| `領悟技能` | 找 `get_skill( pSkill->associate )` |
| `預備功夫` | 找「哪個技能的 `associate == 這招的 slot`」 |
| `領悟機率` | `Degree` 經 `PryChance[]` 轉字串 |
| `職業限制` | 每一行 `Limit` |
| `限 制` | 每一條 `#Restrict` 經 `restrict_value()` 組字串 |
| `教 導` | 若沒有 teacher / teach data，常見輸出就是「沒有人教導」 |

## `Degree` 對照 `領悟機率`

`do_pry()` 不是直接印數字，而是用 `PryChance[]` 對照：

| `Degree` 門檻 | `pry` 顯示 |
| --- | --- |
| `>= 300` | 極高 |
| `>= 250` | 很高 |
| `>= 200` | 高 |
| `>= 150` | 一般 |
| `>= 100` | 低 |
| `>= 50` | 很低 |
| `>= -1` | 極低 |

所以：

- `Degree 5` 會顯示 `極低`
- `Degree 50` 會顯示 `很低`

## 熟練度稱號對照

職業限制那句：

```text
熟練度最高可以到一代宗師
```

不是直接寫死字串，而是 `Limit` 第三欄經 `adeptation_name()` 轉出來。

| `Limit` 上限值 | 稱號 |
| --- | --- |
| `0` | 毫無根基 |
| `1-9` | 初學乍練 |
| `10-19` | 粗通皮毛 |
| `20-29` | 初窺門徑 |
| `30-39` | 馬馬虎虎 |
| `40-49` | 心神領會 |
| `50-59` | 出類拔萃 |
| `60-69` | 神乎其技 |
| `70-79` | 出神入化 |
| `80-89` | 登峰造極 |
| `90-99` | 一代宗師 |
| `>= 100` | 深不可測 |

所以：

- `Limit ... 40` 会顯示 `心神領會`
- `Limit ... 90` 會顯示 `一代宗師`

## 職業中文名對照

目前 repo 裡常見對照如下：

| 中文文案 | 內部值 |
| --- | --- |
| 平民 | `CLASS_DEMOS` |
| 文官 | `CLASS_SCHOLAR` |
| 武官 | `CLASS_FIGHTER` |
| 道士 | `CLASS_SHAMAN` |
| 盜賊 | `CLASS_THIEF` |
| 郎中 | `CLASS_DOCTOR` |
| 伶人 | `CLASS_BARD` |
| 將軍 | `CLASS_GENERAL` |
| 刺客 | `CLASS_BRAVO` |
| 天師 | `CLASS_MAGE` |
| 鑄劍師 | `CLASS_SMITH` |

注意 `pry` 顯示的中文職業名來自 `class_name()`，通常會保留遊戲裡原本的全形排版，例如 `將  軍`。

## `gold blade` 範例

以下用目前 repo 裡的 [gold_blade.ski](H:\repos\merc-fju-3.0\skill\g\gold_blade.ski) 當範例。

### 目前 `.ski` 實際內容

關鍵欄位是：

```text
Name            gold blade~
Cname           紫金六陽刀法~
Weapon          WEAPON_BLADE
Teach           NO
Type            TAR_CHAR_OFFENSIVE
Rating          RATING_SKILL
Costtype        COST_MOVE
Associate       -1
Degree          5
Limit           CLASS_FIGHTER    1  40
Limit           CLASS_GENERAL    1  90
Limit           CLASS_BRAVO      1  90
```

### 對應 `pry` 文案應該怎麼讀

| 玩家看到的句子 | 對應欄位 | 目前 repo 實際值 |
| --- | --- | --- |
| `英文名稱﹕gold blade` | `Name` | `gold blade` |
| `中文名稱﹕紫金六陽刀法` | `Cname` | `紫金六陽刀法` |
| `攻擊武器﹕大刀` | `Weapon` | `WEAPON_BLADE` |
| `互相教導﹕不可以` | `Teach` | `NO` |
| `技能功能﹕攻擊類` | `Type` | `TAR_CHAR_OFFENSIVE` |
| `技能分類﹕技能` | `Rating` | `RATING_SKILL` |
| `浪費數值﹕體力` | `Costtype` | `COST_MOVE` |
| `領悟技能﹕從缺` | `Associate` | `-1` |
| `預備功夫﹕從缺` 或某招後繼技能 | 反向找 `associate == SLOT_GOLD_BLADE` | 依整個 skill tree 決定 |
| `領悟機率﹕極低` | `Degree` | `5` |

### 職業限制應怎麼解

目前 `.ski` 有三行 `Limit`：

```text
Limit           CLASS_FIGHTER    1  40
Limit           CLASS_GENERAL    1  90
Limit           CLASS_BRAVO      1  90
```

所以依目前 repo，較接近的 `pry` 解讀應該是：

- 武官等級最低一級可學，熟練上限是 `心神領會`
- 將軍等級最低一級可學，熟練上限是 `一代宗師`
- 刺客等級最低一級可學，熟練上限是 `一代宗師`
- 其他職業不能學

### 這和你貼的文案哪裡不同

你貼的版本是：

- `預備功夫﹕傲寒六訣(ice blade)`
- 只有 `將軍` 可學
- `將軍` 上限寫成 `一代宗師`
- 限制列了 `敏捷 >= 25`、`力量 >= 30`、`傲寒六訣熟練度 >= 登峰造極`

但目前 repo 的 [gold_blade.ski](H:\repos\merc-fju-3.0\skill\g\gold_blade.ski) 沒有這些設定：

- `Associate` 目前是 `-1`
- 沒有任何 `#Restrict`
- `Limit` 目前包含 `fighter / general / bravo`

也就是說，這段文案比較像：

- 舊版本資料
- 玩家整理文
- 或你預期中的設計稿

而不是目前 repo 內這份 `.ski` 的直接輸出。

## 維護建議

如果你未來是從玩家文案回填 `.ski`，建議流程是：

1. 先看實際 `.ski`
2. 再看這頁確認每一句文案對應哪個欄位
3. 若文案和 `.ski` 衝突，先決定要修資料還是修說明
4. 如果目標是讓 `pry` 真正印出那段文案，就要改 `.ski`，不是只改 docs

## 相關頁面

- [`.ski` 技能檔格式說明](./skill-file-format.html)
- [`.ski` 進階 Loader Reference](./skill-loader-reference.html)
- [`.ski` 常數查表](./skill-constants.html)
