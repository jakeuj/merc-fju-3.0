#!/usr/bin/env bash

# Bash-friendly launcher for environments that do not ship csh/tcsh.
# Usage:
#   cd src
#   ./startup.bash [existing-ini]
#
# Without an argument, this script generates merc.ini from merc.sample.ini
# and rewrites HOME DIRECTORY to the current repo root.

set -eu

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
TEMPLATE_INI="${SCRIPT_DIR}/merc.sample.ini"
LOCAL_INI="${SCRIPT_DIR}/merc.ini"
INI_FILE="${1:-${LOCAL_INI}}"
LOG_DIR="${REPO_ROOT}/log"
SLEEP_SECONDS=360
LOG_INDEX=1000

ulimit -s 1024 >/dev/null 2>&1 || true

if [ -f "${SCRIPT_DIR}/shutdown.txt" ]; then
  rm -f "${SCRIPT_DIR}/shutdown.txt"
fi

mkdir -p "${LOG_DIR}"
mkdir -p "${REPO_ROOT}/player"

for header in {a..z} {A..Z}; do
  mkdir -p "${REPO_ROOT}/player/${header}"
done

if [ $# -eq 0 ]; then
  if [ ! -f "${TEMPLATE_INI}" ]; then
    echo "bug: no merc.sample.ini template exists." >&2
    exit 1
  fi

  perl -0pe "s#^HOME DIRECTORY\\s*=\\s*.*#HOME DIRECTORY\\t\\t=\\t${REPO_ROOT}#m" "${TEMPLATE_INI}" \
    > "${LOCAL_INI}"
fi

cd "${SCRIPT_DIR}"

while true; do
  while [ -e "${LOG_DIR}/${LOG_INDEX}.log" ]; do
    LOG_INDEX=$((LOG_INDEX + 1))
  done

  LOG_FILE="${LOG_DIR}/${LOG_INDEX}.log"

  if [ ! -e "${SCRIPT_DIR}/merc" ]; then
    echo "bug: no merc exists." >>"${LOG_FILE}" 2>&1
    exit 0
  fi

  "${SCRIPT_DIR}/merc" "${INI_FILE}" >>"${LOG_FILE}" 2>&1

  if [ -e "${SCRIPT_DIR}/shutdown.txt" ]; then
    rm -f "${SCRIPT_DIR}/shutdown.txt"
    exit 0
  fi

  sleep "${SLEEP_SECONDS}"
done
