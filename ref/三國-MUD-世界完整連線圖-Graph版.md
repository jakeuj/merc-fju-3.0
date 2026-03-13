# 三國 MUD 世界完整連線圖（Graph 版）

此文件提供 **三國 MUD 世界完整連線圖（Graph 版）**，用來作為：

- `map.md` / `mapmd-json` 的世界拓樸參考
- `.roo` / generator 的上位世界圖
- AREA 之間的連線規劃藍圖
- choke point / branch / secret-zone 的結構依據

設計原則：

- 主幹線清楚
- 各州郡有支線與回環
- 城市、郊外、關隘、秘境分層
- 保留逐步擴寫到 120+ AREA 的空間

---

## 一、Graph 使用說明

節點命名規則：

- `city_*`：主城 / 城鎮
- `road_*`：官道 / 交通區
- `wild_*`：野外 / 山林 / 郊區
- `fort_*`：關隘 / 軍事據點
- `dng_*`：地下 / 洞窟 / 古墓
- `sec_*`：秘境 / 靈界 / 上古遺跡
- `hub_*`：世界級交通樞紐

連線類型建議：

- `-->`：主線單向理解可視為世界導向
- 實作時可依 AREA 改成雙向
- 關隘與秘境可做成條件解鎖、單向門、事件門

---

## 二、世界總覽 Graph

```mermaid
graph TD

%% ===== 中原主骨架 =====
city_xiliang[西涼]
city_tianshui[天水]
city_anding[安定]
city_changan[長安]
city_hongnong[弘農]
fort_hangu[函谷關]
fort_hulao[虎牢關]
city_loyang[洛陽]
city_chenliu[陳留]
city_xuzhou[徐州]

city_xiliang --> city_tianshui
city_tianshui --> city_anding
city_anding --> city_changan
city_changan --> city_hongnong
city_hongnong --> fort_hangu
fort_hangu --> fort_hulao
fort_hulao --> city_loyang
city_loyang --> city_chenliu
city_chenliu --> city_xuzhou

%% ===== 北方支線 =====
city_loyang --> city_puyang[濮陽]
city_puyang --> city_nanpi[南皮]
city_nanpi --> city_beiping[北平]
city_beiping --> fort_yijing[易京]
fort_yijing --> wild_bailang[白狼山]
wild_bailang --> city_xiangping[襄平]

%% ===== 荊州支線 =====
city_loyang --> city_wan[宛]
city_wan --> city_xinye[新野]
city_xinye --> city_xiangyang[襄陽]
city_xiangyang --> city_jiangxia[江夏]
city_jiangxia --> city_chaisang[柴桑]
city_jiangxia --> wild_yunmeng[雲夢大澤]

%% ===== 江東支線 =====
city_xuzhou --> city_shouchun[壽春]
city_shouchun --> city_jianye[建業]
city_jianye --> city_kuaiji[會稽]

%% ===== 南方支線 =====
city_chaisang --> city_changsha[長沙]
city_changsha --> city_lingling[零陵]
city_lingling --> city_guiyang[桂陽]
city_guiyang --> city_nanhai[南海]

%% ===== 蜀漢主線 =====
city_chengdu[成都]
city_jiangzhou[江州]
fort_yongan[永安]
city_jiangling[江陵]
wild_wuling[武陵]
city_changsha --> wild_wuling
city_chengdu --> city_jiangzhou
city_jiangzhou --> fort_yongan
fort_yongan --> city_jiangling
city_jiangling --> wild_wuling

%% ===== 荊州-蜀漢咽喉 =====
fort_yiling[夷陵]
fort_yongan --> fort_yiling
fort_yiling --> city_jiangling
```

---

## 三、中原核心區 Graph

```mermaid
graph LR

city_loyang[洛陽]
wild_loyang_east[洛陽東郊]
wild_longqu[龍渠丘陵]
wild_fengqiu[封丘森林]
dng_loyang_sewer[洛陽地下水區]
road_to_puyang[往濮陽官道]
road_to_wan[往宛官道]
dng_ancient_tomb[帝王古墓]
sec_catacomb_depths[忘川地穴]

city_loyang --> wild_loyang_east
wild_loyang_east --> wild_longqu
wild_loyang_east --> wild_fengqiu
city_loyang --> dng_loyang_sewer
dng_loyang_sewer --> dng_ancient_tomb
dng_ancient_tomb --> sec_catacomb_depths
city_loyang --> road_to_puyang
city_loyang --> road_to_wan
```

### 中原區節點說明

| 節點 | 類型 | 題材 |
|---|---|---|
| 洛陽 | 城市 hub | 歷史城市 |
| 洛陽東郊 | 城郊 | 江湖 / 新手野外 |
| 龍渠丘陵 | 野外 | 探險遺跡 |
| 封丘森林 | 野外 | 詭異民俗 |
| 洛陽地下水區 | 地下 | 仙俠 / 詭異 |
| 帝王古墓 | 深層地下 | 探險 / 仙俠 |

---

## 四、關中與西域 Graph

