# 三國 MUD Spec-First AREA Scaffold

本資料夾將 `world-graph.json` 的 130 個世界節點，升級為更貼近 **Merc-FJU / mapmd-json** 的 spec-first scaffold。

每個 `area/<node_id>/map.md` 皆包含：
- 人類可讀的 prose scaffold
- 一個 `mapmd-json` fenced block
- 最小可擴充的 cluster / node / edge stub
- 對應世界圖的 worldLinks / interaction hints / generation hints

建議工作流：
1. 先編修 `Theme / Mood / Signature scenes / NPC roles / Quest hooks`
2. 再編修 `mapmd-json` 中的 `clusters / nodes / edges`
3. 最後交給 `.roo` / generator 做下游輸出
