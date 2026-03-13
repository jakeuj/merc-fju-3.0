# 黑石洞

## Metadata

- Id: `dng_black_rock_cave`
- Label: 黑石洞
- Type: dungeon
- Theme: 探險遺跡
- Subtheme: 山洞 / 古器
- Region: 關中西域 (`guanzhong`)
- LevelRange: 38-50
- Tags: dungeon

## World Connections

- up: wild_black_rock_hills
- down: sec_iron_sky_vault

## map.md Prose Scaffold

Theme: 探險遺跡
Subtheme: 山洞 / 古器
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
- 傳聞說 黑石洞 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 深處可能藏有條件解鎖的支路或事件房。

## Graph Context

Adjacent nodes:
- sec_iron_sky_vault
- wild_black_rock_hills

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
