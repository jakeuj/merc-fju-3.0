# Merc-FJU 3.0 Source Overview

## Repo Reality Check
- Treat the current workspace as `merc-fju-3.0`, not the older 2.0 ops layout.
- Use `README.md` as the first source for build and startup expectations.
- Do not assume helper wrappers such as `start-merc.sh`, `start-merc.ps1`, `start-merc.cmd`, or `scripts/bootstrap.sh`; they are not present in this repo snapshot.
- Do not cite `docs/DATA_LAYOUT.md` or `docs/RUNTIME_RESET.md`; `docs/` currently contains the `3yWebsite` docs site instead.
- `docs/current-game/` now also contains hand-maintained runtime docs for `.ski` / `pry` behavior and Pages versions of the legacy `document/` manuals; use those as the first documentation layer for skill-format questions, then verify against `src/load.c`, `src/act_info.c`, `src/bit.c`, `src/class.c`, and `src/merc.h`.

## Core Paths
| Path | Purpose |
| --- | --- |
| `src/` | C source files, `Makefile*`, `merc.ini`, legacy `startup` launcher |
| `include/` | Shared headers and declarations |
| `area/` | Area data (`index`, `mob`, `obj`, `roo`, `res`, `shp`, plus some area-specific extras such as `map`) |
| `angel/`, `command/`, `skill/`, `social/` | Gameplay data files loaded by specific subsystems |
| `data/`, `board/`, `etc/` | System data and semi-dynamic files |
| `help/`, `greeting/`, `joke/` | Player-facing text |
| `docs/current-game/` | Current-game docs site, including `.ski` field, loader, constants, and `pry` crosswalk pages |
| `player/`, `mail/`, `log/`, `debug/`, `vote/` | Runtime-changing directories |
| `document/` | Merc-FJU format manuals and project-specific docs |
| `doc/` | Upstream Merc/Diku license and reference docs |
| `scripts/convert_big5_to_utf8.py` | Encoding conversion / UTF-8 verification helper |

## Legacy `document/README` Tree Crosswalk
- `document/README` describes an older release-package view of the project.
- That view is still useful for orientation, but it should be translated into the current repo before you explain load flow or editing entry points.

### Legacy package tree -> today repo
- legacy `src/` -> today `src/`, still the code, build files, and startup scripts
- legacy `area/` -> today `area/`, still world-data storage, but modern area work also layers `map.md`, plans, and tracker files on top
- legacy `data/` -> today `data/`, still semi-static game/system data
- legacy `document/` -> today `document/`, still the original format manuals; fast reading entry points now also exist under `docs/current-game/`
- legacy runtime dirs like `player/`, `mail/`, `log/`, `debug/` -> still runtime-changing directories in the current repo

### Area package note
The legacy README's explanation of `index / mob / obj / res / roo / shp` is still directionally correct, but detailed area authoring belongs to `merc-area-builder`, not this explainer skill.

### Ops note
The legacy README's `make clean; make`, `startup &`, and `merc.ini` guidance should be mapped to `README.md`, `src/startup.bash`, `src/merc.sample.ini`, and `merc-local-ops`, not repeated as if they were today-only truths.

## Build and Startup
```bash
cd src
make clean && make
```

- For FreeBSD, copy `Makefile.bsd` to `Makefile` first.
- The repo README documents startup through:

```bash
cd src
./startup &
```

- When explaining startup issues, distinguish:
  - compile problems in `src/`
  - launcher behavior in `src/startup`
  - runtime data-load errors from `area/`, `data/`, `help/`, or related directories

## Config Notes
- `src/merc.ini` is the checked-in config file to inspect first.
- `etc/` exists and contains runtime/semi-dynamic files, but this repo snapshot does not include `etc/merc.ini`.
- Important config families:
  - identity and ports: `NAME`, `MUD PORT`, `HOME DIRECTORY`
  - file layout: `HELP DIRECTORY`, `SOCIAL DIRECTORY`, `ANGEL DIRECTORY`, `AREA DIRECTORY`, `PLAYER DIRECTORY`
  - gameplay toggles: `Player Angel`, `Attack Value`, `Skill Value`
  - operational policy: `Strict Password`, `Strict Email`, `Multi login`, `Check Server`

## Common Code Entry Points
- `ini.c`: config parsing and related file-path behavior
- `db.c`, `load.c`, `reload.c`: world/data loading and reload paths
- `interp.c`, `act_*.c`: command dispatch and player-facing actions
- `fight.c`, `magic.c`, `skill.c`, `spell.c`: combat and skills
- `job.c`, `variable.c`, `system.c`: global game rules and fixed behaviors
- `file.c`, `save.c`: persistence and file I/O

## Command vs Job Dispatch
- `interp.c` first resolves normal commands from the command table and dispatches to `do_*` handlers.
- After that, it can also dispatch room, mob, or object `job` handlers by matching the player's typed command against loaded `job->keyword`.
- `act_move.c`, `act_obj.c`, and `act_info.c` are common homes for built-in verbs such as movement, object actions, and look/info commands.
- `job.c` is the lookup/registration point for named job functions that area or data files can bind through `#Job`.
- Important implication: `#Keyword` in a room description is only descriptive text for `look`/`examine`; it does not create a usable command by itself.
- Current repo example: `area/newfight/roo/1211.roo` hints at `bore hole`, but there is no `do_bore` in the checked-in source, and `job.c` currently exposes only a small set of job functions. So text can imply an interaction that is not currently implemented.

## Data Format References
- `docs/current-game/legacy-documentation.md`
- `docs/current-game/legacy-readme.md`
- `docs/current-game/mobile-file-format.md`
- `docs/current-game/object-file-format.md`
- Current object-loader pitfall: area `obj/*.obj` uses loader fields such as `Name / ShortDesc / Description / Takeable / WearLoc / Value*`; do not explain or scaffold them with runtime/save-style names like `Keywords / ExtraFlags / WearFlags`.
- `docs/current-game/room-file-format.md`
- `docs/current-game/reset-file-format.md`
- Current reset-loader pitfall: legacy docs mention `S` as a terminator, but the checked-in `src/load.c` `load_resets()` reads until EOF; a literal `S` line can break parsing in this repo snapshot.
- `docs/current-game/shop-file-format.md`
- `docs/current-game/title-file-format.md`
- `docs/current-game/copyright-notice.md`
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`

## Skill Docs References
- `docs/current-game/skill-file-format.md`
- `docs/current-game/skill-loader-reference.md`
- `docs/current-game/skill-constants.md`
- `docs/current-game/skill-pry-crosswalk.md`

Use these before explaining or changing area-format details.
