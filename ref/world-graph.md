# world-graph.md
此文件為 `world-graph.json` 的人類可讀說明版本，用來理解三國 MUD 世界拓撲結構。
主要用途：
- 世界地圖設計文件
- AREA 規劃參考
- `map.md` / `.roo` generator 的上位設計

---
## 世界統計
- Nodes (AREA 節點)： **130**
- Edges (連線)： **272**
- Regions： **9**

---
## Region 列表
- `zhongyuan` : 中原
- `guanzhong` : 關中西域
- `youzhou` : 幽州遼東
- `yanzhao` : 兗州河北
- `jingzhou` : 荊州
- `jiangdong` : 江東
- `shu` : 蜀漢
- `south` : 荊南南蠻
- `world_events` : 世界事件與秘境

---
## 中原 (`zhongyuan`)
節點數：18

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_loyang | 洛陽 | city | 歷史城市 | 1-15 |
| district_loyang_palace | 洛陽皇城 | district | 歷史城市 | 5-15 |
| district_loyang_east_market | 洛陽東市 | district | 歷史城市 | 1-10 |
| district_loyang_west_market | 洛陽西市 | district | 歷史城市 | 1-10 |
| district_loyang_scholar | 洛陽書院街 | district | 歷史城市 | 5-15 |
| wild_loyang_east | 洛陽東郊 | outskirts | 江湖 | 1-12 |
| wild_longqu_hills | 龍渠丘陵 | wild | 探險遺跡 | 8-18 |
| wild_fengqiu_forest | 封丘森林 | wild | 詭異民俗 | 10-20 |
| wild_farming_village | 河畔農村 | wild | 歷史城市 | 1-10 |
| road_puyang | 往濮陽官道 | road | 軍旅 | 8-18 |
| road_wan | 往宛官道 | road | 江湖 | 8-18 |
| road_chenliu | 往陳留驛路 | road | 歷史城市 | 8-18 |
| dng_loyang_sewer | 洛陽地下水區 | dungeon | 仙俠 | 12-22 |
| dng_sewer_depths | 地下深渠 | dungeon | 詭異民俗 | 15-25 |
| dng_royal_tomb | 帝王古墓 | dungeon | 探險遺跡 | 18-30 |
| sec_catacomb_depths | 忘川地穴 | secret | 仙俠 | 25-35 |
| wild_old_bridge | 古橋渡口 | wild | 江湖 | 6-16 |
| wild_tea_pavilion | 十里茶亭 | wild | 江湖 | 5-15 |

## 關中西域 (`guanzhong`)
節點數：30

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_changan | 長安 | city | 歷史城市 | 18-30 |
| district_changan_palace | 長安宮城 | district | 歷史城市 | 20-30 |
| district_changan_west_market | 長安西市 | district | 歷史城市 | 18-28 |
| district_changan_noble | 長安勳貴里 | district | 歷史城市 | 20-30 |
| wild_changan_outer | 長安外城 | outskirts | 江湖 | 18-28 |
| fort_hangu | 函谷關 | fort | 軍旅 | 22-34 |
| fort_hangu_outer | 函谷關前道 | fort | 軍旅 | 20-32 |
| fort_hangu_watch | 函谷關望樓 | fort | 軍旅 | 24-36 |
| road_western_trade | 西行商道 | road | 歷史城市 | 20-32 |
| city_hongnong | 弘農 | city | 歷史城市 | 16-28 |
| wild_hongnong_farmland | 弘農近郊 | wild | 歷史城市 | 14-24 |
| fort_hulao | 虎牢關 | fort | 軍旅 | 24-36 |
| city_anding | 安定 | city | 軍旅 | 24-36 |
| city_tianshui | 天水 | city | 軍旅 | 28-40 |
| city_xiliang | 西涼 | city | 軍旅 | 32-45 |
| wild_xiliang_steppe | 西涼荒原 | wild | 探險遺跡 | 30-42 |
| wild_oasis_settlement | 綠洲聚落 | wild | 歷史城市 | 30-42 |
| dng_desert_ruins | 荒漠遺跡 | dungeon | 探險遺跡 | 35-48 |
| sec_nomad_sky_temple | 蒼天祭壇 | secret | 仙俠 | 42-55 |
| wild_red_canyon | 赤崖峽谷 | wild | 軍旅 | 32-44 |
| wild_salt_road | 鹽商古道 | road | 江湖 | 28-40 |
| fort_border_camp | 邊塞大營 | fort | 軍旅 | 34-46 |
| wild_horse_plain | 牧馬平原 | wild | 軍旅 | 30-42 |
| dng_sand_burial_pit | 流沙葬坑 | dungeon | 詭異民俗 | 38-50 |
| sec_western_star_observatory | 西境觀星臺 | secret | 仙俠 | 45-58 |
| wild_wind_gate | 風門隘口 | fort | 軍旅 | 34-46 |
| road_return_changan | 還京官驛 | road | 歷史城市 | 20-30 |
| wild_black_rock_hills | 黑石丘陵 | wild | 探險遺跡 | 33-45 |
| dng_black_rock_cave | 黑石洞 | dungeon | 探險遺跡 | 38-50 |
| sec_iron_sky_vault | 鐵蒼穹秘庫 | secret | 探險遺跡 | 50-62 |

