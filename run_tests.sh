#!/usr/bin/bash

set -e
set -o pipefail

source venv/bin/activate

pytest -v --headless
EXIT_CODE=$?

deactivate

if [ $EXIT_CODE -eq 0 ]; then
  echo "All tests successful"
  exit 0
else
  echo "Tests failed"
  exit 1
fi
