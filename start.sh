#!/usr/bin/env bash
set -e

if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

mkdir -p data/raw_html data/cache

python -c "
from db.base import Base
from db.session import engine
Base.metadata.create_all(bind=engine)
print('DB ready')
"

exec gunicorn api.main:app \
  --workers \ \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind \:\ \
  --timeout 120 \
  --keep-alive 5 \
  --access-logfile - \
  --error-logfile -
