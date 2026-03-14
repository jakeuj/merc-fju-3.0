# AGENTS.md

This repository is a Merc MUD codebase with both legacy runtime/build paths and an active spec-first area rebuild workflow. Follow these rules during Codex tasks in this repo.

## Repo orientation

- Assume the repository root in Codex Cloud is `/workspace/merc-fju-3.0`.
- Prefer repo instructions and checked-in workflow docs over generic Merc MUD assumptions.
- This repo actively uses:
  - `.agents/skills/` for repo-specific workflows
  - `plans/` for long-lived planning
  - `area/rebuild_plan.md` for the day-to-day area rebuild tracker
- If a task touches existing/new areas, area planning, maps, `.roo`, or world links, treat the area rebuild docs as authoritative before editing files.

## Skill usage

- If the task is about area files, world links, `map.md`, `mapmd-json`, `.roo`, `index/mob/obj/res/shp`, `area/directory.lst`, or long-running area rebuild work, use:
  - `.agents/skills/merc-area-builder/SKILL.md`
- If the task is about local build, startup, `merc.ini`, logs, debug output, or environment/runtime troubleshooting, also check:
  - `.agents/skills/merc-local-ops/SKILL.md`
  - Treat the primary supported local environments as `Windows + WSL (Ubuntu)` and `macOS + Docker (Ubuntu)`.
- If the task is about explaining source structure, load flow, or finding code entry points, also check:
  - `.agents/skills/merc-source-explainer/SKILL.md`
- Read only the relevant skill sections needed for the task, but do not skip the skill when the task clearly matches it.

## Area rebuild workflow

- The canonical long-running workflow lives in:
  - `plans/0001-world-map-area-rebuild.md`
  - `area/rebuild_plan.md`
  - `plans/area/*.md`
- File roles:
  - `plans/0001-*.md`: global strategy and workflow rules
  - `plans/area/NNNN-*.md`: single-area design and validation intent
  - `area/rebuild_plan.md`: operational tracker for `todo / in_progress / done / blocked / next_action / next_prompt / delivery_gate`
- For any request like "continue next area", "繼續實作 area", or "continue rebuild", interpret `next area` as the next actionable area, not simply the next name in candidate order.
- Always read `area/rebuild_plan.md` first:
  - If there is an `in_progress` area, continue that area.
  - Only move to a `todo` area when no `in_progress` area remains.

## Delivery gate rules

- Respect `delivery_gate` in `area/rebuild_plan.md`:
  - `spec_in_progress` / `implementation_in_progress`: continue the current area
  - `spec_ready_for_commit` / `implementation_ready_for_commit`: commit the current milestone before moving on
  - `validated_ready_to_advance`: the area is complete enough to move to the next actionable area
  - `blocked`: resolve the blocker; do not skip to another area as a workaround
- Do not silently advance from one area to another if the tracker still says the current area must be committed or finished first.

## Area source of truth

- For spec-first areas:
  - Human design source of truth: `area/<area>/map.md`
  - Machine-readable canonical graph: embedded `mapmd-json`
  - Current projection target: `.roo`
- If prose and `mapmd-json` disagree, treat `mapmd-json` as the generator input and fix the prose.
- Do not treat generated `.roo` files as the design source when `map.md` exists.

## Area editing rules

- Before editing area data, inspect:
  - `area/directory.lst`
  - target area directory
  - relevant `plans/area/*.md`
  - `area/rebuild_plan.md` if the task is part of the rebuild flow
- Confirm room schema and exits against current code, especially:
  - `src/load.c`
  - `src/act_move.c`
- Valid movement directions are not limited to four cardinal directions; current area work may use:
  - `north`, `east`, `south`, `west`, `up`, `down`, `enter`, `out`
- `.roo` room content may include formal blocks such as:
  - `#Exit`
  - `#Keyword`
  - `#Job`
  - `#Enquire`
- When connecting a new area to an existing area, keep both sides in sync:
  - the new area spec/runtime files
  - the existing boundary room file
  - `area/directory.lst` if the new area becomes loadable

## Planning metadata requirements

- When an area task uses `ref/Readme.md` to choose references, templates, or scaffold material, update the single-area plan and/or tracker with:
  - `ref_inputs_used`
  - `ref_inputs_deferred`
  - `theme_basis`
  - `compliance_check`
