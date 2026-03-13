# Merc-FJU 3.0 Source Overview

## Repo Reality Check
- Treat the current workspace as `merc-fju-3.0`, not the older 2.0 ops layout.
- Use `README.md` as the first source for build and startup expectations.
- Do not assume helper wrappers such as `start-merc.sh`, `start-merc.ps1`, `start-merc.cmd`, or `scripts/bootstrap.sh`; they are not present in this repo snapshot.
- Do not cite `docs/DATA_LAYOUT.md` or `docs/RUNTIME_RESET.md`; `docs/` currently contains the `3yWebsite` docs site instead.

## Core Paths
| Path | Purpose |
| --- | --- |
| `src/` | C source files, `Makefile*`, `merc.ini`, legacy `startup` launcher |
| `include/` | Shared headers and declarations |
| `area/` | Area data (`index`, `mob`, `obj`, `roo`, `res`, `shp`, plus some area-specific extras such as `map`) |
| `angel/`, `command/`, `skill/`, `social/` | Gameplay data files loaded by specific subsystems |
| `data/`, `board/`, `etc/` | System data and semi-dynamic files |
| `help/`, `greeting/`, `joke/` | Player-facing text |
| `player/`, `mail/`, `log/`, `debug/`, `vote/` | Runtime-changing directories |
| `document/` | Merc-FJU format manuals and project-specific docs |
| `doc/` | Upstream Merc/Diku license and reference docs |
| `scripts/convert_big5_to_utf8.py` | Encoding conversion / UTF-8 verification helper |

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

## Data Format References
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`

Use these before explaining or changing area-format details.