## 幽州遼東 (`youzhou`)
節點數：16

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_beiping | 北平 | city | 歷史城市 | 20-32 |
| district_beiping_market | 北平市集 | district | 歷史城市 | 20-30 |
| district_beiping_station | 北平車站 | district | 歷史城市 | 20-30 |
| wild_beiping_outer | 北平郊區 | outskirts | 江湖 | 18-28 |
| road_yijing | 易京官道 | road | 軍旅 | 22-32 |
| fort_yijing | 易京 | fort | 軍旅 | 26-38 |
| fort_northern_watch | 北方哨樓 | fort | 軍旅 | 28-40 |
| wild_bailang | 白狼山 | wild | 探險遺跡 | 30-42 |
| wild_wolf_forest | 狼林 | wild | 詭異民俗 | 32-44 |
| dng_ancient_cave | 古洞遺跡 | dungeon | 探險遺跡 | 35-48 |
| sec_spirit_peak | 白狼靈峰 | secret | 仙俠 | 42-55 |
| city_xiangping | 襄平 | city | 軍旅 | 34-46 |
| wild_liaodong_plain | 遼東平原 | wild | 軍旅 | 32-44 |
| wild_barbarian_camp | 胡營舊地 | wild | 軍旅 | 34-46 |
| road_north_border | 北境邊道 | road | 軍旅 | 34-46 |
| sec_starfall_crater | 星墜天坑 | secret | 仙俠 | 46-60 |

## 兗州河北 (`yanzhao`)
節點數：14

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_chenliu | 陳留 | city | 歷史城市 | 15-26 |
| district_chenliu_station | 陳留驛站 | district | 歷史城市 | 15-25 |
| wild_chenliu_west | 陳留西郊 | outskirts | 江湖 | 14-24 |
| city_puyang | 濮陽 | city | 軍旅 | 20-32 |
| wild_old_battlefield | 古戰場 | wild | 軍旅 | 22-34 |
| city_nanpi | 南皮 | city | 歷史城市 | 24-36 |
| wild_hebei_plain | 河北平原 | wild | 軍旅 | 24-36 |
| sec_yellow_turban_ruins | 黃巾殘營 | secret | 詭異民俗 | 28-40 |
| fort_river_crossing | 渡河營寨 | fort | 軍旅 | 26-38 |
| road_nanpi_beiping | 河北北道 | road | 歷史城市 | 24-36 |
| road_chenliu_loyang | 洛陳驛路 | road | 歷史城市 | 12-22 |
| wild_floodplain | 河濱灘地 | wild | 詭異民俗 | 20-30 |
| dng_river_cavern | 河蝕洞窟 | dungeon | 探險遺跡 | 28-40 |
| sec_dragonbone_ford | 龍骨淺灘 | secret | 探險遺跡 | 35-48 |

