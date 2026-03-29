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
| `city_jiangxia` | 江夏 / 荊州東岸江港主城 | `14401-14430` | `rebuild addition` | 承接江夏水道東界，落成渡口外門、港前主街、市集補給區與水軍官署骨架。 |
| `wild_yunmeng` | 雲夢大澤 / 迷霧濕地野外 | `14501-14530` | `rebuild addition` | 承接江夏南向水巷外側，落成濕地邊樁、霧中高埠、半沉石碑與深沼前帶。 |
| `dng_sunken_temple` | 沉沒古廟 / 濕地下探 dungeon | `14601-14630` | `rebuild addition` | 承接雲夢深沼下方，落成積水前庭、封紋中殿、鎖鏈祭室與深封井口骨架。 |
| `city_chaisang` | 柴桑 / 江岸東口城市 | `14701-14730` | `rebuild addition` | 承接江夏東向幹道，落成西向江門、江岸主街、市集補給與南向轉場區骨架。 |
| `sec_chibi_battlefield` | 赤壁古戰場 / 江岸古戰場祕區 | `14801-14830` | `rebuild addition` | 承接柴桑南緣路標，落成灰燼坡帶、殘艦灘口、火痕主陣與祭火高地骨架。 |
| `city_changsha` | 長沙 / 荊南主城 | `14901-14930` | `rebuild addition` | 承接柴桑南向官道，落成北門、主街、市集補給、官署前街與南門官道骨架。 |
| `wild_wuling` | 武陵山 / 深山野外前帶 | `15001-15030` | `rebuild addition` | 承接長沙西牌山路，落成石碑山路、靈木坡面、山腹高徑與霧帶谷口骨架。 |
| `city_lingling` | 零陵 / 南境山城 | `15101-15130` | `rebuild addition` | 承接長沙南向官道，落成北門、主街、市集補給、官署前街與南門官道骨架。 |
| `city_guiyang` | 桂陽 / 南嶺邊地城鎮 | `15201-15230` | `rebuild addition` | 承接零陵南向官道，落成北門、主街、市集補給、官署前街與南門官道骨架。 |
| `wild_nanman_jungle` | 南蠻密林 / 部族邊徑 wild | `15301-15330` | `rebuild addition` | 承接桂陽西岔，落成濕根主路、圖騰林口、祭柱空地與根台高徑骨架。 |
| `dng_serpent_temple` | 蛇神殿 / 血祭封殿 dungeon | `15401-15430` | `rebuild addition` | 承接南蠻密林林下祠痕，落成潮濕前廳、蛇紋甬道、滴血祭槽與封紋內殿骨架。 |
| `city_nanhai` | 南海 / 南境海港 hub | `15501-15530` | `rebuild addition` | 承接桂陽南路，落成港街、市集補給、港務前街與臨海南口骨架。 |
| `wild_south_sea_route` | 南海外航道 / 礁岸海路 wild | `15601-15630` | `rebuild addition` | 承接南海臨海南口，落成近海棧道、潮石灣、退潮礁坪與外航前帶骨架。 |
| `dng_boat_graveyard` | 沉舟墓場 / 外海 wreck dungeon | `15701-15730` | `rebuild addition` | 承接南航分水渦口，落成破桅前廊、漏艙窄道、錨鏈井口與墓場深艙骨架。 |
| `wild_pirate_islands` | 海盜群島 / 外海碎島 wild | `15801-15830` | `rebuild addition` | 承接沉舟墓場外海破舷，落成礁灣主徑、海寇舊寨、風旗高脊與外礁深灘骨架。 |
| `fort_naval_base` | 水軍大營 / 海防軍營 fort | `15901-15930` | `rebuild addition` | 承接海盜群島東向暗棧，落成棧門柵關、補給棚區、望樓高位與內港水門骨架。 |
| `city_jianye` | 建業 / 江東都城 hub | `16001-16030` | `rebuild addition` | 承接水軍大營內港水門，落成南街、中街、市集牌樓、官署前街與港向街口骨架。 |
| `district_jianye_port` | 建業港區 / 商港分區 | `16101-16130` | `rebuild addition` | 承接建業港向街口，落成碼頭主道、貨棚泊位、船行牌坊與商船外棧骨架。 |
| `wild_jianye_west` | 建業西郊 / 水鄉外帶 | `16201-16230` | `rebuild addition` | 承接建業西坊，落成西坊回道、水圳旁徑、茶亭前坪與更西村路骨架。 |
| `wild_mountain_pass` | 會稽山道 / 抬升山路 wild | `16301-16330` | `rebuild addition` | 承接建業南坡，落成入山坡口、松風棧道、風碑岔台與山腰茶棚骨架。 |
| `city_kuaiji` | 會稽 / 山城與門派主城 | `16401-16430` | `rebuild addition` | 承接會稽北口，落成北口山門、會稽主街、坡上市集與門派街口骨架。 |
| `dng_temple_ruins` | 山中古寺 / 古祠地脈 dungeon | `16501-16530` | `rebuild addition` | 承接古祠地脈，落成地脈石梯、滴水甬道、供臺中殿與深封石室前帶骨架。 |
| `wild_river_delta` | 江東水域 / 洲灘渡汊 wild | `16601-16630` | `rebuild addition` | 承接會稽東市，落成出城木棧、分流渡灣、舊樁灘岸與洲心渡口骨架。 |
| `sec_water_ruins` | 水底遺跡 / 裂井殘宮 secret | `16701-16730` | `rebuild addition` | 承接海盜群島外礁深灘，落成裂井落點、沉殿前甬、光紋偏廊與殘宮核心骨架。 |
| `city_xuzhou` | 徐州 / 東線州府 hub | `16801-16820` | `rebuild addition` | 承接陳留東街路標，落成西門甬道、州府十字、市集牌樓、州府前街與南門驛帶骨架。 |
| `road_shouchun_xuzhou` | 淮東官道 / 徐壽驛路 road | `16901-16920` | `rebuild addition` | 承接徐州南門驛口，落成北口驛道、官道中段、路亭歇腳點與南下官道口骨架。 |
| `city_shouchun` | 壽春 / 淮南據點 hub | `17001-17020` | `rebuild addition` | 承接淮東官道南口，落成北門甬道、城心十字、市集牌樓、官署前街與田野外口骨架。 |
| `wild_shouchun_fields` | 壽春田野 / 近郊田埂 wild | `17101-17120` | `rebuild addition` | 承接壽春田野外口，落成田埂岔路、灌渠小橋、曬穀場前與南向土道骨架。 |
| `city_puyang` | 濮陽 / 河北前沿 hub | `17201-17220` | `rebuild addition` | 承接濮陽林野與官渡糧道殘線，落成西門、主街十字、市集、軍務前街與東糧道口骨架。 |
| `road_puyang` | 往濮陽官道 / 中原北行 road | `17301-17320` | `rebuild addition` | 承接洛陽北門與濮陽南驛，落成北郊驛口、官道中段、路亭與盤查坡口骨架。 |
| `city_nanpi` | 南皮 / 河北北段主城 | `17401-17420` | `rebuild addition` | 承接濮陽北路與河北主線，落成南路牌口、主街十字、市集、官署前街與北道牌樓骨架。 |
| `wild_hebei_plain` | 河北平原 / 北地主線 wild | `17501-17520` | `rebuild addition` | 承接南皮東口與更南營道，落成平原外道、風碑岔台、低坡草道與營道前帶骨架。 |
| `fort_river_crossing` | 渡河營寨 / 河渡要地 fort | `17601-17620` | `rebuild addition` | 承接河北平原營道與渡河要地，落成關前營道、寨門、內營主道、軍需棚與望樓骨架。 |
| `road_nanpi_beiping` | 河北北道 / 北地主線 road | `17701-17720` | `rebuild addition` | 承接南皮北道牌樓與北平大通驛站，落成官道中段、路亭與北行坡口骨架。 |
| `road_yijing` | 易京官道 / 北境軍旅 road | `17801-17820` | `rebuild addition` | 承接北平郊區邊關整隊場，落成驛道石坊、路亭與易京前路口骨架。 |
| `fort_yijing` | 易京 / 北境軍鎮 fort | `17901-17920` | `rebuild addition` | 承接易京官道北界，落成前寨口、關門、內營主道、軍需棚與北望樓骨架。 |
| `wild_bailang` | 白狼山 / 山前異域 wild | `18001-18020` | `rebuild addition` | 承接易京東側寨牆，落成碎石坡、狼煙岔脊、風蝕石壇與北狼隘口骨架。 |
| `dng_ancient_cave` | 古洞遺跡 / 洞窟遺封 dungeon | `18101-18120` | `rebuild addition` | 承接白狼山裂縫洞口，落成潮濕前廳、斷紋甬道、封印主室與靈峰裂井骨架。 |
| `wild_barbarian_camp` | 胡營舊地 / 邊地敵蹤 wild | `18201-18220` | `rebuild addition` | 承接白狼山東向荒徑，落成舊柵外口、獸骨火堆、破帳空坪與東向城路口骨架。 |
| `city_xiangping` | 襄平 / 遼東邊城 city | `18301-18330` | `rebuild addition` | 承接胡營舊地東向城路口，落成主街、驛站、太守府前街與北向分流骨架。 |
| `wild_liaodong_plain` | 遼東平原 / 北地開闊 wild | `18401-18420` | `rebuild addition` | 承接襄平北原牌樓，落成外坡、草痕官跡、風草臺與牧馬低帶骨架。 |
| `road_north_border` | 北境邊道 / 遼東北向 road | `18501-18520` | `rebuild addition` | 承接襄平北境邊道路口，落成驛牌、盤查側棚、路亭與北風哨坡骨架。 |
| `fort_northern_watch` | 北方哨樓 / 高處狼煙哨 fort | `18601-18620` | `rebuild addition` | 承接易京北望樓上層，落成升梯接臺、北哨柵門、軍令帶與狼煙高臺骨架。 |
| `wild_wolf_forest` | 狼林 / 深林狼群 wild | `18701-18720` | `rebuild addition` | 承接白狼山北狼隘口，落成枯針松徑、狼骨岔路、霧痕林腹與月嚎空地骨架。 |
| `sec_spirit_peak` | 白狼靈峰 / 高處祭天 secret | `18801-18820` | `rebuild addition` | 承接古洞遺跡靈峰裂井，落成風祭石階、雲裂祭坪、狼紋天壇與天熒觀台骨架。 |
| `sec_starfall_crater` | 星墜天坑 / 墜星異坑 secret | `18901-18920` | `rebuild addition` | 承接白狼山風蝕石壇，落成焦痕坑緣、裂星斜坡、星核碎坪與天隕觀缺骨架。 |
| `wild_hidden_valley` | 隱谷 / 深谷秘徑 wild | `19001-19020` | `rebuild addition` | 承接武陵山隱谷西徑，落成殘碑岔地、靜風谷坪、裂石空場與沉陵坳口骨架。 |
| `dng_ancient_tomb_shu` | 蜀漢古墓 / 石門古墓 dungeon | `19101-19120` | `rebuild addition` | 承接隱谷沉陵坳口，落成前廳石券、斷燈墓道、封紋中庭與內槨石門骨架。 |
| `city_jiangling` | 江陵 / 荊蜀轉接主城 | `19301-19320` | `rebuild addition` | 承接武陵山北山關路，落成南城門、城心十字、西市補給線與西關路口構成的城市 hub。 |
| `fort_yiling` | 夷陵 / 蜀荊咽喉 fort | `19401-19420` | `rebuild addition` | 承接江陵西關，落成關前柵道、夷陵關門、甕城主道與西向關坪構成的主線關隘。 |
| `fort_yongan` | 永安 / 上游堡寨 fort | `19501-19520` | `rebuild addition` | 承接夷陵西關，落成永安柵道、永安堡門、堡門內道與西嶺堡口構成的內層堡壘。 |
| `city_jiangzhou` | 江州 / 上游港城 hub | `19601-19620` | `rebuild addition` | 承接永安西嶺堡口，落成東嶺城門、江州十字、臨江市口、州府前街與西城官道口構成的蜀中上游城市 hub。 |
| `city_chengdu` | 成都 / 蜀漢都城 hub | `19701-19720` | `rebuild addition` | 承接江州西城官道口，落成東城門、錦城十字、市樓牌坊、學舍外街與西郊城關構成的蜀漢都城母城。 |
| `wild_chengdu_outer` | 成都近郊 / 都城西側城外外帶 | `19801-19820` | `rebuild addition` | 承接 `city_chengdu` 西郊城關，落成官道、茶亭、圩田與林地構成的近郊 wild 骨架。 |

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
- `city_jiangxia`：把江夏水道東界正式接進江港主城，透過渡口外門、港前木棧、市集補給與水軍官署把主線重新收束成東岸港務 hub。
- `wild_yunmeng`：把江夏南向水巷正式接進雲夢濕地前帶，透過蘆牆泥道、半乾草洲、石碑泥潭與深沼前帶把主線轉入詭異濕地探索節奏。
- `dng_sunken_temple`：把雲夢深沼正式接進沉沒古廟，透過積水前庭、漏水廊道、封紋中殿與深封井口把主線轉入下探遺跡 dungeon。
- `city_chaisang`：把江夏東向幹道正式接進柴桑，透過西向江門、江岸主街、水行市集與城務前院把主線重新收束成江岸東進的城市 hub。
- `sec_chibi_battlefield`：把柴桑南向赤壁路標正式接進江岸古戰場祕區，透過灰坡、殘艦灘、火痕主陣與祭火高地把節奏切進帶戰痕回聲的 secret battlefield。
- `city_changsha`：把柴桑南向官道正式接進長沙，透過北門、主街、市集補給、官署前街與南門官道把主線重新收束成荊南主城 hub。
- `wild_wuling`：把長沙西牌正式接進武陵山前帶，透過石碑山路、靈木坡面、山腹高徑與霧帶谷口把節奏切進深山 wild。
- `city_lingling`：把長沙南向官道正式接進零陵，透過北門、主街、市集補給、官署前街與南門官道把主線重新收束成更南一段的山城 hub。
- `city_guiyang`：把零陵南向官道正式接進桂陽，透過北門、主街、市集補給、官署前街與南門官道把主線重新收束成南嶺邊地城鎮 hub。
- `wild_nanman_jungle`：把桂陽西岔正式接進南蠻密林前帶，透過濕根主路、圖騰林口、祭柱空地與根台高徑把節奏切進濕熱密林 wild。
- `dng_serpent_temple`：把南蠻密林的林下祠痕正式接進蛇神殿，透過潮濕前廳、蛇紋甬道、滴血祭槽與封紋內殿把節奏切進封閉 dungeon。
- `city_nanhai`：把桂陽南路正式接進南海港城，透過港街、市集補給、港務前街與臨海南口把節奏收束成南境海港 hub。
- `wild_south_sea_route`：把南海臨海南口正式接進近海外航前帶，透過近海棧道、潮石灣、退潮礁坪與外航前帶把節奏切進海路 wild。
- `dng_boat_graveyard`：把南航分水下方的渦潮裂口正式接進沉舟墓場，透過破桅前廊、漏艙窄道、錨鏈井口與墓場深艙把節奏切進海上 wreck dungeon。
- `wild_pirate_islands`：把沉舟墓場外海破舷正式接進海盜群島，透過礁灣主徑、海寇舊寨、風旗高脊與外礁深灘把節奏重新打開成高風險外海 wild。
- `fort_naval_base`：把海盜群島東向暗棧正式接進水軍大營，透過棧門柵關、補給棚區、望樓高位與內港水門把節奏收束成軍事海防 fort。
- `city_jianye`：把水軍大營內港水門正式接進建業，透過南街、中街、市集牌樓、官署前街與港向街口把節奏收束成江東主城 hub。
- `district_jianye_port`：把建業港向街口正式接進建業港區，透過碼頭主道、貨棚泊位、船行牌坊與商船外棧把節奏延伸成商港服務分區。
- `wild_jianye_west`：把建業西坊正式接進建業西郊，透過西坊回道、水圳旁徑、茶亭前坪與更西村路把節奏從主城切回江東水鄉式的城郊外帶。
- `wild_mountain_pass`：把建業南坡正式接進會稽山道，透過入山坡口、松風棧道、風碑岔台與山腰茶棚把節奏從水鄉城郊切進抬升的山路 wild。
- `city_kuaiji`：把會稽北口正式接進會稽城，透過北口山門、會稽主街、坡上市集與門派街口把節奏從山道收束成山城 city hub。
- `dng_temple_ruins`：把古祠地脈正式接進山中古寺，透過地脈石梯、滴水甬道、供臺中殿與深封石室前帶把節奏從山城傳聞切進封閉 dungeon。
- `wild_river_delta`：把會稽東市正式接進江東外水 wild，透過出城木棧、分流渡灣、舊樁灘岸與洲心渡口把節奏從封閉古寺重新打開成可辨位的江汊探索帶。
- `sec_water_ruins`：把海盜群島外礁深灘正式接進水底 secret，透過裂井落點、沉殿前甬、光紋偏廊與殘宮核心把節奏從外海 wild 切進靜壓殘宮。
- `city_xuzhou`：把陳留東街路標正式接進徐州，透過西門、主街十字、市集牌樓、州府前街與南門驛帶把節奏從祕境鏈拉回東線州府與陸路交通 hub。
- `road_shouchun_xuzhou`：把徐州南門驛口正式接進淮東官道，透過北口驛道、路亭前坪、換馬坡口與南下官道口把節奏從州城收束推進成真正的壽春南路旅程。
- `city_shouchun`：把淮東官道南口正式接進壽春，透過北門、城心十字、市集牌樓、官署前街與田野外口把節奏從驛路重新收束成淮南母城與下一段分流 hub。
- `wild_shouchun_fields`：把壽春田野外口正式接進近郊 wild，透過田埂岔路、灌渠小橋、曬穀場前與南向土道把節奏從城內秩序鬆開成可辨位的外郊前帶。
- `city_puyang`：把濮陽林野與官渡糧道之間的缺口正式補成前沿主城，透過西門、城心十字、市集、軍務前街與東糧道口把河北前線的補給與軍旅節奏重新收束成城市 hub。
- `road_puyang`：把洛陽北門與濮陽南驛之間的抽象 world link 正式補成北行官道，透過北郊驛口、路牌石、路亭與盤查坡口把長路節奏重新接回中原主線。
- `city_nanpi`：把濮陽北路正式接進河北主城，透過南路牌口、主街、市集、官署前街與北道牌樓把前沿壓力轉成更有地方勢力感的北方城市節奏。
- `wild_hebei_plain`：把南皮東口正式接進河北平原，透過官道平野、風碑岔台、低坡草道與營道前帶把北地主線重新打開成開闊的平原 wild。
- `fort_river_crossing`：把河北平原南向營道正式接進渡河營寨，透過關前營道、寨門、內營主道、軍需棚與望樓把平原節奏重新收束成河渡要地的 fort。
- `road_nanpi_beiping`：把南皮北道牌樓正式接進河北北道，透過官道中段、里程石、路亭與北行官道口把河北主線重新拉長成往北平去的旅途節奏，並先以北平大通驛站作為 legacy travel anchor。
- `road_yijing`：把北平郊區邊關整隊場正式接進易京官道，透過驛道石坊、換班木樁、路亭與易京前路口把北平北境外帶再往軍鎮前線推進一層，並已正式銜接 `fort_yijing`。
- `fort_yijing`：把易京官道北界正式收束成北境軍鎮關隘，透過前寨口、關前柵道、易京關門、軍需棚與北望樓把北境主線從 road 切進真正的 fort choke point，並已正式銜接 `wild_bailang`。
- `wild_bailang`：把易京東側寨牆正式接進白狼山前帶，透過碎石坡、風裂石徑、狼煙岔脊、裂縫洞口與北狼隘口把北境主線從軍鎮秩序切進邊山探索 wild。
- `dng_ancient_cave`：把白狼山裂縫洞口正式接進古洞遺跡，透過裂縫落台、潮濕前廳、斷紋甬道、石門前廊與封印主室把北境主線再往地下遺跡壓深一層。
- `wild_barbarian_camp`：把白狼山東向荒徑正式接進胡營舊地，透過斷草營徑、風旗殘道、獸骨火堆與巡望高臺把北境主線重新拉回帶人為敵蹤記憶的 hostile wild。
- `city_xiangping`：把胡營舊地東向城路口正式接進襄平，透過西城路口、主街、驛站前街、藥材行前與太守府前街把北境主線重新收束成可整補、訓練與北向分流的遼東邊城 hub。
- `wild_liaodong_plain`：把襄平北原牌樓正式接進遼東平原，透過北原外坡、草痕官跡、遼東平野、風草臺與牧馬低帶把北境主線重新打開成可辨位的開闊北地 wild。
- `road_north_border`：把襄平北境邊道路口正式接進北境邊道，透過驛牌木樁邊、北境官道中段、盤查側棚、路亭前坪與北風哨坡把北境主線重新收成更有軍務秩序感的 road。
- `fort_northern_watch`：把易京北望樓正式接進更高處的北方哨樓，透過升梯接臺、北哨柵門、軍令木案、糧箭棚與狼煙高臺把北境主線再往上抬成更純粹的前線 watch fort。
- `wild_wolf_forest`：把白狼山北狼隘口正式接進狼林，透過枯針松徑、狼骨岔路、霧痕林腹、失蹤者舊營與月嚎空地把北境主線切進更封閉也更偏 folklore 的深林 wild。
- `sec_spirit_peak`：把古洞遺跡的靈峰裂井正式接進白狼靈峰，透過風祭石階、雲裂祭坪、狼紋天壇、靈泉祭井與天熒觀台把北境主線切進更高處也更稀有的祭天祕境。
- `sec_starfall_crater`：把白狼山風蝕石壇正式接進星墜天坑，透過焦痕坑緣、裂星斜坡、星核碎坪、殞光裂庭與天隕觀缺把北境主線切進更焦灼也更失衡的墜星祕境。
- `wild_hidden_valley`：把武陵山隱谷西徑正式接進隱谷，透過殘碑岔地、伏苔斷階、靜風谷坪、裂石空場與沉陵坳口把蜀漢西山鏈切進更收束也更帶古痕壓力的深谷 wild。
- `dng_ancient_tomb_shu`：把隱谷沉陵坳口正式接進蜀漢古墓，透過沉陵落階、前廳石券、斷燈墓道、封紋中庭與內槨石門把蜀地深谷主線切進封閉石門 dungeon。
- `wild_spirit_forest`：把武陵山東岔靈林正式接進靈木森林，透過藤影小徑、古碑風根地、靈木空場、懸藤高台與青燐深處把蜀地西山鏈重新打開成仙俠 wild 支線。
- `city_jiangling`：把武陵山北山關路正式接進江陵，透過南城門、入城大道、城心十字、西市補給線與西關路口把蜀地山林節奏重新收束成荊蜀轉接主城。
- `fort_yiling`：把江陵西關路口正式接進夷陵，透過關前柵道、夷陵關門、甕城主道、軍需棚區與西向關坪把城市節奏再收束成蜀荊咽喉的主線 fort。
- `fort_yongan`：把夷陵西向關坪正式接進永安，透過永安柵道、永安堡門、堡門內道、軍械棚區與西嶺堡口把邊界軍旅再收成更厚重的上游堡寨 fort。
- `city_jiangzhou`：把永安西嶺堡口正式接進江州，透過東嶺城門、江州十字、臨江市口、州府前街與西城官道口把蜀地上游主線重新收束成城市 hub。
- `city_chengdu`：把江州西城官道口正式接進成都，透過東城門、入城御道、錦城十字、市樓牌坊、學舍外街與西郊城關把蜀地上游主線重新收束成蜀漢都城母城。
- `wild_chengdu_outer`：把成都西郊城關正式接進成都近郊，透過城關外坡、西郊官道、茶亭前坪、圩田路肩、路旁林地與更西官道把都城節奏重新鬆開成可辨位的近郊 wild。

## 維護規則

- 若 runtime 新增、移除或重排 area，應同步更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`。
- 若重建區有新的 `map.md`、world link 或 room block 變更，優先以 `area/directory.lst`、`area/<area>/index`、`plans/area/*.md` 與 `area/rebuild_plan.md` 為準再回寫這份文件。
