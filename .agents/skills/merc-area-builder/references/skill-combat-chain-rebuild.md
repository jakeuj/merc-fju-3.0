# Skill Combat Chain Rebuild

當任務是在追「mob 技能配置是否因舊資料清值、簡化或錯位，導致實際功能偏弱」時，先把問題當成 runtime data audit，而不是先假設是全域戰鬥倍率問題。

## 先讀哪些檔

- `plans/0002-skill-combat-chain-audit.md`
- `plans/failenable-npc-skill-audit.md`
- `docs/current-game/skill-combat-audit.json`
- `docs/current-game/skills.md`
- `docs/current-game/skills.json`
- `docs/3yWebsite/docs/data/skills.json`
- `docs/3yWebsite/docs/data/players.json`
- `skill/skill.lst`

## 目前已確認的結論

- `Attack Value`、`Skill Value`、`Mob Practice` 不是直接戰鬥倍率來源；不要把它們當成第一優先修值點。
- `military blade`、`military steps`、`imperial sword`、`imperial steps`、`night blade`、`shadowtrace steps`、`cavalry lance` 是刻意存在的 NPC-only 技能。
- guard-family 試點已經證明：問題確實可能來自 mob 掛了錯位或過弱的 legacy 技能鏈，但目前證據更偏向「局部配置失真」，不是「整個技能系統全面被閹割」。
- `get_adeptation()` / failenable 主要拿 `#Damage Value` 去估算熟練度是否太差；這個訊號對抓模板過弱有用，但不等於完整戰鬥強度。

## Mob.txt 補充語義

`document/mob.txt` 對技能鏈重建有三個實用提醒：

- `Enable <adept> '<skill>'`
  - 這是固定熟練度，不經 `AutoEnable` 反推
- `AutoEnable '<skill>'`
  - 這是 loader-side 自動熟練度，不能和固定 `Enable` 混讀
- `AttackRatio / DodgeRatio`
  - 這兩個欄位會和 mob `Level` 一起影響 `get_adeptation()` 的目標強度
- `#Learn`
  - `Adept / Cost / Inventory / Name` 雖然不是 combat template，但仍是 mob 端 skill-facing data

所以後續看到「同一技能名」時，至少先區分：

- skill 檔模板本身是否失真
- mob 是固定 `Enable` 還是 `AutoEnable`
- 問題是戰鬥鏈錯位，還是 teacher / service loop 的 `#Learn` 設定矛盾

## 多維戰力判讀

先把 `#Damage Value` 當成底層傷害模板，不要把它當成唯一平衡旋鈕。實際技能強度至少還會被這些欄位拉動：

- `#Damage Chance`
- `#Damage Parry`
- `#Damage Innate`
- `Wait`
- `Cost`
- `CostType`
- `Weapon`
- `Check`

此外還要回看：

- `src/fight.c`
  - 命中、護甲、閃避、保護類效果如何進入最終傷害
- `src/skill.c`
  - 技能等待時間、資源消耗、武器限制與施放門檻

判讀原則：

- 高階技能不一定要比同階所有技能都有更高 `Value`
- 若技能本來走高頻、輕兵、暴擊、反擊或特殊武器風格，允許 `Value` 低於同階重兵模板
- 若只是把所有高階技能 `Value` 一碗端平，通常會破壞技能差異性並放大 failenable 以外的平衡問題

## 執行順序

1. 先掃 `area/*/mob/*.mob` 的 `Enable`、`AutoEnable`、`#Learn`
2. 先把目標 mob 分成三類：
 - `ok`：舊技能仍符合角色身份鏈
 - `restore_candidate`：技能名或熟練度明顯錯位，已有足夠 legacy/runtime 證據可直接改
 - `suspect`：看起來怪，但證據不足
3. 優先處理會直接影響城市守衛、宮廷守衛、城內戰鬥 NPC、常駐教學/服務 NPC 的樣本
4. 若證據足夠，直接修改 runtime data，不要只停在分析
5. 修改後同步更新 `docs/current-game/skill-combat-audit.json`
6. 若這輪改到 runtime `skill/*.ski`，同步重建 `docs/current-game/skills.json` 與可讀分類頁：
 - `python -X utf8 scripts/build_current_game_skill_registry.py`
 - `python -X utf8 scripts/generate_current_game_skills_pages.py`
7. 若判讀規則或範圍有變，再補 `plans/0002-skill-combat-chain-audit.md`
8. 若開始動玩家向 skill ladder，也同步把 `document/mob.txt` 的 mob-side wiring 納入 pre-check：
 - 代表樣本是否用固定 `Enable`
 - 還是靠 `AutoEnable + AttackRatio / DodgeRatio`
 - 是否同時承擔 `#Learn` 教學職能

## 舊技能判讀原則

- 舊技能還在被 mob 使用，不等於它就是壞資料。
- 先問「這個技能鏈在舊站是給誰走的」：
 - `skills.json` 看技能名、類型、升階鏈、可否教導
 - `players.json` 看玩家攻略裡它實際屬於哪種職系或成長路線
- 若舊技能在玩家攻略裡是入門技能或江湖路線，但現在掛在正式軍旅 / 皇城守衛身上，優先視為錯位。
- 若 mob 本身是技師、老師父、招式投影怪、劇情型小怪或特殊 boss，保留舊技能的門檻較低，不要為了統一而亂改。
- 若任務是重建玩家向技能鏈，先把同鏈技能依 `players.json` / `skills.json` 排出進階順序，再檢查上述多維欄位是否共同支撐那個階梯；不要只看到 `Value=20` 就整條直線上調。

## 高價值殘留點

- 注意 `skill name typo` 或殘留 alias；例如 `area/loyang/mob/571.mob` 的 `gdragon step`
- 注意 `Enable 100` 的 legacy skill 是否其實只是多年未審的預設值
- 注意城防 / 皇城 / 夜行 NPC 是否還掛著玩家向入門技能，而不是身份專用技能

## 驗證

- `make -C src -f Makefile.lin merc`
- 若有 runtime data 變更，做一次 smoke test
- 檢查 `log/*`、`debug/*`
- 特別看 `Load_skill`、`Load_mobiles`、`LOG_FAILENABLE`

## 回報格式

回報時至少交代：

- 哪些舊技能樣本已確認可以保留
- 哪些 mob 已修正
- 哪些樣本仍是 `suspect`
- 下一輪最值得接續的子批次
