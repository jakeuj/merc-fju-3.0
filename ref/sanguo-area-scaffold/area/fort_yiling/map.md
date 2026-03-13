# 夷陵

## Metadata

- Id: `fort_yiling`
- Label: 夷陵
- Type: fort
- Theme: 軍旅
- Subtheme: 咽喉 / 關道
- Region: 蜀漢 (`shu`)
- LevelRange: 42-56
- Tags: chokepoint

## World Connections

- west: fort_yongan
- east: city_jiangling

## map.md Prose Scaffold

Theme: 軍旅
Subtheme: 咽喉 / 關道
Mood: 戒備、軍令、壓迫
SignatureScenes:
- 關門
- 望樓
- 營寨
NPC roles:
- 校尉
- 斥候
- 守兵
Quest hooks:
- 傳遞軍令
- 偵查敵情
- 修補防線
Interaction cues:
- #Enquire 關門
- #Enquire 軍營
- #Keyword 軍旗
Rumor seeds:
- 傳聞說 夷陵 一帶近來有不同尋常的動靜。
Secret node or hidden hook:
- 深處可能藏有條件解鎖的支路或事件房。

## Graph Context

Adjacent nodes:
- city_jiangling
- fort_yongan

## Suggested Room Clusters

- 關前道
- 關門
- 內營
- 望樓 / 密道

## TODO

- 補 3~8 個代表房間節點
- 決定 #Keyword / #Enquire / #Job
- 對齊鄰接 AREA 的進出口語意
- 補 NPC、怪物、掉落、任務與服務節點
- 依等級帶調整危險度與資源密度
