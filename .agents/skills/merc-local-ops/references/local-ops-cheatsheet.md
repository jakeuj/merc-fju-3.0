# Merc Local Ops Cheatsheet

## Repo Reality Check
- Use the current `merc-fju-3.0` workspace, not older wrapper-based flows.
- Do not assume `start-merc.sh`, `start-merc.ps1`, `start-merc.cmd`, or `scripts/bootstrap.sh`; they are not present in this repo snapshot.
- Primary checked-in config template: `src/merc.sample.ini`
- Primary startup entry: `src/startup`

## Build
Preferred environments:
- `Windows + WSL (Ubuntu)`: build and run inside WSL
- `macOS + Docker (Ubuntu)`: build and smoke test inside Ubuntu containers

Do not treat a macOS-native build as proof that Ubuntu is also clean.

### Windows + WSL (Ubuntu)
Probe from PowerShell:
```powershell
Get-Command make, gcc, wsl -ErrorAction SilentlyContinue
```

Check the WSL toolchain:
```powershell
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && command -v make && command -v gcc'
```

Build inside WSL:
```powershell
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make clean && make'
```

### macOS + Docker (Ubuntu)
Build inside Ubuntu:
```bash
docker run --rm -v "$PWD":/workspace/merc-fju-3.0 -w /workspace/merc-fju-3.0 \
  ubuntu:24.04 bash -lc '
    apt-get update &&
    apt-get install -y build-essential perl &&
    mkdir -p log player mail debug vote &&
    make -C src -f Makefile.lin clean &&
    make -C src -f Makefile.lin merc
  '
```

This is the preferred Linux validation path when the host is macOS.

### Other Linux / Ubuntu
```bash
cd src
make clean && make
```

For explicit Linux build path:
```bash
make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc
```

Why:
- `src/Makefile.lin` is the Linux build path that Codex Cloud containers will typically use
- this repo now expects `Makefile.lin` to carry `-lcrypt` on non-Darwin platforms
- if `make -C src -f Makefile.lin` still fails on `crypt`, verify the workspace contains the patched `src/Makefile.lin` before adding packages

Path rule:
- `H:\repos\merc-fju-3.0` -> `/mnt/h/repos/merc-fju-3.0`
- keep build and startup in the same environment when possible

FreeBSD:
```bash
cd src
cp Makefile.bsd Makefile
make clean && make
```

Notes:
- on macOS, prefer Ubuntu Docker tests when you want Linux parity
- if mac build is clean but Docker Ubuntu warns, trust the Docker result for Linux compatibility

## Startup
From `src/`:
```bash
./startup &
```

Important:
- `src/startup` uses `csh -f`, not `bash`
- on WSL, check `command -v csh || command -v tcsh` before assuming startup is usable
- if `csh` is missing, treat that as a shell dependency issue, not as proof that `merc` itself is broken

WSL / bash-friendly launcher:
```bash
cd src
./startup.bash &
```

Docker Ubuntu smoke test from macOS host:
```bash
docker run --rm -v "$PWD":/workspace/merc-fju-3.0 -w /workspace/merc-fju-3.0 \
  ubuntu:24.04 bash -lc '
    apt-get update &&
    apt-get install -y build-essential perl &&
    mkdir -p log player mail debug vote &&
    make -C src -f Makefile.lin merc &&
    rm -f debug/* &&
    timeout 60s bash -lc "cd src && ./startup.bash"
  '
```

Then inspect the newest `log/*.log` on the mounted workspace and look for:
- `三國歪傳之降龍伏虎開始正常運作.`
- any newly-created `debug/*` files

Default behavior:
- generates `src/merc.ini` from `src/merc.sample.ini`
- rewrites `HOME DIRECTORY` to the current repo root
- keeps the checked-in template ini untouched
- if `src/merc.sample.ini` was fixed after an earlier bad generation, delete `src/merc.ini` first so startup regenerates it from the repaired template

`src/startup` should now follow the same generated-ini pattern when `csh` is available.

