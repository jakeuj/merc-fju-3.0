---
layout: default
title: Area Development Handbook
---

# Area Development Handbook

這份文件是 `merc-fju-3.0` 新 AREA / AREA rebuild 工作流的正式人類可讀入口，用來整理 spec-first 區域開發的骨架、權責分工、固定交付節奏與最低驗證要求。

它的目標不是取代 repo 內既有規則來源，而是把分散在 `AGENTS.md`、`plans/`、`area/rebuild_plan.md`、skill reference 與現行 docs 的共通流程收斂成一份可回讀的 handbook。

## Scope

這份 handbook 適用於下列工作：

- 新 AREA 規劃與重建
- `plans/area/*.md` 單區計畫
- `area/<area>/map.md` spec-first 設計
- `.roo` scaffold 與 runtime area data 落地
- world links、external exits、boundary room 同步
- area rebuild tracker 與固定 prompt 接續

不適用或只作補充索引的範圍：

- `docs/3yWebsite/`
  - 舊站鏡像與 reference baseline，不是現行 runtime source of truth
- `docs/current-game/*`
  - 現行 area / skill registry 的補充文件，不取代 runtime 與 planning 檔
- 單純技能 loader、啟動腳本或平台建置細節
  - 仍以對應 skill、`AGENTS.md` 與 repo 實際檔案為準

## Source Of Truth Order

若不同文件之間看起來有重疊，預設依下列順序判定：

1. `AGENTS.md`
   - repo 級規則、area rebuild 約束、驗證範圍與環境慣例
2. `plans/0001-world-map-area-rebuild.md`
   - 全局 area rebuild 流程、delivery gate、固定 prompt、roadmap
3. `area/rebuild_plan.md`
   - 日常追蹤狀態、next actionable area、當前 `delivery_gate`
4. `plans/area/NNNN-area-slug.md`
   - 單區題材、world links、保留房號與驗證意圖
5. `area/<area>/map.md`
   - 單區人類可讀 spec；其中嵌入的 `mapmd-json` 是 machine-readable canonical graph
6. runtime 與 loader 事實來源
   - `area/directory.lst`
   - `area/<area>/index`
   - `area/<area>/roo/*`
   - `src/load.c`
   - `src/act_move.c`
7. 補充說明與 reference
   - `ref/Readme.md`
   - `docs/current-game/*`
   - `docs/3yWebsite/*`

補充規則：

- 若 `map.md` prose 和 `mapmd-json` 衝突，generator 一律以 `mapmd-json` 為準，再回頭修 prose
- 若 `docs/current-game/areas.md` 與 runtime 不一致，仍以 runtime 與 planning 檔案為準，再回寫 docs
- 若新規則尚未寫進 repo 的 authoritative docs，就不能只靠口頭習慣當成硬規則

## Workflow Layers

AREA 開發 pipeline 固定拆成七層：

1. `World Graph`
   - 用 `area/world_map.md` 與 `ref/Readme.md` 決定世界位置、母城掛接與題材缺口
2. `Area Queue`
   - 用 `area/rebuild_plan.md` 決定目前要做哪一區
3. `Area Plan`
   - 用 `plans/area/NNNN-area-slug.md` 固定單區邊界、外部連線、題材與驗證目標
4. `Area Spec`
   - 用 `area/<area>/map.md` 描述 narrative spec 與 `mapmd-json`
5. `Projection + Implementation`
   - 用 generator 投影 `.roo`，再補 `index / mob / obj / res / shp / boundary rooms`
6. `Runtime Validation`
   - 用 build、smoke test、`log/*`、`debug/*` 驗證 area 可載入
7. `Commit / Merge Gate`
   - 只有 `delivery_gate` 允許時，才可 commit、結束當前 milestone 或進下一區

## File Roles

各層主要檔案職責如下：

- `plans/0001-*.md`
  - 全局策略、候選排序、長期規則與 systemization roadmap
- `plans/area/NNNN-area-slug.md`
  - 單區設計意圖、保留房號、external links、題材定位、驗證目標
