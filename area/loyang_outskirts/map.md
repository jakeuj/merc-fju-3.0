# 洛陽東郊 (`loyang_outskirts`)

## Area Intent

`loyang_outskirts` 是 `loyang` 的第一圈城郊延伸，用來承接玩家離開洛陽主城後的第一段野外節奏。

第一版目標不是一次做滿 NPC / reset / shop，而是先把下面三件事固定下來：

- 從 `東陽門` 出城後的主幹道骨架
- 從官道分出去的龍渠農田與丘陵支線
- 一個明確可讀、可問路、可往下延伸的地下水區入口

這一版刻意維持「城郊秩序仍在，但危險感已經開始滲入」的語氣。玩家應該會感受到：

- 西側仍看得見城門與護城河，回城很近
- 東側開始進入巡邏稀薄、地形起伏變大的丘陵帶
- 南側水渠與農舍提供補給、傳聞與地下入口的過渡感

## Theme Positioning

- Theme: `歷史城市風`
- Subtheme: `軍旅風`
- LevelRange: `1-20`
- Parent area: `loyang`
- Gap filled in world layer: 主城外郊、巡檢線、田野與地下入口的過渡帶

## Player Flow

1. 玩家從洛陽東陽門出城後，先看見橋頭、石橋與官道秩序。
2. 官道中段透過路亭與告示牌提供 `#Enquire` 導流，讓玩家知道可以回城、前往丘陵，或尋找地下入口。
3. 主路繼續往東走會到龍渠丘陵口，形成之後銜接下一個野外 AREA 的邊界。
4. 由水渠農田支線往南走，會抵達被石板掩住的暗井，再以 `down/up` 形成第一條非平面連線。

## Cluster Notes

### `city-edge`

- 房間重點：城門外橋頭、護城河石橋
- 玩家感受：秩序、守備、回城安全感
- 對外角色：承接 `loyang` 的東陽門邊界

### `east-road`

- 房間重點：路亭、告示牌、東郊官道
- 玩家感受：巡檢壓力、旅人往來、主路清楚
- 對外角色：作為前往龍渠丘陵的主幹線

### `canal-fields`

- 房間重點：龍渠分水口、田埂岔口、渠畔農舍
- 玩家感受：農田近郊、民生痕跡、水路暗示
- 對外角色：補給與傳聞支線，並導向地下入口

### `dragon-channel-hills`

- 房間重點：龍渠丘陵口、丘陵巡路
- 玩家感受：從城郊秩序過渡到較危險的地帶
- 對外角色：作為後續 `wild_longqu_hills` / `龍渠丘陵` 的邊界 stub

### `underground-entry`

- 房間重點：覆板暗井、井下檢修道
- 玩家感受：潮濕、封閉、可疑、像是正式地下區之前的前哨
- 對外角色：作為 `洛陽地下水區` 的入口 stub

## Planned World Links

這些是世界層連接意圖；其中西側回洛陽已在 spec 內落成正式邊界出口，其餘兩條仍先保留為 world-link 規劃：

- `west` from `7501`: planned link to `loyang` room `556` (`東陽門`)
- `east` from `7510`: planned link to `龍渠丘陵`
- `down` beyond `7512`: planned continuation to `洛陽地下水區`

## Runtime Metadata Notes

- `#Enquire` 第一版會落在橋頭、路亭、告示牌與暗井，讓玩家能問 `洛陽 / 回城 / 官道 / 巡哨 / 地下水區`
- `#Keyword` 第一版會落在城門、告示牌、水渠、石板、井梯，讓文字提示直接對應探索意圖
- `#Job` 第一版暫不新增。若之後要把暗井石板改成必須 `lift slab`、`pull ring` 或其他特殊互動，再補對應 job 與程式端實作

## Suggested Layout