What `startup` does:
- clears `shutdown.txt` if present
- chooses the next free `../log/<number>.log`
- runs `../src/merc merc.ini`
- loops again after 360 seconds unless `shutdown.txt` exists

## Basic Checks
Check binary and config:
```bash
ls -l src/merc
grep -n "HOME DIRECTORY" src/merc.sample.ini
grep -n "MUD PORT" src/merc.sample.ini
```

Container workspace path:
- in Docker Ubuntu examples, use `/workspace/merc-fju-3.0`
- ensure generated `src/merc.ini` points `HOME DIRECTORY` there when the process runs inside the container

If startup still behaves like the old broken config after fixing `src/merc.sample.ini`:
```bash
rm -f src/merc.ini
cd src
./startup.bash
```

INI selection behavior:
- `./merc some.ini` -> use the explicit ini file
- `./merc` -> use env var `merc` if set, otherwise fallback to `merc.ini`
- for local multi-machine work, prefer `./startup.bash` first so `merc.ini` is generated correctly

Check runtime directories:
```bash
ls -ld log player mail debug vote
test -w log && echo log:writable || echo log:not-writable
test -w player && echo player:writable || echo player:not-writable
```

If `log/` or `player/` is missing:
```bash
mkdir -p log player
```

Check recent logs:
```bash
ls -t log | head
tail -n 80 log/1000.log
```

Interpret startup success from the latest log first:
- `三國歪傳之降龍伏虎開始正常運作.` means the server reached normal runtime
- `Broken pipe` or `write_to_descriptor: 寫入錯誤` right after a manual probe often just means the test client disconnected
- `debug/bugs` may still contain older startup failures and should not outweigh a newer successful `log/*.log`

Check for tracked runtime noise after tests:
```bash
git status --short
```

Common tracked files that may change during local startup checks:
- `debug/error`
- `etc/net.log`
- `etc/stock`

If those changes are only test side effects and not part of the task:
```bash
git checkout -- debug/error etc/net.log etc/stock
```

If you want to keep local runtime noise out of `git status` without changing repo rules:
```bash
git update-index --skip-worktree \
  debug/error \
  debug/failenable \
  etc/address \
  etc/net.log \
  etc/stock \
  data/immlist \
  etc/database \
  etc/player.new \
  etc/wizard.log
```

Check current local skip list:
```bash
git ls-files -v | rg '^S '
```

Undo for one file when you really need to edit and commit it:
```bash
git update-index --no-skip-worktree etc/net.log
```

For untracked local-only noise such as `src/shutdown.txt`, prefer `.git/info/exclude`:
```bash
printf '\nsrc/shutdown.txt\n' >> .git/info/exclude
```

Smoke test without `startup`:
```bash
cd /mnt/h/repos/merc-fju-3.0
mkdir -p log player
cp src/merc.sample.ini src/merc.ini
perl -0pi -e 's#^HOME DIRECTORY\s*=\s*.*#HOME DIRECTORY\t\t=\t/mnt/h/repos/merc-fju-3.0#m' src/merc.ini
cp src/merc.ini src/merc.test.ini
cd src
timeout 8s ./merc merc.test.ini > ../log/merc-startup-smoke.log 2>&1
tail -n 80 ../log/merc-startup-smoke.log
```

Use this to separate:
- `startup` shell problems
- wrong `HOME DIRECTORY`
- real world-data load failures
- tracked runtime file noise that should not be committed

## Common Failures

### `merc` binary missing
Meaning:
- `src/startup` cannot find `../src/merc`

Fix:
```bash
cd src
make clean && make
```

If PowerShell cannot run `make`:
```powershell
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make clean && make'
```

### PowerShell says `make` is not recognized
Meaning:
- the current shell is not the actual build environment
- this does not yet prove the repo is unbuildable

Check:
```powershell
Get-Command make, gcc, wsl -ErrorAction SilentlyContinue
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && command -v make && command -v gcc'
```

Interpretation:
- if WSL has `make` and `gcc`, switch to WSL-backed build commands
- only treat it as missing toolchain if both PowerShell and WSL lack them

