
# 三國 MUD 歷史事件系統

這是一個用於 MUD 世界的 **歷史事件框架 (Historical Event System)**。

用途：
- 動態改變世界
- 改變 NPC / 任務
- 觸發戰場 / PvP
- 改變地圖控制權

---

## 系統結構

```
events/
   huangjin_rebellion.json
   guandu_battle.json
   chibi_battle.json
   wuzhangyuan.json
```

每個事件可以影響：

- AREA
- NPC
- QUEST
- WORLD STATE

---

## 使用方式

伺服器可定期檢查：

```
current_event
```

並套用對應 world state。
