
# 三國 MUD 世界 120+ AREA 完整探索網路

此文件提供一份 **大型三國 MUD 世界探索結構**，約 **120+ AREA 節點**，設計目標：

- 世界探索路線清晰
- 每區域有合理主題
- 適合 `map.md` / generator / roo scaffold
- 支援長期擴充

區域分為：

- 城市
- 城郊
- 軍事
- 江湖
- 探險
- 仙俠
- 詭異

---

# 世界主骨架

```
西涼 → 天水 → 安定 → 長安 → 弘農 → 虎牢關 → 洛陽 → 陳留 → 徐州
                                  │
                                  ├→ 濮陽 → 南皮 → 北平 → 易京 → 白狼山 → 襄平
                                  │
                                  └→ 宛 → 新野 → 襄陽 → 江夏 → 柴桑 → 長沙
                                                          │
                                                          └→ 零陵 → 桂陽 → 南海

成都 → 江州 → 永安 → 江陵 → 武陵 → 長沙
```

---

# 中原區 (30 AREA)

## 洛陽核心

- loyang_city
- imperial_palace
- east_market
- west_market
- scholar_district

## 洛陽周邊

- loyang_outskirts
- dragon_channel
- canal_fields
- farming_village
- old_bridge

## 洛陽地下

- loyang_sewers
- sewer_depths
- forgotten_catacombs
- ancient_tomb
- tomb_labyrinth

## 洛陽北路

- road_to_puyang
- bandit_hills
- abandoned_watchtower
- ruined_fort
- haunted_forest

## 洛陽南路

- road_to_wan
- tea_pavilion
- forest_trail
- ancient_shrine
- hill_pass

---

# 關中與西域 (20 AREA)

## 長安

- changan_city
- palace_district
- merchant_square
- noble_residence
- west_market

## 函谷關

- hangu_pass
- gate_fort
- canyon_path
- guard_barracks

## 西涼

- xiliang_steppe
- nomad_camp
- ruined_tower
- ancient_ruins
- desert_shrine
- oasis_settlement

---

# 北方幽州 (18 AREA)

## 北平

- beiping_city
- city_station
- northern_market
- beiping_outskirts

## 易京

- yijing_fort
- outer_wall
- watchtower
- military_camp

## 白狼山

- white_wolf_foothills
- wolf_forest
- barbarian_camp
- ancient_cave
- spirit_peak

## 襄平

- xiangping_city
- border_market
- eastern_gate

---

# 荊州 (18 AREA)

## 襄陽

- xiangyang_city
- fan_castle
- xiangyang_market
- military_dock

## 新野

- xinye_town
- countryside
- rebel_hideout

## 江夏

- jiangxia_port
- river_fort
- naval_barracks

## 雲夢大澤

- yunmeng_swamp
- sunken_ruins
- spirit_marsh
- lost_temple

---

# 江東 (16 AREA)

## 壽春

- shouchun_city
- eastern_gate
- river_fields

## 建業

- jianye_city
- port_district
- naval_base
- merchant_quarter

## 會稽

- kuaiji_city
- mountain_pass
- temple_ruins

## 江東水域

- river_delta
- pirate_islands
- water_ruins

---

# 蜀漢 (14 AREA)

## 成都

- chengdu_city
- palace_garden
- scholar_district
- city_market

## 江州

- jiangzhou_port
- river_fort

## 永安

- yongan_fort
- cliff_path

## 武陵

- wuling_mountains
- spirit_forest
- hidden_valley

---

# 南方 (12 AREA)

## 長沙

- changsha_city
- southern_market
- farmland

## 零陵

- lingling_town
- mountain_road

## 桂陽

- guiyang_forest
- tribal_village

## 南蠻

- nanman_jungle
- serpent_temple
- jungle_ruins

---

# 世界秘境 (12 AREA)

## 古戰場

- guandu_battlefield
- chibi_battlefield
- tiger_pass_warzone

## 上古遺跡

- lost_dynasty_ruins
- ancient_machine_city
- celestial_temple

## 靈界入口

- spirit_gate
- ghost_valley
- nether_world

## 神秘之地

- immortal_valley
- star_fall_crater
- dragon_bone_ruins

---

# AREA 數量統計

| 類型 | 數量 |
|-----|------|
城市 | 22 |
城郊 | 18 |
軍事 | 16 |
江湖 | 18 |
探險 | 22 |
仙俠 | 14 |
詭異 | 10 |

總數：約 **120+ AREA**

---

# 建議開發順序

Phase 1 (新手區)

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

# map.md 範例

```
Theme: 江湖
LevelRange: 10-20

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

Connections:
west: loyang_city
east: dragon_channel
down: ancient_cave
```
