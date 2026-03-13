# 易京官道

## Metadata

- Id: `road_yijing`
- Label: 易京官道
- Type: road
- Theme: 軍旅
- Subtheme: 北方驛道
- Region: 幽州遼東 (`youzhou`)
- LevelRange: 22-32
- Tags: connector

## World Connections

- south: wild_beiping_outer
- north: fort_yijing

## map.md Prose Scaffold

Theme: 軍旅
Subtheme: 北方驛道
Mood: 旅途中轉、消息流通
SignatureScenes:
- 路亭
- 驛站牌
- 分岔口
NPC roles:
- 驛卒
- 旅人
- 押鏢人
Quest hooks:
- 問路
- 護送
- 攔查可疑過客
Interaction cues:
- #Enquire 去路
- #Keyword 路牌
- #Keyword 驛站
Rumor seeds:
- 傳聞說 易京官道 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 可預留一條支線通往地下區、秘境或特殊事件區。

## Graph Context

Adjacent nodes:
- fort_yijing
- wild_beiping_outer

## Suggested Room Clusters

- 路口
- 中段遭遇區
- 終點轉接節點

## TODO

- 補 3~8 個代表房間節點
- 決定 #Keyword / #Enquire / #Job
- 對齊鄰接 AREA 的進出口語意
- 補 NPC、怪物、掉落、任務與服務節點
- 依等級帶調整危險度與資源密度
