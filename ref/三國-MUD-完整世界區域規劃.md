
# 三國 MUD 世界完整區域地圖規劃

此文件是一份 **完整三國 MUD 世界區域規劃藍圖**，用於規劃 AREA、map.md、NPC、任務與探索內容。

目標：

- 建立完整世界探索結構
- 每個區域有明確主題
- 保持題材平衡
- 適合逐步擴充

區域等級以 **玩家 progression** 為導向。

---

# 世界主線交通骨架

```
西涼 → 天水 → 安定 → 長安 → 弘農 → 洛陽 → 陳留 → 徐州
                    │      │
                    │      └ 壽春 → 建業 → 會稽
                    │
                    └ 宛 → 新野 → 襄陽 → 江夏 → 柴桑
                                  │
                                  └ 長沙 → 零陵 → 桂陽 → 南海

成都 → 江州 → 永安 → 江陵 → 武陵 → 長沙
```

---

# 區域等級分佈

| 等級 | 區域類型 |
|---|---|
| 1‑10 | 城郊 / 官道 |
| 10‑20 | 山林 / 小型盜匪 |
| 20‑35 | 戰場 / 幫派 |
| 35‑50 | 古墓 / 洞窟 |
| 50‑70 | 大型秘境 |
| 70+ | 上古遺跡 / 世界事件 |

---

# 中原核心區

## 洛陽 (Lv1‑20)

AREA

- loyang_city
- loyang_market
- loyang_palace

外圍

- loyang_outskirts
- dragon_channel_hills
- loyang_sewers

主題

歷史城市 + 江湖

---

## 弘農 (Lv15‑25)

AREA

- hongnong_city
- tiger_pass (虎牢關)
- hongnong_farmland

主題

軍旅 + 歷史

---

## 陳留 (Lv20‑30)

AREA

- chenliu_city
- chenliu_west_fields
- yellow_turban_ruins

主題

歷史 + 軍旅

---

# 北方幽州區

## 北平 (Lv20‑35)

AREA

- beiping_city
- beiping_station
- beiping_outskirts

主題

歷史 + 軍旅

---

## 易京 (Lv30‑40)

AREA

- yijing_fort
- northern_watchtower
- yijing_battlefield

主題

軍旅

---

## 白狼山 (Lv35‑50)

AREA

- white_wolf_mountain
- barbarian_camp
- ancient_cave

主題

探險 + 異族

---

# 西域與長安區

## 長安 (Lv25‑40)

AREA

- changan_city
- imperial_district
- changan_market

主題

歷史城市

---

## 函谷關 (Lv35‑45)

AREA

- hangu_pass
- pass_gate
- canyon_road

主題

軍旅

---

## 西涼荒原 (Lv40‑55)

AREA

- xiliang_steppe
- nomad_camp
- ancient_ruins

主題

軍旅 + 探險

---

# 荊州區

## 襄陽 (Lv30‑45)

AREA

- xiangyang_city
- fan_castle
- xiangyang_market

主題

軍旅 + 歷史

---

## 新野 (Lv35‑50)

AREA

- xinye_town
- countryside
- rebel_hideout

主題

江湖

---

## 雲夢大澤 (Lv40‑60)

AREA

- yunmeng_swamp
- lost_temple
- spirit_marsh

主題

詭異 + 仙俠

---

# 江東區

## 壽春 (Lv35‑50)

AREA

- shouchun_city
- river_gate
- eastern_fields

主題

歷史

---

## 建業 (Lv40‑60)

AREA

- jianye_city
- port_district
- naval_base

主題

歷史 + 水軍

---

## 江東水域 (Lv45‑65)

AREA

- river_delta
- pirate_islands
- water_ruins

主題

探險

---

# 蜀漢區

## 成都 (Lv40‑60)

AREA

- chengdu_city
- imperial_garden
- scholar_district

主題

歷史城市

---

## 武陵山 (Lv45‑70)

AREA

- wuling_mountains
- hidden_valley
- spirit_forest

主題

仙俠

---

## 蜀漢古墓 (Lv55‑75)

AREA

- ancient_tomb
- tomb_labyrinth
- tomb_guardian

主題

探險 + 仙俠

---

# 南方蠻荒區

## 長沙 (Lv40‑55)

AREA

- changsha_city
- southern_market
- countryside

主題

歷史

---

## 桂陽山林 (Lv50‑65)

AREA

- guiyang_forest
- tribal_village
- sacred_cave

主題

江湖 + 探險

---

## 南蠻密林 (Lv60‑80)

AREA

- nanman_jungle
- jungle_ruins
- serpent_temple

主題

探險 + 詭異

---

# 世界級秘境

## 古戰場

AREA

- guandu_battlefield
- chibi_battlefield
- tiger_pass_warzone

主題

軍旅

---

## 上古遺跡

AREA

- lost_dynasty_ruins
- ancient_machine_city
- celestial_temple

主題

探險 + 仙俠

---

## 靈界入口

AREA

- spirit_gate
- ghost_valley
- nether_world

主題

詭異 + 仙俠

---

# 區域總數統計

| 類型 | 區域數 |
|---|---|
| 城市 | 12 |
| 城郊 | 14 |
| 軍事 | 10 |
| 江湖 | 10 |
| 探險 | 12 |
| 仙俠 | 8 |
| 詭異 | 6 |

總 AREA 約 **70+**。

---

# 建議開發順序

Phase 1

- 洛陽
- 洛陽東郊
- 龍渠丘陵
- 洛陽地下水

Phase 2

- 北平
- 北平郊區
- 易京
- 白狼山

Phase 3

- 襄陽
- 新野
- 雲夢大澤

Phase 4

- 長安
- 函谷關
- 西涼

Phase 5

- 成都
- 武陵
- 古墓

---

# map.md 範例模板

```
Theme: 江湖
LevelRange: 15‑25

SignatureScenes:
- 山道茶棚
- 破廟
- 古橋

NPC:
- 浪人劍客
- 店小二
- 說書人

QuestHooks:
- 找失鏢
- 追查黑衣人
- 尋找秘笈

Connections:
west: loyang_city
east: dragon_channel_hills
down: ancient_cave
```
