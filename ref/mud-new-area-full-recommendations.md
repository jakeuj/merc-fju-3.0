# MUD 新 AREA 開發完整建議整理

本文件整理一套適合交給本地 Codex 執行的 **MUD 新 AREA spec-first 開發建議清單**。  
目標是讓未來新增 AREA 時，有固定流程、固定文件、固定模板、固定驗證工具、固定 smoke test、固定 gate、固定 prompt，而不是每次重新發明流程。

---

## 一、總體目標

新 AREA 開發真正要建立的不是單一區域，而是 **可持續擴充的新區開發系統**。

建議拆成六個層次：

1. 世界規劃層
2. 單區 spec 層
3. 生成器層
4. 驗證器層
5. 啟動 / smoke test 層
6. Git / PR / Codex workflow 層

新 AREA 開發最常見風險：

- 房號衝突
- exit 對不回去
- 地圖 spec 跟 `.roo` 脫鉤
- reset / mob / obj 漏檔
- `directory.lst` 沒同步
- 同一區做到一半跳去下一區
- 一次改太多，壞了不知道哪裡出問題

所以建議本地 Codex 幫你補齊：**文件 + 工具 + 規則 + prompt 套件**。

---

## 二、建議補齊的文件清單

### 1. `docs/area-development-handbook.md`
用途：新 AREA 開發總手冊。

建議內容：
- 新 AREA 開發完整流程
- spec-first 說明
- `map.md` 應包含欄位
- 何時可以生成 `.roo`
- 何時可以掛進 `directory.lst`
- 何時必做 smoke test
- 何時才能進下一個 area

---

### 2. `docs/area-delivery-gates.md`
用途：把 gate 明文化，避免 Codex 跳步。

建議固定 gate：
- `spec_in_progress`
- `spec_ready_for_commit`
- `implementation_in_progress`
- `implementation_ready_for_commit`
- `validated_ready_to_advance`
- `blocked`

建議內容：
- 每個 gate 的定義
- 進 gate 的條件
- 哪些 gate 不准跳下一區
- 哪些 gate 必須先 commit

---

### 3. `docs/area-vnum-policy.md`
用途：定義新 AREA 的房號保留規則。

建議內容：
- 新 area 一律從 `xx01` 起跳
- `reserved_room_block` 的計算方式
- 至少保留 headroom
- 不跨百位段
- `planned_vnum_range` 要寫整段，不只寫目前已用號碼
- extension block 的追加規則
- `directory.lst` 的註解同步規則

---

### 4. `docs/area-external-exit-policy.md`
用途：定義新 AREA 如何接到既有世界。

建議內容：
- external exit 定義
- `mapmd-json` 如何表示 external exit
- 何時只在 spec 註記，何時必須同步改既有 `.roo`
- 舊主城 / 舊 area 接線 patch 規範
- 單向 / 雙向出口要求
- 入口 / 出口房的命名與註解規則

---

### 5. `docs/area-acceptance-checklist.md`
用途：新 AREA 合併前的最後 checklist。

建議內容：
- 已有 plan
- 已有 `map.md`
- `reserved_room_block` 已登記
- room vnum 無衝突
- `.roo` 已生成
- `mob/obj/res/shp` 已補最小可用版本
- 已掛入 `directory.lst`
- 已補與既有世界的 external exits
- smoke test 成功
- log 無 parse error
- debug 無本次新增 area 相關新錯誤
- tracker 狀態已更新

---

### 6. `docs/codex-area-workflow.md`
用途：給本地 Codex / 未來其他 AI agent 用的 workflow 文件。

建議內容：
- 一個 task 只做一個 area
- 固定 branch 命名
- 固定 prompt
- 固定產出清單
- 固定檢查順序
- 什麼情況不能繼續做下一區

---

### 7. `docs/area-design-rules.md`
用途：定義內容設計規則。

建議內容：
- 每個新 AREA 要先回答的問題
- 每區至少要有的 cluster 類型
- 每區 room 設計規則
- 每區 NPC / object / reset 最小集

---

### 8. `docs/area-theme-allocation-guide.md`
用途：把 theme / subtheme 選用規則寫死。

建議內容：
- 六大題材如何分布
- 哪些類型不要過度重複
- 主城外郊 / 邊關 / 地下 / 遺跡 / 秘境 的風格過渡方式

---

