# 洛陽

## Metadata

- Id: `city_loyang`
- Label: 洛陽
- Type: city
- Theme: 歷史城市
- Subtheme: 帝都 / 新手主城
- Region: 中原 (`zhongyuan`)
- LevelRange: 1-15
- Tags: capital, hub

## World Connections

- west: fort_hulao
- east: city_chenliu
- enter: district_loyang_palace
- east: district_loyang_east_market
- west: district_loyang_west_market
- north: district_loyang_scholar
- east: wild_loyang_east
- north: road_puyang
- south: road_wan
- east: road_chenliu
- down: dng_loyang_sewer

## map.md Prose Scaffold

Theme: 歷史城市
Subtheme: 帝都 / 新手主城
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
- 傳聞說 洛陽 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 可預留一條支線通往地下區、秘境或特殊事件區。

## Graph Context

Adjacent nodes:
- city_chenliu
- district_loyang_east_market
- district_loyang_palace
- district_loyang_scholar
- district_loyang_west_market
- dng_loyang_sewer
- fort_hulao
- road_chenliu
- road_puyang
- road_wan
- wild_loyang_east

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