- Do not write vague notes like "referenced ref files"; be explicit about what was used and what was deliberately deferred.

## Validation for area work

- Minimum validation for spec-first work:
  - run `.agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py area/<area>/map.md --validate-only`
- Minimum validation for loadable runtime area work:
  - verify VNUMs and boundary links
  - verify `index / mob / obj / res / shp / roo` consistency
  - check `area/directory.lst` ordering
- For area smoke tests:
  - clear or baseline `debug/*` first
  - establish which `log/*` file(s) belong to this run
  - prefer `45` to `60` second timeout windows if using `timeout`
  - do not call the startup successful until you find a clear success signal such as `三國歪傳之降龍伏虎開始正常運作`
  - after success, still inspect `debug/*` and the run log for new area-related warnings/errors

## Build commands

- Preferred `macOS` native validation build:
  - `make -C src clean && make -C src merc`
- Preferred `Windows + WSL (Ubuntu)` local build:
  - `cd src && make clean && make`
- Preferred `macOS + Docker (Ubuntu)` validation build:
  - `docker run --rm -v "$PWD":/workspace/merc-fju-3.0 -w /workspace/merc-fju-3.0 ubuntu:24.04 bash -lc 'apt-get update && apt-get install -y build-essential perl && mkdir -p log player mail debug vote && make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc'`
- Preferred Linux / Codex Cloud build:
  - `make -C src -f Makefile.lin merc`
- Clean rebuild when needed:
  - `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
- Do not treat a Darwin/macOS-native build as proof that Ubuntu is clean; if the task mentions Linux parity, warnings, or container deployment, validate in Ubuntu.
- Current repo baseline expects both the macOS native build and the Ubuntu `Makefile.lin` build to be warning-free; if either side regresses, validate both before closing the task.

## Important build detail

- `src/Makefile.lin` is the Linux build path used in Codex Cloud.
- Non-Darwin builds must link `-lcrypt`.
- The current repository already patches `src/Makefile.lin` to add `LIBS` and pass `$(LIBS)` at link time.
- If a cloud task reports unresolved `crypt`, first verify the checked-out branch still contains that patch before installing extra packages.

## Runtime directories

- Before smoke tests or startup checks, ensure these directories exist:
  - `log`
  - `player`
  - `mail`
  - `debug`
  - `vote`
- Minimal command:
  - `mkdir -p log player mail debug vote`

## Config and startup

- Checked-in template: `src/merc.sample.ini`
- Generated local runtime config: `src/merc.ini`
- Preferred launcher in modern shells:
  - `cd src && ./startup.bash`
- On `Windows + WSL (Ubuntu)`, prefer running `startup.bash` inside WSL or bridge from `startup-wsl.ps1`.
- On `macOS + Docker (Ubuntu)`, prefer Ubuntu container smoke tests with `timeout 45` to `60` seconds and inspect the mounted `log/` + `debug/`.
- Legacy launcher:
  - `cd src && ./startup`
- `src/startup` depends on `csh` / `tcsh`; if unavailable, treat that as a shell dependency issue and use `startup.bash` or direct binary tests.
- If `src/merc.sample.ini` changes, delete `src/merc.ini` before regenerating it.
- In Codex Cloud smoke tests, ensure `HOME DIRECTORY` resolves to `/workspace/merc-fju-3.0`.

## General validation

- For compile-focused tasks, the default validation is:
  - `make -C src -f Makefile.lin merc`
- For warning-cleanup or cross-platform parity tasks, the default validation is both:
  - `make -C src clean && make -C src merc`
  - `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
- For config-related tasks, also inspect:
  - `grep -n "HOME DIRECTORY" src/merc.sample.ini src/merc.ini`
- For startup-related tasks, check the newest file in `log/` and relevant files under `debug/`.

## Network and environment assumptions

- Setup and maintenance scripts have internet access.
- Agent internet access may be disabled unless the environment explicitly enables it.
- Exports made in setup scripts do not automatically persist into the agent phase.

## Scope guidance

- Treat compiler / linker errors as `src/*.c`, `include/*.h`, and `Makefile*` problems first.
- Treat `Load_room`, duplicate VNUM, reset parse failures, and similar messages as world-data issues rather than pure environment issues.
- Do not invent missing wrappers such as `start-merc.sh` or `scripts/bootstrap.sh`; they are not part of this repo.