### 9. `docs/room-narrative-style-guide.md`
用途：統一房間敘述風格。

建議內容：
- room title 命名規則
- 短描述 / 長描述風格
- `#Keyword` / `#Enquire` 風格
- 場景語氣一致性
- 如何讓相鄰房間有辨識度

---

### 10. `docs/mapmd-json-spec.md`
用途：人類可讀版 `mapmd-json` 規格說明。

---

### 11. `docs/git-branch-policy-for-areas.md`
用途：AREA 開發的 Git / branch 規則。

建議內容：
- 新 AREA 預設 `codex/<area>-implementation`
- 同一區未完成前不再切新 branch
- 同一 PR 只做單一 area 或單一里程碑
- merge 後才開始下一區

---

### 12. `docs/pr-template-new-area.md`
用途：新 AREA 的 PR 模板。

建議欄位：
- area 名稱
- theme / subtheme
- reserved_room_block
- external exits
- 影響到的既有 area
- smoke test 結果
- world consistency check 結果
- 風險點

---

## 三、建議補齊的模板文件

### 13. `templates/area-plan.template.md`
用途：新 AREA 立項模板。

建議欄位：
- `area_slug`
- `title`
- `theme`
- `subtheme`
- `reserved_room_block`
- `planned_vnum_range`
- `delivery_gate`
- `status`
- `parent_region`
- `upstream_links`
- `downstream_links`
- `external_exits`
- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`
- `role_in_world`
- `traversal_role`
- `narrative_role`
- `difficulty_band`
- `expected_room_count`
- `required_clusters`
- `required_npcs`
- `required_objects`
- `required_resets`
- `shops_needed`
- `special_systems`
- `smoke_test_strategy`
- `blocker_risks`
- `acceptance_notes`

---

### 14. `templates/map.md.template`
用途：新 AREA spec 模板。

至少要有：
- `# Overview`
- `# Theme`
- `# Progression Role`
- `# Area Topology`
- `# Cluster Design`
- `# Room Intent`
- `# NPC Intent`
- `# Object Intent`
- `# Reset Strategy`
- `# External Exits`
- `# Validation Notes`
- `# mapmd-json`

---

### 15. `templates/area-readme.template.md`
用途：AREA 目錄下的快速說明。

內容建議：
- 這區是什麼
- 跟哪裡連
- 房號範圍
- 主題
- 目前狀態
- 特殊注意事項

---

### 16. `templates/new-area-checklist.template.md`
用途：每個 area 實作時一起複製，避免漏步。

---

## 四、建議補齊的 Schema

### 17. `schemas/mapmd-json.schema.json`
用途：定義 `mapmd-json` 格式。

至少要有：
- area metadata
- reserved_room_block
- rooms
- exits
- external_exits
- clusters
- tags
- optional content hooks

---

### 18. `schemas/area-plan.schema.json`
用途：驗證 plan 檔欄位完整。

---

## 五、建議補齊的工具清單

你已經有 `world-consistency-checker.py`。接下來建議補這些：

### 19. `tools/area_vnum_allocator.py`
用途：自動找下一個可用 `reserved_room_block`。

功能建議：
- 掃描現有 `area/`、`data/`、`directory.lst`
- 找已使用 room vnum
- 根據規則選下一段 `xx01-xxNN`
- 可指定預估房數
- 自動預留 headroom
- 輸出建議 block

---

### 20. `tools/area_scaffold_generator.py`
用途：自動建立新 AREA 目錄與初始檔案。

功能建議：
- 建立 `area/<slug>/`
- 複製 `map.md.template`
- 複製 `README.md`
- 建立 plan 草稿
- 預填 `reserved_room_block`
- 可選擇 theme / subtheme

---

### 21. `tools/mapmd_validate.py`
用途：驗證 `map.md` 裡 machine-readable 區塊。

檢查建議：
- JSON 結構合法
- room vnum 在保留段內
- room slug 唯一
- exit target 存在
- external exit 格式正確
- cluster id 合法
- required metadata 存在

---

### 22. `tools/generate_area_from_map.py`
用途：從 `map.md` 產出 `.roo` 與初始資料。

建議支援：
- `--dry-run`
- `--write`
- external exit 支援
- dry-run diff
- CLI 參數化

---

### 23. `tools/area_patch_existing_world.py`
用途：新 AREA 接到舊世界時，自動產出 patch 建議。

