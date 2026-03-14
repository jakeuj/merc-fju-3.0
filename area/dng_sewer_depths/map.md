# 地下深渠 (`dng_sewer_depths`)

## Area Intent

`dng_sewer_depths` 承接 `dng_loyang_sewer` 深井鐵梯下方的真正深層水道，讓玩家從「仍保有退路與人為檢修痕跡」的地下前帶，進一步下探到更接近封印核心、黑水積流與廢棄機關殘骸交錯的危險區。

第一版目標先固定：

- 一條由鐵梯落點往深處延伸的主深渠
- 一條偏向維修側室與遺失祭具的支線
- 一條 `down/up` 的更深封印槽非平面連線
- 以 `#Enquire` / `#Keyword` 暗示退路、黑水、機關與封印殘痕

## Theme Positioning

- Theme: `詭異民俗風`
- Subtheme: `深層水道`
- LevelRange: `15-25`
- Parent area: `dng_loyang_sewer`
- World gap filled: 把洛陽地下水區的深井 stub 擴張成真正可探索的深層水道，讓地下鏈從入口前哨自然延伸到更危險的封印段落

## Player Flow

1. 玩家從 `dng_loyang_sewer/9460` 向下進入本區時，先感受到濕冷鐵鏽味轉成更厚重的黑水腐氣。
2. 主線沿著深渠甬道與閘門廊道向內推進，逐步強化壓迫感、失衡的機關感與退路焦慮。
3. 側室支線提供遺物、祭具與殘留人為操作痕跡，讓深層區不只剩單向戰鬥。
4. 最深處的封印深槽以 `down/up` 預留更深墓井或古代遺構，保留地下鏈下一段延伸空間。

## Cluster Notes

### `shaft-foot`

- 房間重點：鐵梯底座、深渠入口
- 玩家感受：剛離開上層，退路仍可辨識，但壓迫感已明顯加重
- 對外角色：承接 `dng_loyang_sewer/9460`

### `blackwater-main`

- 房間重點：黑水甬道、淤泥閘門、回聲橋段
- 玩家感受：黑暗加深、水聲混亂、路線更不易判斷
- 對外角色：作為 deeper sewer 主探索線

### `service-relic`

- 房間重點：維修偏室、漂木堆、遺失祭具間
- 玩家感受：雜亂、潮濕、像有人想補修卻中途棄置
- 對外角色：提供線索、遺物與人為痕跡

### `sealed-basin`

- 房間重點：鎖閘前廊、封印深槽、下沉井口
- 玩家感受：詭異、危險、像是深處還有真正被鎮住的東西
- 對外角色：作為未來更深封印墓井 / 地底遺構入口 stub

## Planned World Links

- `up` from `9461`: planned link to `dng_loyang_sewer` room `9460`
- `down` from `9470`: planned continuation to `更深封印墓井 / 地底遺構`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在鐵梯底座、淤泥閘門、鎖閘前廊與封印深槽，讓玩家能問 `退路 / 深處 / 黑水 / 封印`
- `#Keyword` 第一版會落在鐵梯、水痕、木樁、祭具、鎖閘，讓地下探索提示直接落在 room prose
- `#Job` 第一版暫不新增；先以 room prose 與出口設計承擔互動引導

## Suggested Layout

