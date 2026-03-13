#!/usr/bin/env bash

# Bash-friendly launcher for environments that do not ship csh/tcsh.
# Usage:
#   cd src
#   ./startup.bash [merc.ini]

set -u

INI_FILE="${1:-merc.ini}"
LOG_DIR="../log"
SLEEP_SECONDS=360
LOG_INDEX=1000

ulimit -s 1024 >/dev/null 2>&1 || true

if [ -f shutdown.txt ]; then
  rm -f shutdown.txt
fi

mkdir -p "${LOG_DIR}"

while true; do
  while [ -e "${LOG_DIR}/${LOG_INDEX}.log" ]; do
    LOG_INDEX=$((LOG_INDEX + 1))
  done

  LOG_FILE="${LOG_DIR}/${LOG_INDEX}.log"

  if [ ! -e ../src/merc ]; then
    echo "bug: no merc exists." >>"${LOG_FILE}" 2>&1
    exit 0
  fi

  ../src/merc "${INI_FILE}" >>"${LOG_FILE}" 2>&1

  if [ -e shutdown.txt ]; then
    rm -f shutdown.txt
    exit 0
  fi

  sleep "${SLEEP_SECONDS}"
done