功能建議：
- 根據 external exit metadata
- 找到要補的既有 `.roo`
- 產出 patch plan
- 先 dry-run 顯示 diff
- 可選擇是否套用

---

### 24. `tools/area_smoke_test_runner.py`
用途：自動跑本機 smoke test。

功能建議：
- 清空本輪 `debug/*`
- 建立 `log` 基線
- 確保 `merc.ini` 正確
- 執行 `merc` 或 `startup.bash`
- 支援 timeout 45~60 秒
- 收集新 log
- 收集新 debug
- 輸出摘要報告

---

### 25. `tools/log_parse_summary.py`
用途：解析啟動 log，抓 area 載入錯誤。

關鍵字建議：
- `Load_room`
- `duplicate`
- `parse error`
- `mob`
- `obj`
- `reset`
- `unknown`
- `vnum`

---

### 26. `tools/area_acceptance_gate.py`
用途：自動判斷 AREA 是否可前進 gate。

檢查建議：
- 文件有沒有
- spec 是否存在
- `.roo` 是否存在
- `directory.lst` 是否已掛
- smoke test 是否成功
- log / debug 是否乾淨
- 輸出建議 gate 與原因

---

### 27. `tools/update_rebuild_tracker.py`
用途：自動更新 `area/rebuild_plan.md` 的狀態欄位。

功能建議：
- 從 `todo` 移到 `in_progress`
- 更新 `delivery_gate`
- 更新 `next_action`
- 更新 `next_prompt`
- 更新 `done/blocked`

---

### 28. `tools/world_graph_diff.py`
用途：比對世界拓樸前後差異。

輸出建議：
- 新增節點
- 新增連線
- 修改連線
- 是否破壞既有主鏈

---

## 六、建議補齊的腳本

### 29. `scripts/ci_validate_new_area.sh`
用途：CI 用的最小驗證腳本。

流程建議：
- `mapmd_validate`
- `world-consistency-checker`
- `area_smoke_test_runner`
- `area_acceptance_gate`

---

### 30. `scripts/new_area_bootstrap.sh`
用途：快速建立新 area。

功能建議：
- 呼叫 vnum allocator
- 建 plan
- 建目錄
- 建 map.md
- 建 README
- 更新 tracker

---

### 31. `scripts/validate_area.sh`
用途：對單一 area 做完整驗證。

---

### 32. `scripts/validate_world.sh`
用途：對全世界做 consistency check。

---

## 七、建議補齊的 Prompt 套件

### 33. `prompts/new-area-master-prompt.md`
用途：固定主 prompt。

建議內容重點：
- 先讀 `area/rebuild_plan.md`
- 先讀 `plans/area/*.md`
- 先讀 `area/<area>/map.md`
- 遵守 `delivery_gate`
- 若已有 `in_progress` area，優先續做
- 若無 `in_progress`，才選第一個 `todo`
- 不得在同一輪切去下一個 area
- 先驗證 spec，再生成資料，再驗證 runtime

---

### 34. `prompts/new-area-spec-prompt.md`
用途：專門生成 `map.md`。

---

### 35. `prompts/new-area-implementation-prompt.md`
用途：專門從 spec 落地 `.roo` / `mob/obj/res/shp`。

---

### 36. `prompts/new-area-validation-prompt.md`
用途：專門要求 Codex 跑 validator / smoke test / gate 判定。

---

### 37. `prompts/fix-area-load-error-prompt.md`
用途：當 `Load_room` / parse error / duplicate vnum 時，讓本地 Codex 專門做修復。

---

## 八、新 AREA 開發的內容設計規則

### 核心原則
1. 一個 AREA 一個 task / PR  
2. 先 spec，後生成  
3. 先 validator，後自動化  
4. external exit 一開始就納入 spec  
5. smoke test 要標準化  
6. delivery gate 要硬性執行  

### 每個新 AREA 要先回答的問題
- 這區的世界定位是什麼？
- 這區是主鏈、支線、地下入口、過渡區，還是終點區？
- 它補的是哪個題材缺口？
- 它解決的是哪個 traversal 空洞？

### 每區至少要有的 cluster 類型
以城郊區為例，預設至少要有：
- 主道路
- 側路 / 分岔
- 地標
- 過渡點
- 危險點
- 返回點

