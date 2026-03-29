# 隱谷 (`wild_hidden_valley`)

## Area Intent

`wild_hidden_valley` 承接 `wild_wuling` 的隱谷西徑，把武陵山深處原本只像獵戶與失蹤者口耳相傳的谷地正式展成一段可載入 wild。這裡不再靠高處視野或異象壓迫人，而是用更收束的地勢、更多殘痕與更安靜的危險感，讓玩家意識到自己正走進一塊可能通往更古老地下遺跡的前帶。

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `隱谷 / 秘徑`
- LevelRange: `44-58`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_hidden_valley",
    "title": "隱谷",
    "design_notes": "第一版 spec-first 草案。先固定谷口折徑、殘碑岔地、伏苔斷階、靜風谷坪、舊獵人棚、裂石空場、藏泉石罅與沉陵坳口，把武陵山西岔後的深谷前帶正式展成可載入 wild。",
    "level_range": "44-58",
    "planned_vnum_range": "19001-19020",
    "reserved_room_block": "19001-19020",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "隱谷 / 秘徑"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 19001,
        "target_area": "wild_wuling",
        "target_room_vnum": 15010,
        "label": "隱谷西徑"
      },
      {
        "direction": "down",
        "source_vnum": 19008,
        "target_area": "dng_ancient_tomb_shu",
        "target_room_vnum": 19101,
        "label": "沉陵坳口"
      }
    ],
    "clusters": [
      { "id": "entry", "label": "谷口入口帶" },
      { "id": "path", "label": "殘碑與斷階" },
      { "id": "valley", "label": "谷坪與獵棚" },
      { "id": "depth", "label": "裂石與沉陵前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 19001,
      "name": "谷口折徑",
      "description": "從武陵山的隱谷西徑再往內一步，山路就忽然收成一道較低而更靜的折徑。這裡的風不像高處那麼顯眼，卻總帶著一種讓人下意識放輕腳步的壓力，像谷裡本來就不歡迎太張揚的來客。",
      "sector_type": "SECT_FIELD",
      "cluster": "entry",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "world-link-east"],
      "exits": [
        { "direction": "east", "to": 15010, "external": true },
        { "direction": "west", "to": 19002 }
      ],
      "enquires": ["山路", "回去", "谷裡"]
    },
    {
      "vnum": 19002,
      "name": "殘碑岔地",
      "description": "一截半埋在土裡的殘碑斜斜立在岔地中央，碑面字痕幾乎被苔與泥吃光，只剩它還努力維持著這裡曾有路名與去向的樣子。比起指路，它現在更像在提醒人不要太相信眼前任何看似自然的通道。",
      "sector_type": "SECT_FIELD",
      "cluster": "path",
      "coord": [-1, 0, 0],
      "labels": ["junction", "stele", "landmark"],
      "exits": [
        { "direction": "east", "to": 19001 },
        { "direction": "north", "to": 19003 },
        { "direction": "west", "to": 19004 }
      ],
      "enquires": ["石碑", "岔路", "方向"]
    },
    {
      "vnum": 19003,
      "name": "伏苔斷階",
      "description": "斷階沿著低坡斜斜往上露出，石面全被厚苔覆住，只剩踩上去時那種過於整齊的硬感提醒你它原本不是天然形成。這裡像一段被山谷慢慢吞掉的舊路，既像遺跡，也像警告。",
      "sector_type": "SECT_FIELD",
      "cluster": "path",
      "coord": [-1, 1, 0],
      "labels": ["steps", "moss", "old-road"],
      "exits": [
        { "direction": "south", "to": 19002 },
        { "direction": "west", "to": 19005 }
      ],
      "enquires": ["斷階", "苔", "舊路"]
    },
    {
      "vnum": 19004,
      "name": "靜風谷坪",
      "description": "谷坪看起來平整得近乎不自然，連風到了這裡都像先停一拍再繼續往前走。你很難說出哪裡不對，只會本能覺得這塊地曾經被人用過，而且用途恐怕不只是獵戶歇腳那麼單純。",
      "sector_type": "SECT_FIELD",
      "cluster": "valley",
      "coord": [-2, 0, 0],
      "labels": ["plaza", "valley-floor", "quiet"],
      "exits": [
        { "direction": "east", "to": 19002 },
        { "direction": "north", "to": 19005 },
        { "direction": "south", "to": 19006 }
      ],
      "enquires": ["谷坪", "風", "這裡"]
    },
    {
      "vnum": 19005,
      "name": "舊獵人棚",
      "description": "幾根灰木與傾倒棚架還勉強支著這處舊獵人棚，棚下殘留的繩鉤、火痕與刮刀口讓人看得出曾有人在谷裡待得比普通路過更久。最奇怪的是，這些痕跡都停在某個時間點之後，再也沒人回來補完它們。",
      "sector_type": "SECT_FIELD",
      "cluster": "valley",
      "coord": [-2, 1, 0],
      "labels": ["camp", "shelter", "hunter"],
      "exits": [
        { "direction": "south", "to": 19004 },
        { "direction": "east", "to": 19003 },
        { "direction": "west", "to": 19007 }
      ],
      "enquires": ["獵人", "棚子", "痕跡"]
    },
    {
      "vnum": 19006,
      "name": "裂石空場",
      "description": "空場中央有一道向內收束的裂石縫，像地面曾被什麼東西從裡頭硬頂開過，再慢慢冷掉。周圍沒有真正的遺構，卻到處是讓人懷疑這裡曾被當成某種前場或試探口的痕跡。",
      "sector_type": "SECT_FIELD",
      "cluster": "depth",
      "coord": [-2, -1, 0],
      "labels": ["open-ground", "split-rock", "warning"],
      "exits": [
        { "direction": "north", "to": 19004 },
        { "direction": "west", "to": 19008 }
      ],
      "enquires": ["裂石", "空場", "下面"]
    },
    {
      "vnum": 19007,
      "name": "藏泉石罅",
      "description": "石罅裡滲出的細泉很清，卻沒有讓這附近多出半分安穩感，反而像把谷裡更深處的冷氣息慢慢帶了上來。站在這裡時，很容易覺得自己離某種真正被掩起來的入口已經不遠了。",
      "sector_type": "SECT_FIELD",
      "cluster": "depth",
      "coord": [-3, 1, 0],
      "labels": ["spring", "crevice", "hidden"],
      "exits": [
        { "direction": "east", "to": 19005 },
        { "direction": "south", "to": 19008 }
      ],
      "enquires": ["泉", "石縫", "入口"]
    },
    {
      "vnum": 19008,
      "name": "沉陵坳口",
      "description": "坳口地勢往內塌出一道不太自然的陰口，像山谷在這裡忽然轉成了另一種更古、更閉鎖的地形語言。即使還沒真正下探，也能感覺到底下那股氣息跟普通深谷完全不是一回事。",
      "sector_type": "SECT_FIELD",
      "cluster": "depth",
      "coord": [-3, 0, -1],
      "labels": ["sink", "future-down", "deep-link"],
      "exits": [
        { "direction": "east", "to": 19006 },
        { "direction": "north", "to": 19007 },
        { "direction": "down", "to": 19101, "external": true }
      ],
      "enquires": ["坳口", "下面", "古陵"]
    }
  ]
}
```
