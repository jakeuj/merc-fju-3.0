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

Check recent logs:
```bash
ls -t log | head
tail -n 80 log/1000.log
```

## Common Failures

### `merc` binary missing
Meaning:
- `src/startup` cannot find `../src/merc`

Fix:
```bash
cd src
make clean && make
```

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
