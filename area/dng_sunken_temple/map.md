# 沉沒古廟 (`dng_sunken_temple`)

## Area Intent

`dng_sunken_temple` 承接 `wild_yunmeng` 深沼前帶之下的第一段真正濕地下探區，讓玩家從霧與泥的不確定，轉入一座被積水、石廊、殘紋與半沉祭室慢慢壓緊呼吸的古廟 dungeon。

第一版目標先固定：

- 一條由上而下穿過積水前庭、漏水廊道與封紋中殿的主探索線
- 一條向側翼分出的祭器偏室 / 碑廊支線
- 一條 `up/down` 連到封檻落井與更深封井的非平面下探線
- 以 `#Enquire` / `#Keyword` 暗示入口、石門、水痕、封印與退路

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `沉沒古廟 / 濕地下探`
- LevelRange: `58-68`
- Parent region: `雲夢深沼`
- World gap filled: 讓雲夢段正式進入下探遺跡 dungeon，並為更深封印沼域建立前帶

## Suggested Layout

```text
雲夢深沼前帶
   |
[14601] 裂口落階 -- [14602] 積水前庭 -- [14603] 漏水廊道 -- [14604] 封紋中殿 -- [14608] 封檻落井 -- [14612] 深封井口
                                             |                                      |
                                             |                                      +-- down -- future secret
                                             |
                                             +-- east -- [14605] 碑廊偏室 -- [14606] 祭器殘庫 -- [14607] 水蝕後堂

                                          [14609] 殘門石階 -- [14610] 鎖鏈祭室 -- [14611] 回水暗渠
```

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_sunken_temple",
    "title": "沉沒古廟",
    "design_notes": "第一版 spec-first 草案。先固定深沼裂口下方的積水前庭、碑廊支線與封檻落井，讓雲夢線自然轉入沉沒古廟 dungeon。",
    "level_range": "58-68",
    "planned_vnum_range": "14601-14630",
    "reserved_room_block": "14601-14630",
    "theme": {
      "primary": "仙俠",
      "secondary": "沉沒古廟 / 濕地下探"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 14601,
        "target_area": "wild_yunmeng",
        "label": "深沼裂口"
      },
      {
        "direction": "down",
        "source_vnum": 14612,
        "target_area": "sec_spirit_marsh",
        "label": "更深封井"
      }
    ],
    "clusters": [
      { "id": "entry-sump", "label": "裂口前庭" },
      { "id": "flooded-corridor", "label": "積水主廊" },
      { "id": "inscription-hall", "label": "碑紋偏廊" },
      { "id": "ritual-wing", "label": "祭室側翼" },
      { "id": "sealed-well", "label": "封井前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 14601,
      "name": "裂口落階",
      "description": "深沼下方裂開一道斜斜沉下去的石階，階面滿是滑冷水膜與淤泥。每往下走一步，地表的霧聲就淡一分，而古廟裡那種悶住水氣的回音便更近一層。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-sump",
      "coord": [0, 0, -1],
      "labels": ["entry", "world-link-up"],
      "exits": [
        { "direction": "up", "to": 14512, "external": true },
        { "direction": "down", "to": 14602 }
      ],
      "enquires": ["入口", "退路"]
    },
    {
      "vnum": 14602,
      "name": "積水前庭",
      "description": "前庭的石磚幾乎全被積水淹過一層，踩下去時會帶出細小渦紋與沉響。幾根斷柱仍勉強撐著上方黑影，讓人分不清這裡是迎人的大廳，還是早已失去正面意義的廢墟。",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-sump",
      "coord": [0, 0, -2],
      "labels": ["anteroom", "waterlogged"],
      "exits": [
        { "direction": "up", "to": 14601 },
        { "direction": "east", "to": 14603 }
      ],
      "enquires": ["前面", "古廟"]
    },
    {
      "vnum": 14603,
      "name": "漏水廊道",
      "description": "廊頂不時滴下細冷水珠，打在地面積水上，像一個永遠數不完拍子的鼓點。兩側牆面殘留的舊紋早被水痕拉開，只剩幾段筆劃還倔強地黏在石上。",
      "sector_type": "SECT_INSIDE",
      "cluster": "flooded-corridor",
      "coord": [1, 0, -2],
      "labels": ["main-hall", "dripping"],
      "exits": [
        { "direction": "west", "to": 14602 },
        { "direction": "east", "to": 14604 },
        { "direction": "south", "to": 14605 }
      ],
      "keywords": [
        {
          "keyword": "水痕",
          "description": "牆上的水痕層層疊疊，像在替這座古廟默默記著每一次水位曾漲到哪裡。"
        }
      ],
      "enquires": ["深處", "碑廊"]
    },
    {
      "vnum": 14604,
      "name": "封紋中殿",
      "description": "中殿的地面刻著大半已被磨鈍的封紋，只有中心幾道痕線仍隱約看得出當年的用意。空氣在這裡格外安靜，安靜得連腳邊水聲都像被某種更老、更重的東西壓低了。",
      "sector_type": "SECT_INSIDE",
      "cluster": "flooded-corridor",
      "coord": [2, 0, -2],
      "labels": ["core", "seal"],
      "exits": [
        { "direction": "west", "to": 14603 },
        { "direction": "east", "to": 14608 },
        { "direction": "south", "to": 14609 }
      ],
      "keywords": [
        {
          "keyword": "符文",
          "description": "封紋邊角被泥水磨得模糊，唯有幾筆還保留著微微外擴的走勢，像仍在死守某條不該鬆開的界線。"
        }
      ],
      "enquires": ["封印", "石門"]
    },
    {
      "vnum": 14605,
      "name": "碑廊偏室",
      "description": "一排立碑斜靠在偏室牆邊，碑面大多被水蝕得發白，卻還能看出原本用來記人、記名或記某種祭序。濕氣在這裡帶著更細的霉味，讓人不自覺放慢了呼吸。",
      "sector_type": "SECT_INSIDE",
      "cluster": "inscription-hall",
      "coord": [1, -1, -2],
      "labels": ["records", "side-room"],
      "exits": [
        { "direction": "north", "to": 14603 },
        { "direction": "east", "to": 14606 }
      ],
      "enquires": ["石門", "名字"]
    },
    {
      "vnum": 14606,
      "name": "祭器殘庫",
      "description": "石架與木箱的殘片散在水裡，還有些看不出原形的銅器半浸半露，像只差一點就能被重新辨認。只是越往裡看，越能感覺這裡當年收藏的恐怕不只是祭器，而是整套不想再被打開的儀式。",
      "sector_type": "SECT_INSIDE",
      "cluster": "inscription-hall",
      "coord": [2, -1, -2],
      "labels": ["storage", "ritual"],
      "exits": [
        { "direction": "west", "to": 14605 },
        { "direction": "east", "to": 14607 }
      ],
      "keywords": [
        {
          "keyword": "石門",
          "description": "偏室盡頭的石門雖然早已鬆動，門縫間卻仍卡著幾條像故意留住不讓它完全敞開的鎖紋。"
        }
      ]
    },
    {
      "vnum": 14607,
      "name": "水蝕後堂",
      "description": "後堂已被水氣侵得像快化開一樣，牆角與樑底都有細碎石屑不時剝落。堂內最古怪的不是殘敗，而是那種好像曾經有什麼東西在這裡久留、直到最近才終於離開的空感。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-wing",
      "coord": [3, -1, -2],
      "labels": ["rear-room", "unease"],
      "exits": [
        { "direction": "west", "to": 14606 },
        { "direction": "south", "to": 14611 }
      ],
      "enquires": ["後面", "退路"]
    },
    {
      "vnum": 14608,
      "name": "封檻落井",
      "description": "中殿東側斷開一道直通下方黑水的落井，井緣則以厚重封檻與石鏈圍了一圈。站在這裡往下看，會覺得井裡的黑不只是沒光，而像有什麼東西把所有反光都壓了回去。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-well",
      "coord": [3, 0, -3],
      "labels": ["pit", "drop"],
      "exits": [
        { "direction": "west", "to": 14604 },
        { "direction": "down", "to": 14612 },
        { "direction": "east", "to": 14610 }
      ],
      "keywords": [
        {
          "keyword": "鎖鏈",
          "description": "粗石鏈半沉在水邊，明明早該鬆朽，卻仍維持著一種不像自然留下的拉力。"
        }
      ]
    },
    {
      "vnum": 14609,
      "name": "殘門石階",
      "description": "一段通往側翼的石階在這裡只剩半邊完整，另一半早被水蝕與地裂吞掉。破門框斜倒在旁，讓這條路看起來像不歡迎人，卻又明顯曾是廟裡很重要的一條進退線。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-wing",
      "coord": [2, -1, -3],
      "labels": ["stairs", "broken"],
      "exits": [
        { "direction": "north", "to": 14604 },
        { "direction": "south", "to": 14610 }
      ],
      "enquires": ["側室", "退路"]
    },
    {
      "vnum": 14610,
      "name": "鎖鏈祭室",
      "description": "祭室四周垂著幾道長短不一的石鏈，鏈尾浸在水裡，隨著細微水波輕輕撞出悶聲。中央祭臺只剩輪廓，卻仍讓人很難忽視這裡當年曾有某種需要被牢牢鎖住的東西。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-wing",
      "coord": [3, -1, -3],
      "labels": ["ritual", "chains"],
      "exits": [
        { "direction": "north", "to": 14609 },
        { "direction": "west", "to": 14608 },
        { "direction": "east", "to": 14611 }
      ],
      "keywords": [
        {
          "keyword": "祭臺",
          "description": "祭臺中央凹得極深，邊緣還看得出曾經嵌放過某種圓形或印紋物件的痕跡。"
        }
      ],
      "enquires": ["祭室", "封印"]
    },
    {
      "vnum": 14611,
      "name": "回水暗渠",
      "description": "暗渠裡的水並不急，卻總在往看不見的更深處回流，像整座古廟仍悄悄把多餘的水與聲音都送往同一個地方。牆面靠近水線的位置浮著一層細亮苔光，使這裡比其他地方更像活著。",
      "sector_type": "SECT_INSIDE",
      "cluster": "ritual-wing",
      "coord": [4, -1, -3],
      "labels": ["channel", "flow"],
      "exits": [
        { "direction": "west", "to": 14610 },
        { "direction": "north", "to": 14607 }
      ],
      "enquires": ["暗渠", "深處"]
    },
    {
      "vnum": 14612,
      "name": "深封井口",
      "description": "井底在這裡終於收成一個更窄、更深的封井口，四周刻痕比上層更完整，連水聲都像被它們壓得只剩細碎回響。只要再往下探，走的就不再只是沉沒古廟，而是更像整片大澤底下真正不該見光的部分。",
      "sector_type": "SECT_INSIDE",
      "cluster": "sealed-well",
      "coord": [3, 0, -4],
      "labels": ["deep-edge", "world-link-down"],
      "exits": [
        { "direction": "up", "to": 14608 }
      ],
      "enquires": ["下面", "深處", "去路"]
    }
  ]
}
```
