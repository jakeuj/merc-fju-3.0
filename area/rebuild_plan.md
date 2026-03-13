# Area Rebuild Tracker

這份檔案是 area 重建的日常追蹤看板，配合 `plans/` 內的正式計畫一起使用。

## References

- 全局計畫：`plans/0001-world-map-area-rebuild.md`
- 單區計畫：`plans/area/0002-loyang-outskirts.md`
- 世界圖參考：`area/world_map.md`

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

執行規則：

- 若 `in_progress` 區塊有項目，優先續做該區
- 否則從 `todo` 區塊選第一個沒有 blocker 的 area
- 若當前區塊完成，更新本檔後再移動到下一區

## Candidate Queue

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`

## Todo

### `loyang_outskirts`

- status: `todo`
- plan: `plans/area/0002-loyang-outskirts.md`
- parent_region: `loyang`
- world_links: `洛陽東郊`, `龍渠丘陵`, `洛陽地下水區入口`
- next_action: 建立 `area/loyang_outskirts/map.md` 第一版 spec 草案
- notes: 第一個正式新 AREA，目的是驗證 spec-first `map.md -> mapmd-json -> .roo`

### `beiping_outskirts`

- status: `todo`
- plan: `not created yet`
- parent_region: `beiping`
- world_links: `北平郊區`, `易京`, `白狼山`
- next_action: 在 `loyang_outskirts` 穩定後建立單區計畫檔
- notes: 北方交通與邊關混合型候選

### `jingxiang_road`

- status: `todo`
- plan: `not created yet`
- parent_region: `future regional chain`
- world_links: `襄陽`, `新野`, `江夏`, `荊襄大道`
- next_action: 等 `loyang_outskirts` 與 `beiping_outskirts` 後再評估
- notes: docs 依據足夠，但 repo 內尚未有直接母城 area，成本較高

## In Progress

- none

## Done

- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `plans/0001-world-map-area-rebuild.md` 已建立
- `plans/area/0002-loyang-outskirts.md` 已建立

## Blocked

- none

## Current Recommended Next Step

建立 `area/loyang_outskirts/map.md` 的第一版 spec 草案。

建議可直接使用的 prompt：

`根據 plans/area/0002-loyang-outskirts.md 與 area/world_map.md，建立 area/loyang_outskirts/map.md 的第一版 spec 草案。`
