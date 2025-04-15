#!/bin/bash


source /opt/venv/vin/activate

cd /app

RUN_PORT=${RUN_PORT:-8002}
RUN_HOST=${HOST:-0.0.0.0}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app 