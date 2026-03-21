# 江東水域 (`wild_river_delta`)

## Area Intent

`wild_river_delta` 承接 `city_kuaiji` 的東市轉角，把玩家從山城裡累積的傳聞、補給與地脈壓力重新放回開闊的外水視野。這裡不是遠海，也不是純官道，而是由洲灘、蘆汊與分流渡灣組成的江東水路前帶，讓會稽鏈在地下古寺之後重新展開成可辨位、可轉場、也能預留更多支線的 wild 節點。

## Theme Positioning

- Theme: `探險遺跡`
- Subtheme: `江東水域 / 洲灘渡汊`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "wild_river_delta",
    "title": "江東水域",
    "design_notes": "第一版 spec-first 草案。先固定會稽東市外的木棧入口、分流渡灣、洲灘橫路與兩條預留 world link，讓會稽鏈在古寺 dungeon 之後重新打開成江東外水 wild。",
    "level_range": "100-100",
    "planned_vnum_range": "16601-16630",
    "reserved_room_block": "16601-16630",
    "theme": {
      "primary": "探險遺跡",
      "secondary": "江東水域 / 洲灘渡汊"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 16601,
        "target_area": "city_kuaiji",
        "label": "會稽東市"
      },
      {
        "direction": "east",
        "source_vnum": 16608,
        "target_area": "harbor_outpost",
        "label": "江汊外埠"
      },
      {
        "direction": "south",
        "source_vnum": 16610,
        "target_area": "islet_shrine",
        "label": "洲心古祠"
      }
    ],
    "clusters": [
      { "id": "entry-dock", "label": "離城木棧" },
      { "id": "delta-main", "label": "分流主汊" },
      { "id": "sandbank-path", "label": "洲灘小路" },
      { "id": "outer-branch", "label": "外汊預留" },
      { "id": "islet-ford", "label": "洲心渡口" }
    ]
  },
  "rooms": [
    {
      "vnum": 16601,
      "name": "出城木棧",
      "description": "離開會稽東市最後一排鋪面後，腳下的青石很快被潮濕木棧與縛樁纜索取代。城裡的人聲仍在身後，但眼前已是被水氣撐開的視野與更碎、更散的江汊路線，像整座山城到了這裡才真正把人放出去。",
      "sector_type": "SECT_FIELD",
      "cluster": "entry-dock",
      "coord": [0, 0, 0],
      "labels": ["west-link", "entry"],
      "exits": [
        { "direction": "west", "to": 16410, "external": true },
        { "direction": "east", "to": 16603 },
        { "direction": "south", "to": 16602 }
      ],
      "enquires": ["木棧", "會稽", "去路"]
    },
    {
      "vnum": 16602,
      "name": "蘆汊淺灘",
      "description": "蘆草把水面切成一道道不明顯的暗縫，鞋底踩下去時總會帶起一層細泥。這裡不像真正的深水，卻也不是能隨便快走的平地，只要一分心，就可能把自己帶進更低更濕的泥汊裡。",
      "sector_type": "SECT_FIELD",
      "cluster": "entry-dock",
      "coord": [0, 1, 0],
      "labels": ["shallows", "reed-bank"],
      "exits": [
        { "direction": "north", "to": 16601 }
      ],
      "enquires": ["蘆草", "淺灘"]
    },
    {
      "vnum": 16603,
      "name": "分流渡灣",
      "description": "幾股水路在這裡互相牽扯，既不寬闊到像主河，也不狹窄到能一眼看清走向。站在渡灣中段時，玩家能清楚感覺到這片水域真正的危險不是怪，而是你以為自己記得來路。",
      "sector_type": "SECT_FIELD",
      "cluster": "delta-main",
      "coord": [1, 0, 0],
      "labels": ["junction", "waterway"],
      "exits": [
        { "direction": "west", "to": 16601 },
        { "direction": "east", "to": 16604 },
        { "direction": "south", "to": 16605 }
      ],
      "enquires": ["分流", "渡灣", "外汊"]
    },
    {
      "vnum": 16604,
      "name": "舊樁灘岸",
      "description": "岸邊還留著一些半朽的舊樁，像曾有人打算在這裡長久停舟，最後卻只把痕跡留給潮水和藻苔。比起會稽城內那種穩定的人煙感，這裡更像許多計畫都曾來過、又都沒有真正留下。",
      "sector_type": "SECT_FIELD",
      "cluster": "delta-main",
      "coord": [2, 0, 0],
      "labels": ["old-piles", "shore"],
      "exits": [
        { "direction": "west", "to": 16603 },
        { "direction": "east", "to": 16608 },
        { "direction": "south", "to": 16606 }
      ],
      "enquires": ["舊樁", "灘岸", "外埠"]
    },
    {
      "vnum": 16605,
      "name": "沙嘴小路",
      "description": "一條被水和風慢慢推成的沙嘴小路勉強把兩片洲灘接在一起。路很窄，卻也因此讓人更能感覺自己不是走在平地，而是在幾條江汊互相妥協後留下的暫時空隙上。",
      "sector_type": "SECT_FIELD",
      "cluster": "sandbank-path",
      "coord": [1, 1, 0],
      "labels": ["sandbar", "path"],
      "exits": [
        { "direction": "north", "to": 16603 },
        { "direction": "east", "to": 16606 }
      ],
      "enquires": ["沙嘴", "小路"]
    },
    {
      "vnum": 16606,
      "name": "漁火淺洲",
      "description": "洲上殘著幾點不知是昨夜還是更早留下的漁火灰痕，四周卻安靜得像這裡從來沒有真正熱鬧過。這份半有人氣、半被潮汐吞沒的感覺，正是江東外水最容易讓人記錯安全感的地方。",
      "sector_type": "SECT_FIELD",
      "cluster": "sandbank-path",
      "coord": [2, 1, 0],
      "labels": ["islet", "fishing-fire"],
      "exits": [
        { "direction": "west", "to": 16605 },
        { "direction": "north", "to": 16604 },
        { "direction": "south", "to": 16610 }
      ],
      "enquires": ["漁火", "淺洲", "渡口"]
    },
    {
      "vnum": 16608,
      "name": "更東外汊",
      "description": "水面到這裡明顯更開，連風向都像比前頭多了一層鹹濕與空曠。若再往東，便不只是會稽外圍的水路，而是更靠近外埠與陌生航道的地方，許多還沒落地的支線都像正從那頭招手。",
      "sector_type": "SECT_FIELD",
      "cluster": "outer-branch",
      "coord": [3, 0, 0],
      "labels": ["east-link", "outer-branch"],
      "exits": [
        { "direction": "west", "to": 16604 }
      ],
      "enquires": ["外汊", "外埠", "航道"]
    },
    {
      "vnum": 16610,
      "name": "洲心渡口",
      "description": "這座渡口不大，卻比前面的洲灘更有一種『若真要往別處去，就得在這裡決定』的意味。往南的水道被草影和低霧慢慢收細，像把一條更私密、更古老的支線藏在看似平常的洲心之後。",
      "sector_type": "SECT_FIELD",
      "cluster": "islet-ford",
      "coord": [2, 2, 0],
      "labels": ["south-link", "ford"],
      "exits": [
        { "direction": "north", "to": 16606 }
      ],
      "enquires": ["渡口", "洲心", "古祠"]
    }
  ]
}
```
