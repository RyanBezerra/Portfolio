#!/bin/bash
set -x  # Ativa o modo de depuração
echo "Building the project..."
python3.12 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Error occurred while installing requirements."
  exit 1
fi
echo "Collect Static..."
python3.12 manage.py collectstatic --noinput --clear
if [ $? -ne 0 ]; then
  echo "Error occurred while collecting static files."
  exit 1
fi
