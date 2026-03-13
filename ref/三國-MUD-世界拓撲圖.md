
# 三國 MUD 世界完整拓撲圖

此文件提供 **三國 MUD 世界區域拓撲圖 (Topology Map)**。  
用途：

- 作為 `map.md` 規劃依據
- 規劃 AREA 連接
- 協助 generator / roo scaffold
- 確保世界探索路線合理

以下使用 **Mermaid graph** 描述世界拓撲。

---

# 世界主幹拓撲

```mermaid
graph LR

XILIANG[西涼]
TIANSHUI[天水]
ANDING[安定]
CHANGAN[長安]
HONGNONG[弘農]
HU_LAO[虎牢關]
LOYANG[洛陽]
CHENLIU[陳留]
XUZHOU[徐州]

XILIANG --> TIANSHUI
TIANSHUI --> ANDING
ANDING --> CHANGAN
CHANGAN --> HONGNONG
HONGNONG --> HU_LAO
HU_LAO --> LOYANG
LOYANG --> CHENLIU
CHENLIU --> XUZHOU
```
---

# 北方幽州拓撲

```mermaid
graph LR

LOYANG --> PUYANG[濮陽]
PUYANG --> NANPI[南皮]
NANPI --> BEIPING[北平]
BEIPING --> YIJING[易京]
YIJING --> BAILANG[白狼山]
BAILANG --> XIANGPING[襄平]
```
---

# 荊州拓撲

```mermaid
graph LR

LOYANG --> WAN[宛]
WAN --> XINYE[新野]
XINYE --> XIANGYANG[襄陽]
XIANGYANG --> JIANGXIA[江夏]
JIANGXIA --> CHAISANG[柴桑]

JIANGXIA --> YUNMENG[雲夢大澤]
XIANGYANG --> FANCASTLE[樊城]
```
---

# 江東拓撲

```mermaid
graph LR

XUZHOU --> SHOUCHUN[壽春]
SHOUCHUN --> JIANYE[建業]
JIANYE --> KUAJI[會稽]

JIANYE --> JIANGDONG_RIVER[江東水域]
JIANGDONG_RIVER --> PIRATE_ISLAND[海盜群島]
```
---

# 蜀漢拓撲

```mermaid
graph LR

CHENGDU[成都]
JIANGZHOU[江州]
YONGAN[永安]
JIANGLING[江陵]
WULING[武陵]
CHANGSHA[長沙]

CHENGDU --> JIANGZHOU
JIANGZHOU --> YONGAN
YONGAN --> JIANGLING
JIANGLING --> WULING
WULING --> CHANGSHA
```
---

# 南方拓撲

```mermaid
graph LR

CHANGSHA --> LINGLING[零陵]
LINGLING --> GUIYANG[桂陽]
GUIYANG --> NANHAI[南海]

GUIYANG --> NANMAN_JUNGLE[南蠻密林]
NANMAN_JUNGLE --> SERPENT_TEMPLE[蛇神殿]
```
---

# 秘境與世界事件拓撲

```mermaid
graph LR

LOYANG --> ANCIENT_TOMB[帝王古墓]
ANCIENT_TOMB --> TOMB_LABYRINTH[古墓迷宮]

BAILANG --> ANCIENT_CAVE[古洞遺跡]

YUNMENG --> SPIRIT_REALM[靈界入口]

WULING --> IMMORTAL_VALLEY[仙靈谷]
```
---

# 世界交通節點 (Choke Points)

| 節點 | 作用 |
|----|----|
虎牢關 | 中原東西門戶 |
函谷關 | 關中入口 |
易京 | 北方戰略要地 |
白狼山 | 遼東邊境 |
夷陵 | 蜀漢與荊州咽喉 |

---

# 世界區域統計

| 類型 | 數量 |
|---|---|
城市 | 14 |
城郊 | 12 |
軍事 | 10 |
江湖 | 10 |
探險 | 12 |
仙俠 | 8 |
詭異 | 6 |

總區域 ≈ **70–90 AREA**

---

# 建議 map.md 連線形式

```
Connections:

west: changan
east: loyang
north: puyang
south: xinye
down: ancient_tomb
enter: city_gate
```
