# Failenable NPC 技能審計表

來源依據：

- runtime source of truth：`skill/*.ski`、`skill/skill.lst`、`src/merc.h`、`data/symbol.def`
- 現行 repo 補充紀錄：`docs/current-game/skills.md`
- 現行 repo 機器可讀台帳：`docs/current-game/skills.json`
- 舊站參考：`docs/3yWebsite/docs/data/skills.json`
- 舊站參考：`docs/3yWebsite/docs/skills.md`
- `docs/3yWebsite/docs/system.md`
- `area/loyang/*`
- `area/beiping/*`

| VNUM | 身份 | 戰鬥重要度 | 現用攻擊技能 | 現用步法 | docs 對應來源 | 目標技能層級 | 採既有升階或新造 | 原因 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 501 | 城市守衛 | 核心 | gdragon steps | gdragon steps | `cloud steps -> gdragon steps` 屬軍職步法前段 | 城防中階 | 新造 | 城市守衛需要制式刀法與軍中步法，不再只掛基礎步法。 |
| 503 | 城門守衛 | 核心 | evil fist | gdragon steps | 舊配置混入非軍旅拳法 | 城防高階 | 新造 | 城門守衛是玩家最常接觸的城防樣本，必須有穩定軍旅刀技。 |
| 536 | 鏢師 | 次要 | long fist | gdragon step | `hua sword` 教學 NPC，主功能是教導 | 自保級 | 新造 | 降級為單留步法的次要戰鬥 NPC，避免弱 offensive 技破壞定位。 |
| 541 | 小將 / 轉職者 | 次要 | evil fist | gdragon steps | 轉職 / 教學型 NPC | 自保級 | 新造 | 保留老將的步法威儀，不強塞不合身份的主攻招式。 |
| 545 | 騎兵 | 核心 | long fist | gdragon steps | docs 缺軍旅槍術對應 | 軍旅中階 | 新造 | 騎兵應該用槍，不應靠空手技能撐場。 |
| 555 | 李肅 | 核心 | gsword | mirage steps | 皇城 / 宮廷劍士語彙 | 皇城中高階 | 新造 | 配合其宮廷政變身份，改掛宮城系劍法與步法。 |
| 560 | 禁軍護衛 | 核心 | hua sword | gdragon steps | 皇宮護衛但舊技仍是入門華山系 | 軍旅高階 | 新造 | 禁軍先用軍旅制式刀步，和城市守衛拉開熟練度層級。 |
| 565 | 殿前護衛 | 核心 | fonxan sword | sky steps | 舊劍法 / 步法屬江湖升階但數值偏弱 | 皇城高階 | 新造 | 殿前護衛需要明確高於禁軍的御衛劍步。 |
| 569 | 殿前護衛 | 核心 | fonxan sword | sky steps | 同上 | 皇城頂階 | 新造 | 等級 85 殿前護衛應使用最完整的御衛套裝。 |
| 576 | 殿前護衛 | 核心 | fonxan sword | sky steps | 同上 | 皇城高階 | 新造 | 以熟練度分層，不再讓高階守衛掛同質弱技。 |
| 577 | 殿前護衛 | 核心 | fonxan sword | sky steps | 同上 | 皇城高階 | 新造 | 同 576，維持殿前護衛梯度。 |
| 578 | 殿前護衛 | 核心 | gsword | mirage steps | 舊配置偏江湖散招 | 皇城中階 | 新造 | 讓較低階殿前護衛仍保有正式御衛技體系。 |
| 589 | 盜賊 | 核心 | six fire | mirage steps | 盜賊不應以火掌作主輸出 | 夜行高階 | 新造 | 改成夜行刀法 + `shadowtrace steps`，並補武器 reset。 |
| 9001 | 皇宮禁衛軍 | 核心 | gdragon steps | gdragon steps | 皇城士卒需要正式兵制技能 | 皇城入門 | 新造 | 補上劍技，建立北平皇宮的第一層梯階。 |
| 9002 | 殿前武士 | 核心 | dream blade | gdragon steps | 舊刀法雖有名號但本體偏弱 | 軍旅高階 | 新造 | 以刀法熟練度與裝備把殿前武士拉高於一般禁衛軍。 |
| 9008 | 京城大盜 | 核心 | gdragon steps | gdragon steps | 大盜缺少對應夜行刀步 | 夜行中階 | 新造 | 大盜需要一套真正能出招的夜行刀法 + `shadowtrace steps`。 |
| 9009 | 御前護衛 | 核心 | fonxan sword | gdragon steps | 御前護衛需高於殿前武士 | 皇城高階 | 新造 | 改為御衛專屬劍步，塑造皇城最強常駐守衛。 |
| 9011 | 扶桑浪人 | 核心 | gdragon steps | gdragon steps | docs 缺扶桑浪人對應技能鏈 | 夜行入門 | 新造 | 補武士刀與 `shadowtrace steps`，讓浪人保有異邦刀客感。 |

處理原則：

- 戰鬥核心 NPC 優先用高階技能或新技能，不保留 `Enable 100` 弱技。
- 戰鬥次要 NPC 可降為單一自保步法，避免為了消 warning 硬掛不合身份的 offensive skill。
- 這份審計表只處理 failenable 高風險群，未展開全服技能重平衡。
