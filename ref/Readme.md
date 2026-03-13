# ref Index

這份索引整理 `ref/` 內目前可用的參考資料、原型資料夾與世界規劃檔，方便先找方向，再深入讀各子資料夾內的 README 或範例檔。

## 使用建議

- 要做世界級規劃，先看「世界藍圖與拓樸」
- 要做新 AREA 的 spec-first 草案，先看「AREA scaffold 與 template」
- 要研究自動生成或 editor 原型，再看「生成器與編輯器原型」
- 要補 NPC / 勢力 / 經濟 / 歷史事件系統，再看「模擬與系統原型」

## 世界藍圖與拓樸

- `三國-MUD-120area-world-map.md`
  - 120 個 area 規模的世界圖草案
- `三國-MUD-世界130AREA-可視化世界地圖.md`
  - 130 AREA 視覺化世界地圖說明
- `三國-MUD-世界130AREA-可視化世界地圖.png`
  - 世界地圖 PNG 版本
- `三國-MUD-世界130AREA-可視化世界地圖.svg`
  - 世界地圖 SVG 版本
- `三國-MUD-世界完整連線圖-Graph版.md`
  - 用 graph 角度描述世界連線
- `三國-MUD-世界拓撲圖.md`
  - 世界拓樸規劃稿
- `三國-MUD-世界設計總藍圖-Architecture-Map.md`
  - 偏架構總覽的世界設計藍圖
- `三國-MUD-世界題材強化方案.md`
  - 世界題材分配與強化構想
- `三國-MUD-完整世界區域規劃.md`
  - 完整世界區域規劃稿
- `三國-MUD-題材分布表.md`
  - 題材分布整理表
- `world-graph.json`
  - 世界圖的結構化 graph 資料
- `world-graph.md`
  - `world-graph.json` 的文字說明版
- `sanguo-area-cluster-map.md`
  - area/cluster 層級的地圖規劃
- `sanguo-area-distribution.md`
  - area 分布整理
- `sanguo-player-flow-map.md`
  - 玩家流向規劃
- `sanguo-progression-map.md`
  - 成長與探索 progression 規劃
- `sanguo-room-density-map.md`
  - 房間密度分布圖說明
- `sanguo-room-density-map.png`
  - 房間密度圖
- `sanguo-mud-worldmap-professional.svg`
  - 專業版世界地圖 SVG

## AREA Scaffold 與 Template

- `area-template-wild_loyang_east.md`
  - 洛陽東郊型野外 area template，最接近目前 `loyang_outskirts` 類需求
- `mud-area-templates/`
  - 單一 area 類型模板集合
  - 例：`city_loyang.md`、`dng_royal_tomb.md`、`fort_hulao.md`
- `sanguo-area-scaffold/`
  - 根據 `world-graph.json` 自動生成的 130 個 area scaffold
  - 每個 area 已有基本 `map.md` 骨架
  - 先看 `sanguo-area-scaffold/README.md`
- `sanguo-area-specfirst/`
  - 更貼近 Merc-FJU / `mapmd-json` 的 spec-first scaffold
  - 每個節點都有 `area/<node_id>/map.md`
  - 先看 `sanguo-area-specfirst/README.md`

## 生成器與編輯器原型

- `mud-world-builder/`
  - 世界生成器 scaffold，可由 `world-graph.json` 生成 AREA / CLUSTER / ROOM 骨架
  - 先看 `mud-world-builder/README.md`
- `mud-ai-map-generator/`
  - AI 地圖生成原型
  - 先看 `mud-ai-map-generator/README.md`
- `mudlet-map-generator/`
  - 產生 Mudlet 地圖的原型工具
  - 先看 `mudlet-map-generator/README.md`
- `mud-world-map-editor/`
  - 世界地圖編輯器原型
- `mud-world-map-editor-pro/`
  - 世界地圖編輯器進階版原型

## 模擬與系統原型

- `mud-ai-faction-strategy-system/`
  - 勢力策略模擬
- `mud-character-relationship-system/`
  - 角色關係模擬
- `mud-economy-system/`
  - 城市經濟與 trade route 模擬
- `mud-faction-control-system/`
  - 勢力控制 / 戰鬥 schema 原型
- `mud-hero-ai-system/`
  - 英雄 AI 規則與模擬
- `mud-history-event-system/`
  - 歷史事件與戰役資料
- `mud-npc-ecosystem-system/`
  - NPC 生態與 spawn 規則

這些資料夾大多都各自附有 `README.md`，適合在需要對應子系統時再深入讀，不必一開始全部載入。

## 目前最值得優先參考的路徑

若目標是目前這個 repo 的 area 重建與 spec-first 流程，優先順序建議如下：

1. `world-graph.json`
2. `三國-MUD-世界設計總藍圖-Architecture-Map.md`
3. `三國-MUD-題材分布表.md`
4. `area-template-wild_loyang_east.md`
5. `sanguo-area-specfirst/`
6. `sanguo-area-scaffold/`

## 對目前工作的直接價值

- `loyang_outskirts` 類規劃：
  - 優先看 `area-template-wild_loyang_east.md`
  - 再看 `sanguo-area-specfirst/` 中相近的 `wild_*` 節點
- 世界級 area rebuild：
  - 優先看 `world-graph.json`、世界藍圖系列 `.md`、題材分布表
- 未來若要做工具化：
  - 再看 `mud-world-builder/`、`mud-ai-map-generator/`、`mud-world-map-editor/`
