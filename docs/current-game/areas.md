---
layout: default
title: Current Game Areas
---

# Current Game Areas

這份文件只記錄目前 `merc-fju-3.0` repo 會實際載入的 area 台帳與近來重建區域摘要，用來避免和 `docs/3yWebsite/` 的舊站參考資料混在一起。

對應的機器可讀補充台帳在 `docs/current-game/areas.json`。

## 邊界

- `docs/3yWebsite/`：reference-only，主要提供舊版世界觀、地圖、命名語彙與歷史脈絡。
- `docs/current-game/areas.md`：現行 repo 會載入的 area 索引與重建區補充說明。

## Runtime Source Of Truth

真正決定目前遊戲 area 是否存在、載入順序為何、房間邊界如何銜接的來源仍然是 repo 內的 runtime 與規劃檔案，包括 `area/directory.lst`、`area/<area>/index`、`area/<area>/map.md`、`plans/area/*.md`、`area/rebuild_plan.md`、`area/world_map.md`。

這份文件只做開發紀錄，不取代上述 runtime / planning 資料。

## Area Catalog

| Area | 中文名稱 / 用途 | 房間範圍 | 分類 | 備註 |
| --- | --- | --- | --- | --- |
| `limbo` | 特殊地方 / 預設基本區域 | `0001-0500` | `legacy core` | 基本房間與基礎物件載入區，固定作為第一個 area。 |
| `loyang` | 洛陽城 / 主城 | `0501-0744` | `legacy core` | 可作出生地與 recall 主城，洛陽重建鏈的母城。 |
| `beiping` | 北平 / 北方主城 | `9001-9063` | `legacy core` | 北方交通樞紐，北平郊區鏈的母城。 |
| `new` | 新手區 / 教學區 | `0450-0477` | `newbie / training` | 提供新手導覽、基礎指令與遊戲節奏入門。 |
| `newfight` | 新手練功區 / 初期升級區 | `1201-1295` | `newbie / training` | 承接新手區後的低等戰鬥與練功流程。 |
| `pk_area` | PK區 / 對戰場 | `1301-1333` | `special combat` | 玩家與幫派對戰專用區。 |
| `free_fight` | 三國競技場 / 自由戰鬥區 | `7001-7044` | `special combat` | 特殊戰鬥用途 area。 |
| `loyang_outskirts` | 洛陽東郊 / 洛陽外郊過渡帶 | `7501-7512` | `rebuild addition` | 洛陽地表鏈起點，連回 `loyang` 並往丘陵與地下入口延伸。 |
| `wild_longqu_hills` | 龍渠丘陵 / 城郊外圈丘陵探索帶 | `9401-9410` | `rebuild addition` | 承接洛陽東郊東向邊界，轉入較危險的野外與遺跡前帶。 |
| `dng_loyang_sewer` | 洛陽地下水區 / 地下前哨 | `9451-9460` | `rebuild addition` | 由洛陽東郊暗井下探的第一層地下水道。 |
| `dng_sewer_depths` | 地下深渠 / 深層黑水水道 | `9461-9470` | `rebuild addition` | 洛陽地下鏈的第二段，強化封印與黑水深渠壓力。 |
| `dng_royal_tomb` | 帝王古墓 / 古墓機關秘境前帶 | `9481-9490` | `rebuild addition` | 從深渠轉入古墓與機關探索段。 |
| `sec_catacomb_depths` | 忘川地穴 / 靈異地穴 secret zone | `9491-9499` | `rebuild addition` | 由古墓往下銜接異象核心與秘壇風險。 |
| `sec_rift_below` | 異象裂谷 / 裂谷秘境前帶 | `9501-9512` | `rebuild addition` | 地穴之下的裂風與冷光裂谷區。 |
| `sec_rift_core` | 裂谷心核 / 底層核心區 | `9601-9612` | `rebuild addition` | 承接異象裂谷，進入心核脈動與封界壓力。 |
| `sec_rift_deeps` | 裂界深層 / 深層封印帶 | `9701-9712` | `rebuild addition` | 裂谷核心之下的第二層核心區，保留更深裂界禁底的後續延伸。 |
| `beiping_outskirts` | 北平郊區 / 北境外郊過渡帶 | `9101-9108` | `rebuild addition` | 由 `beiping` 往易京與白狼山方向展開的第一段外郊。 |
| `jingxiang_road` | 荊襄大道 / 荊州走廊幹道 | `9301-9310` | `rebuild addition` | 目前以 world-link stub 方式保留襄陽、新野、江夏的後續母城掛接。 |
| `sec_rift_abyss` | 裂界禁底 / 禁底封印帶 | `9801-9812` | `rebuild addition` | 由裂界深層下探到禁底落點、封印回廊與禁底界井。 |
| `sec_rift_nadir` | 裂界禁牢 / 禁牢封印帶 | `9901-9912` | `rebuild addition` | 承接裂界禁底，轉入更高壓的禁牢封印與界井前帶。 |
| `sec_rift_prison_core` | 封印核心 / 心獄鎮封帶 | `10001-10012` | `rebuild addition` | 由裂界禁牢再下探到鎮封主廊、護印支線與封印井心。 |
| `sec_rift_underseal_dais` | 鎮封底座 / 反衝承壓層 | `10101-10112` | `rebuild addition` | 承接封印核心井心下方，落成鎮封主環與本核前緣過渡帶。 |
| `sec_rift_true_core` | 裂界本核 / 失穩封圈 | `10201-10212` | `rebuild addition` | 由鎮封底座再下探到本核外環、導脈偏廊與核心井場。 |
| `sec_rift_core_below` | 裂核下層 / 深井脈道過渡層 | `10301-10312` | `rebuild addition` | 承接裂界本核最深縱井，轉入更危險的裂核下層通道。 |
| `sec_rift_core_below_deeps` | 裂核深層 / 底脈渦腹承接區 | `10401-10412` | `rebuild addition` | 由裂核下層再下探到渦腹主脈與底潮封口的深層承接區。 |
| `sec_rift_core_vein_abyss` | 裂核脈淵 / 渦核深腹高壓前帶 | `10501-10512` | `rebuild addition` | 承接裂核深層封檻臺，下探到脈淵環脈、倒灌裂庭與沉界井緣。 |
| `sec_rift_underseal_basin` | 禁底封脈盆 / 沉壓承接層 | `10601-10612` | `rebuild addition` | 承接裂核脈淵沉檻，下探到封脈環池、壓紋支廊與底盆沉門。 |
| `sec_rift_sealed_core_basin` | 封核沉盆 / 內壓核心 | `10701-10712` | `rebuild addition` | 承接禁底封脈盆沉門，下探到封核環盆、回壓渠廊與封心前庭。 |
| `sec_rift_sealed_core_heart` | 封心核心 / 心脈主井 | `10801-10812` | `rebuild addition` | 承接封核沉盆深井，下探到封心環脈、心壓偏廊與裂核前座。 |
| `sec_rift_core_spirit_nadir` | 核心魄淵 / 心魄沉座 | `10901-10912` | `rebuild addition` | 承接封心核心深座，下探到核心沉環、失魄偏廊與魄淵前座。 |
| `sec_rift_core_spirit_abyss` | 魄淵深井 / 暗層沉降 | `11001-11012` | `rebuild addition` | 承接核心魄淵座，下探到深井環脈、空響偏廊與魄核前座。 |
| `sec_rift_spirit_core_hollow` | 魄核空井 / 空腹暗層 | `11101-11112` | `rebuild addition` | 承接魄淵深井沉座，下探到空腹環脈、失響偏廊與裂魄前座。 |
| `sec_rift_spirit_core_void` | 裂魄空心 / 虛腹暗層 | `11201-11212` | `rebuild addition` | 承接魄核空井沉井座，下探到裂腹環脈、寂響偏廊與真空前座。 |
| `sec_rift_spirit_core_vacuum` | 裂魄真空 / 真空深腹 | `11301-11312` | `rebuild addition` | 承接裂魄空心虛座，下探到真空環脈、滅響偏廊與歸零前座。 |
| `sec_rift_spirit_core_null` | 裂魄歸零 / 歸零深庭 | `11401-11412` | `rebuild addition` | 承接裂魄真空座，下探到歸零沉庭、空滅偏廊與零界前座。 |
| `sec_rift_spirit_core_zero` | 裂魄零界 / 零界深井 | `11501-11512` | `rebuild addition` | 承接裂魄歸零座，下探到零界內庭、無痕偏廊與空白前座。 |
| `sec_rift_spirit_core_blank` | 裂魄空白 / 空白深井 | `11601-11612` | `rebuild addition` | 承接裂魄零界座，下探到空白內庭、失序偏廊與白界前座。 |
| `sec_rift_spirit_core_white` | 裂魄白界 / 白界深井 | `11701-11712` | `rebuild addition` | 承接裂魄空白座，下探到白界內庭、失名偏廊與素界前座。 |
| `sec_rift_spirit_core_plain` | 裂魄素界 / 素界深井 | `11801-11812` | `rebuild addition` | 承接裂魄白界座，下探到素界內庭、澹痕偏廊與澹界前座。 |
| `sec_rift_spirit_core_faint` | 裂魄澹界 / 澹界深井 | `11901-11912` | `rebuild addition` | 承接裂魄素界座，下探到澹界內庭、微痕偏廊與微界前座。 |
| `sec_rift_spirit_core_trace` | 裂魄微界 / 微界深井 | `12001-12012` | `rebuild addition` | 承接裂魄澹界座，下探到微界內庭、細痕偏廊與塵界前座。 |
| `sec_rift_spirit_core_mote` | 裂魄塵界 / 塵界深井 | `12101-12112` | `rebuild addition` | 承接裂魄微界座，下探到塵界內庭、塵粒偏廊與粒界前座。 |
| `sec_rift_spirit_core_grain` | 裂魄粒界 / 粒界深井 | `12201-12212` | `rebuild addition` | 承接裂魄塵界座，下探到粒界內庭、末粒偏廊與末界前座。 |
| `sec_rift_spirit_core_last` | 裂魄末界 / 末界深井 | `12301-12312` | `rebuild addition` | 承接裂魄粒界座，下探到末界內庭、終塵偏廊與終界前座。 |
| `sec_rift_spirit_core_final` | 裂魄終界 / 終界井腹 | `12401-12412` | `rebuild addition` | 承接裂魄末界座，下探到終界內庭、極終偏廊與終核前座。 |
| `sec_rift_spirit_core_terminal` | 裂魄絕界 / 絕界井核 | `12501-12512` | `rebuild addition` | 承接裂魄終界座，下探到絕界內庭、滅終偏廊與滅核前座。 |
| `sec_rift_spirit_core_extinct` | 裂魄滅界 / 滅界井腹 | `12601-12612` | `rebuild addition` | 承接裂魄絕界座，下探到滅界內庭、寂滅偏廊與寂核前座。 |
| `sec_rift_spirit_core_silent` | 裂魄寂界 / 寂界井腹 | `12701-12712` | `rebuild addition` | 承接裂魄滅界座，下探到寂界內庭、寥寂偏廊與寥核前座。 |
| `sec_rift_spirit_core_dim` | 裂魄寥界 / 寥界井腹 | `12801-12812` | `rebuild addition` | 承接裂魄寂界座，下探到寥界內庭、微寥偏廊與微寥前座。 |
| `sec_rift_spirit_core_gloam` | 裂魄微寥 / 微寥井腹 | `12901-12912` | `rebuild addition` | 承接裂魄寥界座，下探到微寥內庭、晦微偏廊與晦核前座。 |
| `sec_rift_spirit_core_umbral` | 裂魄晦界 / 晦界井腹 | `13001-13012` | `rebuild addition` | 承接裂魄微寥座，下探到晦界內庭、冥晦偏廊與冥核前座。 |
| `sec_rift_spirit_core_nether` | 裂魄冥界 / 冥界井腹 | `13101-13112` | `rebuild addition` | 承接裂魄晦界座，下探到冥界內庭、幽冥偏廊與玄冥前座。 |
| `sec_rift_spirit_core_stygian` | 裂魄玄冥 / 玄冥井腹 | `13201-13212` | `rebuild addition` | 承接裂魄冥界座，下探到玄冥內庭、玄幽偏廊與玄冥前座。 |
| `sec_rift_spirit_core_chthonic` | 裂魄幽玄 / 幽玄井腹 | `13301-13312` | `rebuild addition` | 承接裂魄玄冥座，下探到幽玄內庭、冥幽偏廊與玄幽前座。 |
| `sec_rift_spirit_core_abysmal` | 裂魄玄幽 / 玄幽井腹 | `13401-13412` | `rebuild addition` | 承接裂魄幽玄座，下探到玄幽內庭、幽冥偏廊與玄幽前座。 |
| `sec_rift_spirit_core_tartarean` | 裂魄冥淵 / 冥淵井腹 | `13501-13512` | `rebuild addition` | 承接裂魄玄幽座，下探到冥淵內庭、淵冥偏廊與冥獄前座。 |
| `sec_rift_spirit_core_infernal` | 裂魄冥獄 / 冥獄井腹 | `13601-13612` | `rebuild addition` | 承接裂魄冥淵座，下探到冥獄內庭、獄冥偏廊與業獄前座。 |
| `sec_rift_spirit_core_gehennal` | 裂魄業獄 / 業獄井腹 | `13701-13712` | `rebuild addition` | 承接裂魄冥獄座，下探到業獄內庭、業冥偏廊與寒獄前座。 |
| `city_chenliu` | 陳留 / 中原樞紐城 | `13801-13830` | `rebuild addition` | queue reset 後的第一個主世界城市 hub，先落地主街、服務區、軍旅區與南驛轉接骨架。 |
| `wild_puyang_forest` | 濮陽林野 / 官渡前帶野外 | `13901-13930` | `rebuild addition` | 承接陳留北路的林野探索帶，整合林間主徑、濕窪側線與舊哨土塍。 |
| `dng_guandu_battlefield` | 官渡古戰場 / 鏖兵戰地 dungeon | `14001-14030` | `rebuild addition` | 承接濮陽林野北向荒路，落成壕溝、焚糧車與殘旗高地交錯的古戰場前段。 |
| `fort_hulao` | 虎牢關 / 東都門戶關隘 | `14101-14120` | `rebuild addition` | 承接官渡古戰場北界，落成關前坡道、甕城、軍營與關樓高差構成的軍事 choke point。 |
| `city_xiangyang` | 襄陽城 / 荊州門戶主城 | `14201-14230` | `rebuild addition` | 承接荊襄大道北界，落成南城門、主街十字、西市補給線與東碼頭構成的城市 hub。 |
| `wild_jiangxia_river` | 江夏水道 / 江岸水路野外 | `14301-14330` | `rebuild addition` | 承接襄陽東碼頭外緣，落成離城木棧、蘆葦濕灘、水寨殘樁與東向渡口前帶。 |

