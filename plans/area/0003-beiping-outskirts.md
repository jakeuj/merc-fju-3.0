# Beiping Outskirts Initial Area Plan

## Summary

建立第二個正式新 AREA：`beiping_outskirts`。此區域承接 `beiping` 主城北側外郊，作為往易京與白狼山方向的第一段邊境過渡帶。

## Theme Positioning

- theme: `軍旅風`
- subtheme: `歷史城市風`
- 世界缺口角色：補足北平母城外圈的哨卡、驛道、河灘補給與北境山徑前帶

## Scope (Milestone 1)

- 建立 `area/beiping_outskirts/map.md` 的 spec 草案
- 建立最小可載入資產：`index`、`roo`、`mob`、`obj`、`res`、`shp`
- 與 `beiping/9001` 建立正式邊界連接（`9001 <-> 9101`）
- 將 `beiping_outskirts` 掛入 `area/directory.lst`

## World Links

- `south`: 回 `beiping`（`9001`）
- `north`: 預留通往易京官道
- `east`: 預留通往白狼山前哨

## Ref Compliance Check

- `ref_inputs_used`
  - `ref/Readme.md`
  - `area/world_map.md`
  - `docs/3yWebsite/map/bepin.html`
- `ref_inputs_deferred`
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - 其他模擬型 prototype
- `theme_basis`
  - `三國-MUD-題材分布表.md`
  - `references/theme-world-allocation.md`
  - `area/world_map.md`
- `compliance_check`
  - compliant；本輪僅使用 world-map 與既有 area 風格做 spec-first 落地

## Validation Targets

- `beiping_outskirts` 可由 `directory.lst` 載入
- `beiping/9001` 與 `beiping_outskirts/9101` 形成雙向出口
- `.res` 能正常解析並放置最小 NPC/物件

## Implementation Outcome (Round 1)

- `area/beiping_outskirts` 已完成最小可載入集合
- `9001 <-> 9101` 邊界出口已落地
- `map.md` 已補齊完整 `mapmd-json` rooms 與 exits，並用 generator 驗證 / 產生 `.roo`
- 修正 `obj/9753.obj` weapon 欄位，避免載入時出現 `Wieldable` 命令錯誤

## Smoke Test Outcome

- 在 WSL 以 `timeout 45 bash ./startup.bash` 啟動測試
- `log/1002.log` 出現「三國歪傳之降龍伏虎開始正常運作」成功訊號
- 清空後檢查 `debug/*`，未再出現 `beiping_outskirts` 相關 load error
- 此區可視為 `validated_ready_to_advance`
