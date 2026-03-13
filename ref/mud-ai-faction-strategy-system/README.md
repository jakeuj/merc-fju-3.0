
# 三國 MUD AI 勢力戰略系統 (AI Faction Strategy System)

這個系統讓三國勢力 **AI 自動決策**：

- 攻擊城市
- 防守據點
- 派兵支援
- 擴張領土

目標：
讓 MUD 世界變成 **持續演化的三國戰場**。

---

## AI 行為

AI 每個 tick 會做決策：

1. 檢查敵方領土
2. 選擇最近戰略城市
3. 發起攻城或防守

---

## 系統流程

```
world state
   ↓
faction AI
   ↓
choose target
   ↓
spawn battle
   ↓
update territory
```

---

## 使用方式

```
python ai_strategy_sim.py
```

會模擬 AI 勢力爭奪城市。