```mermaid
graph LR

city_changan[長安]
wild_changan_outer[長安外城]
fort_hangu[函谷關]
road_western_trade[西行商道]
city_anding[安定]
city_tianshui[天水]
city_xiliang[西涼]
wild_xiliang_steppe[西涼荒原]
wild_oasis[綠洲聚落]
dng_desert_ruins[荒漠遺跡]
sec_nomad_sky_temple[蒼天祭壇]

city_changan --> wild_changan_outer
city_changan --> fort_hangu
city_changan --> road_western_trade
road_western_trade --> city_anding
city_anding --> city_tianshui
city_tianshui --> city_xiliang
city_xiliang --> wild_xiliang_steppe
wild_xiliang_steppe --> wild_oasis
wild_xiliang_steppe --> dng_desert_ruins
dng_desert_ruins --> sec_nomad_sky_temple
```

---

## 五、北方幽州 Graph

```mermaid
graph LR

city_beiping[北平]
wild_beiping_outer[北平郊區]
road_yijing[易京官道]
fort_yijing[易京]
fort_northern_watch[北方哨樓]
wild_bailang[白狼山]
wild_wolf_forest[狼林]
dng_ancient_cave[古洞遺跡]
sec_spirit_peak[白狼靈峰]
city_xiangping[襄平]
wild_liaodong_plain[遼東平原]

city_beiping --> wild_beiping_outer
wild_beiping_outer --> road_yijing
road_yijing --> fort_yijing
fort_yijing --> fort_northern_watch
fort_yijing --> wild_bailang
wild_bailang --> wild_wolf_forest
wild_bailang --> dng_ancient_cave
dng_ancient_cave --> sec_spirit_peak
wild_bailang --> city_xiangping
city_xiangping --> wild_liaodong_plain
```

---

## 六、兗州與河北 Graph

```mermaid
graph LR

city_chenliu[陳留]
wild_chenliu_west[陳留西郊]
road_puyang[陳留北道]
city_puyang[濮陽]
wild_old_battlefield[古戰場]
city_nanpi[南皮]
wild_hebei_plain[河北平原]
sec_yellow_turban_ruins[黃巾殘營]
fort_river_crossing[渡河營寨]

city_chenliu --> wild_chenliu_west
city_chenliu --> road_puyang
road_puyang --> city_puyang
city_puyang --> wild_old_battlefield
city_puyang --> city_nanpi
city_nanpi --> wild_hebei_plain
wild_old_battlefield --> sec_yellow_turban_ruins
wild_hebei_plain --> fort_river_crossing
```

---

## 七、荊州 Graph

```mermaid
graph LR

city_xinye[新野]
wild_xinye_fields[新野郊野]
city_xiangyang[襄陽]
fort_fancheng[樊城]
road_jingxiang[荊襄大道]
city_jiangxia[江夏]
fort_river_fort[水軍寨]
wild_yunmeng[雲夢大澤]
dng_sunken_temple[沉沒古廟]
sec_spirit_marsh[澤靈沼境]
city_chaisang[柴桑]

city_xinye --> wild_xinye_fields
wild_xinye_fields --> city_xiangyang
city_xiangyang --> fort_fancheng
city_xiangyang --> road_jingxiang
road_jingxiang --> city_jiangxia
city_jiangxia --> fort_river_fort
city_jiangxia --> city_chaisang
city_jiangxia --> wild_yunmeng
wild_yunmeng --> dng_sunken_temple
dng_sunken_temple --> sec_spirit_marsh
```

---

## 八、江東 Graph

```mermaid
graph LR

city_shouchun[壽春]
wild_shouchun_fields[壽春田野]
city_jianye[建業]
wild_jianye_west[建業西郊]
fort_naval_base[水軍大營]
city_kuaiji[會稽]
wild_mountain_pass[山道關口]
dng_temple_ruins[山中古寺]
wild_river_delta[江東水域]
wild_pirate_islands[海盜群島]
sec_water_ruins[水底遺跡]

city_shouchun --> wild_shouchun_fields
city_shouchun --> city_jianye
city_jianye --> wild_jianye_west
city_jianye --> fort_naval_base
city_jianye --> city_kuaiji
city_kuaiji --> wild_mountain_pass
wild_mountain_pass --> dng_temple_ruins
city_jianye --> wild_river_delta
wild_river_delta --> wild_pirate_islands
wild_pirate_islands --> sec_water_ruins
```

---

## 九、蜀漢 Graph

```mermaid
graph LR

city_chengdu[成都]
wild_chengdu_outer[成都近郊]
city_jiangzhou[江州]
fort_yongan[永安]
fort_yiling[夷陵]
city_jiangling[江陵]
wild_wuling[武陵山]
wild_spirit_forest[靈木森林]
wild_hidden_valley[隱谷]
dng_ancient_tomb_shu[蜀漢古墓]
sec_immortal_valley[仙靈谷]

city_chengdu --> wild_chengdu_outer
city_chengdu --> city_jiangzhou
city_jiangzhou --> fort_yongan
fort_yongan --> fort_yiling
fort_yiling --> city_jiangling
city_jiangling --> wild_wuling
wild_wuling --> wild_spirit_forest
wild_wuling --> wild_hidden_valley
wild_hidden_valley --> dng_ancient_tomb_shu
dng_ancient_tomb_shu --> sec_immortal_valley
```

