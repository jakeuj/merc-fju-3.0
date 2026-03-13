# 洛陽地下水區

## Metadata

- Id: `dng_loyang_sewer`
- Label: 洛陽地下水區
- Type: dungeon
- Theme: 仙俠
- Subtheme: 下水道 / 地下水脈
- Region: 中原 (`zhongyuan`)
- LevelRange: 12-22
- Tags: underground

## World Connections

- up: city_loyang
- down: dng_sewer_depths

## map.md Prose Scaffold

Theme: 仙俠
Subtheme: 下水道 / 地下水脈
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
- 傳聞說 洛陽地下水區 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 深處可能藏有條件解鎖的支路或事件房。

## Graph Context

Adjacent nodes:
- city_loyang
- dng_sewer_depths

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
