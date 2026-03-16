---
layout: default
title: Skill Combat Audit
---

# Skill Combat Audit

這頁是目前 `merc-fju-3.0` 技能戰鬥鏈盤點與重建工作的人工可讀入口；機器可讀台帳仍以 `skill-combat-audit.json` 為主。

## 目前結論

- guard-family 試點已證明：部分 mob 的技能偏弱或不合身份，確實可能來自舊配置殘留，而不是單純體感錯覺。
- 目前更像是「局部配置失真」，不是「全域技能系統全面被閹割」。
- `Attack Value`、`Skill Value`、`Mob Practice` 已確認不是直接戰鬥倍率來源。
- NPC-only 技能 `military blade`、`military steps`、`imperial sword`、`imperial steps`、`night blade`、`shadowtrace steps`、`cavalry lance` 目前屬刻意設計，不應再被當成 loader 壞資料。

## 已落地樣本

- `area/loyang/mob/559.mob`
  - 已從錯位的 legacy 組合拉回 `military blade` + `military steps`
- `area/beiping/mob/9010.mob`
  - 已補 entry-level 城門衛軍技能帶
- `area/beiping/mob/9018.mob`
  - 已補 junior palace guard 技能帶

## 目前還沒做完的事

- loyang / beiping 仍有一批非試點 mob 掛著 legacy combat skill，尚未正式判讀
- 舊技能仍在被使用，不代表一定要刪；必須先判斷它是不是仍符合角色身份鏈
- 需要持續區分：
  - 可保留的 legacy skill
  - 明顯錯位、應替換的 legacy skill
  - 證據不足、待下一輪再審的 suspect

## 下一輪建議做法

1. 先重掃 `area/*/mob/*.mob` 的 `Enable`、`AutoEnable`、`#Learn`
2. 以 loyang / beiping 內尚未納入試點、但仍掛 legacy combat skill 的樣本優先
3. 優先處理城市 / 宮廷 / 城內常駐戰鬥 NPC，再處理特殊 boss、技能投影怪、劇情怪
4. 修改 runtime data 後，同步更新 `skill-combat-audit.json`
5. 做 build 與 smoke test

## 相關檔案

- [技能戰鬥鏈重建計畫](/H:/repos/merc-fju-3.0/plans/0002-skill-combat-chain-audit.md)
- [Failenable NPC 技能審計表](/H:/repos/merc-fju-3.0/plans/failenable-npc-skill-audit.md)
- [技能戰鬥鏈機器可讀台帳](/H:/repos/merc-fju-3.0/docs/current-game/skill-combat-audit.json)
- [現行技能補充說明](/H:/repos/merc-fju-3.0/docs/current-game/skills.md)
