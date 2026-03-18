# Mob Flags And Constants

用於查 `document/mob.txt` 裡的怪物旗標、效果旗標與常數。這份檔特別把 legacy 文件前半段與附註段落合併，因為原文件的附註常數表並不完整。

## Table Of Contents

- Act Flags
- Effect Flags
- Sex Constants
- Class Constants
- Position Constants
- Notes On Incomplete Legacy Tables

## Act Flags

legacy 文件在主說明區列出的可用旗標如下：

```text
IsNPC                   1
Sentinel                2
Scavenger               4
Aggressive             32
StayArea               64
Wimpy                 128
Pet                   256
Train                 512
Practice             1024
Rebirth              2048
RebornFight          4096
Ask                  8192
AutosetValue        16384
NoReborn            32768
NoKill              65536
Enroll             131072
AlignGood          262144
AlignEvil          524288
NoSummon          1048576
```

legacy 文件對作者的提醒：

- `IsNPC`
  - 內定存在，可不手填。
- `Sentinel`
  - 讓怪留在房內；商店老闆也建議加這個。
- `Scavenger`
  - 會撿地上物品。
- `Aggressive`
  - 會主動打玩家，使用要保守。
- `StayArea`
  - 會移動，但不離開本區。
- `Wimpy`
  - 掉到一定血量會逃。
- `Pet`
  - 文件明講當時「目前沒有用，不要設」。
- `Train`
  - 可幫玩家升屬性。
- `Practice`
  - 文件說當時「目前沒使用」。
- `Rebirth`
  - 可幫玩家轉職。
- `RebornFight`
  - 死後再生另一支怪。
- `Ask`
  - 可讓玩家透過怪送信。
- `AutosetValue`
  - 系統依等級自動回填部分數值。
- `NoReborn`
  - 不會在 reset 時重生。
- `NoKill`
  - 不能被攻擊殺害。
- `Enroll`
  - 會記恨。
- `AlignGood` / `AlignEvil`
  - 明確標成善良或邪惡陣營。
- `NoSummon`
  - 不能被 `summon` 召喚。

## Effect Flags

legacy 文件主說明區列出的可用效果如下：

```text
'blind'              1
'invisible'          2
'detect evil'        4
'detect invis'       8
'detect magic'      16
'detect hidden'     32
'sanctuary'         64
'faerie fire'      128
'infrared'         256
'curse'            512
'poison'          1024
'protect'         2048
'sneak'           4096
'hide'            8192
'sleep'          16384
'charm'          32768
'flying'         65536
'pass door'     131072
'fixity'        262144
'mask'          524288
'detect mask'  1048576
```

用途是給怪物附加能力或狀態，例如偵測、保護、隱匿、飛行等。

## Sex Constants

```text
SEX_NEUTRAL  0
SEX_MALE     1
SEX_FEMALE   2
```

## Class Constants

```text
CLASS_DEMOS      0
CLASS_SCHOLAR    1
CLASS_FIGHTER    2
CLASS_SHAMAN     3
CLASS_THIEF      4
CLASS_DOCTOR     5
CLASS_BARD       6
CLASS_GENERAL    7
CLASS_BRAVO      8
CLASS_MAGE       9
CLASS_SMITH     10
```

repo-specific 提醒：

- `Class` 很影響轉職師父、技能使用與 teacher 型 NPC。
- 實作時先對 repo 內已成功載入範例，不要只因 legacy 表有列就假設 loader 一定接受新寫法。

## Position Constants

`#Job` 會用到的最低狀態常數：

```text
POS_DEAD       0
POS_SLEEPING   1
POS_RESTING    2
POS_FIGHTING   3
POS_STANDING   4
```

一般互動預設多半是 `POS_STANDING`。

## Notes On Incomplete Legacy Tables

- `document/mob.txt` 附註裡的 Act 常數表只列到 `ACT_ENROLL`，沒有把 `AlignGood`、`AlignEvil`、`NoSummon` 收進去；這三個要以前面主說明區為準。
- `document/mob.txt` 附註裡的 Effect 常數表只列到 `AFF_PASS_DOOR`，沒有收 `fixity`、`mask`、`detect mask`；這三個同樣以前面主說明區為準。
- 因此查旗標或效果時，不要只看附註那張表，否則會漏掉後補的欄位。
