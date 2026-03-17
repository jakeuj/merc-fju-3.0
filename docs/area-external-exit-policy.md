---
layout: default
title: Area External Exit Policy
---

# Area External Exit Policy

這份文件整理新 AREA 接回既有世界時的 external exit 規則，目標是避免 `map.md` spec、生成出的 `.roo`、既有 boundary room 與 `area/directory.lst` 各自講各話。

總覽仍以 [AREA 開發手冊](./area-development-handbook.html) 為準；這份文件專注在 external exit 的表示方式、雙邊同步責任與最小驗證要求。

## What Counts As An External Exit

當某個出口要接到「本次 spec 之外、但 repo 內已存在的既有房號」時，這就是 external exit。

常見情境：

- 新 area 接回既有主城
- 新 area 接到既有地城鏈
- 當前 area 先保留往未來區域的 world-link stub

要分清楚兩種情況：

- 接到 repo 內已存在的既有房號
  - 屬於 runtime 邊界整合
- 只是在 spec 中保留未來規劃方向
  - 屬於 planned world link，不等於已落地的 runtime exit

## Spec Representation

對既有房號的合法 external exit，應在 `mapmd-json` 上標示 `external: true`。

意義：

- generator 會保留這個出口
- 驗證時不要求目標房間也出現在同一份 spec 內
- 它仍會投影成正式 `.roo #Exit`

不要做的事：

- 只在 prose 寫「這裡通往洛陽」卻不寫進 `mapmd-json`
- 只在 `.roo` 手改出口，卻不回寫 spec
- 把 planned link 和已落地的 external exit 混成同一種資料

## Synchronization Contract

一個新 area 若要正式接回既有世界，預設要同步三個面向：

1. 新 area 的 spec 與 runtime 檔
2. 既有 boundary room 的 `.roo`
3. `area/directory.lst`

如果只改了其中一側，就容易出現：

- spec/runtime 分裂
- 單向出口沒補回程
- loader 雖能載入，但玩家走法不一致

## Bidirectional Rule

預設 external exit 應為可來回的成對出口。

若要做例外，必須明講原因：

- 單向落穴
- 傳送型入口
- 劇情限定的 one-way 通道

若 runtime intent 就是單向，應在 spec 中明確標示 `one_way` 或等價意圖，不要只是漏補 reverse exit。

## Planned Links Vs. Runtime Links

判讀方式如下：

- `Planned World Links`
  - 用來描述未來接線意圖
  - 可先留在 `map.md` prose
  - 不等於現在就要出現在 `.roo`
- external exit
  - 是當前 runtime 真正要落地的接線
  - 必須進 `mapmd-json`
  - 必須同步到 `.roo`
  - 若 area 已可載入，還要同步檢查既有邊界房與 `area/directory.lst`

## Integration Sequence

建議順序：

1. 先在單區 plan 固定 `external_links`
2. 在 `mapmd-json` 寫出 external exit
3. 先跑 `--validate-only`
4. 生成 `.roo`
5. patch 既有 boundary room
6. 掛入 `area/directory.lst`
7. 做 loader / smoke test

## Validation Requirements

至少檢查：

- 目標既有房號確實存在
- 方向是否合法，包含 `north/east/south/west/up/down/enter/out`
- reverse exit 是否成對，除非刻意 one-way
- 生成後 `.roo` 和既有 boundary room 的出口敘述一致
- smoke test 後沒有新的 boundary warning / parse error / `Load_room`

若這輪做了 boundary room patch，成功訊號不能只看 generator；仍必須看 loader 與 run log。

## Naming And Documentation Rule

在單區 plan 裡，`external_links` 應至少寫清楚：

- 連到哪個 area
- 連到哪個 room
- 使用哪個方向
- 這條連線在世界層扮演什麼角色

若只寫「接洛陽」而沒寫房號與方向，對後續維護幾乎沒有幫助。

## Common Failure Patterns

常見失誤：

- `map.md` 有寫外部接線，但 `mapmd-json` 沒寫
- 新 area 有出口，既有邊界房沒補回程
- `directory.lst` 已掛，boundary 還沒 patch 完
- planned link 被誤當成已落地 runtime exit
- 單向出口其實不是設計，而只是漏做 reverse exit

## Relationship To Other Docs

- 流程總覽： [docs/area-development-handbook.md](./area-development-handbook.html)
- 房號政策： [docs/area-vnum-policy.md](./area-vnum-policy.html)
- 驗收： [docs/area-acceptance-checklist.md](./area-acceptance-checklist.html)
- 全局規則： `plans/0001-world-map-area-rebuild.md`
