#!/bin/bash
set -euo pipefail

# Render sets PORT. Default to 10000 for local use.
PORT="${PORT:-10000}"

# Install the package in editable mode
pip install -e .

exec libretranslate --host 0.0.0.0 --port $PORT
