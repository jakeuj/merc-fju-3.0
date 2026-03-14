# AGENTS.md

This repository is a Merc MUD codebase with legacy build paths plus modern local and cloud workflows. Follow these rules during Codex Cloud tasks.

## Task flow

- Expect Codex Cloud to create a container, check out the selected branch or commit, run the environment setup script, then start the agent phase.
- If the environment resumes from cache, expect the maintenance script to run instead of the full setup script.
- Assume the repository root in Codex Cloud is `/workspace/merc-fju-3.0`.
- Use this file to decide build and validation commands before guessing.

## Build commands

- Preferred Linux / Codex Cloud build:
  - `make -C src -f Makefile.lin merc`
- Clean rebuild when needed:
  - `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
- Local macOS / general repo build alternative:
  - `make -C src clean && make -C src`

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
- Legacy launcher:
  - `cd src && ./startup`
- `src/startup` depends on `csh` / `tcsh`; if unavailable, treat that as a shell dependency issue and use `startup.bash` or direct binary tests.
- If `src/merc.sample.ini` changes, delete `src/merc.ini` before regenerating it.
- In Codex Cloud smoke tests, ensure `HOME DIRECTORY` resolves to `/workspace/merc-fju-3.0`.

## Validation

- For compile-focused tasks, the default validation is:
  - `make -C src -f Makefile.lin merc`
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
