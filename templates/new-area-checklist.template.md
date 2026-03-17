# New Area Checklist: `<area_slug>`

## Planning

- [ ] 已建立 `plans/area/NNNN-<area_slug>.md`
- [ ] 已固定 `theme` / `subtheme`
- [ ] 已固定 `reserved_room_block`
- [ ] 已固定 `planned_vnum_range`
- [ ] 已寫明 `external_links`
- [ ] 已補齊 `ref_inputs_used / ref_inputs_deferred / theme_basis / compliance_check`

## Spec

- [ ] 已建立 `area/<area_slug>/map.md`
- [ ] `mapmd-json` 已可通過 `--validate-only`
- [ ] planned world links 和 runtime external exits 已分清楚
- [ ] direction 只使用合法方向
- [ ] reverse exit 已成對，或明確標示 `one_way`

## Runtime

- [ ] 已生成第一批 `.roo`
- [ ] 已建立最小 `index`
- [ ] 已建立最小 `mob / obj / res / shp`
- [ ] 若有 external exit，既有 boundary room 已 patch
- [ ] 若 area 已可載入，`area/directory.lst` 已更新
- [ ] `Capital` 設定已檢查

## Validation

- [ ] 已做對應 build
- [ ] 已做 smoke test
- [ ] 已找到成功訊號
- [ ] 已檢查 `log/*`
- [ ] 已檢查 `debug/*`
- [ ] 若有 `obj` 變更，已檢查 `debug/badobject`
- [ ] 若有 `mob Enable` 變更，已檢查 `debug/failenable`

## Closeout

- [ ] `area/rebuild_plan.md` 已更新
- [ ] 單區 plan 已回寫本輪重要決策
- [ ] 若 runtime registry 變動，已更新 `docs/current-game/areas.*`
- [ ] 已判斷當前 `delivery_gate`
- [ ] 已決定是否可 commit 或可前進下一區