---

## 十、南方與南蠻 Graph

```mermaid
graph LR

city_changsha[長沙]
wild_changsha_outer[長沙郊野]
city_lingling[零陵]
wild_mountain_road[南嶺山道]
city_guiyang[桂陽]
wild_guiyang_forest[桂陽山林]
city_nanhai[南海]
wild_nanhai_port[海港外埠]
wild_nanman_jungle[南蠻密林]
dng_serpent_temple[蛇神殿]
sec_jungle_ruins[叢林遺城]
sec_deep_swamp_altar[深澤祭壇]

city_changsha --> wild_changsha_outer
city_changsha --> city_lingling
city_lingling --> wild_mountain_road
wild_mountain_road --> city_guiyang
city_guiyang --> wild_guiyang_forest
city_guiyang --> city_nanhai
city_guiyang --> wild_nanman_jungle
wild_nanman_jungle --> dng_serpent_temple
wild_nanman_jungle --> sec_jungle_ruins
sec_jungle_ruins --> sec_deep_swamp_altar
city_nanhai --> wild_nanhai_port
```

---

## 十一、世界級秘境與事件 Graph

```mermaid
graph LR

sec_guandu[官渡古戰場]
sec_chibi[赤壁古戰場]
sec_hulao_war[虎牢幻戰]
sec_lost_dynasty[失落王朝遺跡]
sec_machine_city[機關古城]
sec_celestial_temple[天衡神殿]
sec_spirit_gate[靈界入口]
sec_ghost_valley[幽魂山谷]
sec_nether_world[冥域]
sec_starfall[星墜天坑]
sec_dragonbone[龍骸遺原]

city_puyang --> sec_guandu
city_chaisang --> sec_chibi
fort_hulao --> sec_hulao_war
wild_longqu --> sec_lost_dynasty
sec_lost_dynasty --> sec_machine_city
sec_machine_city --> sec_celestial_temple
wild_yunmeng --> sec_spirit_gate
sec_spirit_gate --> sec_ghost_valley
sec_ghost_valley --> sec_nether_world
wild_bailang --> sec_starfall
sec_starfall --> sec_dragonbone
```

---

## 十二、120+ AREA 擴充用分層規則

你之後若要從目前世界圖擴到 **120+ AREA**，建議每個主節點都拆成 3～6 個子節點：

### 城市節點拆法

- 外城門
- 主街
- 市集
- 官府 / 軍營 / 銀行
- 居民區
- 特殊入口（下水道 / 皇宮 / 驛站）

### 郊外節點拆法

- 官道
- 岔路口
- 農田 / 林地
- 廢屋 / 破廟
- 特殊怪區
- 秘密支線入口

### 關隘節點拆法

- 關前道
- 外寨
- 關門
- 關樓
- 軍械所
- 後山密道

### 地下 / 秘境節點拆法

- 入口前廳
- 主廊道
- 支路房
- 機關 / 封印房
- 核心區
- 隱藏房 / Boss 房

---

## 十三、推薦 Graph 對接格式

在 `map.md` / `mapmd-json` 中可對應成：

```md
Theme: 軍旅
Subtheme: 關隘守備
LevelRange: 25-35

Connections:
west: city_hongnong
east: fort_hulao
north: fort_watchtower
south: wild_supply_route
down: dng_secret_tunnel
```

Graph node metadata 建議：

```json
{
  "id": "fort_hulao",
  "label": "虎牢關",
  "type": "fort",
  "theme": "軍旅",
  "subtheme": "關隘 / 戰場",
  "levelRange": "30-40",
  "worldLinks": ["city_hongnong", "city_loyang", "sec_hulao_war"]
}
```

---

## 十四、優先實作順序

### Phase 1：新手可玩主線

- 洛陽
- 洛陽東郊
- 龍渠丘陵
- 洛陽地下水區

### Phase 2：北方支線

- 北平
- 北平郊區
- 易京
- 白狼山

### Phase 3：荊州支線

- 新野
- 襄陽
- 江夏
- 雲夢大澤

### Phase 4：關中西域

- 長安
- 函谷關
- 西涼荒原

### Phase 5：蜀漢與江東

- 建業
- 會稽
- 成都
- 武陵山

### Phase 6：世界級秘境

- 帝王古墓
- 黃巾殘營
- 赤壁古戰場
- 靈界入口
- 天衡神殿

---

## 十五、總結

這份 Graph 版世界圖可以當成你的 **上位世界 schema**：

- 橫向：州郡主線交通
- 縱向：城市 → 郊外 → 關隘 / 地下 / 秘境
- 深度：支線、隱藏區、世界事件區

如果你下一步要進入真正可生成的規格化階段，最適合接著做的是：

1. `world-graph.json`
2. 各大州郡 `map.md`
3. 節點等級分佈表
4. world connector / choke point 規格表
