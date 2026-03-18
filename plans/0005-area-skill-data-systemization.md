# Area / Skill Data Systemization

## Summary

把 `docs/area-data-systemization-assessment.md` 的結論正式落成 repo roadmap，採 `structured JSON source -> exporter -> legacy runtime files` 的三層模型，先處理 skill canonical source，再做 per-area content pilot，最後補 validation、diff 與 docs packaging。

## Current Status

- v1 已落地：skill canonical source、skill exporter、`loyang_outskirts` area content pilot、current-game skill read model / runtime audit pipeline 都已實作
- runtime loader contract 維持不變；驗證已覆蓋 exporter round-trip、current-game docs reproducibility、WSL Linux build 與 startup smoke test
- 後續若要延伸，優先把更多 area 納入 `content.json`，而不是回退到 DB-first 設計

## Non-Goals

- 不改 `src/load.c` / `src/file.c` 的 runtime loader contract
- 不以 database 作為 v1 source of truth
- 不在第一輪把 `roo`、`index`、`directory.lst`、boundary patch 一起納入 area content exporter

## Phase 1: Skill Structured Source

- 新增 `data/structured/skills/skills.json` 作為 canonical structured source
- 新增 `schemas/skill-registry.schema.json`
- 新增 `scripts/export_structured_skills.py --check|--write`
- `skill/skill.lst` 與 `skill/*.ski` 維持 runtime artifact，由 exporter 生成
- `runtime_contract` 以 slot / type / cost / weapon / check 等 loader-sensitive 欄位為核心
- `document` 保留 `.ski` 的欄位與 `#Damage` / `#Affect` 區塊 AST，確保 round-trip 可檢查、可重建

## Phase 2: Area Content Structured Source

- 保留 `area/<area>/map.md + mapmd-json` 作為 topology source
- 另新增 `area/<slug>/content.json` 與 `schemas/area-content.schema.json`
- 新增 `scripts/export_area_content.py <area_slug> --check|--write`
- v1 只覆蓋 `mob / obj / res / shp / area-level balance metadata`
- pilot area 固定選 `area/loyang_outskirts`

## Phase 3: Docs And Audit Packaging

- `scripts/build_current_game_skill_registry.py` 改成 structured registry 為主、runtime readback 為 audit
- `docs/current-game/skills.json` 與相關 pages 繼續作為 generated read model
- exporter 預設先走 diff/check gate，再允許 write

## Acceptance Criteria

- `python -X utf8 scripts/export_structured_skills.py --check` 通過
- `python -X utf8 scripts/export_area_content.py loyang_outskirts --check` 通過
- `python -X utf8 scripts/build_current_game_skill_registry.py` 可重建 `docs/current-game/skills.json`
- `python -X utf8 scripts/generate_current_game_skills_pages.py` 第二次重跑無新增 diff
- 若 pilot area runtime 檔有語意差異，補 `make -C src -f Makefile.lin merc`
