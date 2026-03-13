# 虎牢關 (fort_hulao)

關隘 / choke point AREA 模板

---

## Area Metadata

- AreaId: `fort_hulao`
- Type: fort
- Region: 關中
- Theme: 軍旅
- Subtheme: 關隘 / 戰場
- LevelRange: 30-40
- Tags: chokepoint, battle

---

## Area Concept

虎牢關是東西交通的軍事咽喉。

設計目標：

1. 世界交通 choke point
2. 軍事任務區
3. 戰場事件區

---

## Signature Scenes

- 關門
- 關樓
- 軍營
- 望樓

---

## NPC Roles

- 守關將軍
- 巡邏士兵
- 軍需官

---

## mapmd-json

```json
{
  "schema":"mapmd-json/v1",
  "areaId":"fort_hulao",
  "type":"fort",
  "levelRange":"30-40",
  "topology":{
    "clusters":[
      {"id":"fort_hulao:approach","label":"關前道"},
      {"id":"fort_hulao:gate","label":"關門"},
      {"id":"fort_hulao:camp","label":"軍營"},
      {"id":"fort_hulao:watch","label":"望樓"}
    ],
    "nodes":[
      {"id":"fort_hulao.approach"},
      {"id":"fort_hulao.gate"},
      {"id":"fort_hulao.camp"},
      {"id":"fort_hulao.watch"}
    ],
    "edges":[
      {"from":"fort_hulao.approach","to":"fort_hulao.gate"},
      {"from":"fort_hulao.gate","to":"fort_hulao.camp"},
      {"from":"fort_hulao.camp","to":"fort_hulao.watch"}
    ]
  }
}
```