### Wrong `HOME DIRECTORY`
Meaning:
- `merc.ini` still points at an old machine path
- on Codex Cloud, it may still point at a macOS / WSL path instead of `/workspace/merc-fju-3.0`

Check:
```bash
grep -n "HOME DIRECTORY" src/merc.ini
pwd
```

Fix:
- edit `src/merc.ini` so `HOME DIRECTORY` matches the actual repo path used at runtime
- for one-off verification, generate a temporary `src/merc.test.ini` instead of immediately rewriting the checked-in file
- if the template was just repaired, deleting `src/merc.ini` and rerunning startup is usually safer than hand-editing a stale generated file

### `generate_ticket: 沒有中獎的資料.`
Meaning:
- the ini was parsed without any `Ticket Set = ...` entries
- this is an ini/template completeness issue, not proof that a separate ticket data file is missing

Check:
```bash
grep -n "Ticket Set" src/merc.sample.ini
grep -n "Ticket Set" src/merc.ini
```

Fix:
- restore the missing `Ticket Set` lines in `src/merc.sample.ini`
- delete stale `src/merc.ini`
- rerun `./startup.bash` so the regenerated `merc.ini` includes the repaired ticket configuration

### `startup` exists but `csh` is missing
Meaning:
- the launcher script is present
- the current WSL/Linux environment lacks its required shell

Check:
```bash
cd /mnt/h/repos/merc-fju-3.0/src
command -v csh || command -v tcsh
head -n 5 startup
```

Interpretation:
- if no `csh` / `tcsh` is installed, `startup` cannot be the immediate test path
- fall back to direct `./merc <temp-ini>` smoke testing first

### Immediate exit because of `shutdown.txt`
Check:
```bash
ls src/shutdown.txt
```

Fix:
```bash
rm -f src/shutdown.txt
cd src
./startup &
```

### Runtime directory not writable
Meaning:
- startup can launch, but the game cannot create or update runtime files

Check:
```bash
ls -ld log player mail debug vote board etc data
test -w log && echo ok || echo fail
```

Fix:
- repair ownership or permissions for the blocked directory
- verify with `test -w <dir>` before retrying

### Tracked runtime files changed after startup tests
Meaning:
- the repo contains some checked-in runtime-ish files
- local smoke tests touched them, but that does not automatically mean they belong in the commit

Check:
```bash
git status --short
```

Typical examples:
- `debug/error`
- `etc/net.log`
- `etc/stock`

Fix:
- if the task was only build/startup verification, reset those files before committing
- if the task intentionally changed runtime defaults or seed data, review them like normal source changes

### Startup log shows data-load failure
Examples:
- `Load_room`
- duplicate VNUM
- malformed mob/obj/room/reset data

Interpretation:
- local ops is no longer the primary problem
- switch to area/data debugging and inspect the first real parser/load error in the log

Check:
```bash
ls -t log | head
tail -n 120 log/1000.log
```

## Triage Order
1. Confirm `src/merc` exists
2. Confirm `src/merc.ini` paths are sane
3. Confirm runtime directories are writable
4. Remove stale `shutdown.txt`
5. Start with `src/startup`
6. Read the newest `log/*.log`
7. If logs show world-data errors, stop blaming local ops and fix the data
## Windows + WSL 啟動

- 若 CLion / PowerShell 難以直接把 `src/startup.bash` 當 shell script 跑，優先使用 repo 根目錄的 `startup-wsl.ps1`
- `startup-wsl.ps1` 應以自己的所在位置推導 repo 根目錄，再用 `wsl.exe wslpath -a` 轉成 WSL 路徑
- PowerShell wrapper 只負責進入 WSL 並呼叫 `src/startup.bash`；不要在 wrapper 內重複實作 `merc.ini` 生成與 log loop
- 若 wrapper 失敗，先檢查：
- `Get-Command wsl.exe`
- `wsl.exe bash -lc 'command -v wslpath && command -v bash'`