## Recent Rebuild Areas

### 洛陽地表鏈

- `loyang_outskirts`：把洛陽東陽門外的橋頭、官道、龍渠農田與地下入口整成第一圈城郊過渡帶，作為洛陽重建鏈的地表起點。
- `wild_longqu_hills`：承接洛陽東郊的丘陵巡路，將玩家節奏從主城近郊推進到丘陵遺跡與外野探索線。

### 洛陽地下鏈

- `dng_loyang_sewer`：把洛陽東郊暗井正式延伸成可載入的地下水脈與水門前帶，建立地下鏈入口層。
- `dng_sewer_depths`：從地下水區更下探到黑水主渠、機關側室與封印深槽，讓地下鏈進入真正的深層危險帶。
- `dng_royal_tomb`：把黑水深渠下方的下沉井口接成帝王古墓前帶，完成水道向古墓機關秘境的主題轉折。
- `sec_catacomb_depths`：由帝王古墓再往下推進到靈異地穴與異象核心，建立高風險高回報的第一層 secret zone。
- `sec_rift_below`：承接忘川地穴最深處，落成裂谷著階、風脊與祕境沉門前帶，讓地下鏈進入更深的異象裂谷區。
- `sec_rift_core`：把異象裂谷下方接成心核主廊、晶脈支線與底層封界，形成真正的地下高風險核心節點。
- `sec_rift_deeps`：再由裂谷心核下探到封印回廊、禁制支線與禁底界井前帶，為未來裂界禁底保留延伸空間。
- `sec_rift_abyss`：把裂界深層下方接成禁底落點、封印回廊與禁底界井，讓地下鏈正式轉入禁底封印段。
- `sec_rift_nadir`：再由裂界禁底下探到禁牢前帶、鎮鎖側線與禁牢界井，形成更深一層的禁牢封印節點。
- `sec_rift_prison_core`：由裂界禁牢再往下落成鎮封主廊、護印支線與封印井心，讓地下鏈抵達目前已知的封印核心前帶。
- `sec_rift_underseal_dais`：承接封印井心下方的鎮封底座，補齊主環、承壓旁廊與本核前緣，形成進入本核前的最後緩衝層。
- `sec_rift_true_core`：由鎮封底座最深縱井再下探到失穩封圈與核心井場，讓地下鏈正式進入裂界本核主區。
- `sec_rift_core_below`：把裂界本核下方接成落井接臺、深井裂道與封橋前帶，讓地下鏈轉入裂核層。
- `sec_rift_core_below_deeps`：再由裂核下層下探到渦腹主脈、鎮紋旁廊與底潮封口，形成更深渦腹承接區。
- `sec_rift_core_vein_abyss`：承接裂核深層最底端，下探到深腹環脈、倒灌裂庭與沉界井緣，作為更深禁底封脈區前的高壓前帶。
- `sec_rift_underseal_basin`：承接裂核脈淵沉檻，下探到封脈環池、壓紋支廊與底盆沉門，作為更深禁底核心區前的沉壓承接層。
- `sec_rift_sealed_core_basin`：承接禁底封脈盆沉門，下探到封核環盆、回壓渠廊與封心前庭，作為更深裂核封心區前的核心承壓內盆。
- `sec_rift_sealed_core_heart`：承接封核沉盆深井，下探到封心環脈、心壓偏廊與裂核前座，作為更深裂核心魄區前的主心脈節點。
- `sec_rift_core_spirit_nadir`：承接封心核心深座，下探到核心沉環、失魄偏廊與魄淵前座，作為更深核心魄淵暗層前的心魄沉降帶。
- `sec_rift_core_spirit_abyss`：承接核心魄淵座，下探到深井環脈、空響偏廊與魄核前座，作為更深魄核空井區前的暗層沉降帶。
- `sec_rift_spirit_core_hollow`：承接魄淵深井沉座，下探到空腹環脈、失響偏廊與裂魄前座，作為更深裂魄空心區前的空腹暗層帶。
- `sec_rift_spirit_core_void`：承接魄核空井沉井座，下探到裂腹環脈、寂響偏廊與真空前座，作為更深裂魄真空區前的虛腹暗層帶。
- `sec_rift_spirit_core_vacuum`：承接裂魄空心虛座，下探到真空環脈、滅響偏廊與歸零前座，作為更深裂魄歸零區前的真空深腹過渡帶。
- `sec_rift_spirit_core_null`：承接裂魄真空座，下探到歸零沉庭、空滅偏廊與零界前座，作為更深裂魄零界區前的歸零深庭過渡帶。
- `sec_rift_spirit_core_zero`：承接裂魄歸零座，下探到零界內庭、無痕偏廊與空白前座，作為更深裂魄空白區前的零界深井過渡帶。
- `sec_rift_spirit_core_blank`：承接裂魄零界座，下探到空白內庭、失序偏廊與白界前座，作為更深裂魄白界區前的空白深井過渡帶。
- `sec_rift_spirit_core_white`：承接裂魄空白座，下探到白界內庭、失名偏廊與素界前座，作為更深裂魄素界區前的白界深井過渡帶。
- `sec_rift_spirit_core_plain`：承接裂魄白界座，下探到素界內庭、澹痕偏廊與澹界前座，作為更深裂魄澹界區前的素界深井過渡帶。
- `sec_rift_spirit_core_faint`：承接裂魄素界座，下探到澹界內庭、微痕偏廊與微界前座，作為更深裂魄微界區前的澹界深井過渡帶。
- `sec_rift_spirit_core_trace`：承接裂魄澹界座，下探到微界內庭、細痕偏廊與塵界前座，作為更深裂魄塵界區前的微界深井 plateau 過渡帶。
- `sec_rift_spirit_core_mote`：承接裂魄微界座，下探到塵界內庭、塵粒偏廊與粒界前座，作為更深裂魄粒界區前的塵界深井 plateau 過渡帶。
- `sec_rift_spirit_core_grain`：承接裂魄塵界座，下探到粒界內庭、末粒偏廊與末界前座，作為更深裂魄末界區前的粒界深井 plateau 過渡帶。
- `sec_rift_spirit_core_last`：承接裂魄粒界座，下探到末界內庭、終塵偏廊與終界前座，作為更深裂魄終界區前的末界深井 plateau 過渡帶。
- `sec_rift_spirit_core_final`：承接裂魄末界座，下探到終界內庭、極終偏廊與終核前座，作為更深裂魄絕界區前的終界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_terminal`：承接裂魄終界座，下探到絕界內庭、滅終偏廊與滅核前座，作為更深裂魄滅界區前的絕界井核 plateau 過渡帶。
- `sec_rift_spirit_core_extinct`：承接裂魄絕界座，下探到滅界內庭、寂滅偏廊與寂核前座，作為更深裂魄寂界區前的滅界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_silent`：承接裂魄滅界座，下探到寂界內庭、寥寂偏廊與寥核前座，作為更深裂魄寥界區前的寂界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_dim`：承接裂魄寂界座，下探到寥界內庭、微寥偏廊與微寥前座，作為更深裂魄微寥區前的寥界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_gloam`：承接裂魄寥界座，下探到微寥內庭、晦微偏廊與晦核前座，作為更深裂魄晦界區前的微寥井腹 plateau 過渡帶。
- `sec_rift_spirit_core_umbral`：承接裂魄微寥座，下探到晦界內庭、冥晦偏廊與冥核前座，作為更深裂魄冥界區前的晦界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_nether`：承接裂魄晦界座，下探到冥界內庭、幽冥偏廊與玄冥前座，作為更深裂魄玄冥區前的冥界井腹 plateau 過渡帶。
- `sec_rift_spirit_core_stygian`：承接裂魄冥界座，下探到玄冥內庭、玄幽偏廊與玄冥前座，作為更深裂魄幽玄區前的玄冥井腹 plateau 過渡帶。
- `sec_rift_spirit_core_chthonic`：承接裂魄玄冥座，下探到幽玄內庭、冥幽偏廊與玄幽前座，作為更深裂魄玄幽區前的幽玄井腹 plateau 過渡帶。
- `sec_rift_spirit_core_abysmal`：承接裂魄幽玄座，下探到玄幽內庭、幽冥偏廊與玄幽前座，作為更深裂魄冥淵區前的玄幽井腹 plateau 過渡帶。
- `sec_rift_spirit_core_tartarean`：承接裂魄玄幽座，下探到冥淵內庭、淵冥偏廊與冥獄前座，作為更深裂魄冥獄區前的冥淵井腹 plateau 過渡帶。
- `sec_rift_spirit_core_infernal`：承接裂魄冥淵座，下探到冥獄內庭、獄冥偏廊與業獄前座，作為更深裂魄業獄區前的冥獄井腹 plateau 過渡帶。
- `sec_rift_spirit_core_gehennal`：承接裂魄冥獄座，下探到業獄內庭、業冥偏廊與寒獄前座，作為更深裂魄寒獄區前的業獄井腹 plateau 過渡帶。

### 北方鏈

- `beiping_outskirts`：把北平北側外郊整理成哨卡、驛道、河灘與北境山徑前帶，補齊往易京與白狼山方向的邊關過渡感。

### 荊州幹道鏈

- `jingxiang_road`：先把荊州走廊的巡檢亭、驛館支線與可疑地窖落成為可載入 area，母城連線則維持在 spec 的 world-link 層。

### 中原城市鏈

- `city_chenliu`：把陳留先落成可載入的中原樞紐城骨架，整合西門、主街、商旅補給、軍旅訓練與南驛轉接，作為 queue reset 後回到三國地表主線的第一個正式城市 hub。

### 官渡前帶鏈

- `wild_puyang_forest`：把陳留北路外的林野前帶先落成可載入 area，透過林蔭主徑、濕窪獵徑與舊哨高地把玩家節奏從城市補給推到官渡戰前外圍。
- `dng_guandu_battlefield`：把濮陽林野北向荒路正式接進官渡古戰場，透過壕溝、焚糧車列、殘旗坡與死地前帶把節奏推進到真正的戰地 dungeon。
- `fort_hulao`：把官渡古戰場北界正式接進虎牢關，透過關門、甕城、軍需棚與關樓望樓把節奏轉成重兵把守的戰略門戶。
- `city_xiangyang`：把荊襄大道北界正式接進襄陽城，透過城門、市集、官署與東碼頭把節奏從關隘轉回荊州主城與水陸交通 hub。
- `wild_jiangxia_river`：把襄陽東碼頭正式接進江岸水路野外，透過離城木棧、蘆葦濕灘、水寨殘樁與候船渡口把主線推往江夏方向。

## 維護規則

- 若 runtime 新增、移除或重排 area，應同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`。
- 若重建區有新的 `map.md`、world link 或 room block 變更，優先以 `area/directory.lst`、`area/<area>/index`、`plans/area/*.md` 與 `area/rebuild_plan.md` 為準再回寫這份文件。
