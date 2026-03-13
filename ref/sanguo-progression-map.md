
# 三國 MUD 世界 AREA 探索節奏圖 (Progression Map)

此文件定義 **玩家等級 → 世界區域 → 探索節奏**。  
目標是讓玩家在 120+ AREA 世界中自然推進，不會迷失或跳級。

設計原則：
- 每 10 等級一個主要區域
- 每個階段包含：City / Outskirts / Wild / Dungeon
- 關隘 (Fort) 作為區域過渡
- Secret 作為高風險探索

---

# 世界 Progression 主線

| 等級 | 區域 | 節點 | 類型 |
|---|---|---|---|
| Lv1 | 洛陽 | city_loyang | City |
| Lv5 | 洛陽東郊 | wild_loyang_east | Outskirts |
| Lv10 | 龍渠丘陵 | wild_longqu_hills | Wild |
| Lv15 | 陳留 | city_chenliu | City |
| Lv20 | 濮陽森林 | wild_puyang_forest | Wild |
| Lv25 | 官渡古戰場 | dng_guandu_battlefield | Dungeon |
| Lv30 | 虎牢關 | fort_hulao | Fort |
| Lv35 | 襄陽 | city_xiangyang | City |
| Lv40 | 江夏水域 | wild_jiangxia_river | Wild |
| Lv45 | 雲夢大澤 | dng_yunmeng_swamp | Dungeon |
| Lv50 | 建業 | city_jianye | City |
| Lv55 | 會稽山林 | wild_kuaiji_mountains | Wild |
| Lv60 | 武陵山脈 | wild_wuling_mountains | Wild |
| Lv65 | 南蠻叢林 | wild_nanman_jungle | Wild |
| Lv70 | 南蠻神殿 | dng_nanman_temple | Dungeon |
| Lv75 | 上古遺跡 | dng_ancient_ruins | Dungeon |
| Lv80 | 靈界入口 | secret_spirit_gate | Secret |

---

# 世界地圖節奏圖

```
Lv1  洛陽 (City)
   │
Lv5  洛陽東郊 (Outskirts)
   │
Lv10 龍渠丘陵 (Wild)
   │
Lv15 陳留 (City)
   │
Lv20 濮陽森林 (Wild)
   │
Lv25 官渡古戰場 (Dungeon)
   │
Lv30 虎牢關 (Fort)
   │
Lv35 襄陽 (City)
   │
Lv40 江夏水域 (Wild)
   │
Lv45 雲夢大澤 (Dungeon)
   │
Lv50 建業 (City)
   │
Lv55 會稽山林 (Wild)
   │
Lv60 武陵山脈 (Wild)
   │
Lv65 南蠻叢林 (Wild)
   │
Lv70 南蠻神殿 (Dungeon)
   │
Lv75 上古遺跡 (Dungeon)
   │
Lv80 靈界入口 (Secret)
```

---

# 探索節奏循環

每個區域遵循固定節奏：

```
City
 ↓
Outskirts
 ↓
Wild
 ↓
Dungeon
 ↓
Fort (區域轉換)
 ↓
Next City
```

---

# 玩家體驗設計

## 低等級 (Lv1–20)

特色：

- 新手教學
- 簡單探索
- 城市任務

區域：

- 洛陽
- 龍渠丘陵
- 陳留

---

## 中等級 (Lv20–50)

特色：

- 大量野外
- 副本探索
- 軍事關隘

區域：

- 官渡戰場
- 虎牢關
- 襄陽
- 江夏

---

## 高等級 (Lv50–80)

特色：

- 遠征探索
- 古代遺跡
- 秘境

區域：

- 南蠻
- 上古遺跡
- 靈界

---

# Endgame 設計

建議加入：

| 區域 | 類型 |
|---|---|
| 天界入口 | Secret |
| 魔界裂隙 | Dungeon |
| 古神遺跡 | Raid |
| 三國戰場 | Event |