## 荊州 (`jingzhou`)
節點數：16

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_wan | 宛 | city | 歷史城市 | 14-24 |
| wild_wan_outer | 宛城外道 | outskirts | 江湖 | 14-24 |
| city_xinye | 新野 | city | 江湖 | 18-30 |
| wild_xinye_fields | 新野郊野 | wild | 江湖 | 18-28 |
| city_xiangyang | 襄陽 | city | 軍旅 | 24-38 |
| fort_fancheng | 樊城 | fort | 軍旅 | 26-40 |
| road_jingxiang | 荊襄大道 | road | 江湖 | 22-34 |
| city_jiangxia | 江夏 | city | 軍旅 | 28-42 |
| fort_river_fort | 水軍寨 | fort | 軍旅 | 30-44 |
| wild_yunmeng | 雲夢大澤 | wild | 詭異民俗 | 30-44 |
| dng_sunken_temple | 沉沒古廟 | dungeon | 仙俠 | 36-50 |
| sec_spirit_marsh | 澤靈沼境 | secret | 仙俠 | 44-58 |
| city_chaisang | 柴桑 | city | 歷史城市 | 30-42 |
| wild_reed_bank | 蘆葦水岸 | wild | 江湖 | 24-36 |
| dng_boat_graveyard | 沉舟墓場 | dungeon | 探險遺跡 | 34-48 |
| sec_spirit_gate | 靈界入口 | secret | 仙俠 | 48-62 |

## 江東 (`jiangdong`)
節點數：14

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_xuzhou | 徐州 | city | 歷史城市 | 20-32 |
| city_shouchun | 壽春 | city | 歷史城市 | 24-36 |
| wild_shouchun_fields | 壽春田野 | wild | 歷史城市 | 22-34 |
| city_jianye | 建業 | city | 歷史城市 | 30-44 |
| district_jianye_port | 建業港區 | district | 歷史城市 | 30-42 |
| fort_naval_base | 水軍大營 | fort | 軍旅 | 32-46 |
| wild_jianye_west | 建業西郊 | outskirts | 江湖 | 28-40 |
| city_kuaiji | 會稽 | city | 江湖 | 34-48 |
| wild_mountain_pass | 會稽山道 | wild | 江湖 | 34-46 |
| dng_temple_ruins | 山中古寺 | dungeon | 仙俠 | 40-54 |
| wild_river_delta | 江東水域 | wild | 探險遺跡 | 34-48 |
| wild_pirate_islands | 海盜群島 | wild | 江湖 | 40-54 |
| sec_water_ruins | 水底遺跡 | secret | 仙俠 | 48-62 |
| road_shouchun_xuzhou | 淮東官道 | road | 歷史城市 | 20-32 |

## 蜀漢 (`shu`)
節點數：12

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_chengdu | 成都 | city | 歷史城市 | 34-48 |
| district_chengdu_market | 成都市井 | district | 歷史城市 | 34-46 |
| district_chengdu_scholar | 成都學舍 | district | 歷史城市 | 36-48 |
| wild_chengdu_outer | 成都近郊 | outskirts | 江湖 | 30-42 |
| city_jiangzhou | 江州 | city | 歷史城市 | 36-50 |
| fort_yongan | 永安 | fort | 軍旅 | 40-54 |
| fort_yiling | 夷陵 | fort | 軍旅 | 42-56 |
| city_jiangling | 江陵 | city | 歷史城市 | 38-52 |
| wild_wuling | 武陵山 | wild | 仙俠 | 40-54 |
| wild_spirit_forest | 靈木森林 | wild | 仙俠 | 42-56 |
| wild_hidden_valley | 隱谷 | wild | 探險遺跡 | 44-58 |
| dng_ancient_tomb_shu | 蜀漢古墓 | dungeon | 探險遺跡 | 48-62 |