- `area/rebuild_plan.md`
  - 日常追蹤看板，保存 `todo / in_progress / done / blocked / next_action / next_prompt / delivery_gate`
- `area/<area>/map.md`
  - 單區 spec，兼具人類可讀敘事與 machine-readable `mapmd-json`
- `area/directory.lst`
  - area 載入順序與 loadable runtime registry
- `docs/current-game/areas.md` / `docs/current-game/areas.json`
  - 現行 runtime area registry 的補充說明，只有在 runtime area 真正新增、移除、重排時才同步更新

## Fixed Prompt And Queue Discipline

長期接續 area rebuild 使用固定主 prompt：

`繼續實作下一個待建 area`

執行規則：

1. 先讀 `area/rebuild_plan.md`
2. 若有 `in_progress`，優先續做該區
3. 否則選第一個沒有 blocker 的 `todo`
4. 再讀對應的 `plans/area/NNNN-*.md`
5. 若需要世界層背景，再讀 `area/world_map.md` 與 `ref/Readme.md`

語意規則：

- 這裡的 `next area` 指的是 next actionable area，不是 candidate order 的下一個新名字
- 只要仍有 `in_progress` area，就不得自行跳去下一個 `todo`
- 若當前 area 仍卡在 `spec_ready_for_commit` 或 `implementation_ready_for_commit`，應先 commit，而不是切下一區
- 若 `delivery_gate` 是 `blocked`，應先處理 blocker，不得把做下一區當成繞路

## Single Unit Of Work

預設工作單位是「一輪任務只處理一個 area milestone」。

這代表：

- 可以分成 spec milestone 和 implementation milestone
- 但同一輪不應同時推進兩個不同 area 的主要 runtime 變更
- 若同時需要修改既有邊界房、`area/directory.lst` 或 docs，仍視為同一個 area milestone 的連動修改

## Area Plan Contract

每個 `plans/area/NNNN-area-slug.md` 至少應固定回答：

