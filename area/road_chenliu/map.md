# 往陳留驛路 (`road_chenliu`)

## Area Intent

`road_chenliu` 承接 `wild_chenliu_west` 的 `更西荒道`，把原本還只是「往更西去」的灰色外帶，正式收束成有車轍、木堠、驛棚、盤查土坡與歇腳點的西行驛路。這裡不是直接把玩家瞬間送回洛陽，也不是再做一段跟茶亭田埂差不多的近郊 wild，而是一條會讓人明顯感到「陳留的城影已退遠，真正的中原長路節奏開始接手」的 road 節點。

## Theme Positioning

- Theme: `歷史城市`
- Subtheme: `西行驛道 / 中原長路`
- LevelRange: `15-25`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "road_chenliu",
    "title": "往陳留驛路",
    "design_notes": "第一版 spec-first 草案。先固定 wild_chenliu_west 更西荒道之後的正式驛路入口、車轍主線、木堠岔點、棚亭歇腳點與盤查土坡，讓陳留西向交通層正式切進可載入 road 骨架。",
    "level_range": "15-25",
    "planned_vnum_range": "20901-20920",
    "reserved_room_block": "20901-20920",
    "theme": {
      "primary": "歷史城市",
      "secondary": "西行驛道 / 中原長路"
    },
    "world_links": [
      {
        "direction": "east",
        "source_vnum": 20901,
        "target_area": "wild_chenliu_west",
        "target_room_vnum": 20808,
        "label": "更西荒道"
      }
    ],
    "clusters": [
      { "id": "east-approach", "label": "陳留西緣接道口" },
      { "id": "main-road", "label": "車轍主線" },
      { "id": "rest-stop", "label": "驛棚歇腳點" },
      { "id": "checkpoint", "label": "盤查與木堠帶" },
      { "id": "west-edge", "label": "更西驛路前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 20901,
      "name": "更西驛路口",
      "description": "從陳留西郊的荒道再往前走，腳下的散土與灰痕慢慢被反覆碾實成更有方向感的驛路口。回頭還能辨出陳留方向殘留的牆影與棚煙，往西卻已經是一種真正交給車轍、木堠與旅隊節奏接手的長路開頭。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-approach",
      "coord": [0, 0, 0],
      "labels": ["entry", "east-edge", "road-start"],
      "exits": [
        { "direction": "east", "to": 20808, "external": true },
        { "direction": "west", "to": 20902 }
      ],
      "enquires": ["陳留", "驛路", "去向"]
    },
    {
      "vnum": 20902,
      "name": "車轍長段",
      "description": "這段路被車轍壓得很深，連泥色都被往返人馬磨出一種穩定的舊亮。它沒有城郊茶亭那種鬆散人情，取而代之的是一種誰都知道該往哪走、也知道哪些地方最好不要在天黑後停太久的長路秩序。",
      "sector_type": "SECT_FIELD",
      "cluster": "main-road",
      "coord": [-1, 0, 0],
      "labels": ["main-road", "wagon-ruts", "westbound"],
      "exits": [
        { "direction": "east", "to": 20901 },
        { "direction": "west", "to": 20903 },
        { "direction": "south", "to": 20904 }
      ],
      "enquires": ["車轍", "長路", "旅隊"]
    },
    {
      "vnum": 20903,
      "name": "驛牌木堠",
      "description": "路邊立著刻痕已深的木堠與驛牌，字跡雖被風吹雨打得不算完整，卻仍清楚提醒旅人東邊是陳留、往西才是真正更遠的去處。站在這裡時，你會第一次感到自己不再只是離城，而是已經被正式交給一條跨城長路。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "main-road",
      "coord": [-2, 0, 0],
      "labels": ["marker", "route-info", "midway"],
      "exits": [
        { "direction": "east", "to": 20902 },
        { "direction": "west", "to": 20905 }
      ],
      "keywords": [
        {
          "keyword": "驛牌",
          "description": "木牌上的刻字被風磨得有些毛邊，但還能辨出陳留方向與更西路段的提示，顯示這裡早就不是只憑口耳相傳辨路的灰帶。"
        }
      ],
      "enquires": ["驛牌", "陳留", "更西"]
    },
    {
      "vnum": 20904,
      "name": "驛棚前坪",
      "description": "幾張長凳、粗布棚腳與栓馬木柱把這塊前坪整理成驛路上最像樣的停手點。真正趕路的人會在這裡補水、換口糧，也會在天色轉暗前最後打聽前頭那一段路是不是又有差役加重盤問。",
      "sector_type": "SECT_FIELD",
      "cluster": "rest-stop",
      "coord": [-1, -1, 0],
      "labels": ["rest-stop", "service", "shelter"],
      "exits": [
        { "direction": "north", "to": 20902 },
        { "direction": "west", "to": 20907 },
        { "direction": "enter", "to": 20906 }
      ],
      "enquires": ["驛棚", "歇腳", "補給"]
    },
    {
      "vnum": 20905,
      "name": "西行岔堠",
      "description": "木堠旁的路面微微抬高，讓主路與旁邊較低的一段盤查坡清楚分出層次。往東仍是驛牌與陳留方向，往西則是更長、更安靜，也更需要靠自己判斷天色與路感的西行驛路。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "checkpoint",
      "coord": [-3, 0, 0],
      "labels": ["fork", "checkpoint-nearby", "westward"],
      "exits": [
        { "direction": "east", "to": 20903 },
        { "direction": "west", "to": 20908 },
        { "direction": "south", "to": 20907 }
      ],
      "enquires": ["木堠", "岔路", "盤查"]
    },
    {
      "vnum": 20906,
      "name": "驛棚內",
      "description": "棚內擺著粗茶桶、舊水囊與幾面已被擦得發亮的木碗，角落還掛著幾塊替旅人記方向的木牌。這裡談不上安穩，只能算是在真正重新上路前，勉強把人和行囊都整理回長路節奏的小縫口。",
      "sector_type": "SECT_INSIDE",
      "cluster": "rest-stop",
      "coord": [-1, -1, 1],
      "labels": ["inside", "rest", "nonplanar"],
      "exits": [
        { "direction": "out", "to": 20904 }
      ],
      "enquires": ["木牌", "茶水"]
    },
    {
      "vnum": 20907,
      "name": "盤查土坡",
      "description": "坡口地面被靴底、輪痕與牲口蹄印踩得結實，顯示差役與驛卒常在這裡攔人問話。比起城門那種公開的盤查，這裡更像旅路上的次一級節點，專門用來篩掉那些看起來不像單純趕路的人。",
      "sector_type": "SECT_FIELD",
      "cluster": "checkpoint",
      "coord": [-2, -1, 0],
      "labels": ["checkpoint", "slope", "rumor"],
      "exits": [
        { "direction": "north", "to": 20905 },
        { "direction": "east", "to": 20904 }
      ],
      "enquires": ["盤查", "差役", "夜路"]
    },
    {
      "vnum": 20908,
      "name": "更西驛道前帶",
      "description": "再往西去，陳留方向的痕跡已經只剩偶爾回頭時才能抓住的背景，真正支撐人不迷路的，只剩更寬的驛路本身、輪痕的深淺與風裡傳來的遠處棚燈味。它還沒有把你真正送進洛陽，但很清楚已經把人正式放上兩城之間該有的長路。 ",
      "sector_type": "SECT_FIELD",
      "cluster": "west-edge",
      "coord": [-4, 0, 0],
      "labels": ["west-edge", "future-loyang-contract", "departure"],
      "exits": [
        { "direction": "east", "to": 20905 }
      ],
      "enquires": ["更西", "洛陽", "遠路"]
    }
  ]
}
```
