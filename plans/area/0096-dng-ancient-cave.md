# Dng Ancient Cave Initial Area Plan

## Summary

建立下一個待建新 AREA：`dng_ancient_cave`。此區承接 `wild_bailang` 的裂縫洞口，把北境鏈從邊山 wild 正式切進濕冷封閉、帶封印與遺物感的地下 dungeon，讓 `白狼山 -> 古洞遺跡` 不再只停在抽象 graph，而是成為一段可辨位、可問路、也能預留更高秘境轉折的地下探索節點。

## Theme Positioning

- theme: `探險遺跡`
- subtheme: `洞窟遺封`
- experience_type: `Dungeon`
- player_loop_focus: `地下轉場 / 封印甬道 / 殘碑辨位 / 深處壓力`
- contrast_with_previous_two:
  - 相對於 `fort_yijing` 的軍鎮秩序與 `wild_bailang` 的開闊山前風感，`dng_ancient_cave` 應把節奏重新收緊成濕冷封閉、回音與封印殘痕主導的地下壓力，而不是再延續山脊外帶。
- 世界缺口角色：
  - 把 `wild_bailang/18006` 的下探預留正式轉成地下遺跡節點
  - 為後續 `sec_spirit_peak` 建立明確的地下通往更高秘境的過渡母點
- reserved_room_block: `18101-18120`
- planned_vnum_range: `18101-18120`
- level_range: `35-48`
- external_links:
  - `up`: `wild_bailang` / 裂縫洞口
  - `up`: `sec_spirit_peak` / 白狼靈峰預留
- delivery_gate: `spec_ready_for_commit`

## Reference Entry Points

- `area/world_map.md`
- `ref/Readme.md`
- `ref/sanguo-progression-map.md`
- `ref/三國-MUD-題材分布表.md`
- `ref/sanguo-area-specfirst/area/dng_ancient_cave/map.md`
- `ref/world-graph.md`
- `docs/3yWebsite/docs/data/players.json`
- `docs/3yWebsite/docs/data/skills.json`
- `plans/area/0095-wild-bailang.md`

## Ref Compliance Check

- `ref_inputs_used`
  - `area/world_map.md`
  - `ref/Readme.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `ref/sanguo-area-specfirst/area/dng_ancient_cave/map.md`
  - `ref/world-graph.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
  - `plans/area/0095-wild-bailang.md`
- `ref_inputs_deferred`
  - `docs/3yWebsite/map/bepin.html`
  - `ref/sanguo-area-specfirst/area/sec_spirit_peak/map.md`
  - `ref/sanguo-area-specfirst/area/city_xiangping/map.md`
  - 各類原型工具與模擬系統
- `theme_basis`
  - `world-graph` 明確把 `dng_ancient_cave` 放在 `wild_bailang` 之後，並形成 `Wild -> Dungeon` 的自然 family 切換
  - `題材分布表` 把北境白狼山段定成 `探險遺跡 / 詭異` 的傳說帶，支持由山前 wild 再往下切成更封閉的洞窟遺跡
  - `world_map` 把白狼山定位成遼東 / 襄平方向的邊境節點，適合在此補一個由地表轉入地下的探索缺口
  - `players.json / skills.json` 沒有提出比既有白狼山分流更強的城市服務優先訊號，支持先補這個下探 dungeon 節點
- `compliance_check`
  - compliant；在 `Wild` 之後切到 `Dungeon`，符合 queue variety，也直接承接 `wild_bailang/18006` 的既有下探預留

## Validation Results

- `python -X utf8 tools/mapmd_validate.py area/dng_ancient_cave/map.md`
  - passed (`Validated 8 room(s) across 1 file(s). Result: 0 error(s), 0 warning(s).`)
- `python -X utf8 .agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/dng_ancient_cave/map.md --validate-only`
  - passed (`Validation succeeded for 8 room(s).`)

## Runtime Notes

- pending

## Next Step Prompt

`先 commit 目前 dng_ancient_cave 的 spec milestone；commit 後直接做 implementation milestone，補齊 wild_bailang/18006 <-> dng_ancient_cave/18101 runtime boundary 並在通過 validate / build / smoke 後自動前進。`
