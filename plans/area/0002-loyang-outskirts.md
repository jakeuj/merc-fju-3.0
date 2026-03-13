# Loyang Outskirts Initial Area Plan

## Summary

建立第一個正式的新 AREA：`loyang_outskirts`。這個區域是 `loyang` 的母城外郊延伸，用來驗證 `map.md -> mapmd-json -> .roo` 的 spec-first 流程。

## Design Intent

- 承接洛陽主城外部動線
- 表現 `洛陽東郊`、`龍渠丘陵`、`洛陽地下水區入口` 的相鄰關係
- 讓玩家從主城服務鏈自然走到野外與地下入口
- 在第一版就包含平面道路與至少一條非平面連線

## Theme Positioning

- theme: `歷史城市風`
- subtheme: `軍旅風`
- 世界缺口角色：補足主城外郊、巡邏線、田野與地下入口的過渡帶

題材落地原則：

- 主骨架是洛陽近郊與官道感，不做純野外荒地
- 輔以巡邏哨、路亭、田埂、水渠、告示與軍情壓力
- 房間描述、問路詞、NPC 口吻與支線鉤子都要維持同一語氣

## Initial Scope

第一版只做 `map.md` 規格草案，不直接要求完整 `mob/obj/res/shp`。

最小可行內容：

- 一條東郊主幹道
- 一條丘陵或田野支線
- 一個地下入口或水路入口
- 至少一個 `#Enquire` 節點
- 至少一個 `enter/out` 或 `up/down` 連線

## World Links

建議世界連接：

- `west` 或 `enter`：回洛陽城
- `east`：通往龍渠丘陵
- `down`：通往洛陽地下水區

## Required Spec Content

`area/loyang_outskirts/map.md` 應包含：

- 區域用途與玩家流向 prose
- `mapmd-json` graph schema
- room clusters
- world links
- 主要服務 / 問路點
- 需要 `#Keyword`、`#Job`、`#Enquire` 的節點說明

## Reference Entry Points

在開始寫這個 area 的 `map.md` 前，優先從 `ref/Readme.md` 進入下列參考：

- `area-template-wild_loyang_east.md`
- `sanguo-area-specfirst/` 中相近的 `wild_*` 節點
- 必要時再補 `sanguo-area-scaffold/`

本輪先不使用：

- `mud-world-builder/` 與其他 editor / generator 原型
- 經濟、勢力、歷史事件、NPC 生態等模擬系統原型

原因：

- `loyang_outskirts` 第一版目標是完成 `map.md` 拓樸與題材草案
- 還沒進入工具化生成、經濟模擬或動態事件階段

## Suggested Room Clusters

- `city-edge`
- `east-road`
- `canal-fields`
- `dragon-channel-hills`
- `underground-entry`

## Suggested Theme Hooks

- `city-edge`
  - 主題感：城門外緩衝帶、回城導流、官道秩序
- `east-road`
  - 主題感：巡邏線、告示、路亭、行旅與軍情風聲
- `canal-fields`
  - 主題感：洛陽近郊農田、水渠、民居與補給感
- `dragon-channel-hills`
  - 主題感：從城市秩序過渡到較危險的丘陵地帶
- `underground-entry`
  - 主題感：潮濕、封閉、可疑入口，作為地下水區前哨

## First-Round Validation

- `mapmd-json` 可被 scaffold script `--validate-only` 接受
- 合法方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非刻意標示 `one_way`
- `#Enquire` 節點對應到玩家可理解的問路詞
- 主題檢查通過：房間、NPC、`#Enquire`、`#Keyword` 與 cluster 語氣一致，不偏成純江湖或純仙俠

## Next Step Prompt

當這份計畫成為當前目標時，可直接使用：

`根據 plans/area/0002-loyang-outskirts.md、area/world_map.md 與 ref/Readme.md，建立 area/loyang_outskirts/map.md 的第一版 spec 草案。`

## Assumptions

- `loyang` 仍是現有母城，不在這一輪重建範圍內
- 第一版重點是 topology 與 room-spec intent，不是完整內容量產
- 地下水區在第一版可以先作為入口節點，不必一次做完整地下區域

## Implementation Outcome

`loyang_outskirts` 已完成第一個可整合的實作里程碑，驗證了這條流程：

`plan -> map.md -> mapmd-json -> .roo scaffold -> mob/obj/res/shp -> directory integration -> smoke test`

本次實際落地內容：

- 建立 `area/loyang_outskirts/map.md`
- 以 generator 產生 `roo/7501-7512.roo`
- 補上最小 `index`、`mob`、`obj`、`res`、`shp`
- 將 `loyang_outskirts` 掛入 `area/directory.lst`
- 把 `loyang/556` 與 `loyang_outskirts/7501` 接成正式邊界出口
- 在 WSL 內用 `./merc merc.ini` 做 smoke test，成功跑到「開始正常運作」

## Lessons From This Case

- `mapmd-json` 不能只描述 area 內部互連；第一個正式新 area 落地後，已證明需要支援 external exit，才能把 spec 當成真正的 source of truth
- `delivery_gate` 很重要：如果沒有它，固定 prompt 很容易在 area 還該 commit 或還在整合時，就誤跳下一區
- reset parser 比文件更保守；像 `.res` 結尾和空白行這種細節，最好優先比對現有 repo 內可正常載入的範例
- WSL smoke test 足以把「資料載入錯誤」和「只是常駐程式被 timeout 終止」清楚分開

## Recommended Next Implementation Scopes

若後續仍留在 `loyang_outskirts`，優先考慮：

- 把 `east` 方向正式接到未來 `龍渠丘陵`
- 把 `down` 方向正式接到未來 `洛陽地下水區`
- 視需要補更多 reset、服務 NPC、戰鬥遭遇與地圖提示

若 `delivery_gate` 已改成可前進下一區，則下一個候選應回到 `beiping_outskirts`
