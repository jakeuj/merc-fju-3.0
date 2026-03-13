# Merc Local Ops Cheatsheet

## Repo Reality Check
- Use the current `merc-fju-3.0` workspace, not older wrapper-based flows.
- Do not assume `start-merc.sh`, `start-merc.ps1`, `start-merc.cmd`, or `scripts/bootstrap.sh`; they are not present in this repo snapshot.
- Primary checked-in config: `src/merc.ini`
- Primary startup entry: `src/startup`

## Build
```bash
cd src
make clean && make
```

PowerShell -> probe local toolchain first:
```powershell
Get-Command make, gcc, wsl -ErrorAction SilentlyContinue
```

If PowerShell has no `make` but `wsl.exe` exists, check the WSL toolchain:
```powershell
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && command -v make && command -v gcc'
```

If that succeeds, build inside WSL:
```powershell
wsl.exe bash -lc 'cd /mnt/h/repos/merc-fju-3.0/src && make clean && make'
```

Path rule:
- `H:\repos\merc-fju-3.0` -> `/mnt/h/repos/merc-fju-3.0`
- keep build and startup in the same environment when possible

FreeBSD:
```bash
cd src
cp Makefile.bsd Makefile
make clean && make
```

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

What `startup` does:
- clears `shutdown.txt` if present
- chooses the next free `../log/<number>.log`
- runs `../src/merc merc.ini`
- loops again after 360 seconds unless `shutdown.txt` exists

## Basic Checks
Check binary and config:
```bash
ls -l src/merc
grep -n "HOME DIRECTORY" src/merc.ini
grep -n "MUD PORT" src/merc.ini
```

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

Smoke test without `startup`:
```bash
cd /mnt/h/repos/merc-fju-3.0
mkdir -p log player
perl -0pe 's#^HOME DIRECTORY\s*=\s*.*#HOME DIRECTORY\t\t=\t/mnt/h/repos/merc-fju-3.0#m' src/merc.ini > src/merc.test.ini
cd src
timeout 8s ./merc merc.test.ini > ../log/merc-startup-smoke.log 2>&1
tail -n 80 ../log/merc-startup-smoke.log
```

Use this to separate:
- `startup` shell problems
- wrong `HOME DIRECTORY`
- real world-data load failures

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

Check:
```bash
grep -n "HOME DIRECTORY" src/merc.ini
pwd
```

Fix:
- edit `src/merc.ini` so `HOME DIRECTORY` matches the actual repo path used at runtime
- for one-off verification, generate a temporary `src/merc.test.ini` instead of immediately rewriting the checked-in file

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
