#!/bin/bash
# Serve docs/ at http://localhost:8000 (with /api/embed Gemini proxy) and open the root site.
# If port 8000 is already in use (another open*.command is running) just open the URL.
SUBPATH=""
cd "$(dirname "$0")" || exit 1
if ! lsof -nP -iTCP:8000 -sTCP:LISTEN >/dev/null 2>&1; then
  python3 pipeline/serve_local.py --port 8000 &
  SERVER_PID=$!
  sleep 1
fi
open "http://localhost:8000/${SUBPATH}"
if [ -n "${SERVER_PID:-}" ]; then
  wait "$SERVER_PID"
fi
