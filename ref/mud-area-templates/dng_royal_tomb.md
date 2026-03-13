# 帝王古墓 (dng_royal_tomb)

地下迷宮 / dungeon AREA 模板

---

## Area Metadata

- AreaId: `dng_royal_tomb`
- Type: dungeon
- Theme: 探險遺跡
- Subtheme: 古墓 / 機關
- LevelRange: 20-35
- Tags: dungeon, tomb

---

## Area Concept

埋葬古代帝王的地下墓穴。

設計目標：

1. 探索迷宮
2. 機關解謎
3. Boss 房

---

## Signature Scenes

- 墓道入口
- 石門
- 陷阱通道
- 主墓室

---

## NPC Roles

- 守墓機關
- 墓靈
- 古墓守衛

---

## mapmd-json

```json
{
  "schema":"mapmd-json/v1",
  "areaId":"dng_royal_tomb",
  "type":"dungeon",
  "levelRange":"20-35",
  "topology":{
    "clusters":[
      {"id":"dng_royal_tomb:entry","label":"墓道入口"},
      {"id":"dng_royal_tomb:corridor","label":"墓道"},
      {"id":"dng_royal_tomb:trap","label":"陷阱區"},
      {"id":"dng_royal_tomb:boss","label":"主墓室"}
    ],
    "nodes":[
      {"id":"dng_royal_tomb.entry"},
      {"id":"dng_royal_tomb.corridor"},
      {"id":"dng_royal_tomb.trap"},
      {"id":"dng_royal_tomb.boss_room"}
    ],
    "edges":[
      {"from":"dng_royal_tomb.entry","to":"dng_royal_tomb.corridor"},
      {"from":"dng_royal_tomb.corridor","to":"dng_royal_tomb.trap"},
      {"from":"dng_royal_tomb.trap","to":"dng_royal_tomb.boss_room"}
    ]
  }
}
```