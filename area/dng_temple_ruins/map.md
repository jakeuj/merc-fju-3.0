# 山中古寺 (`dng_temple_ruins`)

## Area Intent

`dng_temple_ruins` 承接 `city_kuaiji` 的古祠地脈預留，把會稽山城裡那些關於地脈、封印與門派避談之事，正式轉進一座潮濕、殘敗而仍帶禁制感的山中古寺 dungeon。

## Theme Positioning

- Theme: `仙俠`
- Subtheme: `古寺 / 異聞`
- LevelRange: `100-100`

## mapmd-json

```mapmd-json
{
  "area": {
    "schema": "mapmd-json/v1",
    "name": "dng_temple_ruins",
    "title": "山中古寺",
    "design_notes": "第一版 spec-first 草案。先固定地脈入口、殘鐘前廳、滴水甬道、封印偏室、供臺中殿與更深石室前帶，讓會稽鏈正式從山城傳聞切進可下探的古寺 dungeon。",
    "level_range": "100-100",
    "planned_vnum_range": "16501-16530",
    "reserved_room_block": "16501-16530",
    "theme": {
      "primary": "仙俠",
      "secondary": "古寺 / 異聞"
    },
    "world_links": [
      {
        "direction": "up",
        "source_vnum": 16501,
        "target_area": "city_kuaiji",
        "label": "古祠地脈"
      },
      {
        "direction": "down",
        "source_vnum": 16510,
        "target_area": "sec_kuaiji_seal_chamber",
        "label": "深封石室"
      }
    ],
    "clusters": [
      { "id": "entry-hall", "label": "地脈入口" },
      { "id": "corridor", "label": "滴水甬道" },
      { "id": "side-cell", "label": "封印偏室" },
      { "id": "main-shrine", "label": "供臺中殿" },
      { "id": "deep-seal", "label": "深封前帶" }
    ]
  },
  "rooms": [
    {
      "vnum": 16501,
      "name": "地脈石梯",
      "description": "石梯從山城底下的地脈縫隙一路往下，潮氣與舊灰味在這裡已經濃到能把城上的人聲整個隔開。你很難說這裡究竟還算不算古寺入口，只能確定從踏上這階開始，會稽城裡那些不能明說的傳聞就不再只是傳聞。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-hall",
      "coord": [0, 0, 0],
      "labels": ["up-link", "entry"],
      "exits": [
        { "direction": "up", "to": 16406, "external": true },
        { "direction": "south", "to": 16503 },
        { "direction": "east", "to": 16502 }
      ],
      "enquires": ["入口", "石梯", "退路"]
    },
    {
      "vnum": 16502,
      "name": "殘鐘前廳",
      "description": "前廳裡掛著半裂的殘鐘，鐘身上的紋路早已斑駁，卻仍透著某種不願徹底消散的靈意。空氣裡沒有風，鐘卻偶爾發出極輕的震顫聲，像深處還有什麼正沿著石壁慢慢醒來。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "entry-hall",
      "coord": [1, 0, 0],
      "labels": ["hall", "bell"],
      "exits": [
        { "direction": "west", "to": 16501 }
      ],
      "enquires": ["殘鐘", "前廳"]
    },
    {
      "vnum": 16503,
      "name": "滴水甬道",
      "description": "甬道狹長而陰濕，頂上的裂隙不停有細水滴下來，讓每一步回音都像在替更深處數拍子。會稽城裡那種帶著人情和秩序的氣味在這裡已完全退去，只剩石與水把整段路守得死死的。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "corridor",
      "coord": [0, -1, 0],
      "labels": ["main-way", "wet"],
      "exits": [
        { "direction": "north", "to": 16501 },
        { "direction": "south", "to": 16504 },
        { "direction": "east", "to": 16505 }
      ],
      "enquires": ["甬道", "深處", "水聲"]
    },
    {
      "vnum": 16504,
      "name": "供臺中殿",
      "description": "中殿前的供臺大半已經崩塌，卻仍看得出這裡曾經是整座古寺最核心的敬奉之地。如今香灰成了潮泥，殘燭成了黑痕，只剩那股被人刻意壓住的禁制感還死死盤在這裡。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "main-shrine",
      "coord": [0, -2, 0],
      "labels": ["altar", "core"],
      "exits": [
        { "direction": "north", "to": 16503 },
        { "direction": "south", "to": 16510 },
        { "direction": "west", "to": 16507 },
        { "direction": "east", "to": 16506 }
      ],
      "enquires": ["供臺", "中殿", "封印"]
    },
    {
      "vnum": 16505,
      "name": "裂壁偏龕",
      "description": "偏龕藏在甬道旁的裂壁內側，石龕邊緣還殘留著被刀器刮去符文的痕跡。這裡不像真正的退路，倒更像有人曾想在正殿外側偷偷做些不該被發現的事。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-cell",
      "coord": [1, -1, 0],
      "labels": ["side-room", "glyph"],
      "exits": [
        { "direction": "west", "to": 16503 },
        { "direction": "south", "to": 16506 }
      ],
      "enquires": ["偏龕", "符文"]
    },
    {
      "vnum": 16506,
      "name": "封印偏室",
      "description": "偏室裡的地面和石柱都刻滿了曾被修補又再度崩裂的封印紋，像每一次補強都只證明了一件事，那就是這裡真正鎮著的東西從來沒有安分過。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "side-cell",
      "coord": [1, -2, 0],
      "labels": ["seal-room", "ritual"],
      "exits": [
        { "direction": "north", "to": 16505 },
        { "direction": "west", "to": 16504 }
      ],
      "enquires": ["封印", "偏室", "石柱"]
    },
    {
      "vnum": 16507,
      "name": "殘經藏角",
      "description": "這一角曾經似乎堆滿經卷，如今只剩發黑紙灰與被水浸爛的木架。可即使經文早散，這裡仍有一種像被字句和祈願長久壓過的沉重，讓人不敢久待。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "main-shrine",
      "coord": [-1, -2, 0],
      "labels": ["scripture", "ash"],
      "exits": [
        { "direction": "east", "to": 16504 },
        { "direction": "south", "to": 16508 }
      ],
      "enquires": ["殘經", "紙灰"]
    },
    {
      "vnum": 16508,
      "name": "石縫水牢",
      "description": "石縫間積著冷水，讓這裡像半間牢室、半段天然裂穴。腳下每一次踩動水面，四周都會回出比你預期更遠的空響，像下方還有更深一層的東西正等待被驚動。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-seal",
      "coord": [-1, -3, 0],
      "labels": ["water", "deep"],
      "exits": [
        { "direction": "north", "to": 16507 },
        { "direction": "east", "to": 16510 }
      ],
      "enquires": ["水牢", "深處"]
    },
    {
      "vnum": 16510,
      "name": "深封石室前",
      "description": "石室前的空氣幾乎凝成了看不見的重量，像只要再向下探一步，古寺真正想藏住的東西就會從更深的黑暗裡把目光投上來。這裡不像終點，更像一道在多年失守後勉強仍算存在的最後界線。 ",
      "sector_type": "SECT_INSIDE",
      "cluster": "deep-seal",
      "coord": [0, -3, 0],
      "labels": ["down-link", "seal-front"],
      "exits": [
        { "direction": "north", "to": 16504 },
        { "direction": "west", "to": 16508 }
      ],
      "enquires": ["石室", "封印", "更深"]
    }
  ]
}
```
