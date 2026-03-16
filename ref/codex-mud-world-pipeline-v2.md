# Codex + MUD World Building Pipeline v2

本文件是進階版的 **Codex + MUD 世界建設流程**， 目標是支援 **大型世界
(100+ AREA)** 的半自動生成與驗證。

設計目標：

-   Spec‑First World Design
-   AI Agent 可續跑
-   World Consistency 自動檢查
-   CI 可驗證

------------------------------------------------------------------------

# Pipeline Architecture

World Graph ↓ Area Queue ↓ Area Spec ↓ Code Generator ↓ Runtime
Validation ↓ PR + Merge ↓ Next Area

------------------------------------------------------------------------

# 1 World Graph Layer

世界結構由人工維護。

主要檔案：

-   world-graph.json
-   area/world_map.md
-   題材分布表.md

用途：

-   定義區域連線 topology
-   定義 theme 分布
-   定義探索 progression

範例：

loyang ↓ loyang_outskirts ↓ wild_longqu_hills ↓ dng_loyang_sewer

Agent 不允許直接修改 world graph。

------------------------------------------------------------------------

# 2 Area Queue

Queue 由

area/rebuild_plan.md

管理。

狀態：

todo in_progress done blocked

固定 Prompt：

「繼續實作下一個待建 area」

Agent 行為：

if in_progress exists → continue

else → pick first todo

------------------------------------------------------------------------

# 3 Area Plan

每個 area 一個 plan：

plans/area/XXXX-area.md

包含：

-   theme
-   subtheme
-   reserved_room_block
-   vnum_range
-   external links

用途：

避免 AI invent 世界設定。

------------------------------------------------------------------------

# 4 Area Spec

area/`<area>`{=html}/map.md

包含：

Narrative Zone Layout Cluster Design Gameplay Intent

machine readable spec：

mapmd-json

------------------------------------------------------------------------

# 5 Generator

Generator script：

generate_roo_from_map_md.py

輸出：

roo mob obj res shp

------------------------------------------------------------------------

# 6 Implementation

AI 補充：

NPC shop reset dialogue

更新：

area/directory.lst

------------------------------------------------------------------------

# 7 Runtime Validation

必做 smoke test。

檢查：

log/*.log debug/*

自動檢測：

duplicate vnum parse error Load_room

------------------------------------------------------------------------

# 8 Delivery Gates

spec_in_progress spec_ready_for_commit implementation_in_progress
implementation_ready_for_commit validated_ready_to_advance

只有 validated_ready_to_advance 才允許開始下一區。

------------------------------------------------------------------------

# 9 Git Workflow

branch：

codex/area-`<name>`{=html}

每個 AREA 一個 PR。

Example：

PR #21 Add area loyang_outskirts PR #22 Add area wild_longqu_hills

------------------------------------------------------------------------

# 10 Codex Task Strategy

每個 Task 只處理一個 AREA。

流程：

generate spec generate roo validate commit PR

------------------------------------------------------------------------

# 11 World Consistency Checker

建議新增工具：

world-check.py

檢查：

duplicate vnum orphan exits unreachable room broken exit links

------------------------------------------------------------------------

# 12 Graph Diff

每個 PR 自動生成 world graph diff。

Example：

Before

loyang → gate

After

loyang → outskirts → hills

------------------------------------------------------------------------

# 13 CI Pipeline

CI 建議流程：

build merc ↓ load area ↓ smoke test ↓ world validation

------------------------------------------------------------------------

# 14 Recommended Cadence

1 AREA / Task 1 PR / AREA

Example：

Day1 loyang_outskirts Day2 wild_longqu_hills Day3 dng_loyang_sewer

------------------------------------------------------------------------

# 15 Agent Loop

Agent 執行：

read rebuild_plan.md → pick next area → load area plan → generate spec →
generate roo → validate → commit

------------------------------------------------------------------------

# Summary

最佳流程：

World Graph ↓ Area Plan ↓ Area Spec ↓ Generate Data ↓ Runtime Test ↓ PR
↓ Next Area

此 pipeline 可支援 **100+ AREA 世界建設**。
