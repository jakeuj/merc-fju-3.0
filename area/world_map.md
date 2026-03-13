# Merc-FJU World Map Reference

這份檔案是給 area 規劃與 `map.md` spec-first 設計使用的世界地圖參考，不是 runtime 載入檔。

## Sources

- `help/map.hlp`
- `docs/3yWebsite/docs/maps.md`
- `docs/3yWebsite/docs/data/maps.json`
- `docs/3yWebsite/map/index.html`
- `docs/3yWebsite/map/loyang.html`
- `docs/3yWebsite/map/bepin.html`

## Purpose

- 給新 AREA 規劃時當世界拓樸參考
- 幫助判斷 `Serial` / `Capital` / 交通節點 / 城市外郊的相對位置
- 讓 `area/<new_area>/map.md` 可以先站在世界圖上決定自己接在哪裡
- 用 `maps.json` 確認 docs 目前實際有整理過哪些城市圖與交通摘要

## World Skeleton

以下主骨架整理自 `help/map.hlp` 與 `docs/3yWebsite/map/index.html`：

```text
西涼 - 天水 - 安定 - 長安 - 弘農 - 洛陽 - 陳留 - 徐州
                     |      |      |
                     |      |      + 壽春 - 建業 - 會稽
                     |      |
                     |      + 濮陽 - 南皮 - 北平 - 襄平
                     |
                     + 宛 - 新野 - 襄陽 - 江夏 - 柴桑
                                    |
                                    + 長沙 - 零陵 - 桂陽 - 南海

成都 - 江州 - 永安 - 江陵 - 武陵 - 長沙
```

`docs/3yWebsite/docs/data/maps.json` 的 `map/index.html` 摘要也對應同一張世界圖，因此目前 docs 的 HTML 與 JSON 在世界主骨架上是一致的。

## Lettered World Connectors

`help/map.hlp` 內的字母節點可以當成 world choke point / pass / battlefield 的規劃提示：

- `H` 函谷關：長安與中原之間的重要關卡
- `V` 虎牢關：弘農 / 洛陽一帶的重要門戶
- `R` 易京：北平外圍的北方節點
- `S` 白狼山：遼東 / 襄平方向的邊境節點
- `U` 夷陵：蜀漢往荊州方向的咽喉

這些點很適合做成：

- 單向或強守備的 `one_way` / gate-style topology
- 戰場型 area
- 城郊與主城之間的轉接 area

## City And Surrounding Hints

`docs/3yWebsite/map/index.html` 還列出「城市的周邊」：

- 洛陽東郊
- 陳留西郊
- 洛陽地下水區
- 北平郊區
- 龍渠丘陵
- 封丘森林
- 朱仙鎮
- 樊城
- 平原外草原
- 荊襄大道
- 白狼山
- 建業西郊
- 雲夢大澤

這些名稱很適合拿來當新 AREA 候選，因為它們天生就是「已知主城或主幹線外的一塊相鄰區域」。

## JSON Coverage Snapshot

`docs/3yWebsite/docs/data/maps.json` 目前已整理的 `map/*.html` 摘要至少包含：

- 世界索引：`map/index.html`
- 巴士：`map/bus.html`
- 現有或可參考主城：`loyang`、`bepin`、`chanan`、`chenliu`、`honlon`
- 其他城市：`jinyang`、`puyang`、`nanpi`、`xiangping`、`sinya`、`sochu`、`janya`、`quaji`
- 西南與荊州系：`chendo`、`chansa`、`jansha`、`shanyan`
- 特殊區域：`heaven`、`rohan`

這表示未來若要做 world-aware 的新 AREA 規劃，不只可以參考靜態 HTML，也可以直接把 `maps.json` 當成「目前 docs 已收錄地圖節點清單」。

## Bus And Traffic Notes From JSON

`maps.json` 內的 `map/bus.html` 摘要和 `docs/maps.md` 的巴士表一致，目前可直接確認的驛站節點有：

- 洛陽春水站
- 弘農驛站
- 陳留驛站
- 長安驛站
- 北平驛站
- 襄平驛站
- 襄陽驛站
- 新野驛站
- 壽春驛站
- 晉陽驛站

因此若要挑第一個新 AREA，最穩的策略是優先選：

- 已有現存 repo area 可接
- 又同時在 `maps.json` / `maps.md` / `map/index.html` 都有痕跡的節點