```text
洛陽東陽門(556)
   |
[7501] 東陽門外橋頭 -- [7502] 護城河石橋 -- [7503] 東郊路亭 -- [7504] 巡檢告示牌 -- [7505] 東郊官道 -- [7509] 龍渠丘陵口 -- [7510] 丘陵巡路
                                  |                              |
                                [7506] 龍渠分水口 -- [7507] 田埂岔口 -- [7508] 渠畔農舍
                                                          |
                                                        [7511] 覆板暗井
                                                          |
                                                        down
                                                          |
                                                        [7512] 井下檢修道
```

## mapmd-json

```mapmd-json
{
  "area": {
    "name": "loyang_outskirts",
    "title": "洛陽東郊",
    "design_notes": "第一版 spec-first 草案。先固定東陽門外的主幹道、龍渠農田支線與地下入口 stub，再往後拆成 includes 或生成 .roo scaffold。",
    "parent_area": "loyang",
    "level_range": "1-20",
    "planned_vnum_range": "7501-7512",
    "reserved_room_block": "7501-7520",
    "theme": {
      "primary": "歷史城市風",
      "secondary": "軍旅風"
    },
    "world_links": [
      {
        "direction": "west",
        "source_vnum": 7501,
        "target_area": "loyang",
        "target_room_vnum": 556,
        "label": "東陽門"
      },
      {
        "direction": "east",
        "source_vnum": 7510,
        "target_area": "wild_longqu_hills",
        "target_room_vnum": 9401,
        "label": "龍渠丘陵"
      },
      {
        "direction": "down",
        "source_vnum": 7512,
        "target_area": "dng_loyang_sewer",
        "target_room_vnum": 9451,
        "label": "洛陽地下水區"
      }
    ],
    "clusters": [
      {
        "id": "city-edge",
        "label": "城門外緩衝帶"
      },
      {
        "id": "east-road",
        "label": "東郊主官道"
      },
      {
        "id": "canal-fields",
        "label": "龍渠與農田支線"
      },
      {
        "id": "dragon-channel-hills",
        "label": "龍渠丘陵前帶"
      },
      {
        "id": "underground-entry",
        "label": "地下水區入口"
      }
    ]
  },
  "rooms": [
    {
      "vnum": 7501,
      "name": "東陽門外橋頭",
      "description": "高聳的東陽門就在西邊，城牆與角樓把晨光切成整齊的陰影。橋頭鋪著寬大的石板，來往行人都要在此略停，接受守卒盤問後才能沿著官道東行。護城河水自北往南緩慢流過，讓人一離城便感到洛陽的秩序仍緊貼在背後；不少第一次出城的人都會先在這裡回頭認清城門，再放心往東去試東郊的路。",
      "sector_type": "SECT_CITY",
      "cluster": "city-edge",
      "coord": [0, 0, 0],
      "labels": ["entry", "return-gate", "world-link-west"],
      "exits": [
        {
          "direction": "west",
          "to": 556,
          "external": true
        },
        {
          "direction": "east",
          "to": 7502
        }
      ],
      "keywords": [
        {
          "keyword": "城門",
          "description": "東陽門的門洞深而寬闊，門上鐵葉與銅釘在日光下泛著冷光。只要再往西折返一段路，就能重新回到洛陽城內。"
        }
      ],
      "enquires": ["洛陽", "東郊", "出城"]
    },
    {
      "vnum": 7502,
      "name": "護城河石橋",
      "description": "石橋跨在護城河上，橋面雖寬，卻因巡卒與商旅往來顯得有些逼仄。西邊是洛陽城威嚴的東門，東邊的道路則慢慢展開，兩側開始出現田埂與引水溝渠，提醒你已經離開純粹的城區。",
      "sector_type": "SECT_CITY",
      "cluster": "city-edge",
      "coord": [1, 0, 0],
      "labels": ["bridge", "transition"],
      "exits": [
        {
          "direction": "west",
          "to": 7501
        },
        {
          "direction": "east",
          "to": 7503
        },
        {
          "direction": "south",
          "to": 7506
        }
      ]
    },
    {
      "vnum": 7503,
      "name": "東郊路亭",
      "description": "一座半開放的木亭立在路邊，亭柱上仍留著官府重新補漆的痕跡。挑擔的行腳人會在這裡稍歇，巡檢也常借亭角避日。西邊橋頭還清楚可見，往東則是筆直延伸的官道，像把人慢慢送離主城的喧嘩；真要拿東郊當第一段近路來走的人，多半也會先在亭下把去處問明白。",
      "sector_type": "SECT_CITY",
      "cluster": "east-road",
      "coord": [2, 0, 0],
      "labels": ["service", "enquire"],
      "exits": [
        {
          "direction": "west",
          "to": 7502
        },
        {
          "direction": "east",
          "to": 7504
        }
      ],
      "keywords": [
        {
          "keyword": "路亭",
          "description": "亭下擺著簡陋長凳與一只舊茶缸，木柱上有人用小刀刻下了去往丘陵與農舍的方向記號。"
        }
      ],
      "enquires": ["官道", "路亭", "歇腳"]
    },
    {
      "vnum": 7504,
      "name": "巡檢告示牌",
      "description": "官道邊豎著一面厚木告示牌，上頭釘著新舊不一的紙張，內容有巡邏更次、盤查令與最近郊外盜匪的傳聞。牌下常有旅人停步觀看，也有人趁機打聽前方路況；懂門道的人甚至會先在這裡問清楚暗井與地下水區的傳聞，再決定要不要往南試探。",
      "sector_type": "SECT_CITY",
      "cluster": "east-road",
      "coord": [3, 0, 0],
      "labels": ["service", "enquire", "military-pressure"],
      "exits": [
        {
          "direction": "west",
          "to": 7503
        },
        {
          "direction": "east",
          "to": 7505
        },
        {
          "direction": "south",
          "to": 7507
        }
      ],
      "keywords": [
        {
          "keyword": "告示牌",
          "description": "最新一張告示提醒行人入夜後勿獨行丘陵，若要尋找地下水道入口，最好先問清楚白天巡檢留下的方向。"
        }
      ],
      "enquires": ["巡哨", "巡檢", "告示"]
    },
    {
      "vnum": 7505,
      "name": "東郊官道",
      "description": "官道在此稍微抬高，土色也從城外的灰白轉為帶黃的硬地。道路兩旁的草已比橋頭處更高，偶有馬蹄與車輪壓出的深痕。西邊仍有巡兵足跡，東邊卻逐漸只剩地勢起伏與風聲，預告著丘陵地帶的開始。",
      "sector_type": "SECT_FIELD",
      "cluster": "east-road",
      "coord": [4, 0, 0],
      "labels": ["main-road"],
      "exits": [
        {
          "direction": "west",
          "to": 7504
        },
        {
          "direction": "east",
          "to": 7509
        }
      ]
    },
    {
      "vnum": 7506,
      "name": "龍渠分水口",
      "description": "一道人工水渠自護城河旁引出，在這裡分成較窄的水路，沿著田地邊界蜿蜒而去。水聲壓低了官道上的交談，偶爾還能看見農人挑著木桶來此取水。這裡雖還算安全，卻已多了一點遠離城門視線的鬆動感。",
      "sector_type": "SECT_FIELD",
      "cluster": "canal-fields",
      "coord": [1, -1, 0],
      "labels": ["waterway", "branch"],
      "exits": [
        {
          "direction": "north",
          "to": 7502
        },
        {
          "direction": "east",
          "to": 7507
        }
      ],
      "keywords": [
        {
          "keyword": "水渠",
          "description": "渠水清中帶著泥味，兩側木樁與石塊勉強維持著水路邊界，看得出這條分水口平時也兼作附近農田的命脈。"
        }
      ]
    },
    {
      "vnum": 7507,
      "name": "田埂岔口",
      "description": "狹長的田埂在此分成兩條，一條往東去農舍，一條往南順著被雜草遮住的岔路沒入暗處。岔口木樁上掛著巡檢夜裡留下的風燈，昏黃光圈剛好照住那條貼地延伸的\u001b[1;32m草痕\u001b[0m與一叢過分潮濕的枯草，像是故意把某條不該太醒目的路留給看得懂的人。若想弄清南邊那條隱路通往哪裡，不妨先留意草痕與枯草。回頭往北仍能看到官道邊的告示牌，讓這處岔口帶著一種介於民生與隱患之間的微妙氣氛；若不是熟門熟路的人，往南那條草痕很容易被當成普通田埂漏看過去。",
      "sector_type": "SECT_CITY",
      "cluster": "canal-fields",
      "coord": [3, -1, 0],
      "labels": ["branch", "decision-point"],
      "exits": [
        {
          "direction": "north",
          "to": 7504
        },
        {
          "direction": "west",
          "to": 7506
        },
        {
          "direction": "east",
          "to": 7508
        },
        {
          "direction": "south",
          "to": 7511,
          "exit_desc": "南邊那叢過分潮濕的枯草斜壓在窄道口，後頭像還藏著能再往裡摸去的空隙。若想看清楚這條隱路，得先把枯草撥開。",
          "exit_keyword": "枯草",
          "flags": ["IsDoor", "Closed"]
        }
      ],
      "keywords": [
        {
          "keyword": "草痕",
          "description": "一條被反覆踩伏的草痕貼著田埂往南延去，不像農人日常走出的短路，反而像有人刻意留著通往某處隱蔽入口的暗路。若順著這道草痕再往南摸去，多半就能靠近草後藏著的東西。"
        },
        {
          "keyword": "枯草",
          "description": "南邊那叢枯草表面沾著不合時節的潮氣，底下像還壓著更冷硬的東西。草根被人反覆撥開又合攏，像是專門拿來遮住後頭那條窄道；若想看清草後到底藏了什麼，不妨試著把枯草打開(open)。"
        }
      ],
      "enquires": ["農舍", "田埂", "岔口"]
    },
    {
      "vnum": 7508,
      "name": "渠畔農舍",
      "description": "一間低矮農舍靠著水渠而建，屋前晾著幾束尚未捆好的稻草與兩只木桶。雖說離洛陽不算遠，屋主人仍把門窗補得很結實，像是提防夜裡從丘陵或水道摸來的不速之客。",
      "sector_type": "SECT_FIELD",
      "cluster": "canal-fields",
      "coord": [4, -1, 0],
      "labels": ["rest-stop", "rumor-node"],
      "exits": [
        {
          "direction": "west",
          "to": 7507
        }
      ],
      "keywords": [
        {
          "keyword": "農舍",
          "description": "木門上新補過的橫木很顯眼，門旁還掛著一盞能照到田埂邊緣的舊燈，像是主人不願讓夜色完全吞沒周圍。"
        }
      ]
    },
    {
      "vnum": 7509,
      "name": "龍渠丘陵口",
      "description": "官道在這裡開始沿著低丘邊緣蜿蜒，地勢明顯高低不平，視野也被土坡與灌木切碎。回望西邊仍能辨出洛陽方向的煙塵與車馬，但往東的風聲更硬，像在催促旅人正式離開城郊的庇蔭。",
      "sector_type": "SECT_HILLS",
      "cluster": "dragon-channel-hills",
      "coord": [5, 0, 0],
      "labels": ["boundary-east", "world-link-east"],
      "exits": [
        {
          "direction": "west",
          "to": 7505
        },
        {
          "direction": "east",
          "to": 7510
        }
      ],
      "enquires": ["丘陵", "東路"]
    },
    {
      "vnum": 7510,
      "name": "丘陵巡路",
      "description": "巡路沿著丘腰向東延伸，兩側的土坡已足以遮住洛陽城影，只剩偶爾能看見的旗影與道路標石證明這裡仍屬官道系統。再往前便是更長的龍渠丘陵路段，巡卒的身影也變得稀疏許多。",
      "sector_type": "SECT_HILLS",
      "cluster": "dragon-channel-hills",
      "coord": [6, 0, 0],
      "labels": ["world-boundary", "planned-link-longqu"],
      "exits": [
        {
          "direction": "west",
          "to": 7509
        },
        {
          "direction": "east",
          "to": 9401,
          "external": true
        }
      ]
    },
    {
      "vnum": 7511,
      "name": "覆板暗井",
      "description": "枯草後方藏著一口被厚石板半掩的暗井，井沿長滿濕滑青苔，空氣裡有一股明顯的潮味。石板旁留著幾道近期搬動過的刮痕，像是有人仍在利用這條井路往來；透過石板邊緣那道狹窄縫隙往下望去，黯淡井壁邊還能隱約辨出一段鐵梯。若想真正打開往下的路，不妨先看看石板。",
      "sector_type": "SECT_INSIDE",
      "cluster": "underground-entry",
      "coord": [3, -2, 0],
      "labels": ["special-entry", "vertical-link"],
      "exits": [
        {
          "direction": "north",
          "to": 7507
        },
        {
          "direction": "down",
          "to": 7512,
          "exit_desc": "厚重石板斜壓在井口上，只留一道透氣縫，縫下隱約可見鐵梯影子。若想往下，得先設法把石板打開。",
          "exit_keyword": "石板",
          "flags": ["IsDoor", "Closed"]
        }
      ],
      "keywords": [
        {
          "keyword": "暗井",
          "description": "這口暗井藏在枯草與石板後頭，不走近幾乎看不真切。井口沒有完全封死，像是故意留給熟門熟路的人上下；若真想沿著這條路下去，關鍵多半就在壓住井口的石板。"
        },
        {
          "keyword": "石板",
          "description": "石板邊角磨損得不自然，若仔細看，還能發現泥土上有被人反覆拖移的痕跡。這塊石板看起來並不是封死用的，更像是暫時掩住井口；若想把往下的井路露出來，不妨試著打開(open)石板。"
        },
        {
          "keyword": "井梯",
          "description": "井壁內側釘著一段向下延伸的鐵梯，表面滿是潮氣與鏽色，但還勉強能承重。只要石板讓出空間，順著井梯往下就能進入井底檢修道。"
        }
      ],
      "enquires": ["地下水區", "暗井", "井口"]
    },
    {
      "vnum": 7512,
      "name": "井下檢修道",
      "description": "井底連著一小段狹窄檢修道，腳下石面長年受潮，踩上去會發出低悶的回音。水氣從更深處持續湧來，夾著陳舊淤泥與腐木味，讓人明白這裡只是地下水區真正入口前的一段前哨。抬頭仍能透過井口見到些微天光。",
      "sector_type": "SECT_INSIDE",
      "cluster": "underground-entry",
      "coord": [3, -2, -1],
      "labels": ["underground-foyer", "world-link-down"],
      "exits": [
        {
          "direction": "up",
          "to": 7511
        },
        {
          "direction": "down",
          "to": 9451,
          "external": true
        }
      ],
      "keywords": [
        {
          "keyword": "井口",
          "description": "抬頭能看到一圈灰白天光掛在井壁上方，偶爾還會有遠遠的腳步聲自井沿傳下來，提醒你回到地面的路仍在上頭。"
        },
        {
          "keyword": "水門",
          "description": "檢修道更深處有一扇生鏽水門半掩在黑暗中，門縫後不時傳來水流拍擊石壁的聲音，像是在提醒你真正的地下水路還在前方。"
        }
      ],
      "enquires": ["出口", "上去", "井底"]
    }
  ]
}
```
