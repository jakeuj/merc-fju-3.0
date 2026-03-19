# <Area Title> Initial Area Plan

## Summary

建立下一個待建新 AREA：`<area_slug>`。說明這個區域承接哪條世界鏈、補哪個玩法或題材缺口、目前預計先做 spec 還是已準備進 implementation。

## Theme Positioning

- theme: `<primary theme>`
- subtheme: `<secondary theme>`
- 世界缺口角色：說明這區補的是什麼 progression / world / traversal 缺口

## Area Metadata

- area_slug: `<area_slug>`
- level_range: `<min-max within 1-100>`
- reserved_room_block: `<xx01-xxNN>`
- planned_vnum_range: `<xx01-xxNN>`
- parent_area: `<parent area or none>`
- delivery_gate: `<spec_in_progress | spec_ready_for_commit | implementation_in_progress | implementation_ready_for_commit | validated_ready_to_advance | blocked>`

## Scope (Milestone 1: Spec)

- 建立 `area/<area_slug>/map.md` 第一版
- 固定 cluster、world links、room intent 與 `mapmd-json`
- 明確標示與既有 area 的 boundary 假設
- 註明本輪刻意 deferred 的 runtime 工作

## Scope (Milestone 2: Implementation)

- 以 `map.md` 生成 `roo/*.roo` 第一版
- 補齊最小 `index / mob / obj / res / shp`
- 視需要掛入 `area/directory.lst`
- 視需要補既有 boundary room

## World Links (Spec Intent)

- `<direction>`: 通往 `<target area>` room `<vnum or planned target>`
- `<direction>`: 通往 `<target area>` room `<vnum or planned target>`

## External Links

- source: `<room vnum>`
  direction: `<direction>`
  target_area: `<existing area>`
  target_room_vnum: `<existing room vnum>`
  status: `<planned | runtime>`
  note: `<why this link exists>`

## Ref Compliance Check

- `ref_inputs_used`
  - `<ref path>`
  - `<ref path>`
- `ref_inputs_deferred`
  - `<ref path or category>`
  - `<ref path or category>`
- `theme_basis`
  - `<basis>`
  - `<basis>`
- `compliance_check`
  - `<compliant or exception with reason>`

## Validation Targets

- `plans/area/*.md` 的 `level_range`、`map.md` 的 `LevelRange` 與 `mapmd-json.area.level_range` 一致
- `map.md` 內含有效 `mapmd-json`
- `--validate-only` 可通過
- 方向只使用 `north/south/east/west/up/down/enter/out`
- reverse exit 成對，除非明確標示 `one_way`
- external links 與 boundary assumptions 可被回讀

## Validation Results

- `<command>`
  - `<pending / passed / failed and notes>`

## Runtime Notes

- `area/directory.lst`: `<not touched / updated>`
- boundary room patches: `<none / details>`
- deferred items: `<list>`

## Risks And Blockers

- `<risk or blocker>`
- `<risk or blocker>`

## Next Step Prompt

`<next recommended prompt>`
