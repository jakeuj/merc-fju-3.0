# 建業

## Metadata

- Id: `city_jianye`
- Label: 建業
- Type: city
- Theme: 歷史城市
- Subtheme: 江東都城
- Region: 江東 (`jiangdong`)
- LevelRange: 30-44
- Tags: hub, capital

## World Connections

- north: city_shouchun
- east: district_jianye_port
- south: fort_naval_base
- west: wild_jianye_west
- east: city_kuaiji
- south: wild_river_delta

## map.md Prose Scaffold

Theme: 歷史城市
Subtheme: 江東都城
Mood: 秩序、煙火氣、地方勢力流動
SignatureScenes:
- 城門
- 主街
- 市集
NPC roles:
- 守門兵
- 掌櫃
- 行人
Quest hooks:
- 打聽地方消息
- 協助跑腿送信
- 追查城內異聞
Interaction cues:
- #Enquire 城門
- #Enquire 市集
- #Keyword 告示
Rumor seeds:
- 傳聞說 建業 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 可預留一條支線通往地下區、秘境或特殊事件區。

## Graph Context

Adjacent nodes:
- city_kuaiji
- city_shouchun
- district_jianye_port
- fort_naval_base
- wild_jianye_west
- wild_river_delta

## Suggested Room Clusters

- 主入口 / 城門
- 主街 / 中央節點
- 服務區（店鋪 / 官署 / 驛站）
- 可延伸支線區

## TODO

- 補 3~8 個代表房間節點
- 決定 #Keyword / #Enquire / #Job
- 對齊鄰接 AREA 的進出口語意
- 補 NPC、怪物、掉落、任務與服務節點
- 依等級帶調整危險度與資源密度