```text
洛陽地下水區深井鐵梯(9460)
   |
[9461] 鐵梯底座 -- [9462] 黑水甬道 -- [9463] 淤泥閘門 -- [9464] 回聲深渠 -- [9467] 鎖閘前廊
                                      |                                  |
                                   [9465] 維修偏室 -- [9466] 漂木堆渠間 -- [9469] 遺失祭具間
                                                                         |
                                                                      [9467] 鎖閘前廊 -- [9468] 封印深槽
                                                                                           |
                                                                                        [9470] 下沉井口

[9470] down -> future deeper sealed depths
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_sewer_depths",
    "title": "地下深渠",
    "design_notes": "第一版 spec-first 草案。先固定深井鐵梯以下的黑水主渠、維修支線與封印深槽非平面入口。",
    "parent_area": "dng_loyang_sewer",
    "level_range": "15-25",
    "planned_vnum_range": "9461-9470",
    "theme": {
      "primary": "詭異民俗風",
      "secondary": "深層水道"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 9461,
        "target_area": "dng_loyang_sewer",
        "target_room_vnum": 9460,
        "label": "深井鐵梯"
      },
      {
        "direction": "down",
        "source_vnum": 9470,
        "target_area": "dng_royal_tomb_depths",
        "label": "更深封印墓井"
      }
    ],
    "clusters": [
      { "id": "shaft-foot", "label": "深井底座前帶" },
      { "id": "blackwater-main", "label": "黑水主渠" },
      { "id": "service-relic", "label": "維修與遺物支線" },
      { "id": "sealed-basin", "label": "鎖閘與封印深槽" }
    ]
  },
  "rooms": [
    {
      "vnum": 9461,
      "name": "鐵梯底座",
      "description": "鐵梯在這裡沒入一片帶著黑色油光的淺水，井壁上的鏽痕像被無數雙手反覆抓過。抬頭還能勉強望見上層那一絲較亮的灰光，往前則只剩濃重潮氣與深處傳來的低沉拍水聲。",
      "sector_type": "SECT_INSIDE",
      "cluster": "shaft-foot",
      "coord": [0, 0, -3],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 9460, "external": true },
        { "direction": "east", "to": 9462 }
      ],
      "enquires": ["退路", "鐵梯"]
    },
    {
      "vnum": 9462,
      "name": "黑水甬道",
      "description": "甬道地面覆著一層不知深淺的黑水，踩下去時總會晚半拍才傳回濺水聲。牆面殘留的刻線像是舊時維修記號，但多數早被潮氣與污泥蓋過。",
      "sector_type": "SECT_INSIDE",
      "cluster": "blackwater-main",
      "coord": [1, 0, -3],
      "labels": ["channel", "transition"],
      "exits": [
        { "direction": "west", "to": 9461 },
        { "direction": "east", "to": 9463 }
      ],
      "keywords": [
        {
          "keyword": "水痕",
          "description": "牆上的水痕高低交錯，顯示這條深渠有時只是積水，有時卻會被整股黑水灌滿。"
        }
      ]
    },
    {
      "vnum": 9463,
      "name": "淤泥閘門",
      "description": "一道厚重石閘半陷在淤泥裡，閘槽兩側還看得出粗糙機關滑軌。它像曾用來控制深渠水勢，如今卻只剩卡死的木樁和被泥水吞沒的轉柄。",
      "sector_type": "SECT_INSIDE",
      "cluster": "blackwater-main",
      "coord": [2, 0, -3],
      "labels": ["gate", "junction"],
      "exits": [
        { "direction": "west", "to": 9462 },
        { "direction": "east", "to": 9464 },
        { "direction": "south", "to": 9465 }
      ],
      "keywords": [
        {
          "keyword": "木樁",
          "description": "木樁被水泡得發黑開裂，像是有人曾急著用它臨時卡住閘門，卻再也沒有回來處理。"
        }
      ],
      "enquires": ["黑水", "閘門"]
    },
    {
      "vnum": 9464,
      "name": "回聲深渠",
      "description": "深渠在這裡略為抬高，兩側石壁把每一滴水聲都放大成不安的迴響。再往前看，隱約能看見一片像鎖閘又像祭門的黑影橫在通道盡頭。",
      "sector_type": "SECT_INSIDE",
      "cluster": "blackwater-main",
      "coord": [3, 0, -3],
      "labels": ["deep-main", "echo"],
      "exits": [
        { "direction": "west", "to": 9463 },
        { "direction": "east", "to": 9467 }
      ],
      "enquires": ["深處", "回音"]
    },
    {
      "vnum": 9465,
      "name": "維修偏室",
      "description": "偏室裡倒著幾架腐朽木梯與拆散的滑輪，牆角還留著半箱沒來得及搬走的鐵件。這裡像曾有人試圖修復深渠設施，但工作只做到一半便突然中止。",
      "sector_type": "SECT_INSIDE",
      "cluster": "service-relic",
      "coord": [2, -1, -3],
      "labels": ["side-room", "maintenance"],
      "exits": [
        { "direction": "north", "to": 9463 },
        { "direction": "east", "to": 9466 }
      ],
      "keywords": [
        {
          "keyword": "鐵件",
          "description": "鐵件邊角帶著符刻與卡榫痕，顯示這些機關原本就不只是普通水利設施。"
        }
      ]
    },
    {
      "vnum": 9466,
      "name": "漂木堆渠間",
      "description": "一堆被黑水推來的漂木與爛布在這裡卡成半堵矮牆，木料底下不時冒出細碎氣泡。若仔細翻看，還能發現幾件不該出現在深層水道裡的祭繩與銅片。",
      "sector_type": "SECT_INSIDE",
      "cluster": "service-relic",
      "coord": [3, -1, -3],
      "labels": ["debris", "search"],
      "exits": [
        { "direction": "west", "to": 9465 },
        { "direction": "east", "to": 9469 }
      ],
      "keywords": [
        {
          "keyword": "漂木",
          "description": "漂木間夾著幾段帶符墨痕跡的麻繩，像是某種封印儀式殘留下來的耗材。"
        }
      ]
    },
    {
      "vnum": 9467,
      "name": "鎖閘前廊",
      "description": "前廊地面嵌著數道導水槽，槽邊則刻著早被磨鈍的鎮壓紋路。站在這裡時，深處傳來的水聲反而變小，像有什麼東西把更下方的空間整個吞住了。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-basin",
      "coord": [4, 0, -3],
      "labels": ["sealed", "threshold"],
      "exits": [
        { "direction": "west", "to": 9464 },
        { "direction": "south", "to": 9469 },
        { "direction": "east", "to": 9468 }
      ],
      "enquires": ["封印", "前廊", "退路"]
    },
    {
      "vnum": 9468,
      "name": "封印深槽",
      "description": "石槽中央陷成一圈更黑、更深的井口，邊緣圍著半殘銅鎖與斷裂石柱。井口下方沒有任何可見光影，只有一股帶著寒意的濕風緩慢往上冒，像深處仍有什麼被壓在更底下。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-basin",
      "coord": [5, 0, -3],
      "labels": ["deep-pit", "world-link-down"],
      "exits": [
        { "direction": "west", "to": 9467 },
        { "direction": "down", "to": 9470 }
      ],
      "keywords": [
        {
          "keyword": "銅鎖",
          "description": "銅鎖表面滿是舊符和裂紋，既像鎖具，也像某種專門用來鎮壓井底異物的法器。"
        }
      ],
      "enquires": ["深處", "井口"]
    },
    {
      "vnum": 9469,
      "name": "遺失祭具間",
      "description": "角落堆著裂開的陶盞、沉重銅片與被水泡鬆的木匣，像曾有人把祭具與維修器具一併拖進這裡暫放。室內瀰漫著一股混雜鐵鏽、潮泥與香灰的古怪氣味。",
      "sector_type": "SECT_INSIDE",
      "cluster": "service-relic",
      "coord": [4, -1, -3],
      "labels": ["relic", "rumor"],
      "exits": [
        { "direction": "north", "to": 9467 },
        { "direction": "west", "to": 9466 }
      ],
      "keywords": [
        {
          "keyword": "祭具",
          "description": "祭具形制混雜得很奇怪，有些像廟宇器物，有些卻更像配合機關使用的零件。"
        }
      ],
      "enquires": ["祭具", "來路"]
    },
    {
      "vnum": 9470,
      "name": "下沉井口",
      "description": "封印深槽底部還藏著一道向下開裂的沉井口，井緣佈滿被黑水磨亮的石面與殘破鎖扣。從這裡往下只看得見一整片吞光的濕黑，像是更深處仍有一層真正被刻意隔開的地底構造。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-basin",
      "coord": [5, 0, -4],
      "labels": ["vertical", "future-depth"],
      "exits": [
        { "direction": "up", "to": 9468 }
      ],
      "enquires": ["井口", "下方"]
    }
  ]
}
```
