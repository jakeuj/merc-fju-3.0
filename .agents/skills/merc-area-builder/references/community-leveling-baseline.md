# Community Leveling Baseline (2011)

這份補充參考整理 `https://disp.cc/b/mud_3y/2mUG`（2011-09-28，玩家整理的「現今三歪升級區域參考」）。

## 用途

- 補玩家實際體感的練功帶與城鎮順序
- 幫 `level_range`、queue 合理性與服務節點強度做 community-side sanity check
- 補 `players.json` / `skills.json` 不會直接說的「大家當年實際去哪裡練」訊號

## 它不是什麼

- 不是官方世界圖
- 不是設計規格
- 不是單一職系以外都適用的絕對 leveling route
- 不是用來覆蓋 current repo `world_map`、`ref/` 或單區 plan 的依據

## 玩家向練功帶快照

- `Lv1-15`
  - 新手練功區
- `Lv15-21`
  - 陳留城
  - 北平郊區
- `Lv21-30`
  - 陳留西郊
- `Lv30-52`
  - 長安城
- `Lv52-60`
  - 洛陽南方的草原
  - 原文另註：建議先把 `SK` 練滿再升
- `Lv60-67`
  - 赤壁
  - 洛陽城
- `Lv67-73`
  - 建業城
  - 洛陽城
- `Lv73-77`
  - 洛陽城（將軍府殿前護衛）
- `Lv77-87`
  - 羅漢宮
- `Lv87-99`
  - 天庭
- `Lv99-100`
  - 建業城（環城道路四位）
  - 弘農城（傾城名伶・卉沁）

## 使用規則

- 若單區 `level_range` 已由 `world_map`、`progression map`、`players.json / skills.json` 大致決定，再用這份資料做最後 sanity check
- 若玩家文和設計圖衝突，優先保留 repo 內正式世界規劃；這份資料只能幫你看「玩家體感是否完全失真」
- 特別適合拿來回答：
  - 某個城市是不是合理的 midgame 練功城
  - 某個區是否應該承接城內練功、城郊過渡，還是更偏 service hub
  - 長安、弘農、建業這類城市在玩家眼中是否曾承接高等練功帶

## 回寫要求

- 若這輪有採用這份玩家向 leveling baseline，單區 plan / tracker 的 `ref_inputs_used` 要記精確 URL
- `theme_basis` 或 `compliance_check` 應明講它影響的是：
  - `level_range` sanity check
  - 玩家體感順序
  - 還是某個城市作為 grind / service hub 的合理性
