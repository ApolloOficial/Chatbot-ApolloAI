#!/bin/sh
set -eu
PROMETHEUS_MULTIPROC_DIR="$(mktemp -d /tmp/apolloai-metrics.XXXXXX)"
export PROMETHEUS_MULTIPROC_DIR
exec gunicorn --config gunicorn.conf.py --bind 0.0.0.0:5000 --workers 2 --timeout 90 wsgi:app