### 每區 room 設計規則
- 不要每房都只是路
- 至少有 1~2 個辨識性地標房
- 至少有 1 個節奏轉折房
- 至少有 1 個回看世界關係的房
- 不要所有出口都只做平面線性串接

### 每區 NPC / object / reset 最小集
至少要定義：
- 路標 NPC / 守衛 / 路人
- 1 個題材強化 NPC
- 1 個互動點
- 1 組基本 reset

---

## 九、建議的實作優先順序

### 第一階段：先補最必要
1. `docs/area-development-handbook.md`
2. `docs/area-delivery-gates.md`
3. `docs/area-vnum-policy.md`
4. `templates/area-plan.template.md`
5. `templates/map.md.template`
6. `schemas/mapmd-json.schema.json`
7. `tools/area_vnum_allocator.py`
8. `tools/mapmd_validate.py`
9. `tools/area_smoke_test_runner.py`
10. `prompts/new-area-master-prompt.md`

### 第二階段：補效率工具
11. `tools/area_scaffold_generator.py`
12. `tools/update_rebuild_tracker.py`
13. `tools/area_acceptance_gate.py`
14. `tools/log_parse_summary.py`
15. `scripts/new_area_bootstrap.sh`
16. `scripts/validate_area.sh`

### 第三階段：補大型世界工具
17. `tools/world_graph_diff.py`
18. `docs/area-theme-allocation-guide.md`
19. `docs/room-narrative-style-guide.md`
20. `docs/pr-template-new-area.md`
21. `scripts/validate_world.sh`
22. CI pipeline

---

## 十、可直接丟給本地 Codex 的一次性任務

```md
請為我的 MUD 新 AREA 開發流程補齊一整套 spec-first world building toolkit，目標是讓未來新增 AREA 時有固定文件、固定模板、固定 validator、固定 smoke test、固定 gate、固定 prompt。

請優先建立以下內容：

一、文件
- docs/area-development-handbook.md
- docs/area-delivery-gates.md
- docs/area-vnum-policy.md
- docs/area-external-exit-policy.md
- docs/area-acceptance-checklist.md
- docs/codex-area-workflow.md
- docs/area-design-rules.md
- docs/area-theme-allocation-guide.md
- docs/room-narrative-style-guide.md
- docs/mapmd-json-spec.md
- docs/git-branch-policy-for-areas.md
- docs/pr-template-new-area.md

二、模板
- templates/area-plan.template.md
- templates/map.md.template
- templates/area-readme.template.md
- templates/new-area-checklist.template.md

三、schema
- schemas/mapmd-json.schema.json
- schemas/area-plan.schema.json

四、工具
- tools/area_vnum_allocator.py
- tools/area_scaffold_generator.py
- tools/mapmd_validate.py
- tools/generate_area_from_map.py
- tools/area_patch_existing_world.py
- tools/area_smoke_test_runner.py
- tools/log_parse_summary.py
- tools/area_acceptance_gate.py
- tools/update_rebuild_tracker.py
- tools/world_graph_diff.py

五、腳本
- scripts/ci_validate_new_area.sh
- scripts/new_area_bootstrap.sh
- scripts/validate_area.sh
- scripts/validate_world.sh

六、prompt 套件
- prompts/new-area-master-prompt.md
- prompts/new-area-spec-prompt.md
- prompts/new-area-implementation-prompt.md
- prompts/new-area-validation-prompt.md
- prompts/fix-area-load-error-prompt.md

實作要求：
1. 所有工具都要先以 dry-run 為預設友善模式
2. 文件內容要互相一致
3. schema、validator、generator 的欄位定義必須一致
4. 新 AREA workflow 必須遵守 delivery_gate
5. 保留 external exit 支援
6. 保留 reserved_room_block / planned_vnum_range 規則
7. 先產出最小可用版本，不要過度設計
8. 每個檔案都要有清楚用途與使用方式
```

---

## 十一、最後的實戰建議

最值得堅持的原則：

- 一個 AREA 一個 task / PR
- 先 spec，後生成
- 先 validator，後自動化
- external exit 一開始就納入 spec
- smoke test 要標準化
- gate 要硬性執行

這套流程的價值不是「一次生成一個新區」，而是讓你未來擴充 50、100、120 個 AREA 時，仍然能維持一致、可驗證、可回溯的開發節奏。
