---
layout: default
title: Area VNUM Policy
---

# Area VNUM Policy

這份文件整理新 AREA 的 room VNUM 保留規則，目標是降低房號衝突、避免跨區混用號段，並讓 spec-first area 在第一版落地後仍保有擴充空間。

總覽仍以 [AREA 開發手冊](./area-development-handbook.html) 與 `plans/0001-world-map-area-rebuild.md` 為準；這份文件專注在 `reserved_room_block`、`planned_vnum_range` 與 extension block。

## Core Policy

新 AREA 的第一段 room 保留區，預設採「某個新百位段的 `xx01` 起跳」策略。

設計目的：

- 讓保留段可讀、可追蹤
- 保留首版之後的 headroom
- 延續 repo 既有 `501`、`9001`、`9101` 這種起號習慣
- 避免未來每次擴房都被迫重編整區

## Reservation Rules

建立新 area 時，至少要先固定：

- `reserved_room_block`
- `planned_vnum_range`

規則如下：

- 第一段 `reserved_room_block` 必須從某個 `xx01` 開始
- block 大小用「首版預估房數 + 至少 8 格 headroom」後往上取到最近的 `10`
- block 結尾採整十收尾，例如 `9501-9520`、`9601-9630`
- 若估算後會跨出同一百位段，就改用下一個百位段的 `xx01`
- `planned_vnum_range` 預設宣告整段保留區，而不是只寫到當前最後一號
- `mapmd-json` 內實際使用的 room vnum 不必連號，但同一輪新 area 預設應先落在同一個保留段內

## Extension Blocks

extension block 不是禁止，但應視為例外而非常態。

只在下列情況下使用：

- 原本首段保留區已用完
- 單區 plan 已明確說明原因
- `map.md` metadata 已同步
- tracker 已同步記錄

extension block 規則：

- 不要把 extension block 寫成臨時口頭決定
- 優先保持區內的可理解分段
- 若可能，仍採整十收尾
- 不要把 extension block 當成一開始就能無限分裂的預設設計

## Existing Exceptions

repo 內已有一些歷史遺留切段，例如 `9451/9461/9481/9491` 這類地下鏈分段。

對這些既有區域的處理原則：

- 保留現狀
- 不為了符合新政策而硬重編既有 area
- 但未來新 area 不再沿用同一百位拆給多區的做法

## Allocation Workflow

在真正選定新 block 前，至少檢查下列範圍：

- `area/`
- `area/directory.lst`
- `plans/area/*.md`
- `src/`
- `data/`

最低流程：

1. 估算首版房數
2. 加上至少 8 格 headroom
3. 向上取到最近的 `10`
4. 從新百位段的 `xx01` 選 block
5. 搜尋 repo 內是否有衝突
6. 把結果寫入單區 plan 與 tracker

## Directory Comment Rule

若新 area 已進入 loadable runtime 狀態，`area/directory.lst` 的房號註解應反映首段保留區，而不是只反映目前實作到的最後一號。

這是為了讓後續維護者能直接看出：

- 這區本來保留多少擴充空間
- 哪些房號仍屬於同一個 area 規劃邊界

## Relationship To Capital

room VNUM 保留規則與 `Capital` 是不同議題，但新 area 常一起被誤判。

補充共識：

- 新 AREA 預設 `Capital 0`
- 只有當 area 被明確設計成出生地、首都或系統級 home 候選時，才考慮非零 `Capital`
- 城郊、外野、地下入口前哨這類過渡區，不應因為是新 area 就自動進入出生地清單

## Required Writeback

只要本輪有新 area 或 block 變更，至少回寫：

- `plans/area/NNNN-area-slug.md`
- `area/rebuild_plan.md`
- `area/<area>/map.md` metadata
- `area/directory.lst` 註解

## Relationship To Other Docs

- 流程總覽： [docs/area-development-handbook.md](./area-development-handbook.html)
- 世界接線： [docs/area-external-exit-policy.md](./area-external-exit-policy.html)
- 全局規則： `plans/0001-world-map-area-rebuild.md`
