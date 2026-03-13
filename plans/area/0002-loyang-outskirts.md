# Loyang Outskirts Initial Area Plan

## Summary

建立第一個正式的新 AREA：`loyang_outskirts`。這個區域是 `loyang` 的母城外郊延伸，用來驗證 `map.md -> mapmd-json -> .roo` 的 spec-first 流程。

## Design Intent

- 承接洛陽主城外部動線
- 表現 `洛陽東郊`、`龍渠丘陵`、`洛陽地下水區入口` 的相鄰關係
- 讓玩家從主城服務鏈自然走到野外與地下入口
- 在第一版就包含平面道路與至少一條非平面連線

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

## Suggested Room Clusters

- `city-edge`
- `east-road`
- `canal-fields`
- `dragon-channel-hills`
- `underground-entry`

## First-Round Validation

- `mapmd-json` 可被 scaffold script `--validate-only` 接受
- 合法方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非刻意標示 `one_way`
- `#Enquire` 節點對應到玩家可理解的問路詞

## Next Step Prompt

當這份計畫成為當前目標時，可直接使用：

`根據 plans/area/0002-loyang-outskirts.md 與 area/world_map.md，建立 area/loyang_outskirts/map.md 的第一版 spec 草案。`

## Assumptions

- `loyang` 仍是現有母城，不在這一輪重建範圍內
- 第一版重點是 topology 與 room-spec intent，不是完整內容量產
- 地下水區在第一版可以先作為入口節點，不必一次做完整地下區域
