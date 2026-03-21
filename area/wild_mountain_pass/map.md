# 會稽山道 (`wild_mountain_pass`)

## Area Intent

`wild_mountain_pass` 承接 `wild_jianye_west` 的南去坡口，把江東主城外帶的水氣與村路節奏正式推進成抬升的石磴、棧路與風口岔徑，讓玩家在進入 `city_kuaiji` 前先經過一段真正有遠行感的山路 wild。

## Theme Positioning

- Theme: `江湖`
- Subtheme: `山道 / 棧路`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_mountain_pass",
    "title": "會稽山道",
    "design_notes": "第一版 spec-first 草案。先固定北側入山坡口、石磴主線、風碑岔台、山腰茶棚、祠痕裂階與南下進城前路，讓建業鏈正式轉進會稽方向的山道 wild。",
    "level_range": "100-100",
    "planned_vnum_range": "16301-16330",
    "reserved_room_block": "16301-16330",
    "theme": {
      "primary": "江湖",
      "secondary": "山道 / 棧路"
    },
    "world_links": [
      {
        "direction": "north",
        "source_vnum": 16301,
        "target_area": "wild_jianye_west",
        "label": "建業南坡"
      },
      {
        "direction": "south",
        "source_vnum": 16310,
        "target_area": "city_kuaiji",
        "label": "會稽北口"
      },
      {
        "direction": "down",
        "source_vnum": 16306,
        "target_area": "dng_temple_ruins",
        "label": "山腹古祠"
      }
    ],
    "clusters": [
      { "id": "north-entry", "label": "入山坡口" },
      { "id": "stone-steps", "label": "石磴主線" },
      { "id": "wind-fork", "label": "風口岔台" },
      { "id": "rest-shelf", "label": "茶棚歇腳" },
      { "id": "cliff-path", "label": "崖邊棧路" }
    ]
  },
  "rooms": [
    {
      "vnum": 16301,
      "name": "入山坡口",
      "description": "從建業西郊再往南走，地勢終於開始把人的步子往上拉。這裡還留著官道餘韻，但風已經先一步變成山風，像在提醒每個旅人從這裡開始，路不再只是把人送離主城，而是真正把人帶進另一種地貌。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-entry",
      "coord": [0, 0, 0],
      "labels": ["north-link", "entry"],
      "exits": [
        { "direction": "north", "to": 16210, "external": true },
        { "direction": "south", "to": 16303 },
        { "direction": "east", "to": 16302 }
      ],
      "enquires": ["山路", "北邊", "建業"]
    },
    {
      "vnum": 16302,
      "name": "坡邊石級",
      "description": "石級沿著坡邊一階一階往上盤去，讓視野雖然還沒有真正打開，腳底卻已經先學會該怎麼跟著山勢呼吸。這裡不像險地，卻已經很明白地把平地上的直線習慣改成了山路的耐心。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "north-entry",
      "coord": [1, 0, 0],
      "labels": ["stone-step", "slope"],
      "exits": [
        { "direction": "west", "to": 16301 }
      ],
      "enquires": ["石級", "坡邊"]
    },
    {
      "vnum": 16303,
      "name": "松風棧道",
      "description": "棧道貼著山壁往前伸去，松風從高處一陣陣掃下來，讓人很難再把這裡當成單純的離城路。走到這一段時，主城的秩序感已經退成背後的記憶，取而代之的是山路本身的節奏。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "stone-steps",
      "coord": [0, -1, 0],
      "labels": ["main-road", "plank-way"],
      "exits": [
        { "direction": "north", "to": 16301 },
        { "direction": "south", "to": 16304 },
        { "direction": "east", "to": 16305 }
      ],
      "enquires": ["棧道", "松風", "前路"]
    },
    {
      "vnum": 16304,
      "name": "風碑岔台",
      "description": "岔台上立著被山風吹得發白的舊碑，碑面上的指向雖然模糊，卻仍看得出一條往會稽、一條繞入更深山腹的分流。這裡不像真正的關口，卻是每個人都得先做選擇的地方。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "wind-fork",
      "coord": [0, -2, 0],
      "labels": ["fork", "marker"],
      "exits": [
        { "direction": "north", "to": 16303 },
        { "direction": "south", "to": 16310 },
        { "direction": "east", "to": 16306 },
        { "direction": "west", "to": 16307 }
      ],
      "enquires": ["風碑", "岔路", "會稽"]
    },
    {
      "vnum": 16305,
      "name": "山腰茶棚",
      "description": "茶棚靠著山腰平出的一小塊地搭起來，遠不如城郊茶亭寬鬆，卻正好有一種只夠旅人喘口氣、聽一兩句路況的分寸。真正走山的人多半不求舒服，只求知道接下來哪一段最難走。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-shelf",
      "coord": [1, -1, 0],
      "labels": ["rest", "tea-shed"],
      "exits": [
        { "direction": "west", "to": 16303 },
        { "direction": "south", "to": 16306 }
      ],
      "enquires": ["茶棚", "歇腳", "路況"]
    },
    {
      "vnum": 16306,
      "name": "祠痕裂階",
      "description": "裂開的石階往山腹陰處斜斜沉下去，兩側還留著模糊可辨的香灰痕與殘祠構件。它不像現在就會把人吞進去，卻很明白地暗示這條山道底下還藏著更古老也更不穩定的東西。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-shelf",
      "coord": [1, -2, 0],
      "labels": ["down-link", "ruin-trace"],
      "exits": [
        { "direction": "north", "to": 16305 },
        { "direction": "west", "to": 16304 }
      ],
      "enquires": ["古祠", "裂階", "山腹"]
    },
    {
      "vnum": 16307,
      "name": "崖邊小徑",
      "description": "小徑沿著崖邊收得很窄，明明不算深谷，卻已足夠讓人下意識把腳步壓穩。這條側徑不像主線那樣直白，卻更能讓人聽見山裡真正的風聲和水聲從哪裡穿出來。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "cliff-path",
      "coord": [-1, -2, 0],
      "labels": ["side-path", "cliff"],
      "exits": [
        { "direction": "east", "to": 16304 },
        { "direction": "south", "to": 16308 }
      ],
      "enquires": ["小徑", "崖邊"]
    },
    {
      "vnum": 16308,
      "name": "雲縫觀路",
      "description": "站在這裡往回看，建業方向的平地已經被雲縫和山稜切得零碎，只剩依稀可辨的來路。前方的坡勢則更明顯地往南收攏，像整條山道正在把人一步步送向真正的山城地界。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "cliff-path",
      "coord": [-1, -3, 0],
      "labels": ["view", "southward"],
      "exits": [
        { "direction": "north", "to": 16307 },
        { "direction": "east", "to": 16310 }
      ],
      "enquires": ["雲縫", "來路", "南邊"]
    },
    {
      "vnum": 16310,
      "name": "南下山門",
      "description": "山門前的路勢忽然收束得很整齊，像亂石、棧路和風口到這裡都先被看不見的城鎮秩序接住了。再往南去，旅人要面對的便不再只是山，而是會稽本身的門戶與人聲。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "wind-fork",
      "coord": [0, -3, 0],
      "labels": ["south-link", "gate"],
      "exits": [
        { "direction": "north", "to": 16304 },
        { "direction": "west", "to": 16308 }
      ],
      "enquires": ["山門", "會稽", "進城"]
    }
  ]
}
```
