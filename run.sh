#!/usr/bin/env bash

cd "$(dirname "$0")"
python3 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e ./

export HOST_NAME=0.0.0.0
export HOST_PORT=11103
python3 -m test_flask