# 洛陽 (city_loyang)

大型城市 AREA 模板（城市 / hub 類型）

---

## Area Metadata

- AreaId: `city_loyang`
- Type: city
- Region: 中原 (zhongyuan)
- Theme: 歷史城市
- Subtheme: 帝都 / 商業 / 政治中心
- LevelRange: 1-15
- Tags: capital, hub, service

---

## Area Concept

洛陽是整個世界的核心城市。

設計目標：

1. 玩家主要活動城市
2. 任務與資訊中心
3. 服務 NPC 集中地

---

## Signature Scenes

- 城門
- 主街
- 東市
- 西市
- 皇城入口

---

## NPC Roles

- 城門守兵
- 店鋪掌櫃
- 說書人
- 官府差役

---

## World Links

| direction | target |
|---|---|
| east | wild_loyang_east |
| west | road_chenliu |
| north | road_puyang |
| south | road_wan |

---

## mapmd-json

```json
{
  "schema": "mapmd-json/v1",
  "areaId": "city_loyang",
  "type": "city",
  "levelRange": "1-15",
  "topology": {
    "clusters":[
      {"id":"city_loyang:gate","label":"城門"},
      {"id":"city_loyang:main","label":"主街"},
      {"id":"city_loyang:market","label":"市集"},
      {"id":"city_loyang:palace","label":"皇城入口"}
    ],
    "nodes":[
      {"id":"city_loyang.gate"},
      {"id":"city_loyang.street"},
      {"id":"city_loyang.market"},
      {"id":"city_loyang.palace_gate"}
    ],
    "edges":[
      {"from":"city_loyang.gate","to":"city_loyang.street"},
      {"from":"city_loyang.street","to":"city_loyang.market"},
      {"from":"city_loyang.street","to":"city_loyang.palace_gate"}
    ]
  }
}
```