## 荊南南蠻 (`south`)
節點數：7

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| city_changsha | 長沙 | city | 歷史城市 | 30-42 |
| city_lingling | 零陵 | city | 江湖 | 34-46 |
| city_guiyang | 桂陽 | city | 江湖 | 36-48 |
| city_nanhai | 南海 | city | 探險遺跡 | 40-54 |
| wild_nanman_jungle | 南蠻密林 | wild | 探險遺跡 | 42-56 |
| dng_serpent_temple | 蛇神殿 | dungeon | 詭異民俗 | 48-62 |
| sec_jungle_ruins | 叢林遺城 | secret | 仙俠 | 54-68 |

## 世界事件與秘境 (`world_events`)
節點數：3

| id | 名稱 | type | theme | level |
|----|----|----|----|----|
| sec_chibi_battlefield | 赤壁古戰場 | secret | 軍旅 | 50-65 |
| sec_machine_city | 機關古城 | secret | 探險遺跡 | 55-70 |
| sec_nether_world | 冥域 | secret | 仙俠 | 60-75 |

---
## Edge 示例
以下為部分世界連線示例：

| from | to | direction |
|----|----|----|
| city_xiliang | city_tianshui | east |
| city_tianshui | city_xiliang | west |
| city_tianshui | city_anding | east |
| city_anding | city_tianshui | west |
| city_anding | city_changan | east |
| city_changan | city_anding | west |
| city_changan | city_hongnong | east |
| city_hongnong | city_changan | west |
| city_hongnong | fort_hangu | east |
| fort_hangu | city_hongnong | west |
| fort_hangu | fort_hulao | east |
| fort_hulao | fort_hangu | west |
| fort_hulao | city_loyang | east |
| city_loyang | fort_hulao | west |
| city_loyang | city_chenliu | east |
| city_chenliu | city_loyang | west |
| city_chenliu | city_xuzhou | east |
| city_xuzhou | city_chenliu | west |
| city_loyang | district_loyang_palace | enter |
| district_loyang_palace | city_loyang | out |
| city_loyang | district_loyang_east_market | east |
| district_loyang_east_market | city_loyang | west |
| city_loyang | district_loyang_west_market | west |
| district_loyang_west_market | city_loyang | east |
| city_loyang | district_loyang_scholar | north |
| district_loyang_scholar | city_loyang | south |
| city_loyang | wild_loyang_east | east |
| wild_loyang_east | city_loyang | west |
| wild_loyang_east | wild_longqu_hills | east |
| wild_longqu_hills | wild_loyang_east | west |
| wild_loyang_east | wild_fengqiu_forest | north |
| wild_fengqiu_forest | wild_loyang_east | south |
| wild_loyang_east | wild_farming_village | south |
| wild_farming_village | wild_loyang_east | north |
| city_loyang | road_puyang | north |
| road_puyang | city_loyang | south |
| city_loyang | road_wan | south |
| road_wan | city_loyang | north |
| city_loyang | road_chenliu | east |
| road_chenliu | city_loyang | west |

(完整連線請參考 `world-graph.json`)

---
## Node Schema
```json
{
"id": "city_loyang",
"label": "洛陽",
"type": "city",
"theme": "歷史城市",
"region": "zhongyuan",
"levelRange": "1-15",
"subtheme": "帝都 / 新手主城",
"tags": ["capital","hub"]
}
```

---
## Edge Schema
```json
{
"from": "city_loyang",
"to": "city_chenliu",
"direction": "east"
}
```

---
## 使用建議
1. `world-graph.json` 作為世界拓撲核心。
2. 每個 node 對應一個 AREA。
3. edges 對應 AREA 間出口。
4. AREA 內再展開為 rooms。