這也是目前 `loyang_outskirts` 與 `beiping_outskirts` 會排在前面的原因。

## Existing Repo Areas

目前 repo 內正式存在的 area：

- `loyang`
- `beiping`
- `new`
- `newfight`
- `pk_area`
- `free_fight`
- `limbo`

其中和世界地圖直接對得上的主城級 area 主要是：

- `loyang`
- `beiping`

因此，第一批新 AREA 最適合從「現有主城旁邊的外郊 / 轉接帶」開始；這樣同時滿足 repo 現況與 `maps.json` 的 coverage。

## Current City References

### Loyang

`docs/3yWebsite/map/loyang.html` 顯示洛陽城內部已有明確服務節點：

- 皇宮入口
- 武器店
- 防具店
- 道具店
- 藥品店
- 銀行
- 鏢局
- 鐵匠
- 馬房
- 下水道入口
- 軍營

這表示洛陽很適合作為外郊 AREA 的母城，因為：

- 玩家補給鏈完整
- 問路點與服務點容易對上 `#Enquire`
- 能自然延伸出「東郊 / 地下水區 / 龍渠丘陵」這些相鄰新圖
- `maps.json` 也已有 `map/loyang.html` 摘要，可作為 docs-aligned 依據

### Beiping

`docs/3yWebsite/map/bepin.html` 顯示北平目前可辨識節點有：

- 天津渡口
- 八仙飯店
- 車站
- 永定渡口
- 紫禁城
- 糧倉
- 楓橋殿
- 往易京方向出口

這表示北平很適合作為：

- 北方交通樞紐
- 驛站 / 渡口 / 邊關型 area 的母城
- 通往易京 / 白狼山 / 襄平支線的入口
- `maps.json` 也已有 `map/bepin.html` 摘要，可作為 docs-aligned 依據

## Recommended First New Area Candidates

### Candidate A: `loyang_outskirts`

建議優先度：最高

理由：

- 直接貼著現有 `loyang`
- `docs/3yWebsite/map/index.html` 已明列 `洛陽東郊`
- `maps.json` 已收錄 `map/loyang.html` 與 `map/bus.html` 摘要
- 可自然延伸到 `龍渠丘陵`、`洛陽地下水區`
- 很適合拿來驗證 spec-first `map.md -> .roo` 工作流

建議主題：

- 城郊道路
- 農田 / 水渠 / 丘陵
- 通往地下水區的入口
- 低到中等級野外怪區
- 一到兩個可問路節點，例如回城牌亭、巡邏哨、渡口口

建議世界連接：

- west / enter: 回洛陽城
- east: 通往龍渠丘陵
- down: 通往洛陽地下水區

### Candidate B: `beiping_outskirts`

建議優先度：高

理由：

- 直接貼著現有 `beiping`
- `docs/3yWebsite/map/index.html` 已明列 `北平郊區`
- `maps.json` 已收錄 `map/bepin.html` 與 `map/bus.html` 摘要
- 還能往 `易京`、`白狼山` 方向擴充
- 適合做驛站、邊關、補給與野外路線混合區

建議主題：

- 北門外官道
- 驛站 / 車站 / 渡口分流
- 邊境哨站
- 通往山地或草原的外圍帶

### Candidate C: `jingxiang_road`

建議優先度：中

理由：

- `荊襄大道` 是天然幹道型新 area 題材
- `maps.json` 已收錄 `map/shanyan.html`、`map/sinya.html`、`map/jansha.html`
- 可串 `襄陽`、`新野`、`江夏` 等節點
- 但目前 repo 尚未有這些母城 area，落地成本比 A/B 高

## Recommendation

若目標是「先用一個新 AREA 驗證剛做好的 plan」，建議從下面順序選：

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`

其中最適合作為第一個正式範例的是 `loyang_outskirts`，因為它同時滿足：

- 有現成母城 `loyang`
- 有 docs 明示的世界位置
- 有服務點與 `#Enquire` 場景
- 很容易做出 `enter/out`、`up/down`、平面道路並存的 3D spec

## Suggested Next Step

若要正式開始第一個新 AREA，建議直接建立：

- `area/loyang_outskirts/map.md`

然後在 `map.md` 內先定義：

- 與洛陽的連接方式
- 東郊主幹道
- 丘陵支線
- 地下水區入口
- 至少一個 `#Enquire` 節點
- 至少一個 `enter/out` 或 `up/down` 的非平面連線
