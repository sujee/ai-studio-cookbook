#!/usr/bin/env bash
set -euo pipefail

# Minimal bootstrap runner for the UDR app with Nebius
# Requires NEBIUS_API_KEY in the environment

if [ -z "${NEBIUS_API_KEY:-}" ]; then
  echo "NEBIUS_API_KEY is not set. export NEBIUS_API_KEY=..." >&2
  exit 1
fi

WORKDIR=${WORKDIR:-$(pwd)}
APP_DIR="$WORKDIR/udr-nebius"

if [ ! -d "$APP_DIR" ]; then
  git clone https://github.com/demianarc/nebiusaistudiodeepresearch "$APP_DIR"
fi

# Backend
cd "$APP_DIR/backend"
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp -f env.example .env || true
# ensure required settings
sed -i '' 's#^DEFAULT_MODEL=.*#DEFAULT_MODEL=nebius-kimi-k2#' .env || true
sed -i '' 's#^FRONTEND_URL=.*#FRONTEND_URL=http://localhost:3004#' .env || true
# inject the key (no quotes)
if ! grep -q '^NEBIUS_API_KEY=' .env; then echo "NEBIUS_API_KEY=$NEBIUS_API_KEY" >> .env; fi
./launch_server.sh >/dev/null 2>&1 &

# Frontend
cd "$APP_DIR/frontend"
[ -f .env.local ] || cp env.example .env.local
sed -i '' 's#^NEXT_PUBLIC_BACKEND_BASE_URL=.*#NEXT_PUBLIC_BACKEND_BASE_URL=http://localhost#' .env.local
sed -i '' 's#^NEXT_PUBLIC_BACKEND_PORT=.*#NEXT_PUBLIC_BACKEND_PORT=8000#' .env.local
sed -i '' 's#^NEXT_PUBLIC_API_VERSION=.*#NEXT_PUBLIC_API_VERSION=v1#' .env.local
sed -i '' 's#^NEXT_PUBLIC_ENABLE_V2_API=.*#NEXT_PUBLIC_ENABLE_V2_API=false#' .env.local
sed -i '' 's#^NEXT_PUBLIC_DRY_RUN=.*#NEXT_PUBLIC_DRY_RUN=false#' .env.local
npm install --silent
npm run dev -- -p 3004
