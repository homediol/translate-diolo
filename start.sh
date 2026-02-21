#!/bin/bash
set -euo pipefail

# Render sets PORT. Default to 10000 for local use.
PORT="${PORT:-10000}"

exec libretranslate --host 0.0.0.0 --port $PORT
