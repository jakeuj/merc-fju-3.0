# 帝王古墓

## Metadata

- Id: `dng_royal_tomb`
- Label: 帝王古墓
- Type: dungeon
- Theme: 探險遺跡
- Subtheme: 古墓 / 機關
- Region: 中原 (`zhongyuan`)
- LevelRange: 18-30
- Tags: dungeon

## World Connections

- up: dng_sewer_depths
- down: sec_catacomb_depths

## map.md Prose Scaffold

Theme: 探險遺跡
Subtheme: 古墓 / 機關
Mood: 幽深、危險、秘密感強
SignatureScenes:
- 入口前廳
- 陰暗通道
- 封印或機關
NPC roles:
- 守關怪物
- 殘魂
- 迷途者
Quest hooks:
- 深入調查
- 尋回遺物
- 破解封印
Interaction cues:
- #Enquire 入口
- #Keyword 石門
- #Keyword 符文
Rumor seeds:
- 傳聞說 帝王古墓 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 深處可能藏有條件解鎖的支路或事件房。

## Graph Context

Adjacent nodes:
- dng_sewer_depths
- sec_catacomb_depths

## Suggested Room Clusters

- 入口前廳
- 主通道
- 支路房
- 核心區 / Boss 房

## TODO

- 補 3~8 個代表房間節點
- 決定 #Keyword / #Enquire / #Job
- 對齊鄰接 AREA 的進出口語意
- 補 NPC、怪物、掉落、任務與服務節點
- 依等級帶調整危險度與資源密度