- `theme`
- `subtheme`
- `reserved_room_block`
- `planned_vnum_range`
- `external_links`
- `delivery_gate`
- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`

設計上的最低要求：

- `external_links` 要明講會接到哪個既有 area / room
- `planned_vnum_range` 要寫整段保留區，不只寫當前最後一號
- 若這輪只做 spec，也要先把 boundary assumptions 寫清楚
- 若是用 `ref/Readme.md` 選 reference，必須明講哪些有用、哪些刻意 deferred

## Area Spec Contract

每個 `area/<area>/map.md` 至少應包含：

- 區域用途與玩家流向
- 題材與 subtheme
- cluster 設計
- room intent / scene intent
- external exits / planned world links
- 驗證備註
- `mapmd-json`

`mapmd-json` 的角色：

- 它是 canonical machine-readable graph schema
- room 視為 node，exit 視為 edge
- 可包含 `cluster`、`labels`、`coord` 等 metadata
- 可用 `external: true` 表示合法的既有世界外部連線

## VNUM And Boundary Rules

在正式拆出 `docs/area-vnum-policy.md` 與 `docs/area-external-exit-policy.md` 前，這份 handbook 先固定最低共識：

- 新 AREA 的第一段 `reserved_room_block` 預設從某個 `xx01` 起跳
- block 大小用「首版預估房數 + 至少 8 格 headroom」後往上取到最近的 `10`
- `planned_vnum_range` 應宣告整段保留區
- 若 extension block 被使用，必須在 plan、spec metadata 與 tracker 明確註記
- 新 AREA 若要接到既有房號，應先在 `mapmd-json` 寫出 external exit，再同步 patch 既有 boundary room
- 新 AREA 成為 loadable runtime area 時，要同步更新新 area 自身、既有邊界房、以及 `area/directory.lst`

## Delivery Gates

每個 area milestone 都要受 `delivery_gate` 控制：

- `spec_in_progress`
  - 還在整理 `map.md`、cluster、theme、room intent 或 external links
- `spec_ready_for_commit`
  - spec 已形成穩定里程碑，應先 commit
- `implementation_in_progress`
  - 已開始落地 `.roo`、`mob / obj / res / shp`、`directory.lst` 或 boundary patches
- `implementation_ready_for_commit`
  - runtime data 已穩定並完成必要驗證，應先 commit
- `validated_ready_to_advance`
  - 當前 area 已達到可安全進下一區的狀態
- `blocked`
  - 有 blocker，需停在當前 area

判讀規則：

- `*_in_progress` 表示繼續做當前 area
- `*_ready_for_commit` 表示先 commit
- `validated_ready_to_advance` 才能安全前進下一個 actionable area
- `blocked` 表示先解 blocker，不得自行跳區

## Validation Levels

依任務範圍分層驗證：

### Spec / Plan / Tracker Only

最低驗證：

```bash
python .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/<area>/map.md --validate-only
```

通常不需要為了純 spec / planning 變更硬跑 build。

### Loadable Runtime Area Work

最低檢查：

- VNUM 與 boundary links
- `index / mob / obj / res / shp / roo` 一致性
- `area/directory.lst` 順序
- loader / smoke test 結果

常用 build：

```bash
make -C src clean && make -C src merc
```

若是在 Linux / Codex Cloud：

```bash
make -C src -f Makefile.lin merc
```

### Smoke Test Discipline

做 area smoke test 前後，至少遵守：

1. 建立 `log player mail debug vote` 目錄
2. 清空或 baseline 本輪 `debug/*`
3. 先確認本輪要看的 log 範圍
4. 若使用 `timeout`，優先給 `45` 到 `60` 秒
5. 必須看到明確成功訊號，例如 `三國歪傳之降龍伏虎開始正常運作`
6. 成功後仍要回看 `log/*` 與 `debug/*` 是否有本輪新 area 相關 warning / error

## Recommended Integration Sequence

當一個新 AREA 從 plan 走到真正可載入時，建議固定照下面順序：

1. 完成 `plans/area/NNNN-*.md`
2. 完成 `area/<area>/map.md`
3. 先跑 `--validate-only`
4. 產生第一批 `.roo`
5. 補 `index`
6. 補最小 `mob / obj / res / shp`
7. 補 external exit 與既有 boundary room patch
8. 掛入 `area/directory.lst`
9. 做 build 與 smoke test
10. 檢查 `log/*`、`debug/*`
11. 更新 `delivery_gate`
12. 回寫 tracker、單區 plan 與必要 docs

## Required Closeout Updates

每輪 area 工作收尾時，至少檢查：

- `area/rebuild_plan.md`
  - status、`next_action`、`next_prompt`、`delivery_gate` 是否已更新
- 對應 `plans/area/*.md`
  - 是否已回寫 ref metadata、boundary decision、blocker 或 extension block
- `docs/current-game/areas.md` / `docs/current-game/areas.json`
  - 只有在現行 loadable runtime area registry 真正變動時才同步
- 經驗回寫
  - 單區特殊決策回寫單區 plan / tracker
  - 可重用 parser / loader / validation 規則回寫 skill reference
  - 全局流程缺口回寫 `plans/0001-world-map-area-rebuild.md`

## Reference Entry Points

依用途選讀：

- 全局流程：`plans/0001-world-map-area-rebuild.md`
- 日常接續：`area/rebuild_plan.md`
- 單區設計：`plans/area/*.md`
- 世界藍圖 / template / scaffold：`ref/Readme.md`
- runtime area registry 補充：`docs/current-game/areas.md`
- 舊站世界觀與歷史資料：`docs/3yWebsite/`

## Companion Docs

這份 handbook 是 Stage 1 的入口文件；目前已搭配下列 companion docs：

- `docs/area-delivery-gates.md`
- `docs/area-vnum-policy.md`
- `docs/area-external-exit-policy.md`
- `docs/area-acceptance-checklist.md`
- `docs/codex-area-workflow.md`

若 companion docs 和全局流程看起來有差異，仍以 `AGENTS.md`、`plans/0001-world-map-area-rebuild.md` 與 `area/rebuild_plan.md` 為準，再回頭修 docs。
