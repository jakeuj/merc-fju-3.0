
# 三國世界 AREA 類型分布規劃圖

此文件用於規劃 **三國 MUD 世界 120+ AREA 的類型分布**，避免地圖探索節奏失衡。

設計原則：

- 城市作為 **Hub**
- 郊外作為 **過渡區**
- 野外作為 **主要探索**
- 關隘作為 **choke point**
- 地下區作為 **高密度探索**
- 秘境作為 **稀有內容**

---

# 世界規模

建議世界大小：

- **120 AREA**

---

# AREA 類型分布

| 類型 | 數量 | 比例 | 用途 |
|---|---|---|---|
| City | 15 | 12% | 城市 hub |
| Outskirts | 20 | 17% | 城郊過渡 |
| Wild | 35 | 29% | 野外探索 |
| Fort | 15 | 12% | 關隘 / choke point |
| Dungeon | 25 | 21% | 探索副本 |
| Secret | 10 | 8% | 秘境 |

總計：**120 AREA**

---

# 視覺化分布

```
Wild      █████████████████████████
Dungeon   ██████████████████
Outskirts ███████████████
City      ███████████
Fort      ███████████
Secret    ███████
```

---

# 各州建議配置

## 中原

| 類型 | 數量 |
|---|---|
City | 3 |
Outskirts | 3 |
Wild | 5 |
Dungeon | 3 |
Fort | 2 |

## 關中

| 類型 | 數量 |
|---|---|
City | 2 |
Outskirts | 2 |
Wild | 3 |
Dungeon | 2 |
Fort | 3 |

## 幽州

| 類型 | 數量 |
|---|---|
City | 2 |
Wild | 4 |
Fort | 2 |
Dungeon | 2 |

## 荊州

| 類型 | 數量 |
|---|---|
City | 3 |
Outskirts | 3 |
Wild | 5 |
Dungeon | 3 |
Fort | 1 |

## 江東

| 類型 | 數量 |
|---|---|
City | 2 |
Outskirts | 3 |
Wild | 4 |
Dungeon | 2 |
Fort | 1 |

## 蜀漢

| 類型 | 數量 |
|---|---|
City | 2 |
Wild | 4 |
Dungeon | 4 |
Fort | 2 |

## 南蠻

| 類型 | 數量 |
|---|---|
City | 1 |
Wild | 5 |
Dungeon | 3 |
Secret | 2 |

---

# 世界設計節奏

建議探索節奏：

```
City
 ↓
Outskirts
 ↓
Wild
 ↓
Dungeon
 ↓
Secret
```

玩家會自然形成：

- 探索
- 回城
- 再深入

---

# 進階設計

建議在 120 AREA 中加入：

| 類型 | 數量 |
|---|---|
世界 Boss 區 | 3 |
大型迷宮 | 4 |
戰場事件 | 3 |
隱藏區 | 5 |

---

# 建議世界拓撲結構

```
City
 ├─ Outskirts
 │   ├─ Wild
 │   │   ├─ Dungeon
 │   │   └─ Secret
 │   └─ Wild
 └─ Road → Next City
```
